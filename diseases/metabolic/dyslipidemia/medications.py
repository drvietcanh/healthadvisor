"""
Medications - Thuốc điều trị rối loạn lipid máu
================================================

Thông tin về các loại thuốc giảm mỡ máu
Backward compatible - Import từ submodule
"""

from .medications.statins import STATINS
from .medications.fibrates import FIBRATES
from .medications.other_medications import OTHER_MEDICATIONS
from .medications.treatment_protocols import TREATMENT_PROTOCOLS
from .medications.medication_utils import (
    get_medication_info as _get_medication_info,
    get_side_effects as _get_side_effects,
    get_treatment_recommendation as _get_treatment_recommendation
)

# Export để backward compatible
__all__ = [
    'STATINS',
    'FIBRATES',
    'OTHER_MEDICATIONS',
    'TREATMENT_PROTOCOLS',
    'get_medication_info',
    'get_side_effects',
    'get_treatment_recommendation'
]


# Wrapper functions để backward compatible
def get_medication_info(medication_name: str):
    """Lấy thông tin chi tiết về thuốc"""
    return _get_medication_info(
        medication_name,
        STATINS["common_statins"],
        FIBRATES["common_fibrates"],
        OTHER_MEDICATIONS
    )


def get_side_effects(medication_type: str = "statin"):
    """Lấy danh sách tác dụng phụ"""
    return _get_side_effects(medication_type, STATINS, FIBRATES)


def get_treatment_recommendation(ldl: float, has_diabetes: bool = False,
                                 has_cvd: bool = False, triglyceride: float = 0):
    """Đề xuất phác đồ điều trị dựa trên LDL và yếu tố nguy cơ"""
    return _get_treatment_recommendation(
        ldl, has_diabetes, has_cvd, triglyceride, TREATMENT_PROTOCOLS
    )
