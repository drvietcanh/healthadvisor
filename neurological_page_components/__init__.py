"""
Neurological Page Components
Components cho trang Thần Kinh
"""

from .dementia_tab import render_dementia_tab
from .insomnia_tab import render_insomnia_tab
from .stroke_tab import render_stroke_tab
from .epilepsy_tab import render_epilepsy_tab
from .headache_tab import render_headache_tab
from .befast_check_tab import render_befast_check_tab

__all__ = [
    'render_dementia_tab',
    'render_insomnia_tab',
    'render_stroke_tab',
    'render_epilepsy_tab',
    'render_headache_tab',
    'render_befast_check_tab',
]
