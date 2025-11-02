"""
Blood Sugar Analysis - Phân tích xu hướng đường huyết
"""
import pandas as pd
from datetime import datetime, timedelta
import streamlit as st

from health_trends.analysis.trend_calculator import calculate_trend


@st.cache_data(ttl=300)
def analyze_blood_sugar_trend(df, days=30):
    """
    Phân tích xu hướng đường huyết
    
    Args:
        df: DataFrame từ Nhật ký
        days: Số ngày phân tích
    
    Returns:
        dict với kết quả phân tích
    """
    if df is None or len(df) == 0:
        return None
    
    # Kiểm tra có cột đường huyết không
    if 'Đường huyết' not in df.columns:
        return None
    
    # Lọc N ngày gần nhất
    cutoff_date = datetime.now() - timedelta(days=days)
    df['Ngày'] = pd.to_datetime(df['Ngày'])
    df_recent = df[df['Ngày'] >= cutoff_date].copy()
    
    # Lọc bỏ giá trị null
    df_recent = df_recent[df_recent['Đường huyết'].notna()]
    
    if len(df_recent) < 2:
        return None
    
    # Sort theo ngày
    df_recent = df_recent.sort_values('Ngày')
    
    # Phân tích xu hướng
    bs_trend = calculate_trend(df_recent['Đường huyết'], days=min(7, days))
    
    # Thống kê
    bs_avg = df_recent['Đường huyết'].mean()
    bs_max = df_recent['Đường huyết'].max()
    bs_min = df_recent['Đường huyết'].min()
    
    # Đếm số lần cao/thấp
    high_count = len(df_recent[df_recent['Đường huyết'] > 7.0])  # > 126 mg/dL
    low_count = len(df_recent[df_recent['Đường huyết'] < 3.9])   # < 70 mg/dL
    
    # Phân loại
    if bs_avg < 5.6:
        bs_category = "Bình thường"
        bs_status = "good"
    elif bs_avg < 7.0:
        bs_category = "Tiền tiểu đường"
        bs_status = "warning"
    else:
        bs_category = "Tiểu đường"
        bs_status = "bad"
    
    return {
        "trend": bs_trend,
        "avg": round(bs_avg, 1),
        "max": round(bs_max, 1),
        "min": round(bs_min, 1),
        "high_count": high_count,
        "low_count": low_count,
        "category": bs_category,
        "status": bs_status,
        "data_points": len(df_recent),
        "days_analyzed": days
    }

