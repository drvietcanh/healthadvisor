"""
Mất Ngủ - Nguyên nhân
Causes of Insomnia
"""

from typing import Dict, List

CAUSES = {
    "medical_causes": {
        "title": "🏥 Nguyên Nhân Y Khoa",
        "description": "Bệnh tật gây mất ngủ:",
        "causes": [
            {
                "name": "Đau mãn tính",
                "examples": [
                    "Đau lưng, đau khớp",
                    "Đau do viêm khớp",
                    "Đau do ung thư"
                ],
                "mechanism": "Đau → Khó ngủ, tỉnh giấc"
            },
            {
                "name": "Khó thở",
                "examples": [
                    "Suy tim (khó thở khi nằm)",
                    "COPD (khó thở đêm)",
                    "Hen suyễn (cơn hen đêm)"
                ],
                "mechanism": "Khó thở → Tỉnh giấc, không ngủ được"
            },
            {
                "name": "Tiểu đêm",
                "examples": [
                    "Suy thận",
                    "Tiểu đường (tiểu nhiều)",
                    "Phì đại tuyến tiền liệt (nam giới)",
                    "Uống nhiều nước buổi tối"
                ],
                "mechanism": "Tiểu nhiều lần → Tỉnh giấc nhiều lần"
            },
            {
                "name": "Bệnh thần kinh",
                "examples": [
                    "Hội chứng chân không yên (RLS)",
                    "Rối loạn vận động chân tay khi ngủ (PLMD)"
                ]
            },
            {
                "name": "Hội chứng ngưng thở khi ngủ",
                "description": "Ngáy to, ngưng thở khi ngủ → Tỉnh giấc nhiều lần",
                "warning": "⚠️ Rất nguy hiểm, cần điều trị!"
            }
        ]
    },
    
    "medications": {
        "title": "💊 Thuốc Gây Mất Ngủ",
        "description": "Nhiều thuốc có thể gây mất ngủ:",
        "drugs": [
            {
                "name": "Thuốc huyết áp",
                "examples": ["Beta-blocker (Metoprolol)", "ACE-I (Enalapril)"],
                "mechanism": "Có thể gây rối loạn giấc ngủ"
            },
            {
                "name": "Corticoid",
                "examples": ["Prednisolone", "Methylprednisolone"],
                "mechanism": "Kích thích thần kinh → Mất ngủ",
                "note": "Đặc biệt nếu uống buổi tối"
            },
            {
                "name": "Thuốc chống trầm cảm",
                "examples": ["SSRI (Fluoxetine)", "SNRI"],
                "mechanism": "Kích thích thần kinh → Mất ngủ"
            },
            {
                "name": "Thuốc giảm đau",
                "examples": ["Codeine", "Morphine"],
                "mechanism": "Có thể gây mất ngủ"
            },
            {
                "name": "Cà phê, trà",
                "mechanism": "Caffeine kích thích → Khó ngủ",
                "when": "Đặc biệt nếu uống buổi tối (>14h)"
            }
        ]
    },
    
    "psychological": {
        "title": "🧠 Nguyên Nhân Tâm Lý",
        "causes": [
            {
                "name": "Trầm cảm",
                "description": "Trầm cảm → Mất ngủ (thức dậy sớm)",
                "note": "Ngược lại, mất ngủ cũng gây trầm cảm → Vòng luẩn quẩn"
            },
            {
                "name": "Lo âu",
                "description": "Lo lắng, suy nghĩ nhiều → Khó ngủ"
            },
            {
                "name": "Stress, căng thẳng",
                "description": "Công việc, gia đình → Khó ngủ"
            }
        ]
    },
    
    "lifestyle": {
        "title": "🏃 Thói Quen Xấu Gây Mất Ngủ",
        "habits": [
            {
                "name": "Giờ ngủ không đều",
                "description": "Ngủ muộn cuối tuần, dậy muộn → Rối loạn nhịp sinh học"
            },
            {
                "name": "Xem màn hình trước khi ngủ",
                "description": "Điện thoại, TV → Ánh sáng xanh ức chế melatonin"
            },
            {
                "name": "Phòng ngủ không tốt",
                "description": "Nóng, sáng, ồn → Khó ngủ"
            },
            {
                "name": "Ngủ trưa quá dài",
                "description": "Ngủ trưa >2 giờ → Khó ngủ đêm"
            },
            {
                "name": "Uống rượu bia",
                "description": "Rượu giúp ngủ nhanh nhưng làm giảm chất lượng giấc ngủ"
            }
        ]
    }
}

