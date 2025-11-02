"""
Health Trends Analysis Module
Module phân tích xu hướng sức khỏe
"""

from health_trends.analysis.trend_calculator import calculate_trend
from health_trends.analysis.bp_analysis import analyze_blood_pressure_trend
from health_trends.analysis.bs_analysis import analyze_blood_sugar_trend
from health_trends.analysis.weight_analysis import analyze_weight_trend
from health_trends.analysis.health_score import get_overall_health_score

__all__ = [
    "calculate_trend",
    "analyze_blood_pressure_trend",
    "analyze_blood_sugar_trend",
    "analyze_weight_trend",
    "get_overall_health_score"
]

