"""
Hướng dẫn sơ cứu nhanh cho người già
"""

FIRST_AID_GUIDES = {
    "heart_attack": {
        "name": "Đau tim cấp (Nhồi máu cơ tim)",
        "icon": "❤️",
        "signs": {
            "title": "🔍 Dấu hiệu nhận biết:",
            "items": [
                "Đau ngực dữ dội, như bị đè nặng, siết chặt",
                "Đau lan ra vai trái, cánh tay trái, hàm, lưng",
                "Khó thở, thở gấp",
                "Đổ mồ hôi lạnh, choáng váng",
                "Buồn nôn, nôn mửa",
                "Lo lắng, sợ hãi, cảm giác chết"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY (Mỗi giây rất quan trọng!):",
            "steps": [
                "1️⃣ **GỌI 115 NGAY LẬP TỨC** - Đừng chờ!",
                "2️⃣ **Ngồi hoặc nằm nghỉ** - Không vận động",
                "3️⃣ **Nới lỏng quần áo** - Để thở dễ hơn",
                "4️⃣ **Nếu có thuốc tim:**",
                "   - Aspirin 81mg: ngậm 3-4 viên (khoảng 250-325mg)",
                "   - Thuốc giãn mạch (nếu bác sĩ kê): đặt dưới lưỡi",
                "5️⃣ **Giữ bình tĩnh** - Đừng hoảng loạn",
                "6️⃣ **Không ăn uống gì** - Tránh sặc",
                "7️⃣ **Chờ xe cấp cứu** - Không tự lái xe đi viện!"
            ]
        },
        "dont": {
            "title": "❌ TUYỆT ĐỐI KHÔNG:",
            "items": [
                "❌ Không chờ xem triệu chứng có qua không",
                "❌ Không tự lái xe đi bệnh viện",
                "❌ Không để người bệnh đi lại, vận động",
                "❌ Không cho uống nước (có thể sặc)"
            ]
        },
        "note": "⏱️ **THỜI GIAN VÀNG:** 90 phút đầu quyết định sống còn!"
    },
    
    "stroke": {
        "name": "Đột quỵ (Tai biến mạch máu não)",
        "icon": "🧠",
        "signs": {
            "title": "🔍 Nhận biết nhanh bằng F.A.S.T:",
            "items": [
                "**F - Face (Mặt):** Cười méo một bên, xệ một bên mặt",
                "**A - Arm (Tay):** Giơ 2 tay lên, 1 tay rơi xuống, yếu",
                "**S - Speech (Nói):** Nói lảm nhảm, ngọng, không nói được",
                "**T - Time (Gọi ngay):** GỌI 115 NGAY!"
            ]
        },
        "other_signs": [
            "Đau đầu dữ dội đột ngột",
            "Chóng mặt, mất thăng bằng",
            "Nhìn mờ, nhìn đôi",
            "Tê/liệt nửa người",
            "Lú lẫn, không nhận ra người thân"
        ],
        "actions": {
            "title": "⚡ XỬ LÝ NGAY:",
            "steps": [
                "1️⃣ **GỌI 115 NGAY** - Càng sớm càng tốt!",
                "2️⃣ **Nằm nghiêng sang bên yếu** - Tránh sặc",
                "3️⃣ **Đầu hơi cao** - Kê gối nhẹ",
                "4️⃣ **Nới lỏng quần áo** - Cúc áo, thắt lưng",
                "5️⃣ **GHI GIỜ xuất hiện triệu chứng** - Quan trọng!",
                "6️⃣ **Không cho ăn uống** - Có thể sặc",
                "7️⃣ **Giữ ấm** - Đắp chăn",
                "8️⃣ **Theo dõi hô hấp** - Sẵn sàng CPR"
            ]
        },
        "dont": {
            "title": "❌ TUYỆT ĐỐI KHÔNG:",
            "items": [
                "❌ Không cho uống thuốc (trừ khi bác sĩ chỉ định)",
                "❌ Không đắp thuốc, xoa bóp",
                "❌ Không chích máu đầu ngón tay (vô ích!)",
                "❌ Không tự đưa đi viện - Chờ xe 115"
            ]
        },
        "note": "⏱️ **VÀNG 3 GIỜ:** Điều trị trong 3-4.5 giờ đầu hiệu quả nhất!"
    },
    
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
    
    "choking_child": {
        "name": "Trẻ em hóc dị vật (Nghẹn)",
        "icon": "👶",
        "signs": {
            "title": "🔍 Dấu hiệu trẻ bị hóc:",
            "items": [
                "Ho dữ dội, khó thở",
                "Mặt đỏ/tím, mắt trợn",
                "Không nói được, không khóc được",
                "Đưa tay lên cổ (động tác báo hiệu)",
                "Mất ý thức (nếu nặng)"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY (Quy tắc 5 lần - 5 lần):",
            "steps": [
                "**CHO TRẺ < 1 TUỔI:**",
                "",
                "1️⃣ **VỖ LƯNG 5 LẦN:**",
                "   - Đặt trẻ nằm sấp trên đùi, đầu thấp hơn ngực",
                "   - Dùng gót bàn tay vỗ mạnh giữa 2 xương bả vai",
                "   - Vỗ 5 lần, kiểm tra xem dị vật ra chưa",
                "",
                "2️⃣ **ÉP NGỰC 5 LẦN:**",
                "   - Lật trẻ nằm ngửa trên đùi",
                "   - Đặt 2 ngón tay giữa xương ức",
                "   - Ấn mạnh xuống 5 lần (1 giây/lần)",
                "",
                "3️⃣ **LẶP LẠI** vỗ lưng - ép ngực cho đến khi:",
                "   - Dị vật ra",
                "   - Trẻ ho được, khóc được",
                "   - Trẻ mất ý thức → Chuyển CPR",
                "",
                "**CHO TRẺ 1-8 TUỔI:**",
                "",
                "4️⃣ **VỖ LƯNG 5 LẦN:**",
                "   - Trẻ cúi đầu thấp",
                "   - Vỗ mạnh giữa 2 xương bả vai 5 lần",
                "",
                "5️⃣ **ÉP BỤNG (Heimlich) 5 LẦN:**",
                "   - Đứng sau trẻ, vòng tay quanh eo",
                "   - Một tay nắm đấm, đặt trên rốn",
                "   - Tay kia nắm cổ tay, ấn mạnh vào trong và lên trên",
                "   - Ấn 5 lần (như muốn nhấc trẻ lên)",
                "",
                "6️⃣ **LẶP LẠI** cho đến khi dị vật ra hoặc trẻ mất ý thức",
                "",
                "**TRẺ MẤT Ý THỨC:**",
                "7️⃣ **GỌI 115 NGAY** - Đồng thời bắt đầu CPR nếu biết"
            ]
        },
        "dont": {
            "title": "❌ TUYỆT ĐỐI KHÔNG:",
            "items": [
                "❌ KHÔNG móc tay vào miệng trẻ (đẩy dị vật sâu hơn)",
                "❌ KHÔNG đánh vào lưng khi trẻ đang đứng thẳng",
                "❌ KHÔNG cầm chân trẻ lộn ngược (nguy hiểm!)",
                "❌ KHÔNG bỏ cuộc - Tiếp tục vỗ/ép cho đến khi giúp đỡ đến"
            ]
        },
        "prevention": {
            "title": "🛡️ PHÒNG NGỪA:",
            "items": [
                "✅ Cắt thức ăn nhỏ cho trẻ < 3 tuổi",
                "✅ Tránh: nho nguyên quả, hạt, kẹo cứng",
                "✅ Giám sát khi trẻ ăn",
                "✅ Để đồ chơi nhỏ xa tầm tay trẻ"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NGAY NẾU:",
            "items": [
                "⛔ Trẻ không thể ho, không thể thở",
                "⛔ Trẻ tím tái, mất ý thức",
                "⛔ Sau khi dị vật ra nhưng trẻ vẫn khó thở",
                "⛔ Không chắc chắn dị vật đã ra hết"
            ]
        },
        "note": "⏱️ **QUAN TRỌNG:** Mỗi giây đều quý! Hóc dị vật có thể gây tử vong trong vài phút!"
    },
    
    "hypoglycemia": {
        "name": "Hạ đường huyết (Tiểu đường)",
        "icon": "🍬",
        "signs": {
            "title": "🔍 Dấu hiệu:",
            "items": [
                "Đói bụng đột ngột",
                "Run tay, chân",
                "Đổ mồ hôi lạnh",
                "Hồi hộp, tim đập nhanh",
                "Chóng mặt, yếu người",
                "Lú lẫn, cáu gắt bất thường",
                "Nhìn mờ",
                "Nghiêm trọng: Co giật, hôn mê"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY (Quy tắc 15-15):",
            "steps": [
                "1️⃣ **ĂN ĐƯỜNG NGAY:**",
                "   - 15g đường (3-4 viên kẹo hoặc 1 thìa đường)",
                "   - Hoặc: 150ml nước ngọt có ga",
                "   - Hoặc: 1 hộp sữa có đường nhỏ",
                "   - Hoặc: 1 thìa mật ong",
                "2️⃣ **Ngồi/nằm nghỉ 15 phút**",
                "3️⃣ **Đo lại đường huyết** (nếu có máy)",
                "4️⃣ **Nếu vẫn < 70 mg/dL:** Ăn thêm 15g đường nữa",
                "5️⃣ **Sau khi hồi phục:** Ăn bữa phụ nhẹ (bánh mì, chuối)"
            ]
        },
        "severe": {
            "title": "🚨 Nếu NGHIÊM TRỌNG (lơ mơ, không nuốt được):",
            "steps": [
                "❗ **GỌI 115 NGAY**",
                "❗ **Đặt nghiêng người** - Tránh sặc",
                "❗ **KHÔNG cho ăn/uống** - Có thể sặc",
                "❗ **Nếu có Glucagon injection:** Tiêm theo hướng dẫn",
                "❗ **Chờ xe cấp cứu**"
            ]
        },
        "prevention": {
            "title": "💡 Phòng ngừa:",
            "items": [
                "✅ Luôn mang theo kẹo/đường khi ra ngoài",
                "✅ Ăn đúng giờ, không bỏ bữa",
                "✅ Đo đường huyết thường xuyên",
                "✅ Điều chỉnh thuốc/insulin đúng liều",
                "✅ Đeo vòng tay/thẻ ghi \"Bệnh tiểu đường\""
            ]
        },
        "note": "💊 Người tiểu đường dùng insulin/thuốc hạ đường cần đặc biệt cảnh giác!"
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
    
    "chest_pain": {
        "name": "Đau ngực (Không rõ nguyên nhân)",
        "icon": "💔",
        "call_115": {
            "title": "🚨 GỌI 115 NGAY nếu:",
            "items": [
                "❗ Đau ngực dữ dội, như bị ép chặt",
                "❗ Đau lan ra vai, cánh tay trái, hàm, lưng",
                "❗ Kèm khó thở, đổ mồ hôi lạnh",
                "❗ Kèm buồn nôn, chóng mặt",
                "❗ Người trên 40 tuổi + có bệnh tim mạch",
                "❗ Đau > 5 phút không giảm"
            ]
        },
        "actions": {
            "title": "⚡ Trong lúc chờ:",
            "steps": [
                "1️⃣ Ngồi hoặc nằm nghỉ",
                "2️⃣ Nới lỏng quần áo",
                "3️⃣ Giữ bình tĩnh",
                "4️⃣ Không ăn uống",
                "5️⃣ Nếu có Aspirin 81mg: ngậm 3-4 viên (nếu không dị ứng)"
            ]
        },
        "note": "⚠️ Đau ngực có thể là dấu hiệu đau tim - KHÔNG CHỦ QUAN!"
    },
    
    "poisoning": {
        "name": "Ngộ độc",
        "icon": "☠️",
        "signs": {
            "title": "🔍 Dấu hiệu ngộ độc:",
            "items": [
                "Buồn nôn, nôn mửa",
                "Đau bụng",
                "Tiêu chảy",
                "Chóng mặt, lơ mơ",
                "Khó thở",
                "Co giật (nếu nặng)"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY:",
            "steps": [
                "1️⃣ **GỌI 115 NGAY** - Hoặc Trung tâm chống độc: 024.3929.5743",
                "2️⃣ **HỎI người bệnh** (nếu còn tỉnh):",
                "   - Uống/Nhậu gì?",
                "   - Bao nhiêu?",
                "   - Khi nào?",
                "3️⃣ **LƯU Ý:**",
                "   - Nếu hôn mê, nằm nghiêng (tránh sặc)",
                "   - Giữ lại vật gây ngộ độc (thuốc, chai lọ...)",
                "   - KHÔNG tự ý gây nôn (trừ khi nhân viên y tế hướng dẫn)",
                "4️⃣ **ĐỢI xe cấp cứu** - Theo dõi hô hấp, mạch"
            ]
        },
        "dont": {
            "title": "❌ TUYỆT ĐỐI KHÔNG:",
            "items": [
                "❌ KHÔNG cho uống sữa/trứng sống (làm sai lệch)",
                "❌ KHÔNG tự ý cho uống than hoạt tính (chỉ khi bác sĩ chỉ định)",
                "❌ KHÔNG gây nôn khi uống chất tẩy/axit (làm bỏng thêm)",
                "❌ KHÔNG bỏ cuộc - Tiếp tục theo dõi"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 HOẶC TRUNG TÂM CHỐNG ĐỘC NGAY:",
            "items": [
                "⛔ Nghi ngờ ngộ độc (dù nhẹ)",
                "⛔ Hôn mê, lơ mơ",
                "⛔ Khó thở",
                "⛔ Co giật",
                "⛔ Ngộ độc ở trẻ em"
            ]
        },
        "note": "💡 **QUAN TRỌNG:** Mỗi phút đều quý! Gọi ngay Trung tâm chống độc để được hướng dẫn chính xác!"
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
    
    "drowning": {
        "name": "Đuối nước",
        "icon": "🌊",
        "signs": {
            "title": "🔍 Dấu hiệu đuối nước:",
            "items": [
                "Người trong nước, không nổi được",
                "Kêu cứu, vẫy tay",
                "Ho, sặc nước",
                "Tím tái, mất ý thức (nếu đã chìm)"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY (Ưu tiên an toàn bản thân!):",
            "steps": [
                "1️⃣ **GỌI 115 NGAY** - Đồng thời kêu cứu",
                "",
                "2️⃣ **NẾU BIẾT BƠI:**",
                "   - Ném phao cứu sinh, dây, gậy cho nạn nhân",
                "   - Nếu nhảy xuống: Nhảy từ phía sau, tránh bị kéo xuống",
                "   - Đưa nạn nhân lên bờ an toàn",
                "",
                "3️⃣ **KHI ĐÃ LÊN BỜ:**",
                "   - Đặt nạn nhân nằm ngửa",
                "   - Kiểm tra thở, mạch",
                "",
                "4️⃣ **NẾU KHÔNG THỞ:**",
                "   - Bắt đầu CPR ngay (ép tim + thổi ngạt)",
                "   - Tiếp tục cho đến khi xe cấp cứu đến",
                "",
                "5️⃣ **NẾU CÒN THỞ:**",
                "   - Đặt nằm nghiêng (tránh sặc nước)",
                "   - Giữ ấm, theo dõi",
                "   - Dù tỉnh vẫn cần đưa bệnh viện"
            ]
        },
        "dont": {
            "title": "❌ TUYỆT ĐỐI KHÔNG:",
            "items": [
                "❌ KHÔNG nhảy xuống nếu KHÔNG biết bơi",
                "❌ KHÔNG để nạn nhân nằm ngửa nếu đang nôn (sặc!)",
                "❌ KHÔNG bỏ cuộc CPR sớm (có thể cứu sống sau 20-30 phút)",
                "❌ KHÔNG xốc nước (vô ích, nguy hiểm!)"
            ]
        },
        "prevention": {
            "title": "🛡️ PHÒNG NGỪA:",
            "items": [
                "✅ Học bơi từ nhỏ",
                "✅ Không bơi một mình",
                "✅ Mặc áo phao khi đi tàu thuyền",
                "✅ Không uống rượu khi bơi",
                "✅ Giám sát trẻ em khi gần nước"
            ]
        },
        "note": "⏱️ **QUAN TRỌNG:** Đuối nước gây tử vong nhanh. An toàn bản thân là trên hết!"
    },
    
    "electric_shock": {
        "name": "Điện giật",
        "icon": "⚡",
        "signs": {
            "title": "🔍 Dấu hiệu:",
            "items": [
                "Người bị điện giật đang tiếp xúc nguồn điện",
                "Co giật, không rời tay được",
                "Bỏng ở điểm tiếp xúc",
                "Ngất xỉu, ngừng thở"
            ]
        },
        "actions": {
            "title": "⚡ XỬ LÝ NGAY (An toàn bản thân trước!):",
            "steps": [
                "1️⃣ **TẮT NGUỒN ĐIỆN NGAY** - Rút phích cắm, tắt công tắc",
                "   - Nếu không tắt được → Dùng vật không dẫn điện (gỗ, nhựa) đẩy nạn nhân ra",
                "   - TUYỆT ĐỐI KHÔNG chạm vào nạn nhân khi còn điện!",
                "",
                "2️⃣ **GỌI 115 NGAY**",
                "",
                "3️⃣ **KIỂM TRA** thở, mạch",
                "",
                "4️⃣ **NẾU KHÔNG THỞ:**",
                "   - Bắt đầu CPR (ép tim + thổi ngạt)",
                "   - Tiếp tục cho đến khi xe cấp cứu đến",
                "",
                "5️⃣ **NẾU CÒN THỞ:**",
                "   - Đặt nằm nghiêng",
                "   - Giữ ấm",
                "   - Che vết bỏng bằng gạc sạch",
                "   - KHÔNG bôi gì lên vết bỏng"
            ]
        },
        "dont": {
            "title": "❌ TUYỆT ĐỐI KHÔNG:",
            "items": [
                "❌ KHÔNG chạm vào nạn nhân khi còn điện",
                "❌ KHÔNG dùng tay ướt, kim loại để kéo nạn nhân",
                "❌ KHÔNG bỏ cuộc CPR sớm"
            ]
        },
        "when_call_115": {
            "title": "🚨 GỌI 115 NGAY:",
            "items": [
                "⛔ Người bị điện giật (dù nhẹ)",
                "⛔ Bất tỉnh, ngừng thở",
                "⛔ Bỏng do điện (dù nhỏ)",
                "⛔ Điện giật ở trẻ em"
            ]
        },
        "note": "💡 **QUAN TRỌNG:** Điện giật có thể gây ngừng tim ngay. Xử trí nhanh quyết định sống còn!"
    }
}

def get_first_aid_guide(condition):
    """Lấy hướng dẫn sơ cứu theo tình trạng"""
    return FIRST_AID_GUIDES.get(condition)

