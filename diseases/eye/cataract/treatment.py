"""
Đục Thủy Tinh Thể - Điều trị
Treatment of Cataract
"""

from typing import Dict, List

TREATMENT = {
    "surgery": {
        "title": "🔪 Phẫu Thuật - Điều Trị Duy Nhất",
        "description": "Đục thủy tinh thể CHỈ có thể chữa bằng phẫu thuật (KHÔNG có thuốc chữa):",
        "method": {
            "name": "Phẫu Thuật Phaco (Phacoemulsification)",
            "description": "Phương pháp phổ biến nhất (90% ca)",
            "how": [
                "Rạch nhỏ (2-3mm) ở giác mạc",
                "Dùng sóng siêu âm phá vỡ thủy tinh thể đục",
                "Hút ra ngoài",
                "Đặt thủy tinh thể nhân tạo (IOL) vào trong",
                "Không cần khâu (vết thương tự lành)"
            ],
            "duration": "15-30 phút",
            "anesthesia": "Gây tê tại chỗ (không cần gây mê)",
            "recovery": "Về nhà trong ngày, khỏi sau 1-2 tuần"
        },
        "when_to_operate": {
            "title": "⏰ Khi Nào Nên Phẫu Thuật?",
            "indicators": [
                {
                    "name": "Ảnh hưởng cuộc sống",
                    "description": "Nhìn mờ ảnh hưởng công việc, sinh hoạt hàng ngày",
                    "examples": [
                        "Không đọc được sách, báo",
                        "Không xem được TV",
                        "Khó lái xe (đặc biệt ban đêm)",
                        "Khó làm việc nhà",
                        "Nguy cơ té ngã (không nhìn rõ)"
                    ]
                },
                {
                    "name": "Thị lực giảm",
                    "criteria": "Thị lực <20/40 (6/12) hoặc theo bác sĩ",
                    "note": "Không nhất thiết phải đợi đến mù hoàn toàn!"
                },
                {
                    "name": "Đục thủy tinh thể nặng",
                    "description": "Bác sĩ đánh giá đục nặng, sẽ nặng hơn"
                }
            ],
            "note": "💡 Quyết định phẫu thuật tùy thuộc vào: Mức độ ảnh hưởng cuộc sống, không phải chỉ thị lực!"
        },
        "risks": {
            "title": "⚠️ Biến Chứng Phẫu Thuật",
            "description": "Phẫu thuật AN TOÀN, nhưng có thể có biến chứng:",
            "common": [
                "Viêm mắt (1-2%) → Điều trị bằng thuốc nhỏ mắt",
                "Tăng nhãn áp (1-2%) → Điều trị bằng thuốc",
                "Phù giác mạc (1-2%) → Tự khỏi sau vài tuần"
            ],
            "rare": [
                "Nhiễm trùng mắt (0.1%) → Nghiêm trọng, cần điều trị ngay",
                "Bong võng mạc (0.1%) → Cần phẫu thuật",
                "Xuất huyết mắt (rất hiếm)",
                "Mất thị lực vĩnh viễn (rất hiếm, <0.01%)"
            ],
            "success_rate": "95-98% thành công, không có biến chứng nghiêm trọng"
        },
        "after_surgery": {
            "title": "🏥 Sau Phẫu Thuật",
            "care": [
                {
                    "name": "Ngay sau mổ",
                    "items": [
                        "Đeo kính bảo vệ mắt",
                        "Nhỏ thuốc kháng sinh, kháng viêm (theo chỉ định)",
                        "Tránh dụi mắt",
                        "Tránh nước vào mắt (1 tuần)",
                        "Tránh gắng sức, nâng vật nặng (1 tuần)"
                    ]
                },
                {
                    "name": "1-2 tuần đầu",
                    "items": [
                        "Nhỏ thuốc đều đặn",
                        "Không dụi mắt",
                        "Không bơi lội",
                        "Tránh bụi, khói",
                        "Tái khám theo lịch"
                    ]
                },
                {
                    "name": "Sau 1-2 tuần",
                    "items": [
                        "Thị lực cải thiện rõ",
                        "Có thể làm việc bình thường",
                        "Có thể cần đeo kính mới (đọc sách, xa/gần)"
                    ]
                }
            ]
        }
    },
    
    "no_medical_treatment": {
        "title": "❌ KHÔNG Có Thuốc Chữa",
        "description": "Quan trọng: KHÔNG có thuốc nhỏ mắt, thuốc uống nào CHỮA được đục thủy tinh thể!",
        "false_claims": [
            "Thuốc nhỏ mắt 'chữa đục thủy tinh thể' → KHÔNG có tác dụng",
            "Thực phẩm chức năng → KHÔNG chữa được",
            "Chỉ có PHẪU THUẬT mới chữa được!"
        ],
        "prevention": "Có thể LÀM CHẬM tiến triển bằng: Tránh ánh sáng tia cực tím, ăn uống lành mạnh"
    }
}

