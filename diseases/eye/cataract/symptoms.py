"""
Đục Thủy Tinh Thể - Triệu chứng
Symptoms of Cataract
"""

from typing import Dict, List

SYMPTOMS = {
    "common_symptoms": {
        "title": "🔍 Triệu Chứng Thường Gặp",
        "description": "Đục thủy tinh thể phát triển từ từ, triệu chứng tăng dần:",
        "symptoms": [
            {
                "name": "Nhìn mờ",
                "icon": "👁️",
                "description": "Nhìn mờ dần, như qua lớp sương mù",
                "progression": [
                    "Giai đoạn đầu: Nhìn mờ nhẹ",
                    "Giai đoạn giữa: Nhìn mờ rõ rệt",
                    "Giai đoạn nặng: Nhìn mờ gần như hoàn toàn"
                ],
                "note": "⚠️ Mờ dần, KHÔNG đau, KHÔNG đỏ mắt"
            },
            {
                "name": "Chói mắt với ánh sáng",
                "icon": "💡",
                "description": "Chói mắt khi gặp ánh sáng (đèn xe, mặt trời)",
                "why": "Thủy tinh thể đục → Ánh sáng bị tán xạ → Chói",
                "impact": "Khó lái xe ban đêm (chói đèn xe)"
            },
            {
                "name": "Nhìn đôi một mắt",
                "icon": "👀",
                "description": "Nhìn một vật thành hai (chỉ một mắt bị)",
                "why": "Thủy tinh thể đục không đều → Ánh sáng bị khúc xạ khác nhau"
            },
            {
                "name": "Màu sắc nhạt đi",
                "icon": "🌈",
                "description": "Màu sắc không còn tươi, nhạt đi",
                "why": "Thủy tinh thể đục → Màu vàng, nâu → Màu sắc bị lọc",
                "example": "Màu xanh có vẻ xám, màu đỏ có vẻ nâu"
            },
            {
                "name": "Thay đổi độ kính",
                "icon": "👓",
                "description": "Độ kính thay đổi thường xuyên",
                "why": "Thủy tinh thể đục → Độ khúc xạ thay đổi",
                "note": "Có thể cận thị tăng (nhưng không phải do cận thận thật)"
            },
            {
                "name": "Nhìn tốt hơn khi trời tối",
                "icon": "🌙",
                "description": "Nhìn rõ hơn khi ánh sáng yếu",
                "why": "Ánh sáng yếu → Ít tán xạ → Nhìn rõ hơn",
                "note": "Ngược với tăng nhãn áp (nhìn tệ hơn khi tối)"
            }
        ]
    },
    
    "progression": {
        "title": "📊 Tiến Triển",
        "description": "Đục thủy tinh thể phát triển từ từ:",
        "stages": [
            {
                "stage": "Giai đoạn đầu",
                "duration": "Vài năm",
                "symptoms": [
                    "Nhìn mờ nhẹ",
                    "Chói mắt khi gặp ánh sáng",
                    "Có thể không ảnh hưởng cuộc sống"
                ]
            },
            {
                "stage": "Giai đoạn giữa",
                "duration": "Vài năm",
                "symptoms": [
                    "Nhìn mờ rõ rệt",
                    "Khó đọc sách, xem TV",
                    "Khó lái xe (đặc biệt ban đêm)",
                    "Ảnh hưởng cuộc sống hàng ngày"
                ]
            },
            {
                "stage": "Giai đoạn nặng",
                "duration": "Nhiều năm",
                "symptoms": [
                    "Nhìn mờ gần như hoàn toàn",
                    "Chỉ còn nhìn thấy sáng/tối",
                    "Ảnh hưởng nghiêm trọng cuộc sống",
                    "Cần phẫu thuật"
                ]
            }
        ],
        "note": "💡 Tiến triển chậm (5-10 năm) → Có thời gian chuẩn bị phẫu thuật"
    },
    
    "warning_signs": {
        "title": "🚨 Dấu Hiệu Cần Khám Ngay",
        "signs": [
            "Nhìn mờ đột ngột (KHÔNG phải đục thủy tinh thể → Nghĩ đến đột quỵ mắt, bong võng mạc)",
            "Đau mắt, đỏ mắt (KHÔNG phải đục thủy tinh thể → Nghĩ đến viêm, tăng nhãn áp)",
            "Mờ một mắt đột ngột (Nghĩ đến đột quỵ)",
            "Nhìn có 'bóng đen' che (Nghĩ đến bong võng mạc)",
            "Mờ kèm đau đầu (Nghĩ đến tăng nhãn áp)"
        ],
        "note": "⚠️ Đục thủy tinh thể KHÔNG đau, KHÔNG đỏ, KHÔNG đột ngột! Nếu có → Khám NGAY!"
    }
}

