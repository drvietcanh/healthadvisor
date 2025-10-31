"""
Exercise Levels - Mức độ vận động
Phân loại người mới bắt đầu, trung bình, nâng cao
"""

EXERCISE_LEVELS = {
    "beginner": {
        "name": "Người mới bắt đầu / Người già",
        "icon": "🐢",
        "duration": "15-30 phút/ngày",
        "frequency": "3-4 ngày/tuần",
        "intensity": "Nhẹ nhàng",
        "recommendations": [
            "Đi bộ chậm 15-20 phút",
            "Yoga, thái cực",
            "Làm vườn",
            "Vận động tại nhà",
        ],
        "notes": [
            "Bắt đầu từ nhẹ, tăng dần",
            "Không cố gắng quá sức",
            "Nghỉ ngơi khi mệt",
            "Tham khảo bác sĩ nếu có bệnh nền"
        ]
    },
    
    "intermediate": {
        "name": "Trung bình",
        "icon": "🚶",
        "duration": "30-45 phút/ngày",
        "frequency": "4-5 ngày/tuần",
        "intensity": "Vừa phải",
        "recommendations": [
            "Đi bộ nhanh 30 phút",
            "Đạp xe 30 phút",
            "Bơi lội 30 phút",
            "Tập gym nhẹ",
        ],
        "notes": [
            "Tập đều đặn mỗi tuần",
            "Kết hợp cardio + tạ nhẹ",
            "Tăng cường dần"
        ]
    },
    
    "advanced": {
        "name": "Nâng cao",
        "icon": "🏃",
        "duration": "45-60 phút/ngày",
        "frequency": "5-6 ngày/tuần",
        "intensity": "Cao",
        "recommendations": [
            "Chạy bộ 30-45 phút",
            "HIIT 20-30 phút",
            "Tập tạ nặng",
            "Thể thao đối kháng"
        ],
        "notes": [
            "Tập chuyên nghiệp",
            "Có người hướng dẫn",
            "Chế độ dinh dưỡng phù hợp"
        ]
    }
}

__all__ = ['EXERCISE_LEVELS']
