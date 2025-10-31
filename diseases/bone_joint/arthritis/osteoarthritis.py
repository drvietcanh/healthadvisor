"""
Osteoarthritis - Thoái hóa khớp
Bệnh khớp phổ biến nhất ở người già
"""

# Thông tin chung
OSTEOARTHRITIS_INFO = {
    "title": "🦴 Thoái Hóa Khớp (Osteoarthritis)",
    "simple_explanation": """
💡 Thoái hóa khớp là gì?
    
Giống như bánh xe sau nhiều năm dùng sẽ mòn, khớp xương của chúng ta cũng vậy.
- Sụn khớp (lớp đệm giữa 2 đầu xương) bị mòn dần
- Xương chà xát vào nhau → Đau, cứng khớp
- Thường ở: Gối, háng, cột sống, ngón tay
    
🕐 Ai dễ bị?
- Người > 50 tuổi (80% người 65+ có dấu hiệu)
- Phụ nữ sau mãn kinh
- Người thừa cân, béo phì
- Lao động nặng, vận động viên cũ
- Gia đình có người bị
    """,
    
    "common_joints": {
        "knee": {
            "name": "Gối",
            "frequency": "Phổ biến nhất",
            "why": "Chịu toàn bộ trọng lượng cơ thể",
            "symptoms": ["Đau khi đứng lên ngồi xuống", "Cứng gối buổi sáng", "Kêu răng rắc khi di chuyển"]
        },
        "hip": {
            "name": "Háng",
            "frequency": "Rất phổ biến",
            "symptoms": ["Đau vùng háng, mông", "Khó khăn khi đi lại", "Đau lan xuống đùi"]
        },
        "spine": {
            "name": "Cột sống",
            "frequency": "Phổ biến",
            "symptoms": ["Đau lưng, cứng lưng", "Khó cúi, ngửa", "Có thể chèn ép dây thần kinh"]
        },
        "fingers": {
            "name": "Ngón tay",
            "frequency": "Thường gặp",
            "symptoms": ["Sưng, đau khớp ngón", "U cục ở khớp (Heberden, Bouchard)", "Khó cầm nắm"]
        }
    }
}

# Triệu chứng
OSTEOARTHRITIS_SYMPTOMS = {
    "title": "🔍 Triệu Chứng Thoái Hóa Khớp",
    
    "early_stage": [
        "Đau khớp khi vận động (nhưng giảm khi nghỉ)",
        "Cứng khớp buổi sáng (<30 phút)",
        "Kêu răng rắc khi di chuyển",
        "Hơi sưng khớp sau khi dùng nhiều"
    ],
    
    "advanced_stage": [
        "Đau liên tục, kể cả khi nghỉ",
        "Cứng khớp kéo dài",
        "Sưng khớp rõ ràng",
        "Biến dạng khớp (gối vẹo, ngón tay cong)",
        "Hạn chế vận động (khó leo cầu thang, đứng dậy)",
        "Teo cơ quanh khớp (cơ đùi yếu khi đau gối)"
    ],
    
    "red_flags": [
        "🚨 Sốt + đau khớp → Có thể nhiễm trùng khớp",
        "🚨 Đau đột ngột, dữ dội → Gãy xương?",
        "🚨 Tê bì, yếu chân/tay → Chèn ép dây thần kinh?",
        "🚨 Sưng nóng đỏ → Viêm khớp dạng thấp?"
    ]
}

# Điều trị
OSTEOARTHRITIS_TREATMENT = {
    "title": "💊 Điều Trị Thoái Hóa Khớp",
    
    "non_drug": {
        "title": "1️⃣ Không dùng thuốc (Ưu tiên!):",
        "methods": [
            {
                "method": "⚖️ Giảm cân",
                "explanation": "Mỗi 5kg giảm → Giảm áp lực gối 15-20kg!",
                "benefit": "Giảm đau 50%, chậm tiến triển"
            },
            {
                "method": "🏃 Tập thể dục",
                "explanation": "Tăng cơ bắp → Bảo vệ khớp",
                "types": ["Đi bộ nhẹ", "Bơi lội", "Yoga", "Thái cực quyền", "Đạp xe"]
            },
            {
                "method": "🧊 Chườm lạnh/nóng",
                "explanation": "Chườm lạnh khi sưng đau cấp, chườm nóng khi cứng",
                "how": "15-20 phút, 3-4 lần/ngày"
            },
            {
                "method": "👟 Dụng cụ hỗ trợ",
                "explanation": "Gậy chống, đế giày, nẹp khớp",
                "benefit": "Giảm áp lực lên khớp"
            }
        ]
    },
    
    "medications": {
        "title": "2️⃣ Thuốc điều trị:",
        "topical": {
            "type": "Thuốc bôi ngoài (An toàn nhất)",
            "examples": ["Gel Diclofenac (Voltaren)", "Capsaicin cream", "Menthol gel"],
            "how": "Bôi trực tiếp lên khớp đau, 3-4 lần/ngày",
            "note": "✅ Ít tác dụng phụ, phù hợp người già"
        },
        "oral": {
            "type": "Thuốc uống giảm đau",
            "mild": {
                "drug": "Paracetamol (Panadol)",
                "dose": "500-1000mg, 3-4 lần/ngày",
                "note": "Dùng đầu tiên, an toàn"
            },
            "moderate": {
                "drug": "NSAIDs (Ibuprofen, Diclofenac, Meloxicam)",
                "dose": "Theo chỉ định bác sĩ",
                "note": "⚠️ Uống SAU ăn, tránh dạ dày. Không dùng lâu dài"
            }
        },
        "injections": {
            "type": "Tiêm khớp",
            "corticosteroid": {
                "what": "Tiêm Corticoid vào khớp",
                "when": "Đau nhiều, sưng rõ",
                "duration": "Hiệu quả 1-3 tháng",
                "note": "Chỉ 2-3 lần/năm, không lạm dụng"
            },
            "hyaluronic_acid": {
                "what": "Tiêm Acid Hyaluronic (bổ sung dịch khớp)",
                "when": "Gối khô, kêu răng rắc",
                "duration": "3-5 mũi, mỗi tuần 1 mũi",
                "note": "Đắt (500,000-2,000,000đ/mũi), hiệu quả 6-12 tháng"
            }
        },
        "supplements": {
            "type": "Thực phẩm chức năng",
            "glucosamine": {
                "what": "Glucosamine + Chondroitin",
                "effect": "Chưa chắc chắn, một số nghiên cứu cho thấy giảm đau nhẹ",
                "cost": "200,000-500,000đ/tháng",
                "note": "Có thể thử, không hại nhưng hiệu quả không rõ ràng"
            }
        }
    },
    
    "surgery": {
        "title": "3️⃣ Phẫu thuật (Khi thuốc không đỡ):",
        "when": [
            "Đau nặng, không chịu được",
            "Mất chức năng khớp hoàn toàn (không đi được)",
            "Biến dạng khớp nhiều"
        ],
        "options": [
            {
                "type": "Nội soi khớp",
                "what": "Làm sạch khớp, sửa sụn",
                "when": "Giai đoạn sớm, sụn còn"
            },
            {
                "type": "Thay khớp",
                "what": "Thay khớp gối/háng nhân tạo",
                "when": "Giai đoạn muộn, khớp hỏng hoàn toàn",
                "note": "Tuổi thọ khớp nhân tạo: 15-20 năm"
            }
        ]
    }
}

# Quản lý
OSTEOARTHRITIS_MANAGEMENT = {
    "title": "📋 Quản Lý Hàng Ngày",
    
    "daily_tips": [
        "✅ Vận động nhẹ mỗi ngày (đi bộ 20-30 phút)",
        "✅ Nghỉ ngơi khi đau nhiều, không gắng sức",
        "✅ Giữ cân nặng hợp lý",
        "✅ Dùng gậy chống nếu cần (không xấu hổ!)",
        "❌ Tránh ngồi xổm, quỳ gối",
        "❌ Tránh mang vác nặng",
        "❌ Tránh leo cầu thang quá nhiều"
    ],
    
    "exercises": {
        "knee": [
            "Ngồi thẳng, duỗi chân lên cao (giữ 10 giây)",
            "Nằm, gập duỗi gối nhẹ nhàng",
            "Đạp xe tại chỗ (không tải trọng)"
        ],
        "hip": [
            "Đứng, đưa chân sang ngang",
            "Nằm, nâng chân lên cao",
            "Đi bộ trên mặt phẳng"
        ],
        "fingers": [
            "Nắm, mở bàn tay",
            "Uốn từng ngón tay",
            "Xoa bóp nhẹ khớp"
        ]
    },
    
    "nutrition": {
        "good_foods": [
            "Cá béo (cá hồi, cá thu) - Omega-3 chống viêm",
            "Rau xanh (bông cải, cải bó xôi) - Vitamin K",
            "Trái cây (cam, dâu) - Vitamin C",
            "Sữa, sữa chua - Canxi",
            "Gừng, nghệ - Chống viêm tự nhiên"
        ],
        "avoid_foods": [
            "Thức ăn nhiều đường → Tăng viêm",
            "Thức ăn chiên rán → Tăng viêm",
            "Rượu bia → Làm nặng đau"
        ]
    }
}

