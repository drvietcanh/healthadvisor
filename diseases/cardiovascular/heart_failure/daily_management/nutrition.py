"""
Heart Failure Nutrition Management
Hướng dẫn ăn uống cho người suy tim
"""

NUTRITION_SIMPLE = {
    "main_rule_vn": """
🍽️ NGUYÊN TẮC ĂN UỐNG CHO NGƯỜI SUY TIM:

Nhớ 3 GIẢM, 3 TĂNG:

📉 3 GIẢM:
1. GIẢM MUỐI (quan trọng nhất!)
2. GIẢM NƯỚC (nếu bác sĩ dặn)
3. GIẢM MỠ ĐỘNG VẬT

📈 3 TĂNG:
1. TĂNG RAU CỦ
2. TĂNG ĐẠM (thịt nạc, cá, trứng)
3. TĂNG KALI (chuối, cam, khoai)
""",
    
    "salt_restriction_simple": {
        "why_vn": """
🧂 TẠI SAO PHẢI GIẢM MUỐI?

Muối giữ nước → Nước tích nhiều → Tim phải bơm nhiều hơn → Tim càng yếu

Giống như bắt người đã mệt phải kéo thêm nước nặng vậy!
""",
        "how_much_vn": """
📊 ĂN BAO NHIÊU MUỐI?

Người bình thường: 1 thìa cà phê muối/ngày
Người suy tim: ½ thìa cà phê muối/ngày (hoặc ít hơn)

💡 MẸO TÍNH NHANH:
- 1 thìa cà phê muối = 5g
- Bạn cần ăn < 2-3g muối/ngày
""",
        "hidden_salt_vn": """
🕵️ MUỐI ẨN - TRÁNH CÁC MÓN NÀY:

❌ Đồ MẶN:
- Mắm, nước mắm, tương
- Muối chua, dưa chua
- Chả, giò, thịt nguội
- Xúc xích, thịt xông khói
- Snack (khoai chiên, bánh quy mặn)

❌ Đồ HỘP/ĐÓNG GÓI:
- Mì gói (rất nhiều muối!)
- Đồ hộp (cá hộp, thịt hộp)
- Nước sốt chai (tương ớt, xì dầu)
- Bột canh, hạt nêm, mì chính

❌ ĂN NGOÀI:
- Phở (nước dùng mặn)
- Bún, miến (nước dùng)
- Cơm quán (thường nấu mặn)
- Đồ ăn nhanh
""",
        "tips_vn": """
💡 LÀM SAO ĂN NGON MÀ ÍT MUỐI?

✅ THAY MUỐI BẰNG:
- Chanh, giấm
- Gừng, tỏi, hành
- Tiêu, ớt (ít)
- Rau thơm (ngò, rau răm, húng)

✅ NẤU Ở NHÀ:
- Tự nấu, tự nêm nhạt
- Nếu ăn phở/bún: bỏ nước dùng, chỉ ăn rau + thịt

✅ ĐỌC NHÃN:
- Chọn sản phẩm ghi "ít muối" hoặc "không muối"
- Tránh sản phẩm có > 120mg natri/100g
"""
    },
    
    "fluid_restriction_simple": {
        "why_vn": """
💧 TẠI SAO PHẢI HẠN CHẾ NƯỚC?

Nếu suy tim nặng:
- Thận làm việc kém
- Nước tích lại trong cơ thể
- Phù chân, phù phổi, khó thở

Nhưng không phải ai cũng phải hạn chế!
→ Hỏi bác sĩ xem bạn có cần không.
""",
        "how_much_vn": """
📏 UỐNG BAO NHIÊU NƯỚC?

Nếu bác sĩ bảo hạn chế:
- Thường: 1 - 1.5 lít/ngày (5-7 ly)
- Suy tim nặng: 0.8 - 1 lít/ngày (4-5 ly)

💡 CÁCH TÍNH:
Tất cả chất lỏng đều tính:
- Nước lọc, trà
- Súp, cháo, canh
- Sữa, nước hoa quả
- Thạch, kem
""",
        "tips_vn": """
💡 MẸO KIỂM SOÁT NƯỚC:

✅ Dùng ly nhỏ
✅ Súc miệng khi khát (đừng nuốt)
✅ Ngậm đá lạnh
✅ Nhai kẹo cao su không đường
✅ Cân mỗi sáng - nếu tăng cân đột ngột (1-2kg) = tích nước!
"""
    },
    
    "what_to_eat_vn": {
        "breakfast_examples": [
            "🥣 Cháo thịt băm (nhạt) + trứng + rau",
            "🍞 Bánh mì + trứng luộc + cà chua",
            "🥛 Sữa tươi không đường + yến mạch + chuối"
        ],
        "lunch_examples": [
            "🍚 Cơm + cá hấp (ít muối) + rau luộc + canh rau",
            "🍚 Cơm + ức gà luộc + đậu hũ + rau xào",
            "🍚 Cơm + thịt bò xào rau củ (ít muối)"
        ],
        "dinner_examples": [
            "🍜 Miến gà (bỏ nước dùng, chỉ ăn thịt + rau)",
            "🍚 Cơm + cá kho (rất nhạt) + rau",
            "🥗 Salad gà + bánh mì nguyên cám"
        ],
        "snacks": [
            "🍌 Chuối (tốt, nhiều kali)",
            "🍊 Cam, quýt",
            "🥜 Hạt không muối (1 nắm nhỏ)",
            "🥛 Sữa chua không đường"
        ]
    },
    
    "foods_to_avoid_simple": [
        "🚫 Đồ CHIÊN RÁN (gà rán, khoai chiên...)",
        "🚫 Đồ MỠ NHIỀU (mỡ lợn, da gà, sườn...)",
        "🚫 Đồ NGỌT (bánh kem, nước ngọt...)",
        "🚫 RƯỢU, BIA (quan trọng!)",
        "🚫 CÀ PHÊ NHIỀU (> 2 ly/ngày)",
        "🚫 Đồ HỘP, ĐÓNG GÓI"
    ]
}

