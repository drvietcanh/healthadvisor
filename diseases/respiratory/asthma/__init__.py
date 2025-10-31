"""
Asthma Module - Hen Suyễn
==========================

Module cung cấp thông tin toàn diện về hen suyễn
"""

from .basic_info import ASTHMA_INFO
from .causes import CAUSES
from .symptoms import SYMPTOMS
from .triggers import TRIGGERS
from .severity import SEVERITY_CLASSIFICATION
from .medications import (
    QUICK_RELIEF_MEDICATIONS,
    CONTROLLER_MEDICATIONS,
    INHALER_TECHNIQUE,
    ACTION_PLAN
)
from .management import (
    PREVENTION,
    HOME_MONITORING,
    LIFESTYLE,
    EXACERBATION_MANAGEMENT
)

__all__ = [
    'ASTHMA_INFO',
    'CAUSES',
    'SYMPTOMS',
    'TRIGGERS',
    'SEVERITY_CLASSIFICATION',
    'QUICK_RELIEF_MEDICATIONS',
    'CONTROLLER_MEDICATIONS',
    'INHALER_TECHNIQUE',
    'ACTION_PLAN',
    'PREVENTION',
    'HOME_MONITORING',
    'LIFESTYLE',
    'EXACERBATION_MANAGEMENT',
]

