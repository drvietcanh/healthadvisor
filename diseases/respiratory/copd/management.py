"""
COPD Management - Quản lý COPD
===============================

Hướng dẫn quản lý COPD toàn diện
"""

from typing import Dict, List

# Bỏ thuốc lá
SMOKING_CESSATION = {
    "title": "🚭 BỎ THUỐC LÁ - Quan Trọng NHẤT!",
    
    "importance": """
⭐ BỎ THUỐC LÁ là điều trị HIỆU QUẢ NHẤT cho COPD:

- Làm CHẬM tiến triển bệnh
- Giảm ho, đờm sau 1 tháng
- Giảm đợt cấp 30-50%
- Cải thiện chức năng phổi (một chút)
- Tăng tuổi thọ 3-5 năm

💊 MỌI THUỐC đều KÉMHIỆU QUẢ hơn bỏ thuốc!
    """,
    
    "benefits_timeline": [
        {
            "time": "20 phút",
            "benefit": "Huyết áp, nhịp tim trở về bình thường"
        },
        {
            "time": "12 giờ",
            "benefit": "Nồng độ CO trong máu giảm"
        },
        {
            "time": "2 tuần - 3 tháng",
            "benefit": "Tuần hoàn, chức năng phổi cải thiện"
        },
        {
            "time": "1-9 tháng",
            "benefit": "Ho, khó thở giảm rõ rệt"
        },
        {
            "time": "1 năm",
            "benefit": "Nguy cơ tim mạch giảm 50%"
        },
        {
            "time": "5-15 năm",
            "benefit": "Nguy cơ đột quỵ = người không hút"
        }
    ],
    
    "methods": [
        {
            "method": "Quyết tâm (Ý chí)",
            "success_rate": "3-5%",
            "pros": "Miễn phí",
            "cons": "Khó, tỷ lệ thành công thấp"
        },
        {
            "method": "Tư vấn + Hỗ trợ",
            "success_rate": "10-15%",
            "pros": "Tăng động lực",
            "service": "Phòng khám cai thuốc (BV lớn)"
        },
        {
            "method": "Thuốc thay thế Nicotine (NRT)",
            "examples": ["Kẹo cao su Nicotine", "Miếng dán Nicotine"],
            "success_rate": "15-20%",
            "price": "500,000-1,000,000đ/tháng"
        },
        {
            "method": "Thuốc uống",
            "examples": ["Varenicline (Champix)", "Bupropion"],
            "success_rate": "25-30% (tốt nhất!)",
            "price": "2,000,000-3,000,000đ/đợt điều trị",
            "note": "Cần đơn bác sĩ"
        }
    ],
    
    "tips": [
        "Chọn ngày bỏ cụ thể (sinh nhật, Tết...)",
        "Nói cho gia đình, bạn bè biết → Hỗ trợ",
        "Vứt bỏ TẤT CẢ thuốc lá, gạt tàn",
        "Tránh nơi có người hút",
        "Tìm hoạt động thay thế (đi bộ, nhai kẹo...)",
        "Uống nhiều nước",
        "Không bỏ cuộc nếu hút lại (thử lại!)"
    ]
}

# Phục hồi chức năng
PULMONARY_REHABILITATION = {
    "title": "🏃 Phục Hồi Chức Năng Phổi",
    
    "what_is_it": """
💡 Phục hồi chức năng phổi là gì?

Chương trình TẬP LUYỆN + GIÁO DỤC:
- Tập thở
- Tập thể dục nhẹ
- Học cách sống với COPD
- Tư vấn dinh dưỡng, tâm lý

→ Giúp SỐNG TỐT HƠN với COPD
    """,
    
    "benefits": [
        "Giảm khó thở 30-40%",
        "Tăng khả năng vận động",
        "Giảm đợt cấp 25%",
        "Cải thiện chất lượng cuộc sống",
        "Giảm lo âu, trầm cảm",
        "Tăng tuổi thọ"
    ],
    
    "components": [
        "Tập thể dục (đi bộ, đạp xe nhẹ)",
        "Tập cơ hô hấp",
        "Kỹ thuật thở (thở môi, thở bụng)",
        "Giáo dục về COPD",
        "Tư vấn dinh dưỡng",
        "Hỗ trợ tâm lý"
    ],
    
    "duration": "6-12 tuần, 2-3 buổi/tuần",
    
    "availability_vietnam": [
        "BV Phổi Trung ương (Hà Nội)",
        "BV Chợ Rẫy (TP.HCM)",
        "Một số BV tỉnh",
        "Có thể tập tại nhà (theo hướng dẫn)"
    ],
    
    "home_program": {
        "title": "Chương Trình Tại Nhà",
        "exercises": [
            "Đi bộ 20-30 phút/ngày",
            "Tập nâng tạ nhẹ (0.5-1kg)",
            "Thở môi khi khó thở",
            "Tập thở bụng 2 lần/ngày"
        ]
    }
}

# Đợt cấp
EXACERBATION_MANAGEMENT = {
    "title": "🚨 Xử Trí Đợt Cấp COPD",
    
    "what_is_exacerbation": """
💡 Đợt cấp là gì?

= Đợt bệnh NẶNG LÊN ĐỘT NGỘT:
- Khó thở tăng
- Ho, đờm nhiều hơn
- Đờm đổi màu (vàng/xanh)

→ Cần điều trị NGAY, có thể nhập viện!
    """,
    
    "warning_signs": [
        "Khó thở tăng rõ rệt",
        "Đờm nhiều hơn bình thường",
        "Đờm vàng/xanh (mủ)",
        "Ho tăng",
        "Sốt",
        "Mệt hơn bình thường"
    ],
    
    "action_plan": {
        "title": "Kế Hoạch Hành Động",
        "green_zone": {
            "name": "🟢 XANH - Bình Thường",
            "signs": "Ho, khó thở như mọi ngày",
            "action": [
                "Uống thuốc đều đặn",
                "Tập thể dục nhẹ",
                "Tái khám định kỳ"
            ]
        },
        "yellow_zone": {
            "name": "🟡 VÀNG - Cảnh Báo",
            "signs": "Khó thở hơn, ho/đờm nhiều hơn",
            "action": [
                "Tăng thuốc xịt ngắn hạn (4-6 lần/ngày)",
                "Uống thuốc giảm đờm",
                "Nghỉ ngơi nhiều",
                "Gọi bác sĩ nếu không đỡ sau 2-3 ngày"
            ]
        },
        "red_zone": {
            "name": "🔴 ĐỎ - Nguy Hiểm",
            "signs": [
                "Khó thở NẶNG",
                "Môi tím",
                "Lú lẫn",
                "Đờm mủ + sốt cao"
            ],
            "action": "📞 GỌI 115 hoặc ĐẾN BV NGAY!"
        }
    },
    
    "treatment": [
        "Tăng liều thuốc giãn phế quản",
        "Corticosteroid uống (5-7 ngày)",
        "Kháng sinh (nếu có nhiễm trùng)",
        "Oxy (nếu SpO2 <90%)",
        "Nhập viện nếu nặng"
    ]
}

# Dinh dưỡng
NUTRITION = {
    "title": "🍽️ Dinh Dưỡng Cho Người COPD",
    
    "importance": "30-40% bệnh nhân COPD SỤT CÂN, yếu cơ → Tiên lượng xấu",
    
    "recommendations": [
        {
            "principle": "Ăn Nhiều Bữa, Ít Lượng",
            "reason": "Bụng no → Đẩy hoành lên → Khó thở",
            "advice": "5-6 bữa nhỏ/ngày thay vì 3 bữa lớn"
        },
        {
            "principle": "Tăng Protein",
            "reason": "Bù đắp mất cơ, tăng sức đề kháng",
            "foods": ["Thịt nạc", "Cá", "Trứng", "Đậu hũ", "Sữa"],
            "target": "1.2-1.5g/kg/ngày"
        },
        {
            "principle": "Đủ Calories",
            "reason": "Thở gắng → Tốn nhiều năng lượng",
            "target": "1.5 lần người bình thường"
        },
        {
            "principle": "Hạn Chế Muối",
            "reason": "Giữ nước → Phù nề → Khó thở",
            "advice": "<5g/ngày"
        },
        {
            "principle": "Uống Đủ Nước",
            "reason": "Làm loãng đờm",
            "target": "1.5-2 lít/ngày"
        }
    ],
    
    "foods_to_eat": [
        "Thịt nạc, cá",
        "Trứng",
        "Sữa tươi",
        "Rau xanh",
        "Trái cây",
        "Ngũ cốc nguyên hạt"
    ],
    
    "foods_to_avoid": [
        "Đồ chiên rán (khó tiêu)",
        "Đồ uống có gas (đầy bụng)",
        "Thức ăn mặn",
        "Rượu bia"
    ]
}

# Vắc-xin
VACCINATION = {
    "title": "💉 Vắc-xin - Phòng Đợt Cấp",
    
    "influenza_vaccine": {
        "name": "Vắc-xin Cúm",
        "frequency": "MỖI NĂM 1 lần (trước mùa đông)",
        "benefit": "Giảm đợt cấp 25-30%",
        "price": "150,000-250,000đ/mũi",
        "note": "⭐ BẮT BUỘC cho người COPD!"
    },
    
    "pneumococcal_vaccine": {
        "name": "Vắc-xin Phế Cầu Khuẩn",
        "types": [
            {
                "type": "PCV13 (Prevenar 13)",
                "dose": "1 mũi",
                "price": "1,500,000-2,000,000đ"
            },
            {
                "type": "PPSV23 (Pneumovax 23)",
                "dose": "1 mũi, nhắc lại sau 5 năm",
                "price": "800,000-1,200,000đ"
            }
        ],
        "benefit": "Giảm viêm phổi nặng, tử vong",
        "recommendation": "Tiêm 1 lần, nhắc sau 5-10 năm"
    },
    
    "covid19_vaccine": {
        "name": "Vắc-xin COVID-19",
        "importance": "Người COPD → COVID-19 nặng hơn",
        "recommendation": "Tiêm đủ liều + nhắc định kỳ"
    }
}

