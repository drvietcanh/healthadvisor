"""
Milestones - Mốc giảm cân và lợi ích
"""

from typing import List, Dict


def get_milestones(current_weight: float, target_weight: float) -> List[Dict]:
    """
    Tạo danh sách milestones
    
    Args:
        current_weight: Cân nặng hiện tại
        target_weight: Cân nặng mục tiêu
    
    Returns:
        List of milestone dicts
    """
    total_loss = current_weight - target_weight
    milestones = []
    
    for pct in [5, 10, 15, 20, 25]:
        loss_kg = current_weight * (pct / 100)
        milestone_weight = current_weight - loss_kg
        
        if milestone_weight >= target_weight:
            milestones.append({
                "percentage": pct,
                "weight": round(milestone_weight, 1),
                "loss_kg": round(loss_kg, 1),
                "benefits": get_milestone_benefits(pct),
                "celebration": get_celebration(pct)
            })
    
    return milestones


def get_milestone_benefits(percentage: int) -> List[str]:
    """Lợi ích khi đạt mốc giảm cân"""
    benefits = {
        5: [
            "✅ Giảm đường huyết rõ rệt",
            "✅ Giảm huyết áp 5-10 mmHg",
            "✅ Giảm triglyceride 20-30%",
            "✅ Cải thiện chất lượng ngủ",
            "✅ Tăng năng lượng"
        ],
        10: [
            "🎯 Giảm nguy cơ tiểu đường 50%",
            "🎯 Giảm huyết áp 10-20 mmHg",
            "🎯 Cải thiện lipid máu đáng kể",
            "🎯 Giảm đau khớp gối rõ rệt",
            "🎯 Tăng sức khỏe tim mạch",
            "🎯 Cải thiện tự tin, tâm lý"
        ],
        15: [
            "🏆 Đảo ngược tiền tiểu đường",
            "🏆 Có thể ngừng thuốc huyết áp (theo bác sĩ)",
            "🏆 Cải thiện đáng kể sức khỏe tim mạch",
            "🏆 Giảm size quần áo 2-3 size",
            "🏆 Tăng tuổi thọ 2-5 năm",
            "🏆 Cải thiện sức khỏe tình dục"
        ],
        20: [
            "👑 Sức khỏe tuyệt vời",
            "👑 Đảo ngược hầu hết biến chứng",
            "👑 Giảm nguy cơ ung thư",
            "👑 Chất lượng cuộc sống cao",
            "👑 Trẻ hóa 5-10 tuổi",
            "👑 Tự tin hoàn toàn"
        ],
        25: [
            "⭐ Hoàn hảo!",
            "⭐ Thành tích đáng tự hào",
            "⭐ Cảm hứng cho người khác",
            "⭐ Sống khỏe, sống vui"
        ]
    }
    return benefits.get(percentage, ["Tiếp tục phát huy!"])


def get_celebration(percentage: int) -> str:
    """Lời chúc mừng khi đạt mốc"""
    celebrations = {
        5: "🎈 Bước đầu thành công! Tự thưởng cho mình đi!",
        10: "🎉 Đã giảm 10%! Thật tuyệt vời!",
        15: "🎊 15% rồi! Bạn là nguồn cảm hứng!",
        20: "🏅 20%! Thành tích phi thường!",
        25: "👑 25%! Bạn là nhà vô địch!"
    }
    return celebrations.get(percentage, "🌟 Tiếp tục nào!")


__all__ = ['get_milestones', 'get_milestone_benefits', 'get_celebration']
