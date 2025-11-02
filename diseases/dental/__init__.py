"""
Dental Health Module - Răng Hàm Mặt
====================================

Module cung cấp thông tin về các bệnh răng miệng phổ biến
"""

from .gingivitis import GINGIVITIS_INFO
from .periodontitis import PERIODONTITIS_INFO
from .toothache import TOOTHACHE_INFO
from .tooth_loss import TOOTH_LOSS_INFO
from .xerostomia import XEROSTOMIA_INFO

__all__ = [
    'GINGIVITIS_INFO',
    'PERIODONTITIS_INFO',
    'TOOTHACHE_INFO',
    'TOOTH_LOSS_INFO',
    'XEROSTOMIA_INFO',
]

