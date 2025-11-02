"""
Suy Thận Mạn - Điều trị
Treatment of Chronic Kidney Disease
"""

from typing import Dict, List

TREATMENT = {
    "goal": {
        "title": "🎯 Mục Tiêu Điều Trị",
        "description": "Điều trị KHÔNG chữa khỏi, nhưng:",
        "objectives": [
            "Làm chậm tiến triển → Tránh đến giai đoạn chạy thận",
            "Giảm triệu chứng → Cải thiện chất lượng sống",
            "Phòng ngừa biến chứng → Thiếu máu, loãng xương, bệnh tim",
            "Chuẩn bị tâm lý cho chạy thận (nếu đến giai đoạn cuối)"
        ],
        "key": "💡 Quan trọng nhất: Kiểm soát NGUYÊN NHÂN (tiểu đường, huyết áp)!"
    },
    
    "medications": {
        "title": "💊 Thuốc Điều Trị",
        "description": "Các thuốc quan trọng:",
        "drugs": [
            {
                "name": "Thuốc Kiểm Soát Nguyên Nhân",
                "description": "QUAN TRỌNG NHẤT - Kiểm soát tiểu đường, huyết áp",
                "drugs": [
                    {
                        "name": "Thuốc huyết áp: ACE-I hoặc ARB",
                        "examples": ["Enalapril", "Losartan", "Valsartan"],
                        "benefit": "Vừa hạ huyết áp, vừa BẢO VỆ thận → Làm chậm tiến triển",
                        "warning": "⚠️ Thuốc này ĐẶC BIỆT quan trọng với người suy thận!"
                    },
                    {
                        "name": "Thuốc tiểu đường",
                        "examples": ["Metformin (nếu eGFR >30)", "Insulin"],
                        "target": "HbA1c <7%, đường huyết ổn định",
                        "benefit": "Kiểm soát tốt → Giảm tổn thương thận 50%"
                    }
                ]
            },
            {
                "name": "Thuốc Giảm Protein Niệu",
                "description": "Giảm protein trong nước tiểu → Bảo vệ thận",
                "drugs": [
                    {
                        "name": "ACE-I hoặc ARB",
                        "benefit": "Giảm protein niệu 30-50%",
                        "target": "<1g protein/24h (nếu có thể)"
                    }
                ]
            },
            {
                "name": "Thuốc Bổ Sung",
                "description": "Bù thiếu hụt do thận không sản xuất được:",
                "drugs": [
                    {
                        "name": "Erythropoietin (EPO)",
                        "description": "Hormone tạo máu",
                        "when": "Khi thiếu máu (Hb <10 g/dL)",
                        "benefit": "Tăng hemoglobin → Giảm mệt mỏi",
                        "side_effects": "Có thể tăng huyết áp"
                    },
                    {
                        "name": "Sắt",
                        "description": "Bổ sung sắt (thường thiếu ở suy thận)",
                        "forms": ["Viên uống", "Tiêm tĩnh mạch (nếu uống không hấp thu)"]
                    },
                    {
                        "name": "Vitamin D",
                        "description": "Thận không chuyển vitamin D → Loãng xương",
                        "forms": ["Calcitriol (vitamin D dạng hoạt động)"],
                        "benefit": "Giảm loãng xương, chuột rút"
                    }
                ]
            },
            {
                "name": "Thuốc Điều Chỉnh Điện Giải",
                "description": "Điều chỉnh canxi, phốt pho, kali:",
                "drugs": [
                    {
                        "name": "Chất gắn phốt pho",
                        "examples": ["Calcium carbonate", "Sevelamer"],
                        "when": "Khi phốt pho cao → Ngứa da, loãng xương",
                        "how": "Uống trong bữa ăn → Gắn phốt pho trong thức ăn"
                    },
                    {
                        "name": "Bổ sung canxi",
                        "when": "Khi canxi thấp",
                        "forms": ["Calcium carbonate", "Calcium citrate"]
                    }
                ]
            }
        ]
    },
    
    "avoid_medications": {
        "title": "❌ Thuốc Cần Tránh",
        "description": "Những thuốc TỔN THƯƠNG thận:",
        "drugs": [
            {
                "name": "NSAIDs (Thuốc giảm đau)",
                "examples": ["Ibuprofen", "Naproxen", "Diclofenac"],
                "why": "Gây tổn thương thận, làm suy thận nặng hơn",
                "alternative": "Dùng Paracetamol (an toàn hơn)",
                "warning": "⚠️ TUYỆT ĐỐI KHÔNG dùng lâu dài nếu suy thận!"
            },
            {
                "name": "Thuốc cản quang (chụp CT có tiêm thuốc)",
                "why": "Có thể gây suy thận cấp",
                "action": "Phải uống đủ nước trước/sau, hoặc tránh nếu suy thận nặng"
            },
            {
                "name": "Một số kháng sinh",
                "examples": ["Aminoglycosides", "Vancomycin (liều cao)"],
                "why": "Tổn thương thận",
                "action": "Phải điều chỉnh liều theo chức năng thận"
            },
            {
                "name": "Metformin (nếu suy thận nặng)",
                "when": "eGFR <30 mL/phút",
                "why": "Nguy cơ nhiễm toan lactic",
                "action": "Phải ngừng, chuyển sang thuốc khác"
            }
        ]
    },
    
    "monitoring": {
        "title": "📊 Theo Dõi",
        "description": "Khám định kỳ để theo dõi tiến triển:",
        "frequency": {
            "stage_1_2": "Mỗi 6-12 tháng",
            "stage_3": "Mỗi 3-6 tháng",
            "stage_4": "Mỗi 1-3 tháng",
            "stage_5": "Mỗi 1 tháng (chuẩn bị chạy thận)"
        },
        "tests": [
            {
                "name": "Xét nghiệm máu",
                "items": [
                    "Creatinine, Ure",
                    "eGFR (độ lọc cầu thận)",
                    "Hemoglobin (thiếu máu)",
                    "Canxi, phốt pho, kali",
                    "PTH (hormone cận giáp)"
                ]
            },
            {
                "name": "Xét nghiệm nước tiểu",
                "items": [
                    "Protein niệu (protein trong nước tiểu)",
                    "Tỷ số Protein/Creatinine",
                    "Tế bào, vi khuẩn (nhiễm trùng)"
                ]
            },
            {
                "name": "Siêu âm thận",
                "frequency": "Mỗi 1-2 năm",
                "purpose": "Đánh giá kích thước thận, sỏi, tắc nghẽn"
            }
        ]
    },
    
    "slowing_progression": {
        "title": "🛡️ Làm Chậm Tiến Triển",
        "description": "Các biện pháp LÀM CHẬM suy thận tiến triển:",
        "methods": [
            {
                "name": "Kiểm soát huyết áp tốt",
                "target": "<130/80 mmHg (tốt nhất <120/80)",
                "benefit": "Làm chậm tiến triển 30-40%"
            },
            {
                "name": "Kiểm soát đường huyết tốt",
                "target": "HbA1c <7%",
                "benefit": "Làm chậm tiến triển 40-50%"
            },
            {
                "name": "Giảm protein niệu",
                "target": "<1g/24h (nếu có thể)",
                "method": "Dùng ACE-I hoặc ARB",
                "benefit": "Làm chậm tiến triển 20-30%"
            },
            {
                "name": "Chế độ ăn hợp lý",
                "details": "Ăn ít muối, ít đạm (theo giai đoạn)",
                "benefit": "Giảm gánh nặng cho thận"
            },
            {
                "name": "Uống đủ nước",
                "amount": "1.5-2L/ngày (nếu không hạn chế)",
                "benefit": "Giúp thận lọc tốt"
            },
            {
                "name": "Tránh thuốc độc thận",
                "drugs": "NSAIDs, thuốc cản quang",
                "benefit": "Không làm tổn thương thêm"
            }
        ]
    }
}

