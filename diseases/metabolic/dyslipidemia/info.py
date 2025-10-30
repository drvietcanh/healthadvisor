"""
Thông tin về Rối loạn Lipid Máu (Dyslipidemia)
==============================================

Cholesterol, LDL, HDL, Triglyceride
"""

DYSLIPIDEMIA_INFO = {
    "name": "Rối loạn Lipid Máu",
    "name_en": "Dyslipidemia",
    "definition": """
Rối loạn lipid máu là tình trạng một hoặc nhiều thành phần mỡ trong máu 
(cholesterol toàn phần, LDL-C, HDL-C, triglyceride) cao hoặc thấp bất thường.
    """,
    
    "simple_explanation": {
        "title": "💡 Giải thích đơn giản: Mỡ Xấu vs Mỡ Tốt",
        "analogy": """
Tưởng tượng mạch máu như con đường:

🚚 LDL (Mỡ XẤU) = Xe tải chở rác:
- Chở cholesterol ĐẾN thành mạch máu
- Đổ rác (mỡ) xuống đường → tắc nghẽn
- Càng nhiều xe tải → càng nhiều rác → đường càng hẹp
- → Nguy cơ tắc nghẽn (nhồi máu, đột quỵ)

🧹 HDL (Mỡ TỐT) = Xe quét rác:
- Hút mỡ TỪ thành mạch máu
- Chở về gan để xử lý, thải ra ngoài
- Càng nhiều xe quét → đường càng sạch
- → Bảo vệ tim mạch

🎯 MỤC TIÊU:
- GIẢM xe tải rác (LDL) ↓
- TĂNG xe quét rác (HDL) ↑
        """,
        
        "ldl_bad": {
            "name": "LDL - Mỡ XẤU (Low-Density Lipoprotein)",
            "why_bad": [
                "Dễ BÁM vào thành mạch máu",
                "Tạo MẢNG XƠ VỮA (giống cặn bẩn)",
                "Làm mạch máu HẸP dần",
                "Mảng vỡ → TẮC mạch → NHỒI MÁU"
            ],
            "example": """
Ví dụ: Ống nước bị cặn bẩn bám
- Ban đầu: Nước chảy tốt
- Lâu ngày: Cặn bám → ống hẹp → nước chảy yếu
- Cuối cùng: Cặn nhiều quá → TẮC → không chảy được
            """,
            "goal": "LDL càng THẤP càng TỐT (mục tiêu <100 mg/dL)"
        },
        
        "hdl_good": {
            "name": "HDL - Mỡ TỐT (High-Density Lipoprotein)",
            "why_good": [
                "HÚT mỡ RA khỏi thành mạch máu",
                "Chở về gan để phá hủy",
                "LÀM SẠCH mạch máu",
                "NGĂN CHẶN xơ vữa động mạch"
            ],
            "example": """
Ví dụ: Đội vệ sinh làm sạch đường
- Hút rác (mỡ) trên đường (mạch máu)
- Chở về bãi rác (gan) để xử lý
- Đường sạch → xe chạy tốt → tim khỏe
            """,
            "goal": "HDL càng CAO càng TỐT (mục tiêu ≥60 mg/dL)"
        },
        
        "triglyceride": {
            "name": "Triglyceride - Mỡ Dự trữ",
            "simple": """
Triglyceride = Mỡ THỪA từ ăn uống

- Ăn nhiều đường, tinh bột, rượu
- → Cơ thể chuyển thành mỡ để dự trữ
- → Triglyceride tăng trong máu
- → Tích tụ ở gan, mạch máu

Giống như: Ăn nhiều quá → mỡ bụng
            """,
            "danger": [
                "TG >150: Tăng nguy cơ tim mạch",
                "TG >500: Nguy cơ VIÊM TỤY - cấp cứu!"
            ],
            "solution": [
                "Giảm đường, tinh bột",
                "Bỏ rượu bia",
                "Tập thể dục",
                "Giảm cân"
            ]
        }
    },
    
    "statistics_vietnam": {
        "prevalence": "~30% dân số >40 tuổi",
        "stroke_patients": "68.6% bệnh nhân đột quỵ có rối loạn lipid",
        "awareness": "Chỉ 20% biết mình có bệnh",
        "treatment": "< 10% được điều trị đúng cách"
    },
    
    "key_points": [
        "Rối loạn lipid là thành phần của Hội chứng Chuyển hóa",
        "Nguyên nhân chính gây xơ vữa động mạch",
        "Tăng nguy cơ nhồi máu cơ tim, đột quỵ",
        "65% liên quan với béo phì",
        "Có thể kiểm soát bằng chế độ ăn + thuốc"
    ]
}

# Mục tiêu lipid máu theo hướng dẫn của Hội Tim Mạch Việt Nam & ESC/EAS
LIPID_TARGETS = {
    "cholesterol_total": {
        "name": "Cholesterol toàn phần",
        "unit": "mg/dL",
        "optimal": "<200",
        "borderline": "200-239",
        "high": "≥240",
        "note": "Tổng của LDL + HDL + VLDL"
    },
    
    "ldl_cholesterol": {
        "name": "LDL-C (Cholesterol xấu)",
        "unit": "mg/dL",
        "optimal": "<100",
        "near_optimal": "100-129",
        "borderline": "130-159",
        "high": "160-189",
        "very_high": "≥190",
        "targets": {
            "low_risk": "<116",
            "moderate_risk": "<100",
            "high_risk": "<70",
            "very_high_risk": "<55"
        },
        "note": "Mục tiêu khác nhau tùy nguy cơ tim mạch"
    },
    
    "hdl_cholesterol": {
        "name": "HDL-C (Cholesterol tốt)",
        "unit": "mg/dL",
        "low_male": "<40",
        "low_female": "<50",
        "optimal": "≥60",
        "note": "Cao hơn là tốt hơn - bảo vệ tim mạch"
    },
    
    "triglyceride": {
        "name": "Triglyceride (Mỡ máu)",
        "unit": "mg/dL",
        "optimal": "<150",
        "borderline": "150-199",
        "high": "200-499",
        "very_high": "≥500",
        "note": "Liên quan với tiểu đường, béo phì"
    },
    
    "non_hdl": {
        "name": "Non-HDL-C",
        "unit": "mg/dL",
        "formula": "TC - HDL-C",
        "optimal": "<130",
        "high": "≥160",
        "note": "Chỉ số tốt hơn LDL đơn thuần"
    },
    
    "tc_hdl_ratio": {
        "name": "Tỷ lệ TC/HDL-C",
        "optimal": "<3.5",
        "average": "3.5-5.0",
        "high_risk": ">5.0",
        "note": "Dự đoán nguy cơ tim mạch"
    }
}

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

# Nguyên nhân
CAUSES = {
    "primary": {
        "name": "Nguyên phát (Di truyền)",
        "causes": [
            {
                "name": "Tăng cholesterol máu gia đình",
                "detail": "Gen di truyền → LDL rất cao từ nhỏ",
                "prevalence": "1/200-500 người",
                "characteristics": "LDL >190 mg/dL, ban vàng ở mí mắt"
            },
            {
                "name": "Tăng triglyceride máu gia đình",
                "detail": "Gen → TG rất cao",
                "prevalence": "Hiếm",
                "characteristics": "TG >500 mg/dL, nguy cơ viêm tụy"
            }
        ]
    },
    
    "secondary": {
        "name": "Thứ phát (Do bệnh/lối sống)",
        "causes": [
            {
                "name": "Béo phì",
                "detail": "65% rối loạn lipid liên quan béo phì",
                "mechanism": "Tăng LDL, TG; Giảm HDL",
                "icon": "⚖️"
            },
            {
                "name": "Tiểu đường type 2",
                "detail": "70% tiểu đường có rối loạn lipid",
                "mechanism": "Tăng TG, giảm HDL, LDL nhỏ đặc",
                "icon": "🩸"
            },
            {
                "name": "Chế độ ăn không lành mạnh",
                "detail": "Nhiều chất béo bão hòa, trans fat",
                "mechanism": "Tăng LDL, giảm HDL",
                "icon": "🍔"
            },
            {
                "name": "Ít vận động",
                "detail": "Ngồi nhiều, không tập thể dục",
                "mechanism": "Giảm HDL, tăng TG",
                "icon": "🛋️"
            },
            {
                "name": "Hút thuốc lá",
                "detail": "Giảm HDL 10-15%",
                "mechanism": "Oxy hóa LDL → xơ vữa",
                "icon": "🚬"
            },
            {
                "name": "Uống rượu nhiều",
                "detail": ">2 ly/ngày",
                "mechanism": "Tăng TG",
                "icon": "🍺"
            },
            {
                "name": "Thuốc",
                "detail": "Corticoid, beta-blocker, thiazide...",
                "mechanism": "Tác dụng phụ",
                "icon": "💊"
            },
            {
                "name": "Bệnh thận",
                "detail": "Hội chứng thận hư",
                "mechanism": "Tăng cholesterol",
                "icon": "🫘"
            },
            {
                "name": "Suy giáp",
                "detail": "Thiếu hormone giáp",
                "mechanism": "Giảm chuyển hóa LDL → tăng LDL",
                "icon": "🦋"
            }
        ]
    }
}

# Biến chứng
COMPLICATIONS = {
    "cardiovascular": {
        "name": "Tim Mạch",
        "icon": "❤️",
        "risk_increase": "2-4 lần",
        "complications": [
            {
                "name": "Xơ vữa động mạch",
                "detail": "LDL bám vào thành động mạch → mảng xơ vữa",
                "timeline": "Bắt đầu từ 20 tuổi, tiến triển chậm"
            },
            {
                "name": "Bệnh mạch vành",
                "detail": "Hẹp động mạch vành → đau thắt ngực",
                "risk": "LDL >190: Nguy cơ x3"
            },
            {
                "name": "Nhồi máu cơ tim",
                "detail": "Mảng vữa vỡ → tắc động mạch vành",
                "risk": "Nguyên nhân #1 tử vong do lipid cao"
            },
            {
                "name": "Đột quỵ",
                "detail": "Tắc động mạch não",
                "risk": "68.6% đột quỵ có rối loạn lipid"
            },
            {
                "name": "Bệnh động mạch ngoại biên",
                "detail": "Hẹp động mạch chi dưới → đau khi đi",
                "risk": "Có thể dẫn đến hoại tử, cắt cụt"
            }
        ]
    },
    
    "pancreas": {
        "name": "Tụy",
        "icon": "🫀",
        "risk_increase": "Khi TG >500",
        "complications": [
            {
                "name": "Viêm tụy cấp",
                "detail": "TG >500 mg/dL → viêm tụy dữ dội",
                "symptoms": "Đau bụng dữ dội, nôn, sốt",
                "risk": "Nguy hiểm tính mạng"
            }
        ]
    },
    
    "other": {
        "name": "Khác",
        "complications": [
            "Ban vàng (xanthomas) - mảng vàng ở da, gân",
            "Cung giác mạc - vòng trắng quanh mống mắt",
            "Gan nhiễm mỡ",
            "Sỏi mật"
        ]
    }
}

# Liên kết với bệnh khác
RELATED_DISEASES = {
    "metabolic_syndrome": {
        "name": "Hội chứng Chuyển hóa",
        "relation": "Rối loạn lipid là 1 trong 5 thành phần",
        "criteria": "TG ≥150 mg/dL hoặc HDL <40 (nam) / <50 (nữ)",
        "page": "4_⚖️_Hội_Chứng_Chuyển_Hóa"
    },
    
    "obesity": {
        "name": "Béo phì",
        "relation": "65% rối loạn lipid có béo phì",
        "mechanism": "Mỡ nội tạng → tăng LDL, TG; giảm HDL",
        "page": "4_⚖️_Hội_Chứng_Chuyển_Hóa"
    },
    
    "diabetes": {
        "name": "Tiểu đường Type 2",
        "relation": "70% tiểu đường có rối loạn lipid",
        "mechanism": "Kháng insulin → tăng TG, LDL nhỏ đặc",
        "page": "3_🩸_Tiểu_Đường"
    },
    
    "hypertension": {
        "name": "Cao huyết áp",
        "relation": "60% cao HA có rối loạn lipid",
        "mechanism": "Cùng gốc: béo phì, kháng insulin",
        "page": "2_❤️_Tim_Mạch"
    },
    
    "cardiovascular": {
        "name": "Bệnh tim mạch",
        "relation": "Nguyên nhân chính gây xơ vữa ĐM",
        "risk": "LDL >190 → Nguy cơ x3",
        "page": "2_❤️_Tim_Mạch"
    }
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

# Phòng ngừa
PREVENTION = {
    "lifestyle": {
        "title": "Thay đổi lối sống (Quan trọng nhất!)",
        "measures": [
            {
                "category": "Chế độ ăn",
                "icon": "🍽️",
                "actions": [
                    "Giảm chất béo bão hòa (<7% calories)",
                    "Tránh trans fat (0%)",
                    "Tăng chất xơ (25-30g/ngày)",
                    "Ăn cá béo 2-3 lần/tuần (omega-3)",
                    "Thay thịt đỏ bằng gà, cá",
                    "Dùng dầu ô liu thay bơ, mỡ",
                    "Tăng rau xanh, trái cây"
                ]
            },
            {
                "category": "Vận động",
                "icon": "🏃",
                "actions": [
                    "150 phút/tuần hoạt động vừa phải",
                    "Hoặc 75 phút/tuần hoạt động mạnh",
                    "Đi bộ nhanh 30 phút x 5 ngày",
                    "Tập aerobic + tạ nhẹ"
                ],
                "benefit": "Tăng HDL 5-10%, giảm TG 20-30%"
            },
            {
                "category": "Giảm cân",
                "icon": "⚖️",
                "actions": [
                    "Giảm 5-10% cân nặng",
                    "BMI mục tiêu: 18.5-23 (châu Á)"
                ],
                "benefit": "Giảm LDL 5-8%, TG 20%, tăng HDL 20%"
            },
            {
                "category": "Bỏ thuốc lá",
                "icon": "🚭",
                "benefit": "Tăng HDL 10-15%, giảm oxy hóa LDL"
            },
            {
                "category": "Hạn chế rượu",
                "icon": "🍺",
                "limit": "Nam: ≤2 ly/ngày, Nữ: ≤1 ly/ngày",
                "note": "Rượu nhiều → Tăng TG"
            }
        ]
    },
    
    "medications": {
        "title": "Thuốc (Khi lối sống không đủ)",
        "when": [
            "LDL vẫn cao sau 3-6 tháng thay đổi lối sống",
            "Nguy cơ tim mạch cao",
            "Đã có bệnh tim mạch",
            "Tiểu đường + tuổi 40-75",
            "LDL >190 mg/dL"
        ],
        "note": "Phải kết hợp với thay đổi lối sống, không thay thế!"
    }
}

