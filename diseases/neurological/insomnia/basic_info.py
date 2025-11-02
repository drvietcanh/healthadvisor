"""
Mất Ngủ (Insomnia) - Thông tin cơ bản
Basic information about Insomnia
"""

from typing import Dict

INSOMNIA_INFO = {
    "name": "Mất Ngủ",
    "name_en": "Insomnia",
    
    "simple_explanation": """
💡 Mất ngủ là gì? (Giải thích đơn giản)

Tưởng tượng giấc ngủ như cửa nhà:
- Ngủ BÌNH THƯỜNG: Cửa mở dễ dàng, vào giường ngủ ngay
- Mất ngủ: Cửa BỊ KẸT, không vào được → Nằm mãi không ngủ được

😴 Chuyện gì xảy ra:
1. Khó vào giấc ngủ (nằm >30 phút mới ngủ được)
2. Ngủ không sâu, dễ tỉnh giấc (tỉnh nhiều lần trong đêm)
3. Thức dậy sớm (tỉnh trước 6h sáng, không ngủ lại được)
4. Ngủ không đủ → Mệt mỏi, không tập trung

⚠️ ĐẶC ĐIỂM:
- Rất phổ biến ở người già (30-50%)
- Ảnh hưởng nghiêm trọng chất lượng sống
- Có thể do nhiều nguyên nhân (bệnh, thuốc, tâm lý)
- Có thể điều trị được (không cần thuốc ngủ nếu điều trị đúng)
    """,
    
    "definition": """
Mất ngủ là tình trạng khó vào giấc ngủ, khó duy trì giấc ngủ,
hoặc thức dậy quá sớm, dẫn đến chất lượng giấc ngủ kém
và ảnh hưởng đến hoạt động ban ngày.
    """,
    
    "statistics_vietnam": {
        "prevalence": "Rất phổ biến: 30-50% người >60 tuổi",
        "women": "Phụ nữ mất ngủ nhiều hơn nam giới (1.5-2 lần)",
        "increase_with_age": "Tăng theo tuổi: 20-30 tuổi: 10%, 60-70 tuổi: 40%, >80 tuổi: 50%",
        "impact": "Ảnh hưởng nghiêm trọng chất lượng sống, tăng nguy cơ trầm cảm, té ngã"
    },
    
    "types": {
        "acute": {
            "name": "Mất ngủ cấp tính",
            "duration": "<3 tháng",
            "causes": [
                "Stress, căng thẳng",
                "Thay đổi môi trường",
                "Bệnh cấp tính",
                "Thuốc"
            ],
            "prognosis": "Thường tự khỏi sau khi giải quyết nguyên nhân"
        },
        "chronic": {
            "name": "Mất ngủ mạn tính",
            "duration": "≥3 tháng, ≥3 lần/tuần",
            "causes": [
                "Bệnh mãn tính (đau, khó thở, tiểu đêm)",
                "Thuốc (corticoid, thuốc huyết áp, thuốc chống trầm cảm)",
                "Rối loạn tâm thần (trầm cảm, lo âu)",
                "Thói quen ngủ không tốt"
            ],
            "prognosis": "Cần điều trị, có thể cải thiện bằng liệu pháp không dùng thuốc"
        }
    }
}

