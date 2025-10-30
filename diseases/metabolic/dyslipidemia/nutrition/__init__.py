"""
Nutrition Module for Dyslipidemia
==================================

Tổng hợp tất cả thông tin dinh dưỡng cho người rối loạn lipid máu
"""

from .food_classification import (
    FOOD_SAFETY_CLASSIFICATION,
    QUICK_REFERENCE_TABLE
)

from .fat_types import (
    FAT_TYPES_EXPLANATION,
    FAT_COMPARISON
)

from .vietnamese_foods import (
    GOOD_FOODS,
    BAD_FOODS,
    CHOLESTEROL_LOWERING_FOODS
)

from .meal_plans import (
    get_diet_plan_vietnam,
    get_nutrition_tips
)

from .cholesterol_foods import (
    CHOLESTEROL_FOOD_CLASSIFICATION,
    VIETNAMESE_DISHES_CHOLESTEROL,
    COOKING_TIPS_REDUCE_CHOLESTEROL,
    KEY_CHOLESTEROL_MESSAGES
)

__all__ = [
    # Food Classification
    'FOOD_SAFETY_CLASSIFICATION',
    'QUICK_REFERENCE_TABLE',
    
    # Fat Types
    'FAT_TYPES_EXPLANATION',
    'FAT_COMPARISON',
    
    # Vietnamese Foods
    'GOOD_FOODS',
    'BAD_FOODS',
    'CHOLESTEROL_LOWERING_FOODS',
    
    # Cholesterol Foods
    'CHOLESTEROL_FOOD_CLASSIFICATION',
    'VIETNAMESE_DISHES_CHOLESTEROL',
    'COOKING_TIPS_REDUCE_CHOLESTEROL',
    'KEY_CHOLESTEROL_MESSAGES',
    
    # Meal Plans
    'get_diet_plan_vietnam',
    'get_nutrition_tips',
]

