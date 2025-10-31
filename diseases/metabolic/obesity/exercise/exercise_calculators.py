"""
Exercise Calculators - Tính toán calories và kế hoạch tập luyện
"""

from typing import Dict, List
from .activities_data import EXERCISES_CALORIES
from .exercise_levels import EXERCISE_LEVELS


def get_food_equivalents(calories: float) -> List[str]:
    """Tương đương với món ăn Việt Nam"""
    equivalents = []
    
    foods = [
        (400, "1 bát phở"),
        (350, "1 bánh mì thịt"),
        (200, "1 bát cơm"),
        (150, "1 ly cà phê sữa"),
        (100, "1 hộp sữa chua"),
        (70, "1 quả trứng luộc"),
    ]
    
    for cal, food in foods:
        if calories >= cal * 0.9:  # Allow 10% tolerance
            portions = calories / cal
            if portions >= 1:
                equivalents.append(f"{portions:.1f} {food}")
    
    return equivalents[:3]  # Top 3


def calculate_calories_burned(
    activity: str,
    duration_minutes: int,
    weight_kg: float = 70
) -> Dict:
    """
    Tính calories đốt cháy
    
    Args:
        activity: Tên hoạt động
        duration_minutes: Thời gian (phút)
        weight_kg: Cân nặng (kg) - mặc định 70kg
    
    Returns:
        Dict với calories burned và thông tin
    """
    # Tìm activity trong database
    base_calories_per_hour = None
    category_name = None
    
    for category_id, category_data in EXERCISES_CALORIES.items():
        if activity in category_data["activities"]:
            base_calories_per_hour = category_data["activities"][activity]
            category_name = category_data["name"]
            break
    
    if base_calories_per_hour is None:
        return {"error": f"Không tìm thấy hoạt động: {activity}"}
    
    # Điều chỉnh theo cân nặng (base = 70kg)
    # Calories tỷ lệ thuận với cân nặng
    weight_multiplier = weight_kg / 70
    adjusted_calories_per_hour = base_calories_per_hour * weight_multiplier
    
    # Tính theo thời gian
    calories_burned = (adjusted_calories_per_hour / 60) * duration_minutes
    
    # Tương đương món ăn
    food_equivalents = get_food_equivalents(calories_burned)
    
    return {
        "activity": activity,
        "category": category_name,
        "duration_minutes": duration_minutes,
        "weight_kg": weight_kg,
        "calories_burned": round(calories_burned, 0),
        "base_rate": base_calories_per_hour,
        "adjusted_rate": round(adjusted_calories_per_hour, 0),
        "food_equivalents": food_equivalents,
        "note": f"Người {weight_kg}kg {activity} {duration_minutes} phút"
    }


def get_exercise_plan(
    level: str,
    goal: str = "lose_weight",
    available_time: int = 30
) -> Dict:
    """
    Tạo kế hoạch tập luyện
    
    Args:
        level: "beginner", "intermediate", "advanced"
        goal: "lose_weight", "maintain", "build_muscle"
        available_time: Thời gian có (phút/ngày)
    
    Returns:
        Dict với weekly plan
    """
    level_info = EXERCISE_LEVELS.get(level, EXERCISE_LEVELS["beginner"])
    
    if goal == "lose_weight":
        # Focus cardio
        weekly_plan = {
            "monday": {
                "activity": "Đi bộ nhanh",
                "duration": min(available_time, 30),
                "type": "cardio",
                "note": "Khởi động tuần mới"
            },
            "tuesday": {
                "activity": "Làm vườn hoặc việc nhà",
                "duration": 30,
                "type": "daily",
                "note": "Hoạt động nhẹ"
            },
            "wednesday": {
                "activity": "Yoga hoặc Thái cực",
                "duration": min(available_time, 30),
                "type": "gentle",
                "note": "Thư giãn, dẻo dai"
            },
            "thursday": {
                "activity": "Đạp xe hoặc Bơi",
                "duration": min(available_time, 40),
                "type": "cardio",
                "note": "Đốt mỡ hiệu quả"
            },
            "friday": {
                "activity": "Đi bộ + Leo cầu thang",
                "duration": 30,
                "type": "cardio",
                "note": "Kết hợp nhiều động tác"
            },
            "saturday": {
                "activity": "Thể thao (cầu lông, bóng bàn...)",
                "duration": 45,
                "type": "sports",
                "note": "Vui vẻ, giao lưu"
            },
            "sunday": {
                "activity": "Nghỉ ngơi hoặc đi dạo nhẹ",
                "duration": 20,
                "type": "rest",
                "note": "Phục hồi cơ thể"
            }
        }
    
    elif goal == "maintain":
        weekly_plan = {
            "monday": {"activity": "Đi bộ", "duration": 30, "type": "cardio"},
            "wednesday": {"activity": "Yoga", "duration": 30, "type": "gentle"},
            "friday": {"activity": "Thể thao", "duration": 30, "type": "sports"},
            "sunday": {"activity": "Đi dạo", "duration": 30, "type": "gentle"}
        }
    
    else:  # build_muscle
        weekly_plan = {
            "monday": {"activity": "Tập tạ", "duration": 45, "type": "gym"},
            "tuesday": {"activity": "Cardio nhẹ", "duration": 20, "type": "cardio"},
            "wednesday": {"activity": "Tập tạ", "duration": 45, "type": "gym"},
            "thursday": {"activity": "Nghỉ", "duration": 0, "type": "rest"},
            "friday": {"activity": "Tập tạ", "duration": 45, "type": "gym"},
            "saturday": {"activity": "Cardio", "duration": 30, "type": "cardio"},
            "sunday": {"activity": "Nghỉ", "duration": 0, "type": "rest"}
        }
    
    # Tính tổng
    total_minutes = sum(day["duration"] for day in weekly_plan.values())
    estimated_calories = total_minutes * 5  # Rough estimate ~5 cal/min
    
    return {
        "level": level_info["name"],
        "goal": goal,
        "weekly_plan": weekly_plan,
        "total_minutes_per_week": total_minutes,
        "estimated_calories_burned": round(estimated_calories, 0),
        "tips": level_info["notes"]
    }


__all__ = ['calculate_calories_burned', 'get_exercise_plan', 'get_food_equivalents']
