"""
General Health Tips
Các mẹo vặt y tế hữu ích cho người dân

REFACTORED: Tách thành 3 modules nhỏ (fever, temperature, medicine)
"""

from .general_tips_fever import render_fever_tips
from .general_tips_temperature import render_temperature_guide
from .general_tips_medicine import render_medicine_tips

__all__ = [
    'render_fever_tips',
    'render_temperature_guide',
    'render_medicine_tips',
]
