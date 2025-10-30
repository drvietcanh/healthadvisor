"""
COPD - Bệnh Phổi Tắc Nghẽn Mạn Tính
====================================

Thông tin cơ bản về COPD (Chronic Obstructive Pulmonary Disease)
"""

from typing import Dict, List

COPD_INFO = {
    "name": "Bệnh Phổi Tắc Nghẽn Mạn Tính",
    "name_en": "COPD (Chronic Obstructive Pulmonary Disease)",
    
    "simple_explanation": """
💡 COPD là gì? (Giải thích đơn giản)

Tưởng tượng phổi như bóng cao su:
- Phổi BÌNH THƯỜNG: Bóng mềm, căng phồng dễ dàng
- Phổi COPD: Bóng cứng, mất đàn hồi, khó căng phồng

🫁 Chuyện gì xảy ra:
1. Đường thở BỊ HẸP (viêm, phù nề)
2. Túi khí (phế nang) BỊ PHÁ HỦY → mất đàn hồi
3. Khó thở ra → Khí cũ mắc kẹt trong phổi
4. → Khó hít khí mới vào → THIẾU OXY

⚠️ ĐẶC ĐIỂM:
- Bệnh MẠN TÍNH, TIẾN TRIỂN
- KHÔNG THỂ HỒI PHỤC hoàn toàn
- NHƯNG có thể KIỂM SOÁT, làm chậm tiến triển
    """,
    
    "definition": """
COPD là nhóm bệnh phổi tiến triển, gây hạn chế luồng khí thở ra,
bao gồm:
- Viêm phế quản mạn tính (Chronic Bronchitis)
- Khí phế thũng (Emphysema)
    """,
    
    "statistics_vietnam": {
        "prevalence": "4-6% dân số trưởng thành",
        "age_group": "Chủ yếu >40 tuổi",
        "mortality": "Nguyên nhân tử vong thứ 4 tại VN",
        "risk": "90% liên quan đến HÚT THUỐC LÁ",
        "diagnosis": "Chỉ 25% được chẩn đoán đúng"
    },
    
    "types": {
        "chronic_bronchitis": {
            "name": "Viêm Phế Quản Mạn Tính",
            "features": [
                "Ho có đờm ≥3 tháng/năm, ≥2 năm liên tiếp",
                "Đường thở viêm, sưng",
                "Tiết nhiều đờm",
                "Ho nhiều, đặc biệt buổi sáng"
            ],
            "nickname": "Blue bloater (người phù xanh)"
        },
        "emphysema": {
            "name": "Khí Phế Thũng",
            "features": [
                "Túi khí (phế nang) bị phá hủy",
                "Phổi mất đàn hồi",
                "Khó thở nặng",
                "Ít ho, ít đờm"
            ],
            "nickname": "Pink puffer (người thở hổn hển)"
        }
    }
}

# Nguyên nhân
CAUSES = {
    "primary": {
        "name": "🚬 HÚT THUỐC LÁ (Nguyên nhân #1)",
        "percentage": "85-90% ca bệnh",
        "mechanism": [
            "Khói thuốc → Viêm phổi mạn tính",
            "Phá hủy phế nang (túi khí)",
            "Giảm chức năng lông mao",
            "Tăng tiết đờm"
        ],
        "risk": [
            "Hút 1 bao/ngày: Tăng nguy cơ gấp 20 lần",
            "Hút thụ động: Tăng nguy cơ 20-30%",
            "Càng hút lâu → càng nặng"
        ],
        "note": "⚠️ BỎ THUỐC LÁ = Điều trị QUAN TRỌNG NHẤT!"
    },
    
    "environmental": {
        "name": "🏭 Ô Nhiễm Môi Trường",
        "factors": [
            "Khói bụi nhà máy",
            "Khói đốt rơm rạ",
            "Khói bếp than, củi (phụ nữ nông thôn)",
            "Bụi nghề nghiệp (than, xi măng, hóa chất)"
        ],
        "vietnam_specific": [
            "Nấu ăn bằng than, củi không thông gió",
            "Ô nhiễm không khí đô thị (Hà Nội, HCM)",
            "Đốt rơm rạ mùa gặt"
        ]
    },
    
    "genetic": {
        "name": "🧬 Yếu Tố Di Truyền",
        "condition": "Thiếu Alpha-1 Antitrypsin (AAT)",
        "prevalence": "Hiếm (<1%), chủ yếu người da trắng",
        "feature": "COPD xuất hiện sớm (<45 tuổi)"
    },
    
    "other": {
        "name": "Khác",
        "factors": [
            "Nhiễm trùng hô hấp tái đi tái lại thời thơ ấu",
            "Hen suyễn không kiểm soát",
            "Suy dinh dưỡng",
            "Tuổi cao"
        ]
    }
}

# Triệu chứng
SYMPTOMS = {
    "main_symptoms": {
        "title": "🔍 3 Triệu Chứng Chính",
        "symptoms": [
            {
                "name": "Khó thở",
                "icon": "🫁",
                "details": [
                    "Ban đầu: Khó thở KHI GẮN SỨC (đi bộ, leo cầu thang)",
                    "Tiến triển: Khó thở ngay cả KHI NGHỈ",
                    "Đặc điểm: Khó THỞ RA, phải rặn mới thở ra được",
                    "Tư thế: Ngồi cúi người, tựa tay để thở"
                ],
                "progression": "Tiến triển CHẬM, nhiều năm"
            },
            {
                "name": "Ho mạn tính",
                "icon": "😷",
                "details": [
                    "Ho ≥3 tháng/năm, ≥2 năm",
                    "Ho nhiều nhất buổi SÁNG",
                    "Ho có đờm",
                    "Đờm trắng/vàng/xanh"
                ],
                "note": "Nhiều người nghĩ 'ho hút thuốc bình thường' → BỎ LỠ chẩn đoán!"
            },
            {
                "name": "Đờm nhiều",
                "icon": "💧",
                "details": [
                    "Tiết đờm nhiều, đặc biệt buổi sáng",
                    "Màu trắng trong (bình thường)",
                    "Màu vàng/xanh (nhiễm trùng)",
                    "Khó khạc ra"
                ]
            }
        ]
    },
    
    "early_warning_signs": {
        "title": "⚠️ Dấu Hiệu Sớm (Cần Chú Ý)",
        "signs": [
            "Ho mạn tính >3 tháng (đặc biệt người hút thuốc)",
            "Khó thở khi gắng sức nhẹ (đi bộ nhanh, leo 1 tầng)",
            "Đờm nhiều buổi sáng",
            "Hay bị viêm phế quản, viêm phổi",
            "Thường xuyên thấy mệt"
        ],
        "action": "🏥 NÊN ĐI KHÁM và đo chức năng hô hấp (spirometry)"
    },
    
    "severe_symptoms": {
        "title": "🚨 Triệu Chứng NẶNG (Cần Cấp Cứu)",
        "symptoms": [
            "Khó thở NGHIÊM TRỌNG, không nói được câu hoàn chỉnh",
            "Môi, móng tay TÍM (thiếu oxy)",
            "Lú lẫn, buồn ngủ bất thường",
            "Nhịp tim nhanh >120 lần/phút",
            "Sốt cao + đờm mủ",
            "Ho ra máu"
        ],
        "action": "📞 GỌI CẤP CỨU 115 NGAY!"
    },
    
    "exacerbation_triggers": {
        "title": "🔥 Yếu Tố Khiến Bệnh Nặng Lên (Đợt Cấp)",
        "triggers": [
            "Nhiễm trùng (vi khuẩn, virus) - 70-80% đợt cấp",
            "Ô nhiễm không khí tăng",
            "Thời tiết lạnh, ẩm",
            "Không uống thuốc đúng",
            "Hút thuốc lá tiếp tục",
            "Stress, mệt mỏi"
        ],
        "prevention": [
            "✅ Tiêm vắc-xin cúm hàng năm",
            "✅ Tiêm vắc-xin phế cầu",
            "✅ Uống thuốc đều đặn",
            "✅ Tránh khói bụi, ô nhiễm",
            "✅ Giữ ấm khi trời lạnh"
        ]
    }
}

# Biến chứng
COMPLICATIONS = {
    "respiratory": {
        "name": "Hô Hấp",
        "complications": [
            "Suy hô hấp mạn tính → phải thở oxy",
            "Nhiễm trùng phổi tái đi tái lại",
            "Viêm phổi nặng, áp xe phổi",
            "Tràn khí màng phổi (bóng khí vỡ)"
        ]
    },
    
    "cardiovascular": {
        "name": "Tim Mạch",
        "complications": [
            "Cor pulmonale (tim phổi): Tim phải phì đại, suy tim",
            "Tăng áp phổi",
            "Rối loạn nhịp tim",
            "Tăng nguy cơ nhồi máu cơ tim"
        ],
        "note": "COPD + bệnh tim = Rất nguy hiểm!"
    },
    
    "other": {
        "name": "Khác",
        "complications": [
            "Loãng xương (do corticoid, ít vận động)",
            "Trầm cảm, lo âu (40-70% bệnh nhân)",
            "Suy dinh dưỡng, sụt cân",
            "Yếu cơ",
            "Tăng nguy cơ ung thư phổi (hút thuốc)"
        ]
    }
}

# Chẩn đoán
DIAGNOSIS = {
    "spirometry": {
        "name": "🫁 Đo Chức Năng Hô Hấp (Spirometry) - XÉT NGHIỆM QUYẾT ĐỊNH",
        "description": "Đo lượng và tốc độ khí thở vào/ra",
        "criteria": "FEV1/FVC < 0.7 SAU khi dùng thuốc giãn phế quản",
        "interpretation": {
            "FEV1": "Thể tích khí thở ra mạnh trong 1 giây đầu",
            "FVC": "Tổng thể tích khí thở ra tối đa",
            "ratio": "FEV1/FVC < 0.7 → Tắc nghẽn"
        },
        "note": "⚠️ CẦN LÀM nếu: >40 tuổi + hút thuốc + ho/khó thở mạn tính"
    },
    
    "imaging": {
        "name": "📷 Chụp X-quang/CT Phổi",
        "findings": [
            "Phổi căng phồng quá mức",
            "Hoành cơ dẹt (bình thường là vòm)",
            "Phế nang bị phá hủy (khí phế thũng)",
            "Thành phế quản dày"
        ],
        "note": "Không dùng để chẩn đoán chính, nhưng loại trừ bệnh khác"
    },
    
    "other_tests": {
        "name": "Xét Nghiệm Khác",
        "tests": [
            "Khí máu động mạch: Đo mức oxy, CO2",
            "Đo SpO2: Nồng độ oxy máu (bình thường >95%)",
            "Xét nghiệm Alpha-1 Antitrypsin (nếu <45 tuổi)",
            "Công thức máu: Phát hiện nhiễm trùng",
            "ECG, siêu âm tim: Đánh giá tim phổi"
        ]
    }
}

# Phòng ngừa
PREVENTION = {
    "primary": {
        "name": "Phòng Ngừa Sơ Cấp (Chưa Bệnh)",
        "actions": [
            "🚫 KHÔNG HÚT THUỐC LÁ - Quan trọng nhất!",
            "🚫 Tránh khói thuốc thụ động",
            "😷 Đeo khẩu trang khi ô nhiễm cao",
            "🏠 Thông gió tốt khi nấu ăn (dùng quạt hút mùi)",
            "👷 Bảo hộ lao động (nếu tiếp xúc bụi, hóa chất)",
            "💉 Tiêm vắc-xin cúm, phế cầu (người >65 tuổi)"
        ]
    },
    
    "secondary": {
        "name": "Phòng Ngừa Thứ Cấp (Đã Bệnh → Ngăn Nặng)",
        "actions": [
            "✅ BỎ THUỐC LÁ ngay lập tức",
            "💊 Uống thuốc đều đặn",
            "🏃 Tập phục hồi chức năng phổi",
            "💉 Tiêm vắc-xin đầy đủ",
            "🏥 Tái khám định kỳ",
            "⚠️ Nhận biết sớm đợt cấp"
        ]
    }
}

# Phân biệt COPD vs Hen Suyễn
COPD_VS_ASTHMA = {
    "title": "🔍 PHÂN BIỆT COPD VÀ HEN SUYỄN - Dễ Nhầm Lẫn!",
    "introduction": """
Cả 2 bệnh đều khó thở, thở khò khè → Rất dễ nhầm!
NHƯNG: Khác nhau về nguyên nhân, tuổi mắc, điều trị, tiên lượng
    """,
    
    "comparison_table": {
        "age_onset": {
            "feature": "Tuổi khởi phát",
            "copd": "🧓 >40 tuổi (thường >50 tuổi)",
            "asthma": "👶 Thường <20 tuổi (trẻ em, thanh thiếu niên)",
            "key_point": "Hen = bệnh TRẺ, COPD = bệnh GIÀ"
        },
        
        "cause": {
            "feature": "Nguyên nhân",
            "copd": "🚬 Hút thuốc lá (85-90%)",
            "asthma": "🤧 Dị ứng (phấn hoa, bụi, lông thú...)",
            "key_point": "COPD do THUỐC LÁ, Hen do DỊ ỨNG"
        },
        
        "symptom_pattern": {
            "feature": "Triệu chứng",
            "copd": "⏱️ Tiến triển CHẬM, MÃI MÃI có (hàng ngày)",
            "asthma": "⚡ ĐỢT KỊCH PHÁT (có lúc khỏe, có lúc khó thở)",
            "key_point": "COPD = Khó thở MÃI, Hen = Khó thở CƠN"
        },
        
        "time_of_symptoms": {
            "feature": "Thời gian nặng",
            "copd": "🌅 Buổi sáng thường nặng hơn (ho, đờm nhiều)",
            "asthma": "🌙 Ban đêm/sáng sớm thường nặng hơn",
            "key_point": "Cả 2 đều nặng buổi sáng, nhưng hen nặng cả đêm"
        },
        
        "triggers": {
            "feature": "Yếu tố kích thích",
            "copd": "Nhiễm trùng, ô nhiễm, thời tiết lạnh",
            "asthma": "Dị nguyên (phấn, lông, thuốc, thức ăn), gắng sức, khí lạnh, cảm xúc",
            "key_point": "Hen có NHIỀU yếu tố kích phát hơn"
        },
        
        "reversibility": {
            "feature": "Hồi phục",
            "copd": "❌ KHÔNG thể hồi phục hoàn toàn (tổn thương vĩnh viễn)",
            "asthma": "✅ CÓ THỂ hồi phục hoàn toàn (nếu điều trị tốt)",
            "key_point": "⭐ KHÁC BIỆT QUAN TRỌNG NHẤT!"
        },
        
        "bronchodilator_response": {
            "feature": "Đáp ứng thuốc giãn phế quản",
            "copd": "Cải thiện ÍT (<12% FEV1)",
            "asthma": "Cải thiện NHIỀU (≥12% FEV1)",
            "key_point": "Dùng xịt hen → Hen đỡ nhanh, COPD đỡ chậm"
        },
        
        "family_history": {
            "feature": "Tiền sử gia đình",
            "copd": "❌ Thường KHÔNG (trừ thiếu AAT hiếm)",
            "asthma": "✅ Thường CÓ (di truyền)",
            "key_point": "Bố mẹ hen → Con dễ hen, KHÔNG dễ COPD"
        },
        
        "allergy_history": {
            "feature": "Tiền sử dị ứng",
            "copd": "❌ Thường không",
            "asthma": "✅ Thường có (viêm mũi dị ứng, chàm...)",
            "key_point": "Hen thường đi kèm các bệnh dị ứng khác"
        },
        
        "sputum": {
            "feature": "Đờm",
            "copd": "💧 Nhiều đờm (trắng/vàng/xanh), hàng ngày",
            "asthma": "💧 Ít đờm (hoặc đờm nhầy trong)",
            "key_point": "COPD = Đờm nhiều, Hen = Đờm ít"
        },
        
        "smoking": {
            "feature": "Hút thuốc lá",
            "copd": "🚬 Hầu hết có tiền sử hút thuốc",
            "asthma": "🚭 Đa số KHÔNG hút thuốc",
            "key_point": "COPD gần như LUÔN có hút thuốc"
        },
        
        "prognosis": {
            "feature": "Tiên lượng",
            "copd": "⚠️ Tiến triển nặng dần, giảm tuổi thọ",
            "asthma": "✅ Kiểm soát tốt → Sống bình thường",
            "key_point": "Hen kiểm soát được, COPD chỉ làm chậm"
        }
    },
    
    "simple_comparison": {
        "title": "📊 So Sánh Đơn Giản",
        "copd_summary": {
            "icon": "🧓🚬",
            "profile": "Ông già hút thuốc 30 năm",
            "typical": [
                "65 tuổi, hút thuốc 30 năm",
                "Ho, đờm nhiều MỖI SÁNG",
                "Khó thở khi đi bộ, leo cầu thang",
                "Triệu chứng MÃI MÃI có, không biến mất",
                "Xịt thuốc → Đỡ một chút nhưng không hết",
                "Càng ngày càng nặng, không thể hồi phục"
            ]
        },
        
        "asthma_summary": {
            "icon": "👦🤧",
            "profile": "Cậu bé dị ứng",
            "typical": [
                "15 tuổi, không hút thuốc",
                "Có lúc KHỎE HOÀN TOÀN, có lúc khó thở",
                "Khó thở KHI: Gặp mèo, hít phấn hoa, chạy",
                "Ban đêm/sáng sớm thở khò khè",
                "Xịt thuốc hen → Đỡ NGAY",
                "Điều trị tốt → Có thể sống bình thường"
            ]
        }
    },
    
    "confusion_cases": {
        "title": "❓ Trường Hợp Dễ Nhầm",
        "cases": [
            {
                "scenario": "👴 Người già có HEN từ nhỏ + Hút thuốc",
                "answer": "→ Có thể CÓ CẢ HEN VÀ COPD (15-20% trường hợp)",
                "note": "Gọi là ACOS (Asthma-COPD Overlap Syndrome)"
            },
            {
                "scenario": "🧑 Người trẻ <40 tuổi khó thở, hút thuốc",
                "answer": "→ Có thể là HEN NẶNG hoặc COPD hiếm (thiếu AAT)",
                "note": "Cần làm xét nghiệm đặc biệt"
            },
            {
                "scenario": "👵 Bà già ho lâu, không hút thuốc",
                "answer": "→ Có thể là COPD do khói bếp, không chỉ thuốc lá!",
                "note": "Phụ nữ nấu bếp than/củi nhiều năm"
            }
        ]
    },
    
    "when_to_suspect": {
        "suspect_copd": {
            "title": "🤔 Nghĩ Đến COPD Khi:",
            "criteria": [
                "Tuổi >40",
                "Hút thuốc (hoặc hút thuốc lá trước đây)",
                "Ho, đờm MẠN TÍNH (>3 tháng)",
                "Khó thở TIẾN TRIỂN CHẬM (nhiều năm)",
                "Triệu chứng HÀNG NGÀY, không biến mất"
            ]
        },
        
        "suspect_asthma": {
            "title": "🤔 Nghĩ Đến HEN Khi:",
            "criteria": [
                "Tuổi trẻ (<40, đặc biệt trẻ em)",
                "Tiền sử dị ứng (mũi, da, thức ăn...)",
                "Khó thở KỊCH PHÁT, có lúc khỏe hẳn",
                "Thở khò khè, đặc biệt ban đêm",
                "Đáp ứng TỐT với thuốc xịt hen"
            ]
        }
    },
    
    "diagnostic_difference": {
        "title": "🔬 Chẩn Đoán Phân Biệt",
        "spirometry": {
            "test": "Đo chức năng hô hấp (Spirometry)",
            "copd": "FEV1/FVC <0.7, đáp ứng ÍT với giãn phế quản (<12%)",
            "asthma": "FEV1/FVC có thể <0.7, đáp ứng TỐT với giãn phế quản (≥12%)",
            "key": "⭐ Xét nghiệm QUYẾT ĐỊNH để phân biệt!"
        }
    },
    
    "treatment_difference": {
        "title": "💊 Điều Trị Khác Nhau",
        "copd": [
            "Mục tiêu: LÀM CHẬM tiến triển, giảm triệu chứng",
            "Thuốc chính: Giãn phế quản dài hạn",
            "Corticoid: Chỉ dùng khi nặng",
            "Quan trọng nhất: BỎ THUỐC LÁ + Phục hồi chức năng"
        ],
        "asthma": [
            "Mục tiêu: KIỂM SOÁT hoàn toàn, không triệu chứng",
            "Thuốc chính: Corticoid hít (ICS) hàng ngày",
            "Thuốc cấp cứu: Xịt giãn phế quản ngắn hạn",
            "Quan trọng nhất: TRÁNH DỊ NGUYÊN + Dùng thuốc đều"
        ]
    },
    
    "key_message": {
        "title": "🎯 Điểm Quan Trọng Nhất",
        "message": """
HEN vs COPD - Nhớ 3 điểm:

1️⃣ TUỔI: Hen = TRẺ, COPD = GIÀ
2️⃣ NGUYÊN NHÂN: Hen = DỊ ỨNG, COPD = THUỐC LÁ  
3️⃣ HỒI PHỤC: Hen = ĐƯỢC, COPD = KHÔNG

⚠️ Nếu không chắc → ĐI KHÁM, làm đo chức năng hô hấp!
        """
    }
}

# Liên quan đến bệnh khác
RELATED_DISEASES = {
    "common_comorbidities": [
        {
            "disease": "Bệnh Tim Mạch",
            "prevalence": "20-30% bệnh nhân COPD",
            "note": "Cùng nguyên nhân: Hút thuốc, viêm"
        },
        {
            "disease": "Cao Huyết Áp",
            "prevalence": "30-50%",
            "note": "Thiếu oxy mạn tính → tăng huyết áp phổi"
        },
        {
            "disease": "Tiểu Đường Type 2",
            "prevalence": "10-20%",
            "note": "Corticoid → tăng đường huyết"
        },
        {
            "disease": "Loãng Xương",
            "prevalence": "35-70%",
            "note": "Ít vận động + corticoid + thiếu oxy"
        },
        {
            "disease": "Ung Thư Phổi",
            "risk": "Tăng 2-5 lần",
            "note": "Cùng yếu tố nguy cơ: Hút thuốc"
        }
    ]
}

