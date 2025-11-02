"""
Mất Ngủ - Triệu chứng
Symptoms of Insomnia
"""

from typing import Dict, List

SYMPTOMS = {
    "sleep_symptoms": {
        "title": "🔍 Triệu Chứng Về Giấc Ngủ",
        "description": "Các triệu chứng chính:",
        "symptoms": [
            {
                "name": "Khó vào giấc ngủ",
                "icon": "😴",
                "description": "Nằm trên giường >30 phút mà không ngủ được",
                "details": [
                    "Suy nghĩ nhiều, không tắt được suy nghĩ",
                    "Lo lắng về việc không ngủ được",
                    "Xoay trở, không tìm được tư thế thoải mái"
                ]
            },
            {
                "name": "Ngủ không sâu, dễ tỉnh",
                "icon": "😰",
                "description": "Tỉnh giấc nhiều lần trong đêm",
                "details": [
                    "Tỉnh 3-5 lần/đêm hoặc nhiều hơn",
                    "Khó ngủ lại sau khi tỉnh",
                    "Ngủ chập chờn, không sâu"
                ]
            },
            {
                "name": "Thức dậy sớm",
                "icon": "🌅",
                "description": "Tỉnh trước 6h sáng, không ngủ lại được",
                "details": [
                    "Tỉnh lúc 3-4h sáng",
                    "Nằm mãi không ngủ lại được",
                    "Phải dậy sớm"
                ]
            },
            {
                "name": "Cảm giác không ngủ đủ",
                "icon": "😓",
                "description": "Ngủ đủ giờ nhưng vẫn cảm thấy mệt",
                "details": [
                    "Ngủ 7-8 giờ nhưng vẫn mệt",
                    "Chất lượng giấc ngủ kém"
                ]
            }
        ]
    },
    
    "daytime_symptoms": {
        "title": "🔍 Triệu Chứng Ban Ngày (Do mất ngủ)",
        "description": "Mất ngủ → Ảnh hưởng ban ngày:",
        "symptoms": [
            {
                "name": "Mệt mỏi",
                "icon": "😴",
                "description": "Mệt mỏi, buồn ngủ ban ngày"
            },
            {
                "name": "Khó tập trung",
                "icon": "🧠",
                "description": "Khó tập trung, làm việc kém hiệu quả"
            },
            {
                "name": "Cáu gắt",
                "icon": "😠",
                "description": "Dễ cáu gắt, khó chịu"
            },
            {
                "name": "Lo âu về giấc ngủ",
                "icon": "😟",
                "description": "Lo lắng về việc không ngủ được (tạo vòng luẩn quẩn)"
            },
            {
                "name": "Đau đầu",
                "icon": "🤕",
                "description": "Đau đầu khi thức dậy"
            },
            {
                "name": "Suy giảm trí nhớ",
                "icon": "🧠",
                "description": "Quên, khó nhớ"
            }
        ]
    },
    
    "when_to_see_doctor": {
        "title": "👨‍⚕️ Khi Nào Cần Khám?",
        "indicators": [
            "Mất ngủ ≥3 lần/tuần, kéo dài >1 tháng",
            "Ảnh hưởng công việc, sinh hoạt hàng ngày",
            "Mệt mỏi, cáu gắt ban ngày",
            "Có triệu chứng trầm cảm, lo âu",
            "Dùng thuốc ngủ không hiệu quả",
            "Mất ngủ kèm ngáy to, ngưng thở (nghĩ đến hội chứng ngưng thở khi ngủ)"
        ]
    }
}

