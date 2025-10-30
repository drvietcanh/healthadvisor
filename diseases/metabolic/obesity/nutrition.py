"""
Nutrition & Calories - Dinh dưỡng & Calories
============================================

Database thực phẩm Việt Nam, tính calories, meal planning
"""

from typing import Dict, List, Optional

# Database thực phẩm Việt Nam với calories
VIETNAMESE_FOODS = {
    "breakfast": {
        "name": "Món Sáng",
        "foods": {
            "Phở bò": {"calories": 400, "protein": 20, "carbs": 60, "fat": 8},
            "Phở gà": {"calories": 350, "protein": 18, "carbs": 55, "fat": 6},
            "Bánh mì thịt": {"calories": 350, "protein": 15, "carbs": 45, "fat": 12},
            "Bánh mì pate": {"calories": 280, "protein": 10, "carbs": 40, "fat": 10},
            "Bún bò Huế": {"calories": 500, "protein": 22, "carbs": 65, "fat": 14},
            "Bún chả": {"calories": 450, "protein": 20, "carbs": 60, "fat": 12},
            "Xôi thịt": {"calories": 380, "protein": 12, "carbs": 65, "fat": 8},
            "Xôi xéo": {"calories": 320, "protein": 8, "carbs": 55, "fat": 8},
            "Bánh cuốn": {"calories": 200, "protein": 8, "carbs": 35, "fat": 4},
            "Cháo gà": {"calories": 180, "protein": 10, "carbs": 28, "fat": 3},
            "Mì trộn": {"calories": 420, "protein": 15, "carbs": 60, "fat": 12},
            "Hủ tiếu": {"calories": 380, "protein": 15, "carbs": 55, "fat": 10},
        }
    },
    
    "lunch_dinner": {
        "name": "Món Chính (Trưa/Tối)",
        "foods": {
            "Cơm tấm": {"calories": 600, "protein": 25, "carbs": 85, "fat": 15},
            "Cơm gà": {"calories": 550, "protein": 30, "carbs": 75, "fat": 12},
            "Cơm sườn": {"calories": 650, "protein": 28, "carbs": 80, "fat": 20},
            "Cơm rang": {"calories": 520, "protein": 18, "carbs": 70, "fat": 16},
            "Bún riêu": {"calories": 420, "protein": 18, "carbs": 60, "fat": 10},
            "Bún thịt nướng": {"calories": 480, "protein": 22, "carbs": 65, "fat": 12},
            "Mì Quảng": {"calories": 450, "protein": 20, "carbs": 60, "fat": 11},
            "Cao lầu": {"calories": 480, "protein": 18, "carbs": 65, "fat": 13},
            "Bánh xèo": {"calories": 380, "protein": 12, "carbs": 50, "fat": 14},
            "Nem rán (10 cái)": {"calories": 500, "protein": 15, "carbs": 40, "fat": 30},
            "Lẩu (1 người)": {"calories": 450, "protein": 25, "carbs": 35, "fat": 18},
        }
    },
    
    "side_dishes": {
        "name": "Món Phụ",
        "foods": {
            "Cơm trắng (1 bát)": {"calories": 200, "protein": 4, "carbs": 45, "fat": 0.5},
            "Canh chua": {"calories": 120, "protein": 8, "carbs": 15, "fat": 3},
            "Rau luộc": {"calories": 50, "protein": 3, "carbs": 8, "fat": 1},
            "Đậu hũ chiên": {"calories": 180, "protein": 12, "carbs": 8, "fat": 12},
            "Thịt kho tàu (100g)": {"calories": 250, "protein": 18, "carbs": 10, "fat": 16},
            "Cá kho (100g)": {"calories": 200, "protein": 20, "carbs": 8, "fat": 10},
            "Trứng luộc (1 quả)": {"calories": 70, "protein": 6, "carbs": 1, "fat": 5},
            "Trứng chiên (1 quả)": {"calories": 110, "protein": 6, "carbs": 1, "fat": 9},
        }
    },
    
    "snacks": {
        "name": "Món Vặt",
        "foods": {
            "Gỏi cuốn (1 cuốn)": {"calories": 70, "protein": 4, "carbs": 10, "fat": 2},
            "Chả giò (1 cái)": {"calories": 80, "protein": 3, "carbs": 8, "fat": 4},
            "Bánh bao (1 cái)": {"calories": 200, "protein": 6, "carbs": 30, "fat": 6},
            "Bánh pía (1 cái)": {"calories": 180, "protein": 4, "carbs": 28, "fat": 6},
            "Bánh flan": {"calories": 150, "protein": 4, "carbs": 22, "fat": 5},
            "Sữa chua": {"calories": 100, "protein": 5, "carbs": 15, "fat": 2},
            "Trái cây (1 phần)": {"calories": 80, "protein": 1, "carbs": 20, "fat": 0},
        }
    },
    
    "drinks": {
        "name": "Đồ Uống",
        "foods": {
            "Cà phê đen": {"calories": 5, "protein": 0, "carbs": 1, "fat": 0},
            "Cà phê sữa": {"calories": 150, "protein": 3, "carbs": 18, "fat": 7},
            "Trà sữa trân châu": {"calories": 350, "protein": 5, "carbs": 55, "fat": 12},
            "Sinh tố": {"calories": 180, "protein": 3, "carbs": 35, "fat": 4},
            "Nước mía": {"calories": 120, "protein": 1, "carbs": 30, "fat": 0},
            "Nước dừa": {"calories": 50, "protein": 1, "carbs": 12, "fat": 0},
            "Nước ngọt (330ml)": {"calories": 140, "protein": 0, "carbs": 35, "fat": 0},
            "Bia (330ml)": {"calories": 150, "protein": 1, "carbs": 13, "fat": 0},
        }
    }
}

# Phân loại thực phẩm theo mục đích
FOOD_CATEGORIES = {
    "high_protein": {
        "name": "🥩 Giàu Protein (Tốt cho giảm cân)",
        "foods": [
            "Thịt gà luộc/nướng",
            "Cá hấp/nướng",
            "Đậu hũ",
            "Trứng",
            "Tôm",
            "Mực",
            "Sữa không đường"
        ],
        "tip": "Protein giúp no lâu, duy trì cơ bắp khi giảm cân"
    },
    
    "low_calorie": {
        "name": "🥗 Ít Calories (Nên ăn nhiều)",
        "foods": [
            "Rau xanh các loại",
            "Canh chua",
            "Gỏi cuốn",
            "Cháo",
            "Súp",
            "Trái cây (trừ sầu riêng, mít)"
        ],
        "tip": "Ăn nhiều rau → No bụng mà ít calories"
    },
    
    "healthy_carbs": {
        "name": "🍚 Tinh bột Lành mạnh",
        "foods": [
            "Cơm gạo lứt",
            "Khoai lang",
            "Yến mạch",
            "Bí đỏ",
            "Ngô"
        ],
        "tip": "Thay cơm trắng bằng gạo lứt giảm calories 10-15%"
    },
    
    "avoid_high_calorie": {
        "name": "🚫 Tránh (Calories Cao)",
        "foods": [
            "Đồ chiên rán (nem, chả giò, bánh rán)",
            "Trà sữa",
            "Nước ngọt",
            "Bánh ngọt",
            "Thức ăn nhanh",
            "Mỡ, da gà",
            "Nội tạng"
        ],
        "tip": "1 ly trà sữa = 2 bát cơm về calories!"
    },
    
    "portion_control": {
        "name": "⚖️ Kiểm soát khẩu phần",
        "foods": [
            "Dùng đĩa/bát nhỏ hơn",
            "Ăn 50% rau, 25% protein, 25% tinh bột",
            "Nhai chậm 20-30 lần/miếng",
            "Uống nước trước bữa ăn",
            "Dừng khi no 80%"
        ],
        "tip": "Khẩu phần nhỏ hơn 20% → Giảm cân mà không đói"
    }
}

def calculate_daily_calories(
    tdee: float,
    goal: str = "maintain"
) -> Dict:
    """
    Tính calories cần thiết mỗi ngày
    
    Args:
        tdee: Total Daily Energy Expenditure
        goal: "lose_slow", "lose_moderate", "lose_fast", "maintain", "gain"
    
    Returns:
        Dict với calories và breakdown
    """
    goals_deficit = {
        "lose_slow": -300,      # -0.3kg/tuần (cho người già)
        "lose_moderate": -500,  # -0.5kg/tuần
        "lose_fast": -750,      # -0.75kg/tuần
        "maintain": 0,
        "gain": +300
    }
    
    deficit = goals_deficit.get(goal, 0)
    target_calories = tdee + deficit
    
    # Không < 1200 cal cho nữ, 1500 cho nam
    min_calories = 1200
    if target_calories < min_calories:
        target_calories = min_calories
    
    # Chia calories theo bữa (VN thường ăn 3 bữa chính)
    breakfast = target_calories * 0.30  # 30% sáng
    lunch = target_calories * 0.40      # 40% trưa
    dinner = target_calories * 0.25     # 25% tối
    snacks = target_calories * 0.05     # 5% vặt
    
    return {
        "daily_calories": round(target_calories, 0),
        "breakfast": round(breakfast, 0),
        "lunch": round(lunch, 0),
        "dinner": round(dinner, 0),
        "snacks": round(snacks, 0),
        "macros": {
            "protein": round(target_calories * 0.30 / 4, 0),  # 30% protein, 4cal/g
            "carbs": round(target_calories * 0.40 / 4, 0),    # 40% carbs, 4cal/g
            "fat": round(target_calories * 0.30 / 9, 0),      # 30% fat, 9cal/g
        },
        "note": "Tỷ lệ 30-40-30 (P-C-F) phù hợp giảm cân"
    }


def get_meal_plan(daily_calories: float, meal_type: str = "balanced") -> Dict:
    """
    Gợi ý thực đơn theo calories
    
    Args:
        daily_calories: Calories mục tiêu mỗi ngày
        meal_type: "balanced", "low_carb", "vegetarian"
    
    Returns:
        Dict với meal suggestions
    """
    breakfast_cal = daily_calories * 0.30
    lunch_cal = daily_calories * 0.40
    dinner_cal = daily_calories * 0.25
    
    # Gợi ý món ăn phù hợp calories
    if meal_type == "balanced":
        return {
            "breakfast": {
                "target_calories": round(breakfast_cal, 0),
                "suggestions": [
                    "Phở gà (350 cal) + Cà phê đen (5 cal)",
                    "Bánh mì pate (280 cal) + Sữa chua (100 cal)",
                    "Cháo gà (180 cal) + Trứng luộc (70 cal) + Trái cây (80 cal)"
                ]
            },
            "lunch": {
                "target_calories": round(lunch_cal, 0),
                "suggestions": [
                    "Cơm gà (550 cal) + Rau luộc (50 cal)",
                    "Bún thịt nướng (480 cal) + Gỏi cuốn 2 cuốn (140 cal)",
                    "Cơm + Cá kho (200 cal) + Canh chua (120 cal) + Rau (50 cal)"
                ]
            },
            "dinner": {
                "target_calories": round(dinner_cal, 0),
                "suggestions": [
                    "Cháo gà (180 cal) + Rau luộc (50 cal)",
                    "Bún riêu (420 cal)",
                    "Cơm (200 cal) + Đậu hũ chiên (180 cal) + Canh (120 cal)"
                ]
            },
            "snacks": {
                "suggestions": [
                    "Trái cây (80 cal)",
                    "Sữa chua (100 cal)",
                    "Gỏi cuốn 1 cuốn (70 cal)"
                ]
            }
        }
    
    elif meal_type == "low_carb":
        return {
            "note": "Giảm tinh bột, tăng protein",
            "breakfast": {
                "suggestions": [
                    "Trứng chiên 2 quả (220 cal) + Rau luộc (50 cal)",
                    "Cháo gà (180 cal)"
                ]
            },
            "lunch": {
                "suggestions": [
                    "Thịt/Cá nướng (250 cal) + Rau nhiều (100 cal) + Cơm ít (100 cal)",
                    "Lẩu (450 cal) - ăn ít bún"
                ]
            },
            "dinner": {
                "suggestions": [
                    "Gỏi cuốn (140 cal) + Canh (120 cal)",
                    "Salad gà (300 cal)"
                ]
            }
        }
    
    else:  # vegetarian
        return {
            "note": "Chay - tập trung đậu hũ, nấm, rau",
            "breakfast": {
                "suggestions": [
                    "Xôi xéo (320 cal)",
                    "Bánh cuốn chay (200 cal) + Nước dừa (50 cal)"
                ]
            },
            "lunch": {
                "suggestions": [
                    "Cơm (200 cal) + Đậu hũ chiên (180 cal) + Rau (100 cal) + Canh (80 cal)",
                    "Bún riêu chay (380 cal)"
                ]
            },
            "dinner": {
                "suggestions": [
                    "Canh chua chay (100 cal) + Rau luộc (50 cal) + Cơm ít (150 cal)"
                ]
            }
        }


def get_nutrition_tips() -> List[Dict]:
    """Lời khuyên dinh dưỡng cho người Việt giảm cân"""
    return [
        {
            "title": "🍚 Giảm cơm, tăng rau",
            "detail": "Thay vì 1 bát cơm đầy → 2/3 bát + rau nhiều",
            "benefit": "Giảm 100-150 cal/bữa"
        },
        {
            "title": "🥤 Bỏ đồ uống có đường",
            "detail": "Trà sữa, nước ngọt, cà phê sữa → Nước lọc, trà không đường",
            "benefit": "Giảm 300-500 cal/ngày"
        },
        {
            "title": "🍗 Chọn thịt nạc, không da",
            "detail": "Gà bỏ da, thịt nạc, cá → Tránh mỡ, da, nội tạng",
            "benefit": "Giảm 200 cal/bữa"
        },
        {
            "title": "🔥 Hạn chế chiên rán",
            "detail": "Hấp, luộc, nướng thay vì chiên",
            "benefit": "Giảm 30-50% calories"
        },
        {
            "title": "🕐 Ăn tối sớm (trước 7h)",
            "detail": "Tránh ăn khuya → Không tích mỡ",
            "benefit": "Giảm cân hiệu quả hơn 20%"
        },
        {
            "title": "💧 Uống nước trước ăn",
            "detail": "Uống 1-2 cốc nước 30 phút trước bữa ăn",
            "benefit": "No nhanh hơn, ăn ít hơn 15-20%"
        },
        {
            "title": "🥢 Nhai chậm, ăn chậm",
            "detail": "Mỗi miếng nhai 20-30 lần, ăn ít nhất 20 phút/bữa",
            "benefit": "Não kịp nhận tín hiệu no → Ăn ít hơn"
        },
        {
            "title": "📝 Ghi nhật ký ăn uống",
            "detail": "Viết ra tất cả món ăn trong ngày",
            "benefit": "Nhận thức rõ → Kiểm soát tốt hơn"
        }
    ]


def find_food_calories(food_name: str) -> Optional[Dict]:
    """
    Tìm calories của món ăn
    
    Args:
        food_name: Tên món ăn
    
    Returns:
        Dict với calories và macros, hoặc None
    """
    food_name_lower = food_name.lower()
    
    for category_id, category_data in VIETNAMESE_FOODS.items():
        for food, nutrition in category_data["foods"].items():
            if food.lower() in food_name_lower or food_name_lower in food.lower():
                return {
                    "name": food,
                    "category": category_data["name"],
                    **nutrition
                }
    
    return None


def calculate_meal_calories(foods: List[str]) -> Dict:
    """
    Tính tổng calories của một bữa ăn
    
    Args:
        foods: Danh sách các món ăn
    
    Returns:
        Dict với total calories và breakdown
    """
    total_cal = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0
    found_foods = []
    not_found = []
    
    for food in foods:
        result = find_food_calories(food)
        if result:
            total_cal += result["calories"]
            total_protein += result["protein"]
            total_carbs += result["carbs"]
            total_fat += result["fat"]
            found_foods.append(result)
        else:
            not_found.append(food)
    
    return {
        "total_calories": total_cal,
        "macros": {
            "protein": round(total_protein, 1),
            "carbs": round(total_carbs, 1),
            "fat": round(total_fat, 1)
        },
        "foods": found_foods,
        "not_found": not_found,
        "count": len(found_foods)
    }

