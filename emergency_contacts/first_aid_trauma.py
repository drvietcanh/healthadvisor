"""
Sơ cứu Chấn Thương
Trauma First Aid (Bỏng, Chảy máu, Ngã, Chấn thương cột sống)
"""

FIRST_AID_TRAUMA = {
    "burns": {
        "name": "Bỏng nhiệt/Nước sôi",
        "icon": "🔥",
        "signs": {
            "title": "🔍 Phân loại bỏng:",
            "items": [
                "**Bỏng độ 1:** Đỏ da, đau nhẹ (như cháy nắng) - Tự khỏi vài ngày",
                "**Bỏng độ 2:** Phồng rộp, đau nhiều - Cần chăm sóc cẩn thận",
                "**Bỏng độ 3:** Da trắng/đen, mất cảm giác - NGUY HIỂM, cần bác sĩ ngay!"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY (Quy tắc 20 phút):",
            "steps": [
                "1️⃣ **DỘI NƯỚC LẠNH NGAY** - 15-20 phút liên tục",
                "   - Nước máy, nước sạch (không đá lạnh!)",
                "   - Giữ vết bỏng dưới vòi nước hoặc ngâm trong chậu",
                "   - Mục đích: Hạ nhiệt độ da, giảm đau, giảm tổn thương",
                "2️⃣ **CỞI BỎ quần áo/trang sức** - Nếu không dính vào da",
                "   - Nếu dính chặt → KHÔNG được kéo ra!",
                "   - Cắt xung quanh vải, để bác sĩ xử lý",
                "3️⃣ **PHỦ vết bỏng bằng gạc sạch hoặc khăn sạch** - Tránh nhiễm trùng",
                "   - Không băng quá chặt",
                "4️⃣ **GIỮ ẤM** - Đắp chăn nhẹ (tránh vết bỏng)",
                "5️⃣ **KHÔNG bôi gì lên vết bỏng** - Chờ bác sĩ"
            ]
        },
        "dont": {
            "title": "❌ TUYỆT ĐỐI KHÔNG:",
            "items": [
                "❌ KHÔNG bôi kem, dầu, nước mắm, lá cây lên vết bỏng",
                "❌ KHÔNG chọc phồng rộp (phồng rộp bảo vệ da non)",
                "❌ KHÔNG dùng đá lạnh trực tiếp (làm tổn thương thêm)",
                "❌ KHÔNG cởi quần áo nếu dính chặt vào da"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NGAY NẾU:",
            "items": [
                "⛔ Bỏng rộng (lớn hơn lòng bàn tay)",
                "⛔ Bỏng ở mặt, cổ, tay, chân, bộ phận sinh dục",
                "⛔ Bỏng độ 3 (da trắng/đen, mất cảm giác)",
                "⛔ Bỏng do điện, hóa chất",
                "⛔ Trẻ em bỏng (dù nhỏ)",
                "⛔ Người già >60 tuổi bỏng",
                "⛔ Bỏng kèm khó thở, ngất xỉu"
            ]
        },
        "note": "💡 **MẸO:** Bỏng nhẹ (độ 1-2, nhỏ) có thể tự chăm sóc. Bỏng nặng hoặc rộng → BÁC SĨ NGAY!"
    },
    
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

