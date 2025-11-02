"""
Hướng dẫn sơ cứu nhanh cho người già

File này tổng hợp từ các modules:
- first_aid_cardiovascular: Tim mạch, thần kinh
- first_aid_trauma: Chấn thương (bỏng, chảy máu, ngã, cột sống)
- first_aid_pediatric: Nhi khoa (hóc dị vật)
- first_aid_environmental: Môi trường (đuối nước, điện giật)
- first_aid_medical: Y khoa (hạ đường huyết, ngộ độc)
"""

from .first_aid_cardiovascular import FIRST_AID_CARDIOVASCULAR
from .first_aid_trauma import FIRST_AID_TRAUMA
from .first_aid_pediatric import FIRST_AID_PEDIATRIC
from .first_aid_environmental import FIRST_AID_ENVIRONMENTAL
from .first_aid_medical import FIRST_AID_MEDICAL
from .first_aid_additional import FIRST_AID_ADDITIONAL
from .first_aid_additional2 import FIRST_AID_ADDITIONAL2
from .first_aid_additional3 import FIRST_AID_ADDITIONAL3

# Tổng hợp tất cả
FIRST_AID_GUIDES = {}
FIRST_AID_GUIDES.update(FIRST_AID_CARDIOVASCULAR)
FIRST_AID_GUIDES.update(FIRST_AID_TRAUMA)
FIRST_AID_GUIDES.update(FIRST_AID_PEDIATRIC)
FIRST_AID_GUIDES.update(FIRST_AID_ENVIRONMENTAL)
FIRST_AID_GUIDES.update(FIRST_AID_MEDICAL)
FIRST_AID_GUIDES.update(FIRST_AID_ADDITIONAL)
FIRST_AID_GUIDES.update(FIRST_AID_ADDITIONAL2)
FIRST_AID_GUIDES.update(FIRST_AID_ADDITIONAL3)


def get_first_aid_guide(condition):
    """Lấy hướng dẫn sơ cứu theo tình trạng"""
    return FIRST_AID_GUIDES.get(condition)
