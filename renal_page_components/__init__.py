"""
Renal Page Components
Tách từ pages/9_🧪_Thận_Tiết_Niệu.py để dễ quản lý
"""

from .ckd_tab import render_ckd_tab
from .kidney_stones_tab import render_kidney_stones_tab
from .uti_tab import render_uti_tab

__all__ = [
    'render_ckd_tab',
    'render_kidney_stones_tab',
    'render_uti_tab',
]

