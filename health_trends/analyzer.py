"""
Analyzer - Phân tích xu hướng dữ liệu sức khỏe
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
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

@st.cache_data(ttl=300)
def get_overall_health_score(bp_analysis, bs_analysis, weight_analysis):
    """
    Tính điểm sức khỏe tổng thể (0-100)
    
    Args:
        bp_analysis: Kết quả phân tích huyết áp
        bs_analysis: Kết quả phân tích đường huyết
        weight_analysis: Kết quả phân tích cân nặng
    
    Returns:
        dict với score và đánh giá
    """
    score = 100
    issues = []
    
    # Huyết áp (-0 đến -40 điểm)
    if bp_analysis:
        if bp_analysis['status'] == 'critical':
            score -= 40
            issues.append("Huyết áp cao nghiêm trọng")
        elif bp_analysis['status'] == 'bad':
            score -= 25
            issues.append("Huyết áp cao")
        elif bp_analysis['status'] == 'warning':
            score -= 10
            issues.append("Huyết áp hơi cao")
    
    # Đường huyết (-0 đến -30 điểm)
    if bs_analysis:
        if bs_analysis['status'] == 'bad':
            score -= 30
            issues.append("Đường huyết cao")
        elif bs_analysis['status'] == 'warning':
            score -= 15
            issues.append("Tiền tiểu đường")
        
        if bs_analysis['low_count'] > 0:
            score -= 10
            issues.append(f"Có {bs_analysis['low_count']} lần hạ đường huyết")
    
    # Cân nặng (-0 đến -20 điểm)
    if weight_analysis:
        if abs(weight_analysis['change']) > 5:
            score -= 20
            issues.append(f"Cân nặng {weight_analysis['message'].lower()}")
    
    # Xu hướng
    trends_good = 0
    trends_bad = 0
    
    if bp_analysis and bp_analysis['systolic_trend']['trend'] == 'decreasing':
        trends_good += 1
    elif bp_analysis and bp_analysis['systolic_trend']['trend'] == 'increasing':
        trends_bad += 1
    
    if bs_analysis and bs_analysis['trend']['trend'] == 'decreasing':
        trends_good += 1
    elif bs_analysis and bs_analysis['trend']['trend'] == 'increasing':
        trends_bad += 1
    
    # Bonus/penalty cho xu hướng
    score += trends_good * 5
    score -= trends_bad * 5
    
    # Giới hạn 0-100
    score = max(0, min(100, score))
    
    # Đánh giá
    if score >= 85:
        rating = "Xuất sắc"
        emoji = "🌟"
        color = "green"
    elif score >= 70:
        rating = "Tốt"
        emoji = "😊"
        color = "green"
    elif score >= 50:
        rating = "Trung bình"
        emoji = "😐"
        color = "orange"
    else:
        rating = "Cần cải thiện"
        emoji = "😟"
        color = "red"
    
    return {
        "score": round(score),
        "rating": rating,
        "emoji": emoji,
        "color": color,
        "issues": issues,
        "positive_trends": trends_good,
        "negative_trends": trends_bad
    }

