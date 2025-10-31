"""
COPD Other Medications - Các thuốc khác
========================================

Thuốc làm loãng đờm, kháng sinh, theophylline, PDE-4 inhibitor
"""

OTHER_MEDICATIONS = {
    "mucolytics": {
        "name": "Thuốc Làm Loãng Đờm",
        "examples": [
            {
                "name": "Acetylcysteine (NAC)",
                "brand": "ACC, Fluimucil",
                "dose": "200mg x 3 lần/ngày hoặc 600mg x 1 lần/ngày",
                "benefit": "Làm loãng đờm, dễ khạc ra",
                "price": "50,000-150,000đ/tháng"
            },
            {
                "name": "Carbocysteine",
                "brand": "Mucopect",
                "dose": "750mg x 3 lần/ngày",
                "price": "100,000-200,000đ/tháng"
            }
        ],
        "when_to_use": "Khi có nhiều đờm, khó khạc",
        "evidence": "Bằng chứng YẾU, không khuyến cáo thường quy"
    },
    
    "antibiotics": {
        "name": "Kháng Sinh",
        "use": "CHỈ khi ĐỢT CẤP do nhiễm trùng",
        "signs_of_infection": [
            "Đờm vàng/xanh (mủ)",
            "Sốt",
            "Khó thở tăng đột ngột"
        ],
        "examples": [
            "Amoxicillin/Clavulanate (Augmentin)",
            "Azithromycin (Zithromax)",
            "Levofloxacin"
        ],
        "duration": "5-7 ngày",
        "warning": "⚠️ KHÔNG tự ý dùng kháng sinh! Phải có đơn bác sĩ"
    },
    
    "theophylline": {
        "name": "Theophylline",
        "brand": "Aminophylline, Euphyllin",
        "dose": "200-400mg x 2 lần/ngày",
        "benefit": "Giãn phế quản, giảm mệt cơ hô hấp",
        "use": "Thuốc CŨ, ít dùng nay (nhiều tác dụng phụ)",
        "side_effects": ["Buồn nôn", "Đánh trống ngực", "Mất ngủ"],
        "price": "30,000-80,000đ/tháng"
    },
    
    "pde4_inhibitor": {
        "name": "PDE-4 Inhibitor",
        "example": "Roflumilast (Daxas)",
        "use": "COPD rất nặng + viêm phế quản mạn + hay đợt cấp",
        "benefit": "Giảm đợt cấp 15-20%",
        "side_effects": "Tiêu chảy, sụt cân, buồn nôn",
        "price": "1,500,000-2,000,000đ/tháng",
        "note": "Đắt, ít dùng tại VN"
    }
}

