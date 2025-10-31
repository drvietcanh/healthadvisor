"""
Đánh giá Nguy cơ Tim Mạch
Cardiovascular Risk Assessment

File này giữ lại để backward compatibility.
Code đã được tách thành các modules:
- framingham_calculator.py
- risk_assessment.py
- risk_categories.py
- treatment_recommendations.py
"""

# Import từ các modules mới
from .framingham_calculator import calculate_framingham_score
from .risk_assessment import calculate_cardiovascular_risk
from .risk_categories import get_risk_category
from .treatment_recommendations import get_treatment_recommendations

# Export để backward compatibility
__all__ = [
    'calculate_framingham_score',
    'calculate_cardiovascular_risk',
    'get_risk_category',
    'get_treatment_recommendations'
]


