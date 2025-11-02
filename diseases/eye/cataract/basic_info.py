"""
Đục Thủy Tinh Thể (Cataract) - Thông tin cơ bản
Basic information about Cataract
"""

from typing import Dict

CATARACT_INFO = {
    "name": "Đục Thủy Tinh Thể",
    "name_en": "Cataract",
    
    "simple_explanation": """
💡 Đục thủy tinh thể là gì? (Giải thích đơn giản)

Tưởng tượng mắt như máy ảnh:
- Mắt BÌNH THƯỜNG: Thủy tinh thể trong suốt, ánh sáng đi qua rõ ràng
- Mắt ĐỤC THỦY TINH THỂ: Thủy tinh thể bị mờ đục → Ánh sáng không đi qua được

👁️ Chuyện gì xảy ra:
1. Thủy tinh thể (lens) bị ĐỤC, MỜ (như kính bị ố)
2. Ánh sáng không đi qua được → Mắt nhìn MỜ
3. Từ từ nặng hơn → Nhìn như qua lớp sương mù
4. Cuối cùng → MỜ HOÀN TOÀN, chỉ còn nhìn thấy sáng/tối

⚠️ ĐẶC ĐIỂM:
- Rất phổ biến ở người già (>60 tuổi)
- Phát triển TỪ TỪ (nhiều năm)
- CÓ THỂ chữa khỏi bằng phẫu thuật (thay thủy tinh thể)
- Không đau, không đỏ mắt
    """,
    
    "definition": """
Đục thủy tinh thể là tình trạng thủy tinh thể (lens) của mắt bị mờ đục,
khiến ánh sáng không thể đi qua một cách rõ ràng, dẫn đến giảm thị lực.
    """,
    
    "statistics_vietnam": {
        "prevalence": "Rất phổ biến ở người >60 tuổi (50-80%)",
        "age_related": "Tăng theo tuổi: 60-70 tuổi: 30%, 70-80 tuổi: 50%, >80 tuổi: 80%",
        "causes_blindness": "Nguyên nhân mù lòa hàng đầu ở người già (40%)",
        "treatable": "Có thể chữa khỏi bằng phẫu thuật (95% thành công)"
    },
    
    "types": {
        "age_related": {
            "name": "Đục thủy tinh thể do tuổi già",
            "prevalence": "Phổ biến nhất (90%)",
            "progression": "Phát triển từ từ, nhiều năm"
        },
        "traumatic": {
            "name": "Đục thủy tinh thể do chấn thương",
            "cause": "Chấn thương mắt",
            "progression": "Có thể phát triển nhanh"
        },
        "secondary": {
            "name": "Đục thủy tinh thể thứ phát",
            "causes": [
                "Tiểu đường",
                "Dùng corticoid lâu dài",
                "Viêm mắt, bệnh mắt khác"
            ]
        },
        "congenital": {
            "name": "Đục thủy tinh thể bẩm sinh",
            "prevalence": "Hiếm (1-2%)",
            "timing": "Xuất hiện từ khi sinh"
        }
    }
}

