"""
Sơ cứu Môi Trường & Tai Nạn
Environmental First Aid (Đuối nước, Điện giật)
"""

FIRST_AID_ENVIRONMENTAL = {
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

