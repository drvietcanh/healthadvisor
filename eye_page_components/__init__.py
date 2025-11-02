"""
Eye Page Components
"""

from .cataract_tab import render_cataract_tab
from .glaucoma_tab import render_glaucoma_tab
from .amd_tab import render_amd_tab
from .dry_eye_tab import render_dry_eye_tab
from .presbyopia_tab import render_presbyopia_tab

__all__ = [
    'render_cataract_tab',
    'render_glaucoma_tab',
    'render_amd_tab',
    'render_dry_eye_tab',
    'render_presbyopia_tab',
]

