"""
Blood Pressure Analysis - Phân tích xu hướng huyết áp
"""
import pandas as pd
from datetime import datetime, timedelta
import streamlit as st

from health_trends.analysis.trend_calculator import calculate_trend


@st.cache_data(ttl=300)
def analyze_blood_pressure_trend(df, days=30):
    """
    Phân tích xu hướng huyết áp
    
    Args:
        df: DataFrame từ Nhật ký (phải có cột 'Ngày', 'Huyết áp tâm thu', 'Huyết áp tâm trương')
        days: Số ngày phân tích
    
    Returns:
        dict với kết quả phân tích
    """
    if df is None or len(df) == 0:
        return None
    
    # Lọc N ngày gần nhất
    cutoff_date = datetime.now() - timedelta(days=days)
    df['Ngày'] = pd.to_datetime(df['Ngày'])
    df_recent = df[df['Ngày'] >= cutoff_date].copy()
    
    if len(df_recent) < 2:
        return None
    
    # Sort theo ngày
    df_recent = df_recent.sort_values('Ngày')
    
    # Phân tích tâm thu
    sys_trend = calculate_trend(df_recent['Huyết áp tâm thu'], days=min(7, days))
    
    # Phân tích tâm trương  
    dia_trend = calculate_trend(df_recent['Huyết áp tâm trương'], days=min(7, days))
    
    # Thống kê
    sys_avg = df_recent['Huyết áp tâm thu'].mean()
    dia_avg = df_recent['Huyết áp tâm trương'].mean()
    sys_max = df_recent['Huyết áp tâm thu'].max()
    sys_min = df_recent['Huyết áp tâm thu'].min()
    
    # Phân loại huyết áp (theo AHA)
    if sys_avg < 120 and dia_avg < 80:
        bp_category = "Bình thường"
        bp_status = "good"
    elif sys_avg < 130 and dia_avg < 80:
        bp_category = "Cao hơn bình thường"
        bp_status = "warning"
    elif sys_avg < 140 or dia_avg < 90:
        bp_category = "Huyết áp cao giai đoạn 1"
        bp_status = "bad"
    else:
        bp_category = "Huyết áp cao giai đoạn 2"
        bp_status = "critical"
    
    return {
        "systolic_trend": sys_trend,
        "diastolic_trend": dia_trend,
        "avg_systolic": round(sys_avg, 1),
        "avg_diastolic": round(dia_avg, 1),
        "max_systolic": sys_max,
        "min_systolic": sys_min,
        "category": bp_category,
        "status": bp_status,
        "data_points": len(df_recent),
        "days_analyzed": days
    }

