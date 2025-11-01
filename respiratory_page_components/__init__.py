"""
Respiratory Page Components
Tách từ pages/2_🫁_Hô_Hấp.py để dễ quản lý
"""

from .copd_tab import render_copd_tab
from .asthma_tab import render_asthma_tab

__all__ = [
    'render_copd_tab',
    'render_asthma_tab',
]

