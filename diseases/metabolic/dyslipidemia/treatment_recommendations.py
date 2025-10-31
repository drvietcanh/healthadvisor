"""
Treatment Recommendations
Đề xuất điều trị dựa trên nguy cơ tim mạch
"""

from typing import Dict
from .risk_categories import get_risk_category


def get_treatment_recommendations(
    ldl: float,
    risk_level: str,
    current_ldl: float
) -> Dict:
    """
    Đề xuất điều trị
    
    Args:
        ldl: LDL hiện tại (duplicate parameter for compatibility)
        risk_level: Mức độ nguy cơ
        current_ldl: LDL hiện tại
    
    Returns:
        Dict với recommendations
    """
    category_info = get_risk_category(risk_level)
    target_ldl = int(category_info["ldl_target"].replace("<", "").replace("mg/dL", "").strip())
    
    reduction_needed = current_ldl - target_ldl
    reduction_pct = (reduction_needed / current_ldl * 100) if current_ldl > 0 else 0
    
    recommendations = {
        "lifestyle": _get_lifestyle_recommendations(),
        "medication": _get_medication_recommendations(risk_level, reduction_pct),
        "monitoring": _get_monitoring_recommendations(risk_level)
    }
    
    return {
        "current_ldl": current_ldl,
        "target_ldl": target_ldl,
        "reduction_needed": round(reduction_needed, 1),
        "reduction_percentage": round(reduction_pct, 1),
        "risk_level": risk_level,
        "recommendations": recommendations,
        "note": f"Cần giảm LDL {reduction_needed:.0f} mg/dL ({reduction_pct:.0f}%)" if reduction_needed > 0 else "LDL đã đạt mục tiêu!"
    }


def _get_lifestyle_recommendations() -> list:
    """Khuyến nghị về lối sống"""
    return [
        "🥗 Giảm chất béo bão hòa (<7% calories)",
        "🚫 Tránh trans fat hoàn toàn",
        "🐟 Ăn cá béo 2-3 lần/tuần",
        "🥬 Tăng rau xanh, ngũ cốc nguyên hạt",
        "🏃 Vận động 150 phút/tuần",
        "⚖️ Giảm cân nếu thừa cân"
    ]


def _get_medication_recommendations(risk_level: str, reduction_pct: float) -> list:
    """Khuyến nghị về thuốc"""
    if risk_level == "Rất cao":
        return [
            "💊 STATIN liều cao (Atorvastatin 40-80mg hoặc Rosuvastatin 20-40mg)",
            "💊 Có thể thêm Ezetimibe 10mg nếu chưa đạt mục tiêu",
            "💊 Cân nhắc PCSK9 inhibitor nếu LDL vẫn >55 sau dùng thuốc tối đa"
        ]
    
    elif risk_level == "Cao":
        return [
            "💊 STATIN liều trung bình-cao (Atorvastatin 20-40mg)",
            "💊 Tăng liều hoặc thêm Ezetimibe nếu chưa đạt mục tiêu"
        ]
    
    elif risk_level == "Trung bình":
        if reduction_pct > 30:
            return [
                "💊 Cân nhắc STATIN liều thấp-trung bình",
                "⏰ Thử lối sống 3-6 tháng trước khi dùng thuốc"
            ]
        else:
            return [
                "⏰ Thử thay đổi lối sống 3-6 tháng trước",
                "💊 Dùng statin nếu LDL vẫn không đạt mục tiêu"
            ]
    
    else:  # Thấp
        return [
            "✅ KHÔNG CẦN THUỐC - chỉ duy trì lối sống lành mạnh"
        ]


def _get_monitoring_recommendations(risk_level: str) -> list:
    """Khuyến nghị về theo dõi"""
    if risk_level == "Rất cao":
        return [
            "📊 Xét nghiệm lipid 2-3 tháng/lần",
            "🩺 Khám tim mạch 3-6 tháng/lần",
            "🧪 Kiểm tra men gan sau 1-2 tháng dùng statin"
        ]
    
    elif risk_level == "Cao":
        return [
            "📊 Xét nghiệm lipid 3-6 tháng/lần",
            "🩺 Khám tim mạch 6 tháng/lần"
        ]
    
    elif risk_level == "Trung bình":
        return [
            "📊 Xét nghiệm lipid 3-6 tháng sau thay đổi lối sống",
            "🩺 Khám tim mạch 1 năm/lần"
        ]
    
    else:  # Thấp
        return [
            "📊 Xét nghiệm lipid 3-5 năm/lần",
            "🩺 Khám sức khỏe định kỳ hàng năm"
        ]

