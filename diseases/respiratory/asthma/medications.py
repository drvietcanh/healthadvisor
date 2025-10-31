"""
Asthma Medications - Thuốc điều trị Hen Suyễn
===============================================

Hướng dẫn về các loại thuốc điều trị hen suyễn
"""

# Thuốc cắt cơn (Reliever - SABA)
QUICK_RELIEF_MEDICATIONS = {
    "title": "⚡ Thuốc Cắt Cơn (Cấp Cứu)",
    
    "description": """
💡 Thuốc cắt cơn dùng khi:
- Đang lên cơn hen
- Khó thở đột ngột
- Trước khi tập thể dục (nếu bác sĩ chỉ định)

→ Tác dụng NHANH (5-15 phút), không dùng hàng ngày!
    """,
    
    "salbutamol": {
        "name": "Salbutamol (Ventolin, Asthalin)",
        "forms": ["Xịt", "Khí dung", "Viên nén"],
        "how_it_works": "Giãn phế quản NGAY LẬP TỨC",
        "onset": "5-15 phút",
        "duration": "4-6 giờ",
        "when_to_use": [
            "Đang lên cơn hen",
            "Khó thở đột ngột",
            "Trước tập thể dục (nếu bác sĩ chỉ định)"
        ],
        "dosage": {
            "adult": "1-2 nhát xịt/lần, tối đa 4-6 lần/ngày",
            "child": "1 nhát xịt/lần",
            "warning": "Nếu dùng >3-4 lần/tuần → Cần điều trị dự phòng!"
        },
        "side_effects": [
            "Run tay nhẹ (bình thường)",
            "Tim đập nhanh (tạm thời)",
            "Đau đầu"
        ],
        "brand_names_vn": [
            "Ventolin",
            "Asthalin",
            "Salbutamol STADA",
            "Salbutamol Mekophar"
        ],
        "price": "50,000-100,000đ/lọ"
    },
    
    "terbutaline": {
        "name": "Terbutaline (Bricanyl)",
        "forms": ["Xịt", "Khí dung"],
        "how_it_works": "Giống Salbutamol, tác dụng dài hơn một chút",
        "onset": "10-15 phút",
        "duration": "4-6 giờ",
        "brand_names_vn": ["Bricanyl"],
        "note": "Ít phổ biến hơn Salbutamol tại VN"
    }
}

# Thuốc kiểm soát (Controller - ICS, LABA)
CONTROLLER_MEDICATIONS = {
    "title": "🛡️ Thuốc Kiểm Soát (Dự Phòng)",
    
    "description": """
💡 Thuốc kiểm soát dùng HÀNG NGÀY để:
- NGĂN cơn hen xảy ra
- Giảm viêm đường thở
- Kiểm soát bệnh lâu dài

→ Phải dùng ĐỀU ĐẶN, KHÔNG bỏ quên!
    """,
    
    "ics": {
        "title": "1. Corticosteroid xịt (ICS)",
        "description": "Thuốc CHÍNH điều trị hen, giảm viêm",
        "medications": [
            {
                "name": "Beclomethasone (Becotide, Qvar)",
                "dose": "100-400mcg x 2 lần/ngày",
                "brand_names_vn": ["Becotide", "Clenil"],
                "price": "200,000-400,000đ/lọ",
                "note": "Dùng lâu dài an toàn (xịt, không phải uống)"
            },
            {
                "name": "Budesonide (Pulmicort)",
                "dose": "200-400mcg x 2 lần/ngày",
                "brand_names_vn": ["Pulmicort", "Budecort"],
                "price": "250,000-500,000đ/lọ",
                "note": "Phổ biến tại VN"
            },
            {
                "name": "Fluticasone (Flixotide)",
                "dose": "125-250mcg x 2 lần/ngày",
                "brand_names_vn": ["Flixotide"],
                "price": "300,000-600,000đ/lọ",
                "note": "Tác dụng mạnh, dùng cho hen nặng"
            }
        ],
        "side_effects": [
            "Khản giọng (súc miệng sau xịt → giảm)",
            "Nấm miệng (hiếm, súc miệng → tránh)",
            "Ho nhẹ khi mới dùng",
            "⚠️ KHÔNG gây tăng cân, loãng xương (vì xịt, không uống!)"
        ],
        "important": "Phải dùng ĐỀU ĐẶN, không bỏ quên → Mới có hiệu quả!"
    },
    
    "ics_laba": {
        "title": "2. ICS + LABA (Thuốc kết hợp)",
        "description": "2 trong 1: Corticosteroid + Giãn phế quản dài hạn",
        "medications": [
            {
                "name": "Seretide (Fluticasone + Salmeterol)",
                "brand_names_vn": ["Seretide", "Airflusal"],
                "dose": "Xịt 2 lần/ngày",
                "price": "500,000-800,000đ/lọ",
                "note": "Phổ biến nhất tại VN"
            },
            {
                "name": "Symbicort (Budesonide + Formoterol)",
                "brand_names_vn": ["Symbicort"],
                "dose": "Xịt 2 lần/ngày",
                "price": "600,000-900,000đ/lọ",
                "note": "Tác dụng nhanh hơn Seretide"
            },
            {
                "name": "Foster (Beclomethasone + Formoterol)",
                "brand_names_vn": ["Foster"],
                "dose": "Xịt 2 lần/ngày",
                "price": "400,000-700,000đ/lọ"
            }
        ],
        "when_to_use": "Hen vừa → nặng, không kiểm soát được bằng ICS đơn",
        "benefit": "Tiện lợi, chỉ cần 1 lọ thay vì 2 lọ"
    },
    
    "ltra": {
        "title": "3. Montelukast (Singulair)",
        "description": "Thuốc uống, chống dị ứng, giảm viêm",
        "forms": ["Viên", "Bột (trẻ em)"],
        "dosage": {
            "adult": "10mg/ngày (tối)",
            "child_6_14": "5mg/ngày",
            "child_2_5": "4mg/ngày"
        },
        "when_to_use": [
            "Hen do dị ứng",
            "Hen do tập thể dục",
            "Hen nhẹ, không muốn xịt",
            "Kết hợp với ICS nếu chưa đủ"
        ],
        "brand_names_vn": ["Singulair", "Montelukast"],
        "price": "150,000-300,000đ/tháng",
        "side_effects": [
            "Đau đầu (hiếm)",
            "Rối loạn hành vi trẻ em (rất hiếm)",
            "Thường không có tác dụng phụ"
        ]
    }
}

# Kỹ thuật xịt thuốc
INHALER_TECHNIQUE = {
    "title": "🎯 Cách Xịt Thuốc ĐÚNG",
    
    "importance": "Xịt SAI → Thuốc không vào phổi → Không hiệu quả!",
    
    "steps": [
        {
            "step": 1,
            "action": "Lắc lọ thuốc",
            "note": "Trộn đều thuốc"
        },
        {
            "step": 2,
            "action": "Thở ra HẾT sức",
            "note": "Đẩy hết không khí ra"
        },
        {
            "step": 3,
            "action": "Ngậm kín miệng xịt",
            "note": "Môi bọc quanh ống xịt"
        },
        {
            "step": 4,
            "action": "Nhấn xịt + HÍT SÂU chậm",
            "note": "Hít vào miệng, thở ra mũi"
        },
        {
            "step": 5,
            "action": "Nín thở 5-10 giây",
            "note": "Giữ thuốc trong phổi"
        },
        {
            "step": 6,
            "action": "Thở ra chậm",
            "note": "Qua miệng"
        }
    ],
    
    "common_mistakes": [
        "Xịt nhưng không hít",
        "Hít quá nhanh",
        "Không ngậm kín",
        "Xịt nhiều lần liên tiếp (chỉ cần 1-2 lần)"
    ],
    
    "spacer": {
        "title": "💡 Dùng Ống Spacer (Buồng đệm)",
        "benefit": "Dễ dùng hơn, thuốc vào phổi nhiều hơn",
        "when_to_use": [
            "Trẻ em",
            "Người già",
            "Khó phối hợp tay-miệng",
            "Hen nặng"
        ],
        "how_to_use": [
            "Xịt 1 lần vào spacer",
            "Thở ra",
            "Ngậm miệng vào spacer",
            "Hít vào chậm 3-5 lần",
            "Nín thở 5 giây"
        ],
        "price": "100,000-200,000đ/ống"
    },
    
    "after_ics": {
        "title": "⚠️ Sau khi xịt ICS (Corticosteroid)",
        "action": "SÚC MIỆNG bằng nước → Súc họng → Nhổ ra",
        "reason": "Tránh nấm miệng, khản giọng",
        "note": "KHÔNG nuốt nước súc miệng!"
    }
}

# Kế hoạch hành động
ACTION_PLAN = {
    "title": "📋 Kế Hoạch Hành Động Hen Suyễn",
    
    "green_zone": {
        "name": "🟢 XANH - Ổn Định",
        "signs": [
            "Thở bình thường",
            "Không ho, không khò khè",
            "Ngủ ngon",
            "Vận động bình thường"
        ],
        "action": [
            "Tiếp tục dùng thuốc kiểm soát đều đặn",
            "Tái khám định kỳ"
        ]
    },
    
    "yellow_zone": {
        "name": "🟡 VÀNG - Cảnh Báo",
        "signs": [
            "Ho, khò khè nhẹ",
            "Khó thở khi vận động",
            "Thức dậy vì ho/khó thở",
            "Dùng thuốc cắt cơn >2 lần/tuần"
        ],
        "action": [
            "Tăng thuốc kiểm soát (theo hướng dẫn bác sĩ)",
            "Dùng thuốc cắt cơn",
            "Nghỉ ngơi",
            "Gọi bác sĩ nếu không đỡ sau 1-2 ngày"
        ]
    },
    
    "red_zone": {
        "name": "🔴 ĐỎ - Nguy Hiểm",
        "signs": [
            "Khó thở NẶNG, không nói được câu dài",
            "Môi, đầu ngón tay tím",
            "Thuốc cắt cơn không tác dụng",
            "Co kéo cơ liên sườn, hõm trên xương ức",
            "Lú lẫn, ngủ gà"
        ],
        "action": [
            "📞 GỌI 115 NGAY!",
            "Dùng thuốc cắt cơn ngay (2-4 nhát)",
            "Nếu có, dùng Corticosteroid uống (theo chỉ định)",
            "Ngồi thẳng, không nằm",
            "Chờ xe cấp cứu"
        ]
    }
}

