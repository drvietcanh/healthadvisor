"""
Analyzer - Phân tích xu hướng dữ liệu sức khỏe
DEPRECATED: Import từ health_trends.analysis thay vì dùng trực tiếp
"""
# Import từ module mới (backward compatible)
from health_trends.analysis import (
    calculate_trend,
    analyze_blood_pressure_trend,
    analyze_blood_sugar_trend,
    analyze_weight_trend,
    get_overall_health_score
)

# Tất cả functions được import từ module analysis mới
# Giữ file này để backward compatibility

