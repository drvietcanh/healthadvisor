"""
Presbyopia - Điều trị
"""

TREATMENT = {
    "glasses": {
        "title": "👓 Kính lão (Điều chỉnh chính):",
        "reading_glasses": {
            "title": "Kính đọc sách (Reading glasses):",
            "description": "Kính chỉ dùng để đọc, nhìn gần",
            "strength": "Độ kính: +1.0 đến +3.0 (tăng dần theo tuổi)",
            "when_to_use": "Chỉ đeo khi đọc sách, làm việc gần",
            "how_to_choose": [
                "Thử từng độ: +1.0, +1.5, +2.0...",
                "Chọn độ nhìn rõ nhất khi đọc ở khoảng cách 30-40cm",
                "Không quá mạnh (gây mỏi mắt)"
            ],
            "where_to_buy": "Mua ở tiệm kính, không cần toa bác sĩ (nếu chỉ lão thị đơn giản)",
            "note": "⚠️ Nếu có bệnh mắt khác (tăng nhãn áp, đục thủy tinh thể) → Cần khám bác sĩ!"
        },
        "bifocals": {
            "title": "Kính hai tròng (Bifocals):",
            "description": "Kính có 2 phần: Trên nhìn xa, dưới nhìn gần",
            "when_to_use": "Khi vừa cần nhìn xa (lái xe) vừa nhìn gần (đọc)",
            "pros": "Một kính dùng được cả hai",
            "cons": "Khó quen, có thể gây chóng mặt"
        },
        "progressive": {
            "title": "Kính đa tròng (Progressive lenses):",
            "description": "Kính chuyển dần từ nhìn xa → nhìn gần (không có đường chia)",
            "when_to_use": "Khi cần nhìn mọi khoảng cách",
            "pros": "Tự nhiên hơn bifocals",
            "cons": "Đắt hơn, cần thời gian quen"
        }
    },
    
    "contact_lenses": {
        "title": "Kính áp tròng đa tiêu (Multifocal contact lenses):",
        "description": "Dành cho người không muốn đeo kính",
        "note": "Cần bác sĩ chỉ định, phù hợp với một số người"
    },
    
    "surgery": {
        "title": "🔬 Phẫu thuật (Hiếm khi cần):",
        "options": [
            "Đặt thủy tinh thể đa tiêu (Multifocal IOL)",
            "LASIK đa tiêu",
            "Chi phí cao, chỉ một số trường hợp phù hợp"
        ],
        "note": "⚠️ Ít khi cần, đeo kính là phương pháp đơn giản và hiệu quả nhất!"
    },
    
    "lifestyle": {
        "title": "💧 Mẹo sống chung với lão thị:",
        "tips": [
            "✅ Đeo kính lão khi đọc → Giảm mỏi mắt",
            "✅ Đủ ánh sáng khi đọc → Giảm căng mắt",
            "✅ Nghỉ ngơi mắt - Sau 20 phút đọc, nhìn xa 20 giây",
            "✅ Tăng font chữ trên điện thoại, máy tính",
            "✅ Dùng đèn bàn khi đọc → Ánh sáng đủ, không quá chói",
            "✅ Không đọc nơi thiếu sáng → Làm mắt mệt hơn"
        ]
    },
    
    "when_to_see_doctor": {
        "title": "🏥 Khi nào cần khám bác sĩ mắt:",
        "soon": [
            "Lần đầu tiên bị lão thị (để đo chính xác độ kính)",
            "Kính lão không còn đủ (phải đổi độ)",
            "Kèm theo nhìn mờ XA (có thể có bệnh mắt khác)",
            "Đau mắt, nhức đầu khi đọc",
            ">50 tuổi chưa khám mắt lần nào"
        ],
        "note": "💡 Khám mắt định kỳ mỗi 1-2 năm để phát hiện các bệnh mắt khác (tăng nhãn áp, đục thủy tinh thể)"
    }
}

