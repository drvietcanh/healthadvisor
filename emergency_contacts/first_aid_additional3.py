"""
Sơ cứu Bổ Sung 3 - Các tình huống cấp cứu quan trọng
Additional Emergency Situations 3

REFACTORED: Tách thành 3 modules nhỏ (3a, 3b, 3c)
"""

from .first_aid_additional3a import FIRST_AID_ADDITIONAL3A
from .first_aid_additional3b import FIRST_AID_ADDITIONAL3B
from .first_aid_additional3c import FIRST_AID_ADDITIONAL3C

# Tổng hợp từ 3 modules
FIRST_AID_ADDITIONAL3 = {}
FIRST_AID_ADDITIONAL3.update(FIRST_AID_ADDITIONAL3A)
FIRST_AID_ADDITIONAL3.update(FIRST_AID_ADDITIONAL3B)
FIRST_AID_ADDITIONAL3.update(FIRST_AID_ADDITIONAL3C)
