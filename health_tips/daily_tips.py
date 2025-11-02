"""
Daily Health Tips
Mẹo vặt y tế hữu ích hàng ngày từ các nguồn uy tín

REFACTORED: Tách thành 3 modules nhỏ (general, preventive, nutrition)
"""

from health_tips.daily_tips_general import render_daily_health_tips
from health_tips.daily_tips_preventive import render_preventive_care
from health_tips.daily_tips_nutrition import render_nutrition_bone_health, render_nutrition_cholesterol

__all__ = [
    'render_daily_health_tips',
    'render_preventive_care',
    'render_nutrition_bone_health',
    'render_nutrition_cholesterol',
]
