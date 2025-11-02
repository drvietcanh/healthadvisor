"""
UTI - Điều trị
"""

TREATMENT = {
    "medications": {
        "title": "💊 Thuốc điều trị:",
        "antibiotics": {
            "title": "Kháng sinh (BẮT BUỘC):",
            "common": [
                {
                    "name": "Nitrofurantoin (Furadantin)",
                    "dose": "100mg x 2 lần/ngày",
                    "duration": "5-7 ngày",
                    "note": "Thuốc đầu tay, hiệu quả, rẻ"
                },
                {
                    "name": "Trimethoprim/Sulfamethoxazole (Bactrim)",
                    "dose": "Theo chỉ định bác sĩ",
                    "duration": "3-7 ngày",
                    "note": "Hiệu quả, nhưng có thể dị ứng"
                },
                {
                    "name": "Ciprofloxacin",
                    "dose": "250-500mg x 2 lần/ngày",
                    "duration": "3-7 ngày",
                    "note": "Dùng khi viêm nặng, có nguy cơ kháng thuốc"
                }
            ],
            "warning": "⚠️ QUAN TRỌNG: Uống ĐỦ LIỀU, ĐỦ NGÀY (dù hết triệu chứng)! Nếu bỏ giữa chừng → Vi khuẩn kháng thuốc, khó chữa hơn!"
        },
        "pain_relief": {
            "title": "Thuốc giảm đau:",
            "options": [
                "Paracetamol (Panadol) - 500mg x 2-3 lần/ngày",
                "Ibuprofen (Brufen) - 400mg x 2-3 lần/ngày (nếu không đau dạ dày)"
            ]
        }
    },
    
    "self_care": {
        "title": "💧 Chăm sóc tại nhà:",
        "drink_water": {
            "title": "Uống nhiều nước:",
            "amount": "2-3 lít/ngày",
            "why": "Nước tiểu nhiều → Rửa trôi vi khuẩn",
            "tip": "Uống nước lọc, nước trà (không đường)"
        },
        "urinate": {
            "title": "Đi tiểu thường xuyên:",
            "tip": "Đừng nhịn tiểu! Đi tiểu ngay khi muốn",
            "why": "Nhịn tiểu → Vi khuẩn nhân lên trong bàng quang"
        },
        "hygiene": {
            "title": "Vệ sinh sạch sẽ:",
            "tips": [
                "Lau từ trước ra sau sau khi đi vệ sinh (phụ nữ)",
                "Tắm rửa hàng ngày",
                "Mặc quần lót cotton, thoáng mát",
                "Thay quần lót hàng ngày"
            ]
        },
        "avoid": {
            "title": "Tránh:",
            "items": [
                "Cà phê, rượu, nước ngọt (kích thích bàng quang)",
                "Đồ cay, nóng",
                "Quan hệ tình dục khi đang bị (để tránh lây nhiễm)"
            ]
        }
    },
    
    "when_to_see_doctor": {
        "title": "🏥 Khi nào cần khám bác sĩ:",
        "urgent": [
            "🚨 Sốt cao (>38.5°C) với ớn lạnh",
            "🚨 Đau lưng dữ dội (viêm thận)",
            "🚨 Triệu chứng không đỡ sau 2-3 ngày dùng thuốc",
            "🚨 Có máu trong nước tiểu nhiều",
            "🚨 Buồn nôn, nôn không ăn được"
        ],
        "soon": [
            "Triệu chứng nhẹ nhưng kéo dài > 3 ngày",
            "Bị UTI nhiều lần (tái phát)",
            "Người già, có bệnh tiểu đường",
            "Đang mang thai"
        ]
    },
    
    "prevention": {
        "title": "✅ Phòng ngừa:",
        "tips": [
            "Uống đủ nước (2-3 lít/ngày)",
            "Đi tiểu sau khi quan hệ tình dục",
            "Vệ sinh sạch sẽ, lau từ trước ra sau",
            "Không nhịn tiểu lâu",
            "Mặc quần lót thoáng mát, cotton",
            "Tránh dùng xà phòng thơm ở vùng kín (gây kích ứng)",
            "Phụ nữ: Tránh thụt rửa âm đạo (làm mất vi khuẩn tốt)"
        ]
    }
}

