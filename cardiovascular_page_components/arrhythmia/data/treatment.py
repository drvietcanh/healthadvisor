"""
Treatment Data - Xử trí, khi nào khám, và thuốc điều trị
"""

ACTIONS = {
    "immediate": [
        "1️⃣ **Thở sâu, chậm:** Hít vào 4 giây, thở ra 4 giây (làm 5-10 lần)",
        "2️⃣ **Nằm nghỉ:** Nằm xuống, thả lỏng cơ thể",
        "3️⃣ **Uống nước:** Nếu khát hoặc mất nước",
        "4️⃣ **Loại bỏ nguyên nhân:** Nghỉ cà phê, rượu, thuốc cảm",
        "5️⃣ **Theo dõi mạch:** Đếm mạch trong 1 phút",
        "",
        "⏱️ **Nếu không đỡ sau 10 phút** hoặc triệu chứng nặng → Khám bác sĩ ngay"
    ],
    
    "prevention": [
        "✅ **Giảm stress:** Tập thiền, yoga, thư giãn",
        "✅ **Hạn chế cà phê:** Không quá 1-2 ly/ngày",
        "✅ **Ngủ đủ:** 7-9 giờ/đêm",
        "✅ **Tập thể dục vừa phải:** Đi bộ 30 phút/ngày",
        "✅ **Không hút thuốc:** Thuốc lá hại tim",
        "✅ **Kiểm soát huyết áp:** Uống thuốc đều đặn",
        "✅ **Giữ cân nặng hợp lý:** Tránh béo phì"
    ]
}

WHEN_TO_SEE_DOCTOR = {
    "urgent": [
        "🚨 **GỌI 115 NGAY NẾU:**",
        "",
        "- **Ngất xỉu** (mất ý thức)",
        "- **Đau ngực dữ dội** (đau như bị đè ép)",
        "- **Tim đập > 150 nhịp/phút** kèm khó thở",
        "- **Tim < 40 nhịp/phút** kèm chóng mặt",
        "- **Không thở được**",
        "- **Đang có bệnh tim** + triệu chứng mới"
    ],
    
    "soon": [
        "📋 **KHÁM BÁC SĨ TRONG TUẦN NẾU:**",
        "",
        "- Tim bỏ sót nhịp **thường xuyên** (> 5 lần/phút)",
        "- Hồi hộp **kéo dài > 30 phút** không đỡ",
        "- **Mệt mỏi, khó thở** kéo dài",
        "- **Lần đầu tiên** bị rối loạn nhịp tim",
        "- Đang dùng thuốc tim mạch + triệu chứng mới"
    ]
}

MEDICATIONS = {
    "antiarrhythmic": {
        "name": "💊 Thuốc Chống Loạn Nhịp",
        "examples": [
            "**Metoprolol (Betabloc)** - Giảm tim nhanh, hạ huyết áp",
            "**Digoxin** - Tăng sức co bóp tim, chậm nhịp",
            "**Amiodarone** - Chống nhiều loại loạn nhịp (mạnh)",
            "**Verapamil** - Giảm tim nhanh"
        ],
        "note": "⚠️ Uống đúng giờ, đúng liều. KHÔNG tự ý ngưng thuốc!"
    },
    
    "anticoagulation": {
        "name": "💊 Thuốc Chống Đông (Với Rung Nhĩ)",
        "examples": [
            "**Warfarin** - Thuốc cũ, phải xét nghiệm máu",
            "**Apixaban, Dabigatran** - Thuốc mới, không cần xét nghiệm"
        ],
        "note": "🩸 Phòng ngừa đột quỵ do cục máu đông. Dễ chảy máu → Tránh va đập!"
    },
    
    "pacemaker": {
        "name": "🔋 Máy Tạo Nhịp Tim (Pacemaker)",
        "description": "Khi tim đập quá chậm → Gắn máy tạo nhịp",
        "types": [
            "**Tạm thời:** Qua tĩnh mạch, dùng vài ngày",
            "**Vĩnh viễn:** Phẫu thuật gắn máy dưới da"
        ],
        "after_surgery": [
            "✅ Nghỉ ngơi 1 tuần sau phẫu thuật",
            "✅ Tránh động tác tay mạnh 1 tháng",
            "✅ Không đến gần máy quét an ninh",
            "✅ Theo dõi định kỳ mỗi 6 tháng"
        ]
    }
}

