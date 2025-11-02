"""
Types & Causes - Các loại rối loạn nhịp và nguyên nhân
"""

TYPES = {
    "tachycardia": {
        "name": "❤️‍🩹 Tim Đập Nhanh (Tachycardia)",
        "description": "Tim đập **> 100 nhịp/phút** khi nghỉ",
        "examples": [
            "**Sinus tachycardia:** Tim nhanh bình thường (do căng thẳng, uống cà phê)",
            "**Atrial fibrillation:** Tim rung nhĩ, đập không đều (nguy hiểm!)",
            "**Supraventricular:** Tim đập nhanh đột ngột ở người trẻ"
        ],
        "treatment": "Tùy loại: Thở sâu → Thuốc → Sốc điện → Đốt điện",
        "when_worry": "Tim > 150 nhịp/phút kèm khó thở/đau ngực → Gọi 115"
    },
    
    "bradycardia": {
        "name": "❤️‍🩹 Tim Đập Chậm (Bradycardia)",
        "description": "Tim đập **< 60 nhịp/phút**",
        "examples": [
            "**Người khỏe mạnh:** Vận động viên tim đập 40-50 nhịp/phút (bình thường)",
            "**Sick sinus:** Mạch chậm do bệnh tim sẵn có",
            "**Heart block:** Tim bỏ sót nhịp do dẫn truyền bị tắc"
        ],
        "treatment": "Không triệu chứng: Theo dõi. Có triệu chứng: Máy tạo nhịp",
        "when_worry": "Tim < 40 nhịp/phút kèm chóng mặt/ngất → Gọi 115"
    },
    
    "premature": {
        "name": "❤️‍🩹 Tim Bỏ Sót Nhịp (Premature Beat)",
        "description": "Tim đập thêm 1 nhịp sớm, sau đó nghỉ dài rồi đập mạnh",
        "examples": [
            "**PAC:** Nhịp sớm ở tâm nhĩ (ít nguy hiểm)",
            "**PVC:** Nhịp sớm ở tâm thất (cần khám nếu thường xuyên)"
        ],
        "treatment": "Ít: Không cần điều trị. Nhiều: Thuốc, loại bỏ nguyên nhân",
        "when_worry": "Bỏ sót > 5 lần/phút kèm khó thở → Khám bác sĩ"
    }
}

COMMON_CAUSES = {
    "reversible": [
        "**Căng thẳng (Stress)** - Lo lắng, sợ hãi",
        "**Cà phê, trà đậm** - Quá nhiều caffeine",
        "**Rượu, bia** - Sau khi uống",
        "**Thiếu ngủ** - Mệt mỏi kéo dài",
        "**Thuốc** - Thuốc cảm, hen suyễn",
        "**Thiếu nước** - Mất nước"
    ],
    
    "heart_disease": [
        "**Bệnh tim sẵn có** - Bệnh mạch vành, suy tim",
        "**Sau nhồi máu cơ tim** - Tim bị tổn thương",
        "**Bệnh van tim** - Van tim hư hỏng",
        "**Bẩm sinh** - Tim bất thường từ nhỏ"
    ],
    
    "other": [
        "**Tăng huyết áp** - Huyết áp cao lâu ngày",
        "**Rối loạn tuyến giáp** - Cường giáp (tim nhanh)",
        "**Rối loạn điện giải** - Thiếu kali, magie",
        "**Tuổi già** - Tổn thương tim do tuổi tác"
    ]
}

