"""
Digestive Page Components
"""

from .gerd_tab import render_gerd_tab
from .constipation_tab import render_constipation_tab
from .gastritis_tab import render_gastritis_tab
from .peptic_ulcer_tab import render_peptic_ulcer_tab
from .diarrhea_tab import render_diarrhea_tab
from .colitis_tab import render_colitis_tab
from .ibs_tab import render_ibs_tab

__all__ = [
    'render_gerd_tab',
    'render_constipation_tab',
    'render_gastritis_tab',
    'render_peptic_ulcer_tab',
    'render_diarrhea_tab',
    'render_colitis_tab',
    'render_ibs_tab',
]

