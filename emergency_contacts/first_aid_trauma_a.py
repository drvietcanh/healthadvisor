"""
Sơ cứu Chấn Thương A - Bỏng
Trauma First Aid A (Burns)
"""

FIRST_AID_TRAUMA_A = {
    "burns": {
        "name": "Bỏng nhiệt/Nước sôi",
        "icon": "🔥",
        "signs": {
            "title": "🔍 Phân loại bỏng chi tiết:",
            "items": [
                "**Bỏng độ 1 (Bỏng nông):**",
                "   - Đỏ da, đau nhẹ (như cháy nắng)",
                "   - Da khô, không phồng rộp",
                "   - Tự khỏi sau 3-7 ngày, không để sẹo",
                "   - 💡 Có thể tự chăm sóc tại nhà",
                "",
                "**Bỏng độ 2 (Bỏng trung bình):**",
                "   - Đỏ da, phồng rộp (bóng nước)",
                "   - Đau nhiều, chảy dịch",
                "   - Da ướt, hơi trắng khi ấn",
                "   - Khỏi sau 2-3 tuần, có thể để sẹo nhẹ",
                "   - ⚠️ Cần chăm sóc cẩn thận, tránh nhiễm trùng",
                "",
                "**Bỏng độ 3 (Bỏng sâu):**",
                "   - Da trắng, nâu hoặc đen (hoại tử)",
                "   - MẤT CẢM GIÁC (không đau - dây thần kinh bị tổn thương!)",
                "   - Da khô, cứng (như da bò)",
                "   - KHÔNG TỰ KHỎI, cần ghép da",
                "   - 🚨 NGUY HIỂM - Cần bác sĩ NGAY!"
            ],
            "note": "💡 **LƯU Ý:** Bỏng độ 3 KHÔNG đau vì dây thần kinh bị tổn thương - Đừng nhầm là nhẹ!"
        },
        "classification": {
            "title": "📏 Đánh giá diện tích bỏng (Quy tắc lòng bàn tay):",
            "rule": "1 lòng bàn tay = 1% diện tích cơ thể",
            "examples": [
                "Bỏng cả cánh tay = 9% (người lớn)",
                "Bỏng cả chân = 18% (người lớn)",
                "Bỏng ngực + bụng = 18% (người lớn)",
                "Trẻ em: Diện tích tính khác (đầu = 20%, chân = 15%)"
            ],
            "severe_if": [
                "Bỏng >10% diện tích cơ thể",
                "Bỏng độ 3 >5%",
                "Bỏng ở mặt, cổ, tay, chân, bộ phận sinh dục",
                "Bỏng đường hô hấp (hít khói nóng)"
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
        "home_care": {
            "title": "🏠 Chăm sóc tại nhà (Bỏng độ 1-2, nhỏ):",
            "steps": [
                "1️⃣ **Rửa sạch hàng ngày:**",
                "   - Rửa bằng nước muối sinh lý hoặc nước sạch",
                "   - Nhẹ nhàng, không cọ xát",
                "",
                "2️⃣ **Bôi thuốc (nếu bỏng độ 1-2, nhỏ):**",
                "   - Silvadene cream, Flamazine (theo chỉ định bác sĩ)",
                "   - Hoặc mỡ kháng sinh: Bactroban, Fucidin",
                "   - Bôi mỏng, 2-3 lần/ngày",
                "",
                "3️⃣ **Băng vết bỏng:**",
                "   - Dùng gạc không dính (Mepilex, Telfa)",
                "   - Băng nhẹ nhàng, không chặt",
                "   - Thay băng 1-2 lần/ngày",
                "",
                "4️⃣ **Giảm đau:**",
                "   - Paracetamol 500-1000mg × 3-4 lần/ngày",
                "   - Ibuprofen 400mg × 3 lần/ngày (nếu không có chống chỉ định)",
                "",
                "5️⃣ **Phồng rộp:**",
                "   - KHÔNG chọc phồng rộp (bảo vệ da non)",
                "   - Nếu vỡ tự nhiên: Rửa sạch, bôi thuốc, băng",
                "",
                "6️⃣ **Theo dõi dấu hiệu nhiễm trùng:**",
                "   - Sưng, đỏ lan rộng",
                "   - Đau tăng, có mủ",
                "   - Sốt, nổi hạch",
                "   - → Đi khám ngay!"
            ]
        },
        "complications": {
            "title": "⚠️ Biến chứng bỏng:",
            "items": [
                "**Nhiễm trùng:** Phổ biến nhất, có thể nặng → Nhiễm trùng máu",
                "**Sẹo:** Bỏng sâu → Sẹo co rút, mất chức năng",
                "**Mất nước:** Bỏng rộng → Mất dịch qua da → Sốc",
                "**Hít khói nóng:** Bỏng đường hô hấp → Suy hô hấp, nguy hiểm tính mạng",
                "**Hạ thân nhiệt:** Da mất → Mất nhiệt nhanh → Nguy hiểm ở trẻ em, người già"
            ]
        },
        "prevention": {
            "title": "💡 Phòng ngừa bỏng:",
            "items": [
                "✅ **Bếp:**",
                "   - Tay cầm nồi xoay vào trong",
                "   - Không để trẻ em gần bếp",
                "   - Dùng găng tay khi nấu",
                "",
                "✅ **Nước nóng:**",
                "   - Kiểm tra nhiệt độ nước trước khi tắm (đặc biệt trẻ em)",
                "   - Để ấm nước ngoài tầm với trẻ",
                "   - Nhiệt độ nước tắm: 37-38°C (không >40°C)",
                "",
                "✅ **Đồ dùng:**",
                "   - Không để cốc nước nóng trên mép bàn",
                "   - Cẩn thận khi rót nước nóng",
                "   - Kiểm tra ấm nước điện trước khi rót",
                "",
                "✅ **Cháy:**",
                "   - Không hút thuốc trong nhà",
                "   - Lắp báo khói",
                "   - Cẩn thận với nến, đèn dầu"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NGAY NẾU:",
            "items": [
                "⛔ Bỏng độ 3 (da trắng/đen, mất cảm giác) - Dù nhỏ",
                "⛔ Bỏng rộng >10% diện tích cơ thể (lớn hơn 10 lòng bàn tay)",
                "⛔ Bỏng ở mặt, cổ, tay, chân, bộ phận sinh dục",
                "⛔ Bỏng đường hô hấp (hít khói nóng) → Khó thở, khàn tiếng",
                "⛔ Bỏng do điện, hóa chất",
                "⛔ Trẻ em bỏng (dù nhỏ - trẻ dễ biến chứng)",
                "⛔ Người già >60 tuổi bỏng (miễn dịch yếu)",
                "⛔ Bỏng kèm khó thở, ngất xỉu, sốc",
                "⛔ Nhiễm trùng (sưng, đỏ lan, mủ, sốt)"
            ]
        },
        "transport_option": {
            "title": "🚗 Đưa đến bệnh viện:",
            "call_115_recommended": [
                "Bỏng độ 3 (dù nhỏ)",
                "Bỏng rộng >10% diện tích cơ thể",
                "Bỏng ở mặt, cổ, tay, chân, bộ phận sinh dục",
                "Bỏng do điện, hóa chất",
                "Bỏng đường hô hấp (khó thở)",
                "Trẻ em hoặc người già bỏng",
                "Bỏng kèm khó thở, ngất, sốc"
            ],
            "self_transport_allowed": [
                "Bỏng độ 1-2 nhỏ (nhỏ hơn lòng bàn tay)",
                "Đã sơ cứu tốt (dội nước lạnh 15-20 phút)",
                "Người bệnh tỉnh táo, không khó thở",
                "Bệnh viện gần (dưới 20-30 phút)",
                "Để kiểm tra và băng bó đúng cách"
            ],
            "self_transport_note": "💡 **Lưu ý:** Nếu bỏng độ 1-2 nhỏ và đã sơ cứu tốt, có thể tự đưa đến bệnh viện gần để bác sĩ kiểm tra và băng bó. Nhưng nếu nghi ngờ hoặc bỏng lớn → GỌI 115."
        },
        "note": "💡 **QUAN TRỌNG:** Bỏng độ 1-2 nhỏ (nhỏ hơn lòng bàn tay) có thể tự chăm sóc. Bỏng độ 3, rộng, hoặc ở vùng quan trọng → BÁC SĨ NGAY!"
    }
}

