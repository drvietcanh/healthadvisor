"""
Asthma Symptoms - Triệu chứng hen suyễn
========================================

Mô tả các triệu chứng chính, thời điểm, mức độ nặng
"""

SYMPTOMS = {
    "main_symptoms": {
        "title": "🔍 4 Triệu Chứng Chính - Dễ Nhận Biết",
        "symptoms": [
            {
                "name": "Khó Thở ĐỢT",
                "icon": "😤",
                "description": "Khó thở ĐỘT NGỘT, có khi khỏe hẳn",
                "characteristics": [
                    "Xuất hiện BẤT NGỜ",
                    "Thở KHÒ KHÈ (nghe rõ)",
                    "Cảm giác ngực BÍ, CHẶT",
                    "Có lúc khỏe, có lúc khó thở (KHÔNG mãi mãi khó thở)"
                ],
                "key": "⭐ Có lúc KHỎE HOÀN TOÀN = Khác COPD!"
            },
            {
                "name": "Thở Khò Khè (Wheezing)",
                "icon": "🎵",
                "description": "Tiếng HÚT, RỐNG khi thở ra",
                "details": [
                    "Nghe rõ cả khi KHÔNG dùng ống nghe",
                    "Giống tiếng còi, tiếng rống",
                    "Nhiều nhất khi THỞ RA",
                    "Ban đêm/sáng sớm rõ hơn"
                ],
                "note": "Trẻ em thở khò khè → PHẢI NGHĨ ĐẾN HEN!"
            },
            {
                "name": "Ho (Đặc Biệt Ban Đêm)",
                "icon": "😷",
                "description": "Ho khan, không đờm (hoặc ít đờm)",
                "patterns": [
                    "Ho NHIỀU ban đêm, sáng sớm",
                    "Ho khi GẮN SỨC (chạy, cười)",
                    "Ho khi hít KHÔNG KHÍ LẠNH",
                    "Ho SAU KHI gặp dị nguyên"
                ],
                "common_mistake": "Nhiều người tưởng ho do VIÊM họng → Uống kháng sinh KHÔNG đỡ!"
            },
            {
                "name": "Tức Ngực",
                "icon": "🫀",
                "description": "Cảm giác CHẶT NGỰC, khó thở",
                "feelings": [
                    "Như có vật NẶNG đè lên ngực",
                    "Ngực BÍ, CHẶT",
                    "Muốn MỞ RỘNG ngực ra"
                ]
            }
        ]
    },
    
    "timing_patterns": {
        "title": "⏰ Khi Nào Hay Hen?",
        "patterns": [
            {
                "time": "Ban Đêm/Sáng Sớm (3-5 giờ sáng)",
                "reason": "Hormone thay đổi, nhiệt độ giảm",
                "frequency": "Rất phổ biến (70-80% bệnh nhân)",
                "tip": "Thức dậy vì khó thở → CẦN điều trị tốt hơn!"
            },
            {
                "time": "Khi Gắng Sức",
                "examples": ["Chạy", "Leo cầu thang", "Cười nhiều", "Khóc"],
                "name": "Hen khi gắng sức (Exercise-Induced Asthma)",
                "tip": "Xịt thuốc TRƯỚC khi chạy → Phòng được!"
            },
            {
                "time": "Thay Đổi Thời Tiết",
                "triggers": ["Trời lạnh đột ngột", "Gió mùa", "Độ ẩm cao"],
                "note": "Mùa đông, giao mùa hay hen hơn"
            },
            {
                "time": "Sau Khi Tiếp Xúc Dị Nguyên",
                "examples": ["Quét nhà → Bụi bay lên", "Vuốt mèo", "Ngửi nước hoa"],
                "delay": "Có thể SAU vài phút đến vài giờ"
            }
        ]
    },
    
    "severe_attack_signs": {
        "title": "🚨 Cơn Hen NẶNG - Cần Cấp Cứu NGAY!",
        "danger_signs": [
            "Khó thở NẶNG, không nói được câu hoàn chỉnh",
            "Môi, móng tay TÍM (thiếu oxy)",
            "Ngực THỤT SÂU khi hít vào (sườn lõm vào)",
            "Thở rất NHANH (>30 lần/phút)",
            "Lú lẫn, buồn ngủ bất thường",
            "Xịt thuốc MÀ KHÔNG ĐỠ"
        ],
        "action": "📞 **GỌI 115 NGAY!** Không chờ, không tự đi!",
        "while_waiting": [
            "Ngồi thẳng người (KHÔNG nằm)",
            "Xịt thuốc giãn phế quản (2-4 nhát, cách 20 giây)",
            "Thở MÔI (hít mũi, thở ra miệng mím)",
            "Giữ bình tĩnh"
        ]
    },
    
    "children_specific": {
        "title": "👶 Triệu Chứng Hen Ở TRẺ EM",
        "signs": [
            "Ho kéo dài >2 tuần (KHÔNG sốt, không cảm)",
            "Thở khò khè, đặc biệt ban đêm",
            "Khó thở khi chơi, chạy nhảy",
            "Ho sau khi CƯỜI hoặc KHÓC",
            "Thường xuyên viêm phế quản (>3 lần/năm)",
            "Gia đình có người dị ứng/hen"
        ],
        "note": "⚠️ Trẻ <5 tuổi KHÓ chẩn đoán hen (triệu chứng giống cảm, viêm phổi)"
    }
}

