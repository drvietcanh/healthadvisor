"""
Sleep Apnea - Triệu chứng
"""

SYMPTOMS = {
    "nighttime": {
        "title": "🔍 Triệu chứng ban đêm (Người ngủ cùng phát hiện):",
        "symptoms": [
            "**Ngáy to** - Ngáy rất to, có thể nghe từ phòng khác",
            "**Ngưng thở** - Ngừng thở 10-60 giây, sau đó thở lại với tiếng hổn hển",
            "**Thở hổn hển** - Thở mạnh sau khi ngưng thở",
            "**Tỉnh giấc** - Thức dậy nhiều lần trong đêm (nhưng không nhớ)",
            "**Tiểu đêm** - Thức dậy đi tiểu nhiều lần",
            "**Vặn mình nhiều** - Trằn trọc, không yên khi ngủ",
            "**Đổ mồ hôi** - Đổ mồ hôi đêm"
        ],
        "note": "💡 Quan trọng: Người ngủ một mình thường KHÔNG biết mình bị! Phải hỏi người ngủ cùng."
    },
    
    "daytime": {
        "title": "🔍 Triệu chứng ban ngày:",
        "symptoms": [
            "**Mệt mỏi, buồn ngủ** - Mệt mỏi dù ngủ đủ giờ",
            "**Buồn ngủ ban ngày** - Ngủ gật khi xem TV, đọc sách, lái xe",
            "**Đau đầu buổi sáng** - Nhức đầu khi thức dậy",
            "**Khó tập trung** - Trí nhớ kém, không tập trung được",
            "**Cáu gắt** - Dễ giận, thay đổi tâm trạng",
            "**Giảm ham muốn tình dục** - Do mệt mỏi",
            "**Khô miệng, đau họng** - Do thở bằng miệng khi ngủ"
        ]
    },
    
    "risk_factors": {
        "title": "⚠️ Yếu tố nguy cơ:",
        "factors": [
            "**Béo phì** - Đặc biệt béo cổ (chu vi cổ >40cm nam, >37cm nữ)",
            "**Tuổi** - Tăng dần theo tuổi",
            "**Nam giới** - Dễ bị hơn nữ (2:1)",
            "**Tăng huyết áp** - 70% người ngưng thở có tăng HA",
            "**Tiểu đường** - Liên quan chặt chẽ",
            "**Uống rượu, thuốc ngủ** - Làm nặng thêm",
            "**Hút thuốc** - Làm đường thở viêm",
            "**Di truyền** - Có người thân bị → Dễ bị hơn"
        ]
    },
    
    "when_to_see_doctor": {
        "title": "🏥 Khi nào cần khám bác sĩ:",
        "urgent": [
            "🚨 Có người ngủ cùng báo ngưng thở khi ngủ",
            "🚨 Ngáy to kèm ngưng thở",
            "🚨 Buồn ngủ ban ngày quá mức (ngủ gật khi lái xe)",
            "🚨 Mệt mỏi dù ngủ đủ",
            "🚨 Có các yếu tố nguy cơ (béo phì, tăng HA, tiểu đường)"
        ],
        "note": "💡 Quan trọng: Ngưng thở khi ngủ NGUY HIỂM - Tăng nguy cơ đột quỵ, tim mạch! Cần điều trị!"
    }
}

