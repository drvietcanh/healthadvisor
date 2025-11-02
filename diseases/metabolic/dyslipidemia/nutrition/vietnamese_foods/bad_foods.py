"""
Bad Foods - Thực phẩm NÊN TRÁNH (Việt Nam)
"""

BAD_FOODS = {
    "fried_foods_vietnam": {
        "name": "🍟 Đồ Chiên Rán (VN)",
        "foods": [
            "Gà rán KFC, Jollibee, Lotteria",
            "Khoai tây chiên",
            "Chả giò, nem rán",
            "Nem chua rán",
            "Bánh rán donut",
            "Cá chiên giòn, cá lóc chiên",
            "Bì heo chiên",
            "Đậu hủ chiên giòn",
            "Bánh chuối chiên, khoai chiên"
        ],
        "why_bad": "☠️ Trans fat + mỡ bão hòa → TĂNG LDL mạnh nhất",
        "replacement": "→ Nướng, hấp, luộc, xào ít dầu thay vì chiên"
    },
    
    "processed_meat_vietnam": {
        "name": "🌭 Thịt Chế Biến (VN)",
        "foods": [
            "Chả lụa, giò lụa",
            "Giò thủ",
            "Nem chua",
            "Xúc xích",
            "Thịt nguội các loại",
            "Pate",
            "Chả bò",
            "Thịt xông khói"
        ],
        "why_bad": "Mỡ bão hòa + muối cao + phụ gia bảo quản",
        "replacement": "→ Thịt gà luộc, cá hấp tươi",
        "note": "Chả lụa tốt hơn bì heo/giò thủ (ít mỡ hơn)"
    },
    
    "organ_meat_vietnam": {
        "name": "🫀 Nội Tạng (Cholesterol Cực Cao!)",
        "foods": [
            "Óc heo/bò (cholesterol cao nhất!)",
            "Gan (heo/bò/gà)",
            "Tim, lòng",
            "Bầu dục",
            "Lưỡi",
            "Tiết canh",
            "Trứng vịt lộn"
        ],
        "why_bad": "☠️ CHOLESTEROL CỰC CAO (óc heo: 2000mg/100g!)",
        "recommendation": "🚫 TRÁNH HOÀN TOÀN nếu LDL cao",
        "note": "Giới hạn cholesterol <200mg/ngày, 1 bát óc = 10 ngày!"
    },
    
    "fatty_meat_vietnam": {
        "name": "🥩 Thịt Nhiều Mỡ (VN)",
        "foods": [
            "Thịt ba chỉ (ba rọi)",
            "Sườn non",
            "Mỡ heo",
            "Da heo, da gà",
            "Bì heo",
            "Thịt kho tàu",
            "Thịt đông",
            "Chân giò"
        ],
        "why_bad": "Mỡ bão hòa cao → Tăng LDL",
        "recommendation": "⚠️ Chọn thịt nạc, bỏ mỡ, bỏ da",
        "replacement": "→ Thịt nạc vai, thịt đùi gà bỏ da"
    },
    
    "instant_noodles": {
        "name": "🍜 Mì Gói & Đồ Ăn Liền",
        "foods": [
            "Mì tôm, mì gói các loại",
            "Hủ tiếu gói",
            "Phở gói",
            "Miến gói",
            "Cháo ăn liền"
        ],
        "why_bad": "Trans fat (mì chiên) + muối cao + ít dinh dưỡng",
        "recommendation": "🚫 HẠN CHẾ tối đa, <1 lần/tuần",
        "tip": "Nếu ăn: Chọn mì không chiên, bỏ 1/2 gói gia vị, thêm rau"
    },
    
    "street_food_vietnam": {
        "name": "🍢 Đồ Ăn Vặt VN (Cẩn Thận)",
        "foods": [
            "Bánh bao chiên",
            "Bánh tiêu",
            "Quẩy",
            "Bánh cống",
            "Xôi chiên",
            "Bánh tráng nướng nhiều bơ",
            "Ốc xào bơ",
            "Hàu nướng mỡ hành"
        ],
        "why_bad": "Dầu mỡ tái sử dụng + trans fat",
        "recommendation": "⚠️ Ăn thỉnh thoảng, không thường xuyên"
    },
    
    "dairy_vietnam": {
        "name": "🥛 Sữa & Bánh Béo",
        "foods": [
            "Sữa đặc có đường",
            "Kem (kem que, kem ý)",
            "Yaourt có đường",
            "Phô mai",
            "Bánh flan",
            "Trà sữa",
            "Cà phê sữa đá",
            "Sinh tố sữa đặc"
        ],
        "why_bad": "Mỡ bão hòa + đường cao",
        "replacement": "→ Sữa tươi tách béo không đường, yaourt không đường",
        "note": "Cà phê đen OK, thêm sữa tươi tách béo thay sữa đặc"
    },
    
    "bakery_vietnam": {
        "name": "🥐 Bánh Mì & Bánh Ngọt VN",
        "foods": [
            "Bánh mì que (nhiều bơ)",
            "Bánh mì hoa cúc",
            "Bánh bông lan trứng muối",
            "Bánh croissant",
            "Bánh su kem",
            "Bánh kem sinh nhật",
            "Bánh trung thu",
            "Bánh quy bơ"
        ],
        "why_bad": "Trans fat + bơ + đường → Tăng LDL mạnh",
        "recommendation": "⚠️ Ăn thỉnh thoảng, không hàng ngày",
        "better_choice": "Bánh mì đen nguyên cám, bánh không nhân"
    },
    
    "coconut_products": {
        "name": "🥥 Dừa & Sản Phẩm Dừa",
        "foods": [
            "Dầu dừa (90% mỡ bão hòa!)",
            "Nước cốt dừa",
            "Cơm dừa",
            "Bánh dừa",
            "Kẹo dừa"
        ],
        "why_bad": "☠️ 90% mỡ bão hòa - cao hơn mỡ heo!",
        "note": "QUAN NIỆM SAI: Nhiều người nghĩ dầu dừa tốt → KHÔNG đúng cho lipid máu!",
        "replacement": "→ Dầu ô liu, dầu đậu nành",
        "exception": "Nước dừa tươi OK (ít mỡ)"
    },
    
    "high_cholesterol_foods": {
        "name": "🥚 Thực Phẩm Cholesterol Cao",
        "foods": [
            "Trứng gà lòng đào (>2 quả/ngày)",
            "Mực, bạch tuộc (cholesterol cao)",
            "Tôm, cua (vừa phải)",
            "Lòng đỏ trứng muối",
            "Trứng cút"
        ],
        "why_bad": "Cholesterol trong thực phẩm",
        "recommendation": "⚠️ Giới hạn: Trứng <3-4 quả/tuần, tôm cua ít thôi",
        "note": "Mỡ bão hòa & trans fat ẢNH HƯỞNG hơn cholesterol ăn vào"
    }
}

