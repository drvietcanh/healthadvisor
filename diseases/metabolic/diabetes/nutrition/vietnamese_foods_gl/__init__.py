"""
Vietnamese Foods Glycemic Load Module
Bảng GL thực phẩm Việt Nam
"""

from diseases.metabolic.diabetes.nutrition.vietnamese_foods_gl.staple_foods import STAPLE_FOODS_GL
from diseases.metabolic.diabetes.nutrition.vietnamese_foods_gl.root_vegetables import ROOT_VEGETABLES_GL
from diseases.metabolic.diabetes.nutrition.vietnamese_foods_gl.fruits import FRUITS_GL
from diseases.metabolic.diabetes.nutrition.vietnamese_foods_gl.drinks_snacks import DRINKS_GL, SNACKS_GL
from diseases.metabolic.diabetes.nutrition.vietnamese_foods_gl.vegetables import VEGETABLES_GL

# Tổng hợp tất cả
VIETNAMESE_FOODS_GL = (
    STAPLE_FOODS_GL +
    ROOT_VEGETABLES_GL +
    FRUITS_GL +
    DRINKS_GL +
    SNACKS_GL +
    VEGETABLES_GL
)

__all__ = [
    "VIETNAMESE_FOODS_GL",
    "STAPLE_FOODS_GL",
    "ROOT_VEGETABLES_GL",
    "FRUITS_GL",
    "DRINKS_GL",
    "SNACKS_GL",
    "VEGETABLES_GL"
]

