"""
Tiêu Chảy Cấp (Acute Diarrhea) - Thông tin cơ bản
"""

DIARRHEA_INFO = {
    "name": "Tiêu Chảy Cấp",
    "name_en": "Acute Diarrhea",
    
    "simple_explanation": """
💡 Tiêu chảy cấp là gì? (Giải thích đơn giản)

Bình thường: Ruột hấp thu nước từ thức ăn → Phân thành khuôn
Tiêu chảy: Ruột không hấp thu được nước → Phân lỏng, đi nhiều lần

💧 Chuyện gì xảy ra:
1. Vi khuẩn/virus/độc tố vào ruột → Gây viêm ruột
2. Ruột tiết nhiều nước, không hấp thu được nước
3. Phân lỏng, đi nhiều lần (3-10+ lần/ngày)
4. Mất nước → Nguy hiểm! (đặc biệt trẻ em, người già)

⚠️ ĐẶC ĐIỂM:
- Cấp tính: Đột ngột, kéo dài <14 ngày
- Nguyên nhân: Nhiễm trùng (vi khuẩn/virus), ngộ độc thức ăn
- Quan trọng: Bù nước đủ → Không nguy hiểm
    """,
    
    "causes": {
        "infectious": {
            "title": "Nhiễm trùng:",
            "bacteria": [
                "E. coli (thịt sống, rau sống không sạch)",
                "Salmonella (trứng, thịt gà chưa chín)",
                "Campylobacter (thịt gia cầm)",
                "Shigella (nước bẩn, thực phẩm nhiễm khuẩn)"
            ],
            "virus": [
                "Rotavirus (trẻ em)",
                "Norovirus (người lớn, lây nhanh)",
                "Adenovirus"
            ]
        },
        "food_poisoning": {
            "title": "Ngộ độc thức ăn:",
            "causes": [
                "Thức ăn để lâu, ôi thiu",
                "Thức ăn sống, chưa chín kỹ",
                "Nước uống không sạch",
                "Rau sống rửa không kỹ"
            ]
        },
        "other": {
            "title": "Nguyên nhân khác:",
            "causes": [
                "Thuốc (kháng sinh, thuốc nhuận tràng)",
                "Rối loạn tiêu hóa tạm thời",
                "Stress, lo lắng"
            ]
        }
    },
    
    "when_to_worry": {
        "title": "⚠️ Khi nào lo:",
        "signs": [
            "Tiêu chảy > 10 lần/ngày",
            "Có máu trong phân",
            "Sốt cao (>38.5°C)",
            "Mất nước nặng (không đi tiểu >6 giờ, khô miệng)",
            "Trẻ em, người già",
            "Kéo dài > 3 ngày không đỡ"
        ]
    }
}

