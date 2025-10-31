"""
Spine Diseases Module
Bệnh cột sống: Đau thắt lưng, thoát vị đĩa đệm, thoái hóa cột sống
"""

from .back_pain import (
    BACK_PAIN_INFO,
    BACK_PAIN_CAUSES,
    BACK_PAIN_MANAGEMENT,
    BACK_PAIN_EXERCISES
)

from .herniated_disc import (
    HERNIATED_DISC_INFO,
    HERNIATED_DISC_SYMPTOMS,
    HERNIATED_DISC_TREATMENT
)

from .spinal_management import (
    SPINAL_POSTURE,
    SPINAL_EXERCISES,
    SPINAL_PROTECTION
)

__all__ = [
    # Back Pain
    'BACK_PAIN_INFO',
    'BACK_PAIN_CAUSES',
    'BACK_PAIN_MANAGEMENT',
    'BACK_PAIN_EXERCISES',
    
    # Herniated Disc
    'HERNIATED_DISC_INFO',
    'HERNIATED_DISC_SYMPTOMS',
    'HERNIATED_DISC_TREATMENT',
    
    # Spinal Management
    'SPINAL_POSTURE',
    'SPINAL_EXERCISES',
    'SPINAL_PROTECTION'
]

