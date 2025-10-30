"""
Hypertension module - Split into manageable components
"""

from .info import DISEASE_INFO, BP_CLASSIFICATION, SYMPTOMS, DIAGNOSTIC_STEPS
from .medications import MEDICATIONS
from .lifestyle import NUTRITION_PLAN, EXERCISE_PLAN, LIFESTYLE_MODIFICATIONS, WHEN_TO_SEE_DOCTOR, CONVERSATION_STEPS

# Export all for backward compatibility
__all__ = [
    'DISEASE_INFO',
    'BP_CLASSIFICATION',
    'SYMPTOMS',
    'DIAGNOSTIC_STEPS',
    'MEDICATIONS',
    'NUTRITION_PLAN',
    'EXERCISE_PLAN',
    'LIFESTYLE_MODIFICATIONS',
    'WHEN_TO_SEE_DOCTOR',
    'CONVERSATION_STEPS'
]

