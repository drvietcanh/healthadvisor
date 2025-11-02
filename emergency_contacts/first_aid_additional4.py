"""
Sơ cứu Bổ Sung 4 - Các tình huống cấp cứu quan trọng cho người già
Additional Emergency Situations 4

REFACTORED: Tách thành 2 modules nhỏ (4a, 4b)
"""

from .first_aid_additional4a import FIRST_AID_ADDITIONAL4A
from .first_aid_additional4b import FIRST_AID_ADDITIONAL4B

# Tổng hợp từ 2 modules
FIRST_AID_ADDITIONAL4 = {}
FIRST_AID_ADDITIONAL4.update(FIRST_AID_ADDITIONAL4A)
FIRST_AID_ADDITIONAL4.update(FIRST_AID_ADDITIONAL4B)
