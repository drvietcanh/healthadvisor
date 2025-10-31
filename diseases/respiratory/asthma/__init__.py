"""
Asthma Module - Hen Suyễn
==========================

Module cung cấp thông tin toàn diện về hen suyễn
"""

from .basic_info import ASTHMA_INFO

from .causes import CAUSES

from .symptoms import SYMPTOMS

from .triggers import TRIGGERS

from .severity import SEVERITY_CLASSIFICATION

__all__ = [
    'ASTHMA_INFO',
    'CAUSES',
    'SYMPTOMS',
    'TRIGGERS',
    'SEVERITY_CLASSIFICATION',
]

