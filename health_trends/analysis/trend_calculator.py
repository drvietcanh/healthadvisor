"""
Trend Calculator - Tính xu hướng dữ liệu
"""
import pandas as pd
import streamlit as st


@st.cache_data(ttl=300)  # Cache 5 phút
def calculate_trend(data, days=7):
    """
    Tính xu hướng tăng/giảm/ổn định
    
    Args:
        data: Series dữ liệu (đã sort theo thời gian)
        days: Số ngày phân tích
    
    Returns:
        dict với trend, slope, change_percent
    """
    if len(data) < 2:
        return {"trend": "unknown", "slope": 0, "change_percent": 0}
    
    # Lấy N ngày gần nhất
    recent_data = data.tail(days).dropna()
    
    if len(recent_data) < 2:
        return {"trend": "unknown", "slope": 0, "change_percent": 0}
    
    # Tính xu hướng đơn giản: so sánh trung bình 2 nửa
    mid = len(recent_data) // 2
    first_half = recent_data.iloc[:mid].mean()
    second_half = recent_data.iloc[mid:].mean()
    
    change = second_half - first_half
    change_percent = (change / first_half * 100) if first_half != 0 else 0
    
    # Phân loại xu hướng
    if abs(change_percent) < 3:  # <3% = ổn định
        trend = "stable"
    elif change_percent > 0:
        trend = "increasing"
    else:
        trend = "decreasing"
    
    return {
        "trend": trend,
        "slope": change,
        "change_percent": round(change_percent, 1),
        "first_avg": round(first_half, 1),
        "second_avg": round(second_half, 1)
    }

