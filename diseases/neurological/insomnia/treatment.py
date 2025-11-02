"""
Mất Ngủ - Điều trị
Treatment of Insomnia
"""

from typing import Dict, List

TREATMENT = {
    "non_medication": {
        "title": "🏃 Điều Trị Không Dùng Thuốc (QUAN TRỌNG NHẤT!)",
        "description": "Liệu pháp hành vi nhận thức (CBT-I) - Hiệu quả hơn thuốc:",
        "methods": [
            {
                "name": "Vệ Sinh Giấc Ngủ (Sleep Hygiene)",
                "description": "Thói quen tốt để ngủ ngon:",
                "rules": [
                    "Đi ngủ và thức dậy đều giờ (kể cả cuối tuần)",
                    "Chỉ lên giường khi buồn ngủ (không nằm sớm)",
                    "Không xem TV, điện thoại trong phòng ngủ",
                    "Phòng ngủ tối, yên tĩnh, mát mẻ (18-22°C)",
                    "Tránh cà phê, trà sau 14h",
                    "Tránh rượu bia (tuy giúp ngủ nhanh nhưng giảm chất lượng)",
                    "Tập thể dục buổi sáng/chiều (KHÔNG buổi tối)",
                    "Không ngủ trưa quá dài (<30 phút, không quá 15h)"
                ]
            },
            {
                "name": "Kỹ Thuật Thư Giãn",
                "methods": [
                    "Thở sâu: Hít vào 4 giây, giữ 4 giây, thở ra 4 giây",
                    "Thiền, yoga nhẹ trước khi ngủ",
                    "Nghe nhạc nhẹ",
                    "Tắm nước ấm trước khi ngủ (30 phút)",
                    "Đọc sách (không phải điện tử)"
                ]
            },
            {
                "name": "Kiểm Soát Kích Thích",
                "description": "Lên giường chỉ để ngủ (không xem TV, làm việc)",
                "rule": "Nếu nằm >20 phút không ngủ → Dậy, làm việc nhẹ, quay lại khi buồn ngủ"
            },
            {
                "name": "Hạn Chế Giấc Ngủ",
                "description": "Chỉ nằm trên giường số giờ thực sự ngủ được",
                "example": "Nếu ngủ 5 giờ/đêm → Chỉ nằm trên giường 5.5 giờ",
                "benefit": "Tăng hiệu quả giấc ngủ → Dần dần ngủ tốt hơn"
            }
        ],
        "effectiveness": "Hiệu quả 70-80% (tốt hơn thuốc ngủ!), không có tác dụng phụ"
    },
    
    "medications": {
        "title": "💊 Thuốc Ngủ (Chỉ Khi Cần)",
        "description": "Thuốc ngủ chỉ dùng ngắn hạn (<2 tuần), theo chỉ định bác sĩ:",
        "drugs": [
            {
                "name": "Melatonin",
                "description": "Hormone tự nhiên, an toàn",
                "dosage": "1-3mg, uống 1 giờ trước khi ngủ",
                "when": "Rối loạn nhịp sinh học (jet lag, làm ca đêm)",
                "safety": "An toàn, ít tác dụng phụ"
            },
            {
                "name": "Thuốc kháng histamine (Diphenhydramine)",
                "description": "Thuốc dị ứng có tác dụng phụ gây buồn ngủ",
                "when": "Mất ngủ nhẹ, thỉnh thoảng",
                "warning": "⚠️ Có thể gây khô miệng, lơ mơ ngày hôm sau"
            },
            {
                "name": "Z-drugs (Zolpidem, Zopiclone)",
                "description": "Thuốc ngủ mạnh",
                "when": "Mất ngủ nặng, ngắn hạn",
                "warning": "⚠️ Chỉ dùng <2 tuần, có nguy cơ nghiện, lệ thuộc!",
                "side_effects": "Lơ mơ ngày hôm sau, có thể làm việc khi ngủ (nguy hiểm!)"
            },
            {
                "name": "Benzodiazepines (Diazepam, Lorazepam)",
                "description": "Thuốc an thần, gây ngủ",
                "when": "Mất ngủ do lo âu",
                "warning": "⚠️ Có nguy cơ nghiện, lệ thuộc cao! Chỉ dùng ngắn hạn!",
                "elderly": "⚠️ Người già dễ té ngã, lú lẫn → Tránh dùng!"
            }
        ],
        "principles": [
            "Dùng liều thấp nhất có hiệu quả",
            "Dùng ngắn hạn (<2 tuần)",
            "Giảm dần, không ngừng đột ngột",
            "Kết hợp với liệu pháp không dùng thuốc"
        ],
        "warning": "⚠️ KHÔNG dùng thuốc ngủ lâu dài → Nghiện, lệ thuộc, giảm hiệu quả!"
    },
    
    "treat_underlying_cause": {
        "title": "🔍 Điều Trị Nguyên Nhân",
        "description": "Quan trọng: Phải tìm và điều trị nguyên nhân:",
        "conditions": [
            {
                "name": "Đau mãn tính",
                "treatment": "Thuốc giảm đau trước khi ngủ"
            },
            {
                "name": "Khó thở",
                "treatment": "Điều trị suy tim, COPD"
            },
            {
                "name": "Tiểu đêm",
                "treatment": [
                    "Hạn chế nước buổi tối",
                    "Điều trị tiểu đường, suy thận",
                    "Điều trị phì đại tuyến tiền liệt (nam giới)"
                ]
            },
            {
                "name": "Trầm cảm, lo âu",
                "treatment": "Thuốc chống trầm cảm, tư vấn tâm lý"
            },
            {
                "name": "Hội chứng ngưng thở khi ngủ",
                "treatment": "CPAP, giảm cân"
            },
            {
                "name": "Thuốc gây mất ngủ",
                "treatment": "Điều chỉnh thuốc (đổi thuốc, đổi giờ uống)"
            }
        ]
    }
}

