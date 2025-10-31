"""
Guide Components - Các components cho trang Hướng Dẫn
"""

from .quick_start_tab import render_quick_start_tab
from .detailed_guide_tab import render_detailed_guide_tab
from .faq_tab import render_faq_tab
from .tips_tab import render_tips_tab

__all__ = [
    'render_quick_start_tab',
    'render_detailed_guide_tab',
    'render_faq_tab',
    'render_tips_tab'
]

