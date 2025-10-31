"""
Sơ cứu Y Khoa
Medical First Aid (Hạ đường huyết, Ngộ độc)
"""

FIRST_AID_MEDICAL = {
    "hypoglycemia": {
        "name": "Hạ đường huyết (Tiểu đường)",
        "icon": "🍬",
        "signs": {
            "title": "🔍 Dấu hiệu:",
            "items": [
                "Đói bụng đột ngột",
                "Run tay, chân",
                "Đổ mồ hôi lạnh",
                "Hồi hộp, tim đập nhanh",
                "Chóng mặt, yếu người",
                "Lú lẫn, cáu gắt bất thường",
                "Nhìn mờ",
                "Nghiêm trọng: Co giật, hôn mê"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY (Quy tắc 15-15):",
            "steps": [
                "1️⃣ **ĂN ĐƯỜNG NGAY:**",
                "   - 15g đường (3-4 viên kẹo hoặc 1 thìa đường)",
                "   - Hoặc: 150ml nước ngọt có ga",
                "   - Hoặc: 1 hộp sữa có đường nhỏ",
                "   - Hoặc: 1 thìa mật ong",
                "2️⃣ **Ngồi/nằm nghỉ 15 phút**",
                "3️⃣ **Đo lại đường huyết** (nếu có máy)",
                "4️⃣ **Nếu vẫn < 70 mg/dL:** Ăn thêm 15g đường nữa",
                "5️⃣ **Sau khi hồi phục:** Ăn bữa phụ nhẹ (bánh mì, chuối)"
            ]
        },
        "severe": {
            "title": "🚨 Nếu NGHIÊM TRỌNG (lơ mơ, không nuốt được):",
            "steps": [
                "❗ **GỌI 115 NGAY**",
                "❗ **Đặt nghiêng người** - Tránh sặc",
                "❗ **KHÔNG cho ăn/uống** - Có thể sặc",
                "❗ **Nếu có Glucagon injection:** Tiêm theo hướng dẫn",
                "❗ **Chờ xe cấp cứu**"
            ]
        },
        "prevention": {
            "title": "💡 Phòng ngừa:",
            "items": [
                "✅ Luôn mang theo kẹo/đường khi ra ngoài",
                "✅ Ăn đúng giờ, không bỏ bữa",
                "✅ Đo đường huyết thường xuyên",
                "✅ Điều chỉnh thuốc/insulin đúng liều",
                "✅ Đeo vòng tay/thẻ ghi \"Bệnh tiểu đường\""
            ]
        },
        "note": "💊 Người tiểu đường dùng insulin/thuốc hạ đường cần đặc biệt cảnh giác!"
    },
    
    "poisoning": {
        "name": "Ngộ độc",
        "icon": "☠️",
        "signs": {
            "title": "🔍 Dấu hiệu ngộ độc:",
            "items": [
                "Buồn nôn, nôn mửa",
                "Đau bụng",
                "Tiêu chảy",
                "Chóng mặt, lơ mơ",
                "Khó thở",
                "Co giật (nếu nặng)"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY:",
            "steps": [
                "1️⃣ **GỌI 115 NGAY** - Hoặc Trung tâm chống độc: 024.3929.5743",
                "2️⃣ **HỎI người bệnh** (nếu còn tỉnh):",
                "   - Uống/Nhậu gì?",
                "   - Bao nhiêu?",
                "   - Khi nào?",
                "3️⃣ **LƯU Ý:**",
                "   - Nếu hôn mê, nằm nghiêng (tránh sặc)",
                "   - Giữ lại vật gây ngộ độc (thuốc, chai lọ...)",
                "   - KHÔNG tự ý gây nôn (trừ khi nhân viên y tế hướng dẫn)",
                "4️⃣ **ĐỢI xe cấp cứu** - Theo dõi hô hấp, mạch"
            ]
        },
        "dont": {
            "title": "❌ TUYỆT ĐỐI KHÔNG:",
            "items": [
                "❌ KHÔNG cho uống sữa/trứng sống (làm sai lệch)",
                "❌ KHÔNG tự ý cho uống than hoạt tính (chỉ khi bác sĩ chỉ định)",
                "❌ KHÔNG gây nôn khi uống chất tẩy/axit (làm bỏng thêm)",
                "❌ KHÔNG bỏ cuộc - Tiếp tục theo dõi"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 HOẶC TRUNG TÂM CHỐNG ĐỘC NGAY:",
            "items": [
                "⛔ Nghi ngờ ngộ độc (dù nhẹ)",
                "⛔ Hôn mê, lơ mơ",
                "⛔ Khó thở",
                "⛔ Co giật",
                "⛔ Ngộ độc ở trẻ em"
            ]
        },
        "note": "💡 **QUAN TRỌNG:** Mỗi phút đều quý! Gọi ngay Trung tâm chống độc để được hướng dẫn chính xác!"
    }
}

