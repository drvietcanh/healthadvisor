"""
Đánh giá Nguy cơ Tim Mạch
Cardiovascular Risk Assessment
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
    if gender == "male":
        if age < 35:
            points += -1
        elif age < 40:
            points += 0
        elif age < 45:
            points += 1
        elif age < 50:
            points += 2
        elif age < 55:
            points += 3
        elif age < 60:
            points += 4
        elif age < 65:
            points += 5
        elif age < 70:
            points += 6
        else:
            points += 7
    else:  # female
        if age < 35:
            points += -9
        elif age < 40:
            points += -4
        elif age < 45:
            points += 0
        elif age < 50:
            points += 3
        elif age < 55:
            points += 6
        elif age < 60:
            points += 7
        elif age < 65:
            points += 8
        else:
            points += 8
    
    # Total Cholesterol points
    if gender == "male":
        if cholesterol < 160:
            points += -3
        elif cholesterol < 200:
            points += 0
        elif cholesterol < 240:
            points += 1
        elif cholesterol < 280:
            points += 2
        else:
            points += 3
    else:
        if cholesterol < 160:
            points += -2
        elif cholesterol < 200:
            points += 0
        elif cholesterol < 240:
            points += 1
        elif cholesterol < 280:
            points += 1
        else:
            points += 3
    
    # HDL points
    if hdl < 35:
        points += 2
    elif hdl < 45:
        points += 1
    elif hdl < 50:
        points += 0
    elif hdl < 60:
        points += 0
    else:
        points += -1
    
    # Blood Pressure points
    if on_bp_medication:
        if systolic_bp < 120:
            points += 0
        elif systolic_bp < 130:
            points += 2
        elif systolic_bp < 140:
            points += 3
        elif systolic_bp < 160:
            points += 4
        else:
            points += 5
    else:
        if systolic_bp < 120:
            points += 0
        elif systolic_bp < 130:
            points += 0
        elif systolic_bp < 140:
            points += 1
        elif systolic_bp < 160:
            points += 2
        else:
            points += 3
    
    # Smoking
    if smoker:
        points += 2
    
    # Diabetes
    if diabetes:
        points += 2
    
    # Convert points to risk percentage
    # Simplified conversion
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
    
    risk_percentage = risk_map.get(points, 50 if points > 13 else 1)
    
    # Categorize risk
    if risk_percentage < 10:
        category = "Thấp"
        color = "#4CAF50"
        icon = "✅"
        action = "Duy trì lối sống lành mạnh"
    elif risk_percentage < 20:
        category = "Trung bình"
        color = "#FF9800"
        icon = "⚠️"
        action = "Cần thay đổi lối sống, có thể cần thuốc"
    else:
        category = "Cao"
        color = "#F44336"
        icon = "🚨"
        action = "CẦN ĐIỀU TRỊ TÍCH CỰC! Dùng thuốc + lối sống"
    
    return {
        "points": points,
        "risk_percentage": risk_percentage,
        "category": category,
        "color": color,
        "icon": icon,
        "action": action,
        "note": f"Nguy cơ mắc bệnh tim mạch trong 10 năm tới: {risk_percentage}%"
    }


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
    if ldl >= 190:
        risk_factors.append("LDL rất cao (≥190)")
        risk_points += 3
    elif ldl >= 160:
        risk_factors.append("LDL cao (160-189)")
        risk_points += 2
    elif ldl >= 130:
        risk_factors.append("LDL cao biên (130-159)")
        risk_points += 1
    
    # HDL thấp
    threshold = 40 if gender == "male" else 50
    if hdl < threshold:
        risk_factors.append(f"HDL thấp (<{threshold})")
        risk_points += 1
    
    # Tuổi
    if age >= 65:
        risk_factors.append("Tuổi cao (≥65)")
        risk_points += 1
    elif age >= 55:
        risk_factors.append("Tuổi trung niên (55-64)")
        risk_points += 0.5
    
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
    if has_cvd or ldl >= 190 or risk_points >= 5:
        risk_level = "Rất cao"
        ldl_target = "<55"
        color = "#F44336"
        icon = "🚨"
    elif has_diabetes or risk_points >= 3:
        risk_level = "Cao"
        ldl_target = "<70"
        color = "#FF5722"
        icon = "❌"
    elif risk_points >= 2:
        risk_level = "Trung bình"
        ldl_target = "<100"
        color = "#FF9800"
        icon = "⚠️"
    else:
        risk_level = "Thấp"
        ldl_target = "<116"
        color = "#4CAF50"
        icon = "✅"
    
    return {
        "risk_level": risk_level,
        "risk_factors": risk_factors,
        "risk_factors_count": len(risk_factors),
        "ldl_target": ldl_target,
        "color": color,
        "icon": icon,
        "current_ldl": ldl,
        "ldl_reduction_needed": max(0, ldl - int(ldl_target.replace("<", ""))),
    }


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


def get_treatment_recommendations(
    ldl: float,
    risk_level: str,
    current_ldl: float
) -> Dict:
    """
    Đề xuất điều trị
    
    Args:
        ldl: LDL hiện tại
        risk_level: Mức độ nguy cơ
        current_ldl: LDL hiện tại (duplicate for compatibility)
    
    Returns:
        Dict với recommendations
    """
    category_info = get_risk_category(risk_level)
    target_ldl = int(category_info["ldl_target"].replace("<", "").replace("mg/dL", "").strip())
    
    reduction_needed = current_ldl - target_ldl
    reduction_pct = (reduction_needed / current_ldl * 100) if current_ldl > 0 else 0
    
    recommendations = {
        "lifestyle": [
            "🥗 Giảm chất béo bão hòa (<7% calories)",
            "🚫 Tránh trans fat hoàn toàn",
            "🐟 Ăn cá béo 2-3 lần/tuần",
            "🥬 Tăng rau xanh, ngũ cốc nguyên hạt",
            "🏃 Vận động 150 phút/tuần",
            "⚖️ Giảm cân nếu thừa cân"
        ],
        "medication": [],
        "monitoring": []
    }
    
    # Medication recommendations based on risk
    if risk_level == "Rất cao":
        recommendations["medication"] = [
            "💊 STATIN liều cao (Atorvastatin 40-80mg hoặc Rosuvastatin 20-40mg)",
            "💊 Có thể thêm Ezetimibe 10mg nếu chưa đạt mục tiêu",
            "💊 Cân nhắc PCSK9 inhibitor nếu LDL vẫn >55 sau dùng thuốc tối đa"
        ]
        recommendations["monitoring"] = [
            "📊 Xét nghiệm lipid 2-3 tháng/lần",
            "🩺 Khám tim mạch 3-6 tháng/lần",
            "🧪 Kiểm tra men gan sau 1-2 tháng dùng statin"
        ]
    
    elif risk_level == "Cao":
        recommendations["medication"] = [
            "💊 STATIN liều trung bình-cao (Atorvastatin 20-40mg)",
            "💊 Tăng liều hoặc thêm Ezetimibe nếu chưa đạt mục tiêu"
        ]
        recommendations["monitoring"] = [
            "📊 Xét nghiệm lipid 3-6 tháng/lần",
            "🩺 Khám tim mạch 6 tháng/lần"
        ]
    
    elif risk_level == "Trung bình":
        if reduction_pct > 30:
            recommendations["medication"] = [
                "💊 Cân nhắc STATIN liều thấp-trung bình",
                "⏰ Thử lối sống 3-6 tháng trước khi dùng thuốc"
            ]
        else:
            recommendations["medication"] = [
                "⏰ Thử thay đổi lối sống 3-6 tháng trước",
                "💊 Dùng statin nếu LDL vẫn không đạt mục tiêu"
            ]
        recommendations["monitoring"] = [
            "📊 Xét nghiệm lipid 3-6 tháng sau thay đổi lối sống",
            "🩺 Khám tim mạch 1 năm/lần"
        ]
    
    else:  # Thấp
        recommendations["medication"] = [
            "✅ KHÔNG CẦN THUỐC - chỉ duy trì lối sống lành mạnh"
        ]
        recommendations["monitoring"] = [
            "📊 Xét nghiệm lipid 3-5 năm/lần",
            "🩺 Khám sức khỏe định kỳ hàng năm"
        ]
    
    return {
        "current_ldl": current_ldl,
        "target_ldl": target_ldl,
        "reduction_needed": round(reduction_needed, 1),
        "reduction_percentage": round(reduction_pct, 1),
        "risk_level": risk_level,
        "recommendations": recommendations,
        "note": f"Cần giảm LDL {reduction_needed:.0f} mg/dL ({reduction_pct:.0f}%)" if reduction_needed > 0 else "LDL đã đạt mục tiêu!"
    }


