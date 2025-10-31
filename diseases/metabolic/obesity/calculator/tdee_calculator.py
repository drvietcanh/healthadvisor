"""
TDEE Calculator - Tính Total Daily Energy Expenditure
"""

from typing import Dict


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


__all__ = ['calculate_tdee', 'calculate_calories_deficit']
