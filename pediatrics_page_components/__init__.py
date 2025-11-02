"""
Pediatrics Page Components
Components cho trang Nhi Khoa
"""

from .fever_tab import render_fever_tab
from .diarrhea_tab import render_diarrhea_tab
from .seizure_tab import render_seizure_tab

__all__ = [
    'render_fever_tab',
    'render_diarrhea_tab',
    'render_seizure_tab',
]

