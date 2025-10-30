"""
COPD Exercises - Bài tập cho COPD
==================================

Hướng dẫn tập luyện an toàn cho người COPD
"""

from typing import Dict, List

# Lợi ích tập thể dục
EXERCISE_BENEFITS = {
    "title": "🏃 Tập Thể Dục - Quan Trọng Như Thuốc!",
    
    "importance": """
💡 Tại sao phải tập?

COPD → Ít vận động → Yếu cơ → Khó thở hơn → Ít vận động hơn...
→ Vòng xoắn ỐC đi xuống!

TẬP THỂ DỤC phá vỡ vòng xoắn:
✅ Cơ khỏe hơn → Tiêu ít oxy hơn → Khó thở ít hơn
    """,
    
    "benefits": [
        "Giảm khó thở 20-30%",
        "Tăng sức bền",
        "Đi bộ xa hơn",
        "Giảm mệt mỏi",
        "Cải thiện tâm trạng",
        "Giảm đợt cấp",
        "Tăng chất lượng sống"
    ],
    
    "fear_vs_reality": {
        "fear": "❌ Sợ tập → khó thở",
        "reality": "✅ Thực tế: Tập → cơ khỏe → khó thở ít hơn!"
    }
}

# Nguyên tắc tập luyện
EXERCISE_PRINCIPLES = {
    "title": "📋 Nguyên Tắc An Toàn",
    
    "before_starting": [
        "🏥 Hỏi bác sĩ trước (nếu COPD nặng)",
        "💊 Uống thuốc đầy đủ",
        "🫁 Xịt thuốc giãn phế quản 15-30 phút trước tập",
        "🍽️ Không tập sau ăn (chờ 1-2 giờ)"
    ],
    
    "start_slow": {
        "principle": "BẮT ĐẦU CHẬM, TĂNG DẦN",
        "week_1": "5-10 phút/ngày",
        "week_2_4": "Tăng 2-3 phút/tuần",
        "target": "20-30 phút/ngày, 5 ngày/tuần",
        "note": "Không vội, không ép bản thân!"
    },
    
    "intensity": {
        "principle": "Cường Độ VỪA PHẢI",
        "how_to_know": [
            "Có thể nói chuyện được (NHƯNG không thể hát)",
            "Thở nhanh hơn, NHƯNG không hổn hển",
            "Hơi mệt, NHƯNG không kiệt sức"
        ],
        "scale": "3-4/10 trên thang đo mệt"
    },
    
    "warning_signs_stop": {
        "title": "🛑 DỪNG NGAY Khi:",
        "signs": [
            "Khó thở NẶNG, không nói được",
            "Đau ngực",
            "Chóng mặt, muốn ngất",
            "Đánh trống ngực",
            "Mệt quá mức"
        ],
        "action": "Ngồi nghỉ, thở môi, gọi người giúp nếu cần"
    },
    
    "daily_tips": [
        "Tập vào buổi sáng (ít đờm hơn sau 1-2 giờ thức dậy)",
        "Tránh tập khi trời quá nóng/lạnh",
        "Mặc quần áo thoáng mát",
        "Uống nước đủ",
        "Tập cùng bạn bè (vui + an toàn hơn)"
    ]
}

# Kỹ thuật thở
BREATHING_TECHNIQUES = {
    "pursed_lip_breathing": {
        "name": "🫦 Thở Môi (Pursed-Lip Breathing)",
        "when": "KHI khó thở, khi tập, khi leo cầu thang",
        "how": [
            "1️⃣ Hít vào qua MŨI (2 giây)",
            "2️⃣ Thở ra qua MIỆNG MÍM (như thổi nến) (4 giây)",
            "3️⃣ Thở ra GẤP ĐÔI thời gian hít vào"
        ],
        "benefit": [
            "Giữ đường thở MỞ lâu hơn",
            "Khí cũ ra được nhiều hơn",
            "Giảm khó thở ngay",
            "Giảm panic"
        ],
        "practice": "Tập 4-5 lần/ngày, mỗi lần 10 phút"
    },
    
    "diaphragmatic_breathing": {
        "name": "🫁 Thở Bụng (Hoành)",
        "when": "Khi nghỉ ngơi, buổi sáng/tối",
        "how": [
            "1️⃣ Nằm ngửa, gối đầu",
            "2️⃣ Đặt tay lên bụng",
            "3️⃣ Hít vào qua mũi → Bụng NỞ (tay nâng lên)",
            "4️⃣ Thở ra qua miệng → Bụng XẸPxuống (tay hạ)",
            "5️⃣ Ngực ÍT ĐỘNG"
        ],
        "benefit": [
            "Dùng cơ hoành (hiệu quả hơn cơ ngực)",
            "Thở sâu hơn",
            "Giảm công thở",
            "Tăng oxy"
        ],
        "practice": "2 lần/ngày, mỗi lần 5-10 phút"
    },
    
    "paced_breathing": {
        "name": "⏱️ Thở Theo Nhịp",
        "when": "Khi leo cầu thang, đi bộ lên dốc",
        "how": [
            "Hít vào: 1 bước",
            "Thở ra: 2-3 bước",
            "Hoặc: Hít (leo 1 bậc) → Thở ra (leo 2 bậc)"
        ],
        "benefit": "Phối hợp thở + vận động → Bớt khó thở"
    }
}

# Bài tập aerobic
AEROBIC_EXERCISES = {
    "title": "🚶 Bài Tập Tim Mạch (Aerobic)",
    
    "walking": {
        "name": "Đi Bộ - Tốt Nhất Cho COPD",
        "icon": "🚶‍♂️",
        "why_best": "An toàn, dễ làm, hiệu quả cao",
        "how_to": [
            "Bắt đầu: 5-10 phút/ngày",
            "Tăng dần: +2-3 phút/tuần",
            "Mục tiêu: 20-30 phút, 5 ngày/tuần",
            "Tốc độ: Vừa phải, có thể nói chuyện"
        ],
        "tips": [
            "Đi trên mặt phẳng trước, sau đó thử dốc nhẹ",
            "Mang giày thoải mái",
            "Dùng gậy nếu cần",
            "Đi với người khác an toàn hơn"
        ]
    },
    
    "stationary_bike": {
        "name": "Đạp Xe Đứng Yên",
        "icon": "🚴",
        "benefit": "Ít tải trọng lên khớp, an toàn",
        "how_to": [
            "Đạp nhẹ nhàng, KHÔNG ép mạnh",
            "10-20 phút/ngày",
            "Ngồi thẳng, không cúi"
        ]
    },
    
    "water_exercises": {
        "name": "Tập Trong Nước",
        "icon": "🏊",
        "benefit": "Nhẹ nhàng, mát mẻ, giảm tải khớp",
        "examples": ["Đi bộ trong bể nước nông", "Bơi nhẹ"],
        "caution": "Nước KHÔNG quá lạnh"
    }
}

# Bài tập sức mạnh
STRENGTH_EXERCISES = {
    "title": "💪 Bài Tập Sức Mạnh",
    
    "importance": "Cơ khỏe → Làm việc dễ dàng hơn → Ít khó thở",
    
    "upper_body": {
        "name": "Cơ Tay - Vai",
        "exercises": [
            {
                "name": "Nâng Tạ Nhẹ",
                "equipment": "Tạ 0.5-1kg (hoặc chai nước)",
                "how": "Nâng tay lên trên đầu, hạ xuống",
                "reps": "10-15 lần x 2 hiệp",
                "breathing": "Thở ra khi nâng, hít vào khi hạ"
            },
            {
                "name": "Đẩy Tường",
                "how": "Đứng cách tường 30cm, đặt tay lên tường, đẩy người ra xa tường",
                "reps": "10 lần x 2 hiệp"
            }
        ]
    },
    
    "lower_body": {
        "name": "Cơ Chân",
        "exercises": [
            {
                "name": "Ngồi Đứng (Sit-to-Stand)",
                "how": "Ngồi ghế → Đứng lên → Ngồi xuống (KHÔNG dùng tay)",
                "reps": "10 lần x 2 hiệp",
                "note": "Tốt nhất cho COPD!"
            },
            {
                "name": "Nâng Gót Chân",
                "how": "Đứng, nâng gót lên, hạ xuống",
                "reps": "15 lần x 2 hiệp"
            }
        ]
    },
    
    "frequency": "2-3 lần/tuần (KHÔNG ngày liên tiếp)",
    
    "important_notes": [
        "Bắt đầu NHẸ (không tạ hoặc tạ rất nhẹ)",
        "Tăng dần sau 2-3 tuần",
        "Thở ĐỀU, KHÔNG nín thở",
        "Nghỉ 1 ngày giữa các buổi tập"
    ]
}

# Bài tập giãn cơ
FLEXIBILITY_EXERCISES = {
    "title": "🤸 Bài Tập Giãn Cơ",
    
    "importance": "Cơ mềm mại → Vận động dễ dàng → Ít đau mỏi",
    
    "exercises": [
        {
            "name": "Giãn Vai",
            "how": "Xoay vai tròn, phía trước 10 lần, phía sau 10 lần",
            "when": "Buổi sáng, sau tập"
        },
        {
            "name": "Giãn Cổ",
            "how": "Nghiêng cổ sang trái/phải, cúi/ngửa nhẹ nhàng",
            "duration": "Giữ 10 giây mỗi tư thế"
        },
        {
            "name": "Giãn Chân",
            "how": "Ngồi ghế, duỗi chân thẳng, giữ 10 giây",
            "reps": "10 lần mỗi chân"
        }
    ],
    
    "when": "Buổi sáng hoặc sau tập thể dục",
    "tips": [
        "Giãn nhẹ nhàng, KHÔNG giật mạnh",
        "Thở đều khi giãn",
        "Nếu đau → Dừng ngay"
    ]
}

# Hoạt động hàng ngày
DAILY_ACTIVITIES = {
    "title": "🏠 Hoạt Động Hàng Ngày - Tiết Kiệm Sức",
    
    "energy_conservation": [
        {
            "activity": "Tắm rửa",
            "tips": [
                "Ngồi ghế khi tắm",
                "Chuẩn bị đồ sẵn, không phải đi lại nhiều",
                "Lau khô người bằng áo choàng (thay vì khăn)"
            ]
        },
        {
            "activity": "Mặc quần áo",
            "tips": [
                "Ngồi khi mặc",
                "Mặc quần/giày trước khi đứng",
                "Chọn quần áo rộng, dễ mặc"
            ]
        },
        {
            "activity": "Nấu ăn",
            "tips": [
                "Ngồi khi nấu",
                "Để đồ dùng ở tầm tay",
                "Nấu nhiều, chia nhỏ đông lạnh"
            ]
        },
        {
            "activity": "Dọn nhà",
            "tips": [
                "Làm từng việc nhỏ, nghỉ giữa các việc",
                "Dùng gậy chổi dài (không cúi)",
                "Nhờ người giúp việc nặng"
            ]
        },
        {
            "activity": "Leo cầu thang",
            "tips": [
                "Xịt thuốc trước 15 phút",
                "Thở môi khi leo",
                "Hít (1 bậc) → Thở ra (2 bậc)",
                "Nghỉ giữa chừng nếu cần"
            ]
        }
    ],
    
    "general_tips": [
        "Làm việc CHẬM, ổn định",
        "Ưu tiên công việc quan trọng buổi sáng (sức khỏe tốt hơn)",
        "Xen kẽ việc nặng - nhẹ",
        "Nghỉ ngơi đủ giữa các hoạt động"
    ]
}

# Chương trình tập 4 tuần
FOUR_WEEK_PROGRAM = {
    "title": "📅 Chương Trình Tập 4 Tuần Cho Người Mới",
    
    "week_1": {
        "focus": "Làm quen, nhẹ nhàng",
        "aerobic": "Đi bộ 5-10 phút/ngày",
        "strength": "Ngồi-đứng 5 lần x 1 hiệp",
        "breathing": "Thở môi 5 phút x 2 lần/ngày"
    },
    
    "week_2": {
        "focus": "Tăng thời gian",
        "aerobic": "Đi bộ 10-15 phút/ngày",
        "strength": "Ngồi-đứng 8 lần x 2 hiệp + Nâng tạ nhẹ",
        "breathing": "Thở môi + thở bụng 10 phút x 2 lần/ngày"
    },
    
    "week_3": {
        "focus": "Tăng cường độ nhẹ",
        "aerobic": "Đi bộ 15-20 phút/ngày, thử dốc nhẹ",
        "strength": "Ngồi-đứng 10 lần x 2 hiệp + Nhiều bài tập tay",
        "breathing": "Tích hợp thở vào mọi hoạt động"
    },
    
    "week_4": {
        "focus": "Duy trì và tiến xa hơn",
        "aerobic": "Đi bộ 20-30 phút/ngày",
        "strength": "Toàn bộ bài tập, 2-3 lần/tuần",
        "breathing": "Thành thói quen tự nhiên"
    },
    
    "after_4_weeks": [
        "Tiếp tục tăng dần thời gian, cường độ",
        "Thêm các hoạt động khác (bơi, đạp xe...)",
        "Tham gia nhóm tập COPD (nếu có)"
    ]
}

