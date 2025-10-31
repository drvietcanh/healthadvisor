"""
Info Module - Thông tin về béo phì
Split into manageable components
"""

from .disease_info import OBESITY_INFO, BMI_CATEGORIES_ASIAN, CAUSES
from .health_risks import HEALTH_RISKS
from .prevention_tips import PREVENTION, WEIGHT_LOSS_BENEFITS
from .related_diseases import RELATED_DISEASES

__all__ = [
    'OBESITY_INFO',
    'BMI_CATEGORIES_ASIAN',
    'CAUSES',
    'HEALTH_RISKS',
    'PREVENTION',
    'RELATED_DISEASES',
    'WEIGHT_LOSS_BENEFITS'
]
