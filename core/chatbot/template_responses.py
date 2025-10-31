"""
Template Responses
Trả lời mẫu khi không có AI
"""


def get_template_response(message: str, context: str) -> str:
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

