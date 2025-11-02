"""
Sơ cứu Bổ Sung 3A - Hóc dị vật và Sốc nhiệt
Additional Emergency Situations 3A
"""

FIRST_AID_ADDITIONAL3A = {
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
    }
}

