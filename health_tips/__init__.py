"""
Health Tips Module
Mẹo vặt y tế và công cụ tính toán hữu ích cho người dân
"""

from health_tips.paracetamol import (
    calculate_paracetamol_dose,
    render_paracetamol_calculator,
    get_paracetamol_guidelines
)

from health_tips.general_tips import (
    render_fever_tips,
    render_temperature_guide,
    render_medicine_tips
)

from health_tips.daily_tips import (
    render_daily_health_tips,
    render_preventive_care,
    render_nutrition_bone_health,
    render_nutrition_cholesterol
)

from health_tips.exercise_guide import (
    render_general_exercise_tips,
    render_disease_specific_exercises
)

__all__ = [
    "calculate_paracetamol_dose",
    "render_paracetamol_calculator",
    "get_paracetamol_guidelines",
    "render_fever_tips",
    "render_temperature_guide",
    "render_medicine_tips",
    "render_daily_health_tips",
    "render_preventive_care",
    "render_general_exercise_tips",
    "render_disease_specific_exercises",
    "render_nutrition_bone_health",
    "render_nutrition_cholesterol"
]

