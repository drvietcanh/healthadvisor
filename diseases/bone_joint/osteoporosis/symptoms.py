"""
Osteoporosis Symptoms - Triệu Chứng Loãng Xương
"""

SYMPTOMS = {
    "early_stage": {
        "title": "⚠️ Giai Đoạn Sớm:",
        "description": "KHÔNG CÓ triệu chứng! (Thầm lặng)",
        "note": "Đây là lý do tại sao loãng xương nguy hiểm - không biết cho đến khi gãy!"
    },
    
    "advanced_stage": {
        "title": "🔴 Giai Đoạn Muộn:",
        "symptoms": [
            {
                "name": "Đau lưng",
                "description": "Đau âm ỉ, kéo dài (do đốt sống yếu)",
                "location": "Thắt lưng, cổ"
            },
            {
                "name": "Còng lưng (Gù)",
                "description": "Đốt sống gãy/xẹp → Cột sống cong",
                "visual": "Người già còng lưng rõ rệt"
            },
            {
                "name": "Giảm chiều cao",
                "description": "Cao lúc trẻ → Thấp hơn khi già",
                "example": "Giảm >3cm là dấu hiệu đáng lo"
            },
            {
                "name": "Gãy xương dễ dàng",
                "description": "Ngã nhẹ, ho mạnh, cúi người → Gãy",
                "common_sites": [
                    "Cổ tay (ngã chống tay)",
                    "Đốt sống (cúi nhặt đồ)",
                    "Cổ xương đùi (ngã)"
                ]
            }
        ]
    },
    
    "fracture_warning": {
        "title": "🚨 Dấu Hiệu Gãy Xương:",
        "signs": [
            "Đau dữ dội tại chỗ",
            "Sưng, bầm tím",
            "Không cử động được",
            "Biến dạng (nếu gãy hở)"
        ],
        "action": "📞 GỌI 115 hoặc ĐẾN BỆNH VIỆN NGAY!"
    },
    
    "when_to_see_doctor": {
        "title": "💡 Khi Nào Nên Đi Khám:",
        "indicators": [
            "Phụ nữ >50 tuổi",
            "Nam giới >60 tuổi",
            "Gia đình có người loãng xương",
            "Đã gãy xương trước đó",
            "Dùng Corticosteroid >3 tháng",
            "Giảm chiều cao >3cm",
            "Còng lưng rõ rệt"
        ]
    }
}

