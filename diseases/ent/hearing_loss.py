"""
Điếc/Lãng Tai (Hearing Loss)
================================
Bao gồm: Điếc tuổi già, Điếc do tiếng ồn, Điếc đột ngột
"""

HEARING_LOSS_INFO = {
    "name_vn": "Điếc/Lãng Tai",
    "name_en": "Hearing Loss",
    
    "simple_explanation": """
💡 **Điếc/Lãng tai là gì?**

Giống như radio bị mất tín hiệu:
- **Tai không nghe được** hoặc nghe kém hơn trước
- **Có thể một bên** hoặc cả hai bên
- **Người già** thường bị điếc tuổi già (nghe kém dần)

→ Giống như radio cần chỉnh lại âm lượng hoặc sửa máy!
    """,
    
    "what_happens": """
Chuyện gì xảy ra:

1. **Tai không nhận được âm thanh:**
   - Âm thanh → Vào tai ngoài → Tai giữa → Tai trong → Não
   - Bất kỳ bước nào bị hỏng → Không nghe được

2. **Có 3 loại điếc chính:**
   - **Điếc dẫn truyền:** Tai ngoài/giữa bị tắc (ráy tai, viêm tai)
   - **Điếc cảm giác-thần kinh:** Tai trong/ thần kinh bị hỏng (phổ biến nhất)
   - **Điếc hỗn hợp:** Cả hai loại trên

3. **Điếc đột ngột:**
   - Mất thính lực ≥30dB trong ≤3 ngày
   - Cần đi khám NGAY (trong 24-48 giờ đầu)
    """,
    
    "symptoms": {
        "common": [
            "Nghe kém, phải nói to mới nghe được",
            "Thường xuyên hỏi lại \"Hả?\", \"Gì?\"",
            "Nói to hơn bình thường (vì không nghe được giọng mình)",
            "Tăng âm lượng TV/radio (người nhà phàn nàn quá to)",
            "Khó nghe trong môi trường ồn (quán cà phê, tiếng ồn đường)",
            "Nghe như có tiếng vo ve, ù ù trong tai",
            "Lẫn lộn giữa các từ (nghe nhầm \"bác sĩ\" thành \"hạt sen\")"
        ],
        "warning_signs": [
            "🚨 **ĐIẾC ĐỘT NGỘT - CẦN CẤP CỨU NGAY:**",
            "   - Mất thính lực đột ngột trong vài giờ/ngày",
            "   - Thường một bên tai",
            "   - Có thể kèm ù tai, chóng mặt",
            "   - ⚠️ ĐI KHÁM TRONG 24-48 GIỜ ĐẦU → Có thể phục hồi!",
            "   - Sau 2 tuần → Khó phục hồi"
        ]
    },
    
    "causes": {
        "age_related": {
            "title": "👴 Điếc tuổi già (Presbycusis):",
            "description": "Người > 60 tuổi thường nghe kém dần theo tuổi",
            "why": [
                "Tế bào thính giác trong tai già đi và chết dần",
                "Không nghe được âm thanh cao (tiếng chim, điện thoại reo)",
                "Tiến triển từ từ (nhiều năm), không đau đớn"
            ]
        },
        "noise_induced": {
            "title": "🔊 Điếc do tiếng ồn:",
            "description": "Tiếp xúc với tiếng ồn quá lớn trong thời gian dài",
            "sources": [
                "Nghe nhạc quá to qua tai nghe",
                "Làm việc trong môi trường ồn (nhà máy, công trường)",
                "Súng nổ, pháo nổ gần tai",
                "Máy cắt cỏ, máy khoan không có bảo vệ"
            ]
        },
        "sudden_hearing_loss": {
            "title": "🚨 Điếc đột ngột (Sudden Sensorineural Hearing Loss - SSNHL):",
            "description": "Mất thính lực đột ngột, thường một bên tai",
            "causes": [
                "Nhiễm virus (cảm cúm, quai bị)",
                "Chấn thương đầu/tai",
                "Thuốc độc với tai (một số kháng sinh, thuốc lợi tiểu)",
                "Stress căng thẳng quá mức",
                "Không rõ nguyên nhân (70% trường hợp)"
            ],
            "urgent": "⚠️ ĐI KHÁM NGAY - Trong 24-48 giờ đầu có thể phục hồi!"
        },
        "other": [
            "Ráy tai quá nhiều (tắc ống tai)",
            "Viêm tai giữa, viêm tai ngoài",
            "Bệnh Meniere (chóng mặt + điếc + ù tai)",
            "Khối u thần kinh (hiếm nhưng nguy hiểm)"
        ]
    },
    
    "treatment": {
        "sudden_hearing_loss": {
            "title": "🚨 ĐIẾC ĐỘT NGỘT - XỬ TRÍ CẤP CỨU:",
            "urgency": "⚠️ ĐI KHÁM NGAY - Trong 24-48 giờ đầu!",
            "why_urgent": [
                "Điều trị sớm → Có thể phục hồi hoàn toàn",
                "Sau 2 tuần → Khó phục hồi",
                "Bác sĩ sẽ cho thuốc corticoid liều cao (Prednisolone)",
                "Có thể kèm thuốc giãn mạch, vitamin"
            ],
            "do_not": [
                "❌ KHÔNG được tự ý bỏ qua (\"Để mai xem\")",
                "❌ KHÔNG tự uống thuốc",
                "❌ KHÔNG chờ \"tự khỏi\""
            ]
        },
        "age_related": {
            "title": "👴 Điếc tuổi già - Điều trị:",
            "options": [
                "**Máy trợ thính:**",
                "   - Giúp khuếch đại âm thanh",
                "   - Cần đo thính lực để chọn máy phù hợp",
                "   - Giá: 5-50 triệu (tùy loại)",
                "   - Bảo hiểm có thể hỗ trợ một phần",
                "",
                "**Kỹ thuật giao tiếp:**",
                "   - Người thân nói rõ ràng, chậm rãi",
                "   - Nhìn vào mặt khi nói (đọc môi)",
                "   - Tránh nói ở nơi ồn",
                "   - Viết ra giấy nếu cần"
            ]
        },
        "noise_induced": {
            "title": "🔊 Điếc do tiếng ồn:",
            "prevention": [
                "✅ Dùng nút bịt tai khi làm việc ồn",
                "✅ Giảm âm lượng khi nghe nhạc (≤60% mức tối đa)",
                "✅ Nghỉ ngơi sau khi tiếp xúc với tiếng ồn",
                "⚠️ Không thể phục hồi hoàn toàn, chỉ có thể ngăn chặn tiến triển"
            ]
        },
        "other": {
            "wax": "Ráy tai → Rửa tai tại phòng khám",
            "infection": "Viêm tai → Kháng sinh, chống viêm",
            "when_to_see_doctor": [
                "✅ Điếc đột ngột (NGAY LẬP TỨC)",
                "✅ Điếc ngày càng nặng",
                "✅ Điếc một bên tai",
                "✅ Kèm chóng mặt, ù tai",
                "✅ Điếc do chấn thương"
            ]
        }
    },
    
    "prevention": {
        "title": "🛡️ Cách phòng ngừa điếc:",
        "tips": [
            "✅ **Bảo vệ tai khỏi tiếng ồn:**",
            "   - Dùng nút bịt tai khi làm việc/lái xe ồn",
            "   - Giảm âm lượng khi nghe nhạc (≤60%)",
            "   - Không nghe tai nghe quá 1 giờ liên tục",
            "   - Nghỉ 10 phút sau mỗi giờ nghe",
            "",
            "✅ **Vệ sinh tai đúng cách:**",
            "   - Không dùng tăm bông đưa sâu vào tai (đẩy ráy vào sâu hơn)",
            "   - Chỉ lau vành tai, ống tai ngoài",
            "   - Nếu ráy tai nhiều → Đến bác sĩ rửa",
            "",
            "✅ **Khám tai định kỳ:**",
            "   - Người > 60 tuổi: Khám 1-2 lần/năm",
            "   - Đo thính lực (Audiometry) để phát hiện sớm",
            "",
            "✅ **Tránh thuốc độc với tai:**",
            "   - Một số kháng sinh (Gentamicin, Streptomycin) → Chỉ dùng khi thực sự cần",
            "   - Thuốc lợi tiểu (Furosemide) → Theo dõi thính lực",
            "   - Luôn hỏi bác sĩ về tác dụng phụ"
        ]
    },
    
    "hearing_aids": {
        "title": "👂 Máy trợ thính:",
        "when_needed": "Cần khi điếc từ trung bình trở lên (khó nghe trong giao tiếp hàng ngày)",
        "types": [
            "**Máy đeo sau tai (BTE):**",
            "   - Phù hợp mọi mức độ điếc",
            "   - Giá: 10-30 triệu",
            "   - Dễ sử dụng, bền",
            "",
            "**Máy đeo trong tai (ITE):**",
            "   - Nhỏ gọn, kín đáo",
            "   - Giá: 15-50 triệu",
            "   - Cần đo tai để làm vừa",
            "",
            "**Máy cấy trong tai (Cochlear Implant):**",
            "   - Cho điếc nặng/sâu",
            "   - Cần phẫu thuật",
            "   - Giá: 300-500 triệu (bảo hiểm có thể hỗ trợ)"
        ],
        "note": "⚠️ Máy trợ thính KHÔNG chữa khỏi điếc, chỉ giúp nghe tốt hơn. Cần thời gian để quen (2-4 tuần)."
    },
    
    "note": """
⚠️ **LƯU Ý QUAN TRỌNG:**

**ĐIẾC ĐỘT NGỘT:**
- ⚠️ CẦN ĐI KHÁM NGAY - Trong 24-48 giờ đầu!
- Sau 2 tuần → Khó phục hồi
- Đừng chờ \"tự khỏi\" → Mất cơ hội phục hồi

**ĐIẾC TUỔI GIÀ:**
- Bình thường ở người > 60 tuổi
- Cần máy trợ thính để giao tiếp tốt
- Không thể \"chữa khỏi\" nhưng có thể cải thiện

**ĐIẾC DO TIẾNG ỒN:**
- Không thể phục hồi → Quan trọng là phòng ngừa!
- Dùng bảo vệ tai ngay từ đầu
    """
}

