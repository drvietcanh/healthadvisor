"""
Activities Database - Database hoạt động và calories
Calories đốt cháy theo từng loại hoạt động
"""

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

__all__ = ['EXERCISES_CALORIES']
