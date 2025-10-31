"""
Sơ cứu Tim Mạch & Thần Kinh
Cardiovascular & Neurological First Aid
"""

FIRST_AID_CARDIOVASCULAR = {
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
    }
}

