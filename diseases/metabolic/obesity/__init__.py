"""
Obesity (Béo phì) Module
========================

Module cung cấp thông tin, công cụ đánh giá và quản lý béo phì.

BÉO PHÌ là gốc rễ của Hội chứng Chuyển hóa (Metabolic Syndrome),
liên quan trực tiếp đến:
- Tiểu đường type 2
- Cao huyết áp
- Rối loạn lipid máu
- Bệnh tim mạch
- Thoái hóa khớp
- COPD
- Gút
"""

from .info import (
    OBESITY_INFO,
    BMI_CATEGORIES_ASIAN,
    HEALTH_RISKS,
    CAUSES,
    PREVENTION,
    RELATED_DISEASES
)

from .calculators import (
    calculate_bmi,
    calculate_tdee,
    calculate_whr,
    calculate_body_fat_percentage,
    calculate_ideal_weight,
    get_bmi_category,
    get_weight_loss_timeline
)

from .nutrition import (
    VIETNAMESE_FOODS,
    FOOD_CATEGORIES,
    calculate_daily_calories,
    get_meal_plan,
    get_nutrition_tips
)

from .exercise import (
    EXERCISES_CALORIES,
    EXERCISE_LEVELS,
    calculate_calories_burned,
    get_exercise_plan,
    get_safe_exercise_tips
)

from .goals import (
    create_weight_loss_goal,
    calculate_progress,
    get_milestones,
    get_motivation_message
)

__all__ = [
    # Info
    'OBESITY_INFO',
    'BMI_CATEGORIES_ASIAN',
    'HEALTH_RISKS',
    'CAUSES',
    'PREVENTION',
    'RELATED_DISEASES',
    
    # Calculators
    'calculate_bmi',
    'calculate_tdee',
    'calculate_whr',
    'calculate_body_fat_percentage',
    'calculate_ideal_weight',
    'get_bmi_category',
    'get_weight_loss_timeline',
    
    # Nutrition
    'VIETNAMESE_FOODS',
    'FOOD_CATEGORIES',
    'calculate_daily_calories',
    'get_meal_plan',
    'get_nutrition_tips',
    
    # Exercise
    'EXERCISES_CALORIES',
    'EXERCISE_LEVELS',
    'calculate_calories_burned',
    'get_exercise_plan',
    'get_safe_exercise_tips',
    
    # Goals
    'create_weight_loss_goal',
    'calculate_progress',
    'get_milestones',
    'get_motivation_message',
]

