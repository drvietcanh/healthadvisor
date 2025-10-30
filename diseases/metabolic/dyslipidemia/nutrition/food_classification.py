"""
Food Classification - Phân loại thực phẩm theo mức độ an toàn
==============================================================

Hệ thống Traffic Light giúp người dùng dễ dàng phân biệt thực phẩm tốt/xấu
"""

from typing import Dict

# PHÂN LOẠI THỰC PHẨM THEO MỨC ĐỘ AN TOÀN (Traffic Light System)
FOOD_SAFETY_CLASSIFICATION = {
    "title": "🚦 PHÂN LOẠI THỰC PHẨM - Dễ Hiểu, Dễ Nhớ",
    "description": "Hệ thống màu sắc giúp bạn biết ngay thực phẩm nào an toàn!",
    
    "red_danger": {
        "level": "🔴 ĐỎ - NGUY HIỂM",
        "rule": "TRÁNH HOÀN TOÀN hoặc ăn RẤT HIẾM (< 1 lần/tháng)",
        "reason": "Chứa trans fat hoặc cholesterol/mỡ bão hòa CỰC CAO",
        "foods": {
            "trans_fat_foods": [
                "❌ Gà rán, khoai tây chiên (KFC, Lotteria...)",
                "❌ Chả giò, nem rán, đồ chiên giòn",
                "❌ Bánh ngọt công nghiệp (bánh quy, croissant, donut)",
                "❌ Bơ nhân tạo (margarine)",
                "❌ Mì gói (mì tôm, hủ tiếu gói)",
                "❌ Bỏng ngô vi sóng",
                "❌ Pizza đông lạnh"
            ],
            "very_high_cholesterol": [
                "❌ Óc heo, óc bò (2000mg cholesterol/100g!)",
                "❌ Gan (heo/bò/gà)",
                "❌ Lòng, tim, bầu dục",
                "❌ Tiết canh",
                "❌ Trứng vịt lộn"
            ],
            "very_high_saturated_fat": [
                "❌ Mỡ heo, mỡ bò",
                "❌ Bì heo",
                "❌ Da heo, da gà",
                "❌ Dầu dừa, dầu cọ",
                "❌ Nước cốt dừa đặc"
            ]
        },
        "impact": "☠️ Tăng LDL MẠNH, tăng nguy cơ tim mạch GẤP ĐÔI"
    },
    
    "orange_limit": {
        "level": "🟠 CAM - HẠN CHẾ",
        "rule": "Ăn ÍT, chọn thời điểm (< 2-3 lần/tuần, khẩu phần nhỏ)",
        "reason": "Chứa mỡ bão hòa cao hoặc cholesterol cao",
        "foods": {
            "fatty_meat": [
                "⚠️ Thịt bò (chọn phần nạc)",
                "⚠️ Thịt heo (chọn nạc, bỏ mỡ)",
                "⚠️ Thịt ba chỉ (ba rọi)",
                "⚠️ Sườn non",
                "⚠️ Chân giò",
                "⚠️ Thịt kho (giảm mỡ)"
            ],
            "processed_meat": [
                "⚠️ Chả lụa, giò lụa",
                "⚠️ Nem chua",
                "⚠️ Xúc xích",
                "⚠️ Thịt hun khói",
                "⚠️ Pate"
            ],
            "dairy_products": [
                "⚠️ Sữa nguyên kem",
                "⚠️ Phô mai",
                "⚠️ Bơ sữa",
                "⚠️ Kem (ice cream)",
                "⚠️ Sữa đặc có đường"
            ],
            "others": [
                "⚠️ Trứng gà (giới hạn 3-4 quả/tuần)",
                "⚠️ Tôm, cua (cholesterol cao, nhưng ít mỡ bão hòa)",
                "⚠️ Mực, bạch tuộc",
                "⚠️ Trà sữa, cà phê sữa đá",
                "⚠️ Bánh kem, bánh ngọt"
            ]
        },
        "tips": [
            "Chọn phần nạc, bỏ mỡ, bỏ da",
            "Nấu bằng cách hấp, luộc, nướng - KHÔNG chiên",
            "Khẩu phần nhỏ (50-100g thịt/bữa)"
        ],
        "impact": "⚠️ Tăng LDL vừa phải nếu ăn nhiều"
    },
    
    "yellow_moderate": {
        "level": "🟡 VÀNG - VỪA PHẢI",
        "rule": "Ăn được HÀNG NGÀY nhưng KIỂM SOÁT khẩu phần",
        "reason": "Dinh dưỡng tốt nhưng cần cân bằng",
        "foods": {
            "lean_protein": [
                "✓ Thịt gà bỏ da (nạc)",
                "✓ Thịt heo nạc vai",
                "✓ Thịt bò nạc",
                "✓ Cá ít omega-3 (rô phi, chép)",
                "✓ Tôm, cua (vừa phải)"
            ],
            "grains": [
                "✓ Cơm trắng (nên giảm)",
                "✓ Bánh mì trắng (chuyển sang bánh mì nguyên cám)",
                "✓ Bún, phở, miến (OK)",
                "✓ Mì tươi (không chiên)"
            ],
            "dairy_low_fat": [
                "✓ Sữa tươi tách béo",
                "✓ Yaourt không đường",
                "✓ Sữa chua ít đường"
            ],
            "oils": [
                "✓ Dầu đậu nành",
                "✓ Dầu hướng dương",
                "✓ Dầu ngô"
            ]
        },
        "tips": [
            "Thay 50% cơm trắng bằng gạo lứt",
            "Chọn sữa tách béo thay nguyên kem",
            "Nấu bằng dầu thực vật tốt"
        ]
    },
    
    "green_safe": {
        "level": "🟢 XANH LÁ - AN TOÀN",
        "rule": "Ăn TỰ DO, ưu tiên trong thực đơn",
        "reason": "Ít mỡ xấu, nhiều chất xơ, vitamin, khoáng chất",
        "foods": {
            "vegetables": [
                "✅ Rau muống, rau cải, cải thảo",
                "✅ Rau dền, mồng tơi",
                "✅ Bông cải xanh, su hào, su lơ",
                "✅ Cà chua, dưa chuột",
                "✅ Đậu đũa, đậu cove",
                "✅ Nấm các loại"
            ],
            "fruits": [
                "✅ Cam, quýt, bưởi",
                "✅ Táo, lê",
                "✅ Ổi, đu đủ",
                "✅ Dưa hấu, dưa lưới",
                "✅ Chuối (kali tốt)",
                "✅ Thanh long, mận"
            ],
            "whole_grains": [
                "✅ Gạo lứt",
                "✅ Yến mạch (oatmeal) ⭐",
                "✅ Khoai lang",
                "✅ Khoai tây luộc/hấp",
                "✅ Ngô luộc",
                "✅ Bánh mì nguyên cám"
            ],
            "legumes": [
                "✅ Đậu hũ (đậu phụ)",
                "✅ Đậu xanh, đậu đen, đậu đỏ",
                "✅ Đậu nành",
                "✅ Đậu que"
            ]
        },
        "benefits": "✨ Giảm cholesterol tự nhiên, tốt cho tim mạch"
    },
    
    "dark_green_excellent": {
        "level": "🟩 XANH ĐẬM - RẤT TỐT",
        "rule": "NÊN ĂN NHIỀU, ưu tiên số 1!",
        "reason": "GIẢM cholesterol mạnh, bảo vệ tim mạch tích cực",
        "foods": {
            "omega3_fish": [
                "🌟 Cá thu (omega-3 cao, rẻ!)",
                "🌟 Cá nục (omega-3 cao)",
                "🌟 Cá hồi",
                "🌟 Cá ngừ (tươi hoặc đóng hộp)"
            ],
            "nuts_seeds": [
                "🌟 Óc chó (walnut) - Tốt nhất!",
                "🌟 Hạnh nhân",
                "🌟 Hạt điều",
                "🌟 Đậu phộng (luộc/rang nhạt)",
                "🌟 Hạt lanh, hạt chia"
            ],
            "special_oils": [
                "🌟 Dầu ô liu Extra Virgin (EVOO)"
            ],
            "superfoods": [
                "🌟 Yến mạch (giảm LDL 5-10%!)",
                "🌟 Bơ (avocado) - mỡ tốt",
                "🌟 Tỏi (allicin)",
                "🌟 Trà xanh (catechin)"
            ]
        },
        "benefits": "⭐⭐⭐ GIẢM LDL 5-30%, giảm nguy cơ tim mạch 20-40%!",
        "recommendation": "Cá béo 2-3 lần/tuần + Hạt 30g/ngày + Yến mạch sáng"
    }
}

# Bảng tóm tắt nhanh
QUICK_REFERENCE_TABLE = {
    "title": "📊 BẢNG TRA CỨU NHANH - Thực Phẩm Phổ Biến VN",
    
    "breakfast_foods": {
        "title": "🌅 MÓN SÁNG",
        "red": ["Bánh rán donut", "Quẩy chiên", "Bánh tiêu", "Xôi chiên"],
        "orange": ["Bánh mì pate", "Xôi xéo nhiều mỡ", "Cháo lòng"],
        "yellow": ["Bánh mì thịt", "Cháo gà", "Phở (bỏ mỡ)"],
        "green": ["Bánh mì trứng rau", "Bún chả cá (ít dầu)"],
        "dark_green": ["Yến mạch + trái cây", "Bánh mì nguyên cám + bơ (avocado)"]
    },
    
    "lunch_dinner": {
        "title": "🍚 BỮA CHÍNH",
        "red": ["Thịt kho tàu nhiều mỡ", "Gà rán", "Cá chiên giòn", "Đồ ăn vặt chiên"],
        "orange": ["Cơm + thịt ba chỉ", "Bún bò giò heo", "Mì Quảng nhiều mỡ"],
        "yellow": ["Cơm trắng + thịt nạc", "Bún chả (ít mỡ)", "Phở gà"],
        "green": ["Cơm gạo lứt + rau + gà luộc", "Bún cá + rau", "Canh chua cá"],
        "dark_green": ["Cơm gạo lứt + cá thu hấp + rau luộc", "Salad cá hồi"]
    },
    
    "snacks": {
        "title": "🍿 ĐỒ ĂN VẶT",
        "red": ["Snack chiên (khoai tây chiên...)", "Bánh quy bơ", "Kem"],
        "orange": ["Trà sữa", "Bánh bao", "Bánh bông lan"],
        "yellow": ["Sữa chua có đường", "Ngô luộc", "Khoai luộc"],
        "green": ["Trái cây tươi", "Sữa chua không đường"],
        "dark_green": ["Hạt điều/óc chó (30g)", "Táo", "Cam"]
    },
    
    "proteins": {
        "title": "🍖 PROTEIN",
        "red": ["Óc, gan, lòng", "Bì heo", "Da heo/gà"],
        "orange": ["Thịt ba chỉ", "Xúc xích", "Chả lụa"],
        "yellow": ["Thịt heo nạc", "Gà có da", "Trứng (>4 quả/tuần)"],
        "green": ["Gà bỏ da", "Đậu hũ", "Trứng (3-4 quả/tuần)"],
        "dark_green": ["Cá thu", "Cá hồi", "Cá nục", "Đậu phộng"]
    },
    
    "cooking_oils": {
        "title": "🛢️ DẦU/MỠ NẤU ĂN",
        "red": ["Mỡ heo", "Dầu dừa", "Dầu cọ", "Bơ nhân tạo"],
        "orange": ["Bơ sữa"],
        "yellow": ["Dầu đậu nành", "Dầu hướng dương"],
        "green": ["Dầu cải (canola)"],
        "dark_green": ["Dầu ô liu Extra Virgin"]
    },
    
    "beverages": {
        "title": "🥤 ĐỒ UỐNG",
        "red": ["Nước ngọt có ga", "Sinh tố sữa đặc"],
        "orange": ["Trà sữa", "Cà phê sữa đá", "Nước trái cây đóng chai"],
        "yellow": ["Sữa tươi nguyên kem", "Cà phê sữa tươi"],
        "green": ["Sữa tươi tách béo", "Nước ép trái cây tươi"],
        "dark_green": ["Nước lọc", "Trà xanh", "Cà phê đen", "Nước dừa tươi"]
    }
}

