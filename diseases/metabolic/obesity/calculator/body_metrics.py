"""
Body Metrics - Các chỉ số cơ thể (WHR, Body Fat %)
"""

from typing import Dict


def calculate_whr(waist_cm: float, hip_cm: float, gender: str) -> Dict:
    """
    Tính WHR (Waist to Hip Ratio) - Tỷ lệ vòng eo/hông
    Đánh giá phân bố mỡ và nguy cơ tim mạch
    
    Args:
        waist_cm: Vòng eo (cm)
        hip_cm: Vòng hông (cm)
        gender: "male" hoặc "female"
    
    Returns:
        Dict với WHR và risk assessment
    """
    if waist_cm <= 0 or hip_cm <= 0:
        raise ValueError("Vòng eo và vòng hông phải > 0")
    
    whr = waist_cm / hip_cm
    
    # Risk thresholds theo WHO
    if gender == "male":
        if whr < 0.90:
            risk = "Thấp"
            color = "#66BB6A"
            icon = "✅"
        elif whr < 0.95:
            risk = "Trung bình"
            color = "#FFEB3B"
            icon = "⚠️"
        else:
            risk = "Cao"
            color = "#F44336"
            icon = "🚨"
    else:  # female
        if whr < 0.80:
            risk = "Thấp"
            color = "#66BB6A"
            icon = "✅"
        elif whr < 0.85:
            risk = "Trung bình"
            color = "#FFEB3B"
            icon = "⚠️"
        else:
            risk = "Cao"
            color = "#F44336"
            icon = "🚨"
    
    return {
        "whr": round(whr, 2),
        "risk": risk,
        "color": color,
        "icon": icon,
        "threshold": "Nam: <0.90, Nữ: <0.80 (Thấp)",
        "note": "WHR cao → Mỡ bụng nhiều → Nguy cơ tim mạch cao"
    }


def calculate_body_fat_percentage(
    bmi: float,
    age: int,
    gender: str
) -> Dict:
    """
    Ước tính % mỡ cơ thể dựa trên BMI và tuổi
    (Công thức Deurenberg)
    
    Args:
        bmi: BMI value
        age: Tuổi
        gender: "male" hoặc "female"
    
    Returns:
        Dict với body fat % và category
    """
    # Công thức Deurenberg
    # Adult: (1.20 x BMI) + (0.23 x Age) - (10.8 x gender) - 5.4
    # gender: male=1, female=0
    
    gender_value = 1 if gender == "male" else 0
    body_fat = (1.20 * bmi) + (0.23 * age) - (10.8 * gender_value) - 5.4
    body_fat = max(0, body_fat)  # Không âm
    
    # Phân loại theo American Council on Exercise (ACE)
    if gender == "male":
        categories = {
            "essential": (2, 5, "Thiết yếu (vận động viên)", "#4DA6FF"),
            "athletes": (6, 13, "Vận động viên", "#66BB6A"),
            "fitness": (14, 17, "Khỏe mạnh", "#66BB6A"),
            "average": (18, 24, "Trung bình", "#FFEB3B"),
            "obese": (25, 100, "Béo phì", "#F44336")
        }
    else:  # female
        categories = {
            "essential": (10, 13, "Thiết yếu (vận động viên)", "#4DA6FF"),
            "athletes": (14, 20, "Vận động viên", "#66BB6A"),
            "fitness": (21, 24, "Khỏe mạnh", "#66BB6A"),
            "average": (25, 31, "Trung bình", "#FFEB3B"),
            "obese": (32, 100, "Béo phì", "#F44336")
        }
    
    category_name = "Unknown"
    category_color = "#999999"
    
    for cat_id, (min_pct, max_pct, label, color) in categories.items():
        if min_pct <= body_fat <= max_pct:
            category_name = label
            category_color = color
            break
    
    return {
        "body_fat_percentage": round(body_fat, 1),
        "category": category_name,
        "color": category_color,
        "gender": gender,
        "note": "Đây là ước tính, cần DEXA scan để chính xác"
    }


__all__ = ['calculate_whr', 'calculate_body_fat_percentage']
