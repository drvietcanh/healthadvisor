"""
Exercise Module - Tập luyện và vận động cho béo phì
Split into manageable components
"""

from .activities_data import EXERCISES_CALORIES
from .exercise_levels import EXERCISE_LEVELS
from .exercise_calculators import (
    calculate_calories_burned,
    get_exercise_plan,
    get_food_equivalents
)
from .safety_tips import (
    get_safe_exercise_tips,
    get_exercise_by_location
)

__all__ = [
    'EXERCISES_CALORIES',
    'EXERCISE_LEVELS',
    'calculate_calories_burned',
    'get_exercise_plan',
    'get_safe_exercise_tips',
    'get_exercise_by_location',
    'get_food_equivalents'
]
