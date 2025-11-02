"""
Viêm phổi (Pneumonia) Module
=============================

Module cung cấp thông tin toàn diện về viêm phổi
"""

from .basic_info import PNEUMONIA_INFO
from .causes import CAUSES
from .symptoms import SYMPTOMS
from .diagnosis import DIAGNOSIS, COMPLICATIONS
from .treatment import TREATMENT
from .prevention import PREVENTION

__all__ = [
    'PNEUMONIA_INFO',
    'CAUSES',
    'SYMPTOMS',
    'DIAGNOSIS',
    'COMPLICATIONS',
    'TREATMENT',
    'PREVENTION',
]

