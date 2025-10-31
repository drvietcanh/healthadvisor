"""
Cardiovascular Risk Assessment
Đánh giá tổng hợp nguy cơ tim mạch
"""

from typing import Dict


def calculate_cardiovascular_risk(
    ldl: float,
    hdl: float,
    age: int,
    gender: str,
    has_diabetes: bool = False,
    has_hypertension: bool = False,
    smoker: bool = False,
    has_cvd: bool = False
) -> Dict:
    """
    Đánh giá tổng hợp nguy cơ tim mạch
    
    Returns:
        Dict với risk level và recommendations
    """
    risk_factors = []
    risk_points = 0
    
    # LDL cao
    risk_points += _assess_ldl_risk(ldl, risk_factors)
    
    # HDL thấp
    risk_points += _assess_hdl_risk(hdl, gender, risk_factors)
    
    # Tuổi
    risk_points += _assess_age_risk(age, risk_factors)
    
    # Các yếu tố khác
    if has_diabetes:
        risk_factors.append("Tiểu đường")
        risk_points += 2
    
    if has_hypertension:
        risk_factors.append("Cao huyết áp")
        risk_points += 1
    
    if smoker:
        risk_factors.append("Hút thuốc")
        risk_points += 1
    
    if has_cvd:
        risk_factors.append("Đã có bệnh tim mạch")
        risk_points += 3
    
    # Classify risk
    risk_info = _classify_risk_level(risk_points, has_cvd, ldl, has_diabetes)
    
    return {
        "risk_level": risk_info["risk_level"],
        "risk_factors": risk_factors,
        "risk_factors_count": len(risk_factors),
        "ldl_target": risk_info["ldl_target"],
        "color": risk_info["color"],
        "icon": risk_info["icon"],
        "current_ldl": ldl,
        "ldl_reduction_needed": max(0, ldl - int(risk_info["ldl_target"].replace("<", ""))),
    }


def _assess_ldl_risk(ldl: float, risk_factors: list) -> float:
    """Đánh giá nguy cơ từ LDL"""
    if ldl >= 190:
        risk_factors.append("LDL rất cao (≥190)")
        return 3
    elif ldl >= 160:
        risk_factors.append("LDL cao (160-189)")
        return 2
    elif ldl >= 130:
        risk_factors.append("LDL cao biên (130-159)")
        return 1
    return 0


def _assess_hdl_risk(hdl: float, gender: str, risk_factors: list) -> float:
    """Đánh giá nguy cơ từ HDL"""
    threshold = 40 if gender == "male" else 50
    if hdl < threshold:
        risk_factors.append(f"HDL thấp (<{threshold})")
        return 1
    return 0


def _assess_age_risk(age: int, risk_factors: list) -> float:
    """Đánh giá nguy cơ từ tuổi"""
    if age >= 65:
        risk_factors.append("Tuổi cao (≥65)")
        return 1
    elif age >= 55:
        risk_factors.append("Tuổi trung niên (55-64)")
        return 0.5
    return 0


def _classify_risk_level(
    risk_points: float,
    has_cvd: bool,
    ldl: float,
    has_diabetes: bool
) -> Dict:
    """Phân loại mức độ nguy cơ"""
    if has_cvd or ldl >= 190 or risk_points >= 5:
        return {
            "risk_level": "Rất cao",
            "ldl_target": "<55",
            "color": "#F44336",
            "icon": "🚨"
        }
    elif has_diabetes or risk_points >= 3:
        return {
            "risk_level": "Cao",
            "ldl_target": "<70",
            "color": "#FF5722",
            "icon": "❌"
        }
    elif risk_points >= 2:
        return {
            "risk_level": "Trung bình",
            "ldl_target": "<100",
            "color": "#FF9800",
            "icon": "⚠️"
        }
    else:
        return {
            "risk_level": "Thấp",
            "ldl_target": "<116",
            "color": "#4CAF50",
            "icon": "✅"
        }

