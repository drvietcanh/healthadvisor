"""
Related Diseases - Bệnh liên quan đến béo phì
"""

RELATED_DISEASES = {
    "direct_consequences": {
        "diabetes": {
            "name": "Tiểu đường Type 2",
            "risk": "80%",
            "mechanism": "Béo phì → Kháng insulin → Tiểu đường",
            "page": "2_🩸_Tiểu_Đường"
        },
        "hypertension": {
            "name": "Cao huyết áp",
            "risk": "70%",
            "mechanism": "Béo phì → Tăng khối lượng máu → Tăng huyết áp",
            "page": "1_❤️_Tim_Mạch"
        },
        "dyslipidemia": {
            "name": "Rối loạn lipid máu",
            "risk": "65%",
            "mechanism": "Béo phì → Tăng LDL, giảm HDL, tăng triglyceride",
            "page": "1_❤️_Tim_Mạch"  # Tab 3
        }
    },
    
    "complications": {
        "heart_failure": {
            "name": "Suy tim",
            "risk": "2x",
            "mechanism": "Cao huyết áp lâu năm → Suy tim",
            "page": "1_❤️_Tim_Mạch"
        },
        "copd": {
            "name": "COPD",
            "risk": "3x",
            "mechanism": "Béo phì → Khó thở → Giảm chức năng phổi",
            "page": "11_🫁_Hô_Hấp"  # Sẽ tạo
        },
        "osteoarthritis": {
            "name": "Thoái hóa khớp",
            "risk": "4x",
            "mechanism": "Béo phì → Áp lực lên khớp → Mòn sụn",
            "page": "12_🦴_Xương_Khớp"  # Sẽ tạo
        },
        "gout": {
            "name": "Gút",
            "risk": "3x",
            "mechanism": "Béo phì → Axit uric cao → Gút",
            "page": "12_🦴_Xương_Khớp"  # Sẽ tạo
        }
    }
}


__all__ = ['RELATED_DISEASES']
