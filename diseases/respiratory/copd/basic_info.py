"""
COPD - Thông tin cơ bản
Basic information about COPD
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


