"""
Food Database - Database thực phẩm Việt Nam với calories
"""

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

__all__ = ['VIETNAMESE_FOODS', 'FOOD_CATEGORIES']
