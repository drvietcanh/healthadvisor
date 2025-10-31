"""
Glycemic Index (GI) and Glycemic Load (GL) Information
Comprehensive data for Vietnamese foods

File này tổng hợp từ 4 modules:
- glycemic_index: Thông tin GI đơn giản
- glycemic_load_explanation: Giải thích GL và so sánh GI vs GL
- vietnamese_foods_gl: Bảng 45+ thực phẩm Việt Nam với GL
- glycemic_tips: Mẹo áp dụng và giải thích khoa học
"""

from .glycemic_index import GLYCEMIC_INDEX_SIMPLE
from .glycemic_load_explanation import GLYCEMIC_LOAD_EXPLANATION
from .vietnamese_foods_gl import VIETNAMESE_FOODS_GL
from .glycemic_tips import GLYCEMIC_TIPS

# Gộp lại thành GLYCEMIC_INFO như cũ để tương thích ngược
GLYCEMIC_INFO = {
    "glycemic_index_simple": GLYCEMIC_INDEX_SIMPLE,
    "glycemic_load_advanced": {
        **GLYCEMIC_LOAD_EXPLANATION,
        "real_world_examples": VIETNAMESE_FOODS_GL,
        **GLYCEMIC_TIPS
    }
}

# Export để dùng như cũ
__all__ = ['GLYCEMIC_INFO', 'GLYCEMIC_INDEX_SIMPLE', 'GLYCEMIC_LOAD_EXPLANATION', 
           'VIETNAMESE_FOODS_GL', 'GLYCEMIC_TIPS']
