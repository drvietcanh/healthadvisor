"""
Heart Failure module - Split into manageable components
"""

from .info import DISEASE_INFO, SYMPTOMS_SIMPLE
from .medications import MEDICATIONS_SIMPLE
from .daily_management import (
    NUTRITION_SIMPLE,
    EXERCISE_SIMPLE,
    HOME_MONITORING_SIMPLE,
    LIVING_WITH_HF,
    FAQ_SIMPLE,
    CHATBOT_QUESTIONS
)

# Export all for backward compatibility
__all__ = [
    'DISEASE_INFO',
    'SYMPTOMS_SIMPLE',
    'MEDICATIONS_SIMPLE',
    'NUTRITION_SIMPLE',
    'EXERCISE_SIMPLE',
    'HOME_MONITORING_SIMPLE',
    'LIVING_WITH_HF',
    'FAQ_SIMPLE',
    'CHATBOT_QUESTIONS'
]

