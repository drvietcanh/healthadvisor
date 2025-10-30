"""
Goals & Motivation - Mục tiêu & Động lực
========================================

Đặt mục tiêu giảm cân, theo dõi tiến trình, động viên
"""

from typing import Dict, List, Optional
from datetime import datetime, timedelta
import random


def create_weight_loss_goal(
    current_weight: float,
    target_weight: float,
    target_date: Optional[str] = None,
    weekly_loss: float = 0.5
) -> Dict:
    """
    Tạo mục tiêu giảm cân
    
    Args:
        current_weight: Cân nặng hiện tại (kg)
        target_weight: Cân nặng mục tiêu (kg)
        target_date: Ngày mục tiêu (YYYY-MM-DD), None = tự tính
        weekly_loss: Giảm bao nhiêu kg/tuần (0.3-1.0)
    
    Returns:
        Dict với goal details
    """
    if current_weight <= target_weight:
        return {
            "error": "Cân nặng mục tiêu phải nhỏ hơn cân nặng hiện tại"
        }
    
    if weekly_loss < 0.3 or weekly_loss > 1.0:
        weekly_loss = 0.5  # Default safe rate
    
    total_loss = current_weight - target_weight
    weeks_needed = total_loss / weekly_loss
    
    # Tính ngày dự kiến hoàn thành
    today = datetime.now()
    if target_date:
        target_date_obj = datetime.strptime(target_date, "%Y-%m-%d")
        days_available = (target_date_obj - today).days
        weeks_available = days_available / 7
        
        # Kiểm tra có khả thi không
        if weeks_available < weeks_needed:
            suggested_date = today + timedelta(weeks=weeks_needed)
            return {
                "error": "Mục tiêu không khả thi",
                "reason": f"Cần {weeks_needed:.0f} tuần nhưng chỉ có {weeks_available:.0f} tuần",
                "suggestion": f"Nên đặt mục tiêu đến {suggested_date.strftime('%d/%m/%Y')}"
            }
    else:
        target_date_obj = today + timedelta(weeks=weeks_needed)
    
    # Tạo milestones
    milestones = []
    for pct in [5, 10, 15, 20, 25, 30]:
        if pct <= (total_loss / current_weight * 100):
            milestone_weight = current_weight * (1 - pct/100)
            if milestone_weight >= target_weight:
                weeks_to_milestone = (current_weight - milestone_weight) / weekly_loss
                milestone_date = today + timedelta(weeks=weeks_to_milestone)
                milestones.append({
                    "percentage": pct,
                    "weight": round(milestone_weight, 1),
                    "loss_from_start": round(current_weight - milestone_weight, 1),
                    "weeks": round(weeks_to_milestone, 0),
                    "date": milestone_date.strftime("%d/%m/%Y"),
                    "completed": False,
                    "benefits": get_milestone_benefits(pct)
                })
    
    return {
        "id": f"goal_{int(today.timestamp())}",
        "created_date": today.strftime("%Y-%m-%d"),
        "current_weight": current_weight,
        "target_weight": target_weight,
        "total_loss_needed": round(total_loss, 1),
        "weekly_loss_target": weekly_loss,
        "weeks_needed": round(weeks_needed, 0),
        "target_date": target_date_obj.strftime("%Y-%m-%d"),
        "target_date_display": target_date_obj.strftime("%d/%m/%Y"),
        "milestones": milestones,
        "status": "active",
        "is_safe": 0.3 <= weekly_loss <= 1.0,
        "recommendation": get_goal_recommendation(weekly_loss)
    }


def calculate_progress(
    goal: Dict,
    current_weight: float
) -> Dict:
    """
    Tính tiến trình đạt mục tiêu
    
    Args:
        goal: Goal dict từ create_weight_loss_goal()
        current_weight: Cân nặng hiện tại
    
    Returns:
        Dict với progress details
    """
    start_weight = goal["current_weight"]
    target_weight = goal["target_weight"]
    total_loss_needed = start_weight - target_weight
    
    # Tính đã giảm được bao nhiêu
    weight_lost = start_weight - current_weight
    weight_remaining = current_weight - target_weight
    
    # Phần trăm hoàn thành
    if total_loss_needed > 0:
        progress_pct = (weight_lost / total_loss_needed) * 100
    else:
        progress_pct = 0
    
    # Kiểm tra milestones đã đạt
    milestones_completed = []
    next_milestone = None
    
    for milestone in goal["milestones"]:
        if current_weight <= milestone["weight"]:
            milestone["completed"] = True
            milestones_completed.append(milestone)
        elif next_milestone is None:
            next_milestone = milestone
    
    # Tính tốc độ thực tế
    created_date = datetime.strptime(goal["created_date"], "%Y-%m-%d")
    days_elapsed = (datetime.now() - created_date).days
    weeks_elapsed = max(days_elapsed / 7, 0.1)  # Avoid division by zero
    actual_weekly_loss = weight_lost / weeks_elapsed if weight_lost > 0 else 0
    
    # Dự đoán ngày hoàn thành dựa trên tốc độ thực tế
    if actual_weekly_loss > 0:
        weeks_to_target = weight_remaining / actual_weekly_loss
        estimated_completion = datetime.now() + timedelta(weeks=weeks_to_target)
    else:
        estimated_completion = datetime.strptime(goal["target_date"], "%Y-%m-%d")
    
    # Đánh giá
    if progress_pct >= 100:
        status = "completed"
        message = "🎉 Chúc mừng! Bạn đã đạt mục tiêu!"
        color = "#66BB6A"
    elif progress_pct >= 75:
        status = "excellent"
        message = "💪 Xuất sắc! Sắp đến đích rồi!"
        color = "#4DA6FF"
    elif progress_pct >= 50:
        status = "good"
        message = "👍 Tốt lắm! Đã qua nửa chặng đường!"
        color = "#FFEB3B"
    elif progress_pct >= 25:
        status = "fair"
        message = "✊ Cố gắng! Đã có tiến bộ!"
        color = "#FF9800"
    elif progress_pct > 0:
        status = "started"
        message = "🌱 Khởi đầu tốt! Tiếp tục phát huy!"
        color = "#4DA6FF"
    else:
        status = "not_started"
        message = "🚀 Hãy bắt đầu hành trình!"
        color = "#999999"
    
    return {
        "progress_percentage": round(progress_pct, 1),
        "weight_lost": round(weight_lost, 1),
        "weight_remaining": round(weight_remaining, 1),
        "weeks_elapsed": round(weeks_elapsed, 1),
        "actual_weekly_loss": round(actual_weekly_loss, 2),
        "target_weekly_loss": goal["weekly_loss_target"],
        "on_track": abs(actual_weekly_loss - goal["weekly_loss_target"]) < 0.2,
        "milestones_completed": len(milestones_completed),
        "total_milestones": len(goal["milestones"]),
        "next_milestone": next_milestone,
        "estimated_completion": estimated_completion.strftime("%d/%m/%Y"),
        "original_target_date": goal["target_date_display"],
        "status": status,
        "message": message,
        "color": color,
        "motivation": get_motivation_message(status, progress_pct)
    }


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


def get_motivation_message(status: str = None, progress_pct: float = 0) -> str:
    """
    Lấy câu động viên
    
    Args:
        status: Status của tiến trình
        progress_pct: Phần trăm hoàn thành
    
    Returns:
        Motivational message
    """
    if status == "completed":
        messages = [
            "🎉 Chúc mừng! Bạn đã hoàn thành mục tiêu! Tự hào về bản thân nhé!",
            "👑 Xuất sắc! Bạn đã chứng minh sức mạnh của ý chí!",
            "⭐ Thật tuyệt vời! Giờ hãy duy trì thành quả này!"
        ]
    elif progress_pct >= 75:
        messages = [
            "💪 Sắp đến đích rồi! Đừng bỏ cuộc bây giờ!",
            "🔥 Bạn làm được! Chỉ còn chút nữa thôi!",
            "⚡ Tiếp tục phấn đấu! Victory is near!"
        ]
    elif progress_pct >= 50:
        messages = [
            "👍 Đã đi được nửa đường! Bạn rất giỏi!",
            "🌟 Tốt lắm! Momentum đang ở bên bạn!",
            "💫 Cứ giữ nhịp này! Bạn sẽ thành công!"
        ]
    elif progress_pct >= 25:
        messages = [
            "✊ Đã có tiến bộ! Từng bước nhỏ, thành quả lớn!",
            "🌱 Đang trên đường đúng! Kiên trì là chìa khóa!",
            "💚 Bạn làm rất tốt! Hãy tin vào quá trình!"
        ]
    elif progress_pct > 0:
        messages = [
            "🚀 Khởi đầu tốt! Every journey begins with a single step!",
            "🌻 Bước đầu thành công! Tiếp tục nào!",
            "💙 Bạn đã bắt đầu - đó là điều quan trọng nhất!"
        ]
    else:
        messages = [
            "💪 Hãy bắt đầu hôm nay! Bạn làm được!",
            "🔥 Đừng trì hoãn! Hành trình ngàn dặm bắt đầu từ bước chân đầu tiên!",
            "⭐ Tin vào bản thân! Hãy bắt đầu ngay bây giờ!"
        ]
    
    return random.choice(messages)


def get_goal_recommendation(weekly_loss: float) -> str:
    """Khuyến nghị về tốc độ giảm cân"""
    if weekly_loss < 0.3:
        return "⚠️ Quá chậm - có thể tăng cường thêm tập luyện"
    elif weekly_loss <= 0.5:
        return "✅ Tốc độ AN TOÀN và BỀN VỮNG - Phù hợp người già"
    elif weekly_loss <= 0.75:
        return "✅ Tốc độ TỐT - Cân bằng giữa hiệu quả và an toàn"
    elif weekly_loss <= 1.0:
        return "⚠️ Tốc độ NHANH - Cần giám sát sức khỏe, đảm bảo dinh dưỡng"
    else:
        return "🚫 QUÁ NHANH - Nguy hiểm! Nên giảm xuống 0.5-1kg/tuần"


def get_weekly_tips() -> List[str]:
    """Tips động viên hàng tuần"""
    return [
        "📸 Chụp ảnh tiến trình mỗi tuần - Bạn sẽ thấy sự khác biệt!",
        "📝 Ghi nhật ký ăn uống - Viết ra để kiểm soát tốt hơn!",
        "👥 Tìm bạn đồng hành - Cùng nhau vượt qua khó khăn!",
        "🎯 Đặt mục tiêu nhỏ mỗi tuần - Dễ đạt, dễ tạo động lực!",
        "🎁 Tự thưởng khi đạt mốc - Nhưng không phải bằng đồ ăn nhé!",
        "💪 Nhớ rằng: Progress > Perfection!",
        "🌟 Mỗi ngày tốt hơn 1% = 1 năm tốt hơn 3,700%!",
        "🔥 Thất bại là một phần của thành công - Đừng bỏ cuộc!",
        "💚 Yêu bản thân, chăm sóc sức khỏe - Đó là đầu tư tốt nhất!",
        "🌈 Hãy tập trung vào cảm giác khỏe mạnh, không chỉ con số!"
    ]


def get_daily_affirmations() -> List[str]:
    """Lời khẳng định tích cực hàng ngày"""
    return [
        "💪 Hôm nay tôi chọn sức khỏe",
        "🌟 Tôi đang trở nên khỏe mạnh hơn mỗi ngày",
        "✨ Cơ thể tôi xứng đáng được chăm sóc tốt nhất",
        "🎯 Tôi có khả năng đạt mục tiêu của mình",
        "💚 Tôi yêu và tôn trọng cơ thể mình",
        "🔥 Tôi mạnh mẽ hơn tôi nghĩ",
        "🌈 Mỗi bước nhỏ đều quan trọng",
        "⭐ Tôi xứng đáng có một cuộc sống khỏe mạnh",
        "💫 Tôi kiên trì và không bỏ cuộc",
        "🌻 Tôi chọn tiến bộ, không phải hoàn hảo"
    ]


def calculate_bmi_goal(height_cm: float, target_bmi: float = 22.0) -> Dict:
    """
    Tính cân nặng mục tiêu dựa trên BMI
    
    Args:
        height_cm: Chiều cao (cm)
        target_bmi: BMI mục tiêu (mặc định 22 - trung tâm khỏe mạnh châu Á)
    
    Returns:
        Dict với target weight và info
    """
    if target_bmi < 18.5 or target_bmi > 23.0:
        recommendation = "Khuyến nghị BMI 18.5-23.0 cho người Việt Nam/Châu Á"
    else:
        recommendation = "BMI mục tiêu nằm trong vùng khỏe mạnh"
    
    height_m = height_cm / 100
    target_weight = target_bmi * (height_m ** 2)
    
    # Range khỏe mạnh
    healthy_min = 18.5 * (height_m ** 2)
    healthy_max = 23.0 * (height_m ** 2)
    
    return {
        "target_bmi": target_bmi,
        "target_weight": round(target_weight, 1),
        "healthy_range": (round(healthy_min, 1), round(healthy_max, 1)),
        "recommendation": recommendation,
        "note": "Chuẩn Việt Nam/Châu Á: BMI 18.5-23.0 là khỏe mạnh"
    }

