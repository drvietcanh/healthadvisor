"""
ENT Page Components
Components cho trang Tai Mũi Họng
"""

from ent_page_components.hearing_loss_tab import render_hearing_loss_tab
from ent_page_components.tinnitus_tab import render_tinnitus_tab
from ent_page_components.chronic_pharyngitis_tab import render_chronic_pharyngitis_tab
from ent_page_components.vertigo_tab import render_vertigo_tab
from ent_page_components.otitis_media_tab import render_otitis_media_tab

__all__ = [
    "render_hearing_loss_tab",
    "render_tinnitus_tab",
    "render_chronic_pharyngitis_tab",
    "render_vertigo_tab",
    "render_otitis_media_tab"
]

