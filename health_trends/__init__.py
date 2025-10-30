"""
Health Trends - Phân tích xu hướng sức khỏe từ dữ liệu Nhật ký
"""

from .analyzer import (
    analyze_blood_pressure_trend,
    analyze_blood_sugar_trend,
    analyze_weight_trend,
    get_overall_health_score
)

from .alerts import (
    check_bp_alerts,
    check_bs_alerts,
    check_weight_alerts,
    generate_recommendations
)

from .visualizer import (
    create_trend_chart,
    create_comparison_chart,
    create_correlation_chart
)

__all__ = [
    'analyze_blood_pressure_trend',
    'analyze_blood_sugar_trend',
    'analyze_weight_trend',
    'get_overall_health_score',
    'check_bp_alerts',
    'check_bs_alerts',
    'check_weight_alerts',
    'generate_recommendations',
    'create_trend_chart',
    'create_comparison_chart',
    'create_correlation_chart',
]

