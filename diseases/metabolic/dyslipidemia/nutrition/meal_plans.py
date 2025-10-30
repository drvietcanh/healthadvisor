"""
Meal Plans - Kế hoạch ăn uống
==============================

Thực đơn mẫu và lời khuyên dinh dưỡng cho người rối loạn lipid máu
"""

from typing import Dict, List

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

