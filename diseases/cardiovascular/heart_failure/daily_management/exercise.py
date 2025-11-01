"""
Heart Failure Exercise Management
Hướng dẫn vận động cho người suy tim
"""

EXERCISE_SIMPLE = {
    "can_i_exercise_vn": """
❓ SUY TIM CÓ ĐƯỢC VẬN ĐỘNG KHÔNG?

✅ CÓ! Vận động vừa phải RẤT TỐT:
- Giúp tim khỏe hơn
- Tăng sức bền
- Giảm mệt mỏi
- Tâm trạng tốt hơn

❌ NHƯNG:
- Phải vận động ĐÚNG CÁCH
- KHÔNG tập quá sức
- Phải hỏi bác sĩ trước
""",
    
    "safe_exercises_vn": [
        {
            "name": "🚶 ĐI BỘ",
            "description": "Tốt nhất cho người suy tim",
            "how_to": [
                "Đi bộ chậm rãi 10-30 phút/ngày",
                "Đi đều đặn, không vội",
                "Nếu mệt thì nghỉ, ngồi xuống",
                "Đi ở chỗ bằng phẳng (tránh lên dốc)"
            ],
            "target": "Mục tiêu: 30 phút/ngày, 5 ngày/tuần"
        },
        {
            "name": "🧘 TẬP GIÃN CƠ NHẸ NHÀNG",
            "description": "Giãn cơ, yoga nhẹ, tai chi",
            "how_to": [
                "Giãn cơ từng phần: cánh tay, chân, lưng",
                "Hít thở sâu khi giãn",
                "Không giãn quá căng",
                "10-15 phút mỗi ngày"
            ]
        },
        {
            "name": "🪑 TẬP NGỒI",
            "description": "Nếu quá mệt để đi bộ",
            "how_to": [
                "Ngồi trên ghế, co duỗi chân",
                "Xoay cổ tay, cổ chân",
                "Vung tay nhẹ nhàng",
                "5-10 phút, vài lần/ngày"
            ]
        }
    ],
    
    "exercise_rules_vn": """
⚠️ QUY TẮC AN TOÀN KHI TẬP:

✅ TRƯỚC KHI TẬP:
1. Hỏi bác sĩ xem được tập không
2. Chọn thời điểm mát mẻ (sáng sớm, chiều mát)
3. Mặc quần áo thoáng mát
4. Đi giày êm chân

✅ TRONG KHI TẬP:
1. Tập NHẸ NHÀNG, TỪ TỪ
2. Có thể nói chuyện được = vừa sức
3. Không nín thở
4. Uống nước từng ngụm nhỏ (nếu được phép)

🛑 NGỪNG NGAY NẾU:
- Đau ngực
- Khó thở nhiều
- Chóng mặt, muốn ngất
- Mệt quá
- Tim đập loạn, rất nhanh
- Buồn nôn

→ Ngồi xuống nghỉ. Nếu không khỏi sau 5-10 phút: GỌI 115
""",
    
    "what_not_to_do_vn": [
        "❌ KHÔNG nâng vật nặng (>5kg)",
        "❌ KHÔNG đẩy, kéo đồ nặng",
        "❌ KHÔNG chạy bộ nhanh",
        "❌ KHÔNG leo dốc cao",
        "❌ KHÔNG tập khi trời nóng",
        "❌ KHÔNG tập khi đang bị cảm, sốt",
        "❌ KHÔNG tập sau ăn (đợi 1-2 giờ)"
    ]
}

