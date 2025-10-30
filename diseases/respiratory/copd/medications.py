"""
COPD Medications - Thuốc điều trị COPD
=======================================

Hướng dẫn về các loại thuốc điều trị COPD
"""

from typing import Dict, List

# Nguyên tắc điều trị
TREATMENT_PRINCIPLES = {
    "title": "💊 Nguyên Tắc Điều Trị COPD",
    
    "key_points": [
        "🚫 BỎ THUỐC LÁ - Quan trọng NHẤT, hiệu quả HƠN mọi thuốc!",
        "💊 Thuốc KHÔNG chữa khỏi, chỉ GIẢM triệu chứng + LÀM CHẬM bệnh",
        "⏰ Uống thuốc ĐỀU ĐẶN, ĐÚNG GIỜ (ngay cả khi khỏe)",
        "🏥 Tái khám định kỳ, điều chỉnh thuốc",
        "💉 Tiêm vắc-xin cúm, phế cầu hàng năm"
    ],
    
    "treatment_goals": [
        "Giảm triệu chứng (khó thở, ho, đờm)",
        "Tăng khả năng vận động",
        "Giảm số lần đợt cấp",
        "Cải thiện chất lượng cuộc sống",
        "Giảm tỷ lệ tử vong"
    ]
}

# Thuốc giãn phế quản
BRONCHODILATORS = {
    "title": "🫁 Thuốc Giãn Phế Quản - Nòng Cốt Điều Trị",
    
    "simple_explanation": """
💡 Thuốc giãn phế quản là gì?

Tưởng tượng đường thở như ống nước:
- COPD: Ống bị co thắt, hẹp → Khó thở
- Thuốc giãn phế quản: NỞ RỘNG ống → Thở dễ hơn

2 loại chính:
- NGẮN HẠN: Tác dụng nhanh (5 phút), ngắn (4-6 giờ) → Dùng KHI CẦN
- DÀI HẠN: Tác dụng chậm, kéo dài (12-24 giờ) → Dùng HÀNG NGÀY
    """,
    
    "short_acting": {
        "name": "Thuốc Ngắn Hạn (SABA + SAMA)",
        "use": "Dùng KHI CẦN - khi khó thở",
        
        "saba": {
            "name": "SABA - Beta-2 agonist ngắn hạn",
            "examples_vietnam": [
                {
                    "name": "Salbutamol (Ventolin)",
                    "brand": "Ventolin, Asthalin, Asmacort",
                    "form": "Xịt, dung dịch khí dung",
                    "dose": "2 nhát xịt (100mcg/nhát) khi khó thở",
                    "onset": "5 phút",
                    "duration": "4-6 giờ",
                    "price": "50,000-100,000đ/hộp"
                },
                {
                    "name": "Terbutaline",
                    "brand": "Bricanyl",
                    "form": "Viên uống, xịt",
                    "dose": "0.25-0.5mg, 3 lần/ngày",
                    "price": "30,000-80,000đ"
                }
            ]
        },
        
        "sama": {
            "name": "SAMA - Anticholinergic ngắn hạn",
            "examples_vietnam": [
                {
                    "name": "Ipratropium (Atrovent)",
                    "brand": "Atrovent",
                    "form": "Xịt, dung dịch khí dung",
                    "dose": "2 nhát xịt, 4 lần/ngày",
                    "onset": "15-30 phút",
                    "duration": "6-8 giờ",
                    "price": "150,000-250,000đ/hộp"
                }
            ]
        },
        
        "combination": {
            "name": "Kết Hợp SABA + SAMA",
            "example": "Combivent (Salbutamol + Ipratropium)",
            "benefit": "Hiệu quả GẤP ĐÔI so với dùng riêng",
            "price": "200,000-300,000đ"
        },
        
        "when_to_use": [
            "Khi khó thở đột ngột",
            "Trước khi gắng sức (leo cầu thang, đi bộ xa)",
            "Đợt cấp",
            "Tối đa 4-6 lần/ngày"
        ],
        
        "warning": "⚠️ Nếu cần dùng >4 lần/ngày → Bệnh NẶNG, cần gặp bác sĩ!"
    },
    
    "long_acting": {
        "name": "Thuốc Dài Hạn (LABA + LAMA)",
        "use": "Dùng HÀNG NGÀY - dù khỏe hay ốm",
        
        "laba": {
            "name": "LABA - Beta-2 agonist dài hạn",
            "examples_vietnam": [
                {
                    "name": "Formoterol",
                    "brand": "Foradil, Oxis",
                    "duration": "12 giờ",
                    "dose": "2 lần/ngày (sáng, tối)",
                    "price": "300,000-500,000đ/tháng"
                },
                {
                    "name": "Salmeterol",
                    "brand": "Serevent",
                    "duration": "12 giờ",
                    "dose": "2 lần/ngày",
                    "price": "400,000-600,000đ/tháng"
                },
                {
                    "name": "Indacaterol",
                    "brand": "Onbrez",
                    "duration": "24 giờ",
                    "dose": "1 lần/ngày",
                    "price": "600,000-800,000đ/tháng"
                }
            ]
        },
        
        "lama": {
            "name": "LAMA - Anticholinergic dài hạn",
            "examples_vietnam": [
                {
                    "name": "Tiotropium (Spiriva)",
                    "brand": "Spiriva",
                    "duration": "24 giờ",
                    "dose": "1 lần/ngày (buổi sáng)",
                    "price": "800,000-1,200,000đ/tháng",
                    "note": "Thuốc PHỔ BIẾN NHẤT tại VN"
                },
                {
                    "name": "Glycopyrronium",
                    "brand": "Seebri",
                    "duration": "24 giờ",
                    "dose": "1 lần/ngày",
                    "price": "700,000-1,000,000đ/tháng"
                }
            ]
        },
        
        "combination_laba_lama": {
            "name": "Kết Hợp LABA + LAMA (Tốt Nhất!)",
            "examples": [
                {
                    "name": "Ultibro (Indacaterol + Glycopyrronium)",
                    "dose": "1 lần/ngày",
                    "benefit": "Hiệu quả tốt nhất, giảm đợt cấp 30-40%",
                    "price": "1,200,000-1,500,000đ/tháng"
                },
                {
                    "name": "Anoro (Vilanterol + Umeclidinium)",
                    "dose": "1 lần/ngày",
                    "price": "1,000,000-1,400,000đ/tháng"
                }
            ],
            "indication": "COPD nhóm B, C, D"
        },
        
        "when_to_use": "COPD từ GOLD 2 trở lên, mMRC ≥2, CAT ≥10"
    }
}

# Corticosteroid hít (ICS)
INHALED_CORTICOSTEROIDS = {
    "title": "💨 Corticosteroid Hít (ICS) - Chống Viêm",
    
    "simple_explanation": """
💡 ICS là gì?

Thuốc CHỐNG VIÊM đường thở:
- Giảm sưng, viêm phế quản
- Giảm đờm
- Giảm đợt cấp

⚠️ CHÚ Ý:
- KHÔNG phải thuốc giãn phế quản → KHÔNG đỡ ngay
- Phải dùng ĐỀU ĐẶN, lâu dài mới có hiệu quả
- Chỉ dùng khi COPD NẶNG + hay bị đợt cấp
    """,
    
    "examples_vietnam": [
        {
            "name": "Budesonide",
            "brand": "Pulmicort",
            "dose": "200-400mcg x 2 lần/ngày",
            "price": "300,000-500,000đ/tháng"
        },
        {
            "name": "Fluticasone",
            "brand": "Flixotide",
            "dose": "250-500mcg x 2 lần/ngày",
            "price": "400,000-600,000đ/tháng"
        }
    ],
    
    "triple_therapy": {
        "name": "BỘ BA (ICS + LABA + LAMA) - Mạnh Nhất!",
        "examples": [
            {
                "name": "Trelegy (Fluticasone + Vilanterol + Umeclidinium)",
                "dose": "1 lần/ngày",
                "indication": "COPD rất nặng, đợt cấp thường xuyên",
                "benefit": "Giảm đợt cấp 50%, cải thiện triệu chứng tốt nhất",
                "price": "2,000,000-2,500,000đ/tháng"
            }
        ],
        "when_to_use": [
            "COPD nhóm D (nặng + nhiều đợt cấp)",
            "Eosinophil máu cao (≥300)",
            "Đợt cấp ≥2 lần/năm dù đã dùng LABA+LAMA"
        ]
    },
    
    "side_effects": [
        "Nấm miệng (tưa lưỡi) → Súc miệng sau xịt",
        "Khàn giọng",
        "Ho khi xịt",
        "Viêm phổi (nếu dùng lâu, liều cao)"
    ],
    
    "note": "⚠️ KHÔNG dùng ICS cho COPD nhẹ! Chỉ dùng khi có chỉ định rõ ràng"
}

# Các thuốc khác
OTHER_MEDICATIONS = {
    "mucolytics": {
        "name": "Thuốc Làm Loãng Đờm",
        "examples": [
            {
                "name": "Acetylcysteine (NAC)",
                "brand": "ACC, Fluimucil",
                "dose": "200mg x 3 lần/ngày hoặc 600mg x 1 lần/ngày",
                "benefit": "Làm loãng đờm, dễ khạc ra",
                "price": "50,000-150,000đ/tháng"
            },
            {
                "name": "Carbocysteine",
                "brand": "Mucopect",
                "dose": "750mg x 3 lần/ngày",
                "price": "100,000-200,000đ/tháng"
            }
        ],
        "when_to_use": "Khi có nhiều đờm, khó khạc",
        "evidence": "Bằng chứng YẾU, không khuyến cáo thường quy"
    },
    
    "antibiotics": {
        "name": "Kháng Sinh",
        "use": "CHỈ khi ĐỢT CẤP do nhiễm trùng",
        "signs_of_infection": [
            "Đờm vàng/xanh (mủ)",
            "Sốt",
            "Khó thở tăng đột ngột"
        ],
        "examples": [
            "Amoxicillin/Clavulanate (Augmentin)",
            "Azithromycin (Zithromax)",
            "Levofloxacin"
        ],
        "duration": "5-7 ngày",
        "warning": "⚠️ KHÔNG tự ý dùng kháng sinh! Phải có đơn bác sĩ"
    },
    
    "theophylline": {
        "name": "Theophylline",
        "brand": "Aminophylline, Euphyllin",
        "dose": "200-400mg x 2 lần/ngày",
        "benefit": "Giãn phế quản, giảm mệt cơ hô hấp",
        "use": "Thuốc CŨ, ít dùng nay (nhiều tác dụng phụ)",
        "side_effects": ["Buồn nôn", "Đánh trống ngực", "Mất ngủ"],
        "price": "30,000-80,000đ/tháng"
    },
    
    "pde4_inhibitor": {
        "name": "PDE-4 Inhibitor",
        "example": "Roflumilast (Daxas)",
        "use": "COPD rất nặng + viêm phế quản mạn + hay đợt cấp",
        "benefit": "Giảm đợt cấp 15-20%",
        "side_effects": "Tiêu chảy, sụt cân, buồn nôn",
        "price": "1,500,000-2,000,000đ/tháng",
        "note": "Đắt, ít dùng tại VN"
    }
}

# Oxy liệu pháp
OXYGEN_THERAPY = {
    "title": "🫁 Oxy Liệu Pháp - Quan Trọng Với COPD Nặng",
    
    "simple_explanation": """
💡 Thở oxy tại nhà là gì?

Khi phổi yếu, không đủ oxy → Cần bổ sung oxy:
- Máy tạo oxy di động
- Bình oxy
- Thở qua ống mũi

Mục tiêu: Giữ SpO2 ≥90% (nồng độ oxy máu)
    """,
    
    "indications": [
        "SpO2 ≤88% khi nghỉ ngơi",
        "PaO2 ≤55 mmHg (khí máu động mạch)",
        "Cor pulmonale (tim phổi)",
        "Hồng cầu tăng cao (Hct >55%)"
    ],
    
    "prescription": {
        "flow_rate": "1-3 lít/phút (qua ống mũi)",
        "duration": "≥15 giờ/ngày (càng nhiều càng tốt)",
        "target": "SpO2 88-92% (KHÔNG quá cao!)",
        "note": "⚠️ COPD KHÔNG nên thở oxy quá cao (>92%) → Nguy hiểm!"
    },
    
    "types": [
        {
            "type": "Máy tạo oxy (Oxygen Concentrator)",
            "pros": "Dùng điện, không hết oxy, tiết kiệm lâu dài",
            "cons": "Đầu tư ban đầu cao",
            "price": "15-30 triệu đồng (mua 1 lần)",
            "use": "Dùng tại nhà, lâu dài"
        },
        {
            "type": "Bình oxy y tế",
            "pros": "Di động được",
            "cons": "Hết oxy phải đổi, tốn kém",
            "price": "200,000-500,000đ/bình (dùng ~1 tuần)",
            "use": "Ra ngoài, di chuyển"
        }
    ],
    
    "benefits": [
        "Giảm khó thở",
        "Tăng khả năng vận động",
        "Kéo dài sống (duy nhất điều trị làm tăng tuổi thọ!)",
        "Cải thiện chất lượng cuộc sống",
        "Giảm áp lực phổi, bảo vệ tim"
    ],
    
    "insurance": "BHYT chi trả một phần chi phí oxy tại nhà (có chỉ định)"
}

# Hướng dẫn sử dụng thuốc xịt
INHALER_TECHNIQUE = {
    "title": "📖 Cách Dùng Thuốc Xịt Đúng",
    
    "importance": "⚠️ 70-80% bệnh nhân dùng SAI thuốc xịt → Thuốc KHÔNG vào phổi → Không hiệu quả!",
    
    "mdi_technique": {
        "name": "MDI (Ống Xịt Định Liều)",
        "steps": [
            "1️⃣ Lắc thuốc 5-10 lần",
            "2️⃣ Ngửa đầu nhẹ, thở RA hết",
            "3️⃣ Ngậm ống xịt, môi kín",
            "4️⃣ Bấm xịt + HÍT VÀO CÙNG LÚC (quan trọng!)",
            "5️⃣ Hít SÂU, CHẬM",
            "6️⃣ Nín thở 10 giây",
            "7️⃣ Thở ra chậm",
            "8️⃣ Chờ 30 giây nếu xịt nhát thứ 2"
        ],
        "common_mistakes": [
            "❌ Hít quá nhanh → Thuốc dính họng",
            "❌ Không nín thở → Thuốc thở ra ngay",
            "❌ Không lắc trước xịt"
        ]
    },
    
    "spacer": {
        "name": "Buồng Chứa (Spacer) - Giúp Xịt Dễ Hơn",
        "benefit": [
            "Thuốc vào phổi nhiều hơn (40% → 70%)",
            "Không cần phối hợp xịt + hít",
            "Giảm thuốc dính họng"
        ],
        "how_to_use": [
            "Gắn spacer vào ống xịt",
            "Bấm xịt 1 nhát vào spacer",
            "Hít ngay từ spacer (trong 5 giây)",
            "Hít sâu, nín thở 10 giây"
        ],
        "price": "150,000-300,000đ",
        "note": "✅ NÊN DÙNG, đặc biệt người già, trẻ em"
    },
    
    "dpi_technique": {
        "name": "DPI (Ống Hít Bột Khô)",
        "examples": "Spiriva HandiHaler, Onbrez Breezhaler",
        "steps": [
            "1️⃣ Mở nắp, đặt viên thuốc",
            "2️⃣ Đóng nắp (sẽ nghe tiếng lách)",
            "3️⃣ Thở RA hết",
            "4️⃣ Ngậm ống, HÍT MẠNH, NHANH",
            "5️⃣ Nín thở 10 giây",
            "6️⃣ Thở ra"
        ],
        "key_difference": "HÍT MẠNH (khác MDI là hít chậm)"
    },
    
    "after_use": [
        "💧 Súc miệng sau xịt ICS (tránh nấm)",
        "🧼 Rửa ống xịt 1 tuần/lần",
        "📅 Kiểm tra hạn sử dụng",
        "🔢 Đếm số lần xịt còn lại"
    ]
}

