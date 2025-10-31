"""
Risk Calculator - Tính nguy cơ tim mạch
========================================

Framingham Risk Score, ASCVD Risk Calculator

File này tổng hợp từ các modules:
- lipid_classification: Phân loại mức lipid máu
- framingham_calculator: Tính Framingham Risk Score
- risk_assessment: Đánh giá nguy cơ tim mạch tổng hợp
- risk_categories: Phân loại mức độ nguy cơ
- treatment_recommendations: Đề xuất điều trị
"""

from .lipid_classification import classify_lipid_levels
from .framingham_calculator import calculate_framingham_score
from .risk_assessment import calculate_cardiovascular_risk
from .risk_categories import get_risk_category
from .treatment_recommendations import get_treatment_recommendations

# Export all để dùng như cũ
__all__ = [
    'classify_lipid_levels',
    'calculate_framingham_score',
    'calculate_cardiovascular_risk',
    'get_risk_category',
    'get_treatment_recommendations'
]
