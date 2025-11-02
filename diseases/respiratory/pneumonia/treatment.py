"""
Viêm phổi - Điều trị
Treatment of Pneumonia
"""

from typing import Dict, List

TREATMENT = {
    "principles": {
        "title": "💊 Nguyên tắc điều trị",
        "description": "Điều trị viêm phổi cần:",
        "points": [
            "Kháng sinh: Chống vi khuẩn (nếu do vi khuẩn)",
            "Hỗ trợ: Thở oxy, giảm sốt, giảm ho",
            "Theo dõi: Đánh giá đáp ứng điều trị",
            "Phòng biến chứng: Tránh nhiễm trùng máu, suy hô hấp"
        ]
    },
    
    "antibiotics": {
        "title": "🦠 Kháng sinh",
        "description": "Chọn kháng sinh theo mức độ nặng:",
        "mild": {
            "name": "Viêm phổi nhẹ (điều trị tại nhà)",
            "options": [
                {
                    "name": "Amoxicillin + Acid clavulanic",
                    "dosage": "875mg/125mg × 2 lần/ngày",
                    "duration": "5-7 ngày",
                    "note": "Phổ biến nhất, bao phủ phế cầu, Haemophilus"
                },
                {
                    "name": "Azithromycin",
                    "dosage": "500mg × 1 lần/ngày",
                    "duration": "3-5 ngày",
                    "note": "Mycoplasma, Chlamydia, vi khuẩn không điển hình"
                },
                {
                    "name": "Levofloxacin",
                    "dosage": "500mg × 1 lần/ngày",
                    "duration": "7 ngày",
                    "note": "Kháng sinh mạnh, dùng khi nghi kháng thuốc"
                }
            ],
            "note": "⚠️ Uống đủ liều, đủ ngày (KHÔNG tự ngừng khi hết sốt!)"
        },
        "moderate": {
            "name": "Viêm phổi trung bình (nhập viện)",
            "options": [
                {
                    "name": "Ceftriaxone + Azithromycin",
                    "dosage": "Ceftriaxone 1g TM × 1 lần/ngày + Azithromycin 500mg uống",
                    "duration": "7-10 ngày",
                    "note": "Phổ biến ở bệnh viện VN"
                },
                {
                    "name": "Levofloxacin TM",
                    "dosage": "500mg TM × 1 lần/ngày",
                    "duration": "7-10 ngày",
                    "note": "Kháng sinh mạnh, một liều"
                }
            ]
        },
        "severe": {
            "name": "Viêm phổi nặng (ICU)",
            "options": [
                {
                    "name": "Piperacillin/Tazobactam + Azithromycin",
                    "dosage": "4.5g TM × 3 lần/ngày + Azithromycin 500mg TM",
                    "duration": "10-14 ngày",
                    "note": "Phổ rộng, bao phủ vi khuẩn kháng thuốc"
                },
                {
                    "name": "Vancomycin + Ceftriaxone",
                    "dosage": "Theo cân nặng TM + Ceftriaxone 2g TM",
                    "duration": "10-14 ngày",
                    "note": "Khi nghi tụ cầu kháng thuốc (MRSA)"
                }
            ],
            "warning": "⚠️ Viêm phổi nặng = TỬ VONG cao, cần điều trị tích cực!"
        },
        "viral": {
            "name": "Viêm phổi do virus",
            "description": "Không dùng kháng sinh (trừ khi bội nhiễm vi khuẩn)",
            "treatments": [
                {
                    "name": "COVID-19",
                    "treatment": "Remdesivir, Dexamethasone (nếu nặng)",
                    "note": "Tiêm vaccine phòng ngừa là quan trọng nhất"
                },
                {
                    "name": "Cúm",
                    "treatment": "Oseltamivir (Tamiflu) - uống trong 48h đầu",
                    "prevention": "Tiêm vaccine cúm hàng năm"
                },
                {
                    "name": "RSV",
                    "treatment": "Hỗ trợ (thở oxy), không có thuốc đặc hiệu",
                    "note": "Trẻ nhỏ có thể cần thở máy"
                }
            ]
        }
    },
    
    "supportive": {
        "title": "💉 Điều trị hỗ trợ",
        "treatments": [
            {
                "name": "Thở oxy",
                "indication": "SpO2 <92% hoặc khó thở",
                "methods": [
                    "Ống thở mũi: 2-4 L/phút (nhẹ)",
                    "Mặt nạ oxy: 5-10 L/phút (trung bình)",
                    "Thở máy: Nếu suy hô hấp nặng"
                ]
            },
            {
                "name": "Giảm sốt",
                "medications": [
                    "Paracetamol 500mg-1g × 3-4 lần/ngày",
                    "Ibuprofen 400mg × 3 lần/ngày (nếu không có chống chỉ định)"
                ],
                "note": "Uống nhiều nước khi sốt"
            },
            {
                "name": "Giảm ho",
                "medications": [
                    "Ho có đờm: Không dùng thuốc giảm ho (để tống đờm ra)",
                    "Ho khan, mất ngủ: Dextromethorphan, Codein (theo chỉ định BS)"
                ],
                "note": "Ho có đờm = TỐT (tống vi khuẩn ra ngoài)"
            },
            {
                "name": "Bù nước",
                "indication": "Sốt, mất nước",
                "methods": [
                    "Uống nhiều nước, Oresol",
                    "Truyền dịch TM nếu không uống được"
                ]
            }
        ]
    },
    
    "duration": {
        "title": "⏱️ Thời gian điều trị",
        "guidelines": [
            {
                "severity": "Nhẹ",
                "duration": "5-7 ngày",
                "note": "Kháng sinh đủ liều, đủ ngày"
            },
            {
                "severity": "Trung bình",
                "duration": "7-10 ngày",
                "note": "Nhập viện, theo dõi đáp ứng"
            },
            {
                "severity": "Nặng",
                "duration": "10-14 ngày",
                "note": "ICU, điều trị tích cực"
            },
            {
                "severity": "Áp xe phổi",
                "duration": "14-21 ngày",
                "note": "Kháng sinh dài ngày, có thể cần dẫn lưu mủ"
            }
        ],
        "warning": "⚠️ KHÔNG tự ngừng kháng sinh khi hết sốt! Uống đủ liều để diệt hết vi khuẩn"
    },
    
    "monitoring": {
        "title": "📊 Theo dõi điều trị",
        "indicators": [
            {
                "name": "Đáp ứng tốt",
                "signs": [
                    "Sốt giảm sau 48-72h điều trị",
                    "Ho giảm, đờm ít hơn",
                    "Khó thở cải thiện",
                    "Cảm giác khỏe hơn"
                ]
            },
            {
                "name": "Không đáp ứng (cần điều chỉnh)",
                "signs": [
                    "Sốt không giảm sau 72h",
                    "Khó thở nặng hơn",
                    "Đờm nhiều, đổi màu (vàng/xanh)",
                    "Lơ mơ, không tỉnh táo"
                ],
                "action": "→ Cần đổi kháng sinh, có thể cần nhập viện"
            }
        ]
    },
    
    "when_to_hospitalize": {
        "title": "🏥 Khi nào cần nhập viện?",
        "criteria": [
            {
                "indication": "Mức độ nặng (CURB-65 ≥2)",
                "details": [
                    "Lú lẫn, không tỉnh táo",
                    "Thở nhanh ≥30 lần/phút",
                    "Huyết áp tụt <90/60",
                    "Ure máu tăng"
                ]
            },
            {
                "indication": "Suy hô hấp",
                "details": [
                    "SpO2 <92% dù thở oxy",
                    "Khó thở nặng, không nói được câu dài",
                    "Cần thở máy"
                ]
            },
            {
                "indication": "Yếu tố nguy cơ",
                "details": [
                    "Người >65 tuổi",
                    "Bệnh mãn tính nặng (COPD, suy tim, tiểu đường)",
                    "Suy giảm miễn dịch",
                    "Không uống được thuốc (nôn, lơ mơ)"
                ]
            },
            {
                "indication": "Biến chứng",
                "details": [
                    "Nhiễm trùng máu (Sepsis)",
                    "Áp xe phổi",
                    "Tràn dịch màng phổi"
                ]
            }
        ],
        "warning": "⚠️ Người già, bệnh mãn tính → Nên nhập viện sớm để theo dõi!"
    }
}

