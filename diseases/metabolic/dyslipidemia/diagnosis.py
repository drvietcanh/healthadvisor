"""
Chẩn đoán và phân loại Rối loạn Lipid Máu
Diagnosis and classification of Dyslipidemia
"""

# Phân loại lipid theo mức độ
LIPID_CATEGORIES = {
    "cholesterol": [
        {"range": (0, 200), "label": "Tốt", "color": "#4CAF50", "icon": "✅"},
        {"range": (200, 240), "label": "Cao biên", "color": "#FF9800", "icon": "⚠️"},
        {"range": (240, 999), "label": "Cao", "color": "#F44336", "icon": "🚨"}
    ],
    
    "ldl": [
        {"range": (0, 100), "label": "Tối ưu", "color": "#4CAF50", "icon": "✅"},
        {"range": (100, 130), "label": "Gần tối ưu", "color": "#8BC34A", "icon": "👍"},
        {"range": (130, 160), "label": "Cao biên", "color": "#FF9800", "icon": "⚠️"},
        {"range": (160, 190), "label": "Cao", "color": "#FF5722", "icon": "❌"},
        {"range": (190, 999), "label": "Rất cao", "color": "#F44336", "icon": "🚨"}
    ],
    
    "hdl_male": [
        {"range": (0, 40), "label": "Thấp (Nguy hiểm)", "color": "#F44336", "icon": "❌"},
        {"range": (40, 60), "label": "Trung bình", "color": "#FF9800", "icon": "⚠️"},
        {"range": (60, 999), "label": "Tốt (Bảo vệ)", "color": "#4CAF50", "icon": "✅"}
    ],
    
    "hdl_female": [
        {"range": (0, 50), "label": "Thấp (Nguy hiểm)", "color": "#F44336", "icon": "❌"},
        {"range": (50, 60), "label": "Trung bình", "color": "#FF9800", "icon": "⚠️"},
        {"range": (60, 999), "label": "Tốt (Bảo vệ)", "color": "#4CAF50", "icon": "✅"}
    ],
    
    "triglyceride": [
        {"range": (0, 150), "label": "Bình thường", "color": "#4CAF50", "icon": "✅"},
        {"range": (150, 200), "label": "Cao biên", "color": "#FF9800", "icon": "⚠️"},
        {"range": (200, 500), "label": "Cao", "color": "#FF5722", "icon": "❌"},
        {"range": (500, 9999), "label": "Rất cao", "color": "#F44336", "icon": "🚨"}
    ]
}

# Triệu chứng (thường không có!)
SYMPTOMS = {
    "note": "⚠️ QUAN TRỌNG: Rối loạn lipid máu KHÔNG CÓ TRIỆU CHỨNG!",
    "detail": """
Hầu hết người bệnh KHÔNG CÓ biểu hiện gì cho đến khi:
- Xơ vữa động mạch nghiêm trọng
- Nhồi máu cơ tim
- Đột quỵ

→ Cần xét nghiệm định kỳ để phát hiện!
    """,
    
    "rare_signs": [
        {
            "name": "Ban vàng (Xanthomas)",
            "detail": "Mảng màu vàng ở da",
            "location": "Mí mắt, khuỷu tay, gân Achilles",
            "meaning": "Cholesterol rất cao (thường >300)",
            "image": "Chỉ thấy khi lipid RẤT cao"
        },
        {
            "name": "Cung giác mạc",
            "detail": "Vòng trắng quanh mống mắt",
            "meaning": "Cholesterol cao lâu năm",
            "note": "Phổ biến ở người >60 tuổi"
        },
        {
            "name": "Gan to, đau hạ sườn phải",
            "detail": "Gan nhiễm mỡ do TG cao",
            "note": "Khi TG >200"
        },
        {
            "name": "Đau bụng dữ dội",
            "detail": "Viêm tụy cấp",
            "note": "KHI TG >500 - CẤP CỨU!"
        }
    ]
}

# Chẩn đoán
DIAGNOSIS = {
    "screening": {
        "who": [
            "Tất cả nam >40 tuổi, nữ >50 tuổi",
            "Có tiền sử gia đình bệnh tim mạch sớm",
            "Béo phì, tiểu đường, cao huyết áp",
            "Hút thuốc lá",
            "Bệnh thận, suy giáp"
        ],
        "frequency": "3-5 năm/lần nếu bình thường; hàng năm nếu có nguy cơ"
    },
    
    "tests": {
        "lipid_panel": {
            "name": "Xét nghiệm mỡ máu (Lipid panel)",
            "fasting": "Nhịn ăn 9-12 giờ (chỉ uống nước)",
            "measures": [
                "Cholesterol toàn phần (TC)",
                "LDL-C (cholesterol xấu)",
                "HDL-C (cholesterol tốt)",
                "Triglyceride (TG)"
            ],
            "calculated": [
                "Non-HDL-C = TC - HDL-C",
                "TC/HDL ratio",
                "LDL/HDL ratio"
            ]
        },
        
        "other_tests": [
            "ApoB (Apolipoprotein B) - chính xác hơn LDL",
            "Lp(a) - lipoprotein (a) - nguy cơ di truyền",
            "hsCRP - viêm mạch máu",
            "HbA1c - đường huyết",
            "Creatinine, eGFR - chức năng thận"
        ]
    }
}


