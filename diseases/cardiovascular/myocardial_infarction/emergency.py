"""
Nhồi Máu Cơ Tim - Xử trí cấp cứu và Khung giờ vàng
Emergency Management and Golden Time
"""

from typing import Dict, List

EMERGENCY_MANAGEMENT = {
    "golden_time": {
        "title": "⏰ KHUNG GIỜ VÀNG (Golden Time) - QUAN TRỌNG NHẤT!",
        "description": "Thời gian điều trị quyết định số phận cơ tim và tính mạng:",
        "time_windows": [
            {
                "time": "0-2 giờ đầu",
                "name": "GIỜ VÀNG TỐI ĐA",
                "description": "Càng điều trị SỚM trong khung này, càng tốt!",
                "treatment": [
                    "Tiêu sợi huyết (thrombolysis) - Phá vỡ cục máu đông",
                    "Can thiệp mạch vành (PCI) - Đặt stent mở mạch máu"
                ],
                "benefit": "Cứu được 90-95% cơ tim, giảm tử vong 50%",
                "mortality": "Tỷ lệ tử vong <5% nếu điều trị trong khung này",
                "warning": "⚠️ MỖI PHÚT TRÌ HOÃN = 2 TRIỆU TẾ BÀO CƠ TIM CHẾT!"
            },
            {
                "time": "2-6 giờ",
                "name": "GIỜ VÀNG MỞ RỘNG",
                "description": "Vẫn còn cơ hội điều trị hiệu quả",
                "treatment": [
                    "Tiêu sợi huyết vẫn hiệu quả",
                    "Can thiệp mạch vành là tốt nhất"
                ],
                "benefit": "Cứu được 70-80% cơ tim",
                "mortality": "Tỷ lệ tử vong 5-10%",
                "note": "Vẫn tốt, nhưng không tốt bằng 2 giờ đầu!"
            },
            {
                "time": "6-12 giờ",
                "name": "GIỜ VÀNG MUỘN",
                "description": "Cơ hội điều trị giảm đáng kể",
                "treatment": [
                    "Không còn tiêu sợi huyết (quá muộn)",
                    "Chỉ còn can thiệp mạch vành",
                    "Hoặc điều trị nội khoa (thuốc)"
                ],
                "benefit": "Cứu được 30-50% cơ tim",
                "mortality": "Tỷ lệ tử vong 10-20%",
                "warning": "⚠️ Cơ tim đã chết nhiều → Nguy cơ suy tim cao sau này!"
            },
            {
                "time": "Sau 12 giờ",
                "name": "QUÁ MUỘN",
                "description": "Cơ tim đã chết hết, không thể cứu",
                "treatment": [
                    "Điều trị nội khoa (thuốc) để bảo vệ phần cơ tim còn lại",
                    "Phòng ngừa biến chứng",
                    "Chăm sóc hỗ trợ"
                ],
                "benefit": "Không cứu được cơ tim, chỉ ngăn chặn biến chứng",
                "mortality": "Tỷ lệ tử vong 20-30%",
                "complications": "Suy tim mạn tính, loạn nhịp, nguy cơ nhồi máu lại",
                "warning": "🚨 Đừng để đến giai đoạn này!"
            }
        ],
        "summary": "💡 KẾT LUẬN: Điều trị TRONG 2 GIỜ ĐẦU = Tỷ lệ sống 95%, cứu được 90% cơ tim!"
    },
    
    "first_aid": {
        "title": "🚨 XỬ TRÍ NGAY KHI NGHI NGỜ NHỒI MÁU",
        "steps": [
            {
                "step": "1️⃣ GỌI 115 NGAY",
                "description": "KHÔNG đợi, KHÔNG tự lái xe",
                "why": [
                    "Xe cấp cứu có nhân viên y tế điều trị NGAY trên đường",
                    "Có thuốc tiêu sợi huyết trên xe",
                    "Báo trước bệnh viện → Chuẩn bị sẵn phòng can thiệp",
                    "An toàn hơn tự lái xe (có thể ngất, đau ngực khi lái)"
                ],
                "what_to_say": "Tôi nghi ngờ bị nhồi máu cơ tim. Đang có đau ngực, khó thở. Địa chỉ: [nói địa chỉ]"
            },
            {
                "step": "2️⃣ NGỒI/NẰM YÊN, TRÁNH GẮNG SỨC",
                "description": "Nghỉ ngơi hoàn toàn, không đi lại",
                "why": "Gắng sức → Tim đập nhanh → Cần nhiều máu → Tổn thương thêm",
                "position": [
                    "Ngồi tựa lưng, chân thả lỏng",
                    "Hoặc nằm đầu cao (kê 2-3 gối)",
                    "KHÔNG nằm phẳng (khó thở hơn)"
                ]
            },
            {
                "step": "3️⃣ NHAI ASPIRIN (nếu có)",
                "description": "Nhai 1 viên Aspirin 300mg (3-4 viên Aspirin 81mg)",
                "why": "Aspirin làm loãng máu → Giảm cục máu đông",
                "when": "Chỉ khi KHÔNG dị ứng aspirin, KHÔNG có chảy máu dạ dày",
                "how": "NHAI cho tan (hấp thu nhanh hơn nuốt)",
                "warning": "⚠️ Nếu không chắc → Đợi bác sĩ, KHÔNG tự uống!"
            },
            {
                "step": "4️⃣ NITROGLYCERIN (nếu có và đã được bác sĩ kê)",
                "description": "Ngậm 1 viên dưới lưỡi (nếu có)",
                "why": "Giãn mạch vành → Giảm đau ngực",
                "warning": "⚠️ CHỈ dùng nếu đã được bác sĩ kê trước đó. KHÔNG tự mua!"
            },
            {
                "step": "5️⃣ GIỮ ẤM, YÊN TĨNH",
                "description": "Đắp chăn nhẹ, giữ yên tĩnh",
                "why": "Tránh lo lắng → Tim đập nhanh → Tổn thương thêm",
                "note": "Người thân nên bình tĩnh, động viên, không hoảng loạn"
            },
            {
                "step": "6️⃣ KHÔNG cho ăn uống",
                "description": "KHÔNG cho uống nước, ăn gì",
                "why": [
                    "Có thể cần phẫu thuật cấp cứu (phải nhịn ăn)",
                    "Nguy cơ nôn → Sặc vào phổi",
                    "Nếu ngất → Dịch trào ngược"
                ]
            }
        ]
    },
    
    "dont_do": {
        "title": "❌ TUYỆT ĐỐI KHÔNG:",
        "items": [
            "❌ KHÔNG tự lái xe đến bệnh viện (có thể ngất khi lái → Tai nạn)",
            "❌ KHÔNG đợi xem có tự khỏi không (nhồi máu KHÔNG tự khỏi!)",
            "❌ KHÔNG cho uống nhiều nước (có thể cần phẫu thuật)",
            "❌ KHÔNG massage tim (chỉ khi ngừng tim hoàn toàn)",
            "❌ KHÔNG cho uống thuốc không rõ (trừ aspirin nếu chắc chắn)",
            "❌ KHÔNG hoảng loạn (làm tim đập nhanh → Tổn thương thêm)"
        ]
    },
    
    "hospital_preparation": {
        "title": "🏥 CHUẨN BỊ KHI ĐẾN BỆNH VIỆN",
        "description": "Những điều cần làm để điều trị nhanh:",
        "prepare": [
            {
                "item": "Mang theo danh sách thuốc đang uống",
                "why": "Bác sĩ cần biết để tránh tương tác thuốc"
            },
            {
                "item": "Mang theo kết quả khám cũ (nếu có)",
                "why": "So sánh ECG, giúp chẩn đoán nhanh"
            },
            {
                "item": "Nói rõ thời gian bắt đầu đau",
                "why": "Xác định khung giờ vàng, chọn phương pháp điều trị"
            },
            {
                "item": "Nói rõ dị ứng thuốc (nếu có)",
                "why": "Tránh dị ứng khi tiêu sợi huyết"
            },
            {
                "item": "Thông báo bệnh nền (tiểu đường, huyết áp cao...)",
                "why": "Điều chỉnh điều trị phù hợp"
            }
        ]
    }
}

