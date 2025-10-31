"""
Nutrition Tips - Lời khuyên dinh dưỡng giảm cân cho người Việt
"""

from typing import List, Dict


def get_nutrition_tips() -> List[Dict]:
    """Lời khuyên dinh dưỡng cho người Việt giảm cân"""
    return [
        {
            "title": "🍚 Giảm cơm, tăng rau",
            "detail": "Thay vì 1 bát cơm đầy → 2/3 bát + rau nhiều",
            "benefit": "Giảm 100-150 cal/bữa"
        },
        {
            "title": "🥤 Bỏ đồ uống có đường",
            "detail": "Trà sữa, nước ngọt, cà phê sữa → Nước lọc, trà không đường",
            "benefit": "Giảm 300-500 cal/ngày"
        },
        {
            "title": "🍗 Chọn thịt nạc, không da",
            "detail": "Gà bỏ da, thịt nạc, cá → Tránh mỡ, da, nội tạng",
            "benefit": "Giảm 200 cal/bữa"
        },
        {
            "title": "🔥 Hạn chế chiên rán",
            "detail": "Hấp, luộc, nướng thay vì chiên",
            "benefit": "Giảm 30-50% calories"
        },
        {
            "title": "🕐 Ăn tối sớm (trước 7h)",
            "detail": "Tránh ăn khuya → Không tích mỡ",
            "benefit": "Giảm cân hiệu quả hơn 20%"
        },
        {
            "title": "💧 Uống nước trước ăn",
            "detail": "Uống 1-2 cốc nước 30 phút trước bữa ăn",
            "benefit": "No nhanh hơn, ăn ít hơn 15-20%"
        },
        {
            "title": "🥢 Nhai chậm, ăn chậm",
            "detail": "Mỗi miếng nhai 20-30 lần, ăn ít nhất 20 phút/bữa",
            "benefit": "Não kịp nhận tín hiệu no → Ăn ít hơn"
        },
        {
            "title": "📝 Ghi nhật ký ăn uống",
            "detail": "Viết ra tất cả món ăn trong ngày",
            "benefit": "Nhận thức rõ → Kiểm soát tốt hơn"
        }
    ]


__all__ = ['get_nutrition_tips']
