"""
Dyslipidemia (Rối loạn Lipid Máu) Module
=========================================

Rối loạn lipid máu là tình trạng cholesterol và/hoặc triglyceride
trong máu cao hoặc thấp bất thường.

Liên quan chặt chẽ với:
- Béo phì
- Tiểu đường
- Cao huyết áp
- Bệnh tim mạch
"""

from .info import (
    DYSLIPIDEMIA_INFO,
    LIPID_TARGETS,
    LIPID_CATEGORIES,
    CAUSES,
    COMPLICATIONS,
    RELATED_DISEASES
)

from .risk_calculator import (
    classify_lipid_levels,
    calculate_cardiovascular_risk,
    calculate_framingham_score,
    get_risk_category,
    get_treatment_recommendations
)

from .nutrition import (
    FOOD_SAFETY_CLASSIFICATION,
    QUICK_REFERENCE_TABLE,
    FAT_TYPES_EXPLANATION,
    FAT_COMPARISON,
    GOOD_FOODS,
    BAD_FOODS,
    CHOLESTEROL_LOWERING_FOODS,
    get_diet_plan_vietnam,
    get_nutrition_tips
)

from .medications import (
    STATINS,
    FIBRATES,
    OTHER_MEDICATIONS,
    get_medication_info,
    get_side_effects
)

__all__ = [
    # Info
    'DYSLIPIDEMIA_INFO',
    'LIPID_TARGETS',
    'LIPID_CATEGORIES',
    'CAUSES',
    'COMPLICATIONS',
    'RELATED_DISEASES',
    
    # Risk Calculator
    'classify_lipid_levels',
    'calculate_cardiovascular_risk',
    'calculate_framingham_score',
    'get_risk_category',
    'get_treatment_recommendations',
    
    # Nutrition
    'FOOD_SAFETY_CLASSIFICATION',
    'QUICK_REFERENCE_TABLE',
    'FAT_TYPES_EXPLANATION',
    'FAT_COMPARISON',
    'GOOD_FOODS',
    'BAD_FOODS',
    'CHOLESTEROL_LOWERING_FOODS',
    'get_diet_plan_vietnam',
    'get_nutrition_tips',
    
    # Medications
    'STATINS',
    'FIBRATES',
    'OTHER_MEDICATIONS',
    'get_medication_info',
    'get_side_effects',
]

