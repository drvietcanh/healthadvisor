"""
Related Diseases - Bệnh liên quan đến béo phì
"""

RELATED_DISEASES = {
    "direct_consequences": {
        "diabetes": {
            "name": "Tiểu đường Type 2",
            "risk": "80%",
            "mechanism": "Béo phì → Kháng insulin → Tiểu đường",
            "symptoms": [
                "Khát nhiều, uống nhiều",
                "Tiểu nhiều",
                "Ăn nhiều nhưng sụt cân",
                "Mệt mỏi, nhìn mờ"
            ],
            "prevention": "Giảm cân 5-10% → Giảm nguy cơ tiểu đường 50-60%",
            "page": "3_🩸_Tiểu_Đường"
        },
        "hypertension": {
            "name": "Cao huyết áp",
            "risk": "70%",
            "mechanism": "Béo phì → Tăng khối lượng máu → Tăng huyết áp",
            "symptoms": [
                "Huyết áp > 140/90 mmHg",
                "Thường không có triệu chứng",
                "Có thể đau đầu, chóng mặt khi huyết áp rất cao"
            ],
            "prevention": "Giảm cân 1kg → Giảm huyết áp 1-2 mmHg",
            "page": "1_❤️_Tim_Mạch"
        },
        "dyslipidemia": {
            "name": "Rối loạn lipid máu",
            "risk": "65%",
            "mechanism": "Béo phì → Tăng LDL, giảm HDL, tăng triglyceride",
            "symptoms": [
                "Thường không có triệu chứng",
                "Phát hiện qua xét nghiệm máu",
                "Có thể có xơ vữa mạch máu"
            ],
            "prevention": "Giảm cân + Ăn ít mỡ động vật → Giảm LDL 10-15%",
            "page": "1_❤️_Tim_Mạch"
        }
    },
    
    "indirect_consequences": {
        "heart_failure": {
            "name": "Suy tim",
            "risk": "2x",
            "mechanism": "Béo phì → Cao huyết áp lâu năm → Suy tim",
            "symptoms": [
                "Khó thở khi gắng sức",
                "Mệt mỏi, yếu sức",
                "Phù chân, bụng",
                "Ho khi nằm"
            ],
            "prevention": "Kiểm soát huyết áp, tiểu đường + Giảm cân",
            "page": "1_❤️_Tim_Mạch"
        },
        "copd": {
            "name": "COPD",
            "risk": "3x",
            "mechanism": "Béo phì → Khó thở → Giảm chức năng phổi",
            "symptoms": [
                "Khó thở khi gắng sức",
                "Ho mạn tính",
                "Đờm nhiều",
                "Tức ngực"
            ],
            "prevention": "Bỏ thuốc lá + Giảm cân + Tập thể dục phổi",
            "page": "2_🫁_Hô_Hấp"
        }
    },
    
    "other_complications": {
        "osteoarthritis": {
            "name": "Thoái hóa khớp",
            "risk": "4x",
            "mechanism": "Béo phì → Áp lực lên khớp → Mòn sụn",
            "symptoms": [
                "Đau khớp gối, hông",
                "Cứng khớp buổi sáng",
                "Đau khi đi lại",
                "Khớp kêu lục cục"
            ],
            "prevention": "Giảm cân 1kg → Giảm áp lực lên khớp gối 4kg!",
            "page": None
        },
        "gout": {
            "name": "Gút",
            "risk": "3x",
            "mechanism": "Béo phì → Axit uric cao → Gút",
            "symptoms": [
                "Đau khớp đột ngột (ngón chân cái)",
                "Sưng, đỏ, nóng khớp",
                "Đau dữ dội, không chịu được",
                "Tái phát nhiều lần"
            ],
            "prevention": "Giảm cân + Tránh bia rượu, nội tạng + Uống nhiều nước",
            "page": None
        }
    }
}


__all__ = ['RELATED_DISEASES']
