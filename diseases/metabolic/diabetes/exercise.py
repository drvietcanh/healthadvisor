"""
Vận động cho người Tiểu Đường
Bao gồm: Lợi ích, Loại hình, Mục tiêu, An toàn
"""

EXERCISE_SIMPLE = {
    "why_vn": """
🏃 TẠI SAO PHẢI VẬN ĐỘNG?

Vận động giúp:
✓ Giảm đường huyết (tế bào dùng đường mà không cần nhiều insulin)
✓ Giảm cân
✓ Tăng độ nhạy insulin
✓ Giảm nguy cơ tim mạch
✓ Tâm trạng tốt hơn
✓ Ngủ ngon hơn

Vận động đều đặn = THUỐC KHÔNG TỐN TIỀN!
""",
    
    "how_much_vn": """
🎯 MỤC TIÊU:

150 phút/tuần vận động VỪA PHẢI
= 30 phút x 5 ngày

Hoặc: 75 phút/tuần vận động MẠNH

Thêm: Tập kháng lực 2-3 lần/tuần
""",
    
    "types_vn": [
        {
            "name": "🚶 VẬN ĐỘNG NHỊP ĐIỆU (Aerobic)",
            "examples": "Đi bộ nhanh, chạy bộ, bơi, đạp xe, khiêu vũ",
            "benefit": "Giảm đường huyết, tốt cho tim",
            "how_long": "30-60 phút/lần, 5-7 ngày/tuần"
        },
        {
            "name": "🏋️ TẬP KHÁNG LỰC (Tạ)",
            "examples": "Tập tạ nhẹ, dây kháng lực, squat, chống đẩy",
            "benefit": "Tăng cơ, giảm mỡ, tăng độ nhạy insulin",
            "how_long": "20-30 phút, 2-3 lần/tuần"
        },
        {
            "name": "🧘 GIÃN CƠ, YOGA",
            "examples": "Yoga, tai chi, giãn cơ",
            "benefit": "Giảm stress, mềm dẻo, thư giãn",
            "how_long": "10-15 phút mỗi ngày"
        }
    ],
    
    "safety_tips_vn": """
⚠️ AN TOÀN KHI TẬP:

TRƯỚC KHI TẬP:
✅ Đo đường huyết
   - < 5.6 mmol/L (< 100 mg/dL): Ăn bữa phụ trước
   - 5.6 - 13.9 mmol/L (100 - 250 mg/dL): An toàn, tập được
   - > 13.9 mmol/L (> 250 mg/dL): Đợi đường xuống, không tập

✅ Mang theo:
   - Kẹo, nước ngọt (phòng hạ đường)
   - Nước uống
   - Điện thoại
   - Thẻ tiểu đường

TRONG KHI TẬP:
⚠️ Ngừng ngay nếu:
   - Chóng mặt, run, vã mồ hôi (dấu hiệu hạ đường)
   - Đau ngực
   - Khó thở nhiều

SAU KHI TẬP:
✅ Đo lại đường huyết
✅ Uống nước
✅ Ăn bữa phụ nếu cần
""",
    
    "beginner_plan_vn": """
🎯 KẾ HOẠCH CHO NGƯỜI MỚI BẮT ĐẦU:

TUẦN 1-2: Làm quen
- Đi bộ 10-15 phút/ngày
- Tập 3-4 ngày/tuần

TUẦN 3-4: Tăng dần
- Đi bộ 20-25 phút/ngày
- Tập 4-5 ngày/tuần

TUẦN 5-8: Ổn định
- Đi bộ nhanh 30 phút/ngày
- Tập 5 ngày/tuần
- Thêm tập kháng lực 2 ngày

SAU 8 TUẦN:
- Duy trì hoặc tăng cường độ
- Thử các hoạt động mới (bơi, đạp xe, khiêu vũ)
""",
    
    "simple_exercises_vn": {
        "walking": {
            "name": "🚶 Đi bộ",
            "why": "Dễ nhất, an toàn nhất, hiệu quả!",
            "how": "Đi bộ nhanh 30 phút/ngày (sau bữa ăn)",
            "calories": "~150 kcal/30 phút"
        },
        "stairs": {
            "name": "🪜 Leo cầu thang",
            "why": "Tăng cường tim phổi, chân khỏe",
            "how": "Leo 3-5 tầng, 2-3 lần/ngày",
            "calories": "~200 kcal/30 phút"
        },
        "cycling": {
            "name": "🚴 Đạp xe",
            "why": "Tốt cho khớp, giảm đường hiệu quả",
            "how": "Đạp xe 30-45 phút/ngày",
            "calories": "~250 kcal/30 phút"
        },
        "swimming": {
            "name": "🏊 Bơi",
            "why": "Vận động toàn thân, không đau khớp",
            "how": "Bơi 30-45 phút, 2-3 lần/tuần",
            "calories": "~300 kcal/30 phút"
        },
        "resistance": {
            "name": "🏋️ Tập tạ nhẹ",
            "why": "Tăng cơ, giảm mỡ, tăng độ nhạy insulin",
            "how": "Tập 8-12 động tác, mỗi động tác 10-15 lần, 2-3 lần/tuần",
            "exercises": [
                "Squat (ngồi xổm)",
                "Chống đẩy (push-up)",
                "Plank (chống tay)",
                "Tập tạ tay",
                "Dây kháng lực"
            ]
        }
    },
    
    "when_to_exercise_vn": """
⏰ THỜI ĐIỂM TỐT NHẤT:

✅ Sau bữa ăn 1-2 giờ:
   - Đường huyết đang cao
   - Vận động giúp giảm đường sau ăn
   - Ít nguy cơ hạ đường huyết

⚠️ TRÁNH:
   - Tập khi đói (dễ hạ đường)
   - Tập khi đường quá cao (> 13.9 mmol/L)
   - Tập quá muộn (ảnh hưởng ngủ)
""",
    
    "tips_vn": [
        "💡 Bắt đầu chậm, tăng dần - Đừng vội vàng!",
        "💡 Chọn hoạt động bạn THÍCH - Dễ duy trì lâu dài",
        "💡 Đi bộ sau mỗi bữa ăn 10-15 phút - Đơn giản mà hiệu quả!",
        "💡 Tập cùng bạn bè/gia đình - Vui hơn, động lực hơn",
        "💡 Đo đường trước/sau tập - Hiểu cơ thể mình phản ứng thế nào",
        "💡 Mang giày tốt, thoải mái - Bảo vệ chân (quan trọng!)",
        "💡 Kiểm tra chân sau tập - Phát hiện vết thương sớm"
    ]
}

