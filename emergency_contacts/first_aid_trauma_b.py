"""
Sơ cứu Chấn Thương B - Chảy máu, Ngã, Chấn thương cột sống
Trauma First Aid B (Bleeding, Fall, Spinal Injury)
"""

FIRST_AID_TRAUMA_B = {
    "bleeding": {
        "name": "Chảy máu",
        "icon": "🩸",
        "signs": {
            "title": "🔍 Phân loại chảy máu:",
            "items": [
                "**Chảy máu nhẹ:** Chảy ít, tự cầm sau vài phút",
                "**Chảy máu vừa:** Chảy liên tục, cần ép chặt",
                "**Chảy máu nặng:** Chảy thành tia, máu đỏ tươi - NGUY HIỂM!"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY:",
            "steps": [
                "1️⃣ **ÉP CHẶT VẾT THƯƠNG** - Dùng gạc sạch hoặc vải sạch",
                "   - Đặt gạc lên vết thương",
                "   - Dùng lòng bàn tay ép mạnh, liên tục",
                "   - Ép ít nhất 5-10 phút (KHÔNG nhấc tay lên xem!)",
                "",
                "2️⃣ **NÂNG CAO** vùng chảy máu lên cao hơn tim (nếu có thể)",
                "",
                "3️⃣ **NẾU VẪN CHẢY:**",
                "   - Thêm lớp gạc, tiếp tục ép",
                "   - KHÔNG bỏ lớp gạc cũ (giữ lại để tạo cục máu đông)",
                "",
                "4️⃣ **GIỮ ẤM** - Đắp chăn nhẹ (tránh sốc do mất máu)",
                "",
                "5️⃣ **NẾU CHẢY MÁU NẶNG:**",
                "   - GỌI 115 NGAY",
                "   - Tiếp tục ép chặt trong lúc chờ"
            ]
        },
        "dont": {
            "title": "❌ TUYỆT ĐỐI KHÔNG:",
            "items": [
                "❌ KHÔNG rửa vết thương khi đang chảy máu nhiều",
                "❌ KHÔNG bỏ vật lạ ra (nếu có - để bác sĩ xử lý)",
                "❌ KHÔNG buộc garo (trừ khi biết cách, rất nguy hiểm!)",
                "❌ KHÔNG nhấc tay lên để xem máu đã cầm chưa"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NGAY NẾU:",
            "items": [
                "⛔ Chảy máu không cầm sau 10 phút ép chặt",
                "⛔ Chảy máu thành tia (mạch máu lớn)",
                "⛔ Mất nhiều máu (choáng váng, da xanh, mạch nhanh)",
                "⛔ Chảy máu ở cổ, ngực, bụng",
                "⛔ Có vật lạ cắm trong vết thương"
            ]
        },
        "transport_option": {
            "title": "🚗 Đưa đến bệnh viện:",
            "call_115_recommended": [
                "Chảy máu không cầm sau khi ép chặt",
                "Chảy máu thành tia, mất máu nhiều",
                "Chảy máu ở vùng nguy hiểm (cổ, ngực, bụng)",
                "Có vật lạ cắm trong vết thương",
                "Người bệnh choáng váng, da xanh"
            ],
            "self_transport_allowed": [
                "Chảy máu đã cầm được sau khi ép chặt",
                "Vết thương nhỏ, nông",
                "Người bệnh tỉnh táo, ổn định",
                "Bệnh viện gần (dưới 15-20 phút)"
            ],
            "self_transport_note": "⚠️ **Lưu ý:** Tiếp tục ép chặt vết thương khi di chuyển. Nếu máu chảy lại → Dừng lại ép tiếp hoặc gọi 115."
        },
        "note": "💡 **QUAN TRỌNG:** Ép chặt là cách tốt nhất để cầm máu. Đừng bỏ cuộc!"
    },
    
    "fall": {
        "name": "Ngã (Người già)",
        "icon": "🤕",
        "signs": {
            "title": "🔍 Đánh giá sau khi ngã:",
            "items": [
                "Có đau nhiều không?",
                "Có bị thương ở đâu?",
                "Có thể cử động tay, chân không?",
                "Có đau đầu, chóng mặt không?",
                "Có nhớ rõ vì sao ngã không?"
            ]
        },
        "actions": {
            "title": "⚡ Xử lý:",
            "steps": [
                "1️⃣ **Đừng vội đứng dậy** - Nằm yên, đánh giá",
                "2️⃣ **Kiểm tra:**",
                "   - Có đau nghiêm trọng?",
                "   - Có chảy máu?",
                "   - Có biến dạng xương?",
                "3️⃣ **Nếu OK:** Từ từ ngồi dậy, nghỉ 1-2 phút",
                "4️⃣ **Sau đó:** Từ từ đứng dậy, cầm vào đồ vật",
                "5️⃣ **Nếu đau, yếu:** Gọi người giúp, KHÔNG tự đứng"
            ]
        },
        "call_115": {
            "title": "🚨 KHI NÀO GỌI 115?",
            "items": [
                "❗ Đau dữ dội, đặc biệt ở hông, đầu",
                "❗ Không thể đứng dậy, cử động chân",
                "❗ Xương lệch, biến dạng",
                "❗ Chảy máu nhiều",
                "❗ Đau đầu dữ dội, chóng mặt",
                "❗ Bất tỉnh (dù chỉ vài giây)",
                "❗ Đau ngực, khó thở sau khi ngã"
            ]
        },
        "transport_option": {
            "title": "🚗 Đưa đến bệnh viện:",
            "call_115_recommended": [
                "Không thể đứng dậy, không cử động được",
                "Xương lệch, biến dạng rõ ràng",
                "Bất tỉnh (dù chỉ vài giây)",
                "Đau đầu dữ dội, chóng mặt nhiều",
                "Nghi ngờ chấn thương đầu, cổ, lưng",
                "Đau ngực, khó thở sau ngã"
            ],
            "self_transport_allowed": [
                "Có thể đứng dậy, đi lại được",
                "Chỉ đau nhẹ, không có biến dạng",
                "Tỉnh táo, không đau đầu nhiều",
                "Không chảy máu hoặc chỉ chảy ít",
                "Bệnh viện gần (dưới 15-20 phút)",
                "Cần kiểm tra để chắc chắn"
            ],
            "self_transport_note": "⚠️ **Lưu ý:** Ngã ở người già dễ gãy xương hông (đùi) hoặc chấn thương đầu. Nếu nghi ngờ → GỌI 115. Nếu chỉ đau nhẹ và có thể đi lại → Có thể tự đưa đi kiểm tra."
        },
        "prevention": {
            "title": "💡 Phòng ngừa ngã:",
            "items": [
                "✅ Nhà cửa sáng sủa, không vấp",
                "✅ Có tay vịn ở nhà tắm, cầu thang",
                "✅ Đi giày/dép chống trượt",
                "✅ Đứng dậy từ từ (tránh chóng mặt)",
                "✅ Dùng gậy khi đi lại",
                "✅ Tập thể dục giữ thăng bằng"
            ]
        }
    },
    
    "spinal_injury": {
        "name": "Chấn thương cột sống cổ",
        "icon": "🦴",
        "signs": {
            "title": "🔍 Dấu hiệu nghi ngờ chấn thương cột sống:",
            "items": [
                "Đau cổ, lưng dữ dội sau tai nạn",
                "Tê, yếu tay hoặc chân",
                "Không cử động được tay/chân",
                "Mất cảm giác một phần cơ thể",
                "Đau khi cử động cổ",
                "Nhức đầu, chóng mặt sau tai nạn"
            ]
        },
        "risk_situations": {
            "title": "⚠️ Tình huống có nguy cơ cao:",
            "items": [
                "🚗 Tai nạn giao thông (va chạm mạnh)",
                "🏊 Ngã từ trên cao xuống (cầu, mái nhà)",
                "🏊 Lặn xuống nước cạn, đầu đập đáy",
                "⚽ Tai nạn thể thao (đá bóng, võ thuật)",
                "🤕 Ngã đập đầu xuống đất",
                "💥 Vật nặng đập vào đầu/cổ"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY (QUAN TRỌNG: KHÔNG DI CHUYỂN!):",
            "steps": [
                "1️⃣ **GỌI 115 NGAY** - Báo rõ nghi ngờ chấn thương cột sống",
                "",
                "2️⃣ **GIỮ NẠN NHÂN NẰM YÊN** - TUYỆT ĐỐI KHÔNG di chuyển:",
                "   - Nếu nạn nhân đang nằm → Giữ nguyên tư thế",
                "   - Nếu nạn nhân đang ngồi → Giữ thẳng lưng, không để ngã",
                "   - KHÔNG kéo, lôi, bế nạn nhân",
                "",
                "3️⃣ **GIỮ ĐẦU CỔ THẲNG:**",
                "   - Dùng tay giữ 2 bên đầu nạn nhân (như đội mũ bảo hiểm)",
                "   - KHÔNG xoay đầu sang trái, phải, cúi, ngửa",
                "   - Giữ cho đầu, cổ, thân thẳng hàng",
                "   - Nếu có gối → Đặt dưới cổ (không dưới đầu)",
                "",
                "4️⃣ **NẾU PHẢI DI CHUYỂN (chỉ khi NGUY HIỂM):**",
                "   - Chỉ khi: Cháy, nổ, nước dâng...",
                "   - Phải có 3-4 người, di chuyển như một khối",
                "   - Giữ thẳng đầu-cổ-lưng",
                "   - Dùng ván cứng (nếu có)",
                "",
                "5️⃣ **THEO DÕI:**",
                "   - Kiểm tra thở, mạch",
                "   - Động viên nạn nhân nằm yên",
                "   - Giữ ấm (đắp chăn nhẹ)"
            ]
        },
        "dont": {
            "title": "❌ TUYỆT ĐỐI KHÔNG:",
            "items": [
                "❌ KHÔNG kéo, lôi, bế nạn nhân lên",
                "❌ KHÔNG xoay đầu nạn nhân (có thể làm liệt!)",
                "❌ KHÔNG cho nạn nhân ngồi dậy",
                "❌ KHÔNG cố gắng 'nắn' cổ, lưng",
                "❌ KHÔNG cho nạn nhân đi lại, đứng dậy",
                "❌ KHÔNG tự đưa đi bệnh viện bằng xe thường (cần xe cấp cứu có ván cứng)",
                "❌ KHÔNG bỏ cuộc - Tiếp tục giữ yên cho đến khi xe cấp cứu đến"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NGAY NẾU:",
            "items": [
                "⛔ Nghi ngờ chấn thương cột sống (dù nhẹ)",
                "⛔ Đau cổ/lưng sau tai nạn",
                "⛔ Tê, yếu tay/chân",
                "⛔ Sau tai nạn giao thông, ngã từ cao",
                "⛔ Không cử động được một phần cơ thể"
            ]
        },
        "note": "⚠️ **CỰC KỲ QUAN TRỌNG:** Di chuyển sai cách có thể làm liệt vĩnh viễn! Đợi xe cấp cứu với nhân viên y tế chuyên nghiệp!"
    }
}

