"""
Sơ cứu Bổ Sung 4A - Ngã không đứng dậy, Lú lẫn đột ngột, Khó thở đột ngột
Additional Emergency Situations 4A
"""

FIRST_AID_ADDITIONAL4A = {
    "fall_unable_to_get_up": {
        "name": "Ngã và không đứng dậy được (Người già)",
        "icon": "🦽",
        "signs": {
            "title": "🔍 Dấu hiệu ngã nguy hiểm:",
            "items": [
                "Ngã và không tự đứng dậy được",
                "Đau dữ dội khi cử động (có thể gãy xương)",
                "Chảy máu (từ đầu hoặc vết thương)",
                "Không phản ứng, lơ mơ sau khi ngã",
                "Đau cổ, lưng (nghi ngờ chấn thương cột sống)",
                "Đau hông, xương chậu (thường gãy ở người già)"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY:",
            "steps": [
                "1️⃣ **KHÔNG DI CHUYỂN NGAY** nếu:",
                "   - Nghi ngờ gãy xương (đau dữ dội, không cử động được)",
                "   - Nghi ngờ chấn thương cổ/lưng",
                "   - Không tỉnh táo sau khi ngã",
                "",
                "2️⃣ **GỌI 115 NGAY nếu:**",
                "   - Không thể tự đứng dậy",
                "   - Đau dữ dội, nghi ngờ gãy xương",
                "   - Chảy máu nhiều",
                "   - Không tỉnh táo, lơ mơ",
                "",
                "3️⃣ **NẾU NGÃ NHẸ (tỉnh táo, chỉ đau nhẹ):**",
                "   - Hỗ trợ từ từ đứng dậy",
                "   - Nghỉ ngơi, chườm lạnh vết đau",
                "   - Theo dõi 24-48 giờ",
                "",
                "4️⃣ **TRONG KHI CHỜ XE CẤP CỨU:**",
                "   - Giữ nguyên tư thế, không di chuyển",
                "   - Chườm lạnh vết đau (nếu có)",
                "   - Giữ ấm, đắp chăn",
                "   - An ủi, giữ bình tĩnh",
                "   - Không cho uống nước/thuốc nếu không tỉnh táo"
            ]
        },
        "common_causes": {
            "title": "💡 Người già hay ngã do:",
            "items": [
                "Chóng mặt, huyết áp thấp (đứng dậy đột ngột)",
                "Yếu cơ, loãng xương (xương dễ gãy)",
                "Thuốc gây chóng mặt (huyết áp, an thần)",
                "Sàn nhà trơn, tối",
                "Vật cản (dây điện, thảm)",
                "Đi đứng không vững, yếu chân"
            ]
        },
        "prevention": {
            "title": "💡 Phòng ngừa ngã:",
            "items": [
                "✅ Đứng dậy từ từ, không vội vã",
                "✅ Bật đèn khi đi đêm",
                "✅ Giữ sàn nhà khô, không trơn",
                "✅ Dỡ bỏ thảm, dây điện gây vấp",
                "✅ Dùng gậy chống nếu cần",
                "✅ Mang giày dép chắc chắn, không trơn",
                "✅ Lắp tay vịn ở cầu thang, nhà tắm",
                "✅ Tập thể dục nhẹ để tăng sức mạnh cơ"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NGAY NẾU:",
            "items": [
                "⛔ Ngã và không thể tự đứng dậy",
                "⛔ Đau dữ dội, nghi ngờ gãy xương",
                "⛔ Chảy máu nhiều từ vết thương",
                "⛔ Không tỉnh táo sau khi ngã",
                "⛔ Đau cổ, lưng (nghi ngờ chấn thương cột sống)",
                "⛔ Đau hông, không cử động được chân (gãy xương chậu)"
            ]
        },
        "transport_option": {
            "title": "🚗 Đưa đến bệnh viện:",
            "call_115_recommended": [
                "Ngã và không thể tự đứng dậy",
                "Nghi ngờ gãy xương (đau dữ dội, không cử động được)",
                "Chảy máu nhiều, không tỉnh táo",
                "Nghi ngờ chấn thương cột sống",
                "Cần vận chuyển an toàn, không làm tổn thương thêm"
            ],
            "self_transport_allowed": [
                "Ngã nhẹ, tỉnh táo, có thể đứng dậy",
                "Đau nhẹ, không nghi ngờ gãy xương",
                "Không chảy máu, không lơ mơ",
                "Bệnh viện gần (dưới 15-20 phút)",
                "Cần khám để đảm bảo an toàn"
            ],
            "self_transport_note": "⚠️ **Lưu ý:** Ngã ở người già thường dẫn đến gãy xương (đặc biệt hông, xương chậu). Nếu nghi ngờ gãy xương → GỌI 115 để vận chuyển an toàn. Nếu chỉ ngã nhẹ và không có dấu hiệu nguy hiểm → Có thể tự đưa đến bệnh viện gần để kiểm tra."
        },
        "note": "⚠️ **QUAN TRỌNG:** Ngã ở người già thường gây gãy xương (đặc biệt hông) → Cần vận chuyển cẩn thận để không làm tổn thương thêm!"
    },
    
    "sudden_confusion": {
        "name": "Lú lẫn đột ngột",
        "icon": "😵",
        "signs": {
            "title": "🔍 Dấu hiệu lú lẫn nguy hiểm:",
            "items": [
                "Không nhận ra người thân, không biết mình ở đâu",
                "Nói lung tung, không rõ ràng",
                "Không nhớ việc vừa xảy ra",
                "Hành động kỳ lạ, bất thường",
                "Không hiểu lời nói của người khác",
                "Mất phương hướng, đi lạc",
                "Kèm theo: Sốt, đau đầu, yếu liệt tay chân"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY:",
            "steps": [
                "1️⃣ **GỌI 115 NGAY** nếu lú lẫn đột ngột, đặc biệt:",
                "   - Không nhận ra người thân",
                "   - Kèm sốt, đau đầu",
                "   - Kèm yếu liệt tay chân",
                "",
                "2️⃣ **GIỮ BÌNH TĨNH:**",
                "   - Nói chậm, rõ ràng",
                "   - Nhắc nhở người bệnh đang ở đâu, là ai",
                "   - Không tranh cãi, không giận dữ",
                "",
                "3️⃣ **ĐẢM BẢO AN TOÀN:**",
                "   - Không để một mình",
                "   - Tránh nguy hiểm (cầu thang, bếp, dao)",
                "   - Đóng cửa để tránh đi lạc",
                "",
                "4️⃣ **KIỂM TRA:**",
                "   - Nhiệt độ cơ thể (có sốt không?)",
                "   - Dấu hiệu đột quỵ (méo miệng, yếu liệt)",
                "   - Thuốc đã uống (có quên uống hoặc uống sai không?)",
                "",
                "5️⃣ **CHUẨN BỊ THÔNG TIN:**",
                "   - Thuốc đang uống",
                "   - Bệnh nền (cao huyết áp, tiểu đường, tim mạch)",
                "   - Tiền sử đột quỵ, sa sút trí tuệ"
            ]
        },
        "common_causes": {
            "title": "💡 Nguyên nhân lú lẫn đột ngột:",
            "items": [
                "Nhiễm trùng (viêm phổi, nhiễm trùng tiết niệu)",
                "Đột quỵ não (thiếu máu não)",
                "Hạ đường huyết (tiểu đường)",
                "Mất nước nặng",
                "Tác dụng phụ thuốc (an thần, giảm đau)",
                "Tăng/nhộn huyết áp nặng",
                "Sa sút trí tuệ (Alzheimer) - nhưng thường từ từ",
                "Chấn thương đầu (ngã, va đập)"
            ]
        },
        "vs_dementia": {
            "title": "🔍 Phân biệt: Sa sút trí tuệ vs Lú lẫn đột ngột",
            "dementia": {
                "name": "Sa sút trí tuệ (Từ từ):",
                "symptoms": [
                    "Diễn ra từ từ (hàng tháng, hàng năm)",
                    "Mất trí nhớ dần dần",
                    "Không có sốt, đau đầu đột ngột",
                    "Các chức năng cơ thể khác bình thường"
                ],
                "action": "Điều trị lâu dài, không cấp cứu"
            },
            "delirium": {
                "name": "Lú lẫn đột ngột (Cấp cứu):",
                "symptoms": [
                    "Xảy ra đột ngột (vài giờ, vài ngày)",
                    "Không nhận ra người thân, không biết ở đâu",
                    "Kèm sốt, đau đầu, yếu liệt",
                    "Có thể điều trị được nếu tìm đúng nguyên nhân"
                ],
                "action": "🚨 GỌI 115 NGAY - Cần khám ngay!"
            }
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NGAY NẾU:",
            "items": [
                "⛔ Lú lẫn đột ngột (vài giờ, vài ngày)",
                "⛔ Không nhận ra người thân, không biết ở đâu",
                "⛔ Kèm sốt cao >38.5°C",
                "⛔ Kèm đau đầu dữ dội",
                "⛔ Kèm yếu liệt tay chân (nghi ngờ đột quỵ)",
                "⛔ Kèm nôn, co giật",
                "⛔ Mất nước nặng (không uống nước được)"
            ]
        },
        "note": "⚠️ **Lú lẫn đột ngột KHÔNG phải sa sút trí tuệ bình thường** → Thường do nhiễm trùng, đột quỵ, hoặc tác dụng phụ thuốc → Cần khám NGAY để tìm nguyên nhân!"
    },
    
    "sudden_shortness_of_breath": {
        "name": "Khó thở đột ngột",
        "icon": "😰",
        "signs": {
            "title": "🔍 Dấu hiệu khó thở nguy hiểm:",
            "items": [
                "Khó thở đột ngột, không rõ nguyên nhân",
                "Thở gấp, thở nông",
                "Phải ngồi dậy mới thở được (không nằm được)",
                "Tím môi, đầu ngón tay",
                "Đau ngực khi thở",
                "Ho ra máu",
                "Mạch nhanh >120/phút",
                "Lơ mơ, không tỉnh táo"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY:",
            "steps": [
                "1️⃣ **GỌI 115 NGAY** - Khó thở đột ngột có thể nguy hiểm tính mạng!",
                "",
                "2️⃣ **ĐỂ NGỒI DẬY, CHÂN THẢ XUỐNG:**",
                "   - Tư thế ngồi giúp thở dễ hơn",
                "   - Gối cao lưng, cổ",
                "   - Không nằm ngửa (khó thở hơn)",
                "",
                "3️⃣ **NỚI LỎNG QUẦN ÁO:**",
                "   - Cởi áo chật, thắt lưng",
                "   - Đảm bảo không có gì chèn ép cổ, ngực",
                "",
                "4️⃣ **THỞ BẰNG MŨI, THỞ RA BẰNG MIỆNG:**",
                "   - Hít vào chậm, sâu",
                "   - Thở ra từ từ",
                "   - Giữ bình tĩnh (hoảng loạn làm khó thở thêm)",
                "",
                "5️⃣ **NẾU CÓ MÁY THỞ OXY:**",
                "   - Bật máy, đặt ống thở",
                "   - Điều chỉnh lưu lượng oxy (2-4 L/phút)",
                "",
                "6️⃣ **THEO DÕI:**",
                "   - Mạch, huyết áp",
                "   - Màu da, môi (có tím không?)",
                "   - Ý thức (có tỉnh táo không?)"
            ]
        },
        "common_causes": {
            "title": "💡 Nguyên nhân khó thở đột ngột:",
            "items": [
                "Nhồi máu phổi (cục máu đông trong phổi)",
                "Tràn khí màng phổi (phổi vỡ)",
                "Viêm phổi nặng",
                "Suy tim cấp (tim không bơm được máu)",
                "Hen suyễn cấp",
                "Dị vật đường thở (hóc)",
                "Đau tim (nhồi máu cơ tim)",
                "Lo lắng, hoảng loạn (nhưng ít nguy hiểm hơn)"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NGAY NẾU:",
            "items": [
                "⛔ Khó thở đột ngột, nặng",
                "⛔ Không nằm được, phải ngồi dậy",
                "⛔ Tím môi, đầu ngón tay",
                "⛔ Đau ngực kèm khó thở",
                "⛔ Ho ra máu",
                "⛔ Mạch nhanh >120/phút",
                "⛔ Lơ mơ, không tỉnh táo",
                "⛔ Không cải thiện sau 10-15 phút nghỉ ngơi"
            ]
        },
        "vs_normal_breathlessness": {
            "title": "🔍 Phân biệt: Khó thở bình thường vs Nguy hiểm",
            "normal": {
                "name": "Khó thở bình thường (Tạm thời):",
                "symptoms": [
                    "Sau khi leo cầu thang, vận động mạnh",
                    "Tự hết sau vài phút nghỉ ngơi",
                    "Không kèm đau ngực, tím môi",
                    "Tỉnh táo, mạch bình thường"
                ],
                "action": "Nghỉ ngơi, tự khỏi"
            },
            "dangerous": {
                "name": "Khó thở nguy hiểm (Cấp cứu):",
                "symptoms": [
                    "Đột ngột, không rõ nguyên nhân",
                    "Không nằm được, phải ngồi",
                    "Tím môi, đầu ngón tay",
                    "Kèm đau ngực, ho ra máu",
                    "Không cải thiện sau nghỉ ngơi"
                ],
                "action": "🚨 GỌI 115 NGAY!"
            }
        },
        "note": "⚠️ **QUAN TRỌNG:** Khó thở đột ngột có thể là dấu hiệu bệnh nguy hiểm tính mạng (nhồi máu phổi, suy tim, đau tim) → GỌI 115 NGAY!"
    }
}

