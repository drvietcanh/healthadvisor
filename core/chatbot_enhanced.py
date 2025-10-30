"""
Enhanced Chatbot - Hỗ trợ cả OpenAI và Gemini API
"""
import streamlit as st
from typing import List, Dict, Optional
import os

# Import AI libraries
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False


class MedicalChatbot:
    """Chatbot y tế thông minh với câu hỏi gợi ý"""
    
    def __init__(self):
        self.conversation = []
        
    def get_welcome_message(self) -> str:
        """Lời chào và giới thiệu"""
        return """
👋 **Xin chào! Tôi là Bác sĩ AI - Trợ lý sức khỏe của bạn.**

Tôi có thể giúp bạn:
- ✅ Giải thích về bệnh (huyết áp, tiểu đường, đột quỵ...)
- ✅ Tư vấn chế độ ăn uống
- ✅ Hướng dẫn dùng thuốc (không kê đơn)
- ✅ Trả lời thắc mắc về triệu chứng

**Bạn muốn hỏi gì? Chọn bên dưới hoặc gõ câu hỏi nhé!** 😊
"""
    
    def get_suggested_questions(self, context: str = "general") -> List[str]:
        """Câu hỏi gợi ý theo ngữ cảnh"""
        
        suggestions = {
            "general": [
                "Huyết áp bao nhiêu là bình thường?",
                "Dấu hiệu đột quỵ là gì?",
                "Đường huyết cao phải làm sao?",
                "Ăn gì để giảm huyết áp?",
                "Khi nào cần gọi cấp cứu 115?"
            ],
            "hypertension": [
                "Thuốc huyết áp có tác dụng phụ gì?",
                "Ăn bao nhiêu muối mỗi ngày?",
                "Có được bỏ thuốc khi huyết áp đã bình thường?",
                "Vận động thế nào an toàn?",
                "Đo huyết áp đúng cách ra sao?"
            ],
            "diabetes": [
                "Đường huyết 7.5 mmol/L có cao không?",
                "Insulin tiêm vào đâu?",
                "Hạ đường huyết xử trí thế nào?",
                "Ăn carb là ăn gì?",
                "Có cần kiêng trái cây không?"
            ],
            "stroke": [
                "BE-FAST là gì?",
                "Đột quỵ phải làm gì ngay?",
                "Phòng ngừa đột quỵ như thế nào?",
                "Thời gian vàng là bao lâu?",
                "Đột quỵ có khỏi hẳn không?"
            ],
            "nutrition": [
                "Thực đơn cho người huyết áp cao?",
                "Món nào ít muối?",
                "Cách tính carb trong bữa ăn?",
                "Ăn gì tốt cho tim?",
                "Trái cây nào tốt cho tiểu đường?"
            ],
            "medication": [
                "Thuốc uống lúc nào?",
                "Quên uống thuốc thì sao?",
                "Tác dụng phụ thuốc là gì?",
                "Có được uống thuốc cùng lúc?",
                "Khi nào báo bác sĩ về thuốc?"
            ]
        }
        
        return suggestions.get(context, suggestions["general"])
    
    def detect_context(self, message: str) -> str:
        """Phát hiện ngữ cảnh từ câu hỏi"""
        message_lower = message.lower()
        
        if any(word in message_lower for word in ["huyết áp", "cao huyết áp", "tăng huyết áp", "blood pressure"]):
            return "hypertension"
        elif any(word in message_lower for word in ["tiểu đường", "đường huyết", "insulin", "diabetes"]):
            return "diabetes"
        elif any(word in message_lower for word in ["đột quỵ", "stroke", "be-fast", "liệt"]):
            return "stroke"
        elif any(word in message_lower for word in ["ăn", "thức ăn", "món", "thực đơn", "dinh dưỡng"]):
            return "nutrition"
        elif any(word in message_lower for word in ["thuốc", "uống thuốc", "liều", "medication"]):
            return "medication"
        else:
            return "general"
    
    def get_quick_answers(self, question_type: str) -> str:
        """Câu trả lời nhanh cho câu hỏi phổ biến"""
        
        answers = {
            "huyết áp bình thường": """
📊 **Huyết áp bình thường:**

**< 120/80 mmHg** = ✅ Bình thường tuyệt vời!
**120-129/<80** = ⚠️ Hơi cao (cần thay đổi lối sống)
**130-139/80-89** = 🔴 Tăng huyết áp độ 1
**≥ 140/90** = 🚨 Tăng huyết áp độ 2

**Ví dụ dễ hiểu:**
- 115/75 = Hoàn hảo! 🎉
- 125/78 = OK nhưng cẩn thận
- 145/95 = Cần điều trị
""",
            "dấu hiệu đột quỵ": """
🚨 **Dấu hiệu đột quỵ - Nhớ BE-FAST:**

**B** = **B**alance - Mất thăng bằng
**E** = **E**yes - Nhìn mờ, nhìn đôi  
**F** = **F**ace - Xệ mặt, méo miệng
**A** = **A**rm - Yếu tay/chân (1 bên)
**S** = **S**peech - Nói khó, nói lắp
**T** = **T**ime - GỌI 115 NGAY!

**Test nhanh 10 giây:**
1. CƯỜI → Lệch miệng? ❌
2. GIƠ 2 TAY → 1 tay sa? ❌
3. NÓI 1 CÂU → Khó nói? ❌

→ CÓ 1 dấu hiệu = GỌI 115 NGAY!
⏰ Mỗi phút = 2 triệu tế bào não chết!
""",
            "đường cao": """
🍬 **Đường huyết cao - Làm gì ngay:**

**Nếu > 13 mmol/L (>250 mg/dL):**
1. ✅ Uống nhiều nước
2. ✅ Đo tiếp sau 2 giờ
3. ⚠️ Nếu vẫn cao → Gọi bác sĩ
4. 🚨 Nếu buồn nôn, đau bụng → GỌI 115

**Nếu 7-13 mmol/L (126-250):**
1. ✅ Vận động nhẹ 15 phút
2. ✅ Ăn ít carb bữa sau
3. ✅ Uống thuốc đúng giờ
4. 📝 Ghi lại để báo bác sĩ

**Phòng ngừa:**
- Ăn đúng giờ
- Đo đường thường xuyên
- Uống thuốc đủ liều
""",
            "ăn giảm huyết áp": """
🥗 **Ăn gì để giảm huyết áp:**

**✅ NÊN ĂN:**
- 🥬 Rau xanh (cải, rau ngót, rau muống)
- 🍌 Chuối (giàu kali - hạ huyết áp)
- 🥛 Sữa ít béo
- 🐟 Cá (omega-3 rất tốt)
- 🥔 Khoai lang luộc
- 🍊 Cam, quýt (vitamin C)

**🚫 TRÁNH:**
- Đồ MẶN (muối, mắm, tương)
- Đồ CHIÊN RÁN
- Đồ HỘP/ĐÓNG GÓI
- Rượu, bia

**Mẹo:**
Thay muối = Chanh + Gừng + Tỏi + Rau thơm
→ Vừa ngon vừa khỏe!
""",
            "gọi 115": """
🚨 **Khi nào GỌI CẤP CỨU 115:**

**TIM MẠCH:**
⛔ Đau ngực dữ dội
⛔ Khó thở nghiêm trọng
⛔ Huyết áp > 180/120

**THẦN KINH:**
⛔ Yếu liệt đột ngột
⛔ Méo mặt, nói khó
⛔ Đau đầu dữ dội

**TIỂU ĐƯỜNG:**
⛔ Đường > 22 mmol/L (400 mg/dL)
⛔ Hôn mê, co giật
⛔ Buồn nôn nhiều + đau bụng

**KHÁC:**
⛔ Ngất xỉu
⛔ Chảy máu không cầm được
⛔ Bất kỳ tình trạng NGHIÊM TRỌNG đột ngột

**⏰ ĐỪNG TRÌ HOÃN - Gọi ngay!**
Tốt hơn GỌI NHẦM còn hơn BỎ LỠ!
"""
        }
        
        return answers.get(question_type, "")
    
    def generate_response(self, user_message: str, use_ai: bool = True, provider: str = "gemini", api_key: Optional[str] = None) -> tuple:
        """
        Tạo phản hồi cho câu hỏi
        
        Args:
            user_message: Câu hỏi của người dùng
            use_ai: Có dùng AI không
            provider: "gemini" hoặc "openai"
            api_key: API key (optional)
            
        Returns: (response_text, new_context, suggested_questions)
        """
        
        # Phát hiện ngữ cảnh
        context = self.detect_context(user_message)
        
        # Kiểm tra câu hỏi phổ biến
        user_lower = user_message.lower()
        
        quick_answer_map = {
            "huyết áp bình thường": ["huyết áp", "bình thường"],
            "dấu hiệu đột quỵ": ["dấu hiệu", "đột quỵ"],
            "đường cao": ["đường", "cao"],
            "ăn giảm huyết áp": ["ăn", "giảm", "huyết áp"],
            "gọi 115": ["gọi", "115", "cấp cứu"]
        }
        
        # Tìm câu trả lời nhanh
        for answer_key, keywords in quick_answer_map.items():
            if all(kw in user_lower for kw in keywords):
                response = self.get_quick_answers(answer_key)
                if response:
                    suggestions = self.get_suggested_questions(context)
                    return response, context, suggestions
        
        # Nếu không có câu trả lời nhanh, dùng AI hoặc template
        if use_ai:
            response = self._get_ai_response(user_message, context, provider=provider, api_key=api_key)
        else:
            response = self._get_template_response(user_message, context)
        
        suggestions = self.get_suggested_questions(context)
        return response, context, suggestions
    
    def _get_ai_response(self, message: str, context: str, provider: str = "gemini", api_key: Optional[str] = None) -> str:
        """
        Gọi AI (OpenAI hoặc Gemini) để trả lời
        
        Args:
            message: Câu hỏi của người dùng
            context: Ngữ cảnh (hypertension, diabetes, stroke, general)
            provider: "openai" hoặc "gemini"
            api_key: API key (nếu không có sẽ lấy từ env/secrets)
        """
        # System prompts theo context
        system_prompts = {
            "hypertension": "Bạn là chuyên gia tăng huyết áp. Giải thích đơn giản, dễ hiểu bằng tiếng Việt. Luôn nhắc gọi 115 nếu nguy hiểm.",
            "diabetes": "Bạn là chuyên gia tiểu đường. Giải thích về đường huyết bằng cả mmol/L và mg/dL. Ngôn ngữ dễ hiểu, tiếng Việt.",
            "stroke": "Bạn là chuyên gia đột quỵ. Nhấn mạnh BE-FAST và thời gian vàng. Luôn nhắc GỌI 115 NGAY. Trả lời bằng tiếng Việt.",
            "general": "Bạn là bác sĩ gia đình thân thiện. Giải thích y khoa bằng ngôn ngữ đời thường, dễ hiểu. An toàn là trên hết. Trả lời bằng tiếng Việt."
        }
        
        system_prompt = system_prompts.get(context, system_prompts["general"])
        system_prompt += "\n\nQUY TẮC: Không chẩn đoán, không kê đơn. Chỉ giáo dục và tư vấn chung. Trả lời ngắn gọn, dễ hiểu."
        
        # Thử Gemini trước (miễn phí!)
        if provider == "gemini":
            try:
                if not GEMINI_AVAILABLE:
                    raise ImportError("google-generativeai not installed")
                
                # Lấy API key từ parameter hoặc env/secrets
                gemini_key = api_key or os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")
                
                if not gemini_key:
                    return "⚠️ Chưa có Gemini API key. Vui lòng nhập API key ở sidebar!"
                
                genai.configure(api_key=gemini_key)
                model = genai.GenerativeModel('gemini-pro')
                
                # Kết hợp system prompt + user message
                full_prompt = f"{system_prompt}\n\nCâu hỏi: {message}"
                
                response = model.generate_content(full_prompt)
                return response.text
                
            except Exception as e:
                return f"❌ Lỗi Gemini: {str(e)}\n\nVui lòng kiểm tra API key hoặc chuyển sang OpenAI."
        
        # Thử OpenAI
        elif provider == "openai":
            try:
                if not OPENAI_AVAILABLE:
                    raise ImportError("openai not installed")
                
                # Lấy API key
                openai_key = api_key or os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")
                
                if not openai_key:
                    return "⚠️ Chưa có OpenAI API key. Vui lòng nhập API key ở sidebar!"
                
                client = openai.OpenAI(api_key=openai_key)
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": message}
                    ],
                    temperature=0.7,
                    max_tokens=500
                )
                
                return response.choices[0].message.content
                
            except Exception as e:
                return f"❌ Lỗi OpenAI: {str(e)}\n\nVui lòng kiểm tra API key."
        
        else:
            return self._get_template_response(message, context)
    
    def _get_template_response(self, message: str, context: str) -> str:
        """Trả lời mẫu khi không có AI"""
        
        responses = {
            "hypertension": """
Cảm ơn bạn đã hỏi về huyết áp! 💓

Để tư vấn chính xác, tôi cần biết thêm:
- Huyết áp của bạn là bao nhiêu?
- Có triệu chứng gì không?
- Đang dùng thuốc gì?

Hoặc bạn có thể:
- Xem trang **Tim Mạch** để tìm hiểu chi tiết
- Dùng **Công cụ đánh giá huyết áp**
- Đọc phần **Học Dễ** về huyết áp
""",
            "diabetes": """
Cảm ơn bạn đã hỏi về tiểu đường! 🩸

Để giúp bạn tốt hơn, cho tôi biết:
- Đường huyết của bạn là bao nhiêu? (mmol/L hoặc mg/dL)
- Có triệu chứng gì không?
- Đã khám bác sĩ chưa?

Hoặc bạn có thể:
- Xem trang **Tiểu Đường** 
- Dùng **Công cụ chuyển đổi đường huyết**
- Đọc phần **Học Dễ** về tiểu đường
""",
            "stroke": """
⚠️ Về đột quỵ - Thông tin QUAN TRỌNG:

**Dấu hiệu BE-FAST:**
- Mất thăng bằng
- Nhìn mờ
- Xệ mặt
- Yếu tay chân
- Nói khó

→ **BẤT KỲ dấu hiệu nào: GỌI 115 NGAY!**

Bạn muốn hỏi về:
- Phòng ngừa đột quỵ?
- Chăm sóc sau đột quỵ?
- Yếu tố nguy cơ?
""",
            "general": """
Cảm ơn bạn đã hỏi! 😊

Tôi có thể giúp bạn về:
- ❤️ Tim mạch (huyết áp, suy tim...)
- 🩸 Tiểu đường (đường huyết, insulin...)
- 🧠 Thần kinh (đột quỵ, động kinh...)
- 🍽️ Dinh dưỡng (ăn uống lành mạnh)

Bạn quan tâm về chủ đề nào? Hoặc chọn câu hỏi gợi ý bên dưới nhé!
"""
        }
        
        return responses.get(context, responses["general"])

