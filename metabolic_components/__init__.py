"""
Metabolic Components
====================

Components cho trang Hội Chứng Chuyển Hóa & Béo Phì
Tách từ pages/4_⚖️_Hội_Chứng_Chuyển_Hóa.py để dễ quản lý
"""

from .overview import render_overview_tab
from .assessment import render_assessment_tab
from .diseases import render_diseases_tab
from .calories import render_calories_tab
from .goals import render_goals_tab

__all__ = [
    'render_overview_tab',
    'render_assessment_tab',
    'render_diseases_tab',
    'render_calories_tab',
    'render_goals_tab'
]

