"""
Nocturia - Điều trị
"""

TREATMENT = {
    "find_cause": {
        "title": "🎯 Bước 1: Tìm nguyên nhân (QUAN TRỌNG NHẤT):",
        "description": "Phải tìm nguyên nhân mới điều trị được!",
        "tests": [
            "Xét nghiệm đường huyết (xem có tiểu đường không)",
            "Xét nghiệm chức năng thận (creatinine, ure)",
            "Xét nghiệm nước tiểu (xem có nhiễm trùng không)",
            "Siêu âm bàng quang, tuyến tiền liệt (nam giới)",
            "Ghi nhật ký tiểu tiện (bao nhiêu lần/đêm, lượng nước uống)"
        ]
    },
    
    "lifestyle": {
        "title": "💧 Thay đổi lối sống (QUAN TRỌNG - Áp dụng ngay):",
        "fluid_management": {
            "title": "Quản lý nước uống:",
            "tips": [
                "✅ Uống nhiều nước vào BAN NGÀY (trước 6 giờ chiều)",
                "✅ GIẢM nước uống sau 6 giờ tối (chỉ uống khi thật khát)",
                "❌ TRÁNH: Cà phê, trà, rượu bia 4-6 giờ trước khi ngủ",
                "❌ TRÁNH: Uống quá nhiều nước trước khi ngủ (1-2 ly là đủ)"
            ]
        },
        "sleep_hygiene": {
            "title": "Vệ sinh giấc ngủ:",
            "tips": [
                "✅ Đi tiểu TRƯỚC khi ngủ (dù không buồn)",
                "✅ Đi tiểu lại ngay trước khi lên giường",
                "✅ Để đèn ngủ sáng khi đi tiểu ban đêm (tránh ngã)",
                "✅ Lắp tay vịn trong nhà vệ sinh (an toàn)"
            ]
        },
        "leg_elevation": {
            "title": "Nếu có phù chân:",
            "tips": [
                "✅ Kê cao chân khi ngủ (giảm phù)",
                "✅ Mang vớ ép (nếu bác sĩ chỉ định)",
                "✅ Tránh đứng/ngồi lâu ban ngày"
            ]
        }
    },
    
    "medications": {
        "title": "💊 Thuốc điều trị (Theo nguyên nhân):",
        "overactive_bladder": {
            "title": "Nếu bàng quang hoạt động quá mức:",
            "examples": [
                "Oxybutynin (Ditropan) - Giảm co thắt bàng quang",
                "Tolterodine (Detrol)",
                "Solifenacin (Vesicare)"
            ],
            "note": "⚠️ Có thể gây khô miệng, táo bón"
        },
        "antidiuretic": {
            "title": "Thuốc giảm tiết nước tiểu ban đêm:",
            "examples": [
                "Desmopressin (DDAVP) - Giảm sản xuất nước tiểu ban đêm",
                "Chỉ dùng khi không có suy thận, suy tim"
            ],
            "warning": "⚠️ Cần bác sĩ kê đơn, không tự ý dùng!"
        },
        "bph": {
            "title": "Nếu do phì đại tuyến tiền liệt:",
            "note": "→ Xem phần Phì Đại Tuyến Tiền Liệt",
            "examples": [
                "Tamsulosin (Flomax) - Giãn cơ tuyến tiền liệt",
                "Finasteride - Giảm kích thước tuyến tiền liệt"
            ]
        },
        "diabetes": {
            "title": "Nếu do tiểu đường:",
            "note": "→ Kiểm soát đường huyết tốt → Giảm tiểu đêm",
            "meds": "Thuốc điều trị tiểu đường (theo chỉ định)"
        }
    },
    
    "when_to_see_doctor": {
        "title": "🏥 Khi nào cần khám bác sĩ:",
        "soon": [
            "Tiểu đêm ≥2 lần/đêm, ảnh hưởng giấc ngủ",
            "Tiểu đêm mới xuất hiện (trước đây không có)",
            "Kèm theo: Tiểu buốt, tiểu rắt, tiểu máu",
            "Kèm theo: Phù chân, khó thở (suy tim)",
            "Kèm theo: Khát nước nhiều, sụt cân (tiểu đường)"
        ],
        "urgent": [
            "🚨 Tiểu đêm kèm không tiểu được (bí tiểu)",
            "🚨 Tiểu máu",
            "🚨 Sốt, đau lưng (nhiễm trùng thận)"
        ]
    }
}

