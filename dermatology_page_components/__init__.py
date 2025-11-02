"""
Dermatology Page Components
Components cho trang Da Liễu
"""

from dermatology_page_components.tinea_tab import render_tinea_tab
from dermatology_page_components.onychomycosis_tab import render_onychomycosis_tab
from dermatology_page_components.eczema_tab import render_eczema_tab
from dermatology_page_components.pruritus_tab import render_pruritus_tab
from dermatology_page_components.pressure_ulcer_tab import render_pressure_ulcer_tab
from dermatology_page_components.psoriasis_tab import render_psoriasis_tab

__all__ = [
    "render_tinea_tab",
    "render_onychomycosis_tab",
    "render_eczema_tab",
    "render_pruritus_tab",
    "render_pressure_ulcer_tab",
    "render_psoriasis_tab"
]

