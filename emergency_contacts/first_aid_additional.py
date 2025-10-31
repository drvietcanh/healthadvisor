"""
Sơ cứu Bổ Sung
Additional First Aid (Sốc phản vệ, Co giật, Hôn mê, Ngộ độc rượu, Gãy xương)
"""

FIRST_AID_ADDITIONAL = {
    "anaphylaxis": {
        "name": "Sốc phản vệ",
        "icon": "⚡",
        "description": "Phản ứng dị ứng NGHIÊM TRỌNG, có thể CHẾT trong vài phút!",
        "signs": {
            "title": "🔍 Dấu hiệu (xuất hiện trong 5-30 phút):",
            "items": [
                "Khó thở, thở khò khè",
                "Sưng môi, lưỡi, mặt, cổ họng",
                "Phát ban, mẩn đỏ khắp người",
                "Ngứa dữ dội",
                "Mạch nhanh, huyết áp tụt",
                "Chóng mặt, ngất xỉu",
                "Buồn nôn, nôn"
            ]
        },
        "common_triggers": {
            "title": "💡 Thường do:",
            "items": [
                "Thức ăn: Đậu phộng, hải sản, trứng, sữa",
                "Thuốc: Penicillin, Aspirin",
                "Côn trùng đốt: Ong, kiến",
                "Latex (cao su)"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ KHẨN CẤP:",
            "steps": [
                "1️⃣ **GỌI 115 NGAY LẬP TỨC!** (Không chờ đợi!)",
                "2️⃣ **Nếu có EpiPen (Adrenalin tự tiêm):**",
                "   - Tiêm NGAY vào đùi (xuyên qua quần)",
                "   - Giữ 3-10 giây",
                "   - Nếu cần, tiêm mũi 2 sau 5-15 phút",
                "3️⃣ **Đặt nằm, nâng chân cao** (nếu không khó thở)",
                "4️⃣ **Nếu có → Thở oxy**",
                "5️⃣ **Theo dõi hô hấp, mạch**",
                "6️⃣ **Nếu ngừng thở → Hồi sức tim phổi (CPR)**"
            ]
        },
        "prevention": {
            "title": "💡 Phòng ngừa:",
            "items": [
                "Biết rõ dị ứng của mình",
                "Mang theo EpiPen nếu từng bị",
                "Đeo vòng tay cảnh báo dị ứng",
                "Tránh thức ăn/thuốc gây dị ứng",
                "Đọc nhãn thực phẩm cẩn thận"
            ]
        },
        "note": "⚠️ Sốc phản vệ = TÌNH TRẠNG KHẨN CẤP! Mỗi giây đều quý giá!"
    },
    
    "seizure": {
        "name": "Co giật (Động kinh)",
        "icon": "⚡",
        "signs": {
            "title": "🔍 Dấu hiệu:",
            "items": [
                "Co cứng toàn thân",
                "Giật tay, chân",
                "Sùi bọt mép",
                "Mắt trợn ngược",
                "Mất ý thức",
                "Sau đó: Lơ mơ, ngủ gà"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ:",
            "steps": [
                "1️⃣ **Giữ BÌNH TĨNH**",
                "2️⃣ **Đỡ người nằm xuống** - Tránh va đập",
                "3️⃣ **Đặt gối dưới đầu**",
                "4️⃣ **Nghiêng người sang một bên** - Tránh sặc",
                "5️⃣ **Nới lỏng quần áo** (cổ áo, thắt lưng)",
                "6️⃣ **KHÔNG cho bất cứ gì vào miệng** (không khăn, không que)",
                "7️⃣ **Ghi nhớ thời gian** co giật",
                "8️⃣ **Theo dõi hô hấp**"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NẾU:",
            "items": [
                "Co giật >5 phút",
                "Lần co giật thứ 2 ngay sau lần đầu",
                "Ngừng thở sau khi hết co giật",
                "Chấn thương trong lúc co giật",
                "Lần đầu tiên bị co giật",
                "Người có thai/tiểu đường"
            ]
        },
        "after_seizure": {
            "title": "💡 Sau khi hết co giật:",
            "steps": [
                "Để người nằm nghiêng",
                "Lau sạch nước bọt, sùi bọt",
                "Nói chuyện nhẹ nhàng, an ủi",
                "Đợi người tỉnh táo hoàn toàn",
                "Không cho ăn/uống ngay"
            ]
        },
        "dont": {
            "title": "❌ TUYỆT ĐỐI KHÔNG:",
            "items": [
                "❌ KHÔNG giữ chặt người",
                "❌ KHÔNG cho bất cứ gì vào miệng",
                "❌ KHÔNG cố ép ngừng co giật",
                "❌ KHÔNG cho uống thuốc khi đang co giật"
            ]
        }
    },
    
    "unconscious": {
        "name": "Hôn mê/Bất tỉnh",
        "icon": "😴",
        "signs": {
            "title": "🔍 Dấu hiệu:",
            "items": [
                "Không phản ứng khi gọi, lay",
                "Mắt nhắm, không mở",
                "Thở chậm hoặc không đều",
                "Mạch yếu hoặc không bắt được"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ:",
            "steps": [
                "1️⃣ **GỌI 115 NGAY**",
                "2️⃣ **Kiểm tra: Có thở không?**",
                "   - Đặt tay lên ngực",
                "   - Quan sát ngực di động",
                "   - Đặt má gần mũi nghe hơi thở",
                "3️⃣ **Nếu CÓ THỞ:**",
                "   - Đặt nằm nghiêng (tư thế phục hồi)",
                "   - Nâng đầu nhẹ",
                "   - Theo dõi hô hấp, mạch",
                "4️⃣ **Nếu KHÔNG THỞ:**",
                "   - Bắt đầu Hồi sức tim phổi (CPR) ngay",
                "   - 30 lần ép ngực + 2 lần thổi ngạt",
                "   - Tiếp tục cho đến khi xe cấp cứu đến"
            ]
        },
        "recovery_position": {
            "title": "📐 Tư thế phục hồi (nếu có thở):",
            "steps": [
                "Nằm nghiêng sang một bên",
                "Đầu nghiêng ra sau, cằm nâng lên",
                "Tay trên gập, khuỷu tay 90 độ",
                "Chân trên gập đầu gối",
                "Giữ tư thế này"
            ]
        },
        "possible_causes": {
            "title": "💡 Có thể do:",
            "items": [
                "Ngất xỉu (tạm thời)",
                "Đột quỵ",
                "Đau tim",
                "Hạ đường huyết",
                "Ngộ độc",
                "Chấn thương đầu",
                "Sốc"
            ]
        },
        "note": "⚠️ Hôn mê = Nghiêm trọng! Luôn gọi 115!"
    },
    
    "alcohol_poisoning": {
        "name": "Ngộ độc rượu",
        "icon": "🍺",
        "description": "Rượu quá nhiều → Ức chế thần kinh trung ương → Nguy hiểm!",
        "signs": {
            "title": "🔍 Dấu hiệu:",
            "items": [
                "Lơ mơ, không tỉnh táo",
                "Khó đánh thức",
                "Thở chậm, không đều (<8 lần/phút)",
                "Da lạnh, ẩm, tím",
                "Nôn nhiều",
                "Hạ thân nhiệt",
                "Có thể ngừng thở, tử vong"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ:",
            "steps": [
                "1️⃣ **GỌI 115 NGAY** (Đặc biệt nếu thở chậm!)",
                "2️⃣ **Nếu có thở:**",
                "   - Đặt nằm nghiêng (tránh sặc nôn)",
                "   - Giữ ấm (đắp chăn)",
                "   - Theo dõi hô hấp, mạch",
                "3️⃣ **Nếu KHÔNG thở:**",
                "   - Bắt đầu CPR ngay",
                "4️⃣ **KHÔNG cho uống cà phê/đường** - Không giúp!",
                "5️⃣ **KHÔNG để ngủ một mình** - Có thể ngừng thở!",
                "6️⃣ **Đợi xe cấp cứu**"
            ]
        },
        "prevention": {
            "title": "💡 Phòng ngừa:",
            "items": [
                "Uống chậm, từ từ",
                "Không uống khi đói",
                "Uống nước xen kẽ",
                "Biết giới hạn của mình",
                "Không lái xe sau khi uống"
            ]
        },
        "warning": "⚠️ Ngộ độc rượu có thể CHẾT! Không xem thường!"
    },
    
    "fracture": {
        "name": "Gãy xương",
        "icon": "🦴",
        "signs": {
            "title": "🔍 Dấu hiệu:",
            "items": [
                "Đau dữ dội tại vị trí chấn thương",
                "Sưng, bầm tím",
                "Biến dạng (xương lệch, cong)",
                "Không cử động được",
                "Có thể nghe tiếng rắc (khi bị chấn thương)",
                "Có thể nhìn thấy xương lòi ra (gãy hở)"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ:",
            "steps": [
                "1️⃣ **GỌI 115** (Nếu nghiêm trọng, không di chuyển được)",
                "2️⃣ **CẦM MÁU** (nếu có chảy máu):",
                "   - Băng ép, không ép trực tiếp lên xương gãy",
                "3️⃣ **BẤT ĐỘNG (Không di chuyển):**",
                "   - Giữ nguyên tư thế",
                "   - KHÔNG cố nắn xương",
                "   - Nẹp nếu có (băng vào chân/tay lành bên cạnh)",
                "4️⃣ **CHƯỜM LẠNH:**",
                "   - Đá lạnh (bọc khăn) chườm 15-20 phút",
                "   - Giảm sưng, đau",
                "5️⃣ **NẾU GÃY HỞ (xương lòi ra):**",
                "   - KHÔNG đẩy xương vào",
                "   - Che bằng gạc sạch, ẩm",
                "   - Cầm máu nhẹ",
                "6️⃣ **Vận chuyển cẩn thận**",
                "7️⃣ **Theo dõi:**",
                "   - Tê, tái, lạnh (có thể chèn ép mạch máu)",
                "   - Sưng tăng nhanh"
            ]
        },
        "splinting": {
            "title": "📐 Cách nẹp tạm:",
            "methods": [
                "Dùng chân/tay lành làm nẹp",
                "Dùng bảng, gậy, chăn cuộn",
                "Băng cố định, KHÔNG quá chặt",
                "Giữ cả 2 khớp trên và dưới chỗ gãy"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NẾU:",
            "items": [
                "Gãy hở (xương lòi ra)",
                "Gãy cột sống, cổ (KHÔNG di chuyển!)",
                "Gãy xương chậu, đùi",
                "Nhiều vị trí gãy",
                "Chảy máu nhiều",
                "Không cảm giác, không cử động được"
            ]
        },
        "dont": {
            "title": "❌ TUYỆT ĐỐI KHÔNG:",
            "items": [
                "❌ KHÔNG nắn/cố sửa xương",
                "❌ KHÔNG cho ăn/uống (có thể cần phẫu thuật)",
                "❌ KHÔNG băng quá chặt",
                "❌ KHÔNG di chuyển nếu gãy cột sống"
            ]
        },
        "note": "💡 Nếu gãy xương cổ/cột sống → KHÔNG di chuyển! Đợi nhân viên y tế!"
    }
}

