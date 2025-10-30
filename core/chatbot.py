"""
AI Chatbot tư vấn y tế - Hỗ trợ trò chuyện từng bước như bác sĩ
"""
import os
from typing import List, Dict, Optional


class HealthChatbot:
    """Chatbot tư vấn y tế thông minh"""
    
    def __init__(self, disease_type: str = "general"):
        """
        Khởi tạo chatbot
        
        Args:
            disease_type: Loại bệnh (cardiovascular, diabetes, neurological, general)
        """
        self.disease_type = disease_type
        self.conversation_history: List[Dict[str, str]] = []
        self.current_step = 0
        
    def add_message(self, role: str, content: str):
        """Thêm tin nhắn vào lịch sử"""
        self.conversation_history.append({
            "role": role,  # "user" hoặc "assistant"
            "content": content
        })
    
    def get_system_prompt(self) -> str:
        """Lấy system prompt theo loại bệnh"""
        base_prompt = """
Bạn là trợ lý y tế thân thiện, chuyên nghiệp và đáng tin cậy.

NGUYÊN TẮC QUAN TRỌNG:
1. SỬ DỤNG NGÔN NGỮ ĐƠN GIẢN, DỄ HIỂU - tránh thuật ngữ y khoa phức tạp
2. TƯ VẤN AN TOÀN - không chẩn đoán bệnh, không kê đơn thuốc
3. KHUYẾN KHÍCH GẶP BÁC SĨ khi cần thiết
4. THÂN THIỆN, ĐỒNG CẢM với bệnh nhân
5. HỎI TỪNG BƯỚC - như bác sĩ hỏi bệnh
6. GIẢI THÍCH RÕ RÀNG - tại sao cần làm gì
7. KHÔNG ĐÁNG SỢ - động viên tinh thần

KHI NÀO GỌI CẤP CỨU:
- Luôn nhắc gọi 115 với triệu chứng nguy hiểm
- Đau ngực, khó thở nghiêm trọng, yếu liệt đột ngột → GỌI 115 NGAY

PHONG CÁCH TRẢ LỜI:
- Ngắn gọn, dễ hiểu
- Dùng emoji phù hợp (😊 ✅ ⚠️ 🚨)
- Ví dụ cụ thể
- Chia nhỏ thông tin
"""
        
        disease_prompts = {
            "cardiovascular": """
Chuyên môn: TIM MẠCH (tăng huyết áp, suy tim, bệnh mạch vành)
Tập trung: Hướng dẫn ăn ít muối, thuốc tim mạch phổ biến, vận động an toàn
""",
            "diabetes": """
Chuyên môn: TIỂU ĐƯỜNG (típ 1, típ 2)
Tập trung: Đường huyết (mmol/L và mg/dL), ăn uống, insulin, đo đường tại nhà
""",
            "neurological": """
Chuyên môn: THẦN KINH (đột quỵ, động kinh, Parkinson)
Tập trung: Nhận biết triệu chứng cấp cứu, phòng ngừa, phục hồi
""",
            "general": """
Chuyên môn: TƯ VẤN SỨC KHỎE TỔNG QUÁT
Tập trung: Hướng dẫn nhận biết triệu chứng, khi nào cần gặp bác sĩ
"""
        }
        
        return base_prompt + disease_prompts.get(self.disease_type, disease_prompts["general"])
    
    def get_response(self, user_message: str, use_ai: bool = True) -> str:
        """
        Nhận phản hồi từ chatbot
        
        Args:
            user_message: Tin nhắn từ người dùng
            use_ai: Dùng AI (OpenAI) hoặc trả lời mẫu
            
        Returns:
            Phản hồi của chatbot
        """
        self.add_message("user", user_message)
        
        if use_ai:
            response = self._get_ai_response(user_message)
        else:
            response = self._get_template_response(user_message)
        
        self.add_message("assistant", response)
        return response
    
    def _get_ai_response(self, user_message: str) -> str:
        """Gọi API OpenAI để lấy phản hồi"""
        try:
            # Import tại đây để tránh lỗi nếu không cài OpenAI
            import openai
            
            # Kiểm tra API key
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                return "⚠️ Chưa cấu hình API key. Vui lòng thêm OPENAI_API_KEY vào biến môi trường."
            
            # Tạo messages cho API
            messages = [{"role": "system", "content": self.get_system_prompt()}]
            messages.extend(self.conversation_history)
            
            # Gọi API
            client = openai.OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # Model rẻ và nhanh
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"⚠️ Lỗi kết nối AI: {str(e)}\n\nVui lòng thử lại hoặc liên hệ hỗ trợ."
    
    def _get_template_response(self, user_message: str) -> str:
        """Trả lời mẫu khi không dùng AI"""
        user_lower = user_message.lower()
        
        # Phát hiện câu hỏi về triệu chứng cấp cứu
        emergency_keywords = ["đau ngực", "khó thở", "yếu liệt", "méo miệng", "đột quỵ"]
        if any(kw in user_lower for kw in emergency_keywords):
            return """
🚨 CẢNH BÁO: Triệu chứng bạn mô tả có thể NGHIÊM TRỌNG!

👉 GỌI CẤP CỨU 115 NGAY nếu có:
- Đau ngực dữ dội
- Khó thở nặng
- Yếu liệt, tê nửa người
- Méo miệng, nói khó

⏰ THỜI GIAN LÀ VÀNG - Đừng trì hoãn!
"""
        
        # Phát hiện câu hỏi về thuốc
        if "thuốc" in user_lower or "uống" in user_lower:
            return """
💊 VỀ THUỐC ĐIỀU TRỊ:

⚠️ Lưu ý quan trọng:
- Chỉ dùng thuốc theo chỉ định bác sĩ
- KHÔNG tự ý mua thuốc uống
- KHÔNG tự ý ngưng thuốc

Bạn muốn biết về nhóm thuốc nào? 
(Ví dụ: thuốc huyết áp, thuốc tiểu đường...)
"""
        
        # Phát hiện câu hỏi về ăn uống
        if "ăn" in user_lower or "dinh dưỡng" in user_lower or "thức ăn" in user_lower:
            return """
🍽️ VỀ CHẾ ĐỘ ĂN UỐNG:

Tôi có thể tư vấn về:
1️⃣ Thực phẩm nên ăn
2️⃣ Thực phẩm nên tránh  
3️⃣ Thực đơn mẫu hàng ngày
4️⃣ Mẹo nấu ăn lành mạnh

Bạn muốn biết về phần nào? 😊
"""
        
        # Trả lời chung
        return """
Cảm ơn bạn đã chia sẻ! 

Để tư vấn chính xác hơn, bạn có thể cho tôi biết:
- Bạn quan tâm về bệnh gì?
- Có triệu chứng gì không?
- Đã khám bác sĩ chưa?

Tôi sẽ cố gắng tư vấn hết sức! 😊
"""
    
    def reset_conversation(self):
        """Đặt lại cuộc trò chuyện"""
        self.conversation_history = []
        self.current_step = 0

