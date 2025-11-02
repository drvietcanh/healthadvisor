"""
Suy Thận Mạn - Triệu chứng
Symptoms of Chronic Kidney Disease
"""

from typing import Dict, List

SYMPTOMS = {
    "early_stage": {
        "title": "🔍 Triệu Chứng Giai Đoạn Sớm (1-3)",
        "description": "⚠️ QUAN TRỌNG: Giai đoạn sớm THƯỜNG KHÔNG CÓ TRIỆU CHỨNG!",
        "symptoms": [
            {
                "name": "KHÔNG CÓ TRIỆU CHỨNG",
                "icon": "😶",
                "description": "90% người suy thận giai đoạn 1-3 KHÔNG có triệu chứng!",
                "why": "Thận có khả năng bù trừ → Dù chỉ còn 50% chức năng vẫn chưa có triệu chứng",
                "warning": "⚠️ Đây là lý do tại sao 90% người không biết mình bị suy thận!",
                "detection": "Chỉ phát hiện qua xét nghiệm: Creatinine, protein trong nước tiểu"
            },
            {
                "name": "Protein trong nước tiểu",
                "icon": "🧪",
                "description": "Nước tiểu có bọt, đục",
                "simple": "Thận rò rỉ protein → Nước tiểu có bọt (như bọt xà phòng)",
                "test": "Xét nghiệm nước tiểu: Protein dương tính",
                "significance": "Dấu hiệu SỚM NHẤT của tổn thương thận!"
            },
            {
                "name": "Mệt mỏi nhẹ",
                "icon": "😴",
                "description": "Mệt mỏi không rõ nguyên nhân",
                "why": "Thận giảm sản xuất hormone tạo máu → Thiếu máu nhẹ → Mệt mỏi",
                "note": "Dễ nhầm với mệt mỏi do tuổi tác, công việc"
            },
            {
                "name": "Phù nhẹ",
                "icon": "💧",
                "description": "Phù mặt, chân (đặc biệt buổi sáng)",
                "why": "Thận không đào thải được nước → Tích nước trong cơ thể",
                "note": "Dễ nhầm với phù do tim, gan"
            }
        ],
        "note": "⚠️ Vì không có triệu chứng rõ → Phải KHÁM ĐỊNH KỲ nếu có yếu tố nguy cơ!"
    },
    
    "moderate_stage": {
        "title": "🔍 Triệu Chứng Giai Đoạn Trung Bình-Nặng (3-4)",
        "description": "Triệu chứng bắt đầu rõ ràng:",
        "symptoms": [
            {
                "name": "Mệt mỏi nặng",
                "icon": "😴",
                "description": "Mệt đến mức không muốn làm gì",
                "why": "Thiếu máu nặng (thiếu hormone tạo máu từ thận)",
                "details": [
                    "Da xanh, nhợt nhạt",
                    "Mệt mỏi cực độ, không muốn vận động",
                    "Khó thở khi gắng sức nhẹ",
                    "Chóng mặt, hoa mắt"
                ]
            },
            {
                "name": "Phù nặng",
                "icon": "💧",
                "description": "Phù mặt, chân, tay, bụng",
                "details": [
                    "Phù nhiều hơn, kéo dài cả ngày",
                    "Ấn vào da có lỗ lõm (không phồng lại ngay)",
                    "Tăng cân do tích nước",
                    "Phù phổi (khó thở khi nằm)"
                ]
            },
            {
                "name": "Buồn nôn, nôn",
                "icon": "🤢",
                "description": "Buồn nôn, ăn không ngon",
                "why": "Chất độc (ure) tích tụ trong máu → Kích thích dạ dày",
                "details": [
                    "Buồn nôn vào buổi sáng",
                    "Chán ăn, ăn không ngon",
                    "Sụt cân",
                    "Nôn (khi ure máu rất cao)"
                ]
            },
            {
                "name": "Ngứa da",
                "icon": "🫘",
                "description": "Ngứa toàn thân, đặc biệt lưng, chân",
                "why": "Phốt pho tích tụ trong máu → Kích thích da",
                "details": [
                    "Ngứa dai dẳng, không hết",
                    "Gãi nhiều → Da bị tổn thương",
                    "Không đáp ứng với thuốc ngứa thông thường"
                ]
            },
            {
                "name": "Chuột rút, yếu cơ",
                "icon": "💪",
                "description": "Chuột rút thường xuyên, yếu cơ",
                "why": "Rối loạn điện giải (canxi, kali, phốt pho)",
                "details": [
                    "Chuột rút ban đêm",
                    "Yếu cơ, khó vận động",
                    "Tê bì tay chân"
                ]
            },
            {
                "name": "Thay đổi đi tiểu",
                "icon": "🚽",
                "description": "Tiểu ít, tiểu nhiều lần, tiểu đêm",
                "details": [
                    "Tiểu ít (nước tiểu đậm màu, ít)",
                    "Tiểu nhiều lần (thận không cô đặc được)",
                    "Tiểu đêm nhiều (3-4 lần/đêm)",
                    "Nước tiểu có bọt, đục (protein)"
                ]
            },
            {
                "name": "Hơi thở có mùi amoniac",
                "icon": "😷",
                "description": "Hơi thở có mùi tanh, amoniac",
                "why": "Ure tích tụ trong máu → Thải qua hơi thở",
                "note": "⚠️ Dấu hiệu suy thận NẶNG!"
            },
            {
                "name": "Lơ mơ, khó tập trung",
                "icon": "🧠",
                "description": "Lơ mơ, khó suy nghĩ, mất trí nhớ",
                "why": "Chất độc tích tụ trong máu → Tổn thương não",
                "details": [
                    "Lơ mơ, không tỉnh táo",
                    "Khó tập trung",
                    "Mất trí nhớ",
                    "Co giật (nếu ure máu rất cao)"
                ]
            }
        ]
    },
    
    "end_stage": {
        "title": "🔍 Giai Đoạn Cuối (5)",
        "description": "Thận không còn lọc được → Phải chạy thận:",
        "symptoms": [
            "Mệt mỏi cực độ, không thể làm gì",
            "Phù nặng, khó thở (phù phổi)",
            "Buồn nôn, nôn nhiều",
            "Lơ mơ, có thể hôn mê",
            "Chuột rút, co giật",
            "Không tiểu được (hoặc rất ít)",
            "⚠️ Không chạy thận → TỬ VONG trong vài tuần!"
        ]
    },
    
    "warning_signs": {
        "title": "🚨 DẤU HIỆU CẢNH BÁO - Cần Khám Ngay!",
        "signs": [
            "Nước tiểu có bọt, đục (protein)",
            "Nước tiểu có máu (không phải do nhiễm trùng)",
            "Phù mặt, chân không rõ nguyên nhân",
            "Mệt mỏi kéo dài, da xanh",
            "Tăng huyết áp (đặc biệt người trẻ)",
            "Tiểu đêm nhiều (>2 lần/đêm)",
            "Chuột rút thường xuyên, yếu cơ",
            "Ngứa da không rõ nguyên nhân"
        ],
        "note": "⚠️ Có bất kỳ dấu hiệu nào → Đi khám, xét nghiệm máu/nước tiểu ngay!"
    }
}

