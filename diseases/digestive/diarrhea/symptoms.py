"""
Diarrhea - Triệu chứng
"""

SYMPTOMS = {
    "common": {
        "title": "🔍 Triệu chứng thường gặp:",
        "symptoms": [
            "**Đi ngoài lỏng, nhiều lần** - 3-10+ lần/ngày",
            "**Phân lỏng hoặc nước** - Không thành khuôn",
            "**Đau quặn bụng** - Đau từng cơn, vùng bụng dưới",
            "**Buồn nôn, nôn** - Đặc biệt nếu ngộ độc thức ăn",
            "**Đầy bụng, chướng bụng** - Khó chịu ở bụng",
            "**Sốt nhẹ** - 37.5-38°C (nếu nhiễm trùng)"
        ]
    },
    
    "dehydration": {
        "title": "⚠️ Dấu hiệu MẤT NƯỚC (Nguy hiểm!):",
        "mild": {
            "title": "Mất nước nhẹ:",
            "signs": [
                "Khát nước",
                "Miệng khô",
                "Tiểu ít hơn bình thường",
                "Mệt mỏi"
            ]
        },
        "severe": {
            "title": "Mất nước nặng (CẦN CẤP CỨU!):",
            "signs": [
                "🚨 Không đi tiểu >6 giờ",
                "🚨 Khô miệng, mắt trũng",
                "🚨 Da khô, nhăn nheo (véo da không về ngay)",
                "🚨 Chóng mặt, ngất khi đứng",
                "🚨 Tim đập nhanh, yếu mạch",
                "🚨 Lú lẫn (người già)",
                "🚨 Mệt mỏi cực độ, không uống được nước"
            ],
            "warning": "⚠️ Mất nước nặng → CẤP CỨU NGAY! Phải truyền dịch!"
        }
    },
    
    "emergency": {
        "title": "🚨 Dấu hiệu cấp cứu:",
        "signs": [
            "Phân có máu (đỏ tươi hoặc đen)",
            "Sốt cao (>39°C) kèm ớn lạnh",
            "Đau bụng dữ dội",
            "Nôn liên tục, không uống được nước",
            "Dấu hiệu mất nước nặng",
            "Trẻ em < 2 tuổi, người già > 70 tuổi"
        ]
    }
}

