"""
Sơ cứu Bổ Sung 2
Additional First Aid 2 (Chảy máu cam, Ngộ độc thực phẩm, Choking người lớn)
"""

FIRST_AID_ADDITIONAL2 = {
    "nosebleed": {
        "name": "Chảy máu cam",
        "icon": "🩸",
        "description": "Chảy máu từ mũi - Thường gặp, ít nguy hiểm nhưng cần xử lý đúng",
        "common_causes": {
            "title": "💡 Thường do:",
            "items": [
                "Không khí khô",
                "Ngoáy mũi",
                "Chấn thương nhẹ",
                "Cảm cúm, viêm mũi",
                "Tăng huyết áp (người già)",
                "Stress, mệt mỏi"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY:",
            "steps": [
                "1️⃣ **NGỒI DẬY, CÚI ĐẦU NHẸ** (KHÔNG ngửa đầu ra sau!)",
                "   - Mục đích: Máu chảy ra ngoài, không chảy xuống họng",
                "",
                "2️⃣ **BỊT MŨI** - Dùng ngón cái + ngón trỏ bóp chặt 2 cánh mũi",
                "   - Bóp đúng vị trí phần mũi mềm (dưới xương sống mũi)",
                "   - Bóp chặt, liên tục 10-15 phút",
                "",
                "3️⃣ **HÔ HẤP BẰNG MIỆNG** - Thở bằng miệng trong lúc bóp",
                "",
                "4️⃣ **CHƯỜM LẠNH:**",
                "   - Đặt túi đá hoặc khăn lạnh lên gốc mũi",
                "   - Giúp co mạch máu, cầm máu nhanh",
                "",
                "5️⃣ **SAU KHI CẦM MÁU:**",
                "   - Nằm nghỉ 30 phút, nhẹ nhàng",
                "   - Không ngoáy mũi, khạc nhổ trong 24h",
                "   - Không cúi đầu xuống thấp",
                "   - Không tập thể thao mạnh"
            ]
        },
        "dont": {
            "title": "❌ TUYỆT ĐỐI KHÔNG:",
            "items": [
                "❌ KHÔNG ngửa đầu ra sau (máu chảy xuống họng, dễ bị sặc!)",
                "❌ KHÔNG nằm ngửa (máu chảy xuống cổ họng)",
                "❌ KHÔNG bỏ tay ra xem sau vài phút (phải bóp đủ 10-15 phút)",
                "❌ KHÔNG nhét giấy/bông vào mũi (làm tổn thương thêm khi lấy ra)",
                "❌ KHÔNG ngoáy mũi, khạc nhổ sau khi cầm máu"
            ]
        },
        "prevention": {
            "title": "🛡️ PHÒNG NGỪA:",
            "items": [
                "Giữ ẩm không khí (dùng máy phun sương)",
                "Bôi kem vaseline vào trong mũi khi khô",
                "Tránh ngoáy mũi",
                "Xì mũi nhẹ nhàng khi cảm",
                "Kiểm soát huyết áp (nếu bị cao)",
                "Uống đủ nước"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NẾU:",
            "items": [
                "Chảy máu không cầm sau 20 phút bóp chặt",
                "Chảy máu rất nhiều, thành tia",
                "Mất nhiều máu (chóng mặt, choáng)",
                "Chảy máu sau chấn thương đầu/não",
                "Thường xuyên chảy máu cam > 3 lần/tuần",
                "Dùng thuốc chống đông (Warfarin, Aspirin)"
            ]
        },
        "note": "💡 **QUAN TRỌNG:** Phần lớn chảy máu cam tự cầm. Quan trọng là giữ bình tĩnh và bóp đúng cách!"
    },
    
    "choking_adult": {
        "name": "Người lớn hóc dị vật (Nghẹn)",
        "icon": "😮",
        "description": "Dị vật chẹn đường thở - Nguy hiểm, cần xử lý trong vòng vài phút!",
        "signs": {
            "title": "🔍 Dấu hiệu người lớn bị hóc:",
            "items": [
                "Không nói được, ho rất yếu",
                "Khó thở, thở khò khè",
                "Mặt đỏ/tím tái",
                "Đưa tay lên cổ (động tác phổ biến)",
                "Hoảng sợ, vật vã",
                "Mất ý thức (nếu nặng)"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY (Quy tắc Heimlich):",
            "steps": [
                "1️⃣ **HỎI: \"Bạn có bị nghẹn không?\"**",
                "   - Nếu gật đầu: Có dị vật",
                "   - Nếu nói được hoặc ho mạnh: Khuyến khích ho",
                "",
                "2️⃣ **ÉP BỤNG (Heimlich) NGAY:**",
                "   - Đứng sau người, vòng tay quanh eo",
                "   - Một tay nắm đấm, đặt trên rốn",
                "   - Tay kia nắm cổ tay",
                "   - Ấn MẠNH vào trong và LÊN TRÊN (như muốn nhấc người lên)",
                "   - Ấn 5 lần, kiểm tra xem dị vật ra chưa",
                "",
                "3️⃣ **NẾU VẪN CHƯA RA:**",
                "   - VỖ LƯNG 5 LẦN (giữa 2 xương bả vai)",
                "   - ÉP BỤNG 5 LẦN nữa",
                "   - Lặp lại cho đến khi dị vật ra",
                "",
                "4️⃣ **NẾU NGƯỜI NẰM:**",
                "   - Quì trên đùi người",
                "   - Đặt 2 tay lên bụng, ấn mạnh lên trên",
                "",
                "5️⃣ **NẾU NGƯỜI LỚN > 65 tuổi hoặc có thai:**",
                "   - Dùng 2 tay ép ngực (thay vì ép bụng)"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NGAY NẾU:",
            "items": [
                "Dị vật không ra sau nhiều lần ép",
                "Người tím tái, khó thở nhiều",
                "Mất ý thức",
                "Ngừng thở"
            ]
        },
        "if_unconscious": {
            "title": "💀 NẾU MẤT Ý THỨC:",
            "steps": [
                "1️⃣ GỌI 115",
                "2️⃣ Bắt đầu CPR (30 ép ngực + 2 thổi ngạt)",
                "3️⃣ Mỗi lần mở miệng làm hô hấp, kiểm tra xem có dị vật không",
                "4️⃣ Nếu thấy dị vật: Lấy ra",
                "5️⃣ Tiếp tục CPR đến khi xe cấp cứu đến"
            ]
        },
        "prevention": {
            "title": "🛡️ PHÒNG NGỪA:",
            "items": [
                "Nhai kỹ thức ăn trước khi nuốt",
                "Không vừa ăn vừa nói chuyện",
                "Không ăn khi đang vội vã",
                "Tránh rượu bia quá nhiều (giảm phản xạ)",
                "Thức ăn nhỏ, tròn: Cắt làm đôi",
                "Để răng giả lỏng ra khỏi miệng khi ăn"
            ]
        },
        "dont": {
            "title": "❌ TUYỆT ĐỐI KHÔNG:",
            "items": [
                "❌ KHÔNG vỗ lưng khi người đang đứng thẳng",
                "❌ KHÔNG cố móc tay vào miệng (đẩy sâu hơn)",
                "❌ KHÔNG cho uống nước khi đang nghẹn",
                "❌ KHÔNG bỏ cuộc - Tiếp tục ép cho đến khi dị vật ra"
            ]
        },
        "note": "⏱️ **QUAN TRỌNG:** Hóc dị vật có thể GÂY TỬ VONG trong 4-6 phút! Tốc độ là sinh mạng!"
    },
    
    "food_poisoning": {
        "name": "Ngộ độc thực phẩm",
        "icon": "🤢",
        "description": "Ăn thức ăn nhiễm khuẩn/độc tố → Tiêu chảy, nôn mửa",
        "signs": {
            "title": "🔍 Dấu hiệu:",
            "items": [
                "Đau bụng dữ dội, quặn thắt",
                "Nôn mửa nhiều lần",
                "Tiêu chảy (phân lỏng, nhiều nước)",
                "Sốt (có thể có)",
                "Ớn lạnh, mệt mỏi",
                "Chóng mặt (do mất nước)",
                "Xuất hiện 1-6 giờ sau khi ăn"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ:",
            "steps": [
                "1️⃣ **NGỪNG ĂN** - Để hệ tiêu hóa nghỉ",
                "2️⃣ **UỐNG NHIỀU NƯỚC** - Quan trọng nhất!",
                "   - Nước lọc, nước oresol (pha đúng cách)",
                "   - Uống từng ngụm nhỏ, thường xuyên",
                "   - Tránh mất nước nghiêm trọng",
                "",
                "3️⃣ **NẾU NGHIÊM TRỌNG:**",
                "   - Nôn mửa > 6 lần/ngày",
                "   - Tiêu chảy > 10 lần/ngày",
                "   - Sốt cao > 38.5°C",
                "   - Mất nước (khô miệng, ít tiểu)",
                "   → **GỌI 115 HOẶC ĐI BỆNH VIỆN NGAY**",
                "",
                "4️⃣ **KHÔNG uống thuốc:**",
                "   - KHÔNG uống cầm tiêu chảy (giữ độc tố trong cơ thể)",
                "   - KHÔNG uống kháng sinh tự ý (trừ khi bác sĩ chỉ định)",
                "",
                "5️⃣ **Rửa tay sạch** - Tránh lây cho người khác",
                "6️⃣ **Nghỉ ngơi** - Không làm việc nặng"
            ]
        },
        "what_to_eat": {
            "title": "🍲 NÊN ĂN SAU KHI ĐỠ:",
            "items": [
                "Cháo loãng (không thịt)",
                "Bánh mì khô",
                "Chuối",
                "Nước oresol",
                "Tránh sữa, đồ béo, cay, nóng trong 24-48h đầu"
            ]
        },
        "prevention": {
            "title": "🛡️ PHÒNG NGỪA:",
            "items": [
                "Rửa tay sạch trước khi ăn",
                "Ăn đồ nóng, nấu chín",
                "Tránh đồ sống (gỏi, sushi)",
                "Bảo quản thức ăn đúng cách (tủ lạnh)",
                "Kiểm tra hạn sử dụng",
                "Tránh thức ăn để quá 2 giờ ở nhiệt độ phòng",
                "Không ăn thức ăn có mùi vị lạ"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NẾU:",
            "items": [
                "Nôn mửa > 6 lần, tiêu chảy > 10 lần/ngày",
                "Sốt > 38.5°C",
                "Máu trong phân hoặc nôn",
                "Mất nước nghiêm trọng (khô miệng, ít tiểu, chóng mặt)",
                "Đau bụng dữ dội, không thuyên giảm",
                "Người già, trẻ em, phụ nữ có thai",
                "Người có bệnh mãn tính (tiểu đường, tim mạch)",
                "Bệnh kéo dài > 3 ngày không đỡ"
            ]
        },
        "foods_to_avoid": {
            "title": "🚫 MÓN HAY GÂY NGỘ ĐỘC:",
            "items": [
                "Gỏi, sushi, hải sản sống",
                "Thịt/chân gà nướng chưa chín",
                "Trứng sống, kem trứng",
                "Sữa chưa tiệt trùng",
                "Rau sống không rửa kỹ",
                "Thức ăn để lâu, ôi thiu"
            ]
        },
        "note": "💡 **LƯU Ý:** Ngộ độc thực phẩm thường tự khỏi sau 1-3 ngày. Quan trọng là UỐNG ĐỦ NƯỚC để tránh mất nước!"
    }
}

