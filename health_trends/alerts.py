"""
Alerts - Cảnh báo thông minh và gợi ý
"""

def check_bp_alerts(bp_analysis):
    """
    Kiểm tra và tạo cảnh báo về huyết áp
    
    Returns:
        list of dict với alerts
    """
    if not bp_analysis:
        return []
    
    alerts = []
    
    # Huyết áp quá cao
    if bp_analysis['status'] == 'critical':
        alerts.append({
            "type": "danger",
            "title": "⚠️ CẢNH BÁO NGHIÊM TRỌNG",
            "message": f"Huyết áp trung bình {bp_analysis['avg_systolic']}/{bp_analysis['avg_diastolic']} mmHg - Cần đi khám NGAY!",
            "priority": 1
        })
    elif bp_analysis['status'] == 'bad':
        alerts.append({
            "type": "warning",
            "title": "⚠️ Huyết áp cao",
            "message": f"Huyết áp trung bình {bp_analysis['avg_systolic']}/{bp_analysis['avg_diastolic']} mmHg - Nên đi khám bác sĩ",
            "priority": 2
        })
    
    # Xu hướng tăng
    if bp_analysis['systolic_trend']['trend'] == 'increasing':
        if bp_analysis['systolic_trend']['change_percent'] > 10:
            alerts.append({
                "type": "warning",
                "title": "📈 Huyết áp đang tăng",
                "message": f"Huyết áp tâm thu tăng {bp_analysis['systolic_trend']['change_percent']}% trong 7 ngày qua",
                "priority": 2
            })
    
    # Biến động lớn
    if bp_analysis['max_systolic'] - bp_analysis['min_systolic'] > 40:
        alerts.append({
            "type": "info",
            "title": "📊 Huyết áp dao động",
            "message": f"Huyết áp dao động từ {bp_analysis['min_systolic']} đến {bp_analysis['max_systolic']} mmHg - Nên đo đều đặn",
            "priority": 3
        })
    
    return sorted(alerts, key=lambda x: x['priority'])

def check_bs_alerts(bs_analysis):
    """
    Kiểm tra và tạo cảnh báo về đường huyết
    
    Returns:
        list of dict với alerts
    """
    if not bs_analysis:
        return []
    
    alerts = []
    
    # Đường huyết cao
    if bs_analysis['status'] == 'bad':
        alerts.append({
            "type": "danger",
            "title": "⚠️ Đường huyết cao",
            "message": f"Đường huyết trung bình {bs_analysis['avg']} mmol/L - Cần kiểm soát tốt hơn",
            "priority": 1
        })
    elif bs_analysis['status'] == 'warning':
        alerts.append({
            "type": "warning",
            "title": "⚠️ Tiền tiểu đường",
            "message": f"Đường huyết trung bình {bs_analysis['avg']} mmol/L - Cần theo dõi và điều chỉnh chế độ ăn",
            "priority": 2
        })
    
    # Hạ đường huyết
    if bs_analysis['low_count'] > 0:
        alerts.append({
            "type": "danger",
            "title": "🍬 Hạ đường huyết",
            "message": f"Có {bs_analysis['low_count']} lần đường huyết < 3.9 mmol/L - NGUY HIỂM! Luôn mang theo kẹo",
            "priority": 1
        })
    
    # Xu hướng tăng
    if bs_analysis['trend']['trend'] == 'increasing':
        if bs_analysis['trend']['change_percent'] > 15:
            alerts.append({
                "type": "warning",
                "title": "📈 Đường huyết đang tăng",
                "message": f"Đường huyết tăng {bs_analysis['trend']['change_percent']}% - Kiểm tra chế độ ăn và thuốc",
                "priority": 2
            })
    
    # Đường huyết quá cao nhiều lần
    if bs_analysis['high_count'] > bs_analysis['data_points'] * 0.5:
        alerts.append({
            "type": "warning",
            "title": "📊 Kiểm soát chưa tốt",
            "message": f"{bs_analysis['high_count']}/{bs_analysis['data_points']} lần đường huyết > 7.0 mmol/L - Cần điều chỉnh",
            "priority": 2
        })
    
    return sorted(alerts, key=lambda x: x['priority'])

def check_weight_alerts(weight_analysis):
    """
    Kiểm tra và tạo cảnh báo về cân nặng
    
    Returns:
        list of dict với alerts
    """
    if not weight_analysis:
        return []
    
    alerts = []
    
    # Thay đổi đột ngột
    if abs(weight_analysis['change']) > 5:
        if weight_analysis['change'] > 0:
            alerts.append({
                "type": "warning",
                "title": "📈 Tăng cân nhanh",
                "message": f"Tăng {weight_analysis['change']} kg trong {weight_analysis['days_analyzed']} ngày - Kiểm tra chế độ ăn",
                "priority": 2
            })
        else:
            alerts.append({
                "type": "warning",
                "title": "📉 Giảm cân nhanh",
                "message": f"Giảm {abs(weight_analysis['change'])} kg trong {weight_analysis['days_analyzed']} ngày - Nên đi khám",
                "priority": 2
            })
    
    # Thay đổi quá nhanh (>10 kg)
    if abs(weight_analysis['change']) > 10:
        alerts.append({
            "type": "danger",
            "title": "⚠️ Thay đổi cân nặng bất thường",
            "message": f"Cân nặng thay đổi {abs(weight_analysis['change'])} kg - CẦN ĐI KHÁM NGAY!",
            "priority": 1
        })
    
    return sorted(alerts, key=lambda x: x['priority'])

def generate_recommendations(bp_analysis, bs_analysis, weight_analysis, overall_score):
    """
    Tạo gợi ý cải thiện sức khỏe
    
    Returns:
        list of recommendations
    """
    recommendations = []
    
    # Gợi ý chung dựa trên điểm
    if overall_score['score'] >= 85:
        recommendations.append({
            "category": "general",
            "icon": "🎉",
            "title": "Tuyệt vời!",
            "message": "Bạn đang kiểm soát sức khỏe rất tốt. Hãy duy trì thói quen hiện tại!"
        })
    elif overall_score['score'] < 50:
        recommendations.append({
            "category": "general",
            "icon": "⚠️",
            "title": "Cần cải thiện",
            "message": "Sức khỏe của bạn cần được chú ý. Hãy tham khảo bác sĩ và điều chỉnh lối sống."
        })
    
    # Gợi ý về huyết áp
    if bp_analysis:
        if bp_analysis['status'] in ['bad', 'critical']:
            recommendations.append({
                "category": "blood_pressure",
                "icon": "❤️",
                "title": "Huyết áp cao",
                "message": "Giảm muối, ăn nhiều rau quả, vận động 30 phút/ngày, uống thuốc đều đặn"
            })
        
        if bp_analysis['systolic_trend']['trend'] == 'decreasing' and bp_analysis['status'] != 'good':
            recommendations.append({
                "category": "blood_pressure",
                "icon": "👍",
                "title": "Đang cải thiện!",
                "message": "Huyết áp đang giảm dần - Hãy tiếp tục phương pháp hiện tại!"
            })
    
    # Gợi ý về đường huyết
    if bs_analysis:
        if bs_analysis['status'] in ['bad', 'warning']:
            recommendations.append({
                "category": "blood_sugar",
                "icon": "🍽️",
                "title": "Đường huyết cao",
                "message": "Hạn chế đường, tinh bột trắng. Ăn nhiều rau, chọn carb phức (gạo lứt, yến mạch)"
            })
        
        if bs_analysis['low_count'] > 0:
            recommendations.append({
                "category": "blood_sugar",
                "icon": "🍬",
                "title": "Phòng hạ đường huyết",
                "message": "Luôn mang theo kẹo/đường. Ăn đủ bữa, đúng giờ. Kiểm tra liều thuốc với bác sĩ"
            })
        
        if bs_analysis['trend']['trend'] == 'decreasing' and bs_analysis['status'] != 'good':
            recommendations.append({
                "category": "blood_sugar",
                "icon": "👍",
                "title": "Kiểm soát tốt!",
                "message": "Đường huyết đang giảm - Bạn đang làm đúng hướng!"
            })
    
    # Gợi ý về cân nặng
    if weight_analysis:
        if abs(weight_analysis['change']) > 5:
            if weight_analysis['change'] > 0:
                recommendations.append({
                    "category": "weight",
                    "icon": "🏃",
                    "title": "Giảm cân",
                    "message": "Tăng vận động, giảm calo từ đồ chiên rán và đồ ngọt. Uống nhiều nước"
                })
            else:
                recommendations.append({
                    "category": "weight",
                    "icon": "🍲",
                    "title": "Duy trì cân nặng",
                    "message": "Ăn đủ dinh dưỡng, bổ sung protein. Nếu giảm không chủ ý, hãy đi khám"
                })
    
    # Gợi ý vận động
    if bp_analysis or bs_analysis:
        recommendations.append({
            "category": "exercise",
            "icon": "🚶",
            "title": "Vận động mỗi ngày",
            "message": "Đi bộ 30 phút/ngày giúp giảm huyết áp, kiểm soát đường huyết và duy trì cân nặng"
        })
    
    # Gợi ý theo dõi
    if bp_analysis and bp_analysis['data_points'] < 15:
        recommendations.append({
            "category": "tracking",
            "icon": "📊",
            "title": "Đo thường xuyên hơn",
            "message": "Bạn mới đo " + str(bp_analysis['data_points']) + " lần trong " + str(bp_analysis['days_analyzed']) + " ngày. Nên đo mỗi ngày để theo dõi tốt hơn"
        })
    
    return recommendations

