"""
Sơ cứu Bổ Sung 3 - Các tình huống cấp cứu quan trọng
Additional Emergency Situations
"""

FIRST_AID_ADDITIONAL3 = {
    "choking_adult": {
        "name": "Hóc dị vật (Người lớn)",
        "icon": "😰",
        "signs": {
            "title": "🔍 Dấu hiệu hóc dị vật:",
            "items": [
                "Tay nắm cổ, không nói được",
                "Ho dữ dội, ho không hiệu quả",
                "Mặt đỏ, tím tái",
                "Không thở được, không nói được",
                "Nghiêm trọng: Ngất xỉu, bất tỉnh"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY (Heimlich Maneuver):",
            "steps": [
                "1️⃣ **HỎI:** 'Anh/Chị có bị hóc không?' (Nếu không trả lời = Hóc nặng)",
                "2️⃣ **VỖ LƯNG 5 lần:**",
                "   - Đứng sau, hỗ trợ ngực bằng tay trái",
                "   - Vỗ mạnh vào lưng (giữa 2 xương bả vai) 5 lần",
                "   - Kiểm tra xem dị vật có ra không",
                "3️⃣ **ÉP BỤNG (Heimlich) 5 lần:**",
                "   - Đứng sau, ôm người",
                "   - Tay nắm chặt, đặt trên rốn (dưới xương ức)",
                "   - Ép mạnh vào trong và lên trên 5 lần",
                "   - Mục đích: Tạo áp lực đẩy dị vật ra",
                "4️⃣ **LẶP LẠI:** Vỗ lưng 5 lần → Ép bụng 5 lần, cho đến khi dị vật ra hoặc ngất",
                "5️⃣ **NẾU NGẤT:**",
                "   - GỌI 115 NGAY",
                "   - Bắt đầu CPR (hồi sức tim phổi)"
            ]
        },
        "self_help": {
            "title": "🆘 Nếu chỉ có 1 mình:",
            "steps": [
                "1️⃣ **Tự ÉP BỤNG:**",
                "   - Đặt nắm tay lên rốn",
                "   - Tay kia nắm tay, ép mạnh vào trong và lên trên",
                "   - Hoặc ép vào thành ghế, bàn",
                "2️⃣ **GỌI 115 NGAY**"
            ]
        },
        "prevention": {
            "title": "💡 Phòng ngừa:",
            "items": [
                "✅ Nhai kỹ thức ăn trước khi nuốt",
                "✅ Không nói chuyện khi đang ăn",
                "✅ Cắt nhỏ thức ăn (đặc biệt người già)",
                "✅ Tránh ăn khi đang nằm",
                "✅ Cẩn thận với thạch, kẹo cứng, xương cá"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NGAY NẾU:",
            "items": [
                "⛔ Không thể thở, không nói được",
                "⛔ Mặt tím tái, ngất xỉu",
                "⛔ Heimlich không hiệu quả sau nhiều lần",
                "⛔ Sau khi lấy được dị vật nhưng vẫn khó thở"
            ]
        },
        "note": "⏱️ **THỜI GIAN:** Chỉ có vài phút trước khi thiếu oxy → Hành động NHANH!"
    },
    
    "heat_stroke": {
        "name": "Sốc nhiệt/Cảm nắng",
        "icon": "☀️",
        "signs": {
            "title": "🔍 Dấu hiệu sốc nhiệt:",
            "items": [
                "Nhiệt độ cơ thể >40°C (rất nóng khi sờ)",
                "Da đỏ, nóng, khô (KHÔNG ra mồ hôi!)",
                "Đau đầu dữ dội",
                "Chóng mặt, buồn nôn, nôn",
                "Mạch nhanh, thở nhanh",
                "Lơ mơ, lú lẫn, có thể co giật",
                "Nghiêm trọng: Hôn mê"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY (Hạ nhiệt càng nhanh càng tốt!):",
            "steps": [
                "1️⃣ **GỌI 115 NGAY** - Sốc nhiệt nguy hiểm tính mạng!",
                "2️⃣ **ĐƯA VÀO NƠI MÁT:**",
                "   - Vào trong nhà, có điều hòa",
                "   - Hoặc bóng râm, thông thoáng",
                "3️⃣ **HẠ NHIỆT NGAY:**",
                "   - Cởi bỏ quần áo",
                "   - Dội nước lạnh (không đá lạnh) lên người",
                "   - Quạt để tăng bay hơi",
                "   - Đặt khăn ướt lạnh ở cổ, nách, bẹn",
                "4️⃣ **ĐỂ NẰM:** Chân cao hơn đầu (nếu có)",
                "5️⃣ **KHÔNG cho uống nước** nếu lơ mơ (có thể sặc)",
                "6️⃣ **Theo dõi:** Nhiệt độ, mạch, ý thức"
            ]
        },
        "vs_heat_exhaustion": {
            "title": "🔍 Phân biệt: Say nắng nhẹ vs Sốc nhiệt:",
            "heat_exhaustion": {
                "name": "Say nắng nhẹ (Heat Exhaustion):",
                "symptoms": [
                    "Da ướt, ra mồ hôi nhiều",
                    "Mệt mỏi, yếu",
                    "Chóng mặt, buồn nôn",
                    "Nhiệt độ <40°C"
                ],
                "action": "Nghỉ mát, uống nước, tự khỏi"
            },
            "heat_stroke": {
                "name": "Sốc nhiệt (Heat Stroke):",
                "symptoms": [
                    "Da KHÔNG ra mồ hôi (KHÔ), đỏ, nóng",
                    "Nhiệt độ >40°C",
                    "Lơ mơ, co giật, hôn mê"
                ],
                "action": "🚨 GỌI 115 NGAY - Nguy hiểm tính mạng!"
            }
        },
        "prevention": {
            "title": "💡 Phòng ngừa sốc nhiệt:",
            "items": [
                "✅ Uống nhiều nước (2-3L/ngày khi nóng)",
                "✅ Tránh ra ngoài giờ nắng gắt (10h-16h)",
                "✅ Mặc quần áo rộng, sáng màu, thấm mồ hôi",
                "✅ Đội mũ rộng vành, đeo kính râm",
                "✅ Nghỉ ngơi thường xuyên khi làm việc ngoài trời",
                "✅ Tránh uống rượu bia (gây mất nước)",
                "✅ Người già, trẻ em dễ bị → Cẩn thận đặc biệt"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NGAY NẾU:",
            "items": [
                "⛔ Nhiệt độ >40°C, da khô không ra mồ hôi",
                "⛔ Lơ mơ, co giật, hôn mê",
                "⛔ Nôn nhiều, không uống được nước",
                "⛔ Mạch nhanh >120/phút, khó thở"
            ]
        },
        "note": "⚠️ **Sốc nhiệt:** Tỷ lệ tử vong 50-70% nếu không điều trị → Phải hạ nhiệt NGAY!"
    },
    
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
    },
    
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

