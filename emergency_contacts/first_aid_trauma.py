"""
Sơ cứu Chấn Thương
Trauma First Aid (Bỏng, Chảy máu, Ngã, Chấn thương cột sống)

REFACTORED: Tách thành 2 modules nhỏ (a, b)
"""

from .first_aid_trauma_a import FIRST_AID_TRAUMA_A
from .first_aid_trauma_b import FIRST_AID_TRAUMA_B

# Tổng hợp từ 2 modules
FIRST_AID_TRAUMA = {}
FIRST_AID_TRAUMA.update(FIRST_AID_TRAUMA_A)
FIRST_AID_TRAUMA.update(FIRST_AID_TRAUMA_B)
