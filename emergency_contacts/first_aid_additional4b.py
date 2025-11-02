"""
Sơ cứu Bổ Sung 4B - Ngất xỉu và Tăng/Tụt huyết áp khủng hoảng
Additional Emergency Situations 4B
"""

FIRST_AID_ADDITIONAL4B = {
    "syncope_fainting": {
        "name": "Ngất xỉu (Syncope)",
        "icon": "😵",
        "signs": {
            "title": "🔍 Dấu hiệu trước khi ngất:",
            "items": [
                "Chóng mặt, choáng váng",
                "Nhìn mờ, hoa mắt",
                "Đổ mồ hôi lạnh",
                "Buồn nôn",
                "Yếu người, chân tay run",
                "Sau đó: Mất ý thức tạm thời (vài giây đến vài phút)",
                "Tự tỉnh lại sau đó"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY:",
            "steps": [
                "1️⃣ **KHI THẤY DẤU HIỆU TRƯỚC KHI NGẤT:**",
                "   - NẰM XUỐNG hoặc NGỒI XỔM NGAY",
                "   - Nâng chân cao hơn đầu",
                "   - Giúp máu lưu thông lên não",
                "",
                "2️⃣ **KHI ĐÃ NGẤT:**",
                "   - Đặt nằm ngửa, nâng chân cao",
                "   - Nới lỏng quần áo (cổ, thắt lưng)",
                "   - Nghiêng đầu sang một bên (tránh sặc)",
                "   - KHÔNG cho uống nước khi chưa tỉnh hẳn",
                "",
                "3️⃣ **THEO DÕI:**",
                "   - Mạch, huyết áp",
                "   - Thở (có thở không?)",
                "   - Thời gian tỉnh lại",
                "",
                "4️⃣ **SAU KHI TỈNH:**",
                "   - Không cho ngồi dậy ngay",
                "   - Nghỉ ngơi ít nhất 15 phút",
                "   - Uống nước từ từ",
                "",
                "5️⃣ **GỌI 115 NẾU:**",
                "   - Ngất >2-3 phút không tỉnh",
                "   - Ngất nhiều lần",
                "   - Sau ngất: Đau ngực, khó thở, yếu liệt",
                "   - Ngất sau chấn thương đầu"
            ]
        },
        "common_causes": {
            "title": "💡 Nguyên nhân ngất xỉu:",
            "items": [
                "Đứng dậy đột ngột (huyết áp tụt)",
                "Lo lắng, sợ hãi (phản ứng thần kinh)",
                "Mất nước, đói",
                "Thuốc huyết áp (tụt huyết áp quá mức)",
                "Nhịp tim chậm hoặc nhanh bất thường",
                "Đau tim (thiếu máu tim)",
                "Đột quỵ (hiếm gặp)",
                "Người già: Thường do nhiều nguyên nhân kết hợp"
            ]
        },
        "prevention": {
            "title": "💡 Phòng ngừa ngất xỉu:",
            "items": [
                "✅ Đứng dậy từ từ (ngồi dậy → đợi vài giây → đứng)",
                "✅ Uống đủ nước (1.5-2L/ngày)",
                "✅ Ăn đủ bữa, không bỏ bữa",
                "✅ Tránh đứng lâu một chỗ",
                "✅ Đeo tất chân (giúp máu lưu thông)",
                "✅ Kiểm tra thuốc (một số thuốc gây tụt huyết áp)",
                "✅ Điều trị bệnh nền (huyết áp, tim mạch)"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NGAY NẾU:",
            "items": [
                "⛔ Ngất >2-3 phút không tỉnh",
                "⛔ Ngất nhiều lần trong ngày",
                "⛔ Sau ngất: Đau ngực, khó thở",
                "⛔ Sau ngất: Yếu liệt tay chân (nghi ngờ đột quỵ)",
                "⛔ Ngất sau chấn thương đầu",
                "⛔ Ngất khi vận động (nghi ngờ bệnh tim)",
                "⛔ Ngất kèm co giật"
            ]
        },
        "transport_option": {
            "title": "🚗 Đưa đến bệnh viện:",
            "call_115_recommended": [
                "Ngất >2-3 phút không tỉnh",
                "Ngất nhiều lần, ngất kèm đau ngực, khó thở",
                "Ngất sau chấn thương đầu",
                "Nghi ngờ bệnh tim, đột quỵ"
            ],
            "self_transport_allowed": [
                "Ngất nhẹ, đã tỉnh lại, không có triệu chứng nguy hiểm",
                "Người bệnh tỉnh táo, ổn định",
                "Bệnh viện gần (dưới 20 phút)",
                "Cần khám để tìm nguyên nhân"
            ],
            "self_transport_note": "💡 **Lưu ý:** Ngất xỉu có thể do nhiều nguyên nhân (từ nhẹ đến nguy hiểm). Nếu ngất nhẹ và đã tỉnh lại → Có thể tự đưa đến bệnh viện để khám. Nếu ngất nhiều lần hoặc có dấu hiệu nguy hiểm → GỌI 115."
        },
        "note": "⚠️ **Ngất xỉu thường không nguy hiểm nếu tỉnh lại nhanh, nhưng cần khám để tìm nguyên nhân (có thể là bệnh tim, huyết áp...)."
    },
    
    "hypertensive_crisis": {
        "name": "Tăng/Tụt huyết áp khủng hoảng",
        "icon": "📈📉",
        "signs": {
            "title": "🔍 Dấu hiệu huyết áp khủng hoảng:",
            "items": [
                "**TĂNG HUYẾT ÁP NẶNG:**",
                "   - Huyết áp >180/120 mmHg",
                "   - Đau đầu dữ dội",
                "   - Nhìn mờ",
                "   - Đau ngực, khó thở",
                "   - Buồn nôn, nôn",
                "",
                "**TỤT HUYẾT ÁP NẶNG:**",
                "   - Huyết áp <90/60 mmHg",
                "   - Chóng mặt, choáng váng",
                "   - Yếu người, mệt mỏi",
                "   - Đổ mồ hôi lạnh",
                "   - Lơ mơ, lú lẫn",
                "   - Có thể ngất xỉu"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY:",
            "steps": [
                "1️⃣ **GỌI 115 NGAY** - Huyết áp khủng hoảng có thể nguy hiểm!",
                "",
                "2️⃣ **TĂNG HUYẾT ÁP NẶNG (>180/120):**",
                "   - NẰM NGHỈ, giữ bình tĩnh",
                "   - KHÔNG uống thuốc hạ huyết áp mới (có thể tụt quá mức)",
                "   - Nếu đang uống thuốc → Uống liều thường ngày (không tự tăng liều)",
                "   - Theo dõi: Đau ngực, khó thở, đau đầu",
                "",
                "3️⃣ **TỤT HUYẾT ÁP NẶNG (<90/60):**",
                "   - NẰM XUỐNG, nâng chân cao",
                "   - Uống nước từ từ (nếu tỉnh táo)",
                "   - Không đứng dậy đột ngột",
                "   - Theo dõi: Mạch, ý thức",
                "",
                "4️⃣ **KHÔNG TỰ ĐIỀU CHỈNH THUỐC:**",
                "   - Không tự tăng/giảm liều thuốc huyết áp",
                "   - Để bác sĩ quyết định",
                "",
                "5️⃣ **CHUẨN BỊ THÔNG TIN:**",
                "   - Thuốc huyết áp đang uống",
                "   - Huyết áp đo được",
                "   - Triệu chứng hiện tại",
                "   - Bệnh nền khác (tim, thận, tiểu đường)"
            ]
        },
        "common_causes": {
            "title": "💡 Nguyên nhân huyết áp khủng hoảng:",
            "tăng": {
                "name": "Tăng huyết áp nặng:",
                "items": [
                    "Quên uống thuốc huyết áp",
                    "Stress, lo lắng",
                    "Dùng thuốc có muối (chống viêm)",
                    "Bệnh thận nặng",
                    "U tuyến thượng thận (hiếm)"
                ]
            },
            "tụt": {
                "name": "Tụt huyết áp nặng:",
                "items": [
                    "Uống thuốc huyết áp quá liều",
                    "Mất nước nặng (tiêu chảy, nôn)",
                    "Chảy máu (mất máu)",
                    "Nhiễm trùng nặng",
                    "Phản ứng với thuốc"
                ]
            }
        },
        "prevention": {
            "title": "💡 Phòng ngừa:",
            "items": [
                "✅ Uống thuốc huyết áp đúng giờ, đều đặn",
                "✅ Đo huyết áp thường xuyên (sáng, tối)",
                "✅ Ghi nhật ký huyết áp",
                "✅ Ăn ít muối (<5g/ngày)",
                "✅ Uống đủ nước (1.5-2L/ngày)",
                "✅ Tránh stress, lo lắng",
                "✅ Tái khám định kỳ, điều chỉnh thuốc khi cần",
                "✅ Không tự ý tăng/giảm liều thuốc"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NGAY NẾU:",
            "items": [
                "⛔ Tăng huyết áp >180/120 + Đau đầu dữ dội, đau ngực",
                "⛔ Tụt huyết áp <90/60 + Chóng mặt, ngất xỉu",
                "⛔ Huyết áp khủng hoảng + Đau ngực, khó thở",
                "⛔ Huyết áp khủng hoảng + Lơ mơ, lú lẫn",
                "⛔ Huyết áp khủng hoảng + Yếu liệt tay chân (nghi ngờ đột quỵ)"
            ]
        },
        "transport_option": {
            "title": "🚗 Đưa đến bệnh viện:",
            "call_115_recommended": [
                "Huyết áp khủng hoảng + Đau ngực, khó thở",
                "Huyết áp khủng hoảng + Lơ mơ, lú lẫn",
                "Huyết áp khủng hoảng + Nghi ngờ đột quỵ",
                "Tụt huyết áp nặng + Ngất xỉu"
            ],
            "self_transport_allowed": [
                "Huyết áp khủng hoảng nhưng ổn định, không có triệu chứng nguy hiểm",
                "Người bệnh tỉnh táo, ổn định",
                "Bệnh viện gần (dưới 20-30 phút)",
                "Cần khám để điều chỉnh thuốc"
            ],
            "self_transport_note": "⚠️ **Lưu ý:** Huyết áp khủng hoảng có thể dẫn đến đột quỵ, đau tim → Cần xử trí cẩn thận. Nếu có triệu chứng nguy hiểm → GỌI 115. Nếu chỉ tăng/tụt huyết áp mà ổn định → Có thể tự đưa đến bệnh viện để khám."
        },
        "note": "⚠️ **QUAN TRỌNG:** Huyết áp khủng hoảng (quá cao hoặc quá thấp) có thể gây đột quỵ, đau tim → Cần điều trị NGAY. Không tự ý điều chỉnh thuốc!"
    }
}

