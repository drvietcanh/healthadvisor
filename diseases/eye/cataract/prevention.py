"""
Đục Thủy Tinh Thể - Phòng ngừa
Prevention of Cataract
"""

from typing import Dict, List

PREVENTION = {
    "sun_protection": {
        "title": "🕶️ Bảo Vệ Mắt Khỏi Ánh Sáng Mặt Trời",
        "description": "Ánh sáng tia cực tím (UV) là yếu tố nguy cơ chính:",
        "methods": [
            {
                "name": "Đeo kính râm chống tia UV",
                "when": "Khi ra ngoài trời nắng",
                "requirement": "Kính phải có nhãn 'UV400' hoặc '100% UV protection'",
                "benefit": "Giảm nguy cơ 30-40%"
            },
            {
                "name": "Đội mũ rộng vành",
                "benefit": "Che bóng, giảm ánh sáng trực tiếp vào mắt"
            },
            {
                "name": "Tránh nắng giờ cao điểm",
                "time": "10h-14h (tia UV mạnh nhất)"
            }
        ]
    },
    "nutrition": {
        "title": "🍽️ Dinh Dưỡng",
        "description": "Một số chất có thể làm chậm tiến triển:",
        "foods": [
            {
                "name": "Chất chống oxy hóa",
                "foods": [
                    "Rau xanh (rau cải, bông cải xanh)",
                    "Trái cây (cam, quýt, dâu)",
                    "Cà rốt (beta-carotene)"
                ],
                "benefit": "Giảm tổn thương do oxy hóa"
            },
            {
                "name": "Vitamin C",
                "foods": ["Cam, quýt", "Ớt chuông", "Bông cải"],
                "benefit": "Bảo vệ thủy tinh thể"
            },
            {
                "name": "Vitamin E",
                "foods": ["Hạnh nhân", "Hạt hướng dương", "Dầu thực vật"],
                "benefit": "Chống oxy hóa"
            }
        ],
        "note": "💡 Ăn uống lành mạnh → Làm chậm tiến triển, KHÔNG ngăn ngừa hoàn toàn"
    },
    "lifestyle": {
        "title": "🏃 Lối Sống",
        "methods": [
            {
                "name": "Kiểm soát tiểu đường",
                "benefit": "Giảm nguy cơ đục thủy tinh thể thứ phát",
                "target": "HbA1c <7%"
            },
            {
                "name": "Tránh hút thuốc",
                "benefit": "Hút thuốc tăng nguy cơ 2-3 lần"
            },
            {
                "name": "Hạn chế rượu",
                "benefit": "Rượu quá mức tăng nguy cơ"
            },
            {
                "name": "Khám mắt định kỳ",
                "frequency": "Mỗi năm 1 lần (nếu >60 tuổi)",
                "benefit": "Phát hiện sớm, chuẩn bị phẫu thuật"
            }
        ]
    },
    "when_to_see_doctor": {
        "title": "👨‍⚕️ Khi Nào Cần Khám?",
        "indicators": [
            "Nhìn mờ dần (không rõ nguyên nhân)",
            "Chói mắt với ánh sáng",
            "Thị lực giảm ảnh hưởng cuộc sống",
            ">60 tuổi (khám định kỳ)",
            "Có tiểu đường, dùng corticoid lâu dài"
        ],
        "note": "⚠️ Khám sớm → Chuẩn bị phẫu thuật tốt hơn!"
    }
}

