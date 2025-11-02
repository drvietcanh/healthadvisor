"""
Health Score - Tính điểm sức khỏe tổng thể
"""


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

