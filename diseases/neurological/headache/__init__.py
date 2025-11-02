"""
Đau đầu (Headache/Migraine) Module
====================================

Module cung cấp thông tin toàn diện về đau đầu
"""

from .basic_info import HEADACHE_INFO
from .types import HEADACHE_TYPES, DANGEROUS_SIGNS
from .treatment import TREATMENT

__all__ = [
    'HEADACHE_INFO',
    'HEADACHE_TYPES',
    'DANGEROUS_SIGNS',
    'TREATMENT',
]

