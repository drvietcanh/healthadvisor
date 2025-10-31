"""
Asthma (Hen Suyễn) - Thông tin cơ bản
=====================================

Ngôn ngữ bình dân, dễ hiểu cho người dân

File này import và re-export tất cả thông tin từ các modules con
để giữ backward compatibility với code cũ.
"""

# Import từ các modules đã tách
from .basic_info import ASTHMA_INFO
from .causes import CAUSES
from .symptoms import SYMPTOMS
from .triggers import TRIGGERS
from .severity import SEVERITY_CLASSIFICATION

# Re-export để giữ backward compatibility
__all__ = [
    'ASTHMA_INFO',
    'CAUSES',
    'SYMPTOMS',
    'TRIGGERS',
    'SEVERITY_CLASSIFICATION',
]
