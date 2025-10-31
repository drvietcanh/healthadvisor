"""
COPD Exercises - Bài tập cho COPD
==================================

Backward compatible - Import từ submodule
"""

from .exercises.exercise_benefits import EXERCISE_BENEFITS
from .exercises.exercise_principles import EXERCISE_PRINCIPLES
from .exercises.breathing_techniques import BREATHING_TECHNIQUES
from .exercises.aerobic_exercises import AEROBIC_EXERCISES
from .exercises.strength_flexibility import STRENGTH_EXERCISES, FLEXIBILITY_EXERCISES
from .exercises.daily_activities import DAILY_ACTIVITIES
from .exercises.four_week_program import FOUR_WEEK_PROGRAM

# Export để backward compatible
__all__ = [
    'EXERCISE_BENEFITS',
    'EXERCISE_PRINCIPLES',
    'BREATHING_TECHNIQUES',
    'AEROBIC_EXERCISES',
    'STRENGTH_EXERCISES',
    'FLEXIBILITY_EXERCISES',
    'DAILY_ACTIVITIES',
    'FOUR_WEEK_PROGRAM'
]
