"""
Đau đầu - Điều trị
Treatment of Headache
"""

from typing import Dict, List

TREATMENT = {
    "principles": {
        "title": "💊 Nguyên tắc điều trị",
        "description": "Điều trị đau đầu cần:",
        "points": [
            "Phân biệt loại đau đầu (căng thẳng vs đau nửa đầu vs nguy hiểm)",
            "Điều trị cắt cơn (khi đang đau)",
            "Điều trị phòng ngừa (nếu đau thường xuyên)",
            "Loại trừ đau đầu nguy hiểm (xuất huyết não, u não)"
        ]
    },
    
    "tension_headache": {
        "title": "Điều trị đau đầu căng thẳng",
        "acute": {
            "name": "Cắt cơn đau",
            "medications": [
                {
                    "name": "Paracetamol",
                    "dosage": "500-1000mg × 2-3 lần/ngày",
                    "max_daily": "Không quá 4g/ngày",
                    "note": "An toàn, ít tác dụng phụ"
                },
                {
                    "name": "Ibuprofen",
                    "dosage": "400mg × 2-3 lần/ngày",
                    "max_daily": "Không quá 2400mg/ngày",
                    "note": "Hiệu quả hơn Paracetamol, nhưng có thể gây đau dạ dày",
                    "warning": "⚠️ Không dùng nếu có bệnh dạ dày, thận"
                },
                {
                    "name": "Aspirin",
                    "dosage": "300-500mg × 2-3 lần/ngày",
                    "note": "Có thể gây đau dạ dày, không dùng cho trẻ em",
                    "warning": "⚠️ Không dùng nếu có bệnh dạ dày"
                }
            ],
            "non_medication": [
                "Nghỉ ngơi, ngủ một giấc",
                "Massage cổ, gáy, thái dương",
                "Chườm lạnh hoặc nóng",
                "Tắm nước ấm",
                "Tập thở sâu, thư giãn"
            ]
        },
        "prevention": {
            "name": "Phòng ngừa",
            "methods": [
                "Giảm căng thẳng: Yoga, thiền, nghe nhạc",
                "Ngủ đủ 7-8 giờ/đêm",
                "Tập thể dục đều đặn (đi bộ 30 phút/ngày)",
                "Sửa tư thế ngồi (màn hình ngang tầm mắt)",
                "Nghỉ mắt khi làm việc (20-20-20: Mỗi 20 phút nhìn xa 20 giây)",
                "Uống đủ nước (1.5-2L/ngày)",
                "Ăn đều bữa, không để đói",
                "Massage định kỳ cổ, gáy"
            ]
        }
    },
    
    "migraine": {
        "title": "Điều trị đau nửa đầu",
        "acute": {
            "name": "Cắt cơn đau",
            "mild_moderate": [
                {
                    "name": "Paracetamol/Ibuprofen",
                    "note": "Có thể hiệu quả nếu dùng SỚM (trong 30 phút đầu)"
                },
                {
                    "name": "Kết hợp Paracetamol + Caffeine",
                    "note": "Caffeine làm tăng hấp thu thuốc"
                }
            ],
            "moderate_severe": [
                {
                    "name": "Triptans",
                    "examples": [
                        "Sumatriptan 50-100mg (uống hoặc xịt mũi)",
                        "Rizatriptan 10mg",
                        "Zolmitriptan 2.5-5mg"
                    ],
                    "how_to_use": "Dùng NGAY khi đau, KHÔNG đợi nặng",
                    "contraindications": [
                        "Không dùng nếu có bệnh tim, tăng huyết áp không kiểm soát",
                        "Không dùng nếu có tiền sử đột quỵ, thiếu máu cơ tim",
                        "Không dùng khi đang mang thai"
                    ],
                    "warning": "⚠️ Cần bác sĩ kê đơn - KHÔNG tự mua!"
                },
                {
                    "name": "Ergotamine",
                    "note": "Thuốc cũ, ít dùng hơn Triptan",
                    "warning": "Có nhiều tác dụng phụ - Cần bác sĩ chỉ định"
                }
            ],
            "supportive": [
                "Nằm phòng tối, yên tĩnh",
                "Chườm lạnh trán, thái dương",
                "Uống nước (nếu không nôn)",
                "Thuốc chống nôn: Metoclopramide, Domperidone (nếu nôn nhiều)"
            ]
        },
        "prevention": {
            "name": "Phòng ngừa (nếu đau ≥4 lần/tháng)",
            "medications": [
                {
                    "name": "Propranolol",
                    "dosage": "40-160mg/ngày",
                    "note": "Thuốc huyết áp, nhưng phòng ngừa đau nửa đầu hiệu quả",
                    "warning": "Không dùng nếu hen suyễn, suy tim"
                },
                {
                    "name": "Topiramate",
                    "dosage": "25-100mg/ngày",
                    "note": "Thuốc động kinh, phòng ngừa đau nửa đầu",
                    "side_effects": "Giảm cân, tê tay chân, suy nghĩ chậm"
                },
                {
                    "name": "Amitriptyline",
                    "dosage": "10-50mg/ngày (uống buổi tối)",
                    "note": "Thuốc chống trầm cảm, phòng ngừa đau nửa đầu",
                    "side_effects": "Buồn ngủ (nên uống buổi tối)"
                }
            ],
            "lifestyle": [
                "Tránh yếu tố kích phát: Rượu vang, phô mai, chocolate, đồ nướng",
                "Ngủ đủ, đều giờ (thức khuya, ngủ quá nhiều → Đau đầu)",
                "Ăn đều bữa, không bỏ bữa",
                "Giảm căng thẳng: Yoga, thiền, massage",
                "Tập thể dục đều đặn (nhưng không tập khi đang đau)"
            ],
            "note": "⚠️ Dùng thuốc phòng ngừa ít nhất 3-6 tháng mới đánh giá hiệu quả"
        }
    },
    
    "medication_overuse_prevention": {
        "title": "⚠️ Phòng ngừa lạm dụng thuốc",
        "rules": [
            "Không uống thuốc giảm đau quá 2-3 lần/tuần",
            "Tối đa 10 ngày/tháng",
            "Nếu đau đầu thường xuyên → Dùng thuốc PHÒNG NGỪA, không uống thuốc cắt cơn mỗi ngày",
            "Không tự tăng liều thuốc",
            "Nếu đau đầu tăng khi uống thuốc → Có thể đã lạm dụng → Cần bác sĩ"
        ]
    },
    
    "when_to_see_doctor": {
        "title": "👨‍⚕️ Khi nào cần đi khám bác sĩ?",
        "urgent": {
            "name": "Cấp cứu ngay (GỌI 115):",
            "signs": [
                "Đau đầu sét đánh (đau dữ dội đột ngột)",
                "Đau đầu + Sốt + Cứng gáy",
                "Đau đầu sau chấn thương đầu",
                "Đau đầu + Yếu tay chân + Nhìn mờ",
                "Đau đầu lần đầu, rất nặng (người >50 tuổi)"
            ]
        },
        "soon": {
            "name": "Khám trong vài ngày:",
            "signs": [
                "Đau đầu tăng dần, ngày càng nặng",
                "Đau đầu thay đổi đặc tính (khác lạ)",
                "Đau đầu kèm co giật",
                "Đau đầu ở người >50 tuổi lần đầu",
                "Đau đầu ở trẻ em <10 tuổi"
            ]
        },
        "routine": {
            "name": "Khám định kỳ:",
            "signs": [
                "Đau đầu thường xuyên (≥4 lần/tháng)",
                "Đau đầu ảnh hưởng cuộc sống, công việc",
                "Thuốc không còn hiệu quả",
                "Cần tư vấn về thuốc phòng ngừa"
            ]
        }
    }
}

