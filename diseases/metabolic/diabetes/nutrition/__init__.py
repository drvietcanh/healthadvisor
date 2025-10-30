"""
Nutrition module for diabetes - Split into manageable components
"""

from .basics import NUTRITION_BASICS
from .glycemic import GLYCEMIC_INFO
from .recommendations import FOOD_RECOMMENDATIONS

# Export tất cả như một dict để tương thích với code cũ
NUTRITION_SIMPLE = {
    **NUTRITION_BASICS,
    **GLYCEMIC_INFO,
    **FOOD_RECOMMENDATIONS
}

__all__ = ['NUTRITION_SIMPLE', 'NUTRITION_BASICS', 'GLYCEMIC_INFO', 'FOOD_RECOMMENDATIONS']

