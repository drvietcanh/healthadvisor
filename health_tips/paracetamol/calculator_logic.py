"""
Paracetamol Calculator Logic
Tính liều paracetamol theo cân nặng
"""


def calculate_paracetamol_dose(weight_kg: float, age_years: int = None) -> dict:
    """
    Tính liều paracetamol theo cân nặng
    
    Args:
        weight_kg: Cân nặng (kg)
        age_years: Tuổi (năm) - optional, để kiểm tra an toàn
    
    Returns:
        dict: {
            "dose_mg": liều tính bằng mg,
            "syrup_ml": liều siro (nếu dùng siro 160mg/5ml),
            "tablet_formulations": dict với số viên theo từng hàm lượng,
            "max_daily_mg": liều tối đa trong 24h,
            "frequency": khoảng cách giữa các lần (giờ),
            "safety_note": lưu ý an toàn
        }
    """
    if weight_kg <= 0:
        return None
    
    # Liều paracetamol: 10-15mg/kg/lần cho trẻ em
    # Liều người lớn: 500-1000mg/lần (tối đa 4000mg/ngày)
    
    # Trẻ em (< 12 tuổi hoặc < 40kg)
    if age_years and age_years < 12 or weight_kg < 40:
        dose_per_kg = 15  # mg/kg - liều an toàn cho trẻ
        dose_mg = round(weight_kg * dose_per_kg)
        
        # Không quá 1000mg/lần cho trẻ
        dose_mg = min(dose_mg, 1000)
        
        # Liều tối đa ngày: 60mg/kg (không quá 4000mg)
        max_daily_mg = min(int(weight_kg * 60), 4000)
        frequency_hours = 4  # Cách 4-6 giờ
        safety_note = "Trẻ em: Cách 4-6 giờ/lần, tối đa 4 lần/ngày"
    else:
        # Người lớn (≥ 12 tuổi hoặc ≥ 40kg)
        if weight_kg < 50:
            dose_mg = 500
        elif weight_kg < 70:
            dose_mg = 650
        else:
            dose_mg = 1000
        
        max_daily_mg = 4000  # Tối đa 4000mg/ngày cho người lớn
        frequency_hours = 6  # Cách 6-8 giờ
        safety_note = "Người lớn: Cách 6-8 giờ/lần, tối đa 4 lần/ngày"
    
    # Tính siro (160mg/5ml) - thường cho trẻ em
    syrup_ml = None
    if weight_kg < 40:
        syrup_ml = round((dose_mg / 160) * 5, 1)
    
    # Tính số viên theo các hàm lượng phổ biến
    # Các hàm lượng: 250mg, 500mg, 650mg
    tablet_formulations = {}
    
    # Viên 250mg (thường cho trẻ lớn/thanh thiếu niên)
    tablets_250 = dose_mg / 250
    if tablets_250 == int(tablets_250):
        tablet_formulations["250mg"] = int(tablets_250)
    elif tablets_250 < 1:
        tablet_formulations["250mg"] = "1 viên (≈250mg, hơi thiếu)"
    else:
        tablet_formulations["250mg"] = f"{int(tablets_250)}+ viên (không khuyến nghị - dùng loại khác)"
    
    # Viên 500mg (phổ biến nhất)
    tablets_500 = dose_mg / 500
    if tablets_500 == int(tablets_500):
        tablet_formulations["500mg"] = int(tablets_500)
    elif tablets_500 < 1:
        tablet_formulations["500mg"] = "1 viên (≈500mg)"
    else:
        # Làm tròn lên/xuống gần nhất
        if tablets_500 <= 1.5:
            tablet_formulations["500mg"] = "1 viên (≈500mg, hơi thiếu)"
        else:
            tablet_formulations["500mg"] = int(round(tablets_500))
    
    # Viên 650mg (Efferalgan)
    tablets_650 = dose_mg / 650
    if tablets_650 == int(tablets_650):
        tablet_formulations["650mg"] = int(tablets_650)
    elif tablets_650 < 1:
        tablet_formulations["650mg"] = "1 viên (≈650mg, hơi dư)"
    else:
        if tablets_650 <= 1.3:
            tablet_formulations["650mg"] = "1 viên (≈650mg)"
        else:
            tablet_formulations["650mg"] = f"{int(round(tablets_650))} viên (≈{int(round(tablets_650)) * 650}mg)"
    
    # Viên 1000mg (người lớn)
    if dose_mg >= 1000:
        tablets_1000 = dose_mg / 1000
        if tablets_1000 == int(tablets_1000):
            tablet_formulations["1000mg"] = int(tablets_1000)
        else:
            tablet_formulations["1000mg"] = int(round(tablets_1000))
    
    return {
        "dose_mg": dose_mg,
        "syrup_ml": syrup_ml,
        "tablet_formulations": tablet_formulations,
        "max_daily_mg": max_daily_mg,
        "frequency_hours": frequency_hours,
        "safety_note": safety_note,
        "is_child": weight_kg < 40 or (age_years and age_years < 12)
    }

