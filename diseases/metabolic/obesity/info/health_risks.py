"""
Health Risks - Nguy cơ sức khỏe từ béo phì
"""

HEALTH_RISKS = {
    "cardiovascular": {
        "name": "Bệnh Tim Mạch",
        "icon": "❤️",
        "risk_increase": "2-3 lần",
        "diseases": [
            "Cao huyết áp (70% nguy cơ)",
            "Bệnh mạch vành",
            "Suy tim",
            "Đột quỵ",
            "Rối loạn lipid máu"
        ]
    },
    
    "metabolic": {
        "name": "Rối loạn Chuyển hóa",
        "icon": "🩸",
        "risk_increase": "5-10 lần",
        "diseases": [
            "Tiểu đường type 2 (80% nguy cơ)",
            "Hội chứng chuyển hóa",
            "Gan nhiễm mỡ",
            "Sỏi mật"
        ]
    },
    
    "respiratory": {
        "name": "Bệnh Hô Hấp",
        "icon": "🫁",
        "risk_increase": "3-4 lần",
        "diseases": [
            "Ngưng thở khi ngủ (Sleep apnea)",
            "Hen phế quản",
            "COPD",
            "Khó thở khi gắng sức"
        ]
    },
    
    "musculoskeletal": {
        "name": "Bệnh Xương Khớp",
        "icon": "🦴",
        "risk_increase": "4-5 lần",
        "diseases": [
            "Thoái hóa khớp gối",
            "Thoái hóa khớp háng",
            "Gút (axit uric cao)",
            "Đau lưng mãn tính"
        ]
    },
    
    "cancer": {
        "name": "Ung thư",
        "icon": "🎗️",
        "risk_increase": "1.5-2 lần",
        "diseases": [
            "Ung thư đại trực tràng",
            "Ung thư vú (sau mãn kinh)",
            "Ung thư tử cung",
            "Ung thư gan",
            "Ung thư tụy"
        ]
    },
    
    "reproductive": {
        "name": "Sinh Sản",
        "icon": "👶",
        "risk_increase": "2-3 lần",
        "diseases": [
            "Vô sinh ở nữ (PCOS)",
            "Giảm testosterone ở nam",
            "Biến chứng thai kỳ",
            "Rối loạn kinh nguyệt"
        ]
    },
    
    "psychological": {
        "name": "Tâm Lý",
        "icon": "🧠",
        "risk_increase": "2 lần",
        "diseases": [
            "Trầm cảm",
            "Lo âu",
            "Tự ti, mặc cảm",
            "Giảm chất lượng cuộc sống"
        ]
    }
}


__all__ = ['HEALTH_RISKS']
