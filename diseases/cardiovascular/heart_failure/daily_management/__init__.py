"""
Heart Failure Daily Management Components
Tách từ management.py (384 dòng) thành các modules
"""

from .nutrition import NUTRITION_SIMPLE
from .exercise import EXERCISE_SIMPLE
from .monitoring import HOME_MONITORING_SIMPLE
from .lifestyle import LIVING_WITH_HF
from .faq import FAQ_SIMPLE, CHATBOT_QUESTIONS

__all__ = [
    'NUTRITION_SIMPLE',
    'EXERCISE_SIMPLE',
    'HOME_MONITORING_SIMPLE',
    'LIVING_WITH_HF',
    'FAQ_SIMPLE',
    'CHATBOT_QUESTIONS',
]

