"""
Viêm phổi - Phòng ngừa
Prevention of Pneumonia
"""

from typing import Dict, List

PREVENTION = {
    "vaccination": {
        "title": "💉 Tiêm vaccine (QUAN TRỌNG NHẤT!)",
        "description": "Vaccine phòng viêm phổi hiệu quả:",
        "vaccines": [
            {
                "name": "Vaccine phế cầu (Pneumovax 23, Prevenar 13)",
                "target": "Người >65 tuổi, bệnh mãn tính (COPD, tiểu đường, suy tim)",
                "schedule": [
                    "Prevenar 13: 1 mũi (người >65 tuổi chưa tiêm)",
                    "Pneumovax 23: 1 mũi (sau Prevenar 1 năm, hoặc tiêm đơn độc)",
                    "Nhắc lại: 5 năm/lần (người suy giảm miễn dịch)"
                ],
                "effectiveness": "Giảm 50-70% nguy cơ viêm phổi do phế cầu",
                "note": "⚠️ QUAN TRỌNG cho người già, bệnh mãn tính!"
            },
            {
                "name": "Vaccine cúm (Flu shot)",
                "target": "Tất cả người >65 tuổi, bệnh mãn tính, trẻ em",
                "schedule": "Tiêm HÀNG NĂM (virus cúm thay đổi mỗi năm)",
                "effectiveness": "Giảm 40-60% nguy cơ viêm phổi do cúm",
                "note": "Cúm → Biến chứng viêm phổi nặng (đặc biệt người già)"
            },
            {
                "name": "Vaccine COVID-19",
                "target": "Tất cả mọi người",
                "schedule": "Theo khuyến cáo hiện tại (mũi nhắc lại)",
                "effectiveness": "Giảm 80-90% nguy cơ viêm phổi nặng do COVID-19",
                "note": "COVID-19 → Viêm phổi nặng, tử vong cao"
            }
        ]
    },
    
    "lifestyle": {
        "title": "🏃 Lối sống lành mạnh",
        "recommendations": [
            {
                "name": "Bỏ thuốc lá",
                "description": "Hút thuốc → Phổi yếu, dễ nhiễm trùng",
                "benefit": "Giảm 50% nguy cơ viêm phổi",
                "note": "⚠️ QUAN TRỌNG NHẤT!"
            },
            {
                "name": "Rửa tay thường xuyên",
                "description": "Rửa tay bằng xà phòng hoặc nước rửa tay khô",
                "when": [
                    "Sau khi ho, hắt hơi",
                    "Trước khi ăn, nấu ăn",
                    "Sau khi đi vệ sinh",
                    "Sau khi tiếp xúc với người bệnh"
                ]
            },
            {
                "name": "Đeo khẩu trang",
                "description": "Khi ra ngoài, tiếp xúc người bệnh",
                "benefit": "Giảm lây nhiễm vi khuẩn, virus",
                "note": "Đặc biệt quan trọng trong mùa cúm, COVID-19"
            },
            {
                "name": "Tránh tiếp xúc người bệnh",
                "description": "Người bệnh viêm phổi, cúm, COVID-19",
                "if_necessary": "Đeo khẩu trang, giữ khoảng cách"
            },
            {
                "name": "Ăn uống đầy đủ",
                "description": "Dinh dưỡng tốt → Miễn dịch khỏe",
                "foods": [
                    "Rau xanh, trái cây (vitamin C, A)",
                    "Thực phẩm giàu protein (thịt, cá, đậu)",
                    "Uống đủ nước"
                ]
            },
            {
                "name": "Tập thể dục",
                "description": "Tăng cường sức khỏe, miễn dịch",
                "recommendation": "Đi bộ 30 phút/ngày, 5 ngày/tuần"
            },
            {
                "name": "Ngủ đủ giấc",
                "description": "Ngủ 7-8 giờ/đêm → Miễn dịch khỏe",
                "note": "Thiếu ngủ → Dễ nhiễm trùng"
            }
        ]
    },
    
    "special_populations": {
        "title": "👴 Phòng ngừa cho người già",
        "recommendations": [
            {
                "name": "Tiêm vaccine đầy đủ",
                "priority": "Cao nhất",
                "vaccines": [
                    "Vaccine phế cầu (Pneumovax 23 hoặc Prevenar 13)",
                    "Vaccine cúm (hàng năm)",
                    "Vaccine COVID-19 (theo lịch)"
                ]
            },
            {
                "name": "Quản lý bệnh mãn tính",
                "description": "Kiểm soát tốt bệnh nền → Giảm nguy cơ",
                "diseases": [
                    "COPD: Dùng thuốc đều, tránh đợt cấp",
                    "Tiểu đường: Kiểm soát đường huyết",
                    "Suy tim: Uống thuốc đều, tránh phù phổi"
                ]
            },
            {
                "name": "Phòng ngã",
                "description": "Ngã → Nằm liệt giường → Dễ viêm phổi",
                "measures": [
                    "Tập thể dục tăng cơ, thăng bằng",
                    "Đảm bảo nhà cửa an toàn (không trơn trượt)",
                    "Dùng gậy, nạng nếu cần"
                ]
            },
            {
                "name": "Tránh hít sặc",
                "description": "Người già dễ hít sặc → Viêm phổi hít sặc",
                "measures": [
                    "Ăn chậm, nhai kỹ",
                    "Ngồi thẳng khi ăn",
                    "Tránh ăn quá no",
                    "Nếu nuốt khó: Tham khảo bác sĩ"
                ]
            }
        ]
    },
    
    "children": {
        "title": "👶 Phòng ngừa cho trẻ em",
        "recommendations": [
            {
                "name": "Tiêm vaccine đầy đủ",
                "vaccines": [
                    "Vaccine phế cầu (Prevenar 13) - Trong lịch tiêm chủng",
                    "Vaccine cúm (từ 6 tháng tuổi)",
                    "Vaccine Hib, DPT - Phòng viêm phổi do Haemophilus, ho gà"
                ]
            },
            {
                "name": "Nuôi con bằng sữa mẹ",
                "description": "Sữa mẹ → Miễn dịch tốt cho trẻ",
                "duration": "Khuyến nghị ít nhất 6 tháng"
            },
            {
                "name": "Vệ sinh",
                "measures": [
                    "Rửa tay trước khi cho trẻ ăn",
                    "Tránh tiếp xúc người bệnh",
                    "Đeo khẩu trang khi ra ngoài"
                ]
            },
            {
                "name": "Tránh khói thuốc",
                "description": "Khói thuốc thụ động → Trẻ dễ viêm phổi",
                "warning": "⚠️ KHÔNG hút thuốc gần trẻ!"
            }
        ]
    },
    
    "warning_signs": {
        "title": "⚠️ Khi nào cần đi khám ngay?",
        "signs": [
            {
                "name": "Triệu chứng nặng",
                "details": [
                    "Sốt cao >39°C không hạ",
                    "Khó thở nặng, thở nhanh",
                    "Lơ mơ, không tỉnh táo",
                    "Môi, đầu ngón tay tím tái"
                ]
            },
            {
                "name": "Không đáp ứng điều trị",
                "details": [
                    "Uống kháng sinh 3 ngày vẫn sốt",
                    "Ho, khó thở nặng hơn",
                    "Mệt mỏi nhiều hơn"
                ]
            },
            {
                "name": "Yếu tố nguy cơ",
                "details": [
                    "Người >65 tuổi",
                    "Bệnh mãn tính (COPD, tiểu đường, suy tim)",
                    "Suy giảm miễn dịch",
                    "Trẻ <5 tuổi"
                ],
                "note": "→ Nên đi khám SỚM, không đợi nặng!"
            }
        ],
        "emergency": "🚨 GỌI 115 NGAY nếu: Khó thở nặng, lơ mơ, tím tái, huyết áp tụt"
    }
}

