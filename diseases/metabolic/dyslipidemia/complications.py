"""
Nguyên nhân, biến chứng và phòng ngừa Rối loạn Lipid Máu
Causes, complications and prevention of Dyslipidemia
"""

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


