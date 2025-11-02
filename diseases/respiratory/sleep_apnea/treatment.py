"""
Sleep Apnea - Điều trị
"""

TREATMENT = {
    "cpap": {
        "title": "💨 Máy CPAP (Continuous Positive Airway Pressure) - ĐIỀU TRỊ CHÍNH:",
        "how_it_works": "Máy thổi không khí áp lực dương → Giữ đường thở mở → Không ngưng thở",
        "components": [
            "Máy CPAP - Tạo áp lực không khí",
            "Ống dẫn khí",
            "Mặt nạ - Đeo khi ngủ (mũi hoặc mũi-miệng)"
        ],
        "benefits": [
            "✅ Giải quyết HOÀN TOÀN ngưng thở",
            "✅ Ngủ ngon, không mệt mỏi ban ngày",
            "✅ Giảm nguy cơ đột quỵ, tim mạch",
            "✅ Cải thiện chất lượng sống rõ rệt"
        ],
        "challenges": [
            "Khó quen ban đầu (cảm giác khó chịu)",
            "Tiếng máy (máy hiện đại rất yên tĩnh)",
            "Cần đeo mỗi đêm để hiệu quả",
            "Chi phí (có thể hỗ trợ bảo hiểm)"
        ],
        "note": "⚠️ QUAN TRỌNG: Phải đeo MỖI ĐÊM, không bỏ! Chỉ cần 1 đêm không đeo → Triệu chứng quay lại."
    },
    
    "lifestyle": {
        "title": "💧 Thay đổi lối sống (QUAN TRỌNG):",
        "weight_loss": {
            "title": "Giảm cân (Nếu béo phì):",
            "benefit": "Giảm 10% cân nặng → Giảm 50% mức độ ngưng thở!",
            "how": "Ăn ít calo, tập thể dục → Giảm cân → Cải thiện rõ rệt"
        },
        "position": {
            "title": "Tư thế ngủ:",
            "tips": [
                "Nằm nghiêng thay vì nằm ngửa (giảm tắc đường thở)",
                "Gối cao vừa phải (không quá cao)",
                "Có thể dùng gối đặc biệt để nằm nghiêng"
            ]
        },
        "avoid": {
            "title": "Tránh:",
            "items": [
                "❌ Rượu bia trước khi ngủ (làm nặng ngưng thở)",
                "❌ Thuốc ngủ (làm nặng ngưng thở)",
                "❌ Hút thuốc (làm viêm đường thở)",
                "❌ Ăn no trước khi ngủ"
            ]
        }
    },
    
    "oral_appliances": {
        "title": "🦷 Thiết bị miệng (Oral appliances):",
        "description": "Máng hàm đưa hàm dưới ra trước → Giữ đường thở mở",
        "when": "Ngưng thở nhẹ-trung bình, không chịu được CPAP",
        "pros": "Dễ dùng, nhỏ gọn",
        "cons": "Ít hiệu quả hơn CPAP, có thể gây đau hàm"
    },
    
    "surgery": {
        "title": "🔬 Phẫu thuật (Khi các phương pháp khác không hiệu quả):",
        "options": [
            "Cắt amidan, nạo VA (nếu to)",
            "Cắt mô mềm vùng họng (UPPP)",
            "Điều chỉnh hàm (nếu hàm nhỏ)",
            "Mở khí quản (hiếm, chỉ trường hợp nặng)"
        ],
        "note": "⚠️ Phẫu thuật không phải lúc nào cũng hiệu quả. CPAP vẫn là phương pháp tốt nhất!"
    },
    
    "diagnosis": {
        "title": "🔬 Chẩn đoán:",
        "sleep_study": {
            "title": "Đo đa ký giấc ngủ (Polysomnography):",
            "description": "Đo khi ngủ qua đêm tại phòng lab",
            "measures": [
                "Số lần ngưng thở/giờ (AHI - Apnea-Hypopnea Index)",
                "Nồng độ oxy trong máu",
                "Các giai đoạn giấc ngủ",
                "Nhịp tim, huyết áp"
            ],
            "severity": {
                "mild": "AHI 5-15: Ngưng thở nhẹ",
                "moderate": "AHI 15-30: Ngưng thở trung bình",
                "severe": "AHI >30: Ngưng thở nặng"
            }
        },
        "home_test": {
            "title": "Đo tại nhà (Home sleep test):",
            "description": "Đơn giản hơn, đo một số chỉ số cơ bản",
            "note": "Phù hợp ngưng thở nhẹ-trung bình"
        }
    },
    
    "when_to_see_doctor": {
        "title": "🏥 Khi nào cần khám bác sĩ:",
        "urgent": [
            "🚨 Có triệu chứng ngưng thở (ngáy to, mệt mỏi ban ngày)",
            "🚨 Có yếu tố nguy cơ (béo phì, tăng HA)",
            "🚨 Buồn ngủ quá mức (nguy hiểm khi lái xe)",
            "🚨 Có bệnh tim mạch, đột quỵ"
        ],
        "note": "💡 Quan trọng: Ngưng thở khi ngủ cần được chẩn đoán và điều trị! Đừng nghĩ 'chỉ là ngáy'!"
    }
}

