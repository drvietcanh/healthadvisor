"""
Health Tips Module
Mẹo vặt y tế và công cụ tính toán hữu ích cho người dân
"""

try:
    from health_tips.paracetamol import (
        calculate_paracetamol_dose,
        render_paracetamol_calculator,
        get_paracetamol_guidelines
    )
except ImportError:
    calculate_paracetamol_dose = None
    render_paracetamol_calculator = None
    get_paracetamol_guidelines = None

try:
    from health_tips.general_tips import (
        render_fever_tips,
        render_temperature_guide,
        render_medicine_tips
    )
except ImportError:
    render_fever_tips = None
    render_temperature_guide = None
    render_medicine_tips = None

try:
    from health_tips.daily_tips import (
        render_daily_health_tips,
        render_preventive_care,
        render_nutrition_bone_health,
        render_nutrition_cholesterol
    )
except ImportError:
    render_daily_health_tips = None
    render_preventive_care = None
    render_nutrition_bone_health = None
    render_nutrition_cholesterol = None

try:
    from health_tips.exercise_guide import (
        render_general_exercise_tips,
        render_disease_specific_exercises
    )
except ImportError:
    render_general_exercise_tips = None
    render_disease_specific_exercises = None

try:
    from health_tips.practical_tips import (
        render_common_ailments_tab
    )
except ImportError:
    render_common_ailments_tab = None

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
    "render_nutrition_cholesterol",
    "render_common_ailments_tab"
]

