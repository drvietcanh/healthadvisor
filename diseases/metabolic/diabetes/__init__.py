"""
Module Tiểu Đường - Tái cấu trúc theo module nhỏ
Mỗi file < 300 dòng, dễ quản lý và bảo trì
"""

# Import từ các module con
from .info import (
    DISEASE_INFO,
    BLOOD_SUGAR_LEVELS,
    SYMPTOMS,
    RISK_FACTORS,
    COMPLICATIONS
)

from .medications import MEDICATIONS_SIMPLE

from .insulin import INSULIN_INFO, INSULIN_REGIMENS

from .nutrition import NUTRITION_SIMPLE

from .exercise import EXERCISE_SIMPLE

# Export tất cả để tương thích ngược
__all__ = [
    'DISEASE_INFO',
    'BLOOD_SUGAR_LEVELS',
    'SYMPTOMS',
    'RISK_FACTORS',
    'COMPLICATIONS',
    'MEDICATIONS_SIMPLE',
    'INSULIN_INFO',
    'INSULIN_REGIMENS',
    'NUTRITION_SIMPLE',
    'EXERCISE_SIMPLE',
]

