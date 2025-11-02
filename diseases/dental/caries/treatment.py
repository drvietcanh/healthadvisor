"""
Caries - Điều trị
"""

TREATMENT = {
    "early": {
        "title": "💊 Điều trị sớm (Đốm trắng, sâu nhẹ):",
        "fluoride": {
            "title": "Bôi Fluoride:",
            "description": "Fluoride giúp men răng tái khoáng → Ngăn sâu răng tiến triển",
            "where": "Bác sĩ bôi tại phòng khám",
            "frequency": "Mỗi 3-6 tháng"
        },
        "sealants": {
            "title": "Trám phòng ngừa (Sealants):",
            "description": "Trám lỗ hổng trên mặt nhai răng hàm → Ngăn thức ăn dính",
            "when": "Răng hàm có rãnh sâu, dễ sâu",
            "benefit": "Giảm 80% nguy cơ sâu răng hàm"
        }
    },
    
    "moderate": {
        "title": "💊 Điều trị vừa (Có lỗ sâu, chưa đến tủy):",
        "filling": {
            "title": "Trám răng (Filling):",
            "description": "Làm sạch lỗ sâu → Trám bằng vật liệu (amalgam, composite)",
            "process": [
                "Gây tê cục bộ (nếu cần)",
                "Khoan, làm sạch lỗ sâu",
                "Trám bằng vật liệu",
                "Đánh bóng"
            ],
            "duration": "Một lần hẹn, 30-60 phút",
            "cost": "Rẻ (so với chữa tủy, bọc răng)",
            "note": "✅ Điều trị đơn giản, hiệu quả nếu chữa sớm!"
        }
    },
    
    "severe": {
        "title": "💊 Điều trị nặng (Sâu đến tủy):",
        "root_canal": {
            "title": "Chữa tủy răng (Root Canal Treatment):",
            "description": "Lấy tủy răng (thần kinh) → Làm sạch ống tủy → Trám lại",
            "process": [
                "Gây tê",
                "Khoan vào răng, lấy tủy",
                "Làm sạch ống tủy",
                "Trám ống tủy",
                "Bọc răng (thường cần) để bảo vệ răng yếu"
            ],
            "duration": "2-3 lần hẹn, mỗi lần 1-2 giờ",
            "cost": "Đắt (gấp 5-10 lần trám răng)",
            "note": "⚠️ Phức tạp, tốn thời gian, đắt tiền! Chữa sớm để tránh!"
        },
        "extraction": {
            "title": "Nhổ răng (Khi không thể chữa):",
            "when": [
                "Sâu quá nặng, không thể chữa được",
                "Răng lung lay nhiều",
                "Nhiễm trùng nặng"
            ],
            "consequences": [
                "Mất răng → Phải trồng răng (rất đắt)",
                "Ảnh hưởng răng bên cạnh",
                "Ảnh hưởng thẩm mỹ, chức năng nhai"
            ],
            "note": "⚠️ Nhổ răng là biện pháp cuối cùng! Cố gắng giữ răng nếu có thể!"
        }
    },
    
    "prevention": {
        "title": "✅ Phòng ngừa (QUAN TRỌNG NHẤT):",
        "oral_hygiene": {
            "title": "Vệ sinh răng miệng:",
            "tips": [
                "✅ Đánh răng 2 lần/ngày (sáng và tối trước khi ngủ)",
                "✅ Đánh răng đúng cách - Chải kỹ, 2-3 phút",
                "✅ Dùng chỉ nha khoa hàng ngày - Làm sạch kẽ răng",
                "✅ Súc miệng bằng nước súc miệng có Fluoride",
                "✅ Thay bàn chải mỗi 3 tháng"
            ]
        },
        "diet": {
            "title": "Chế độ ăn:",
            "avoid": [
                "❌ Đồ ngọt - Kẹo, bánh, nước ngọt (đặc biệt trước khi ngủ)",
                "❌ Ăn vặt thường xuyên - Làm axit liên tục",
                "❌ Uống nước ngọt nhiều - Axit + đường"
            ],
            "recommend": [
                "✅ Ăn ít đường",
                "✅ Nếu ăn ngọt → Đánh răng ngay sau đó",
                "✅ Uống nước lọc thay vì nước ngọt",
                "✅ Ăn trái cây thay vì kẹo"
            ]
        },
        "regular_checkup": {
            "title": "Khám răng định kỳ:",
            "frequency": "Mỗi 6 tháng - 1 năm",
            "benefits": [
                "Phát hiện sâu răng sớm (trước khi đau)",
                "Làm sạch vôi răng (cao răng)",
                "Bôi Fluoride",
                "Chữa sớm → Rẻ, dễ"
            ]
        },
        "fluoride": {
            "title": "Fluoride:",
            "toothpaste": "Dùng kem đánh răng có Fluoride",
            "water": "Nước có Fluoride (ở một số nơi)",
            "supplements": "Viên Fluoride (nếu bác sĩ chỉ định)"
        }
    },
    
    "when_to_see_doctor": {
        "title": "🏥 Khi nào cần khám bác sĩ:",
        "regular": "Khám định kỳ mỗi 6 tháng - 1 năm (ngay cả khi không đau!)",
        "urgent": [
            "🚨 Đau răng dữ dội",
            "🚨 Đau ban đêm",
            "🚨 Sưng nướu, mặt",
            "🚨 Sốt kèm đau răng"
        ],
        "note": "💡 QUAN TRỌNG: Đừng đợi đến khi đau! Khám định kỳ để phát hiện sớm!"
    }
}

