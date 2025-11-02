"""
Sơ cứu Bổ Sung 3C - Đau bụng cấp, Chấn thương đầu, Rắn cắn, Ngộ độc thực phẩm
Additional Emergency Situations 3C
"""

FIRST_AID_ADDITIONAL3C = {
    "acute_abdominal_pain": {
        "name": "Đau bụng cấp",
        "icon": "😣",
        "signs": {
            "title": "🔍 Dấu hiệu đau bụng nguy hiểm:",
            "items": [
                "Đau bụng dữ dội, đột ngột",
                "Đau bụng kèm sốt cao",
                "Đau bụng kèm nôn ra máu, đi ngoài phân đen",
                "Đau bụng kèm cứng bụng (bụng căng, cứng như gỗ)",
                "Đau bụng không đi tiểu được",
                "Choáng, mạch nhanh, huyết áp tụt"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY:",
            "steps": [
                "1️⃣ **GỌI 115 NGAY nếu có dấu hiệu nguy hiểm**",
                "2️⃣ **NẰM NGHỈ**, không ăn uống",
                "3️⃣ **KHÔNG uống thuốc giảm đau** (che giấu triệu chứng, khó chẩn đoán)",
                "4️⃣ **KHÔNG chườm nóng** (có thể làm viêm ruột thừa vỡ)",
                "5️⃣ **Ghi lại:**",
                "   - Vị trí đau (bụng trên, dưới, phải, trái)",
                "   - Tính chất đau (quặn, âm ỉ, như dao đâm)",
                "   - Kèm theo (nôn, sốt, tiêu chảy)"
            ]
        },
        "dangerous_causes": {
            "title": "⚠️ Các nguyên nhân nguy hiểm:",
            "causes": [
                "Viêm ruột thừa (đau bụng dưới phải, sốt)",
                "Thủng dạ dày/tá tràng (đau bụng trên dữ dội, cứng bụng)",
                "Tắc ruột (đau quặn, nôn, không đi ngoài được)",
                "Viêm tụy cấp (đau bụng trên, lan ra lưng)",
                "Thai ngoài tử cung vỡ (phụ nữ, đau bụng dưới một bên)"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NGAY NẾU:",
            "items": [
                "⛔ Đau bụng dữ dội, đột ngột",
                "⛔ Đau bụng + Sốt cao >38.5°C",
                "⛔ Đau bụng + Nôn ra máu, đi ngoài phân đen",
                "⛔ Đau bụng + Cứng bụng (bụng cứng như gỗ)",
                "⛔ Đau bụng + Choáng, mạch nhanh",
                "⛔ Đau bụng + Không đi tiểu được >12 giờ"
            ]
        },
        "transport_option": {
            "title": "🚗 Đưa đến bệnh viện:",
            "call_115_recommended": [
                "Đau bụng dữ dội, đột ngột",
                "Đau bụng + Sốt cao, cứng bụng",
                "Đau bụng + Nôn ra máu, đi ngoài phân đen",
                "Đau bụng + Choáng, mạch nhanh",
                "Nghi ngờ viêm ruột thừa, thủng dạ dày"
            ],
            "self_transport_allowed": [
                "Đau bụng vừa, có thể chịu được",
                "Không sốt cao, không cứng bụng",
                "Người bệnh tỉnh táo, không choáng",
                "Bệnh viện gần (dưới 20-30 phút)",
                "Cần khám để chẩn đoán chính xác"
            ],
            "self_transport_note": "⚠️ **Lưu ý:** Đau bụng có thể do nhiều nguyên nhân nguy hiểm (viêm ruột thừa, thủng dạ dày...). Nếu đau nhiều hoặc có dấu hiệu nguy hiểm → GỌI 115. Nếu chỉ đau vừa và không có dấu hiệu nguy hiểm → Có thể tự đưa đến bệnh viện gần để khám."
        },
        "note": "⚠️ Đau bụng cấp có thể do nhiều nguyên nhân nguy hiểm → Cần khám ngay!"
    },
    
    "head_injury": {
        "name": "Chấn thương đầu",
        "icon": "🤕",
        "signs": {
            "title": "🔍 Dấu hiệu nguy hiểm:",
            "items": [
                "Ngất xỉu, bất tỉnh (dù chỉ vài giây)",
                "Lơ mơ, không tỉnh táo",
                "Nôn nhiều lần",
                "Đau đầu dữ dội, tăng dần",
                "Chảy máu mũi, tai (dịch não tủy)",
                "Đồng tử không đều (một mắt to, một mắt nhỏ)",
                "Co giật",
                "Yếu liệt tay chân",
                "Lú lẫn, không nhớ việc xảy ra"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY:",
            "steps": [
                "1️⃣ **GỌI 115 NGAY nếu có dấu hiệu nguy hiểm**",
                "2️⃣ **GIỮ ĐẦU VÀ CỔ THẲNG:**",
                "   - Không di chuyển đầu",
                "   - Có thể có chấn thương cột sống cổ",
                "3️⃣ **NẰM NGHỈ**, nâng đầu nhẹ (nếu không nghi ngờ chấn thương cổ)",
                "4️⃣ **KHÔNG cho uống nước, thuốc**",
                "5️⃣ **Chườm lạnh** vết sưng (nếu có)",
                "6️⃣ **Theo dõi:** Ý thức, thở, mạch"
            ]
        },
        "observations": {
            "title": "📊 Theo dõi 24-48 giờ (ngay cả khi nhẹ):",
            "items": [
                "Kiểm tra mỗi 2-3 giờ:",
                "  - Tỉnh táo? (Gọi tên, trả lời câu hỏi)",
                "  - Đồng tử đều? (2 mắt bằng nhau)",
                "  - Có nôn không?",
                "  - Đau đầu tăng hay giảm?",
                "⚠️ Nếu bất kỳ dấu hiệu xấu đi → GỌI 115 NGAY!"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NGAY NẾU:",
            "items": [
                "⛔ Ngất xỉu, bất tỉnh (dù chỉ vài giây)",
                "⛔ Lơ mơ, không tỉnh táo",
                "⛔ Nôn nhiều lần",
                "⛔ Đau đầu dữ dội, tăng dần",
                "⛔ Chảy máu mũi, tai",
                "⛔ Đồng tử không đều",
                "⛔ Co giật",
                "⛔ Yếu liệt tay chân"
            ]
        },
        "note": "⚠️ Chấn thương đầu có thể gây chảy máu trong não → Nguy hiểm tính mạng!"
    },
    
    "snake_bite": {
        "name": "Rắn cắn",
        "icon": "🐍",
        "signs": {
            "title": "🔍 Dấu hiệu rắn độc cắn:",
            "items": [
                "Vết cắn có 2 răng nanh (2 chấm)",
                "Đau, sưng tại vết cắn",
                "Tím tái, hoại tử quanh vết cắn",
                "Nôn, đau bụng",
                "Chóng mặt, yếu người",
                "Khó thở (nếu rắn độc mạnh)",
                "Rối loạn đông máu (chảy máu)"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY:",
            "steps": [
                "1️⃣ **GỌI 115 NGAY** - Hoặc đưa đến bệnh viện có huyết thanh kháng nọc",
                "2️⃣ **GIỮ BÌNH TĨNH**, không hoảng loạn",
                "3️⃣ **BẤT ĐỘNG chi bị cắn:**",
                "   - NẰM YÊN, không di chuyển",
                "   - Buộc nhẹ phía trên vết cắn (không quá chặt!)",
                "   - Chi thấp hơn tim",
                "4️⃣ **RỬA SẠCH vết cắn** bằng nước sạch",
                "5️⃣ **BĂNG BẤT ĐỘNG (Immobilize):**",
                "   - Băng chặt từ đầu chi đến gốc chi",
                "   - Giữ nguyên không cử động",
                "6️⃣ **Ghi nhớ hình dạng rắn** (chụp ảnh nếu an toàn) để bác sĩ xác định",
                "7️⃣ **KHÔNG:**",
                "   - Chích máu, rạch vết cắn",
                "   - Hút máu bằng miệng",
                "   - Buộc quá chặt (cắt đứt máu)",
                "   - Uống rượu (làm loãng máu → Chảy máu thêm)"
            ]
        },
        "hospitals": {
            "title": "🏥 Bệnh viện có huyết thanh kháng nọc:",
            "vietnam": [
                "Viện Pasteur TP.HCM",
                "Bệnh viện Chợ Rẫy (TP.HCM)",
                "Bệnh viện Nhiệt Đới (TP.HCM)",
                "Bệnh viện Bạch Mai (Hà Nội)",
                "Bệnh viện Nhiệt Đới Trung ương (Hà Nội)"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NGAY:",
            "items": [
                "⛔ BẤT KỲ trường hợp rắn cắn nào (kể cả không rõ có độc)",
                "⛔ Vết cắn sưng, đau",
                "⛔ Nôn, chóng mặt",
                "⛔ Khó thở"
            ]
        },
        "transport_option": {
            "title": "🚗 Đưa đến bệnh viện:",
            "call_115_recommended": [
                "Rắn độc cắn (có dấu hiệu độc)",
                "Vết cắn sưng nhiều, đau dữ dội",
                "Nôn, chóng mặt, khó thở",
                "Xa bệnh viện có huyết thanh kháng nọc"
            ],
            "self_transport_allowed": [
                "Rắn cắn (dù chưa rõ có độc)",
                "Đã sơ cứu tốt (bất động chi, băng bó)",
                "Người bệnh tỉnh táo, ổn định",
                "Bệnh viện có huyết thanh kháng nọc gần (dưới 30 phút)",
                "Cần tiêm huyết thanh kháng nọc càng sớm càng tốt"
            ],
            "self_transport_note": "⚠️ **QUAN TRỌNG:** Rắn cắn cần đến bệnh viện có huyết thanh kháng nọc. Nếu bệnh viện gần và có người nhà đưa đi nhanh → Có thể tự đưa đi (tiết kiệm thời gian). Nếu xa hoặc không chắc → GỌI 115. Huyết thanh cần tiêm trong 4 giờ đầu!"
        },
        "note": "⏱️ **QUAN TRỌNG:** Huyết thanh kháng nọc cần tiêm càng sớm càng tốt (trong 4 giờ đầu tốt nhất)!"
    },
    
    "food_poisoning": {
        "name": "Ngộ độc thực phẩm",
        "icon": "🍽️",
        "signs": {
            "title": "🔍 Dấu hiệu:",
            "items": [
                "Nôn mửa, buồn nôn",
                "Tiêu chảy (có thể có máu)",
                "Đau bụng quặn",
                "Sốt",
                "Chóng mặt, yếu người",
                "Mất nước (khát, không đi tiểu)"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ:",
            "steps": [
                "1️⃣ **UỐNG NHIỀU NƯỚC:**",
                "   - Nước oresol (bù điện giải)",
                "   - Nước lọc",
                "   - Uống từng ngụm nhỏ, thường xuyên",
                "2️⃣ **NGHỈ NGƠI**, không ăn trong 4-6 giờ đầu",
                "3️⃣ **Theo dõi:** Triệu chứng, số lần đi ngoài, nôn"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NGAY NẾU:",
            "items": [
                "⛔ Nôn, tiêu chảy nhiều → Mất nước nặng",
                "⛔ Sốt cao >38.5°C",
                "⛔ Tiêu chảy có máu",
                "⛔ Đau bụng dữ dội",
                "⛔ Không đi tiểu được >12 giờ",
                "⛔ Choáng, lơ mơ",
                "⛔ Người già, trẻ em (dễ mất nước nặng)"
            ]
        },
        "prevention": {
            "title": "💡 Phòng ngừa:",
            "items": [
                "✅ Ăn chín, uống sôi",
                "✅ Bảo quản thực phẩm đúng cách (tủ lạnh)",
                "✅ Rửa tay trước khi ăn",
                "✅ Tránh thức ăn để lâu, có mùi lạ",
                "✅ Tránh thịt, cá sống"
            ]
        },
        "transport_option": {
            "title": "🚗 Đưa đến bệnh viện:",
            "call_115_recommended": [
                "Nôn, tiêu chảy nhiều → Mất nước nặng, choáng",
                "Sốt cao >38.5°C, tiêu chảy có máu",
                "Đau bụng dữ dội, không đi tiểu >12 giờ",
                "Người già, trẻ em (dễ mất nước nặng)"
            ],
            "self_transport_allowed": [
                "Nôn, tiêu chảy vừa, chưa mất nước nặng",
                "Người bệnh tỉnh táo, có thể uống nước",
                "Không sốt cao, không có máu trong phân",
                "Bệnh viện gần (dưới 20-30 phút)",
                "Cần truyền dịch để bù nước"
            ],
            "self_transport_note": "💡 **Lưu ý:** Ngộ độc thực phẩm nhẹ có thể tự đưa đến bệnh viện gần để truyền dịch bù nước. Nếu nặng (mất nước nhiều, choáng) → GỌI 115."
        }
    }
}

