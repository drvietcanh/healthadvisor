"""
Cholesterol Dishes & Tips - Món ăn và Mẹo
Cholesterol in Vietnamese Dishes & Cooking Tips
"""

from typing import Dict, List

# So sánh cholesterol một số món ăn phổ biến
VIETNAMESE_DISHES_CHOLESTEROL = {
    "title": "🍜 CHOLESTEROL TRONG MÓN ĂN VIỆT NAM",
    
    "high_dishes": {
        "level": "🔴 Món CAO Cholesterol (> 100mg/phần)",
        "dishes": [
            {
                "name": "Phở bò (1 bát)",
                "cholesterol": "80-120",
                "reason": "Thịt bò + nước dùng xương",
                "how_to_reduce": [
                    "Bỏ mỡ nổi trên nước dùng",
                    "Chọn phần nạc",
                    "Thêm nhiều rau"
                ]
            },
            {
                "name": "Bún bò Huế (1 bát)",
                "cholesterol": "100-150",
                "reason": "Giò heo, chả",
                "how_to_reduce": "Bỏ giò heo, chọn thịt nạc"
            },
            {
                "name": "Cơm sườn (1 phần)",
                "cholesterol": "90-120",
                "reason": "Sườn non nhiều mỡ",
                "how_to_reduce": "Thay sườn bằng thịt nạc hoặc cá"
            },
            {
                "name": "Thịt kho tàu (100g)",
                "cholesterol": "80-100",
                "reason": "Thịt ba chỉ, trứng",
                "how_to_reduce": "Chọn thịt nạc, bỏ mỡ"
            },
            {
                "name": "Bánh xèo (1 cái)",
                "cholesterol": "100-150",
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
                "cholesterol": "60-80",
                "reason": "Thịt gà",
                "tip": "Bỏ da gà"
            },
            {
                "name": "Bún chả (1 bát)",
                "cholesterol": "70-90",
                "reason": "Thịt nướng",
                "tip": "Chọn phần nạc"
            },
            {
                "name": "Cháo gà (1 bát)",
                "cholesterol": "40-60",
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
                "cholesterol": "30-50",
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
                "cholesterol": "25-40",
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


