"""
Osteoporosis Tab Components
Tách từ osteoporosis_tab.py (389 dòng) thành các modules
"""

from .osteoporosis_info import render_osteoporosis_info
from .osteoporosis_symptoms import render_osteoporosis_symptoms  
from .osteoporosis_treatment import render_osteoporosis_treatment
from .osteoporosis_prevention import render_osteoporosis_prevention

__all__ = [
    'render_osteoporosis_info',
    'render_osteoporosis_symptoms',
    'render_osteoporosis_treatment',
    'render_osteoporosis_prevention',
]

