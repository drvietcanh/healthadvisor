"""
Visualizer - Vẽ biểu đồ xu hướng đẹp mắt
==========================================

File này import và re-export tất cả chart functions từ các modules con
để giữ backward compatibility với code cũ.
"""

# Import từ các modules đã tách
from .trend_charts import create_trend_chart
from .comparison_charts import create_comparison_chart, create_correlation_chart
from .weight_charts import create_weight_trend_chart, create_waist_circumference_chart
from .calories_charts import create_calories_balance_chart

# Re-export để giữ backward compatibility
__all__ = [
    'create_trend_chart',
    'create_comparison_chart',
    'create_correlation_chart',
    'create_weight_trend_chart',
    'create_calories_balance_chart',
    'create_waist_circumference_chart',
]
