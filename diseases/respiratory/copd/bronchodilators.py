"""
COPD Bronchodilators - Thuốc giãn phế quản
============================================

Thuốc giãn phế quản ngắn hạn và dài hạn cho COPD
"""

BRONCHODILATORS = {
    "title": "🫁 Thuốc Giãn Phế Quản - Nòng Cốt Điều Trị",
    
    "simple_explanation": """
💡 Thuốc giãn phế quản là gì?

Tưởng tượng đường thở như ống nước:
- COPD: Ống bị co thắt, hẹp → Khó thở
- Thuốc giãn phế quản: NỞ RỘNG ống → Thở dễ hơn

2 loại chính:
- NGẮN HẠN: Tác dụng nhanh (5 phút), ngắn (4-6 giờ) → Dùng KHI CẦN
- DÀI HẠN: Tác dụng chậm, kéo dài (12-24 giờ) → Dùng HÀNG NGÀY
    """,
    
    "short_acting": {
        "name": "Thuốc Ngắn Hạn (SABA + SAMA)",
        "use": "Dùng KHI CẦN - khi khó thở",
        
        "saba": {
            "name": "SABA - Beta-2 agonist ngắn hạn",
            "examples_vietnam": [
                {
                    "name": "Salbutamol (Ventolin)",
                    "brand": "Ventolin, Asthalin, Asmacort",
                    "form": "Xịt, dung dịch khí dung",
                    "dose": "2 nhát xịt (100mcg/nhát) khi khó thở",
                    "onset": "5 phút",
                    "duration": "4-6 giờ",
                    "price": "50,000-100,000đ/hộp"
                },
                {
                    "name": "Terbutaline",
                    "brand": "Bricanyl",
                    "form": "Viên uống, xịt",
                    "dose": "0.25-0.5mg, 3 lần/ngày",
                    "price": "30,000-80,000đ"
                }
            ]
        },
        
        "sama": {
            "name": "SAMA - Anticholinergic ngắn hạn",
            "examples_vietnam": [
                {
                    "name": "Ipratropium (Atrovent)",
                    "brand": "Atrovent",
                    "form": "Xịt, dung dịch khí dung",
                    "dose": "2 nhát xịt, 4 lần/ngày",
                    "onset": "15-30 phút",
                    "duration": "6-8 giờ",
                    "price": "150,000-250,000đ/hộp"
                }
            ]
        },
        
        "combination": {
            "name": "Kết Hợp SABA + SAMA",
            "example": "Combivent (Salbutamol + Ipratropium)",
            "benefit": "Hiệu quả GẤP ĐÔI so với dùng riêng",
            "price": "200,000-300,000đ"
        },
        
        "when_to_use": [
            "Khi khó thở đột ngột",
            "Trước khi gắng sức (leo cầu thang, đi bộ xa)",
            "Đợt cấp",
            "Tối đa 4-6 lần/ngày"
        ],
        
        "warning": "⚠️ Nếu cần dùng >4 lần/ngày → Bệnh NẶNG, cần gặp bác sĩ!"
    },
    
    "long_acting": {
        "name": "Thuốc Dài Hạn (LABA + LAMA)",
        "use": "Dùng HÀNG NGÀY - dù khỏe hay ốm",
        
        "laba": {
            "name": "LABA - Beta-2 agonist dài hạn",
            "examples_vietnam": [
                {
                    "name": "Formoterol",
                    "brand": "Foradil, Oxis",
                    "duration": "12 giờ",
                    "dose": "2 lần/ngày (sáng, tối)",
                    "price": "300,000-500,000đ/tháng"
                },
                {
                    "name": "Salmeterol",
                    "brand": "Serevent",
                    "duration": "12 giờ",
                    "dose": "2 lần/ngày",
                    "price": "400,000-600,000đ/tháng"
                },
                {
                    "name": "Indacaterol",
                    "brand": "Onbrez",
                    "duration": "24 giờ",
                    "dose": "1 lần/ngày",
                    "price": "600,000-800,000đ/tháng"
                }
            ]
        },
        
        "lama": {
            "name": "LAMA - Anticholinergic dài hạn",
            "examples_vietnam": [
                {
                    "name": "Tiotropium (Spiriva)",
                    "brand": "Spiriva",
                    "duration": "24 giờ",
                    "dose": "1 lần/ngày (buổi sáng)",
                    "price": "800,000-1,200,000đ/tháng",
                    "note": "Thuốc PHỔ BIẾN NHẤT tại VN"
                },
                {
                    "name": "Glycopyrronium",
                    "brand": "Seebri",
                    "duration": "24 giờ",
                    "dose": "1 lần/ngày",
                    "price": "700,000-1,000,000đ/tháng"
                }
            ]
        },
        
        "combination_laba_lama": {
            "name": "Kết Hợp LABA + LAMA (Tốt Nhất!)",
            "examples": [
                {
                    "name": "Ultibro (Indacaterol + Glycopyrronium)",
                    "dose": "1 lần/ngày",
                    "benefit": "Hiệu quả tốt nhất, giảm đợt cấp 30-40%",
                    "price": "1,200,000-1,500,000đ/tháng"
                },
                {
                    "name": "Anoro (Vilanterol + Umeclidinium)",
                    "dose": "1 lần/ngày",
                    "price": "1,000,000-1,400,000đ/tháng"
                }
            ],
            "indication": "COPD nhóm B, C, D"
        },
        
        "when_to_use": "COPD từ GOLD 2 trở lên, mMRC ≥2, CAT ≥10"
    }
}

