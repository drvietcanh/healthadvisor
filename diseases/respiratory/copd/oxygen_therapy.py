"""
COPD Oxygen Therapy - Oxy liệu pháp
====================================

Hướng dẫn về thở oxy tại nhà cho COPD nặng
"""

OXYGEN_THERAPY = {
    "title": "🫁 Oxy Liệu Pháp - Quan Trọng Với COPD Nặng",
    
    "simple_explanation": """
💡 Thở oxy tại nhà là gì?

Khi phổi yếu, không đủ oxy → Cần bổ sung oxy:
- Máy tạo oxy di động
- Bình oxy
- Thở qua ống mũi

Mục tiêu: Giữ SpO2 ≥90% (nồng độ oxy máu)
    """,
    
    "indications": [
        "SpO2 ≤88% khi nghỉ ngơi",
        "PaO2 ≤55 mmHg (khí máu động mạch)",
        "Cor pulmonale (tim phổi)",
        "Hồng cầu tăng cao (Hct >55%)"
    ],
    
    "prescription": {
        "flow_rate": "1-3 lít/phút (qua ống mũi)",
        "duration": "≥15 giờ/ngày (càng nhiều càng tốt)",
        "target": "SpO2 88-92% (KHÔNG quá cao!)",
        "note": "⚠️ COPD KHÔNG nên thở oxy quá cao (>92%) → Nguy hiểm!"
    },
    
    "types": [
        {
            "type": "Máy tạo oxy (Oxygen Concentrator)",
            "pros": "Dùng điện, không hết oxy, tiết kiệm lâu dài",
            "cons": "Đầu tư ban đầu cao",
            "price": "15-30 triệu đồng (mua 1 lần)",
            "use": "Dùng tại nhà, lâu dài"
        },
        {
            "type": "Bình oxy y tế",
            "pros": "Di động được",
            "cons": "Hết oxy phải đổi, tốn kém",
            "price": "200,000-500,000đ/bình (dùng ~1 tuần)",
            "use": "Ra ngoài, di chuyển"
        }
    ],
    
    "benefits": [
        "Giảm khó thở",
        "Tăng khả năng vận động",
        "Kéo dài sống (duy nhất điều trị làm tăng tuổi thọ!)",
        "Cải thiện chất lượng cuộc sống",
        "Giảm áp lực phổi, bảo vệ tim"
    ],
    
    "insurance": "BHYT chi trả một phần chi phí oxy tại nhà (có chỉ định)"
}

