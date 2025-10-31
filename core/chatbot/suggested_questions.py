"""
Suggested Questions
Câu hỏi gợi ý theo ngữ cảnh
"""

from typing import List


def get_suggested_questions(context: str = "general") -> List[str]:
    """Câu hỏi gợi ý theo ngữ cảnh"""
    
    suggestions = {
        "general": [
            "Huyết áp bao nhiêu là bình thường?",
            "Dấu hiệu đột quỵ là gì?",
            "Đường huyết cao phải làm sao?",
            "Ăn gì để giảm huyết áp?",
            "Khi nào cần gọi cấp cứu 115?"
        ],
        "hypertension": [
            "Thuốc huyết áp có tác dụng phụ gì?",
            "Ăn bao nhiêu muối mỗi ngày?",
            "Có được bỏ thuốc khi huyết áp đã bình thường?",
            "Vận động thế nào an toàn?",
            "Đo huyết áp đúng cách ra sao?"
        ],
        "diabetes": [
            "Đường huyết 7.5 mmol/L có cao không?",
            "Insulin tiêm vào đâu?",
            "Hạ đường huyết xử trí thế nào?",
            "Ăn carb là ăn gì?",
            "Có cần kiêng trái cây không?"
        ],
        "stroke": [
            "BE-FAST là gì?",
            "Đột quỵ phải làm gì ngay?",
            "Phòng ngừa đột quỵ như thế nào?",
            "Thời gian vàng là bao lâu?",
            "Đột quỵ có khỏi hẳn không?"
        ],
        "nutrition": [
            "Thực đơn cho người huyết áp cao?",
            "Món nào ít muối?",
            "Cách tính carb trong bữa ăn?",
            "Ăn gì tốt cho tim?",
            "Trái cây nào tốt cho tiểu đường?"
        ],
        "medication": [
            "Thuốc uống lúc nào?",
            "Quên uống thuốc thì sao?",
            "Tác dụng phụ thuốc là gì?",
            "Có được uống thuốc cùng lúc?",
            "Khi nào báo bác sĩ về thuốc?"
        ]
    }
    
    return suggestions.get(context, suggestions["general"])

