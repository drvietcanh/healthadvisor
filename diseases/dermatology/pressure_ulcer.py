"""
Loét Tì Đè (Pressure Ulcer/Bedsores)
=====================================
"""

PRESSURE_ULCER_INFO = {
    "name_vn": "Loét Tì Đè",
    "name_en": "Pressure Ulcer/Bedsores",
    
    "simple_explanation": """
💡 **Loét tì đè là gì?**

Giống như da bị "đè ép" quá lâu:
- **Nằm liệt, ngồi xe lăn** → Một chỗ da bị đè ép liên tục
- **Máu không đến được** → Da thiếu máu → Chết → Loét
- **Khó lành** vì vẫn tiếp tục bị đè ép

→ Giống như ống nước bị kẹp → Không có nước → Khô héo!
    """,
    
    "what_happens": """
Chuyện gì xảy ra:

1. **Áp lực lên da:**
   - Người nằm liệt → Vùng xương cụt, gót chân bị đè ép
   - Áp lực chặn mạch máu → Không có máu nuôi da

2. **Da chết, loét:**
   - Thiếu máu → Da chết
   - Vết loét hình thành
   - Có thể sâu đến xương

3. **Nếu không xử trí:**
   - Loét lan rộng, sâu
   - Nhiễm trùng
   - Nguy hiểm đến tính mạng (hiếm)
    """,
    
    "stages": {
        "stage_1": {
            "name": "Độ 1 (Giai đoạn sớm)",
            "description": "Da đỏ, không biến mất khi ấn nhẹ (không có vết loét)",
            "action": "Xử trí ngay: Giảm áp lực, xoay trở thường xuyên"
        },
        "stage_2": {
            "name": "Độ 2 (Vết loét nông)",
            "description": "Da mất một phần (lớp ngoài), đỏ, có thể có mụn nước",
            "action": "Chăm sóc vết thương, giảm áp lực tuyệt đối"
        },
        "stage_3": {
            "name": "Độ 3 (Vết loét sâu)",
            "description": "Mất toàn bộ lớp da, thấy mỡ dưới da (chưa đến xương)",
            "action": "Chăm sóc vết thương chuyên khoa, có thể cần phẫu thuật"
        },
        "stage_4": {
            "name": "Độ 4 (Vết loét rất sâu)",
            "description": "Loét đến xương, gân, có thể thấy xương",
            "action": "Phẫu thuật, điều trị chuyên khoa - Nguy hiểm cao"
        }
    },
    
    "symptoms": {
        "common": [
            "Vùng da đỏ, không biến mất khi ấn (độ 1)",
            "Da nứt, có vết loét (độ 2+)",
            "Đau nhức (đặc biệt khi chạm vào)",
            "Da lạnh, cứng hơn vùng xung quanh",
            "Có thể có mủ, mùi hôi (nhiễm trùng)"
        ],
        "common_locations": [
            "🫳 **Xương cụt** (mông) - Phổ biến nhất (nằm liệt)",
            "🦶 **Gót chân** - Thứ hai (nằm liệt)",
            "🦴 **Xương cùng** - Thứ ba",
            "💪 **Khuỷu tay** - Ít gặp (nằm nghiêng)",
            "👂 **Tai** - Hiếm (nằm nghiêng)",
            "👤 **Vai** - Hiếm (nằm nghiêng)"
        ],
        "warning_signs": [
            "🚨 **Đỏ da không biến mất khi ấn:**",
            "   - Đây là dấu hiệu ĐẦU TIÊN → Xử trí NGAY",
            "",
            "🚨 **Có mủ, mùi hôi:**",
            "   - Nhiễm trùng → Nguy hiểm",
            "",
            "🚨 **Sốt, ớn lạnh:**",
            "   - Nhiễm trùng lan rộng → CẦN KHÁM NGAY",
            "",
            "🚨 **Vết loét sâu, thấy xương:**",
            "   - Độ 4 → Rất nguy hiểm"
        ]
    },
    
    "causes": {
        "main": [
            "Nằm liệt, không xoay trở (nguyên nhân chính)",
            "Ngồi xe lăn lâu",
            "Áp lực liên tục lên một vùng da (đặc biệt vùng xương)",
            "Ma sát (kéo lê trên giường)",
            "Da ẩm ướt (nước tiểu, mồ hôi) → Dễ tổn thương"
        ],
        "risk_factors": [
            "👴 **Tuổi cao:** Da mỏng, dễ tổn thương",
            "🛏️ **Nằm liệt:** Không thể tự xoay trở",
            "🏥 **Bệnh nền:**",
            "   - Tiểu đường (chậm lành)",
            "   - Bệnh tim mạch (thiếu máu đến da)",
            "   - Suy dinh dưỡng (thiếu protein để lành)",
            "",
            "💧 **Da ẩm ướt:**",
            "   - Tiểu không tự chủ",
            "   - Mồ hôi nhiều",
            "",
            "🚭 **Hút thuốc:** Giảm lưu thông máu"
        ]
    },
    
    "treatment": {
        "prevention_first": {
            "title": "🛡️ PHÒNG NGỪA là QUAN TRỌNG NHẤT (Độ 1):",
            "steps": [
                "1. **Xoay trở thường xuyên:**",
                "   - Mỗi 2 giờ (nếu nằm liệt)",
                "   - Xoay trở 30° (nghiêng trái, phải, nằm ngửa)",
                "   - Không để một chỗ bị đè ép quá lâu",
                "",
                "2. **Giảm áp lực:**",
                "   - Đệm chống loét (đệm nước, đệm khí)",
                "   - Gối nhỏ kê dưới gót chân (nâng lên khỏi giường)",
                "   - Gối kê giữa 2 đầu gối (khi nằm nghiêng)",
                "",
                "3. **Kiểm tra da hàng ngày:**",
                "   - Xem có vùng đỏ không?",
                "   - Ấn nhẹ → Đỏ biến mất = OK, không biến mất = Cảnh báo!",
                "",
                "4. **Giữ da khô ráo, sạch sẽ:**",
                "   - Lau khô sau khi tắm, đi tiểu",
                "   - Dùng kem bảo vệ da (barrier cream) nếu da ẩm",
                "",
                "5. **Dinh dưỡng tốt:**",
                "   - Đủ protein (thịt, cá, đậu) → Giúp da lành",
                "   - Đủ vitamin C (cam, ổi) → Tăng đề kháng"
            ]
        },
        "stage_2_3": {
            "title": "💊 Điều trị vết loét (Độ 2-3):",
            "steps": [
                "1. **Giảm áp lực tuyệt đối:**",
                "   - Không để vết loét bị đè ép",
                "   - Xoay trở thường xuyên hơn (mỗi 1-2 giờ)",
                "",
                "2. **Vệ sinh vết loét:**",
                "   - Rửa bằng nước muối sinh lý",
                "   - Băng vết thương (gạc không dính)",
                "   - Thay băng hàng ngày",
                "",
                "3. **Thuốc bôi (theo chỉ định bác sĩ):**",
                "   - Bôi kháng sinh nếu có nhiễm trùng",
                "   - Gel/salve giúp lành vết thương",
                "",
                "4. **Dinh dưỡng:**",
                "   - Tăng protein (thịt, cá, trứng, sữa)",
                "   - Bổ sung vitamin C, kẽm"
            ]
        },
        "when_to_see_doctor": {
            "title": "🏥 Khi nào cần đi khám bác sĩ (KHÁM NGAY nếu):",
            "reasons": [
                "❌ Vết loét độ 2-3-4 (đã có vết loét)",
                "❌ Có mủ, mùi hôi (nhiễm trùng)",
                "❌ Sốt, ớn lạnh (nhiễm trùng lan)",
                "❌ Vết loét không lành sau 2 tuần",
                "❌ Vết loét sâu, thấy xương (độ 4)",
                "❌ Đỏ da không biến mất (độ 1) sau 2 ngày xử trí"
            ]
        },
        "doctor_treatment": {
            "title": "💊 Bác sĩ sẽ làm gì:",
            "options": [
                "📋 **Đánh giá độ nặng:**",
                "   - Đo độ sâu, kích thước vết loét",
                "   - Phân loại độ 1-4",
                "",
                "🔬 **Cấy mủ (nếu nhiễm trùng):**",
                "   - Xác định vi khuẩn",
                "   - Kê kháng sinh phù hợp",
                "",
                "💊 **Thuốc điều trị:**",
                "   - Kháng sinh uống (nếu nhiễm trùng)",
                "   - Thuốc bôi đặc biệt (dressing chuyên khoa)",
                "   - Gel/salve giúp lành vết thương",
                "",
                "🏥 **Chăm sóc vết thương chuyên khoa:**",
                "   - Băng vết thương đúng cách",
                "   - Thay băng định kỳ",
                "",
                "⚡ **Phẫu thuật (nếu độ 4):**",
                "   - Cắt bỏ mô chết",
                "   - Ghép da (nếu cần)",
                "",
                "📋 **Tư vấn phòng ngừa:**",
                "   - Đệm chống loét",
                "   - Kỹ thuật xoay trở",
                "   - Dinh dưỡng"
            ]
        }
    },
    
    "prevention": {
        "title": "🛡️ Cách phòng ngừa loét tì đè:",
        "tips": [
            "✅ **Xoay trở thường xuyên (QUAN TRỌNG NHẤT):**",
            "   - Mỗi 2 giờ (nếu nằm liệt)",
            "   - Xoay trở 30° (nghiêng trái, phải, nằm ngửa)",
            "   - Đặt đồng hồ báo thức",
            "",
            "✅ **Đệm chống loét:**",
            "   - Đệm nước hoặc đệm khí",
            "   - Phân tán áp lực đều",
            "   - Đặc biệt quan trọng cho người nằm liệt",
            "",
            "✅ **Gối hỗ trợ:**",
            "   - Gối nhỏ kê dưới gót chân (nâng lên)",
            "   - Gối giữa 2 đầu gối (khi nằm nghiêng)",
            "   - Tránh gối dưới đầu gối (tăng áp lực gót chân)",
            "",
            "✅ **Kiểm tra da hàng ngày:**",
            "   - Xem có vùng đỏ không?",
            "   - Ấn nhẹ → Đỏ biến mất = OK",
            "   - Đỏ không biến mất = Cảnh báo → Xử trí ngay!",
            "",
            "✅ **Giữ da khô ráo, sạch sẽ:**",
            "   - Tắm rửa hàng ngày",
            "   - Lau khô kỹ (đặc biệt vùng xương cụt, gót chân)",
            "   - Dùng kem bảo vệ da nếu da ẩm (barrier cream)",
            "",
            "✅ **Dinh dưỡng tốt:**",
            "   - Đủ protein (thịt, cá, đậu) → Giúp da khỏe",
            "   - Đủ vitamin C (cam, ổi) → Tăng đề kháng",
            "   - Đủ nước (1.5-2 lít/ngày) → Giữ da đủ ẩm",
            "",
            "✅ **Vận động nhẹ (nếu có thể):**",
            "   - Tập ngồi dậy (nếu có thể)",
            "   - Cử động tay chân (nếu có thể)",
            "   - Tăng lưu thông máu"
        ]
    },
    
    "note": """
⚠️ **LƯU Ý QUAN TRỌNG:**
- PHÒNG NGỪA là QUAN TRỌNG NHẤT → Xoay trở mỗi 2 giờ
- Đỏ da không biến mất khi ấn = Dấu hiệu ĐẦU TIÊN → Xử trí NGAY
- Loét tì đè KHÓ lành → Cần thời gian, kiên trì
- Nhiễm trùng nguy hiểm → Có mủ, mùi hôi, sốt → KHÁM NGAY
- Người nằm liệt + tiểu đường → Nguy cơ cao nhất → Phải phòng ngừa rất cẩn thận
- Đệm chống loét là đầu tư cần thiết (không phải xa xỉ)
    """
}

