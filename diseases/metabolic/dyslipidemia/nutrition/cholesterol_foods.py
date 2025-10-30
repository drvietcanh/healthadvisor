"""
Cholesterol Foods Classification - Phân loại thực phẩm theo cholesterol
=========================================================================

Bảng phân loại thực phẩm giàu/ít cholesterol
"""

from typing import Dict, List

# Bảng phân loại thực phẩm theo cholesterol
CHOLESTEROL_FOOD_CLASSIFICATION = {
    "title": "📊 BẢNG PHÂN LOẠI THỰC PHẨM THEO CHOLESTEROL",
    "unit": "mg cholesterol/100g",
    "daily_limit": "< 200mg/ngày (người lipid cao) hoặc < 300mg/ngày (người bình thường)",
    
    "very_high_cholesterol": {
        "level": "🔴 CỰC CAO (> 200mg/100g)",
        "warning": "☠️ TRÁNH HOÀN TOÀN nếu cholesterol cao!",
        "foods": [
            {
                "name": "Óc heo",
                "cholesterol": 2000,
                "note": "CAO NHẤT! 1 bát (100g) = 10 ngày cholesterol",
                "recommendation": "🚫 KHÔNG nên ăn"
            },
            {
                "name": "Óc bò",
                "cholesterol": 1800,
                "note": "Rất cao",
                "recommendation": "🚫 KHÔNG nên ăn"
            },
            {
                "name": "Gan gà",
                "cholesterol": 564,
                "note": "100g = 3 ngày cholesterol",
                "recommendation": "⚠️ Tối đa 1 lần/tháng, <50g"
            },
            {
                "name": "Gan heo",
                "cholesterol": 355,
                "note": "Cao",
                "recommendation": "⚠️ Tối đa 1-2 lần/tháng, <50g"
            },
            {
                "name": "Gan bò",
                "cholesterol": 389,
                "note": "Cao",
                "recommendation": "⚠️ Tối đa 1-2 lần/tháng, <50g"
            },
            {
                "name": "Lòng đỏ trứng gà",
                "cholesterol": 1085,
                "note": "1 quả trứng = ~200mg cholesterol (chỉ ở lòng đỏ)",
                "recommendation": "⚠️ Giới hạn 3-4 quả/tuần"
            },
            {
                "name": "Lòng đỏ trứng vịt",
                "cholesterol": 884,
                "note": "Cao hơn trứng gà",
                "recommendation": "⚠️ Giới hạn 2-3 quả/tuần"
            },
            {
                "name": "Trứng vịt lộn",
                "cholesterol": 619,
                "note": "Cao",
                "recommendation": "⚠️ Tối đa 1-2 quả/tháng"
            },
            {
                "name": "Lòng, tim, dạ dày",
                "cholesterol": 200-300,
                "note": "Nội tạng đều cao cholesterol",
                "recommendation": "⚠️ Hạn chế tối đa"
            }
        ]
    },
    
    "high_cholesterol": {
        "level": "🟠 CAO (100-200mg/100g)",
        "warning": "Giới hạn khẩu phần, không ăn thường xuyên",
        "foods": [
            {
                "name": "Mực",
                "cholesterol": 233,
                "note": "Cao nhưng ít mỡ bão hòa",
                "recommendation": "⚠️ Ăn được nhưng vừa phải, <100g/lần"
            },
            {
                "name": "Bạch tuộc",
                "cholesterol": 164,
                "note": "Cao",
                "recommendation": "⚠️ Ăn được nhưng vừa phải"
            },
            {
                "name": "Tôm",
                "cholesterol": 152,
                "note": "Cholesterol cao NHƯNG mỡ bão hòa THẤP → Vẫn OK",
                "recommendation": "✅ Ăn được, <150g/lần, 2-3 lần/tuần"
            },
            {
                "name": "Cua",
                "cholesterol": 100,
                "note": "Tương tự tôm",
                "recommendation": "✅ Ăn được bình thường"
            },
            {
                "name": "Bơ sữa",
                "cholesterol": 215,
                "note": "Cao mỡ bão hòa + cholesterol",
                "recommendation": "⚠️ Thay bằng dầu ô liu"
            },
            {
                "name": "Phô mai",
                "cholesterol": 100-120,
                "note": "Cao mỡ bão hòa",
                "recommendation": "⚠️ Hạn chế, chọn loại ít béo"
            }
        ]
    },
    
    "moderate_cholesterol": {
        "level": "🟡 TRUNG BÌNH (50-100mg/100g)",
        "warning": "Ăn được nhưng kiểm soát khẩu phần",
        "foods": [
            {
                "name": "Thịt bò",
                "cholesterol": 70,
                "note": "Chọn phần nạc",
                "recommendation": "✅ Ăn được, chọn nạc, bỏ mỡ, <100g/bữa"
            },
            {
                "name": "Thịt heo",
                "cholesterol": 75,
                "note": "Chọn phần nạc",
                "recommendation": "✅ Ăn được, chọn nạc, bỏ mỡ, <100g/bữa"
            },
            {
                "name": "Thịt gà (có da)",
                "cholesterol": 88,
                "note": "Da chứa nhiều mỡ",
                "recommendation": "⚠️ BỎ DA khi ăn"
            },
            {
                "name": "Thịt gà (bỏ da)",
                "cholesterol": 62,
                "note": "Thấp hơn khi bỏ da",
                "recommendation": "✅ Tốt, ăn được thường xuyên"
            },
            {
                "name": "Chả lụa",
                "cholesterol": 50-70,
                "note": "Tùy loại",
                "recommendation": "✅ Ăn được vừa phải"
            }
        ]
    },
    
    "low_cholesterol": {
        "level": "🟢 THẤP (< 50mg/100g)",
        "warning": "An toàn, ăn tự do",
        "foods": [
            {
                "name": "Cá biển (cá thu, cá nục, cá hồi)",
                "cholesterol": 40-60,
                "note": "Ít cholesterol + Nhiều omega-3",
                "recommendation": "⭐ RẤT TỐT, ăn 2-3 lần/tuần",
                "highlight": true
            },
            {
                "name": "Cá nước ngọt (cá rô phi, cá chép)",
                "cholesterol": 50-70,
                "note": "Ít omega-3 hơn cá biển",
                "recommendation": "✅ Tốt, ăn được thường xuyên"
            },
            {
                "name": "Sữa tươi tách béo",
                "cholesterol": 5,
                "note": "Rất thấp",
                "recommendation": "✅ Rất tốt"
            },
            {
                "name": "Sữa chua không đường",
                "cholesterol": 10,
                "note": "Thấp",
                "recommendation": "✅ Tốt cho sức khỏe"
            }
        ]
    },
    
    "zero_cholesterol": {
        "level": "🟩 KHÔNG CHỨA CHOLESTEROL",
        "note": "⭐ Thực phẩm THỰC VẬT KHÔNG chứa cholesterol!",
        "foods": [
            {
                "category": "Rau củ quả",
                "examples": [
                    "Tất cả các loại rau xanh",
                    "Tất cả các loại trái cây",
                    "Khoai, củ, sắn..."
                ],
                "cholesterol": 0,
                "recommendation": "⭐ Ăn tự do, càng nhiều càng tốt!"
            },
            {
                "category": "Ngũ cốc",
                "examples": [
                    "Gạo, lúa mì",
                    "Yến mạch",
                    "Ngô",
                    "Bánh mì (không trứng, bơ)"
                ],
                "cholesterol": 0,
                "recommendation": "✅ Chọn nguyên cám"
            },
            {
                "category": "Đậu đỗ",
                "examples": [
                    "Đậu hũ",
                    "Đậu xanh, đậu đen, đậu đỏ",
                    "Đậu nành",
                    "Đậu phộng"
                ],
                "cholesterol": 0,
                "note": "Protein thực vật - THAY THẾ TUYỆT VỜI cho thịt!",
                "recommendation": "⭐ Nên ăn thay thịt 2-3 bữa/tuần"
            },
            {
                "category": "Hạt",
                "examples": [
                    "Hạt điều",
                    "Hạt óc chó",
                    "Hạt hạnh nhân",
                    "Hạt chia, hạt lanh"
                ],
                "cholesterol": 0,
                "note": "Giàu mỡ TỐT (omega-3, omega-6)",
                "recommendation": "✅ 30g/ngày"
            },
            {
                "category": "Dầu thực vật",
                "examples": [
                    "Dầu ô liu",
                    "Dầu đậu nành",
                    "Dầu hướng dương",
                    "Dầu cải"
                ],
                "cholesterol": 0,
                "note": "KHÔNG chứa cholesterol (cholesterol chỉ có ở động vật)",
                "recommendation": "✅ Dùng thay mỡ động vật"
            }
        ]
    }
}

# So sánh cholesterol một số món ăn phổ biến
VIETNAMESE_DISHES_CHOLESTEROL = {
    "title": "🍜 CHOLESTEROL TRONG MÓN ĂN VIỆT NAM",
    
    "high_dishes": {
        "level": "🔴 Món CAO Cholesterol (> 100mg/phần)",
        "dishes": [
            {
                "name": "Phở bò (1 bát)",
                "cholesterol": 80-120,
                "reason": "Thịt bò + nước dùng xương",
                "how_to_reduce": [
                    "Bỏ mỡ nổi trên nước dùng",
                    "Chọn phần nạc",
                    "Thêm nhiều rau"
                ]
            },
            {
                "name": "Bún bò Huế (1 bát)",
                "cholesterol": 100-150,
                "reason": "Giò heo, chả",
                "how_to_reduce": "Bỏ giò heo, chọn thịt nạc"
            },
            {
                "name": "Cơm sườn (1 phần)",
                "cholesterol": 90-120,
                "reason": "Sườn non nhiều mỡ",
                "how_to_reduce": "Thay sườn bằng thịt nạc hoặc cá"
            },
            {
                "name": "Thịt kho tàu (100g)",
                "cholesterol": 80-100,
                "reason": "Thịt ba chỉ, trứng",
                "how_to_reduce": "Chọn thịt nạc, bỏ mỡ"
            },
            {
                "name": "Bánh xèo (1 cái)",
                "cholesterol": 100-150,
                "reason": "Tôm, thịt, chiên nhiều dầu",
                "how_to_reduce": "Ăn ít lượng, thêm nhiều rau"
            }
        ]
    },
    
    "moderate_dishes": {
        "level": "🟡 Món TRUNG BÌNH Cholesterol (50-100mg/phần)",
        "dishes": [
            {
                "name": "Cơm gà (1 phần)",
                "cholesterol": 60-80,
                "reason": "Thịt gà",
                "tip": "Bỏ da gà"
            },
            {
                "name": "Bún chả (1 bát)",
                "cholesterol": 70-90,
                "reason": "Thịt nướng",
                "tip": "Chọn phần nạc"
            },
            {
                "name": "Cháo gà (1 bát)",
                "cholesterol": 40-60,
                "reason": "Gà + trứng",
                "tip": "Món nhẹ, OK"
            }
        ]
    },
    
    "low_dishes": {
        "level": "🟢 Món ÍT Cholesterol (< 50mg/phần)",
        "dishes": [
            {
                "name": "Bún cá (1 bát)",
                "cholesterol": 30-50,
                "reason": "Cá ít cholesterol",
                "note": "⭐ Món TỐT!"
            },
            {
                "name": "Phở chay (1 bát)",
                "cholesterol": 0,
                "reason": "Không thịt",
                "note": "⭐ Rất tốt!"
            },
            {
                "name": "Cơm + đậu hũ sốt cà chua",
                "cholesterol": 0,
                "reason": "Thực vật",
                "note": "⭐ Lựa chọn tuyệt vời!"
            },
            {
                "name": "Canh chua cá (1 bát)",
                "cholesterol": 25-40,
                "reason": "Cá + rau",
                "note": "⭐ Món tốt cho tim mạch!"
            }
        ]
    }
}

# Mẹo giảm cholesterol trong nấu ăn
COOKING_TIPS_REDUCE_CHOLESTEROL = {
    "title": "👨‍🍳 MẸO NẤU ĂN GIẢM CHOLESTEROL",
    
    "protein_substitution": {
        "title": "Thay Thế Protein",
        "tips": [
            {
                "from": "Thịt bò, heo",
                "to": "Cá biển (thu, nục, hồi)",
                "benefit": "Giảm cholesterol 50%, tăng omega-3"
            },
            {
                "from": "Thịt đỏ",
                "to": "Thịt gà bỏ da",
                "benefit": "Giảm cholesterol 30%"
            },
            {
                "from": "Thịt động vật",
                "to": "Đậu hũ, đậu nành",
                "benefit": "Cholesterol = 0, protein cao"
            },
            {
                "from": "Trứng cả quả",
                "to": "Chỉ dùng lòng trắng (bỏ lòng đỏ)",
                "benefit": "Cholesterol = 0 (cholesterol ở lòng đỏ)"
            }
        ]
    },
    
    "cooking_methods": {
        "title": "Phương Pháp Nấu",
        "good_methods": [
            {
                "method": "Hấp, Luộc",
                "benefit": "Không thêm mỡ, giữ nguyên dinh dưỡng",
                "examples": "Cá hấp, gà luộc, rau luộc"
            },
            {
                "method": "Nướng",
                "benefit": "Mỡ chảy ra, giảm cholesterol",
                "tip": "Nướng rồi bỏ mỡ chảy ra"
            },
            {
                "method": "Xào (ít dầu)",
                "benefit": "Nhanh, giữ vitamin",
                "tip": "Dùng dầu ô liu, xào nhanh"
            }
        ],
        "bad_methods": [
            {
                "method": "Chiên giòn",
                "reason": "Thêm NHIỀU mỡ + trans fat",
                "recommendation": "❌ TRÁNH"
            },
            {
                "method": "Kho (với nhiều mỡ)",
                "reason": "Mỡ bão hòa cao",
                "tip": "⚠️ Nếu kho: Dùng ít mỡ, bỏ mỡ nổi"
            }
        ]
    },
    
    "ingredient_tips": {
        "title": "Chọn Nguyên Liệu",
        "tips": [
            "Chọn thịt NẠC, bỏ MỠ sạch",
            "BỎ DA gà, vịt",
            "Gạt bỏ MỠ NỔI trên nước dùng",
            "Dùng SỮA TÁCH BÉO thay sữa nguyên kem",
            "Dùng DẦU Ô LIU thay mỡ heo, bơ",
            "TĂNG RAU trong mỗi món (ít nhất 50% đĩa)"
        ]
    },
    
    "portion_control": {
        "title": "Kiểm Soát Khẩu Phần",
        "guidelines": [
            {
                "food": "Thịt/Cá",
                "portion": "100g/bữa (bằng bàn tay)",
                "note": "KHÔNG phải cả đĩa!"
            },
            {
                "food": "Cơm",
                "portion": "1 bát nhỏ (100g)",
                "note": "Thay 50% bằng gạo lứt"
            },
            {
                "food": "Rau",
                "portion": "Tự do, càng nhiều càng tốt",
                "note": "Nên chiếm ≥50% đĩa"
            }
        ]
    }
}

# Key message
KEY_CHOLESTEROL_MESSAGES = {
    "title": "🎯 ĐIỀU QUAN TRỌNG CẦN NHỚ",
    
    "facts": [
        "🥩 Cholesterol CHỈ có trong ĐỘNG VẬT (thịt, trứng, sữa)",
        "🥬 Thực vật (rau, quả, đậu, ngũ cốc) = 0 cholesterol",
        "🔴 Nội tạng (óc, gan, lòng) = cholesterol CỰC CAO → TRÁNH",
        "🐟 Tôm, mực: Cholesterol CAO NHƯNG mỡ bão hòa THẤP → Vẫn OK ăn vừa phải",
        "🥚 Trứng: Cholesterol trong LÒNG ĐỎ (lòng trắng = 0) → Giới hạn 3-4 quả/tuần",
        "⚠️ MỠ BÃO HÒA & TRANS FAT ảnh hưởng LỚN HƠN cholesterol ăn vào!",
        "✅ Ưu tiên: GIẢM mỡ xấu > Lo cholesterol thực phẩm"
    ],
    
    "daily_strategy": [
        "Ăn NHIỀU: Rau, trái cây, ngũ cốc nguyên hạt, đậu",
        "Ăn VỪA: Cá (2-3 lần/tuần), gà bỏ da, thịt nạc",
        "Ăn ÍT: Thịt đỏ, trứng (3-4 quả/tuần), tôm cua",
        "TRÁNH: Nội tạng, chiên rán, mỡ động vật"
    ]
}

