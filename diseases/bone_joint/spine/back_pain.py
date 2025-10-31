"""
Back Pain - Đau thắt lưng
Bệnh phổ biến nhất về cột sống
"""

BACK_PAIN_INFO = {
    "title": "🫁 Đau Thắt Lưng (Low Back Pain)",
    "simple_explanation": """
💡 Đau thắt lưng là gì?

Đau ở vùng lưng dưới (thắt lưng), từ xương sườn cuối đến mông.
- 80% người trưởng thành bị ít nhất 1 lần
- Nguyên nhân: Cơ, dây chằng, đĩa đệm, khớp

🕐 Ai dễ bị?
- Người 30-50 tuổi
- Ngồi nhiều, ít vận động
- Mang vác nặng, vặn người sai tư thế
- Thừa cân, béo phì
- Phụ nữ có thai
- Người cao tuổi
    """,
    
    "types": {
        "acute": {
            "name": "Cấp tính (<6 tuần)",
            "characteristics": "Đau đột ngột, thường do chấn thương",
            "prognosis": "Tự khỏi 90% trong 2-4 tuần"
        },
        "chronic": {
            "name": "Mạn tính (>12 tuần)",
            "characteristics": "Đau kéo dài, tái phát",
            "prognosis": "Cần điều trị tích cực"
        }
    }
}

BACK_PAIN_CAUSES = {
    "title": "🔍 Nguyên Nhân Đau Thắt Lưng",
    
    "mechanical": {
        "title": "1️⃣ Cơ học (90% trường hợp):",
        "causes": [
            {
                "cause": "Căng cơ, dây chằng",
                "why": "Nhấc vật nặng sai tư thế, vặn người đột ngột",
                "characteristics": "Đau khi cử động, giảm khi nghỉ"
            },
            {
                "cause": "Thoát vị đĩa đệm",
                "why": "Đĩa đệm chèn ép dây thần kinh",
                "characteristics": "Đau lan xuống chân, tê bì"
            },
            {
                "cause": "Thoái hóa cột sống",
                "why": "Mòn khớp, xương do tuổi tác",
                "characteristics": "Đau khi đứng lâu, cải thiện khi nghỉ"
            },
            {
                "cause": "Hẹp ống sống",
                "why": "Ống sống bị hẹp, chèn ép tủy sống",
                "characteristics": "Đau khi đi, giảm khi ngồi/cúi"
            }
        ]
    },
    
    "other_causes": {
        "title": "2️⃣ Nguyên nhân khác (ít gặp hơn):",
        "causes": [
            "Nhiễm trùng cột sống",
            "Ung thư di căn",
            "Gãy xương (loãng xương)",
            "Viêm cột sống (viêm khớp dạng thấp)",
            "Bệnh thận (sỏi thận, viêm thận)"
        ]
    },
    
    "risk_factors": [
        "Ngồi nhiều, ít vận động",
        "Mang vác nặng sai tư thế",
        "Thừa cân, béo phì",
        "Hút thuốc lá",
        "Tuổi cao",
        "Căng thẳng, stress"
    ]
}

BACK_PAIN_MANAGEMENT = {
    "title": "💊 Điều Trị Đau Thắt Lưng",
    
    "acute_stage": {
        "title": "Giai đoạn cấp (<6 tuần):",
        "principles": [
            "Nghỉ ngơi ngắn (1-2 ngày), không nằm quá lâu",
            "Vận động nhẹ nhàng sớm",
            "Thuốc giảm đau",
            "Chườm nóng/lạnh"
        ],
        "medications": [
            {
                "drug": "Paracetamol",
                "dose": "500-1000mg, 3-4 lần/ngày",
                "note": "Dùng đầu tiên, an toàn"
            },
            {
                "drug": "NSAIDs (Ibuprofen, Diclofenac)",
                "dose": "Theo chỉ định",
                "note": "Giảm đau + viêm. Uống sau ăn"
            },
            {
                "drug": "Thuốc giãn cơ",
                "example": "Mydocalm, Decontractyl",
                "note": "Khi co cứng cơ nhiều"
            }
        ]
    },
    
    "chronic_stage": {
        "title": "Giai đoạn mạn (>12 tuần):",
        "treatment": [
            "Tập vật lý trị liệu (quan trọng!)",
            "Tập mạnh cơ lưng, bụng",
            "Châm cứu, massage",
            "Thuốc giảm đau (nếu cần)",
            "Tiêm ngoài màng cứng (nếu đau nhiều)",
            "Phẫu thuật (rất ít trường hợp)"
        ]
    },
    
    "red_flags": [
        "🚨 Tê bì, yếu chân/tay",
        "🚨 Mất kiểm soát tiểu tiện",
        "🚨 Đau sau chấn thương nặng",
        "🚨 Sốt + đau lưng",
        "🚨 Sụt cân không rõ nguyên nhân",
        "→ ĐI KHÁM NGAY, không chờ!"
    ]
}

BACK_PAIN_EXERCISES = {
    "title": "🏃 Bài Tập Cho Đau Thắt Lưng",
    
    "acute_phase": {
        "title": "Khi đau cấp:",
        "exercises": [
            {
                "name": "Nằm co gối",
                "how": "Nằm ngửa, co 2 gối lên ngực, giữ 10-20 giây",
                "frequency": "10 lần, 3 lần/ngày"
            },
            {
                "name": "Gập bụng nhẹ",
                "how": "Nằm ngửa, gập đầu gối, nâng đầu và vai nhẹ",
                "frequency": "10 lần, 2 lần/ngày"
            },
            {
                "name": "Đi bộ nhẹ",
                "how": "Đi chậm, 5-10 phút, nhiều lần trong ngày",
                "note": "Vận động nhẹ tốt hơn nằm yên"
            }
        ]
    },
    
    "recovery_phase": {
        "title": "Khi đỡ đau:",
        "exercises": [
            {
                "name": "Tăng cường cơ bụng",
                "how": "Gập bụng, plank",
                "benefit": "Cơ bụng mạnh → Bảo vệ lưng"
            },
            {
                "name": "Tăng cường cơ lưng",
                "how": "Nằm sấp, nâng đầu và chân lên",
                "benefit": "Cơ lưng mạnh → Giữ cột sống thẳng"
            },
            {
                "name": "Kéo giãn",
                "how": "Ngồi co gối, vòng tay ôm gối, kéo về ngực",
                "benefit": "Giảm căng cơ"
            }
        ]
    },
    
    "prevention": {
        "title": "Phòng ngừa tái phát:",
        "exercises": [
            "Tập mạnh cơ lưng, bụng 2-3 lần/tuần",
            "Tập yoga, pilates",
            "Bơi lội (nước giảm áp lực)",
            "Đi bộ đều đặn"
        ]
    },
    
    "important": "⚠️ Tránh các động tác: Gập lưng quá mức, vặn người, nhấc vật nặng"
}

