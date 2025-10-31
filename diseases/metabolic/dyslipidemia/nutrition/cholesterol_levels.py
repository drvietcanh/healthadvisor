"""
Cholesterol Levels - Phân loại mức cholesterol
Cholesterol Level Classification
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
                "cholesterol": "200-300",
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
                "cholesterol": "100-120",
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
                "cholesterol": "50-70",
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
                "cholesterol": "40-60",
                "note": "Ít cholesterol + Nhiều omega-3",
                "recommendation": "⭐ RẤT TỐT, ăn 2-3 lần/tuần",
                "highlight": True
            },
            {
                "name": "Cá nước ngọt (cá rô phi, cá chép)",
                "cholesterol": "50-70",
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


