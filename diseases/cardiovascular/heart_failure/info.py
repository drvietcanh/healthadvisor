"""
Heart Failure Information
Disease explanation and symptoms in simple language
"""

# ============= SUY TIM LÀ GÌ? =============

DISEASE_INFO = {
    "name_vn": "Suy Tim",
    "name_en": "Heart Failure",
    "simple_explanation_vn": """
🫀 SUY TIM LÀ GÌ?

Suy tim có nghĩa là tim bạn không bơm máu tốt như trước. 
Không phải tim ngừng đập, mà tim yếu đi, không đủ sức đẩy máu nuôi cơ thể.

Giống như chiếc bơm nước cũ - vẫn chạy nhưng không đủ mạnh.
""",
    "causes_simple_vn": [
        "💔 Nhồi máu cơ tim (đã bị đau tim trước đây)",
        "📈 Huyết áp cao lâu năm (tim phải làm việc vất vả)",
        "🩺 Bệnh van tim (van tim hỏng, không đóng mở tốt)",
        "🫀 Bệnh cơ tim (cơ tim yếu từ nhiều nguyên nhân)",
        "💓 Rối loạn nhịp tim (tim đập không đều)"
    ]
}

# ============= DẤU HIỆU NHẬN BIẾT =============

SYMPTOMS_SIMPLE = {
    "main_signs_vn": {
        "title": "🚨 5 DẤU HIỆU CHÍNH - Ghi nhớ 5 chữ H:",
        "note": "💡 Đây là cách ghi nhớ DÂN GIAN (mnemonic) để dễ nhớ, không phải phân loại y khoa chính thức. Theo y khoa chuẩn (AHA/ESC), triệu chứng chính là: Dyspnea (khó thở), Edema (phù), Fatigue (mệt mỏi), và giảm khả năng gắng sức.",
        "signs": [
            {
                "letter": "H1 - HỔN HẾN (khó thở)",
                "description": "Thở nhanh, thở gấp, đặc biệt khi:",
                "details": [
                    "- Đi bộ nhanh, leo cầu thang",
                    "- Nằm xuống (phải kê nhiều gối mới thở được)",
                    "- Ban đêm thức giấc vì khó thở",
                    "- Cảm giác như sắp ngạt"
                ]
            },
            {
                "letter": "H2 - HÚNG (phù nước)",
                "description": "Sưng phù ở:",
                "details": [
                    "- Bàn chân, cổ chân (ấn vào lõm xuống)",
                    "- Ống chân, bắp chân",
                    "- Bụng chướng (tích nước trong bụng)",
                    "- Tăng cân đột ngột (2-3kg trong vài ngày)"
                ]
            },
            {
                "letter": "H3 - HƠI (mệt mỏi, uể oải)",
                "description": "Mệt lả không rõ lý do:",
                "details": [
                    "- Làm việc nhà cũng thấy mệt",
                    "- Không muốn hoạt động",
                    "- Ngủ nhiều vẫn mệt",
                    "- Không còn sức như trước"
                ]
            },
            {
                "letter": "H4 - HO (ho dai dẳng)",
                "description": "Ho kéo dài, đặc biệt:",
                "details": [
                    "- Ho ban đêm",
                    "- Ho khi nằm",
                    "- Khạc đờm có bọt màu hồng",
                    "- Ho không khỏi dù uống thuốc ho"
                ]
            },
            {
                "letter": "H5 - HỐI (chóng mặt, choáng váng)",
                "description": "Cảm giác:",
                "details": [
                    "- Đầu quay quay, muốn té",
                    "- Đứng lên bị choáng",
                    "- Tim đập nhanh, hồi hộp",
                    "- Ngất xỉu (nghiêm trọng)"
                ]
            }
        ]
    },
    "emergency_vn": {
        "title": "🚨 KHI NÀO GỌI CẤP CỨU 115?",
        "signs": [
            "⛔ Thở rất khó, phải há hốc mồm thở",
            "⛔ Ngực đau dữ dội",
            "⛔ Tím môi, tím móng tay",
            "⛔ Khạc đờm có máu, bọt hồng",
            "⛔ Choáng váng, sắp ngất",
            "⛔ Tim đập rất nhanh hoặc rất chậm"
        ]
    }
}

