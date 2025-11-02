"""
Suy Thận Mạn (Chronic Kidney Disease) Module
=============================================

Module cung cấp thông tin toàn diện về suy thận mạn tính
"""

from .basic_info import CKD_INFO
from .symptoms import SYMPTOMS
from .causes import CAUSES
from .treatment import TREATMENT
from .dialysis import DIALYSIS
from .diet import DIET

__all__ = [
    'CKD_INFO',
    'SYMPTOMS',
    'CAUSES',
    'TREATMENT',
    'DIALYSIS',
    'DIET',
]

