"""
Health Trends Page Components
Tách từ pages/_📈_Xu_Hướng.py (371 dòng) thành các tabs
"""

from .overview_tab import render_overview_tab
from .blood_pressure_tab import render_blood_pressure_tab
from .blood_sugar_tab import render_blood_sugar_tab
from .weight_tab import render_weight_tab
from .correlation_tab import render_correlation_tab
from .recommendations_section import render_recommendations_section

__all__ = [
    'render_overview_tab',
    'render_blood_pressure_tab',
    'render_blood_sugar_tab',
    'render_weight_tab',
    'render_correlation_tab',
    'render_recommendations_section',
]

