"""
Gout - Bệnh Gút
Bệnh do tăng acid uric máu, gây viêm khớp đau dữ dội
"""

GOUT_INFO = {
    "title": "🦶 Bệnh Gút (Gout)",
    "simple_explanation": """
💡 Bệnh Gút là gì?

Giống như đường tan trong nước, acid uric trong máu cũng vậy.
- Khi acid uric QUÁ NHIỀU → Kết tinh thành tinh thể sắc nhọn
- Tinh thể này lắng đọng ở khớp → Đâm vào mô → ĐAU DỮ DỘI như bị dao đâm!
- Thường ở: Ngón chân cái (80%), gối, cổ chân, khuỷu tay

🕐 Ai dễ bị?
- Nam giới >40 tuổi (nữ ít hơn, thường sau mãn kinh)
- Uống nhiều rượu bia
- Ăn nhiều thịt đỏ, hải sản, nội tạng
- Thừa cân, béo phì
- Gia đình có người bị
- Dùng thuốc lợi tiểu (cho huyết áp cao)
- Bệnh thận
    """,
    
    "hyperuricemia": {
        "title": "⚠️ Tăng Acid Uric Máu (Chưa Phải Gút)",
        "explanation": """
💡 Acid uric cao nhưng CHƯA CÓ CƠN ĐAU:

🔍 Phân biệt:
- **Tăng acid uric máu:** Acid uric cao nhưng chưa có triệu chứng
- **Bệnh Gút:** Acid uric cao + CÓ CƠN ĐAU KHỚP

📊 Mức acid uric:
- Bình thường: Nam < 7 mg/dL (< 420 μmol/L), Nữ < 6 mg/dL (< 360 μmol/L)
- Tăng nhẹ: 7-8 mg/dL (420-480 μmol/L, chưa cần thuốc, chỉ thay đổi lối sống)
- Tăng cao: > 8 mg/dL (> 480 μmol/L, nguy cơ gút cao)
- Rất cao: > 9-10 mg/dL (> 540-600 μmol/L, nguy cơ rất cao)

⚠️ LƯU Ý QUAN TRỌNG:
- Chỉ 10-20% người acid uric cao → BỊ GÚT
- Nhiều người acid uric cao nhưng KHÔNG BAO GIỜ bị gút!
- → Không cần uống thuốc ngay khi chỉ tăng nhẹ!
        """,
        
        "when_to_treat": {
            "no_medication": {
                "title": "KHÔNG cần thuốc (Chỉ thay đổi lối sống):",
                "conditions": [
                    "Acid uric 7-8 mg/dL (420-480 μmol/L)",
                    "Chưa có cơn gút",
                    "Không có sỏi thận",
                    "Không có bệnh tim mạch, tiểu đường"
                ],
                "actions": [
                    "Giảm cân (nếu thừa cân)",
                    "Uống nhiều nước (2-3 lít/ngày)",
                    "Hạn chế rượu bia",
                    "Giảm thịt đỏ, hải sản",
                    "Tập thể dục",
                    "Xét nghiệm lại sau 6 tháng"
                ]
            },
            
            "consider_medication": {
                "title": "Cân nhắc thuốc:",
                "conditions": [
                    "Acid uric > 8-9 mg/dL (> 480-540 μmol/L)",
                    "Đã có >1 cơn gút",
                    "Có sỏi thận do acid uric",
                    "Có bệnh tim mạch, tiểu đường + acid uric cao"
                ],
                "note": "Cần tham khảo bác sĩ, không tự ý uống thuốc"
            }
        },
        
        "monitoring": [
            "Xét nghiệm acid uric 1-2 lần/năm",
            "Theo dõi triệu chứng (có cơn đau khớp không?)",
            "Kiểm tra chức năng thận",
            "Kiểm tra huyết áp, đường huyết"
        ]
    },
    
    "stages": {
        "asymptomatic": {
            "name": "Giai đoạn im lặng",
            "description": "Acid uric cao nhưng chưa có triệu chứng",
            "duration": "Có thể nhiều năm"
        },
        "acute": {
            "name": "Gút cấp - Cơn đau dữ dội",
            "description": "Viêm khớp đau như dao đâm, sưng nóng đỏ",
            "duration": "3-10 ngày, tự khỏi nhưng dễ tái phát"
        },
        "chronic": {
            "name": "Gút mạn",
            "description": "Nhiều cơn, tinh thể lắng đọng thành hạt tophi",
            "complications": "Hủy khớp, sỏi thận"
        }
    }
}

GOUT_SYMPTOMS = {
    "title": "🔍 Triệu Chứng Bệnh Gút",
    
    "acute_attack": {
        "title": "Cơn Gút Cấp:",
        "characteristics": [
            "ĐAU DỮ DỘI như dao đâm (thường ban đêm)",
            "Sưng, nóng, đỏ khớp (như bị bỏng)",
            "Đau đến mức không chịu được chăn đắp lên",
            "Khớp sưng to, bóng",
            "Thường 1 khớp (ngón chân cái 80%)"
        ],
        "timeline": [
            "Bắt đầu: Đau đột ngột, dữ dội (thường nửa đêm)",
            "Đỉnh điểm: Sưng, đau cực điểm trong 24-48 giờ",
            "Giảm dần: Tự khỏi sau 3-10 ngày (nhưng không chữa → tái phát!)"
        ]
    },
    
    "chronic": {
        "title": "Gút mạn:",
        "symptoms": [
            "Nhiều cơn đau tái phát",
            "Nhiều khớp bị cùng lúc",
            "Hạt tophi (cục u dưới da chứa tinh thể acid uric)",
            "Biến dạng khớp",
            "Sỏi thận (đau thắt lưng, tiểu máu)"
        ]
    },
    
    "red_flags": [
        "🚨 Đau dữ dội, sưng nóng đỏ 1 khớp",
        "🚨 Ngón chân cái đau như dao đâm",
        "🚨 Không chịu được chạm nhẹ vào khớp",
        "→ Có thể là cơn GÚT CẤP! Đi khám ngay!"
    ]
}

GOUT_CAUSES = {
    "title": "🔍 Nguyên Nhân Bệnh Gút",
    
    "mechanism": """
Cơ thể tạo ra acid uric từ:
- Purine trong thức ăn (thịt, hải sản)
- Phá vỡ tế bào cơ thể

Thận thải acid uric qua nước tiểu.

Bệnh Gút xảy ra khi:
- Cơ thể tạo QUÁ NHIỀU acid uric (ăn nhiều thịt, rượu)
- HOẶC thận thải QUÁ ÍT (bệnh thận, thuốc lợi tiểu)
→ Acid uric tăng → Kết tinh → Đau!
    """,
    
    "risk_factors": {
        "diet": {
            "title": "Thức ăn (Quan trọng!):",
            "high_purine": [
                "Thịt đỏ (bò, heo, cừu)",
                "Hải sản (tôm, cua, cá mòi, cá cơm)",
                "Nội tạng (gan, thận, tim)",
                "Thịt hun khói",
                "Nước dùng thịt đậm đặc"
            ],
            "alcohol": [
                "Rượu bia (đặc biệt bia!)",
                "Rượu mạnh",
                "→ Ngăn thận thải acid uric"
            ]
        },
        
        "medical": {
            "title": "Bệnh lý:",
            "conditions": [
                "Thừa cân, béo phì",
                "Bệnh thận",
                "Huyết áp cao",
                "Tiểu đường",
                "Tim mạch"
            ],
            "medications": [
                "Thuốc lợi tiểu (cho huyết áp cao)",
                "Aspirin liều thấp",
                "Thuốc ức chế miễn dịch"
            ]
        },
        
        "genetics": {
            "title": "Di truyền:",
            "note": "Gia đình có người bị → Tăng nguy cơ"
        }
    }
}

GOUT_DIET = {
    "title": "🍽️ Chế Độ Ăn Cho Người Bị Gút",
    
    "avoid": {
        "title": "❌ TRÁNH (Acid uric cao):",
        "foods": [
            {
                "category": "Nội tạng",
                "examples": "Gan, thận, tim, lòng",
                "purine_level": "Rất cao",
                "note": "TRÁNH TUYỆT ĐỐI"
            },
            {
                "category": "Hải sản",
                "examples": "Tôm, cua, cá mòi, cá cơm, cá trích",
                "purine_level": "Cao",
                "note": "Hạn chế tối đa"
            },
            {
                "category": "Thịt đỏ",
                "examples": "Thịt bò, heo, cừu",
                "purine_level": "Trung bình-Cao",
                "note": "Hạn chế, <150g/ngày"
            },
            {
                "category": "Rượu bia",
                "examples": "Tất cả các loại",
                "purine_level": "Ngăn thải acid uric",
                "note": "TRÁNH, đặc biệt bia!"
            },
            {
                "category": "Nước ngọt có đường",
                "examples": "Coca, Pepsi, nước ngọt",
                "why": "Fructose → Tăng acid uric",
                "note": "Tránh"
            }
        ]
    },
    
    "limit": {
        "title": "⚠️ HẠN CHẾ:",
        "foods": [
            {
                "food": "Thịt gia cầm (gà, vịt)",
                "amount": "<150g/ngày",
                "note": "Tốt hơn thịt đỏ"
            },
            {
                "food": "Cá nước ngọt",
                "amount": "<100g/ngày",
                "note": "Tránh cá mòi, cá cơm"
            },
            {
                "food": "Đậu phụ, đậu hũ",
                "amount": "Vừa phải",
                "note": "Purine thấp, ăn được"
            }
        ]
    },
    
    "recommended": {
        "title": "✅ NÊN ĂN:",
        "foods": [
            {
                "food": "Rau xanh",
                "examples": "Tất cả các loại",
                "why": "Purine thấp, tốt cho sức khỏe",
                "note": "Ăn nhiều"
            },
            {
                "food": "Trái cây",
                "examples": "Tất cả (tránh quá ngọt)",
                "why": "Vitamin C giúp giảm acid uric",
                "note": "Đặc biệt cam, dâu"
            },
            {
                "food": "Sữa ít béo",
                "why": "Giảm acid uric",
                "note": "1-2 ly/ngày"
            },
            {
                "food": "Cà phê",
                "why": "Giảm nguy cơ gút (nghiên cứu)",
                "note": "1-2 ly/ngày, không đường"
            },
            {
                "food": "Anh đào (cherry)",
                "why": "Giảm acid uric, giảm cơn gút",
                "note": "Có thể ăn hàng ngày"
            }
        ]
    },
    
    "drinking": {
        "title": "💧 Uống nước:",
        "importance": "Uống nhiều nước → Thải acid uric",
        "amount": "2-3 lít/ngày",
        "what": "Nước lọc, nước khoáng, trà xanh",
        "avoid": "Rượu bia, nước ngọt"
    },
    
    "during_attack": {
        "title": "Khi đang có cơn gút:",
        "diet": [
            "Chỉ ăn cháo, súp nhẹ",
            "Uống nhiều nước (3-4 lít/ngày)",
            "TRÁNH tất cả thịt, hải sản",
            "TRÁNH rượu bia tuyệt đối"
        ]
    }
}

