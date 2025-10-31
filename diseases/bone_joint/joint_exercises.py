"""
Joint Exercises - Bài tập chi tiết cho các khớp
Áp dụng cho: Thoái hóa khớp, viêm khớp, đau cột sống
"""

# Bài tập cho GỐI
KNEE_EXERCISES = {
    "title": "🦵 Bài Tập Cho Khớp Gối",
    
    "stretching": {
        "title": "Kéo giãn (Khi cứng, đau nhẹ):",
        "exercises": [
            {
                "name": "Duỗi gối",
                "position": "Ngồi thẳng lưng trên ghế",
                "movement": "Duỗi 1 chân lên cao, giữ 10-20 giây",
                "reps": "10 lần mỗi chân, 2-3 lần/ngày",
                "benefit": "Tăng độ linh hoạt, giảm cứng"
            },
            {
                "name": "Gập gối",
                "position": "Nằm ngửa hoặc ngồi",
                "movement": "Gập gối về phía ngực, giữ 10 giây",
                "reps": "10 lần mỗi chân",
                "benefit": "Kéo giãn cơ sau đùi"
            }
        ]
    },
    
    "strengthening": {
        "title": "Tăng cường cơ (Bảo vệ khớp):",
        "exercises": [
            {
                "name": "Nâng chân thẳng",
                "position": "Nằm ngửa, 1 chân co, 1 chân duỗi",
                "movement": "Nâng chân duỗi lên cao 10-15cm, giữ 5-10 giây",
                "reps": "10-15 lần mỗi chân, 2-3 lần/ngày",
                "benefit": "Tăng cơ đùi trước (tứ đầu) → Bảo vệ gối"
            },
            {
                "name": "Nâng chân ngang",
                "position": "Nằm nghiêng",
                "movement": "Nâng chân trên lên cao, giữ 5 giây",
                "reps": "10-15 lần mỗi chân",
                "benefit": "Tăng cơ đùi ngoài"
            },
            {
                "name": "Ngồi xổm nhẹ",
                "position": "Đứng, tay vịn ghế",
                "movement": "Từ từ ngồi xuống (gối không quá 90°), đứng lên",
                "reps": "10-15 lần, 2 lần/ngày",
                "benefit": "Tăng cơ đùi, mông"
            },
            {
                "name": "Đạp xe tại chỗ",
                "position": "Ngồi trên ghế",
                "movement": "Đạp chân như đạp xe (không tải trọng)",
                "reps": "20-30 lần, 2-3 lần/ngày",
                "benefit": "Vận động gối nhẹ nhàng"
            }
        ]
    },
    
    "low_impact_cardio": {
        "title": "Vận động tim mạch (Không gây đau):",
        "exercises": [
            {
                "name": "Đi bộ",
                "how": "Đi chậm, trên mặt phẳng, giày có đệm",
                "duration": "20-30 phút, 3-5 lần/tuần",
                "note": "Dừng nếu đau tăng"
            },
            {
                "name": "Bơi lội",
                "how": "Bơi hoặc đi bộ trong nước",
                "duration": "20-30 phút",
                "benefit": "Nước giảm áp lực lên gối"
            },
            {
                "name": "Đạp xe",
                "how": "Xe đạp thường hoặc xe đạp tại chỗ",
                "duration": "20-30 phút",
                "note": "Điều chỉnh yên xe cao, giảm lực đạp"
            }
        ]
    },
    
    "avoid": [
        "❌ Chạy bộ (gây đau gối)",
        "❌ Leo cầu thang nhiều",
        "❌ Ngồi xổm, quỳ gối",
        "❌ Nhảy, nhảy dây"
    ]
}

# Bài tập cho HÁNG
HIP_EXERCISES = {
    "title": "🦴 Bài Tập Cho Khớp Háng",
    
    "stretching": [
        {
            "name": "Kéo giãn háng",
            "position": "Nằm ngửa, co 1 gối",
            "movement": "Đưa gối sang bên, kéo giãn háng",
            "reps": "Giữ 20-30 giây, 3 lần mỗi bên"
        },
        {
            "name": "Xoay háng",
            "position": "Nằm ngửa, co 2 gối",
            "movement": "Xoay 2 gối sang trái, phải nhẹ nhàng",
            "reps": "10 lần mỗi bên"
        }
    ],
    
    "strengthening": [
        {
            "name": "Nâng chân ngang",
            "position": "Nằm nghiêng",
            "movement": "Nâng chân trên lên cao, giữ 5 giây",
            "reps": "10-15 lần mỗi chân",
            "benefit": "Tăng cơ háng"
        },
        {
            "name": "Nâng chân thẳng",
            "position": "Nằm sấp",
            "movement": "Nâng 1 chân lên cao, giữ 5 giây",
            "reps": "10-15 lần mỗi chân",
            "benefit": "Tăng cơ mông, đùi sau"
        },
        {
            "name": "Đi bộ",
            "how": "Đi bộ trên mặt phẳng",
            "duration": "20-30 phút",
            "benefit": "Vận động háng nhẹ nhàng"
        }
    ]
}

# Bài tập cho CỔ TAY, NGÓN TAY
HAND_EXERCISES = {
    "title": "✋ Bài Tập Cho Cổ Tay & Ngón Tay",
    
    "exercises": [
        {
            "name": "Nắm - Mở bàn tay",
            "movement": "Nắm chặt tay, giữ 5 giây, mở ra, giãn ngón tay",
            "reps": "10-15 lần mỗi tay, 2-3 lần/ngày"
        },
        {
            "name": "Uốn từng ngón",
            "movement": "Uốn từng ngón tay về lòng bàn tay, giữ 5 giây",
            "reps": "5 lần mỗi ngón"
        },
        {
            "name": "Gập cổ tay",
            "movement": "Gập cổ tay lên xuống, sang trái phải",
            "reps": "10 lần mỗi hướng"
        },
        {
            "name": "Xoa bóp",
            "movement": "Xoa bóp nhẹ các khớp ngón tay",
            "duration": "5-10 phút",
            "benefit": "Giảm cứng, đau"
        },
        {
            "name": "Cầm bóp bóng",
            "equipment": "Bóng stress nhỏ",
            "movement": "Cầm, bóp nhẹ",
            "reps": "10-15 lần",
            "benefit": "Tăng sức cơ tay"
        }
    ]
}

# Bài tập cho VAI
SHOULDER_EXERCISES = {
    "title": "💪 Bài Tập Cho Vai",
    
    "exercises": [
        {
            "name": "Nâng cánh tay",
            "position": "Đứng hoặc ngồi thẳng",
            "movement": "Nâng 1 cánh tay lên cao, giữ 5 giây",
            "reps": "10 lần mỗi tay"
        },
        {
            "name": "Xoay vai",
            "movement": "Xoay vai ra trước, ra sau",
            "reps": "10 lần mỗi hướng"
        },
        {
            "name": "Kéo giãn vai",
            "movement": "Đưa cánh tay ngang, kéo sang bên",
            "reps": "Giữ 20 giây, 3 lần"
        }
    ]
}

# Bài tập cho CỘT SỐNG
SPINE_EXERCISES = {
    "title": "🫁 Bài Tập Cho Cột Sống",
    
    "low_back": {
        "title": "Đau thắt lưng:",
        "exercises": [
            {
                "name": "Nằm co gối",
                "position": "Nằm ngửa",
                "movement": "Co 2 gối lên ngực, giữ 20 giây",
                "reps": "10 lần, 2-3 lần/ngày",
                "benefit": "Kéo giãn lưng dưới"
            },
            {
                "name": "Gập bụng nhẹ",
                "position": "Nằm ngửa, co gối",
                "movement": "Nâng đầu và vai nhẹ, giữ 5 giây",
                "reps": "10-15 lần",
                "benefit": "Tăng cơ bụng → Bảo vệ lưng"
            },
            {
                "name": "Nâng chân",
                "position": "Nằm sấp",
                "movement": "Nâng 1 chân lên, giữ 5 giây",
                "reps": "10 lần mỗi chân",
                "benefit": "Tăng cơ lưng"
            },
            {
                "name": "Tư thế con mèo",
                "position": "Quỳ 4 chân",
                "movement": "Cong lưng lên xuống nhẹ nhàng",
                "reps": "10-15 lần",
                "benefit": "Tăng độ linh hoạt cột sống"
            }
        ]
    },
    
    "posture": {
        "title": "Giữ tư thế đúng:",
        "tips": [
            "Ngồi thẳng, lưng tựa ghế",
            "Màn hình ngang tầm mắt",
            "Đứng dậy mỗi 30-60 phút",
            "Tập tăng cường cơ bụng, lưng"
        ]
    }
}

# Nguyên tắc chung
EXERCISE_PRINCIPLES = {
    "title": "📋 Nguyên Tắc Tập Luyện",
    
    "general": [
        "Bắt đầu NHẸ, tăng dần",
        "Tập ĐỀU ĐẶN (không bỏ nhiều ngày)",
        "Nghỉ khi đau TĂNG (không gắng sức)",
        "Khởi động 5-10 phút trước",
        "Kéo giãn nhẹ sau khi tập"
    ],
    
    "when_to_stop": [
        "🚨 Đau TĂNG khi tập",
        "🚨 Sưng khớp mới",
        "🚨 Cảm thấy mệt mỏi quá",
        "🚨 Chóng mặt, khó thở",
        "→ DỪNG NGAY, nghỉ ngơi"
    ],
    
    "frequency": {
        "stretching": "Hàng ngày (sáng, tối)",
        "strengthening": "2-3 lần/tuần",
        "cardio": "3-5 lần/tuần, 20-30 phút"
    },
    
    "progression": [
        "Tuần 1-2: Làm quen, số lần ít",
        "Tuần 3-4: Tăng số lần, thời gian",
        "Tuần 5+: Duy trì, có thể tăng độ khó"
    ]
}

