"""
Obesity Calculator Module - Các công cụ tính toán cho béo phì
Split into manageable components
"""

from .bmi_calculator import (
    calculate_bmi,
    get_bmi_category,
    calculate_ideal_weight
)
from .tdee_calculator import (
    calculate_tdee,
    calculate_calories_deficit
)
from .body_metrics import (
    calculate_whr,
    calculate_body_fat_percentage
)
from .weight_timeline import (
    get_weight_loss_timeline,
    get_milestone_benefits
)

__all__ = [
    'calculate_bmi',
    'calculate_tdee',
    'calculate_whr',
    'calculate_body_fat_percentage',
    'calculate_ideal_weight',
    'get_bmi_category',
    'get_weight_loss_timeline',
    'calculate_calories_deficit',
    'get_milestone_benefits'
]
