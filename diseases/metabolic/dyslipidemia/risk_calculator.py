"""
Risk Calculator - Tính nguy cơ tim mạch
========================================

Framingham Risk Score, ASCVD Risk Calculator

File này tổng hợp từ 2 modules:
- lipid_classification: Phân loại mức lipid máu
- cardiovascular_risk: Tính toán nguy cơ tim mạch
"""

from .lipid_classification import classify_lipid_levels

from .cardiovascular_risk import (
    calculate_framingham_score,
    calculate_cardiovascular_risk,
    get_risk_category,
    get_treatment_recommendations
)

# Export all để dùng như cũ
__all__ = [
    'classify_lipid_levels',
    'calculate_framingham_score',
    'calculate_cardiovascular_risk',
    'get_risk_category',
    'get_treatment_recommendations'
]
