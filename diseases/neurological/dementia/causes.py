"""
Sa Sút Trí Tuệ - Nguyên nhân và yếu tố nguy cơ
Causes and Risk Factors of Dementia
"""

from typing import Dict, List

CAUSES = {
    "alzheimer_causes": {
        "title": "🔍 Nguyên Nhân Alzheimer (Chưa rõ hoàn toàn)",
        "description": "Alzheimer có thể do:",
        "theories": [
            {
                "name": "Tích tụ protein bất thường",
                "description": "Beta-amyloid và Tau tích tụ trong não → Tổn thương tế bào não",
                "simple": "Giống như rác tích tụ trong nhà → Nhà không dùng được"
            },
            {
                "name": "Viêm não",
                "description": "Viêm mạn tính trong não → Tổn thương tế bào",
                "simple": "Giống như viêm khớp, nhưng ở não"
            },
            {
                "name": "Mất kết nối tế bào thần kinh",
                "description": "Tế bào não mất liên kết → Thông tin không truyền được",
                "simple": "Giống như dây điện đứt → Đèn không sáng"
            }
        ],
        "note": "⚠️ Vẫn đang nghiên cứu, chưa có thuốc chữa khỏi hoàn toàn"
    },
    
    "vascular_causes": {
        "title": "🔍 Nguyên Nhân Sa Sút Trí Tuệ Mạch Máu",
        "description": "Do tổn thương mạch máu não:",
        "causes": [
            {
                "name": "Đột quỵ",
                "description": "Mạch máu não tắc/vỡ → Tổn thương não",
                "mechanism": "Mỗi đột quỵ → Mất một phần chức năng não → Sa sút trí tuệ"
            },
            {
                "name": "Tổn thương mạch máu nhỏ",
                "description": "Mạch máu nhỏ trong não bị tổn thương (do tăng huyết áp, tiểu đường)",
                "mechanism": "Não không nhận đủ máu → Tế bào não chết"
            },
            {
                "name": "Xơ vữa động mạch",
                "description": "Mạch máu não bị hẹp → Thiếu máu nuôi não",
                "mechanism": "Giống như ống nước nghẹt → Nước không đến được"
            }
        ],
        "prevention": "⚠️ CÓ THỂ PHÒNG NGỪA bằng: Kiểm soát huyết áp, tiểu đường, bỏ thuốc lá"
    },
    
    "risk_factors": {
        "title": "⚠️ Yếu Tố Nguy Cơ",
        "description": "Những người có nguy cơ cao bị sa sút trí tuệ:",
        "cannot_change": [
            {
                "name": "Tuổi tác",
                "description": "Càng già, nguy cơ càng cao",
                "facts": [
                    "65-74 tuổi: ~3%",
                    "75-84 tuổi: ~15%",
                    "≥85 tuổi: ~30-50%"
                ]
            },
            {
                "name": "Gen di truyền",
                "description": "Có người thân (bố, mẹ, anh, chị) bị Alzheimer",
                "risk": "Tăng nguy cơ 2-3 lần",
                "note": "Nhưng KHÔNG có nghĩa chắc chắn bị!"
            },
            {
                "name": "Giới tính",
                "description": "Nữ có nguy cơ cao hơn nam (có thể do sống lâu hơn)"
            }
        ],
        "can_change": [
            {
                "name": "Tăng huyết áp",
                "description": "Tăng nguy cơ 1.5-2 lần",
                "action": "Kiểm soát huyết áp <140/90 mmHg",
                "benefit": "Giảm nguy cơ 30-40%"
            },
            {
                "name": "Tiểu đường",
                "description": "Tăng nguy cơ 2 lần",
                "action": "Kiểm soát đường huyết tốt (HbA1c <7%)",
                "benefit": "Giảm nguy cơ 20-30%"
            },
            {
                "name": "Hút thuốc lá",
                "description": "Tăng nguy cơ 1.5-2 lần",
                "action": "BỎ THUỐC LÁ",
                "benefit": "Giảm nguy cơ 30-40%"
            },
            {
                "name": "Béo phì",
                "description": "Tăng nguy cơ 1.5 lần",
                "action": "Giảm cân, BMI <25",
                "benefit": "Giảm nguy cơ 20-30%"
            },
            {
                "name": "Ít vận động",
                "description": "Tăng nguy cơ 1.5 lần",
                "action": "Tập thể dục 30 phút/ngày, 5 ngày/tuần",
                "benefit": "Giảm nguy cơ 30-50%"
            },
            {
                "name": "Ít rèn luyện trí não",
                "description": "Tăng nguy cơ 1.5-2 lần",
                "action": "Đọc sách, học hỏi, chơi cờ, giải đố",
                "benefit": "Giảm nguy cơ 30-50%"
            },
            {
                "name": "Cô đơn, ít giao tiếp",
                "description": "Tăng nguy cơ 1.5 lần",
                "action": "Tham gia hoạt động xã hội, trò chuyện với người thân",
                "benefit": "Giảm nguy cơ 20-30%"
            },
            {
                "name": "Trầm cảm",
                "description": "Tăng nguy cơ 1.5-2 lần",
                "action": "Điều trị trầm cảm (thuốc, tâm lý)",
                "benefit": "Giảm nguy cơ 20-30%"
            },
            {
                "name": "Chấn thương đầu",
                "description": "Tăng nguy cơ 1.5-2 lần",
                "action": "Phòng ngừa ngã (dùng gậy, giày chống trượt)",
                "benefit": "Giảm nguy cơ chấn thương"
            }
        ]
    },
    
    "protective_factors": {
        "title": "✅ Yếu Tố Bảo Vệ (Giảm Nguy Cơ)",
        "description": "Những điều LÀM GIẢM nguy cơ sa sút trí tuệ:",
        "factors": [
            {
                "name": "Rèn luyện trí não",
                "activities": [
                    "Đọc sách, báo hàng ngày",
                    "Chơi cờ, giải đố, sudoku",
                    "Học kỹ năng mới (nấu ăn, thủ công)",
                    "Học ngoại ngữ"
                ],
                "benefit": "Giảm nguy cơ 30-50%",
                "mechanism": "Tạo kết nối mới giữa tế bào não → Bù đắp tổn thương"
            },
            {
                "name": "Tập thể dục đều đặn",
                "activities": [
                    "Đi bộ 30 phút/ngày",
                    "Khiêu vũ, yoga",
                    "Bơi lội",
                    "Tập kháng lực (tạ nhẹ)"
                ],
                "benefit": "Giảm nguy cơ 30-50%",
                "mechanism": "Tăng máu lên não, tăng chất bảo vệ tế bào não"
            },
            {
                "name": "Ăn uống lành mạnh",
                "foods": [
                    "Chế độ Địa Trung Hải: Nhiều rau, cá, dầu olive",
                    "Omega-3 (cá hồi, cá thu)",
                    "Chất chống oxy hóa (quả mọng, rau xanh)",
                    "Ít đường, mỡ động vật"
                ],
                "benefit": "Giảm nguy cơ 20-30%"
            },
            {
                "name": "Ngủ đủ giấc",
                "duration": "7-8 giờ/ngày",
                "benefit": "Não được nghỉ ngơi, phục hồi",
                "mechanism": "Giấc ngủ giúp não loại bỏ chất độc tích tụ"
            },
            {
                "name": "Giao tiếp xã hội",
                "activities": [
                    "Trò chuyện với người thân, bạn bè",
                    "Tham gia câu lạc bộ, hoạt động tình nguyện",
                    "Chơi với cháu, con"
                ],
                "benefit": "Giảm nguy cơ 20-30%",
                "mechanism": "Kích thích não, giảm cô đơn → Giảm trầm cảm"
            },
            {
                "name": "Kiểm soát bệnh mãn tính",
                "diseases": [
                    "Tăng huyết áp: <140/90 mmHg",
                    "Tiểu đường: HbA1c <7%",
                    "Mỡ máu: LDL <100 mg/dL"
                ],
                "benefit": "Giảm nguy cơ 30-40%",
                "mechanism": "Bảo vệ mạch máu não"
            }
        ]
    }
}

