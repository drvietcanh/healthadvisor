"""
Exercise & Physical Activity - Vận động & Đốt cháy Calories
===========================================================

Tính calories đốt cháy, kế hoạch tập luyện cho người Việt
"""

from typing import Dict, List

# Calories đốt cháy theo hoạt động (cal/giờ cho người 70kg)
# Sẽ điều chỉnh theo cân nặng thực tế
EXERCISES_CALORIES = {
    "daily_activities": {
        "name": "🏠 Hoạt động Hàng ngày",
        "activities": {
            "Ngồi, xem TV": 60,
            "Đứng, nấu ăn": 100,
            "Làm việc nhà nhẹ": 150,
            "Lau nhà, quét nhà": 200,
            "Giặt quần áo tay": 180,
            "Làm vườn, tưới cây": 250,
            "Mua sắm đi bộ": 180,
        }
    },
    
    "walking": {
        "name": "🚶 Đi Bộ",
        "activities": {
            "Đi bộ chậm (3 km/h)": 150,
            "Đi bộ vừa (4 km/h)": 200,
            "Đi bộ nhanh (5 km/h)": 250,
            "Đi bộ rất nhanh (6 km/h)": 320,
            "Leo cầu thang": 400,
        }
    },
    
    "cardio": {
        "name": "🏃 Cardio",
        "activities": {
            "Chạy bộ chậm (6 km/h)": 350,
            "Chạy bộ vừa (8 km/h)": 450,
            "Chạy bộ nhanh (10 km/h)": 600,
            "Đạp xe chậm": 250,
            "Đạp xe vừa": 350,
            "Đạp xe nhanh": 500,
            "Bơi lội": 400,
            "Nhảy dây": 600,
        }
    },
    
    "sports": {
        "name": "⚽ Thể Thao",
        "activities": {
            "Cầu lông": 350,
            "Tennis": 400,
            "Bóng đá": 450,
            "Bóng chuyền": 300,
            "Bóng rổ": 400,
            "Bóng bàn": 250,
        }
    },
    
    "gym": {
        "name": "💪 Phòng Gym",
        "activities": {
            "Tập tạ nhẹ": 200,
            "Tập tạ nặng": 350,
            "Máy chạy bộ": 400,
            "Xe đạp tại chỗ": 300,
            "Aerobic": 350,
            "Zumba": 400,
        }
    },
    
    "gentle": {
        "name": "🧘 Nhẹ Nhàng (Cho người già)",
        "activities": {
            "Yoga": 180,
            "Thái cực quyền": 200,
            "Khiêu vũ chậm": 200,
            "Dạo chơi công viên": 150,
            "Vận động nhẹ tại nhà": 120,
        }
    }
}

# Mức độ vận động
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


def calculate_calories_burned(
    activity: str,
    duration_minutes: int,
    weight_kg: float = 70
) -> Dict:
    """
    Tính calories đốt cháy
    
    Args:
        activity: Tên hoạt động
        duration_minutes: Thời gian (phút)
        weight_kg: Cân nặng (kg) - mặc định 70kg
    
    Returns:
        Dict với calories burned và thông tin
    """
    # Tìm activity trong database
    base_calories_per_hour = None
    category_name = None
    
    for category_id, category_data in EXERCISES_CALORIES.items():
        if activity in category_data["activities"]:
            base_calories_per_hour = category_data["activities"][activity]
            category_name = category_data["name"]
            break
    
    if base_calories_per_hour is None:
        return {"error": f"Không tìm thấy hoạt động: {activity}"}
    
    # Điều chỉnh theo cân nặng (base = 70kg)
    # Calories tỷ lệ thuận với cân nặng
    weight_multiplier = weight_kg / 70
    adjusted_calories_per_hour = base_calories_per_hour * weight_multiplier
    
    # Tính theo thời gian
    calories_burned = (adjusted_calories_per_hour / 60) * duration_minutes
    
    # Tương đương món ăn
    food_equivalents = get_food_equivalents(calories_burned)
    
    return {
        "activity": activity,
        "category": category_name,
        "duration_minutes": duration_minutes,
        "weight_kg": weight_kg,
        "calories_burned": round(calories_burned, 0),
        "base_rate": base_calories_per_hour,
        "adjusted_rate": round(adjusted_calories_per_hour, 0),
        "food_equivalents": food_equivalents,
        "note": f"Người {weight_kg}kg {activity} {duration_minutes} phút"
    }


def get_food_equivalents(calories: float) -> List[str]:
    """Tương đương với món ăn Việt Nam"""
    equivalents = []
    
    foods = [
        (400, "1 bát phở"),
        (350, "1 bánh mì thịt"),
        (200, "1 bát cơm"),
        (150, "1 ly cà phê sữa"),
        (100, "1 hộp sữa chua"),
        (70, "1 quả trứng luộc"),
    ]
    
    for cal, food in foods:
        if calories >= cal * 0.9:  # Allow 10% tolerance
            portions = calories / cal
            if portions >= 1:
                equivalents.append(f"{portions:.1f} {food}")
    
    return equivalents[:3]  # Top 3


def get_exercise_plan(
    level: str,
    goal: str = "lose_weight",
    available_time: int = 30
) -> Dict:
    """
    Tạo kế hoạch tập luyện
    
    Args:
        level: "beginner", "intermediate", "advanced"
        goal: "lose_weight", "maintain", "build_muscle"
        available_time: Thời gian có (phút/ngày)
    
    Returns:
        Dict với weekly plan
    """
    level_info = EXERCISE_LEVELS.get(level, EXERCISE_LEVELS["beginner"])
    
    if goal == "lose_weight":
        # Focus cardio
        weekly_plan = {
            "monday": {
                "activity": "Đi bộ nhanh",
                "duration": min(available_time, 30),
                "type": "cardio",
                "note": "Khởi động tuần mới"
            },
            "tuesday": {
                "activity": "Làm vườn hoặc việc nhà",
                "duration": 30,
                "type": "daily",
                "note": "Hoạt động nhẹ"
            },
            "wednesday": {
                "activity": "Yoga hoặc Thái cực",
                "duration": min(available_time, 30),
                "type": "gentle",
                "note": "Thư giãn, dẻo dai"
            },
            "thursday": {
                "activity": "Đạp xe hoặc Bơi",
                "duration": min(available_time, 40),
                "type": "cardio",
                "note": "Đốt mỡ hiệu quả"
            },
            "friday": {
                "activity": "Đi bộ + Leo cầu thang",
                "duration": 30,
                "type": "cardio",
                "note": "Kết hợp nhiều động tác"
            },
            "saturday": {
                "activity": "Thể thao (cầu lông, bóng bàn...)",
                "duration": 45,
                "type": "sports",
                "note": "Vui vẻ, giao lưu"
            },
            "sunday": {
                "activity": "Nghỉ ngơi hoặc đi dạo nhẹ",
                "duration": 20,
                "type": "rest",
                "note": "Phục hồi cơ thể"
            }
        }
    
    elif goal == "maintain":
        weekly_plan = {
            "monday": {"activity": "Đi bộ", "duration": 30, "type": "cardio"},
            "wednesday": {"activity": "Yoga", "duration": 30, "type": "gentle"},
            "friday": {"activity": "Thể thao", "duration": 30, "type": "sports"},
            "sunday": {"activity": "Đi dạo", "duration": 30, "type": "gentle"}
        }
    
    else:  # build_muscle
        weekly_plan = {
            "monday": {"activity": "Tập tạ", "duration": 45, "type": "gym"},
            "tuesday": {"activity": "Cardio nhẹ", "duration": 20, "type": "cardio"},
            "wednesday": {"activity": "Tập tạ", "duration": 45, "type": "gym"},
            "thursday": {"activity": "Nghỉ", "duration": 0, "type": "rest"},
            "friday": {"activity": "Tập tạ", "duration": 45, "type": "gym"},
            "saturday": {"activity": "Cardio", "duration": 30, "type": "cardio"},
            "sunday": {"activity": "Nghỉ", "duration": 0, "type": "rest"}
        }
    
    # Tính tổng
    total_minutes = sum(day["duration"] for day in weekly_plan.values())
    estimated_calories = total_minutes * 5  # Rough estimate ~5 cal/min
    
    return {
        "level": level_info["name"],
        "goal": goal,
        "weekly_plan": weekly_plan,
        "total_minutes_per_week": total_minutes,
        "estimated_calories_burned": round(estimated_calories, 0),
        "tips": level_info["notes"]
    }


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

