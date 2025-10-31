"""
Asthma Management - Quản lý Hen Suyễn
=======================================

Hướng dẫn quản lý hen suyễn toàn diện
"""

# Phòng ngừa đợt cấp
PREVENTION = {
    "title": "🛡️ Phòng Ngừa Đợt Cấp",
    
    "avoid_triggers": {
        "title": "Tránh Yếu Tố Kích Phát",
        "methods": [
            "Không hút thuốc, tránh khói thuốc",
            "Đeo khẩu trang khi ra ngoài (khói, bụi)",
            "Vệ sinh nhà cửa (giảm bụi, nấm mốc)",
            "Tránh phấn hoa trong mùa dị ứng",
            "Giữ ấm khi trời lạnh",
            "Tránh thức ăn gây dị ứng (nếu có)"
        ]
    },
    
    "regular_medication": {
        "title": "Dùng Thuốc Kiểm Soát Đều Đặn",
        "importance": "Thuốc kiểm soát phải dùng HÀNG NGÀY, không bỏ quên",
        "tips": [
            "Đặt báo thức nhắc uống/xịt",
            "Để thuốc ở nơi dễ thấy",
            "Mang theo thuốc khi đi xa",
            "Luôn có thuốc cắt cơn bên mình"
        ]
    },
    
    "vaccination": {
        "title": "💉 Tiêm Vắc-xin",
        "influenza": {
            "vaccine": "Vắc-xin Cúm",
            "frequency": "Mỗi năm 1 lần",
            "benefit": "Giảm đợt cấp hen do cúm",
            "price": "150,000-250,000đ/mũi"
        },
        "pneumococcal": {
            "vaccine": "Vắc-xin Phế Cầu",
            "frequency": "1 lần, nhắc sau 5 năm",
            "benefit": "Phòng viêm phổi",
            "price": "800,000-2,000,000đ/mũi"
        }
    }
}

# Theo dõi tại nhà
HOME_MONITORING = {
    "title": "📊 Theo Dõi Tại Nhà",
    
    "peak_flow_meter": {
        "title": "Máy Đo Lưu Lượng Đỉnh (Peak Flow Meter)",
        "what_is_it": "Dụng cụ đo sức thở",
        "how_to_use": [
            "Thở ra HẾT sức vào máy",
            "Đọc số trên máy",
            "Ghi lại mỗi ngày (sáng, tối)"
        ],
        "benefit": [
            "Phát hiện sớm cơn hen",
            "Biết khi nào cần điều trị",
            "Đánh giá hiệu quả thuốc"
        ],
        "zones": {
            "green": "80-100%: Ổn định",
            "yellow": "50-80%: Cảnh báo, tăng thuốc",
            "red": "<50%: Nguy hiểm, gọi 115!"
        },
        "price": "200,000-500,000đ/máy"
    },
    
    "symptom_diary": {
        "title": "📝 Nhật Ký Triệu Chứng",
        "what_to_record": [
            "Số lần dùng thuốc cắt cơn",
            "Triệu chứng (ho, khó thở)",
            "Thời điểm xuất hiện",
            "Yếu tố kích phát",
            "Chỉ số Peak Flow (nếu có)"
        ],
        "benefit": "Giúp bác sĩ điều chỉnh thuốc tốt hơn"
    }
}

# Lối sống
LIFESTYLE = {
    "title": "🏃 Lối Sống Tốt Cho Hen Suyễn",
    
    "exercise": {
        "title": "Tập Thể Dục",
        "benefit": "Tăng sức khỏe phổi, giảm đợt cấp",
        "recommended": [
            "Đi bộ 30 phút/ngày",
            "Bơi lội (tốt nhất - ẩm ướt, ít bụi)",
            "Yoga, thái cực quyền",
            "Đạp xe nhẹ"
        ],
        "precautions": [
            "Khởi động 10 phút trước",
            "Xịt thuốc cắt cơn trước tập (nếu bác sĩ chỉ định)",
            "Nghỉ ngay nếu khó thở",
            "Tránh tập khi không khí ô nhiễm"
        ],
        "warning": "Nếu hen do tập thể dục → Dùng thuốc trước khi tập"
    },
    
    "diet": {
        "title": "Chế Độ Ăn",
        "foods_to_eat": [
            "Trái cây, rau xanh (chống viêm)",
            "Cá (omega-3)",
            "Thực phẩm giàu vitamin D (sữa, trứng)",
            "Gừng, nghệ (chống viêm tự nhiên)"
        ],
        "foods_to_avoid": [
            "Sulfites (rượu vang, hoa quả khô) - nếu dị ứng",
            "Thực phẩm đã từng gây dị ứng",
            "Đồ ăn nhiều muối (giữ nước → khó thở)"
        ],
        "note": "Mỗi người khác nhau, theo dõi phản ứng của mình"
    },
    
    "stress_management": {
        "title": "Quản Lý Căng Thẳng",
        "why_important": "Căng thẳng → Hen nặng hơn",
        "methods": [
            "Thở sâu, thư giãn",
            "Ngủ đủ giấc",
            "Tập thể dục nhẹ",
            "Tránh stress không cần thiết"
        ]
    }
}

# Xử trí đợt cấp
EXACERBATION_MANAGEMENT = {
    "title": "🚨 Xử Trí Đợt Cấp",
    
    "mild_moderate": {
        "title": "Cơn Hen Nhẹ → Vừa",
        "signs": [
            "Ho, khò khè",
            "Khó thở nhẹ",
            "Vẫn nói được câu dài",
            "Thuốc cắt cơn còn tác dụng"
        ],
        "action": [
            "Ngồi thẳng, bình tĩnh",
            "Xịt thuốc cắt cơn (1-2 nhát)",
            "Đợi 5-10 phút",
            "Nếu không đỡ → Xịt thêm 2 nhát",
            "Nghỉ ngơi, theo dõi",
            "Gọi bác sĩ nếu không cải thiện"
        ]
    },
    
    "severe": {
        "title": "Cơn Hen Nặng",
        "signs": [
            "Khó thở NẶNG",
            "Không nói được câu dài",
            "Môi, đầu ngón tay tím",
            "Thuốc cắt cơn KHÔNG tác dụng",
            "Co kéo cơ liên sườn"
        ],
        "action": [
            "📞 GỌI 115 NGAY!",
            "Xịt thuốc cắt cơn 2-4 nhát (đợi 1-2 phút giữa các lần)",
            "Dùng Corticosteroid uống (nếu có, theo chỉ định)",
            "Ngồi thẳng, không nằm",
            "Mở cửa sổ, thông thoáng",
            "Chờ xe cấp cứu"
        ],
        "while_waiting": [
            "Tiếp tục xịt thuốc cắt cơn mỗi 5-10 phút",
            "Giữ bình tĩnh",
            "Ngồi tư thế giúp thở dễ nhất",
            "Không uống nhiều nước (có thể nghẹn)"
        ]
    }
}

