"""
Medication Utilities - Các hàm helper cho thuốc điều trị mỡ máu
"""

from typing import Dict, List


def get_medication_info(medication_name: str, statins: List[Dict], fibrates: List[Dict], 
                        other_medications: Dict) -> Dict:
    """Lấy thông tin chi tiết về thuốc"""
    medication_name = medication_name.lower()
    
    # Search in Statins
    for statin in statins:
        if medication_name in statin.get("name", "").lower():
            return {
                "type": "Statin",
                "details": statin,
            }
    
    # Search in Fibrates
    for fibrate in fibrates:
        if medication_name in fibrate.get("name", "").lower():
            return {
                "type": "Fibrate",
                "details": fibrate,
            }
    
    # Search in others
    for key, med in other_medications.items():
        if medication_name in med.get("name", "").lower():
            return {
                "type": "Other",
                "details": med
            }
    
    return {"error": "Không tìm thấy thông tin thuốc"}


def get_side_effects(medication_type: str, statins_data: Dict, fibrates_data: Dict) -> Dict[str, List]:
    """Lấy danh sách tác dụng phụ"""
    if medication_type.lower() == "statin":
        return statins_data.get("side_effects", {})
    elif medication_type.lower() == "fibrate":
        return {
            "common": fibrates_data.get("side_effects", []),
            "important_notes": fibrates_data.get("important_notes", [])
        }
    else:
        return {"error": "Vui lòng chọn loại thuốc: statin hoặc fibrate"}


def get_treatment_recommendation(ldl: float, has_diabetes: bool = False, 
                                 has_cvd: bool = False, triglyceride: float = 0,
                                 treatment_protocols: Dict = None) -> Dict:
    """Đề xuất phác đồ điều trị dựa trên LDL và yếu tố nguy cơ
    
    Args:
        ldl: LDL cholesterol (mmol/L)
        has_diabetes: Có tiểu đường không
        has_cvd: Đã có bệnh tim mạch không (nhồi máu tim, đột quỵ)
        triglyceride: Triglyceride (mmol/L)
        treatment_protocols: Dict chứa các phác đồ điều trị
    """
    if not treatment_protocols:
        return {"error": "Thiếu dữ liệu phác đồ điều trị"}
    
    # Nguy cơ rất cao
    if has_cvd:
        return treatment_protocols["very_high_risk"]
    
    # LDL rất cao
    if ldl >= 4.9:
        return treatment_protocols["high"]
    
    # Triglyceride rất cao
    if triglyceride >= 5.7:
        return treatment_protocols["high_triglycerides"]
    
    # LDL cao + tiểu đường
    if ldl >= 2.6 and has_diabetes:
        return treatment_protocols["moderate"]
    
    # LDL trung bình
    if 3.4 <= ldl < 4.9:
        return treatment_protocols["moderate"]
    
    # LDL nhẹ
    if 2.6 <= ldl < 3.4:
        return treatment_protocols["mild"]
    
    return {
        "level": "Bình thường",
        "treatment": ["✅ Duy trì lối sống lành mạnh", "📊 Xét nghiệm lại sau 1 năm"]
    }

