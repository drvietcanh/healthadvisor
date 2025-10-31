"""
Spinal Management - Quản lý cột sống
"""

SPINAL_POSTURE = {
    "title": "🎯 Tư Thế Đúng Cho Cột Sống",
    
    "sitting": {
        "title": "Khi ngồi:",
        "correct": [
            "Ngồi thẳng, lưng tựa ghế",
            "Chân chạm đất, gối 90°",
            "Màn hình ngang tầm mắt",
            "Không cúi đầu quá lâu"
        ],
        "avoid": [
            "Ngồi khom lưng",
            "Ngồi quá thấp hoặc quá cao",
            "Ngồi lâu >1 giờ không đứng dậy"
        ]
    },
    
    "standing": {
        "title": "Khi đứng:",
        "correct": [
            "Đứng thẳng, 2 chân đều",
            "Đầu, vai, hông thẳng hàng",
            "Cân bằng trọng lượng 2 chân"
        ],
        "avoid": [
            "Đứng 1 chân quá lâu",
            "Khom lưng",
            "Đứng lâu không nghỉ"
        ]
    },
    
    "lifting": {
        "title": "Khi nhấc vật nặng:",
        "correct": [
            "Co gối, không cúi lưng",
            "Giữ vật gần người",
            "Nâng bằng chân, không bằng lưng",
            "Không vặn người khi nhấc"
        ],
        "avoid": [
            "Cúi lưng nhấc vật",
            "Nhấc vật xa người",
            "Vặn người đột ngột"
        ]
    },
    
    "sleeping": {
        "title": "Khi ngủ:",
        "best_positions": [
            {
                "position": "Nằm nghiêng",
                "how": "Co gối nhẹ, đệm giữa 2 gối",
                "benefit": "Giảm áp lực lưng"
            },
            {
                "position": "Nằm ngửa",
                "how": "Gối dưới gối, gối nhỏ dưới cổ",
                "benefit": "Giữ cột sống thẳng"
            }
        ],
        "avoid": "Nằm sấp (vặn cổ, lưng)"
    }
}

SPINAL_EXERCISES = {
    "title": "🏃 Bài Tập Cho Cột Sống",
    
    "daily_stretching": [
        {
            "name": "Gập cổ",
            "movement": "Gập cổ về trước, ra sau, sang trái, phải",
            "reps": "Mỗi hướng 10 lần, 2 lần/ngày"
        },
        {
            "name": "Xoay cổ",
            "movement": "Xoay cổ nhẹ nhàng",
            "reps": "10 lần mỗi bên"
        },
        {
            "name": "Cong lưng",
            "movement": "Đứng, cong lưng ra sau nhẹ",
            "reps": "10 lần"
        },
        {
            "name": "Xoay vai",
            "movement": "Xoay vai ra trước, ra sau",
            "reps": "10 lần mỗi hướng"
        }
    ],
    
    "core_strengthening": {
        "title": "Tăng cường cơ bụng, lưng:",
        "exercises": [
            {
                "name": "Plank",
                "position": "Chống tay, giữ thẳng",
                "duration": "Giữ 20-60 giây",
                "reps": "3-5 lần",
                "benefit": "Tăng cơ toàn thân"
            },
            {
                "name": "Gập bụng",
                "position": "Nằm ngửa, co gối",
                "movement": "Nâng đầu và vai lên",
                "reps": "15-20 lần",
                "benefit": "Tăng cơ bụng"
            },
            {
                "name": "Siêu nhân",
                "position": "Nằm sấp",
                "movement": "Nâng tay và chân lên",
                "reps": "10 lần",
                "benefit": "Tăng cơ lưng"
            }
        ],
        "frequency": "2-3 lần/tuần"
    }
}

SPINAL_PROTECTION = {
    "title": "🛡️ Bảo Vệ Cột Sống",
    
    "daily_tips": [
        "Đứng dậy mỗi 30-60 phút khi ngồi",
        "Đi lại, duỗi người",
        "Giữ tư thế đúng",
        "Tránh ngồi/đứng lâu",
        "Nghỉ ngơi khi mệt"
    ],
    
    "ergonomics": {
        "workplace": [
            "Ghế có tựa lưng",
            "Màn hình ngang tầm mắt",
            "Bàn phím, chuột thoải mái",
            "Điều chỉnh chiều cao ghế"
        ],
        "home": [
            "Giường, nệm phù hợp",
            "Gối đúng độ cao",
            "Tránh ngồi ghế quá mềm",
            "Đèn đủ sáng khi đọc"
        ]
    }
}

