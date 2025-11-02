"""
Dental Page Components
=====================

Components để hiển thị các bệnh răng miệng
"""

from .gingivitis_tab import render_gingivitis_tab
from .periodontitis_tab import render_periodontitis_tab
from .toothache_tab import render_toothache_tab
from .tooth_loss_tab import render_tooth_loss_tab
from .xerostomia_tab import render_xerostomia_tab

__all__ = [
    'render_gingivitis_tab',
    'render_periodontitis_tab',
    'render_toothache_tab',
    'render_tooth_loss_tab',
    'render_xerostomia_tab',
]

