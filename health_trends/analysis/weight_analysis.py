"""
Weight Analysis - Phân tích xu hướng cân nặng
"""
import pandas as pd
from datetime import datetime, timedelta
import streamlit as st

from health_trends.analysis.trend_calculator import calculate_trend


@st.cache_data(ttl=300)
def analyze_weight_trend(df, days=30):
    """
    Phân tích xu hướng cân nặng
    
    Args:
        df: DataFrame từ Nhật ký
        days: Số ngày phân tích
    
    Returns:
        dict với kết quả phân tích
    """
    if df is None or len(df) == 0:
        return None
    
    # Kiểm tra có cột cân nặng không
    if 'Cân nặng (kg)' not in df.columns:
        return None
    
    # Lọc N ngày gần nhất
    cutoff_date = datetime.now() - timedelta(days=days)
    df['Ngày'] = pd.to_datetime(df['Ngày'])
    df_recent = df[df['Ngày'] >= cutoff_date].copy()
    
    # Lọc bỏ giá trị null
    df_recent = df_recent[df_recent['Cân nặng (kg)'].notna()]
    
    if len(df_recent) < 2:
        return None
    
    # Sort theo ngày
    df_recent = df_recent.sort_values('Ngày')
    
    # Phân tích xu hướng
    weight_trend = calculate_trend(df_recent['Cân nặng (kg)'], days=min(7, days))
    
    # Thống kê
    weight_avg = df_recent['Cân nặng (kg)'].mean()
    weight_start = df_recent['Cân nặng (kg)'].iloc[0]
    weight_current = df_recent['Cân nặng (kg)'].iloc[-1]
    weight_change = weight_current - weight_start
    
    # Đánh giá
    if abs(weight_change) < 1:
        weight_status = "stable"
        weight_message = "Ổn định"
    elif weight_change > 0:
        weight_status = "increasing"
        if weight_change > 5:
            weight_message = "Tăng nhiều"
        else:
            weight_message = "Tăng nhẹ"
    else:
        weight_status = "decreasing"
        if weight_change < -5:
            weight_message = "Giảm nhiều"
        else:
            weight_message = "Giảm nhẹ"
    
    return {
        "trend": weight_trend,
        "avg": round(weight_avg, 1),
        "start": round(weight_start, 1),
        "current": round(weight_current, 1),
        "change": round(weight_change, 1),
        "status": weight_status,
        "message": weight_message,
        "data_points": len(df_recent),
        "days_analyzed": days
    }

