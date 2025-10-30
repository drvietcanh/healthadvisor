"""
Fat Types - Các loại chất béo
==============================

Giải thích chi tiết về các loại mỡ: Trans fat, Saturated, Unsaturated, Omega-3/6
"""

from typing import Dict

# GIẢI THÍCH CÁC LOẠI CHẤT BÉO
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

