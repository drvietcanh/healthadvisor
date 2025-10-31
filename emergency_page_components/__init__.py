"""
Emergency Page Components
Tách từ pages/10_🚨_Cấp_Cứu.py để dễ quản lý
"""

from .emergency_css import get_emergency_css
from .emergency_numbers_tab import render_emergency_numbers_tab
from .first_aid_tab import render_first_aid_tab
from .contacts_tab import render_contacts_tab
from .medical_info_tab import render_medical_info_tab

__all__ = [
    'get_emergency_css',
    'render_emergency_numbers_tab',
    'render_first_aid_tab',
    'render_contacts_tab',
    'render_medical_info_tab'
]

