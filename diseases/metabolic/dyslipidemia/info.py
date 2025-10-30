"""
Thông tin về Rối loạn Lipid Máu (Dyslipidemia)
==============================================

Cholesterol, LDL, HDL, Triglyceride

File này tổng hợp thông tin từ 3 modules:
- basic_info: Định nghĩa, giải thích cơ bản, mục tiêu lipid
- diagnosis: Chẩn đoán, phân loại, triệu chứng
- complications: Nguyên nhân, biến chứng, phòng ngừa
"""

from .basic_info import (
    DYSLIPIDEMIA_INFO,
    LIPID_TARGETS
)

from .diagnosis import (
    LIPID_CATEGORIES,
    SYMPTOMS,
    DIAGNOSIS
)

from .complications import (
    CAUSES,
    COMPLICATIONS,
    RELATED_DISEASES,
    PREVENTION
)

# Export all để dùng như cũ: from info import DYSLIPIDEMIA_INFO, ...
__all__ = [
    'DYSLIPIDEMIA_INFO',
    'LIPID_TARGETS',
    'LIPID_CATEGORIES',
    'SYMPTOMS',
    'DIAGNOSIS',
    'CAUSES',
    'COMPLICATIONS',
    'RELATED_DISEASES',
    'PREVENTION'
]
