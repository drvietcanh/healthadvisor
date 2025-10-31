"""
COPD Assessment - Đánh giá mức độ COPD
=======================================

Backward compatible - Import từ submodule
"""

from .assessment.mmrc_scale import MMRC_SCALE
from .assessment.cat_questionnaire import CAT_QUESTIONNAIRE
from .assessment.gold_classification import GOLD_CLASSIFICATION
from .assessment.six_minute_walk_test import SIX_MINUTE_WALK_TEST
from .assessment.assessment_utils import (
    calculate_cat_score,
    get_mmrc_grade
)

# Export để backward compatible
__all__ = [
    'MMRC_SCALE',
    'CAT_QUESTIONNAIRE',
    'GOLD_CLASSIFICATION',
    'SIX_MINUTE_WALK_TEST',
    'calculate_cat_score',
    'get_mmrc_grade'
]
