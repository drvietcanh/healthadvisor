"""
Nutrition Module - Dinh dưỡng và calories cho béo phì
Split into manageable components
"""

from .food_database import VIETNAMESE_FOODS, FOOD_CATEGORIES
from .nutrition_calculators import (
    calculate_daily_calories,
    get_meal_plan,
    find_food_calories,
    calculate_meal_calories
)
from .nutrition_tips import get_nutrition_tips

__all__ = [
    'VIETNAMESE_FOODS',
    'FOOD_CATEGORIES',
    'calculate_daily_calories',
    'get_meal_plan',
    'get_nutrition_tips',
    'find_food_calories',
    'calculate_meal_calories'
]
