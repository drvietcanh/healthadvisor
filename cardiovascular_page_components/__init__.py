"""
Cardiovascular Page Components
Tách từ pages/1_❤️_Tim_Mạch.py để dễ quản lý
"""

from .hypertension_tab import render_hypertension_tab
from .heart_failure_tab import render_heart_failure_tab
from .dyslipidemia_tab import render_dyslipidemia_tab
from .blood_pressure_tab import render_blood_pressure_tab

__all__ = [
    'render_hypertension_tab',
    'render_heart_failure_tab',
    'render_dyslipidemia_tab',
    'render_blood_pressure_tab'
]

