"""
COPD - Bệnh Phổi Tắc Nghẽn Mạn Tính
====================================

Thông tin cơ bản về COPD (Chronic Obstructive Pulmonary Disease)

File này tổng hợp thông tin từ 3 modules:
- basic_info: Định nghĩa, nguyên nhân, triệu chứng
- diagnosis: Chẩn đoán, biến chứng
- management: Phòng ngừa, so sánh COPD vs Hen, bệnh liên quan
"""

from typing import Dict, List

from .basic_info import (
    COPD_INFO,
    CAUSES,
    SYMPTOMS
)

from .diagnosis import (
    COMPLICATIONS,
    DIAGNOSIS
)

from .prevention_info import (
    PREVENTION,
    COPD_VS_ASTHMA,
    RELATED_DISEASES
)

# Export all để dùng như cũ
__all__ = [
    'COPD_INFO',
    'CAUSES',
    'SYMPTOMS',
    'COMPLICATIONS',
    'DIAGNOSIS',
    'PREVENTION',
    'COPD_VS_ASTHMA',
    'RELATED_DISEASES'
]
