"""
Instructions - Các hướng dẫn sử dụng cho Nhật ký
Backward compatible - Import từ submodule
"""

from .instructions.overview import render_instructions
from .instructions.blood_pressure_guide import render_bp_guide
from .instructions.file_guide import render_file_guide

# Export để backward compatible
__all__ = [
    'render_instructions',
    'render_bp_guide',
    'render_file_guide'
]
