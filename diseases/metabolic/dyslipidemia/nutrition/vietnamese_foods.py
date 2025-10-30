"""
Vietnamese Foods - Thực phẩm Việt Nam
======================================

Danh sách thực phẩm nên ăn và nên tránh phổ biến tại Việt Nam
"""

from typing import Dict, List

# Thực phẩm NÊN ĂN (Phổ biến tại Việt Nam)
GOOD_FOODS = {
    "fish_vietnam": {
        "name": "🐟 Cá (Dễ mua tại VN)",
        "foods": [
            "Cá thu (giàu omega-3, rẻ!)",
            "Cá nục (omega-3 cao)",
            "Cá trích (bình dân)",
            "Cá hồi (siêu thị)",
            "Cá ngừ đóng hộp (tiện lợi)",
            "Cá basa (rẻ, dễ tìm)",
            "Cá rô phi",
            "Cá chép"
        ],
        "benefit": "Omega-3 → Giảm TG 20-30%, tăng HDL, bảo vệ tim",
        "recommendation": "2-3 lần/tuần, mỗi lần 100-150g",
        "cooking": "Hấp, nướng, kho ít mỡ (KHÔNG chiên giòn)"
    },
    
    "vegetables_vietnam": {
        "name": "🥬 Rau Xanh (VN)",
        "foods": [
            "Rau muống",
            "Cải xanh, cải thảo",
            "Rau dền",
            "Mồng tơi",
            "Su hào, su lơ",
            "Bông cải xanh",
            "Rau ngót",
            "Cà chua",
            "Dưa chuột",
            "Đậu đũa, đậu cove"
        ],
        "benefit": "Chất xơ, vitamin, khoáng chất → Giảm cholesterol tự nhiên",
        "recommendation": "Ít nhất 400g/ngày (1 bát rau mỗi bữa)",
        "cooking": "Luộc, xào ít dầu (dầu ô liu hoặc dầu đậu nành)"
    },
    
    "whole_grains_vietnam": {
        "name": "🌾 Ngũ Cốc & Tinh Bột Tốt",
        "foods": [
            "Gạo lứt (thay cơm trắng)",
            "Yến mạch (siêu thị, chợ)",
            "Ngô luộc",
            "Khoai lang",
            "Khoai tây (luộc/hấp, KHÔNG chiên)",
            "Bí đỏ",
            "Sắn, củ từ"
        ],
        "benefit": "Chất xơ hòa tan → Giảm LDL 5-10%",
        "recommendation": "Thay 50% cơm trắng bằng gạo lứt",
        "note": "Yến mạch có beta-glucan - hiệu quả nhất!"
    },
    
    "nuts_vietnam": {
        "name": "🥜 Hạt (Dễ mua)",
        "foods": [
            "Đậu phộng (rẻ nhất, tốt!)",
            "Hạt điều",
            "Hạt óc chó (siêu thị)",
            "Hạt hạnh nhân (siêu thị)",
            "Hạt bí",
            "Hạt hướng dương",
            "Vừng rang"
        ],
        "benefit": "Mỡ tốt → Giảm LDL 3-5%",
        "recommendation": "30g/ngày (1 nắm tay nhỏ)",
        "warning": "⚠️ Ăn nguyên hạt, KHÔNG MUỐI - nhiều calories!",
        "vietnam_note": "Đậu phộng luộc/rang nhạt - rẻ mà tốt!"
    },
    
    "legumes_vietnam": {
        "name": "🫘 Đậu & Đỗ (VN)",
        "foods": [
            "Đậu hũ (đậu phụ)",
            "Đậu xanh",
            "Đậu đen",
            "Đậu đỏ",
            "Đậu nành",
            "Đỗ xanh",
            "Đậu que (đậu rồng)"
        ],
        "benefit": "Protein thực vật, chất xơ → Thay thịt giảm cholesterol",
        "recommendation": "Thay thịt 2-3 bữa/tuần",
        "vietnam_dishes": "Đậu hũ kho, canh đậu, chè đậu"
    },
    
    "fruits_vietnam": {
        "name": "🍊 Trái Cây (VN Theo Mùa)",
        "foods": [
            "Cam, quýt (vitamin C)",
            "Bưởi (chất xơ pectin)",
            "Táo (pectin giảm LDL)",
            "Chuối (kali)",
            "Đu đủ",
            "Dưa hấu",
            "Xoài (vừa phải)",
            "Ổi",
            "Thanh long",
            "Mận"
        ],
        "benefit": "Chất xơ, vitamin, chống oxy hóa",
        "recommendation": "3-4 phần/ngày",
        "warning": "⚠️ TRÁNH: Sầu riêng (nhiều mỡ), mít (nhiều đường)"
    },
    
    "oils_vietnam": {
        "name": "🌻 Dầu Ăn Tốt (Có Ở VN)",
        "foods": [
            "Dầu ô liu Extra Virgin (siêu thị)",
            "Dầu đậu nành (phổ biến, rẻ, OK)",
            "Dầu hướng dương",
            "Dầu cải (canola oil - siêu thị)"
        ],
        "benefit": "Mỡ không bão hòa → Giảm LDL",
        "recommendation": "2-3 thìa/ngày",
        "cooking": "Xào, trộn salad",
        "warning": "🚫 TRÁNH: Dầu dừa, dầu cọ (nhiều mỡ bão hòa!)"
    },
    
    "other_good": {
        "name": "✅ Khác (VN)",
        "foods": [
            "Nấm các loại (rơm, hương, bào ngư)",
            "Tỏi (allicin giảm cholesterol)",
            "Gừng",
            "Trà xanh VN (catechin)",
            "Rau thơm: Húng, ngò, rau răm"
        ],
        "benefit": "Chống oxy hóa, giảm viêm",
        "recommendation": "Dùng hàng ngày"
    }
}

# Thực phẩm NÊN TRÁNH (Phổ biến VN)
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

# Thực phẩm giảm cholesterol đặc biệt
CHOLESTEROL_LOWERING_FOODS = [
    {
        "name": "Yến mạch (Oatmeal)",
        "mechanism": "Chất xơ beta-glucan → Giảm LDL 5-10%",
        "amount": "1 bát/ngày (40-50g)",
        "benefit": "Hiệu quả như thuốc nhẹ!"
    },
    {
        "name": "Đậu nành",
        "mechanism": "Protein đậu nành → Thay thế thịt",
        "amount": "25g protein đậu nành/ngày",
        "benefit": "Giảm LDL 3-5%"
    },
    {
        "name": "Hạt óc chó (Walnut)",
        "mechanism": "Omega-3, mỡ tốt",
        "amount": "30g/ngày (7 quả)",
        "benefit": "Giảm LDL 5-7%"
    },
    {
        "name": "Trà xanh",
        "mechanism": "Catechin → Chống oxy hóa LDL",
        "amount": "2-3 cốc/ngày",
        "benefit": "Giảm LDL 2-5%"
    },
    {
        "name": "Tỏi",
        "mechanism": "Allicin → Giảm cholesterol",
        "amount": "2-3 tép/ngày",
        "benefit": "Giảm TC 5-8%"
    }
]

