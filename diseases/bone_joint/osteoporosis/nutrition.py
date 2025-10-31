"""
Osteoporosis Nutrition - Dinh Dưỡng Cho Xương Chắc
"""

NUTRITION = {
    "title": "🍽️ Thực Phẩm Tốt Cho Xương",
    
    "calcium_rich_foods": {
        "title": "Thực Phẩm Giàu Canxi:",
        "foods": [
            {
                "name": "Sữa và sản phẩm từ sữa",
                "examples": ["Sữa tươi", "Sữa chua", "Phô mai"],
                "calcium": "300mg/100ml sữa",
                "serving": "1 ly sữa (200ml) = 600mg canxi",
                "tip": "Chọn sữa ít béo nếu lo béo phì"
            },
            {
                "name": "Cá nhỏ ăn cả xương",
                "examples": ["Cá cơm", "Cá mòi", "Cá trích"],
                "calcium": "200-400mg/100g",
                "tip": "Nấu mềm, ăn cả xương"
            },
            {
                "name": "Rau xanh đậm",
                "examples": ["Rau cải xoăn", "Rau chân vịt", "Bông cải xanh"],
                "calcium": "100-200mg/100g",
                "tip": "Nấu chín để dễ hấp thu"
            },
            {
                "name": "Đậu phụ",
                "calcium": "100-150mg/100g",
                "tip": "Nguồn canxi tốt cho người không uống sữa"
            },
            {
                "name": "Hạnh nhân",
                "calcium": "200mg/100g",
                "tip": "Ăn vặt tốt cho xương"
            },
            {
                "name": "Tôm, cua",
                "calcium": "100-150mg/100g",
                "tip": "Ăn cả vỏ (nếu mềm)"
            }
        ]
    },
    
    "vitamin_d_foods": {
        "title": "Thực Phẩm Giàu Vitamin D:",
        "foods": [
            {
                "name": "Cá béo",
                "examples": ["Cá hồi", "Cá thu", "Cá ngừ"],
                "vitamin_d": "400-800 IU/100g"
            },
            {
                "name": "Lòng đỏ trứng",
                "vitamin_d": "40 IU/quả"
            },
            {
                "name": "Sữa bổ sung vitamin D",
                "vitamin_d": "100-150 IU/100ml"
            },
            {
                "name": "Nấm",
                "vitamin_d": "Nếu được phơi nắng"
            }
        ],
        "sunlight": {
            "title": "☀️ Quan Trọng Nhất: Ánh Nắng Mặt Trời",
            "how": "Phơi nắng 15-20 phút/ngày (tay, chân)",
            "time": "Trước 9h sáng hoặc sau 4h chiều",
            "note": "Da tạo vitamin D khi tiếp xúc ánh nắng!"
        }
    },
    
    "daily_requirements": {
        "title": "Nhu Cầu Hàng Ngày:",
        "calcium": {
            "adult": "1,000mg/ngày",
            "women_50": "1,200mg/ngày",
            "men_70": "1,200mg/ngày"
        },
        "vitamin_d": {
            "adult_50": "800-1,000 IU/ngày",
            "adult_70": "1,000-2,000 IU/ngày"
        }
    },
    
    "foods_to_avoid": {
        "title": "Thực Phẩm Nên Hạn Chế:",
        "items": [
            {
                "food": "Muối quá nhiều",
                "reason": "Làm canxi thải ra nước tiểu"
            },
            {
                "food": "Cà phê, trà quá nhiều",
                "reason": "Caffein → Mất canxi"
            },
            {
                "food": "Rượu bia",
                "reason": "Ức chế hấp thu canxi"
            },
            {
                "food": "Đồ uống có gas",
                "reason": "Phospho cao → Cản trở canxi"
            }
        ]
    },
    
    "sample_menu": {
        "title": "💡 Thực Đơn Mẫu (Đủ Canxi):",
        "breakfast": [
            "1 ly sữa tươi (600mg canxi)",
            "Bánh mì + Phô mai (100mg)",
            "= 700mg canxi"
        ],
        "lunch": [
            "Cơm + Cá mòi (200mg)",
            "Rau cải xanh (100mg)",
            "= 300mg canxi"
        ],
        "dinner": [
            "Đậu phụ xào (150mg)",
            "Tôm rim (100mg)",
            "= 250mg canxi"
        ],
        "total": "Tổng: ~1,250mg canxi/ngày ✅"
    }
}

