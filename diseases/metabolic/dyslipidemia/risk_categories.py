"""
Risk Categories
Phân loại và thông tin về các mức độ nguy cơ tim mạch
"""

from typing import Dict


def get_risk_category(risk_level: str) -> Dict:
    """Lấy thông tin chi tiết về category nguy cơ"""
    categories = {
        "Thấp": {
            "description": "Nguy cơ tim mạch thấp",
            "ldl_target": "<116 mg/dL",
            "treatment": "Thay đổi lối sống",
            "follow_up": "Xét nghiệm 3-5 năm/lần"
        },
        "Trung bình": {
            "description": "Nguy cơ tim mạch trung bình",
            "ldl_target": "<100 mg/dL",
            "treatment": "Lối sống + cân nhắc thuốc",
            "follow_up": "Xét nghiệm 1 năm/lần"
        },
        "Cao": {
            "description": "Nguy cơ tim mạch cao",
            "ldl_target": "<70 mg/dL",
            "treatment": "Lối sống + THUỐC STATIN",
            "follow_up": "Xét nghiệm 3-6 tháng/lần"
        },
        "Rất cao": {
            "description": "Nguy cơ tim mạch rất cao",
            "ldl_target": "<55 mg/dL",
            "treatment": "Lối sống + THUỐC MẠNH + theo dõi sát",
            "follow_up": "Xét nghiệm 2-3 tháng/lần"
        }
    }
    return categories.get(risk_level, categories["Trung bình"])

