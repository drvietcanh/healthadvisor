"""
Sa Sút Trí Tuệ - Phòng ngừa
Prevention of Dementia
"""

from typing import Dict, List

PREVENTION = {
    "lifestyle": {
        "title": "🏃 Thay Đổi Lối Sống",
        "description": "Các biện pháp PHÒNG NGỪA hiệu quả:",
        "methods": [
            {
                "name": "🧠 Rèn Luyện Trí Não",
                "priority": "QUAN TRỌNG NHẤT!",
                "activities": [
                    "Đọc sách, báo hàng ngày (30 phút/ngày)",
                    "Chơi cờ, giải đố, sudoku",
                    "Học kỹ năng mới (nấu món mới, học nhạc cụ)",
                    "Học ngoại ngữ",
                    "Chơi game trí não (theo mức độ vừa phải)"
                ],
                "benefit": "Giảm nguy cơ 30-50%",
                "mechanism": "Tạo kết nối mới giữa tế bào não → Bù đắp khi có tổn thương",
                "note": "💡 Quan trọng: Rèn luyện ĐỀU ĐẶN, không phải thỉnh thoảng!"
            },
            {
                "name": "🏃 Tập Thể Dục",
                "recommendation": "150 phút/tuần (30 phút × 5 ngày)",
                "activities": [
                    "Đi bộ nhanh",
                    "Khiêu vũ",
                    "Yoga, thái cực quyền",
                    "Bơi lội",
                    "Tập kháng lực (tạ nhẹ)"
                ],
                "benefit": "Giảm nguy cơ 30-50%",
                "mechanism": [
                    "Tăng máu lên não → Nuôi dưỡng tế bào não",
                    "Tăng chất bảo vệ tế bào não (BDNF)",
                    "Giảm viêm trong não"
                ]
            },
            {
                "name": "🍽️ Ăn Uống Lành Mạnh",
                "diet": "Chế độ Địa Trung Hải (Mediterranean Diet)",
                "foods": [
                    "Nhiều rau xanh (rau cải, bông cải xanh)",
                    "Quả mọng (dâu, việt quất) - Chất chống oxy hóa",
                    "Cá (2-3 lần/tuần): Cá hồi, cá thu - Omega-3",
                    "Ngũ cốc nguyên hạt: Gạo lứt, bánh mì đen",
                    "Đậu, hạt: Đậu nành, hạnh nhân",
                    "Dầu olive, dầu đậu nành"
                ],
                "limit": [
                    "Đường: <25g/ngày",
                    "Thịt đỏ: <3 lần/tuần",
                    "Thực phẩm chế biến sẵn",
                    "Mỡ động vật"
                ],
                "benefit": "Giảm nguy cơ 20-30%"
            },
            {
                "name": "😴 Ngủ Đủ Giấc",
                "duration": "7-8 giờ/ngày",
                "benefit": [
                    "Não được nghỉ ngơi, phục hồi",
                    "Loại bỏ chất độc tích tụ trong não",
                    "Củng cố trí nhớ",
                    "Giảm nguy cơ 20-30%"
                ],
                "tips": [
                    "Đi ngủ đều giờ",
                    "Tránh xem màn hình trước khi ngủ",
                    "Phòng ngủ tối, yên tĩnh",
                    "Tránh cà phê, rượu buổi tối"
                ]
            },
            {
                "name": "👥 Giao Tiếp Xã Hội",
                "activities": [
                    "Trò chuyện với người thân, bạn bè hàng ngày",
                    "Tham gia câu lạc bộ (đọc sách, khiêu vũ...)",
                    "Hoạt động tình nguyện",
                    "Chơi với cháu, con"
                ],
                "benefit": "Giảm nguy cơ 20-30%",
                "mechanism": "Kích thích não, giảm cô đơn → Giảm trầm cảm"
            },
            {
                "name": "🚭 Bỏ Thuốc Lá",
                "benefit": "Giảm nguy cơ 30-40%",
                "mechanism": "Tổn thương mạch máu não → Thiếu máu nuôi não"
            },
            {
                "name": "⚖️ Kiểm Soát Bệnh Mãn Tính",
                "diseases": [
                    {
                        "name": "Tăng huyết áp",
                        "target": "<140/90 mmHg (tốt nhất <130/80)",
                        "benefit": "Giảm nguy cơ 30-40%"
                    },
                    {
                        "name": "Tiểu đường",
                        "target": "HbA1c <7%",
                        "benefit": "Giảm nguy cơ 20-30%"
                    },
                    {
                        "name": "Mỡ máu cao",
                        "target": "LDL <100 mg/dL",
                        "benefit": "Giảm nguy cơ 20-30%"
                    }
                ]
            },
            {
                "name": "🧘 Giảm Căng Thẳng",
                "activities": [
                    "Thiền, yoga",
                    "Thở sâu",
                    "Nghe nhạc",
                    "Làm việc mình thích"
                ],
                "benefit": "Giảm viêm trong não, bảo vệ tế bào não"
            }
        ]
    },
    
    "brain_health": {
        "title": "🧠 Sức Khỏe Não Bộ",
        "description": "Giữ cho não khỏe mạnh:",
        "tips": [
            {
                "name": "Rèn luyện trí não đều đặn",
                "description": "Giống như tập thể dục cho cơ, cần 'tập' cho não",
                "frequency": "Mỗi ngày, ít nhất 15-30 phút"
            },
            {
                "name": "Bảo vệ đầu",
                "description": "Tránh chấn thương đầu",
                "methods": [
                    "Đội mũ bảo hiểm khi đi xe máy",
                    "Phòng ngừa ngã (dùng gậy, giày chống trượt)",
                    "Đảm bảo nhà cửa an toàn (không vấp)"
                ]
            },
            {
                "name": "Kiểm tra thính giác, thị giác",
                "description": "Nghe kém, nhìn kém → Não phải làm việc vất vả hơn",
                "action": "Khám định kỳ, đeo máy trợ thính, kính mắt nếu cần"
            }
        ]
    },
    
    "early_intervention": {
        "title": "⚡ Phát Hiện Sớm và Can Thiệp",
        "description": "Phát hiện SỚM → Điều trị SỚM → Làm chậm tiến triển:",
        "importance": [
            "Điều trị trong giai đoạn đầu → Hiệu quả tốt hơn",
            "Có thể duy trì chức năng lâu hơn",
            "Người bệnh vẫn có thể sống có ý nghĩa nhiều năm",
            "Gia đình có thời gian chuẩn bị, học cách chăm sóc"
        ],
        "what_to_do": [
            "Quan sát dấu hiệu sớm (quên, lú lẫn)",
            "Đi khám bác sĩ thần kinh khi nghi ngờ",
            "Bắt đầu điều trị càng sớm càng tốt",
            "Thay đổi lối sống ngay (rèn luyện trí não, tập thể dục)"
        ],
        "warning": "⚠️ Đừng chủ quan: 'Già rồi, quên là bình thường' → Có thể là sa sút trí tuệ!"
    }
}

