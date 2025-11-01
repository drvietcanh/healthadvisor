"""
Paracetamol Calculator Components
Tách từ paracetamol_calculator.py (356 dòng) thành các modules
"""

from .calculator_logic import calculate_paracetamol_dose
from .render_display import render_paracetamol_calculator
from .guidelines import get_paracetamol_guidelines

__all__ = [
    'calculate_paracetamol_dose',
    'render_paracetamol_calculator',
    'get_paracetamol_guidelines',
]

