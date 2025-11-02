"""
Parasitology Page Components
Components cho trang Ký Sinh Trùng
"""

from .ascarid_tab import render_ascarid_tab
from .hookworm_tab import render_hookworm_tab
from .pinworm_tab import render_pinworm_tab
from .tapeworm_tab import render_tapeworm_tab
from .amoebic_dysentery_tab import render_amoebic_dysentery_tab
from .giardiasis_tab import render_giardiasis_tab
from .toxoplasmosis_tab import render_toxoplasmosis_tab
from .malaria_tab import render_malaria_tab

__all__ = [
    'render_ascarid_tab',
    'render_hookworm_tab',
    'render_pinworm_tab',
    'render_tapeworm_tab',
    'render_amoebic_dysentery_tab',
    'render_giardiasis_tab',
    'render_toxoplasmosis_tab',
    'render_malaria_tab',
]

