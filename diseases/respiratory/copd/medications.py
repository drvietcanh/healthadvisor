"""
COPD Medications - Thuốc điều trị COPD
=======================================

Hướng dẫn về các loại thuốc điều trị COPD

File này import và re-export tất cả thông tin từ các modules con
để giữ backward compatibility với code cũ.
"""

# Import từ các modules đã tách
from .treatment_principles import TREATMENT_PRINCIPLES
from .bronchodilators import BRONCHODILATORS
from .corticosteroids import INHALED_CORTICOSTEROIDS
from .other_medications import OTHER_MEDICATIONS
from .oxygen_therapy import OXYGEN_THERAPY
from .inhaler_technique import INHALER_TECHNIQUE

# Re-export để giữ backward compatibility
__all__ = [
    'TREATMENT_PRINCIPLES',
    'BRONCHODILATORS',
    'INHALED_CORTICOSTEROIDS',
    'OTHER_MEDICATIONS',
    'OXYGEN_THERAPY',
    'INHALER_TECHNIQUE',
]
