"""
Obesity Calculators - Các công cụ tính toán
===========================================

BMI, TDEE, WHR, Body Fat %, Ideal Weight, Timeline...
"""

import math
from typing import Dict, Tuple, Optional
from .info import BMI_CATEGORIES_ASIAN


def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    """
    Tính BMI (Body Mass Index)
    
    Args:
        weight_kg: Cân nặng (kg)
        height_cm: Chiều cao (cm)
    
    Returns:
        BMI value
    
    Formula: BMI = weight(kg) / (height(m))^2
    """
    if weight_kg <= 0 or height_cm <= 0:
        raise ValueError("Cân nặng và chiều cao phải > 0")
    
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)


def get_bmi_category(bmi: float) -> Dict:
    """
    Phân loại BMI theo chuẩn Châu Á
    
    Args:
        bmi: BMI value
    
    Returns:
        Category info dict
    """
    for category_id, category_info in BMI_CATEGORIES_ASIAN.items():
        min_bmi, max_bmi = category_info["range"]
        if min_bmi <= bmi < max_bmi:
            return {
                "id": category_id,
                **category_info
            }
    
    # Default nếu BMI quá cao
    return {
        "id": "obese_2",
        **BMI_CATEGORIES_ASIAN["obese_2"]
    }


def calculate_ideal_weight(height_cm: float, gender: str = "male") -> Dict:
    """
    Tính cân nặng lý tưởng theo công thức Devine (điều chỉnh châu Á)
    
    Args:
        height_cm: Chiều cao (cm)
        gender: "male" hoặc "female"
    
    Returns:
        Dict với ideal weight và range
    """
    if height_cm <= 0:
        raise ValueError("Chiều cao phải > 0")
    
    # Công thức Devine (điều chỉnh cho châu Á)
    # Nam: 50 + 2.3 x (height_in - 60) x 0.9  (0.9 = Asian adjustment)
    # Nữ: 45.5 + 2.3 x (height_in - 60) x 0.9
    
    height_in = height_cm / 2.54  # Convert cm to inches
    
    if gender == "male":
        if height_in <= 60:
            ideal = 50
        else:
            ideal = 50 + 2.3 * (height_in - 60) * 0.9
    else:  # female
        if height_in <= 60:
            ideal = 45.5
        else:
            ideal = 45.5 + 2.3 * (height_in - 60) * 0.9
    
    # BMI 18.5-23 range (chuẩn châu Á)
    height_m = height_cm / 100
    min_weight = 18.5 * (height_m ** 2)
    max_weight = 23.0 * (height_m ** 2)
    
    return {
        "ideal": round(ideal, 1),
        "range": (round(min_weight, 1), round(max_weight, 1)),
        "bmi_range": (18.5, 23.0)
    }


def calculate_tdee(
    weight_kg: float,
    height_cm: float,
    age: int,
    gender: str,
    activity_level: str = "sedentary"
) -> Dict:
    """
    Tính TDEE (Total Daily Energy Expenditure) - Calories cần mỗi ngày
    
    Args:
        weight_kg: Cân nặng (kg)
        height_cm: Chiều cao (cm)
        age: Tuổi
        gender: "male" hoặc "female"
        activity_level: "sedentary", "light", "moderate", "active", "very_active"
    
    Returns:
        Dict với BMR, TDEE, và calories cho các mục tiêu
    """
    # Bước 1: Tính BMR (Basal Metabolic Rate) theo công thức Mifflin-St Jeor
    if gender == "male":
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:  # female
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    
    # Bước 2: Activity multipliers
    activity_multipliers = {
        "sedentary": 1.2,      # Ít vận động (ngồi nhiều)
        "light": 1.375,        # Nhẹ (tập 1-3 ngày/tuần)
        "moderate": 1.55,      # Trung bình (tập 3-5 ngày/tuần)
        "active": 1.725,       # Năng động (tập 6-7 ngày/tuần)
        "very_active": 1.9     # Rất năng động (vận động viên)
    }
    
    multiplier = activity_multipliers.get(activity_level, 1.2)
    tdee = bmr * multiplier
    
    # Bước 3: Calories cho các mục tiêu
    # Giảm cân an toàn: -500 cal/ngày = -0.5kg/tuần
    # Giảm nhanh: -750 cal/ngày = -0.75kg/tuần
    # Tăng cân: +300 cal/ngày = +0.3kg/tuần
    
    return {
        "bmr": round(bmr, 0),
        "tdee": round(tdee, 0),
        "maintain": round(tdee, 0),
        "lose_slow": round(tdee - 300, 0),      # -0.3kg/tuần (cho người già)
        "lose_moderate": round(tdee - 500, 0),  # -0.5kg/tuần (chuẩn)
        "lose_fast": round(tdee - 750, 0),      # -0.75kg/tuần (nhanh)
        "gain": round(tdee + 300, 0),
        "activity_level": activity_level,
        "note": "Calories tối thiểu: Nam >1500, Nữ >1200"
    }


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


def get_weight_loss_timeline(
    current_weight: float,
    target_weight: float,
    weekly_loss: float = 0.5
) -> Dict:
    """
    Tính timeline giảm cân
    
    Args:
        current_weight: Cân nặng hiện tại (kg)
        target_weight: Cân nặng mục tiêu (kg)
        weekly_loss: Giảm bao nhiêu kg/tuần (mặc định 0.5)
    
    Returns:
        Dict với timeline và milestones
    """
    if current_weight <= target_weight:
        return {
            "error": "Cân nặng mục tiêu phải < cân nặng hiện tại"
        }
    
    if weekly_loss <= 0 or weekly_loss > 1:
        weekly_loss = 0.5  # Default safe rate
    
    total_loss = current_weight - target_weight
    weeks_needed = total_loss / weekly_loss
    months_needed = weeks_needed / 4.33  # Average weeks per month
    
    # Milestones (mỗi 5%)
    milestones = []
    for pct in [5, 10, 15, 20, 25]:
        milestone_weight = current_weight * (1 - pct/100)
        if milestone_weight >= target_weight:
            milestone_weeks = (current_weight - milestone_weight) / weekly_loss
            milestones.append({
                "percentage": pct,
                "weight": round(milestone_weight, 1),
                "weeks": round(milestone_weeks, 0),
                "benefits": get_milestone_benefits(pct)
            })
    
    return {
        "current_weight": current_weight,
        "target_weight": target_weight,
        "total_loss_kg": round(total_loss, 1),
        "weekly_loss_kg": weekly_loss,
        "weeks_needed": round(weeks_needed, 0),
        "months_needed": round(months_needed, 1),
        "estimated_date": f"Khoảng {round(months_needed, 0)} tháng",
        "milestones": milestones,
        "is_safe": weekly_loss <= 1,
        "recommendation": "Giảm 0.5-1kg/tuần là an toàn và bền vững"
    }


def get_milestone_benefits(percentage: int) -> list:
    """Lợi ích khi đạt mốc giảm cân"""
    benefits = {
        5: [
            "Giảm đường huyết",
            "Giảm huyết áp 5-10 mmHg",
            "Cải thiện chất lượng ngủ"
        ],
        10: [
            "Giảm 50% nguy cơ tiểu đường",
            "Giảm đau khớp gối",
            "Tăng năng lượng rõ rệt"
        ],
        15: [
            "Đảo ngược tiền tiểu đường",
            "Có thể ngừng thuốc huyết áp",
            "Cải thiện sức khỏe tim mạch"
        ],
        20: [
            "Tăng tuổi thọ 2-5 năm",
            "Giảm nguy cơ ung thư",
            "Cải thiện sức khỏe tổng thể"
        ],
        25: [
            "Sức khỏe tuyệt vời",
            "Đảo ngược hầu hết biến chứng",
            "Chất lượng cuộc sống cao"
        ]
    }
    return benefits.get(percentage, ["Tiếp tục phát huy!"])


def calculate_calories_deficit(tdee: float, target_loss_per_week: float = 0.5) -> Dict:
    """
    Tính deficit calories cần thiết để giảm cân
    
    Args:
        tdee: Total Daily Energy Expenditure
        target_loss_per_week: Mục tiêu giảm bao nhiêu kg/tuần
    
    Returns:
        Dict với daily calories và deficit
    """
    # 1kg mỡ = 7700 calories
    # Giảm 0.5kg/tuần = 3850 cal/tuần = 550 cal/ngày
    
    calories_per_kg = 7700
    weekly_deficit = target_loss_per_week * calories_per_kg
    daily_deficit = weekly_deficit / 7
    
    target_calories = tdee - daily_deficit
    
    # Không giảm quá thấp (nguy hiểm)
    min_calories = 1500 if target_calories > 1500 else 1200
    if target_calories < min_calories:
        target_calories = min_calories
        actual_deficit = tdee - target_calories
        actual_loss = (actual_deficit * 7) / calories_per_kg
        warning = f"⚠️ TDEE quá thấp. Chỉ có thể giảm {actual_loss:.2f}kg/tuần an toàn"
    else:
        warning = None
    
    return {
        "tdee": round(tdee, 0),
        "target_loss_per_week": target_loss_per_week,
        "daily_deficit": round(daily_deficit, 0),
        "target_daily_calories": round(target_calories, 0),
        "warning": warning,
        "breakdown": {
            "from_diet": round(daily_deficit * 0.7, 0),  # 70% từ ăn
            "from_exercise": round(daily_deficit * 0.3, 0)  # 30% từ tập
        }
    }

