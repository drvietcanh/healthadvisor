"""
CAT Questionnaire - Bảng Đánh Giá COPD
"""

CAT_QUESTIONNAIRE = {
    "name": "CAT - Bảng Đánh Giá COPD",
    "full_name": "COPD Assessment Test",
    "description": "8 câu hỏi đánh giá tác động của COPD đến cuộc sống",
    
    "simple_explanation": """
💡 Bảng CAT là gì?

8 câu hỏi đơn giản về:
- Ho nhiều không?
- Có đờm không?
- Ngực tức không?
- Khó thở khi leo cầu thang?
- Làm việc nhà có khó không?
- Ra khỏi nhà có tự tin không?
- Ngủ có ngon không?
- Có còn sức lực không?

→ Điểm càng CAO = COPD ảnh hưởng càng NHIỀU
    """,
    
    "questions": [
        {
            "number": 1,
            "question": "Tôi không bao giờ ho ←→ Tôi ho liên tục",
            "aspect": "Ho",
            "scale": "0 (không ho) đến 5 (ho liên tục)"
        },
        {
            "number": 2,
            "question": "Tôi không có đờm ←→ Lồng ngực tôi đầy đờm",
            "aspect": "Đờm",
            "scale": "0 (không đờm) đến 5 (đầy đờm)"
        },
        {
            "number": 3,
            "question": "Ngực tôi không tức ←→ Ngực tôi rất tức",
            "aspect": "Ngực tức",
            "scale": "0 (không tức) đến 5 (rất tức)"
        },
        {
            "number": 4,
            "question": "Leo cầu thang không khó thở ←→ Leo cầu thang rất khó thở",
            "aspect": "Khó thở khi gắng sức",
            "scale": "0 (không khó thở) đến 5 (rất khó thở)"
        },
        {
            "number": 5,
            "question": "Làm việc nhà không hạn chế ←→ Làm việc nhà rất hạn chế",
            "aspect": "Hoạt động trong nhà",
            "scale": "0 (không hạn chế) đến 5 (rất hạn chế)"
        },
        {
            "number": 6,
            "question": "Tự tin ra khỏi nhà ←→ Không tự tin ra khỏi nhà",
            "aspect": "Sự tự tin",
            "scale": "0 (rất tự tin) đến 5 (không tự tin)"
        },
        {
            "number": 7,
            "question": "Ngủ rất ngon ←→ Không ngủ được vì COPD",
            "aspect": "Giấc ngủ",
            "scale": "0 (ngủ ngon) đến 5 (không ngủ được)"
        },
        {
            "number": 8,
            "question": "Tràn đầy sức lực ←→ Hoàn toàn mệt mỏi",
            "aspect": "Sức lực",
            "scale": "0 (tràn đầy sức lực) đến 5 (hoàn toàn mệt)"
        }
    ],
    
    "scoring": {
        "range": "0-40 điểm",
        "interpretation": {
            "0-10": {
                "level": "Tác động NHẸ",
                "meaning": "COPD ảnh hưởng ít đến cuộc sống",
                "color": "green"
            },
            "11-20": {
                "level": "Tác động TRUNG BÌNH",
                "meaning": "COPD bắt đầu ảnh hưởng đến sinh hoạt",
                "color": "yellow"
            },
            "21-30": {
                "level": "Tác động NẶNG",
                "meaning": "COPD ảnh hưởng nhiều đến cuộc sống",
                "color": "orange"
            },
            "31-40": {
                "level": "Tác động RẤT NẶNG",
                "meaning": "COPD ảnh hưởng nghiêm trọng đến cuộc sống",
                "color": "red"
            }
        }
    },
    
    "clinical_use": [
        "Theo dõi tiến triển bệnh",
        "Đánh giá hiệu quả điều trị",
        "Quyết định thay đổi phác đồ",
        "Đo lường chất lượng cuộc sống"
    ],
    
    "note": "⚠️ Sự thay đổi ≥2 điểm CAT = Có ý nghĩa lâm sàng"
}

