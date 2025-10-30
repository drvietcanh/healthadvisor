"""
Asthma (Hen Suyễn) - Thông tin cơ bản
=====================================

Ngôn ngữ bình dân, dễ hiểu cho người dân
"""

from typing import Dict, List

ASTHMA_INFO = {
    "name": "Hen Suyễn",
    "name_en": "Asthma",
    
    "simple_explanation": """
💡 **Hen suyễn là gì?** (Giải thích đơn giản)

Tưởng tượng đường thở như **ống hơi**:
- **Bình thường**: Ống rộng, thở thoải mái
- **KHI HEN**: Ống bị co lại, sưng lên, đầy đờm → Thở KHÒ KHÈ, khó thở

🔄 Đặc điểm QUAN TRỌNG:
- Có lúc KHỎE HẲN (ống rộng trở lại)
- Có lúc KHÓ THỞ (ống bị co)
- → Khó thở ĐỢT, KHÔNG MÃI MÃI như COPD

⭐ Tin vui: **CÓ THỂ KIỂM SOÁT HOÀN TOÀN!**
- Dùng thuốc đúng → Sống bình thường
- Không dùng thuốc → Nguy hiểm
    """,
    
    "what_happens": {
        "title": "🫁 Chuyện Gì Xảy Ra Khi Hen?",
        "mechanisms": [
            {
                "step": "1. Đường thở VIÊM, NHẠY CẢM",
                "analogy": "Giống như da bị dị ứng, sưng đỏ",
                "result": "Dễ bị kích thích"
            },
            {
                "step": "2. Gặp DỊ NGUYÊN (phấn, bụi, khói...)",
                "analogy": "Như châm diêm vào xăng",
                "result": "Phản ứng dữ dội"
            },
            {
                "step": "3. CƠ đường thở CO THẮT",
                "analogy": "Ống hơi bị bóp chặt",
                "result": "Đường thở HẸP"
            },
            {
                "step": "4. Niêm mạc SƯNG PHÙ",
                "analogy": "Thành ống dày lên",
                "result": "Đường thở càng HẸP hơn"
            },
            {
                "step": "5. Tiết NHIỀU ĐỜM NHẦY",
                "analogy": "Ống bị tắc đờm",
                "result": "Khí KHÔNG qua được"
            }
        ],
        "final_result": "→ KHÓ THỞ, THỞ KHÒ KHÈ, HO"
    },
    
    "statistics_vietnam": {
        "prevalence": "5-10% dân số (1/10 người)",
        "children": "Phổ biến ở trẻ em (10-15%)",
        "adults": "Người lớn 5-7%",
        "trend": "Đang TĂNG (đô thị hóa, ô nhiễm)",
        "control": "Chỉ 30% được kiểm soát tốt (70% dùng thuốc SAI hoặc không đều!)"
    }
}

# Nguyên nhân
CAUSES = {
    "genetic": {
        "name": "🧬 Di Truyền",
        "explanation": "Bố mẹ hen → Con dễ hen (40-60%)",
        "reality": "Nếu CẢ BỐ LẪN MẸ hen → Con hen 60-70%",
        "note": "Di truyền KHUYNH HƯỚNG, không phải chắc chắn 100%"
    },
    
    "allergies": {
        "name": "🤧 Dị Ứng - Nguyên Nhân #1",
        "common_allergens": [
            {
                "type": "Bụi nhà",
                "detail": "Bọ ve bụi (nhỏ li ti, sống trong ga gối, nệm)",
                "note": "PHẢI THƯỜNG XUYÊN!"
            },
            {
                "type": "Phấn hoa",
                "detail": "Mùa xuân, gần cây cỏ",
                "season": "Tháng 2-4"
            },
            {
                "type": "Lông thú",
                "detail": "Chó, mèo, chim",
                "note": "Lông VÀ nước bọt, nước tiểu"
            },
            {
                "type": "Nấm mốc",
                "detail": "Tường ẩm, nhà tắm, tủ quần áo",
                "note": "Nhà ẩm ướt rất dễ"
            },
            {
                "type": "Gián, chuột",
                "detail": "Phân, xác, lông",
                "note": "Thường thấy ở nhà cũ"
            }
        ]
    },
    
    "environmental": {
        "name": "🏭 Môi Trường",
        "factors": [
            "Khói thuốc lá (chủ động + thụ động)",
            "Ô nhiễm không khí (khói xe, nhà máy)",
            "Khói bếp (than, củi, dầu)",
            "Hóa chất (sơn, nước rửa chén, nước hoa)",
            "Khói hương, nhang (nhiều người không nghĩ tới!)"
        ],
        "vietnam_note": "Hà Nội, TP.HCM ô nhiễm cao → Hen tăng"
    }
}

# Triệu chứng
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

# Các yếu tố kích phát (Triggers)
TRIGGERS = {
    "title": "🔥 Các Yếu Tố KÍCH PHÁT Hen",
    "description": "Biết TRÁNH = Giảm cơn hen 50-70%!",
    
    "allergens": {
        "name": "🤧 Dị Nguyên (Allergens)",
        "items": [
            {
                "trigger": "Bụi nhà (Bọ ve bụi)",
                "where": "Ga gối, nệm, thảm, rèm",
                "how_to_avoid": [
                    "Giặt ga gối 1 tuần/lần (nước nóng >60°C)",
                    "Phơi nệm nắng thường xuyên",
                    "Dùng vỏ gối chống ve bụi",
                    "BỎ thảm, rèm dày (nếu được)",
                    "Lau nhà ẩm (không quét khô → bụi bay)"
                ]
            },
            {
                "trigger": "Lông chó, mèo",
                "reality": "Lông, nước bọt, nước tiểu",
                "how_to_avoid": [
                    "TỐT NHẤT: Không nuôi",
                    "Nếu nuôi: Không cho vào phòng ngủ",
                    "Tắm thú cưng 1 tuần/lần",
                    "Rửa tay sau khi sờ"
                ]
            },
            {
                "trigger": "Gián, chuột",
                "where": "Nhà cũ, bếp",
                "how_to_avoid": [
                    "Dọn dẹp sạch sẽ",
                    "Không để thức ăn thừa",
                    "Bít kín khe hở"
                ]
            },
            {
                "trigger": "Nấm mốc",
                "where": "Tường ẩm, nhà tắm, tủ quần áo",
                "how_to_avoid": [
                    "Giảm độ ẩm (<50%)",
                    "Thông gió tốt",
                    "Lau sạch nấm mốc (dùng nước tẩy pha loãng)"
                ]
            }
        ]
    },
    
    "irritants": {
        "name": "💨 Chất Kích Thích",
        "items": [
            {
                "trigger": "Khói thuốc lá",
                "danger": "CỰC KỲ NGUY HIỂM!",
                "effects": [
                    "Làm hen NẶNG hơn",
                    "Thuốc KÉMHIỆU QUẢ hơn",
                    "Trẻ hít khói thuốc → Dễ hen gấp 2-3 lần"
                ],
                "action": "🚫 BỎ THUỐC + TRÁNH khói thuốc thụ động!"
            },
            {
                "trigger": "Ô nhiễm không khí",
                "sources": "Khói xe, bụi, khói nhà máy",
                "how_to_avoid": [
                    "Đeo khẩu trang N95 khi ra đường",
                    "Hạn chế ra ngoài khi AQI >150",
                    "Đóng cửa sổ khi ô nhiễm cao"
                ]
            },
            {
                "trigger": "Mùi nồng",
                "examples": "Nước hoa, xịt phòng, sơn, nước rửa chén",
                "tip": "Chọn sản phẩm KHÔNG MÙI"
            },
            {
                "trigger": "Khói nhang, hương",
                "reality": "Nhiều người KHÔNG biết đây là yếu tố kích hen!",
                "tip": "Thắp ít, thông gió tốt"
            }
        ]
    },
    
    "weather": {
        "name": "🌦️ Thời Tiết",
        "triggers": [
            {
                "condition": "Không khí LẠNH",
                "when": "Mùa đông, sáng sớm, phòng máy lạnh",
                "how_to_avoid": [
                    "Đeo khẩu trang khi ra ngoài trời lạnh",
                    "Hít thở qua mũi (KHÔNG qua miệng)",
                    "Quấn khăn che mũi, miệng"
                ]
            },
            {
                "condition": "Độ ẩm CAO",
                "when": "Mùa mưa, gần biển",
                "problem": "Nấm mốc, ve bụi sinh sôi"
            },
            {
                "condition": "Thay đổi ĐỘT NGỘT",
                "when": "Giao mùa, vào phòng lạnh từ ngoài nóng",
                "tip": "Thích nghi từ từ"
            }
        ]
    },
    
    "infections": {
        "name": "🦠 Nhiễm Trùng",
        "main": "Cảm lạnh, cúm, viêm phế quản",
        "reality": "70-80% cơn hen nặng do NHIỄM TRÙNG đường hô hấp",
        "prevention": [
            "Tiêm vắc-xin cúm HÀNG NĂM",
            "Rửa tay thường xuyên",
            "Tránh người ốm",
            "Tăng cường miễn dịch"
        ]
    },
    
    "emotions": {
        "name": "😭 Cảm Xúc",
        "triggers": "Cười to, khóc, giận dữ, stress",
        "why": "Thở nhanh, mất kiểm soát nhịp thở → Kích hen",
        "tip": "Học THỞ chậm, kiểm soát cảm xúc"
    },
    
    "foods_drugs": {
        "name": "💊 Thức Ăn & Thuốc",
        "foods": [
            "Đồ uống lạnh đá (shock nhiệt độ)",
            "Thực phẩm dị ứng (tôm, cua, trứng, sữa...)",
            "Chất bảo quản (sulfite trong rượu vang, mứt)"
        ],
        "drugs": [
            "Aspirin (10% người hen dị ứng Aspirin!)",
            "Thuốc chống viêm NSAID (Ibuprofen...)",
            "Thuốc hạ áp (Beta-blocker)"
        ],
        "action": "⚠️ BÁO với bác sĩ NẾU bị hen sau uống thuốc!"
    }
}

# Phân loại mức độ
SEVERITY_CLASSIFICATION = {
    "title": "📊 Phân Loại Mức Độ Hen",
    
    "intermittent": {
        "name": "Hen Nhẹ Không Thường Xuyên",
        "symptoms_frequency": "< 2 ngày/tuần",
        "nighttime": "< 2 đêm/tháng",
        "daily_life": "KHÔNG ảnh hưởng",
        "example": "Chỉ hen khi gặp mèo, còn lại khỏe hẳn",
        "icon": "🟢"
    },
    
    "mild_persistent": {
        "name": "Hen Nhẹ Dai Dẳng",
        "symptoms_frequency": "> 2 ngày/tuần (NHƯNG không mỗi ngày)",
        "nighttime": "3-4 đêm/tháng",
        "daily_life": "Ảnh hưởng CHÚT ÍT",
        "example": "Khó thở vài lần/tuần, đôi khi thức giấc ban đêm",
        "icon": "🟡"
    },
    
    "moderate_persistent": {
        "name": "Hen Trung Bình Dai Dẳng",
        "symptoms_frequency": "MỖI NGÀY có triệu chứng",
        "nighttime": "> 1 đêm/tuần",
        "daily_life": "Ảnh hưởng NHIỀU (giới hạn vận động)",
        "example": "Phải xịt thuốc mỗi ngày, hay thức giấc đêm",
        "icon": "🟠"
    },
    
    "severe_persistent": {
        "name": "Hen Nặng Dai Dẳng",
        "symptoms_frequency": "Triệu chứng SUỐT NGÀY",
        "nighttime": "Hầu như MỖI ĐÊM",
        "daily_life": "Ảnh hưởng NGHIÊM TRỌNG",
        "example": "Khó thở liên tục, thường xuyên nhập viện",
        "icon": "🔴"
    }
}

