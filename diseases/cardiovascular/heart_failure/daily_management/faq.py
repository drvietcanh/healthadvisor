"""
Heart Failure FAQ and Chatbot Questions
Câu hỏi thường gặp và câu hỏi cho chatbot
"""

FAQ_SIMPLE = [
    {
        "q_vn": "Suy tim có khỏi được không?",
        "a_vn": "Suy tim là bệnh mãn tính, khó khỏi hẳn. NHƯNG bạn vẫn có thể sống tốt, lâu dài nếu:\n- Uống thuốc đúng\n- Ăn uống đúng cách\n- Vận động vừa phải\n- Theo dõi sát\n\nNhiều người sống 10-20 năm với suy tim!"
    },
    {
        "q_vn": "Tôi có thể làm việc được không?",
        "a_vn": "Tùy mức độ suy tim:\n- Nhẹ: Có thể làm việc nhẹ nhàng\n- Nặng: Nên nghỉ ngơi nhiều\n\nTránh công việc:\n- Nặng nhọc\n- Căng thẳng cao\n- Môi trường nóng"
    },
    {
        "q_vn": "Nếu quên uống thuốc thì sao?",
        "a_vn": "- Nhớ ra trong cùng ngày: Uống ngay\n- Đã gần giờ liều sau: Bỏ qua, KHÔNG uống 2 liều\n- KHÔNG tự ý tăng liều\n- Đặt báo thức để nhớ"
    },
    {
        "q_vn": "Có cần kiêng quan hệ tình dục không?",
        "a_vn": "Không nhất thiết! Nếu bệnh ổn định, bạn vẫn có thể quan hệ bình thường. Hỏi bác sĩ để yên tâm."
    }
]

CHATBOT_QUESTIONS = [
    {
        "step": 1,
        "question_vn": "Xin chào! Tôi là trợ lý tư vấn về bệnh suy tim. Để tôi hiểu tình trạng của bạn:\n\n🤔 Bạn đã được bác sĩ chẩn đoán suy tim chưa?",
        "options": ["Rồi", "Chưa, tôi chỉ nghi ngờ", "Không chắc"]
    },
    {
        "step": 2,
        "question_vn": "Bạn có triệu chứng nào sau đây không? (có thể chọn nhiều)\n\n- Khó thở (đặc biệt khi nằm xuống)\n- Phù chân\n- Mệt mỏi\n- Ho (đặc biệt ban đêm)\n- Chóng mặt",
        "purpose": "Đánh giá triệu chứng"
    },
    {
        "step": 3,
        "question_vn": "Bạn đang uống thuốc gì cho tim không? Nếu có, kể tên giúp tôi nhé.\n\n(Ví dụ: Lasix, Enalapril, Bisoprolol...)"
    },
    {
        "step": 4,
        "question_vn": "Bây giờ bạn muốn tôi tư vấn về phần nào?\n\n1️⃣ Giải thích về bệnh suy tim\n2️⃣ Ăn uống thế nào?\n3️⃣ Thuốc điều trị\n4️⃣ Có được tập thể dục không?\n5️⃣ Theo dõi tại nhà như thế nào?\n6️⃣ Khi nào cần gọi bác sĩ?"
    }
]

