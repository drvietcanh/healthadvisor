"""
BMI Calculator - Tính BMI và phân loại theo chuẩn Châu Á
"""

from typing import Dict


def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    """
    Tính BMI (Body Mass Index)
    
    Args:
        weight_kg: Cân nặng (kg)
        height_cm: Chiều cao (cm)
    
    Returns:
        BMI value
    
    Formula: BMI = weight(kg) / (height(m))^2
    """
    if weight_kg <= 0 or height_cm <= 0:
        raise ValueError("Cân nặng và chiều cao phải > 0")
    
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)


def get_bmi_category(bmi: float, bmi_categories: Dict) -> Dict:
    """
    Phân loại BMI theo chuẩn Châu Á
    
    Args:
        bmi: BMI value
        bmi_categories: Dictionary từ info module
    
    Returns:
        Category info dict
    """
    for category_id, category_info in bmi_categories.items():
        min_bmi, max_bmi = category_info["range"]
        if min_bmi <= bmi < max_bmi:
            return {
                "id": category_id,
                **category_info
            }
    
    # Default nếu BMI quá cao
    return {
        "id": "obese_2",
        **bmi_categories["obese_2"]
    }


def calculate_ideal_weight(height_cm: float, gender: str = "male") -> Dict:
    """
    Tính cân nặng lý tưởng theo công thức Devine (điều chỉnh châu Á)
    
    Args:
        height_cm: Chiều cao (cm)
        gender: "male" hoặc "female"
    
    Returns:
        Dict với ideal weight và range
    """
    if height_cm <= 0:
        raise ValueError("Chiều cao phải > 0")
    
    # Công thức Devine (điều chỉnh cho châu Á)
    # Nam: 50 + 2.3 x (height_in - 60) x 0.9  (0.9 = Asian adjustment)
    # Nữ: 45.5 + 2.3 x (height_in - 60) x 0.9
    
    height_in = height_cm / 2.54  # Convert cm to inches
    
    if gender == "male":
        if height_in <= 60:
            ideal = 50
        else:
            ideal = 50 + 2.3 * (height_in - 60) * 0.9
    else:  # female
        if height_in <= 60:
            ideal = 45.5
        else:
            ideal = 45.5 + 2.3 * (height_in - 60) * 0.9
    
    # BMI 18.5-23 range (chuẩn châu Á)
    height_m = height_cm / 100
    min_weight = 18.5 * (height_m ** 2)
    max_weight = 23.0 * (height_m ** 2)
    
    return {
        "ideal": round(ideal, 1),
        "range": (round(min_weight, 1), round(max_weight, 1)),
        "bmi_range": (18.5, 23.0)
    }


__all__ = ['calculate_bmi', 'get_bmi_category', 'calculate_ideal_weight']
