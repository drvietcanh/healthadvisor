"""
Các hàm tiện ích chung
"""
from datetime import datetime
from typing import Tuple


def convert_blood_sugar(value: float, from_unit: str = "mmol") -> Tuple[float, float]:
    """
    Chuyển đổi đường huyết giữa mmol/L và mg/dL
    
    Args:
        value: Giá trị đường huyết
        from_unit: "mmol" hoặc "mg"
    
    Returns:
        (giá trị mmol/L, giá trị mg/dL)
    """
    if from_unit == "mmol":
        mmol_value = value
        mg_value = value * 18
    else:  # mg/dL
        mg_value = value
        mmol_value = value / 18
    
    return round(mmol_value, 1), round(mg_value, 0)


def classify_blood_pressure(systolic: int, diastolic: int) -> dict:
    """Phân loại huyết áp"""
    if systolic >= 180 or diastolic >= 120:
        return {
            "level": "crisis",
            "name_vn": "CƠN TÁN HUYẾT ÁP",
            "color": "red",
            "action_vn": "🚨 GỌI 115 NGAY!"
        }
    elif systolic >= 140 or diastolic >= 90:
        return {
            "level": "stage2",
            "name_vn": "Tăng huyết áp giai đoạn 2",
            "color": "orange",
            "action_vn": "⚠️ Khám bác sĩ trong tuần này"
        }
    elif systolic >= 130 or diastolic >= 80:
        return {
            "level": "stage1",
            "name_vn": "Tăng huyết áp giai đoạn 1",
            "color": "yellow",
            "action_vn": "📋 Tái khám sau 1 tháng"
        }
    elif systolic >= 120 and diastolic < 80:
        return {
            "level": "elevated",
            "name_vn": "Huyết áp cao bình thường",
            "color": "yellow",
            "action_vn": "💡 Thay đổi lối sống"
        }
    else:
        return {
            "level": "normal",
            "name_vn": "Bình thường",
            "color": "green",
            "action_vn": "✅ Duy trì lối sống lành mạnh"
        }


def calculate_bmi(weight_kg: float, height_cm: float) -> dict:
    """Tính BMI và phân loại"""
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    
    # Tiêu chuẩn châu Á
    if bmi < 18.5:
        category = "Thiếu cân"
        color = "blue"
        risk = "Tăng nguy cơ suy dinh dưỡng"
    elif bmi < 23:
        category = "Bình thường"
        color = "green"
        risk = "Nguy cơ thấp"
    elif bmi < 25:
        category = "Thừa cân"
        color = "yellow"
        risk = "Nguy cơ vừa"
    elif bmi < 30:
        category = "Béo phì độ 1"
        color = "orange"
        risk = "Nguy cơ cao"
    else:
        category = "Béo phì độ 2"
        color = "red"
        risk = "Nguy cơ rất cao"
    
    return {
        "bmi": round(bmi, 1),
        "category_vn": category,
        "color": color,
        "risk_vn": risk
    }


def format_time_ago(hours: float) -> str:
    """Format thời gian đã qua sang tiếng Việt"""
    if hours < 1:
        minutes = int(hours * 60)
        return f"{minutes} phút trước"
    elif hours < 24:
        return f"{int(hours)} giờ trước"
    else:
        days = int(hours / 24)
        remaining_hours = int(hours % 24)
        if remaining_hours > 0:
            return f"{days} ngày {remaining_hours} giờ trước"
        return f"{days} ngày trước"


def get_greeting() -> str:
    """Lấy lời chào theo thời gian"""
    hour = datetime.now().hour
    if hour < 12:
        return "Chào buổi sáng"
    elif hour < 18:
        return "Chào buổi chiều"
    else:
        return "Chào buổi tối"

