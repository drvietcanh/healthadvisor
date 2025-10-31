"""
Medications Module - Thuốc điều trị rối loạn lipid máu
"""

from .statins import STATINS
from .fibrates import FIBRATES
from .other_medications import OTHER_MEDICATIONS
from .treatment_protocols import TREATMENT_PROTOCOLS
from .medication_utils import (
    get_medication_info,
    get_side_effects,
    get_treatment_recommendation
)

__all__ = [
    'STATINS',
    'FIBRATES',
    'OTHER_MEDICATIONS',
    'TREATMENT_PROTOCOLS',
    'get_medication_info',
    'get_side_effects',
    'get_treatment_recommendation'
]

