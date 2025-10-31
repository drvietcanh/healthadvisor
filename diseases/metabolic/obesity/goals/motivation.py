"""
Motivation - Động viên và lời khuyên
"""

import random
from typing import List


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


__all__ = ['get_motivation_message', 'get_goal_recommendation', 'get_weekly_tips', 'get_daily_affirmations']
