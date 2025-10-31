"""
Safety Tips & Exercise by Location - Mẹo an toàn và bài tập theo địa điểm
"""

from typing import Dict, List


def get_safe_exercise_tips() -> List[Dict]:
    """Lời khuyên tập luyện an toàn cho người Việt"""
    return [
        {
            "title": "🌅 Tập buổi sáng hoặc chiều mát",
            "detail": "Tránh tập lúc trưa nắng nóng (11h-15h)",
            "reason": "Phòng say nắng, mất nước"
        },
        {
            "title": "💧 Uống đủ nước",
            "detail": "Uống 250ml trước, trong và sau tập",
            "reason": "Phòng mất nước, chuột rút"
        },
        {
            "title": "🏃 Khởi động 5-10 phút",
            "detail": "Giãn cơ, khởi động nhẹ trước khi tập chính",
            "reason": "Tránh chấn thương cơ, khớp"
        },
        {
            "title": "👟 Mang giày thể thao phù hợp",
            "detail": "Giày êm, chống trơn, vừa vặn",
            "reason": "Bảo vệ khớp gối, mắt cá chân"
        },
        {
            "title": "🩺 Kiểm tra sức khỏe trước khi tập",
            "detail": "Người >50 tuổi hoặc có bệnh nền nên khám bác sĩ",
            "reason": "Đảm bảo an toàn, tránh biến chứng"
        },
        {
            "title": "📈 Tăng cường độ từ từ",
            "detail": "Tăng 10-15% mỗi tuần",
            "reason": "Cơ thể cần thời gian thích nghi"
        },
        {
            "title": "🛌 Nghỉ ngơi đầy đủ",
            "detail": "Ít nhất 1-2 ngày nghỉ/tuần",
            "reason": "Cơ bắp cần thời gian phục hồi"
        },
        {
            "title": "🚨 Dừng ngay nếu có dấu hiệu bất thường",
            "detail": "Đau ngực, chóng mặt, khó thở, đau khớp",
            "reason": "An toàn là trên hết"
        }
    ]


def get_exercise_by_location() -> Dict:
    """Bài tập theo địa điểm - phù hợp Việt Nam"""
    return {
        "at_home": {
            "name": "🏠 Tại nhà (không cần dụng cụ)",
            "exercises": [
                {"name": "Chống đẩy", "reps": "10-15 lần x 3 hiệp", "calories": 100},
                {"name": "Gập bụng", "reps": "15-20 lần x 3 hiệp", "calories": 80},
                {"name": "Squat", "reps": "15-20 lần x 3 hiệp", "calories": 120},
                {"name": "Plank", "reps": "30-60 giây x 3 hiệp", "calories": 100},
                {"name": "Nhảy tại chỗ", "reps": "1 phút x 5 lần", "calories": 150},
            ],
            "total_time": "20-30 phút",
            "total_calories": "~250 cal"
        },
        
        "park": {
            "name": "🌳 Công viên",
            "exercises": [
                {"name": "Đi bộ nhanh", "duration": "20 phút", "calories": 100},
                {"name": "Chạy bộ nhẹ", "duration": "15 phút", "calories": 150},
                {"name": "Thái cực quyền", "duration": "20 phút", "calories": 120},
                {"name": "Khiêu vũ", "duration": "20 phút", "calories": 130},
            ],
            "note": "Hít thở không khí trong lành, gặp gỡ bạn bè"
        },
        
        "stairs": {
            "name": "🪜 Cầu thang (tại nhà/chung cư)",
            "exercises": [
                {"name": "Leo lên xuống cầu thang", "duration": "10 phút", "calories": 150},
                {"name": "Bước lên xuống bậc thang", "reps": "50 lần", "calories": 80},
            ],
            "note": "Đốt cháy calories nhanh, tốt cho tim mạch"
        },
        
        "gym": {
            "name": "💪 Phòng gym / CLB thể thao",
            "exercises": [
                {"name": "Máy chạy bộ", "duration": "20 phút", "calories": 200},
                {"name": "Xe đạp", "duration": "20 phút", "calories": 150},
                {"name": "Tạ nhẹ", "duration": "20 phút", "calories": 120},
                {"name": "Aerobic/Zumba", "duration": "30 phút", "calories": 250},
            ],
            "note": "Có HLV hướng dẫn, thiết bị đầy đủ"
        }
    }


__all__ = ['get_safe_exercise_tips', 'get_exercise_by_location']
