"""
Cholesterol Foods Classification - Phân loại thực phẩm theo cholesterol
=========================================================================

Bảng phân loại thực phẩm giàu/ít cholesterol

File này tổng hợp từ 2 modules:
- cholesterol_levels: Phân loại thực phẩm theo mức cholesterol
- cholesterol_dishes_tips: Món ăn VN, mẹo nấu ăn, thông điệp quan trọng
"""

from .cholesterol_levels import CHOLESTEROL_FOOD_CLASSIFICATION

from .cholesterol_dishes_tips import (
    VIETNAMESE_DISHES_CHOLESTEROL,
    COOKING_TIPS_REDUCE_CHOLESTEROL,
    KEY_CHOLESTEROL_MESSAGES
)

# Export all để dùng như cũ
__all__ = [
    'CHOLESTEROL_FOOD_CLASSIFICATION',
    'VIETNAMESE_DISHES_CHOLESTEROL',
    'COOKING_TIPS_REDUCE_CHOLESTEROL',
    'KEY_CHOLESTEROL_MESSAGES'
]
