"""
Chronic Sinusitis - Triệu chứng
"""

SYMPTOMS = {
    "common": {
        "title": "🔍 Triệu chứng thường gặp:",
        "nasal": {
            "title": "Triệu chứng mũi:",
            "symptoms": [
                "**Nghẹt mũi** - Một hoặc hai bên, kéo dài",
                "**Chảy dịch mũi** - Dịch vàng/xanh, đặc, mùi hôi",
                "**Dịch chảy xuống họng** - Cảm giác có đờm ở họng",
                "**Giảm khứu giác** - Không ngửi thấy mùi hoặc ngửi kém",
                "**Hắt hơi** - Đặc biệt khi tiếp xúc dị nguyên"
            ]
        },
        "facial_pain": {
            "title": "Đau mặt, đầu:",
            "symptoms": [
                "**Đau vùng mặt** - Đau ở trán, má, giữa hai mắt",
                "**Đau đầu** - Đặc biệt buổi sáng, khi cúi xuống",
                "**Đau răng hàm trên** - Do viêm xoang hàm",
                "**Cảm giác nặng mặt** - Như bị ép, đầy"
            ]
        },
        "other": {
            "title": "Triệu chứng khác:",
            "symptoms": [
                "**Ho** - Do dịch chảy xuống họng",
                "**Mệt mỏi** - Do viêm mạn tính",
                "**Sốt nhẹ** - Nếu có nhiễm trùng",
                "**Hơi thở hôi** - Do dịch ứ đọng"
            ]
        }
    },
    
    "duration": {
        "title": "⏰ Thời gian:",
        "chronic": "Kéo dài >12 tuần (khác viêm xoang cấp: <4 tuần)",
        "recurrent": "Tái phát nhiều lần trong năm",
        "note": "💡 Nếu triệu chứng <4 tuần → Viêm xoang cấp. >12 tuần → Viêm xoang mạn."
    },
    
    "when_to_see_doctor": {
        "title": "🏥 Khi nào cần khám bác sĩ:",
        "soon": [
            "Triệu chứng kéo dài >12 tuần",
            "Nghẹt mũi, đau đầu thường xuyên",
            "Giảm khứu giác",
            "Dịch mũi vàng/xanh, mùi hôi",
            "Ảnh hưởng giấc ngủ, sinh hoạt"
        ],
        "urgent": [
            "🚨 Sốt cao, đau mặt dữ dội",
            "🚨 Sưng đỏ quanh mắt",
            "🚨 Nhìn đôi, nhìn mờ",
            "🚨 Cứng cổ, nhức đầu dữ dội (biến chứng hiếm)"
        ]
    }
}

