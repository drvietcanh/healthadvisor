"""
Gout Diet - Chế độ ăn cho người bị Gút
"""

GOUT_DIET = {
    "title": "🍽️ Chế Độ Ăn Cho Người Bị Gút",
    
    "avoid": {
        "title": "❌ TRÁNH (Acid uric cao):",
        "foods": [
            {
                "category": "Nội tạng",
                "examples": "Gan, thận, tim, lòng",
                "purine_level": "Rất cao",
                "note": "TRÁNH TUYỆT ĐỐI"
            },
            {
                "category": "Hải sản",
                "examples": "Tôm, cua, cá mòi, cá cơm, cá trích",
                "purine_level": "Cao",
                "note": "Hạn chế tối đa"
            },
            {
                "category": "Thịt đỏ",
                "examples": "Thịt bò, heo, cừu",
                "purine_level": "Trung bình-Cao",
                "note": "Hạn chế, <150g/ngày"
            },
            {
                "category": "Rượu bia",
                "examples": "Tất cả các loại",
                "purine_level": "Ngăn thải acid uric",
                "note": "TRÁNH, đặc biệt bia!"
            },
            {
                "category": "Nước ngọt có đường",
                "examples": "Coca, Pepsi, nước ngọt",
                "why": "Fructose → Tăng acid uric",
                "note": "Tránh"
            }
        ]
    },
    
    "limit": {
        "title": "⚠️ HẠN CHẾ:",
        "foods": [
            {
                "food": "Thịt gia cầm (gà, vịt)",
                "amount": "<150g/ngày",
                "note": "Tốt hơn thịt đỏ"
            },
            {
                "food": "Cá nước ngọt",
                "amount": "<100g/ngày",
                "note": "Tránh cá mòi, cá cơm"
            },
            {
                "food": "Đậu phụ, đậu hũ",
                "amount": "Vừa phải",
                "note": "Purine thấp, ăn được"
            }
        ]
    },
    
    "recommended": {
        "title": "✅ NÊN ĂN:",
        "foods": [
            {
                "food": "Rau xanh",
                "examples": "Tất cả các loại",
                "why": "Purine thấp, tốt cho sức khỏe",
                "note": "Ăn nhiều"
            },
            {
                "food": "Trái cây",
                "examples": "Tất cả (tránh quá ngọt)",
                "why": "Vitamin C giúp giảm acid uric",
                "note": "Đặc biệt cam, dâu"
            },
            {
                "food": "Sữa ít béo",
                "why": "Giảm acid uric",
                "note": "1-2 ly/ngày"
            },
            {
                "food": "Cà phê",
                "why": "Giảm nguy cơ gút (nghiên cứu)",
                "note": "1-2 ly/ngày, không đường"
            },
            {
                "food": "Anh đào (cherry)",
                "why": "Giảm acid uric, giảm cơn gút",
                "note": "Có thể ăn hàng ngày"
            }
        ]
    },
    
    "drinking": {
        "title": "💧 Uống nước:",
        "importance": "Uống nhiều nước → Thải acid uric",
        "amount": "2-3 lít/ngày",
        "what": "Nước lọc, nước khoáng, trà xanh",
        "avoid": "Rượu bia, nước ngọt"
    },
    
    "during_attack": {
        "title": "Khi đang có cơn gút:",
        "diet": [
            "Chỉ ăn cháo, súp nhẹ",
            "Uống nhiều nước (3-4 lít/ngày)",
            "TRÁNH tất cả thịt, hải sản",
            "TRÁNH rượu bia tuyệt đối"
        ]
    }
}

