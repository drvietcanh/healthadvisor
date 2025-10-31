"""
Bone Joint Page Components
Components để hiển thị trang Khớp - Cột sống
"""

from .arthritis_tab import (
    render_osteoarthritis_tab,
    render_rheumatoid_arthritis_tab
)

from .spine_tab import (
    render_back_pain_tab,
    render_herniated_disc_tab
)

from .gout_tab import render_gout_tab

from .exercises_tab import render_joint_exercises_tab

from .osteoporosis_tab import render_osteoporosis_tab

__all__ = [
    'render_osteoarthritis_tab',
    'render_rheumatoid_arthritis_tab',
    'render_back_pain_tab',
    'render_herniated_disc_tab',
    'render_gout_tab',
    'render_joint_exercises_tab',
    'render_osteoporosis_tab'
]

