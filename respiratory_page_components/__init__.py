"""
Respiratory Page Components
Tách từ pages/2_🫁_Hô_Hấp.py để dễ quản lý
"""

from .copd_tab import render_copd_tab
from .asthma_tab import render_asthma_tab
from .pneumonia_tab import render_pneumonia_tab
from .chronic_cough_tab import render_chronic_cough_tab
from .sleep_apnea_tab import render_sleep_apnea_tab

__all__ = [
    'render_copd_tab',
    'render_asthma_tab',
    'render_pneumonia_tab',
    'render_chronic_cough_tab',
    'render_sleep_apnea_tab',
]

