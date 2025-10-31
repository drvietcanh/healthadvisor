"""
Framingham Risk Score Calculator
Tính điểm nguy cơ tim mạch theo Framingham
"""

from typing import Dict


def calculate_framingham_score(
    age: int,
    gender: str,
    cholesterol: float,
    hdl: float,
    systolic_bp: float,
    on_bp_medication: bool = False,
    smoker: bool = False,
    diabetes: bool = False
) -> Dict:
    """
    Tính Framingham Risk Score (nguy cơ tim mạch 10 năm)
    
    Args:
        age: Tuổi (30-74)
        gender: "male" hoặc "female"
        cholesterol: TC (mg/dL)
        hdl: HDL-C (mg/dL)
        systolic_bp: Huyết áp tâm thu (mmHg)
        on_bp_medication: Đang dùng thuốc huyết áp?
        smoker: Hút thuốc?
        diabetes: Có tiểu đường?
    
    Returns:
        Dict với risk score và category
    """
    # Simplified Framingham Score (ATP III)
    points = 0
    
    # Age points
    points += _get_age_points(age, gender)
    
    # Total Cholesterol points
    points += _get_cholesterol_points(cholesterol, gender)
    
    # HDL points
    points += _get_hdl_points(hdl)
    
    # Blood Pressure points
    points += _get_blood_pressure_points(systolic_bp, on_bp_medication)
    
    # Smoking
    if smoker:
        points += 2
    
    # Diabetes
    if diabetes:
        points += 2
    
    # Convert points to risk percentage
    risk_percentage = _points_to_risk_percentage(points, gender)
    
    # Categorize risk
    category_info = _categorize_risk(risk_percentage)
    
    return {
        "points": points,
        "risk_percentage": risk_percentage,
        "category": category_info["category"],
        "color": category_info["color"],
        "icon": category_info["icon"],
        "action": category_info["action"],
        "note": f"Nguy cơ mắc bệnh tim mạch trong 10 năm tới: {risk_percentage}%"
    }


def _get_age_points(age: int, gender: str) -> int:
    """Tính điểm theo tuổi"""
    if gender == "male":
        if age < 35:
            return -1
        elif age < 40:
            return 0
        elif age < 45:
            return 1
        elif age < 50:
            return 2
        elif age < 55:
            return 3
        elif age < 60:
            return 4
        elif age < 65:
            return 5
        elif age < 70:
            return 6
        else:
            return 7
    else:  # female
        if age < 35:
            return -9
        elif age < 40:
            return -4
        elif age < 45:
            return 0
        elif age < 50:
            return 3
        elif age < 55:
            return 6
        elif age < 60:
            return 7
        elif age < 65:
            return 8
        else:
            return 8


def _get_cholesterol_points(cholesterol: float, gender: str) -> int:
    """Tính điểm theo cholesterol"""
    if gender == "male":
        if cholesterol < 160:
            return -3
        elif cholesterol < 200:
            return 0
        elif cholesterol < 240:
            return 1
        elif cholesterol < 280:
            return 2
        else:
            return 3
    else:
        if cholesterol < 160:
            return -2
        elif cholesterol < 200:
            return 0
        elif cholesterol < 240:
            return 1
        elif cholesterol < 280:
            return 1
        else:
            return 3


def _get_hdl_points(hdl: float) -> int:
    """Tính điểm theo HDL"""
    if hdl < 35:
        return 2
    elif hdl < 45:
        return 1
    elif hdl < 50:
        return 0
    elif hdl < 60:
        return 0
    else:
        return -1


def _get_blood_pressure_points(systolic_bp: float, on_bp_medication: bool) -> int:
    """Tính điểm theo huyết áp"""
    if on_bp_medication:
        if systolic_bp < 120:
            return 0
        elif systolic_bp < 130:
            return 2
        elif systolic_bp < 140:
            return 3
        elif systolic_bp < 160:
            return 4
        else:
            return 5
    else:
        if systolic_bp < 120:
            return 0
        elif systolic_bp < 130:
            return 0
        elif systolic_bp < 140:
            return 1
        elif systolic_bp < 160:
            return 2
        else:
            return 3


def _points_to_risk_percentage(points: int, gender: str) -> int:
    """Chuyển điểm thành phần trăm nguy cơ"""
    if gender == "male":
        risk_map = {
            -3: 1, -2: 1, -1: 2, 0: 2, 1: 3, 2: 4, 3: 5,
            4: 7, 5: 8, 6: 10, 7: 13, 8: 16, 9: 20, 10: 25,
            11: 31, 12: 37, 13: 45
        }
    else:
        risk_map = {
            -2: 1, -1: 2, 0: 2, 1: 2, 2: 3, 3: 3, 4: 4,
            5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 11, 11: 13,
            12: 15, 13: 17, 14: 20, 15: 24
        }
    
    return risk_map.get(points, 50 if points > 13 else 1)


def _categorize_risk(risk_percentage: int) -> Dict:
    """Phân loại mức độ nguy cơ"""
    if risk_percentage < 10:
        return {
            "category": "Thấp",
            "color": "#4CAF50",
            "icon": "✅",
            "action": "Duy trì lối sống lành mạnh"
        }
    elif risk_percentage < 20:
        return {
            "category": "Trung bình",
            "color": "#FF9800",
            "icon": "⚠️",
            "action": "Cần thay đổi lối sống, có thể cần thuốc"
        }
    else:
        return {
            "category": "Cao",
            "color": "#F44336",
            "icon": "🚨",
            "action": "CẦN ĐIỀU TRỊ TÍCH CỰC! Dùng thuốc + lối sống"
        }

