"""
Sơ cứu Bổ Sung 3B - Ngừng tim và Chảy máu cam
Additional Emergency Situations 3B
"""

FIRST_AID_ADDITIONAL3B = {
    "cardiac_arrest": {
        "name": "Ngừng tim - CPR (Hồi sức tim phổi)",
        "icon": "💔",
        "signs": {
            "title": "🔍 Dấu hiệu ngừng tim:",
            "items": [
                "KHÔNG phản ứng (gọi, lay không tỉnh)",
                "KHÔNG thở (kiểm tra 10 giây: Không thấy ngực phập phồng, không nghe thở)",
                "Mất mạch (không bắt được mạch cổ tay, cổ)",
                "Da xanh, tím tái",
                "Đồng tử giãn (mắt mở to)"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY (Chuỗi sống còn):",
            "steps": [
                "1️⃣ **KIỂM TRA AN TOÀN:**",
                "   - Kiểm tra môi trường an toàn (điện, khí độc...)",
                "   - Đừng trở thành nạn nhân tiếp theo!",
                "2️⃣ **KIỂM TRA PHẢN ỨNG:**",
                "   - Lay vai, gọi to: 'Anh/Chị ơi, nghe tôi không?'",
                "   - Không phản ứng → Ngừng tim",
                "3️⃣ **GỌI 115 NGAY:**",
                "   - Hoặc nhờ người khác gọi",
                "   - Nói rõ địa chỉ, tình trạng",
                "4️⃣ **KIỂM TRA THỞ (10 giây):**",
                "   - Ngửa đầu, nâng cằm (mở đường thở)",
                "   - Áp má gần mũi, mắt nhìn ngực",
                "   - Không thấy ngực phập phồng, không nghe thở = Ngừng thở",
                "5️⃣ **BẮT ĐẦU CPR (Hồi sức tim phổi):**",
                "   - **ÉP NGỰC:**",
                "     * Vị trí: Giữa ngực (xương ức)",
                "     * Tay: 2 tay chồng lên nhau, ép thẳng xuống",
                "     * Độ sâu: 5-6 cm",
                "     * Tốc độ: 100-120 lần/phút (như nhịp bài 'Stayin' Alive')",
                "     * Ép 30 lần",
                "   - **HÀ HƠI THỔI NGẠT (nếu có khả năng):**",
                "     * Ngửa đầu, nâng cằm",
                "     * Bịt mũi, thổi vào miệng 2 lần",
                "     * Mỗi lần thổi 1 giây, thấy ngực phồng lên",
                "   - **LẶP LẠI:** 30 ép ngực → 2 hà hơi (5 chu kỳ = 2 phút)",
                "6️⃣ **TIẾP TỤC đến khi:**",
                "   - Xe cấp cứu đến",
                "   - Người bệnh tỉnh lại",
                "   - Quá mệt, không thể tiếp tục",
                "7️⃣ **NẾU CÓ MÁY SỐC TIM (AED):**",
                "   - Bật máy, làm theo hướng dẫn",
                "   - Dán miếng dán lên ngực",
                "   - Máy sẽ phân tích và hướng dẫn sốc điện nếu cần"
            ]
        },
        "compression_only": {
            "title": "💡 CPR chỉ ép ngực (Hands-Only CPR):",
            "description": "Nếu không thể hà hơi, CHỈ ÉP NGỰC cũng hiệu quả!",
            "steps": [
                "1️⃣ Ép ngực liên tục 100-120 lần/phút",
                "2️⃣ Không dừng (trừ khi quá mệt)",
                "3️⃣ Tiếp tục đến khi xe cấp cứu đến"
            ],
            "note": "💡 Ép ngực quan trọng hơn hà hơi - Đừng ngại làm!"
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NGAY:",
            "items": [
                "⛔ Bất kỳ người nào ngất, không phản ứng",
                "⛔ Không thở, không có mạch",
                "⛔ Bắt đầu CPR NGAY, không chờ xe cấp cứu!"
            ]
        },
        "note": "⏱️ **MỖI PHÚT CHẬM:** Giảm 10% cơ hội sống! CPR NGAY → Tăng gấp 2-3 lần cơ hội sống!"
    },
    
    "nosebleed": {
        "name": "Chảy máu cam nặng",
        "icon": "🩸",
        "signs": {
            "title": "🔍 Chảy máu cam:",
            "items": [
                "Máu chảy từ 1 hoặc 2 bên mũi",
                "Có thể chảy ra sau họng (nuốt vào dạ dày)",
                "Nặng: Chảy nhiều, không cầm được"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY:",
            "steps": [
                "1️⃣ **NGỒI THẲNG, NGHIÊNG ĐẦU VỀ PHÍA TRƯỚC:**",
                "   - Không ngửa đầu ra sau (máu sẽ chảy vào họng → Nuốt → Buồn nôn)",
                "2️⃣ **BỊT MŨI 10-15 PHÚT:**",
                "   - Dùng ngón tay cái và trỏ bịt chặt 2 lỗ mũi",
                "   - Thở bằng miệng",
                "   - Giữ nguyên 10-15 phút (đừng thả ra kiểm tra sớm!)",
                "3️⃣ **CHƯỜM LẠNH:**",
                "   - Đặt khăn lạnh lên sống mũi, gáy",
                "   - Giúp co mạch máu",
                "4️⃣ **SAU 15 PHÚT:**",
                "   - Thả tay, kiểm tra",
                "   - Nếu vẫn chảy: Bịt lại thêm 10 phút",
                "5️⃣ **KHÔNG NÓI, KHÔNG XỈ MŨI:**",
                "   - Trong 24 giờ sau",
                "   - Không cúi đầu, không gắng sức"
            ]
        },
        "severe": {
            "title": "🚨 Nếu NGHIÊM TRỌNG:",
            "steps": [
                "1️⃣ **GỌI 115 NGAY nếu:**",
                "   - Chảy máu >20 phút không cầm",
                "   - Chảy máu rất nhiều (ướt đẫm khăn)",
                "   - Cảm thấy choáng, chóng mặt",
                "   - Chảy máu sau chấn thương đầu",
                "2️⃣ **Trong khi chờ xe:**",
                "   - Tiếp tục bịt mũi",
                "   - Ngồi thẳng, không nằm",
                "   - Giữ bình tĩnh"
            ]
        },
        "prevention": {
            "title": "💡 Phòng ngừa:",
            "items": [
                "✅ Giữ ẩm mũi (bôi vaseline, xịt nước muối)",
                "✅ Tránh xỉ mũi mạnh",
                "✅ Tránh chấn thương mũi",
                "✅ Kiểm soát huyết áp (nếu tăng huyết áp)",
                "✅ Tránh không khí khô (dùng máy tạo ẩm)"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NGAY NẾU:",
            "items": [
                "⛔ Chảy máu >20 phút không cầm",
                "⛔ Chảy máu rất nhiều",
                "⛔ Choáng, chóng mặt, mất máu nhiều",
                "⛔ Chảy máu sau chấn thương đầu",
                "⛔ Chảy máu kèm huyết áp cao"
            ]
        },
        "transport_option": {
            "title": "🚗 Đưa đến bệnh viện:",
            "call_115_recommended": [
                "Chảy máu >20 phút không cầm",
                "Chảy máu rất nhiều, choáng váng",
                "Chảy máu sau chấn thương đầu",
                "Mất máu nhiều (da xanh, mạch nhanh)"
            ],
            "self_transport_allowed": [
                "Chảy máu đã cầm được sau khi bịt mũi",
                "Chảy máu nhẹ, không choáng",
                "Người bệnh tỉnh táo",
                "Bệnh viện gần (dưới 15-20 phút)",
                "Cần kiểm tra để đảm bảo an toàn"
            ],
            "self_transport_note": "💡 **Lưu ý:** Chảy máu cam nhẹ sau khi đã cầm được có thể tự đưa đến bệnh viện gần để kiểm tra. Nhưng nếu chảy nhiều hoặc không cầm → GỌI 115."
        }
    }
}

