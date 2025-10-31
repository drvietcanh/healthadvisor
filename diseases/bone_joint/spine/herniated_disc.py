"""
Herniated Disc - Thoát vị đĩa đệm
"""

HERNIATED_DISC_INFO = {
    "title": "🫁 Thoát Vị Đĩa Đệm (Herniated Disc)",
    "simple_explanation": """
💡 Thoát vị đĩa đệm là gì?

Cột sống có các đĩa đệm (như miếng đệm giữa các đốt sống):
- Đĩa đệm: Lớp ngoài cứng, bên trong mềm (như bánh donut)
- Thoát vị: Phần mềm bên trong TRÀN RA NGOÀI
- Chèn ép dây thần kinh → Đau, tê, yếu

🕐 Ai dễ bị?
- Tuổi 30-50
- Ngồi nhiều, ít vận động
- Mang vác nặng sai tư thế
- Vặn người đột ngột
- Thừa cân
    """,
    
    "common_locations": {
        "lumbar": {
            "name": "Thắt lưng (phổ biến nhất)",
            "symptoms": ["Đau lưng", "Đau lan xuống mông, đùi, cẳng chân", "Tê chân", "Yếu chân"]
        },
        "cervical": {
            "name": "Cổ",
            "symptoms": ["Đau cổ", "Đau lan xuống vai, cánh tay", "Tê tay", "Yếu tay"]
        }
    }
}

HERNIATED_DISC_SYMPTOMS = {
    "title": "🔍 Triệu Chứng Thoát Vị Đĩa Đệm",
    
    "main_symptoms": [
        "Đau lưng/cổ (thường 1 bên)",
        "Đau lan xuống chân/tay (đặc trưng!)",
        "Tê bì, kiến bò",
        "Yếu cơ (khó đứng dậy, khó cầm nắm)",
        "Đau tăng khi ho, hắt hơi, rặn",
        "Đau giảm khi nằm nghỉ"
    ],
    
    "severity": {
        "mild": {
            "level": "Nhẹ",
            "symptoms": ["Đau lưng/cổ nhẹ", "Chưa lan xuống chân/tay"],
            "treatment": "Nghỉ ngơi, thuốc giảm đau, tập thể dục"
        },
        "moderate": {
            "level": "Vừa",
            "symptoms": ["Đau lan xuống chân/tay", "Tê nhẹ"],
            "treatment": "Thuốc giảm đau, vật lý trị liệu, tiêm ngoài màng cứng"
        },
        "severe": {
            "level": "Nặng",
            "symptoms": ["Yếu chân/tay rõ", "Mất cảm giác", "Mất kiểm soát tiểu tiện"],
            "treatment": "PHẪU THUẬT (cấp cứu!)"
        }
    },
    
    "red_flags": [
        "🚨 YẾU CHÂN/TAY rõ ràng → Có thể liệt!",
        "🚨 MẤT KIỂM SOÁT tiểu tiện, đại tiện",
        "🚨 Tê bì lan rộng, mất cảm giác hoàn toàn",
        "→ ĐI KHÁM NGAY, có thể cần phẫu thuật!"
    ]
}

HERNIATED_DISC_TREATMENT = {
    "title": "💊 Điều Trị Thoát Vị Đĩa Đệm",
    
    "conservative": {
        "title": "1️⃣ Điều Trị Bảo Tồn (90% trường hợp):",
        "methods": [
            {
                "method": "Nghỉ ngơi",
                "duration": "1-2 ngày, không nằm quá lâu",
                "note": "Nằm quá lâu → Cơ yếu, khó phục hồi"
            },
            {
                "method": "Thuốc giảm đau",
                "drugs": ["Paracetamol", "NSAIDs", "Thuốc giãn cơ"],
                "note": "Giảm đau, viêm"
            },
            {
                "method": "Vật lý trị liệu",
                "what": "Tập mạnh cơ, kéo giãn, massage",
                "duration": "4-6 tuần",
                "benefit": "Quan trọng nhất!"
            },
            {
                "method": "Tiêm ngoài màng cứng",
                "when": "Đau nhiều, không đỡ thuốc",
                "what": "Tiêm Corticoid + thuốc tê",
                "duration": "Hiệu quả 1-3 tháng"
            }
        ],
        "success_rate": "80-90% tự khỏi sau 6-8 tuần"
    },
    
    "surgery": {
        "title": "2️⃣ Phẫu Thuật (10% trường hợp):",
        "indications": [
            "Yếu chân/tay rõ (có thể liệt)",
            "Mất kiểm soát tiểu tiện",
            "Đau không đỡ sau 6 tuần điều trị",
            "Tái phát nhiều lần"
        ],
        "types": [
            {
                "type": "Mổ hở",
                "what": "Lấy đĩa đệm bị thoát vị",
                "recovery": "6-12 tuần"
            },
            {
                "type": "Nội soi",
                "what": "Lấy đĩa đệm qua ống nhỏ",
                "benefit": "Ít xâm lấn, phục hồi nhanh hơn"
            }
        ]
    },
    
    "prevention": [
        "Tập mạnh cơ lưng, bụng",
        "Giữ tư thế đúng",
        "Tránh mang vác nặng sai tư thế",
        "Giữ cân nặng hợp lý",
        "Tập thể dục đều đặn"
    ]
}

