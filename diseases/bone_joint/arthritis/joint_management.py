"""
Joint Management - Quản lý khớp chung
Áp dụng cho cả thoái hóa và viêm khớp
"""

JOINT_EXERCISES = {
    "title": "🏃 Bài Tập Cho Khớp",
    
    "principles": [
        "Vận động NHẸ, ĐỀU ĐẶN tốt hơn không vận động",
        "Nghỉ khi đau nhiều, tập khi đỡ đau",
        "Khởi động 5-10 phút trước",
        "Không tập quá sức"
    ],
    
    "for_pain": {
        "title": "Khi đau:",
        "exercises": [
            "Co duỗi nhẹ khớp (không tải trọng)",
            "Xoa bóp nhẹ",
            "Chườm nóng trước khi tập",
            "Tập trong nước (giảm áp lực)"
        ]
    },
    
    "for_stiffness": {
        "title": "Khi cứng khớp:",
        "exercises": [
            "Chườm nóng 10-15 phút",
            "Vận động nhẹ nhàng, từ từ",
            "Kéo giãn nhẹ",
            "Tránh vận động đột ngột"
        ]
    },
    
    "strengthening": {
        "title": "Tăng cường cơ bắp (bảo vệ khớp):",
        "examples": [
            "Gối: Nâng chân thẳng",
            "Háng: Đưa chân sang ngang",
            "Cổ tay: Cầm tạ nhẹ, gập duỗi",
            "Vai: Nâng cánh tay lên cao"
        ],
        "frequency": "2-3 lần/tuần, mỗi lần 15-20 phút"
    }
}

JOINT_NUTRITION = {
    "title": "🍎 Dinh Dưỡng Cho Khớp",
    
    "anti_inflammatory": {
        "title": "Thực phẩm chống viêm:",
        "foods": [
            {
                "food": "Cá béo (cá hồi, cá thu, cá ngừ)",
                "why": "Omega-3 chống viêm mạnh",
                "how_much": "2-3 lần/tuần"
            },
            {
                "food": "Rau xanh (bông cải, cải bó xôi)",
                "why": "Chất chống oxy hóa",
                "how_much": "Mỗi bữa"
            },
            {
                "food": "Gừng, nghệ",
                "why": "Chống viêm tự nhiên",
                "how_much": "Thêm vào thức ăn"
            },
            {
                "food": "Quả mọng (dâu, việt quất)",
                "why": "Anthocyanin chống viêm",
                "how_much": "Hàng ngày"
            },
            {
                "food": "Dầu olive",
                "why": "Chất béo tốt, chống viêm",
                "how_much": "Thay thế dầu ăn thông thường"
            }
        ]
    },
    
    "bone_health": {
        "title": "Cho xương khớp chắc khỏe:",
        "foods": [
            {
                "food": "Sữa, sữa chua",
                "why": "Canxi + Vitamin D",
                "how_much": "2-3 phần/ngày"
            },
            {
                "food": "Cá nhỏ ăn cả xương (cá cơm)",
                "why": "Canxi tự nhiên",
                "how_much": "1-2 lần/tuần"
            },
            {
                "food": "Rau lá xanh",
                "why": "Canxi + Vitamin K",
                "how_much": "Mỗi bữa"
            }
        ]
    },
    
    "avoid": {
        "title": "Tránh:",
        "foods": [
            "Thức ăn nhiều đường → Tăng viêm",
            "Thức ăn chiên rán → Tăng viêm",
            "Thức ăn chế biến sẵn",
            "Rượu bia quá mức"
        ]
    },
    
    "weight_management": {
        "title": "Quản lý cân nặng:",
        "why": "Mỗi 5kg giảm → Giảm áp lực gối 15-20kg",
        "how": [
            "Ăn nhiều rau, ít tinh bột tinh chế",
            "Vận động đều đặn",
            "Giảm từ từ, không nhịn ăn"
        ]
    }
}

JOINT_PROTECTION = {
    "title": "🛡️ Bảo Vệ Khớp Hàng Ngày",
    
    "daily_tips": [
        {
            "tip": "Giữ tư thế đúng",
            "how": "Ngồi thẳng, đứng thẳng, không khom lưng"
        },
        {
            "tip": "Dùng dụng cụ hỗ trợ",
            "how": "Gậy chống, tay vịn, đế giày",
            "note": "Không xấu hổ khi dùng - Bảo vệ khớp quan trọng hơn!"
        },
        {
            "tip": "Tránh tư thế xấu",
            "how": "Không ngồi xổm, không quỳ gối, không ngồi thấp"
        },
        {
            "tip": "Nghỉ ngơi định kỳ",
            "how": "Nghỉ 5-10 phút mỗi giờ khi làm việc",
            "note": "Đứng dậy, đi lại, duỗi người"
        },
        {
            "tip": "Dùng khớp lớn khi có thể",
            "how": "Mang túi xách bằng vai thay vì tay, đẩy cửa bằng thân thay vì ngón tay"
        },
        {
            "tip": "Giữ ấm khớp",
            "how": "Mặc ấm, đeo găng tay khi trời lạnh",
            "note": "Lạnh làm cứng, đau khớp"
        }
    ],
    
    "ergonomics": {
        "title": "Cải thiện môi trường làm việc:",
        "tips": [
            "Ghế có tựa lưng, chiều cao phù hợp",
            "Màn hình ngang tầm mắt",
            "Bàn phím, chuột ở vị trí thoải mái",
            "Giày dép phù hợp, có đệm"
        ]
    },
    
    "when_to_rest": [
        "Đau nhiều khi vận động",
        "Sưng nóng khớp",
        "Cảm thấy mệt mỏi",
        "⚠️ Nghỉ ngay, không gắng sức!"
    ]
}

