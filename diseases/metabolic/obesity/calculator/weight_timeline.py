"""
Weight Loss Timeline - Tính timeline giảm cân
"""

from typing import Dict


def get_milestone_benefits(percentage: int) -> list:
    """Lợi ích khi đạt mốc giảm cân"""
    benefits = {
        5: [
            "Giảm đường huyết",
            "Giảm huyết áp 5-10 mmHg",
            "Cải thiện chất lượng ngủ"
        ],
        10: [
            "Giảm 50% nguy cơ tiểu đường",
            "Giảm đau khớp gối",
            "Tăng năng lượng rõ rệt"
        ],
        15: [
            "Đảo ngược tiền tiểu đường",
            "Có thể ngừng thuốc huyết áp",
            "Cải thiện sức khỏe tim mạch"
        ],
        20: [
            "Tăng tuổi thọ 2-5 năm",
            "Giảm nguy cơ ung thư",
            "Cải thiện sức khỏe tổng thể"
        ],
        25: [
            "Sức khỏe tuyệt vời",
            "Đảo ngược hầu hết biến chứng",
            "Chất lượng cuộc sống cao"
        ]
    }
    return benefits.get(percentage, ["Tiếp tục phát huy!"])


def get_weight_loss_timeline(
    current_weight: float,
    target_weight: float,
    weekly_loss: float = 0.5
) -> Dict:
    """
    Tính timeline giảm cân
    
    Args:
        current_weight: Cân nặng hiện tại (kg)
        target_weight: Cân nặng mục tiêu (kg)
        weekly_loss: Giảm bao nhiêu kg/tuần (mặc định 0.5)
    
    Returns:
        Dict với timeline và milestones
    """
    if current_weight <= target_weight:
        return {
            "error": "Cân nặng mục tiêu phải < cân nặng hiện tại"
        }
    
    if weekly_loss <= 0 or weekly_loss > 1:
        weekly_loss = 0.5  # Default safe rate
    
    total_loss = current_weight - target_weight
    weeks_needed = total_loss / weekly_loss
    months_needed = weeks_needed / 4.33  # Average weeks per month
    
    # Milestones (mỗi 5%)
    milestones = []
    for pct in [5, 10, 15, 20, 25]:
        milestone_weight = current_weight * (1 - pct/100)
        if milestone_weight >= target_weight:
            milestone_weeks = (current_weight - milestone_weight) / weekly_loss
            milestones.append({
                "percentage": pct,
                "weight": round(milestone_weight, 1),
                "weeks": round(milestone_weeks, 0),
                "benefits": get_milestone_benefits(pct)
            })
    
    return {
        "current_weight": current_weight,
        "target_weight": target_weight,
        "total_loss_kg": round(total_loss, 1),
        "weekly_loss_kg": weekly_loss,
        "weeks_needed": round(weeks_needed, 0),
        "months_needed": round(months_needed, 1),
        "estimated_date": f"Khoảng {round(months_needed, 0)} tháng",
        "milestones": milestones,
        "is_safe": weekly_loss <= 1,
        "recommendation": "Giảm 0.5-1kg/tuần là an toàn và bền vững"
    }


__all__ = ['get_weight_loss_timeline', 'get_milestone_benefits']
