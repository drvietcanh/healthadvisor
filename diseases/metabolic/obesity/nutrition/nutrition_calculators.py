"""
Nutrition Calculators - Tính calories và meal planning
"""

from typing import Dict, List, Optional
from .food_database import VIETNAMESE_FOODS


def calculate_daily_calories(
    tdee: float,
    goal: str = "maintain"
) -> Dict:
    """
    Tính calories cần thiết mỗi ngày
    
    Args:
        tdee: Total Daily Energy Expenditure
        goal: "lose_slow", "lose_moderate", "lose_fast", "maintain", "gain"
    
    Returns:
        Dict với calories và breakdown
    """
    goals_deficit = {
        "lose_slow": -300,      # -0.3kg/tuần (cho người già)
        "lose_moderate": -500,  # -0.5kg/tuần
        "lose_fast": -750,      # -0.75kg/tuần
        "maintain": 0,
        "gain": +300
    }
    
    deficit = goals_deficit.get(goal, 0)
    target_calories = tdee + deficit
    
    # Không < 1200 cal cho nữ, 1500 cho nam
    min_calories = 1200
    if target_calories < min_calories:
        target_calories = min_calories
    
    # Chia calories theo bữa (VN thường ăn 3 bữa chính)
    breakfast = target_calories * 0.30  # 30% sáng
    lunch = target_calories * 0.40      # 40% trưa
    dinner = target_calories * 0.25     # 25% tối
    snacks = target_calories * 0.05     # 5% vặt
    
    return {
        "daily_calories": round(target_calories, 0),
        "breakfast": round(breakfast, 0),
        "lunch": round(lunch, 0),
        "dinner": round(dinner, 0),
        "snacks": round(snacks, 0),
        "macros": {
            "protein": round(target_calories * 0.30 / 4, 0),  # 30% protein, 4cal/g
            "carbs": round(target_calories * 0.40 / 4, 0),    # 40% carbs, 4cal/g
            "fat": round(target_calories * 0.30 / 9, 0),      # 30% fat, 9cal/g
        },
        "note": "Tỷ lệ 30-40-30 (P-C-F) phù hợp giảm cân"
    }


def get_meal_plan(daily_calories: float, meal_type: str = "balanced") -> Dict:
    """
    Gợi ý thực đơn theo calories
    
    Args:
        daily_calories: Calories mục tiêu mỗi ngày
        meal_type: "balanced", "low_carb", "vegetarian"
    
    Returns:
        Dict với meal suggestions
    """
    breakfast_cal = daily_calories * 0.30
    lunch_cal = daily_calories * 0.40
    dinner_cal = daily_calories * 0.25
    
    # Gợi ý món ăn phù hợp calories
    if meal_type == "balanced":
        return {
            "breakfast": {
                "target_calories": round(breakfast_cal, 0),
                "suggestions": [
                    "Phở gà (350 cal) + Cà phê đen (5 cal)",
                    "Bánh mì pate (280 cal) + Sữa chua (100 cal)",
                    "Cháo gà (180 cal) + Trứng luộc (70 cal) + Trái cây (80 cal)"
                ]
            },
            "lunch": {
                "target_calories": round(lunch_cal, 0),
                "suggestions": [
                    "Cơm gà (550 cal) + Rau luộc (50 cal)",
                    "Bún thịt nướng (480 cal) + Gỏi cuốn 2 cuốn (140 cal)",
                    "Cơm + Cá kho (200 cal) + Canh chua (120 cal) + Rau (50 cal)"
                ]
            },
            "dinner": {
                "target_calories": round(dinner_cal, 0),
                "suggestions": [
                    "Cháo gà (180 cal) + Rau luộc (50 cal)",
                    "Bún riêu (420 cal)",
                    "Cơm (200 cal) + Đậu hũ chiên (180 cal) + Canh (120 cal)"
                ]
            },
            "snacks": {
                "suggestions": [
                    "Trái cây (80 cal)",
                    "Sữa chua (100 cal)",
                    "Gỏi cuốn 1 cuốn (70 cal)"
                ]
            }
        }
    
    elif meal_type == "low_carb":
        return {
            "note": "Giảm tinh bột, tăng protein",
            "breakfast": {
                "suggestions": [
                    "Trứng chiên 2 quả (220 cal) + Rau luộc (50 cal)",
                    "Cháo gà (180 cal)"
                ]
            },
            "lunch": {
                "suggestions": [
                    "Thịt/Cá nướng (250 cal) + Rau nhiều (100 cal) + Cơm ít (100 cal)",
                    "Lẩu (450 cal) - ăn ít bún"
                ]
            },
            "dinner": {
                "suggestions": [
                    "Gỏi cuốn (140 cal) + Canh (120 cal)",
                    "Salad gà (300 cal)"
                ]
            }
        }
    
    else:  # vegetarian
        return {
            "note": "Chay - tập trung đậu hũ, nấm, rau",
            "breakfast": {
                "suggestions": [
                    "Xôi xéo (320 cal)",
                    "Bánh cuốn chay (200 cal) + Nước dừa (50 cal)"
                ]
            },
            "lunch": {
                "suggestions": [
                    "Cơm (200 cal) + Đậu hũ chiên (180 cal) + Rau (100 cal) + Canh (80 cal)",
                    "Bún riêu chay (380 cal)"
                ]
            },
            "dinner": {
                "suggestions": [
                    "Canh chua chay (100 cal) + Rau luộc (50 cal) + Cơm ít (150 cal)"
                ]
            }
        }


def find_food_calories(food_name: str) -> Optional[Dict]:
    """
    Tìm calories của món ăn
    
    Args:
        food_name: Tên món ăn
    
    Returns:
        Dict với calories và macros, hoặc None
    """
    food_name_lower = food_name.lower()
    
    for category_id, category_data in VIETNAMESE_FOODS.items():
        for food, nutrition in category_data["foods"].items():
            if food.lower() in food_name_lower or food_name_lower in food.lower():
                return {
                    "name": food,
                    "category": category_data["name"],
                    **nutrition
                }
    
    return None


def calculate_meal_calories(foods: List[str]) -> Dict:
    """
    Tính tổng calories của một bữa ăn
    
    Args:
        foods: Danh sách các món ăn
    
    Returns:
        Dict với total calories và breakdown
    """
    total_cal = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0
    found_foods = []
    not_found = []
    
    for food in foods:
        result = find_food_calories(food)
        if result:
            total_cal += result["calories"]
            total_protein += result["protein"]
            total_carbs += result["carbs"]
            total_fat += result["fat"]
            found_foods.append(result)
        else:
            not_found.append(food)
    
    return {
        "total_calories": total_cal,
        "macros": {
            "protein": round(total_protein, 1),
            "carbs": round(total_carbs, 1),
            "fat": round(total_fat, 1)
        },
        "foods": found_foods,
        "not_found": not_found,
        "count": len(found_foods)
    }


__all__ = [
    'calculate_daily_calories',
    'get_meal_plan',
    'find_food_calories',
    'calculate_meal_calories'
]
