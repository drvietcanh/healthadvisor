"""
Tab: Rối Loạn Nhịp Tim (Arrhythmia)
DEPRECATED: Import từ cardiovascular_page_components.arrhythmia thay vì dùng trực tiếp
"""
# Import từ module mới (backward compatible)
from cardiovascular_page_components.arrhythmia.render import render_arrhythmia_tab

# Export function để các file khác import được
__all__ = ["render_arrhythmia_tab"]
