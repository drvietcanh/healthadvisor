"""
Nutrition - Dinh dưỡng cho người rối loạn lipid máu
===================================================

Thực phẩm tốt/xấu, các loại chất béo
"""

from typing import Dict, List

# GIẢI THÍCH CÁC LOẠI CHẤT BÉO
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

FAT_TYPES_EXPLANATION = {
    "title": "🧈 Các Loại Chất Béo - Tốt và Xấu",
    
    "trans_fat": {
        "name": "Trans Fat - Mỡ CHUYỂN HÓA (XẤU NHẤT!)",
        "icon": "☠️",
        "danger_level": "CỰC KỲ NGUY HIỂM",
        "simple": """
Trans Fat = Dầu thực vật + Hydro → Biến thành mỡ rắn

VÍ DỤ: Biến dầu lỏng thành bơ nhân tạo (margarine)
        """,
        "why_dangerous": [
            "TĂNG LDL (mỡ xấu) ↑↑",
            "GIẢM HDL (mỡ tốt) ↓↓",
            "Gây viêm mạch máu",
            "Tăng nguy cơ tim mạch GẤP ĐÔI",
            "WHO: Trans fat giết 500,000 người/năm"
        ],
        "sources": [
            "🍟 Đồ chiên giòn: Gà rán, khoai tây chiên",
            "🍰 Bánh ngọt công nghiệp: Bánh quy, croissant",
            "🧈 Bơ nhân tạo (margarine)",
            "🍿 Bỏng ngô vi sóng",
            "🍕 Pizza đông lạnh",
            "🍪 Bánh snack đóng gói",
            "☕ Kem coffee (creamer)"
        ],
        "how_to_identify": [
            "Đọc nhãn: 'Partially hydrogenated oil'",
            "Đọc nhãn: 'Shortening'",
            "Đồ ăn giòn lâu, không bị ôi rancid"
        ],
        "recommendation": "🚫 TRÁNH HOÀN TOÀN - 0 gram/ngày!"
    },
    
    "saturated_fat": {
        "name": "Saturated Fat - Mỡ BÃO HÒA (XẤU)",
        "icon": "🥩",
        "danger_level": "Cao",
        "simple": """
Mỡ bão hòa = Mỡ động vật, dầu nhiệt đới

ĐẶC ĐIỂM: Rắn ở nhiệt độ phòng
VÍ DỤ: Mỡ heo, bơ, dầu dừa
        """,
        "why_bad": [
            "TĂNG LDL (mỡ xấu) ↑",
            "Gây xơ vữa động mạch",
            "Tăng nguy cơ tim mạch 20-30%"
        ],
        "sources": [
            "🥩 Thịt đỏ: Bò, heo, dê",
            "🍖 Mỡ động vật: Mỡ heo, nội tạng",
            "🧈 Bơ sữa, kem",
            "🧀 Phô mai",
            "🥛 Sữa nguyên kem",
            "🥥 Dầu dừa, dầu cọ",
            "🍫 Chocolate sữa"
        ],
        "vietnamese_foods": [
            "Thịt kho tàu",
            "Bì heo",
            "Da gà",
            "Nội tạng: Gan, lòng, óc",
            "Chả lụa nhiều mỡ"
        ],
        "recommendation": "⚠️ HẠN CHẾ - <7% tổng calories (khoảng 15-20g/ngày)"
    },
    
    "monounsaturated_fat": {
        "name": "Monounsaturated Fat - Mỡ KHÔNG BÃO HÒA ĐƠN (TỐT)",
        "icon": "🫒",
        "danger_level": "An toàn - Tốt cho tim",
        "simple": """
Mỡ không bão hòa đơn = Dầu thực vật tốt

ĐẶC ĐIỂM: Lỏng ở nhiệt độ phòng
VÍ DỤ: Dầu ô liu, dầu cải
        """,
        "why_good": [
            "GIẢM LDL (mỡ xấu) ↓",
            "TĂNG HDL (mỡ tốt) ↑",
            "Chống viêm",
            "Giảm nguy cơ tim mạch 20-30%"
        ],
        "sources": [
            "🫒 Dầu ô liu (olive oil)",
            "🥑 Bơ (avocado)",
            "🌰 Hạt điều, hạt hạnh nhân",
            "🥜 Đậu phộng",
            "Dầu cải (canola oil)"
        ],
        "recommendation": "✅ NÊN DÙNG - Thay thế mỡ bão hòa"
    },
    
    "polyunsaturated_fat": {
        "name": "Polyunsaturated Fat - Mỡ KHÔNG BÃO HÒA ĐA (TỐT)",
        "icon": "🐟",
        "danger_level": "An toàn - Rất tốt cho tim",
        "simple": """
Mỡ không bão hòa đa = Omega-3, Omega-6

ĐẶC ĐIỂM: Lỏng ngay cả khi lạnh
VÍ DỤ: Dầu cá, dầu hạt lanh
        """,
        "types": {
            "omega3": {
                "name": "Omega-3 (THIẾT YẾU - rất tốt!)",
                "benefits": [
                    "GIẢM triglyceride 20-30%",
                    "Giảm viêm",
                    "Ngăn huyết khối",
                    "Bảo vệ tim mạch mạnh mẽ"
                ],
                "sources": [
                    "🐟 Cá béo: Cá hồi, cá thu, cá ngừ",
                    "🦐 Hải sản",
                    "Hạt lanh, hạt chia",
                    "Óc chó (walnut)"
                ],
                "recommendation": "✅ ĂN NHIỀU - 2-3 lần cá béo/tuần"
            },
            "omega6": {
                "name": "Omega-6",
                "note": "Cần thiết nhưng đừng quá nhiều",
                "sources": [
                    "Dầu đậu nành",
                    "Dầu hướng dương",
                    "Dầu ngô"
                ],
                "recommendation": "⚖️ CÂN BẰNG - Tỷ lệ Omega-6:Omega-3 nên 4:1"
            }
        },
        "recommendation": "✅ NÊN DÙNG - Đặc biệt Omega-3"
    }
}

# So sánh các loại mỡ
FAT_COMPARISON = {
    "title": "📊 So Sánh Các Loại Mỡ",
    "table": [
        {
            "type": "Trans Fat",
            "ldl_effect": "↑↑↑ Tăng nhiều",
            "hdl_effect": "↓↓ Giảm",
            "verdict": "☠️ TRÁNH HOÀN TOÀN",
            "color": "#F44336"
        },
        {
            "type": "Mỡ bão hòa",
            "ldl_effect": "↑↑ Tăng",
            "hdl_effect": "→ Không đổi",
            "verdict": "⚠️ HẠN CHẾ <7%",
            "color": "#FF9800"
        },
        {
            "type": "Mỡ không bão hòa đơn",
            "ldl_effect": "↓ Giảm",
            "hdl_effect": "↑ Tăng",
            "verdict": "✅ TỐT - Dùng thay thế",
            "color": "#4CAF50"
        },
        {
            "type": "Omega-3",
            "ldl_effect": "→ Ít ảnh hưởng",
            "hdl_effect": "↑ Tăng, ↓↓ TG",
            "verdict": "🌟 RẤT TỐT - Nên ăn",
            "color": "#2196F3"
        }
    ]
}

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


def get_diet_plan_vietnam(calories: int = 1800) -> Dict:
    """Kế hoạch ăn giảm cholesterol - Món Việt Nam"""
    return {
        "title": "📋 Thực Đơn 1 Ngày (Món Việt)",
        "total_calories": f"~{calories} kcal",
        
        "breakfast": {
            "time": "6:00-7:00",
            "options": [
                "Phở gà (bỏ mỡ, ít dầu) + rau thơm",
                "Bánh mì thịt nạc + dưa chuột, cà chua (ít pate)",
                "Cháo gà + trứng luộc + rau muống luộc",
                "Yến mạch + chuối + đậu phộng rang (30g)",
                "Bún riêu cua (ít mỡ) + rau sống"
            ],
            "calories": "400-500 kcal"
        },
        
        "morning_snack": {
            "time": "9:00-10:00",
            "options": [
                "Trái cây: Cam/bưởi/ổi (1 phần)",
                "Đậu phộng luộc (30g)",
                "Sữa tươi tách béo không đường"
            ],
            "calories": "100-150 kcal"
        },
        
        "lunch": {
            "time": "12:00-13:00",
            "options": [
                "Cơm gạo lứt + cá thu hấp + rau muống xào + canh rau",
                "Bún cá + rau sống đầy đủ",
                "Cơm + đậu hũ sốt cà chua + rau cải luộc + canh",
                "Cơm + gà luộc bỏ da + rau xào + canh",
                "Hủ tiếu (không chiên) + tôm + giá + rau"
            ],
            "note": "Cơm 1 bát nhỏ (100g), nhiều rau",
            "calories": "500-600 kcal"
        },
        
        "afternoon_snack": {
            "time": "15:00-16:00",
            "options": [
                "Trái cây: Táo/đu đủ/dưa hấu",
                "Hạt điều rang nhạt (30g)",
                "Ngô luộc",
                "Yaourt không đường"
            ],
            "calories": "100-150 kcal"
        },
        
        "dinner": {
            "time": "18:00-19:00",
            "options": [
                "Cơm gạo lứt (ít hơn trưa) + cá nục nướng + rau luộc",
                "Canh chua cá + rau + ít cơm",
                "Miến gà (bỏ da) + rau",
                "Cơm + canh đậu hũ nấu cà chua + rau xào",
                "Bún chả cá (ít dầu) + rau sống"
            ],
            "note": "Ăn tối nhẹ hơn trưa, nhiều canh",
            "calories": "400-500 kcal"
        },
        
        "evening_snack": {
            "time": "20:00 (nếu đói)",
            "options": [
                "Trái cây nhỏ",
                "Sữa tách béo ấm",
                "Trà xanh không đường"
            ],
            "calories": "50-100 kcal"
        },
        
        "important_notes": [
            "🍚 Cơm: Thay 50% cơm trắng bằng gạo lứt",
            "🐟 Protein: Ưu tiên cá, gà bỏ da, đậu hũ",
            "🥬 Rau: Mỗi bữa phải có rau (luộc/xào ít dầu)",
            "🥄 Dầu: Dùng dầu ô liu hoặc dầu đậu nành, KHÔNG mỡ heo",
            "🧂 Muối: Giảm muối, nước mắm",
            "🚫 TRÁNH: Chiên rán, mỡ heo, da, nội tạng",
            "💧 Nước: Uống 1.5-2L/ngày, trà xanh tốt"
        ]
    }


def get_nutrition_tips() -> List[str]:
    """Lời khuyên dinh dưỡng"""
    return [
        "🚫 TRÁNH HOÀN TOÀN trans fat (đồ chiên, bánh công nghiệp)",
        "⚠️ HẠN CHẾ mỡ bão hòa <7% calories (~15-20g/ngày)",
        "✅ DÙNG mỡ tốt: Dầu ô liu, cá béo, hạt",
        "🐟 ĂN CÁ 2-3 lần/tuần (đặc biệt cá béo - omega-3)",
        "🥬 TĂNG rau xanh, trái cây (5 phần/ngày)",
        "🌾 THAY cơm trắng bằng gạo lứt, yến mạch",
        "🥜 ĂN HẠT mỗi ngày (30g óc chó/hạnh nhân)",
        "🥛 CHỌN sữa tách béo thay sữa nguyên kem",
        "🍳 NẤU bằng dầu ô liu, tránh mỡ heo/bơ",
        "📖 ĐỌC NHÃN: Tránh 'partially hydrogenated oil'"
    ]

