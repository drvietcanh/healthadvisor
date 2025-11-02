"""
Suy Thận Mạn - Nguyên nhân
Causes of Chronic Kidney Disease
"""

from typing import Dict, List

CAUSES = {
    "main_causes": {
        "title": "🔍 Nguyên Nhân Chính",
        "description": "2 nguyên nhân phổ biến nhất tại VN:",
        "causes": [
            {
                "name": "Tiểu Đường",
                "prevalence": "Nguyên nhân số 1 (40-50% ca suy thận)",
                "mechanism": "Đường huyết cao → Tổn thương mạch máu nhỏ trong thận → Suy thận",
                "simple": "Giống như đường làm hỏng ống dẫn nước",
                "progression": [
                    "Tiểu đường 5-10 năm → Bắt đầu có protein trong nước tiểu",
                    "Tiểu đường 10-15 năm → Suy thận nhẹ (giai đoạn 1-2)",
                    "Tiểu đường 15-20 năm → Suy thận nặng (giai đoạn 3-4)",
                    "Tiểu đường >20 năm → Suy thận giai đoạn cuối"
                ],
                "prevention": "Kiểm soát đường huyết tốt (HbA1c <7%) → Giảm nguy cơ 50%",
                "warning": "⚠️ Tiểu đường + Suy thận = Rất nguy hiểm, phải kiểm soát tốt!"
            },
            {
                "name": "Tăng Huyết Áp",
                "prevalence": "Nguyên nhân số 2 (25-30% ca suy thận)",
                "mechanism": "Huyết áp cao → Tổn thương mạch máu thận → Suy thận",
                "simple": "Giống như nước áp lực cao làm hỏng bộ lọc",
                "progression": [
                    "Tăng huyết áp >5 năm → Tổn thương thận nhẹ",
                    "Tăng huyết áp >10 năm → Suy thận trung bình",
                    "Tăng huyết áp >15 năm → Suy thận nặng"
                ],
                "prevention": "Kiểm soát huyết áp <140/90 mmHg → Giảm nguy cơ 40%",
                "target": "Mục tiêu tốt nhất: <130/80 mmHg (nếu có tiểu đường)"
            },
            {
                "name": "Viêm Cầu Thận",
                "prevalence": "10-15% ca",
                "description": "Viêm cầu thận (đơn vị lọc của thận) → Tổn thương thận",
                "causes": [
                    "Nhiễm trùng (viêm họng, da) → Viêm cầu thận sau nhiễm",
                    "Bệnh tự miễn (Lupus, viêm khớp dạng thấp)",
                    "Bệnh di truyền (hội chứng Alport)"
                ],
                "warning": "⚠️ Viêm cầu thận → Suy thận nhanh, cần điều trị tích cực"
            },
            {
                "name": "Bệnh Thận Đa Nang",
                "prevalence": "5-10% ca",
                "description": "Bệnh di truyền, nhiều nang trong thận → Phá hủy thận",
                "inheritance": "Di truyền trội (50% con cái bị nếu bố/mẹ bị)",
                "progression": "Tiến triển chậm, thường đến suy thận ở 40-60 tuổi"
            },
            {
                "name": "Sỏi Thận Tái Phát",
                "prevalence": "5% ca",
                "description": "Sỏi thận nhiều lần → Tổn thương thận",
                "prevention": "Uống nhiều nước, điều trị sỏi sớm"
            }
        ]
    },
    
    "risk_factors": {
        "title": "⚠️ Yếu Tố Nguy Cơ",
        "description": "Những người có nguy cơ cao:",
        "high_risk": [
            {
                "name": "Tiểu đường",
                "risk": "Tăng nguy cơ 2-4 lần",
                "action": "Kiểm soát đường huyết tốt, khám thận định kỳ"
            },
            {
                "name": "Tăng huyết áp",
                "risk": "Tăng nguy cơ 1.5-2 lần",
                "action": "Kiểm soát huyết áp <140/90 mmHg"
            },
            {
                "name": "Tuổi >60 tuổi",
                "risk": "Chức năng thận giảm tự nhiên theo tuổi",
                "action": "Khám thận định kỳ, kiểm soát bệnh mãn tính"
            },
            {
                "name": "Bệnh tim mạch",
                "risk": "Tim và thận liên quan chặt chẽ",
                "action": "Kiểm soát tốt bệnh tim"
            },
            {
                "name": "Béo phì",
                "risk": "Tăng nguy cơ 1.5 lần",
                "action": "Giảm cân, ăn uống lành mạnh"
            },
            {
                "name": "Hút thuốc lá",
                "risk": "Tăng nguy cơ 1.5-2 lần",
                "action": "BỎ THUỐC LÁ"
            },
            {
                "name": "Dùng thuốc giảm đau lâu dài",
                "risk": "Tổn thương thận (NSAIDs)",
                "action": "Tránh dùng lâu dài, theo chỉ định bác sĩ"
            },
            {
                "name": "Tiền sử gia đình",
                "risk": "Có người thân bị suy thận",
                "action": "Khám sàng lọc sớm"
            }
        ]
    },
    
    "prevention_factors": {
        "title": "✅ Cách Phòng Ngừa",
        "description": "Các biện pháp GIẢM nguy cơ suy thận:",
        "methods": [
            {
                "name": "Kiểm soát tiểu đường",
                "target": "HbA1c <7%, đường huyết ổn định",
                "benefit": "Giảm nguy cơ 50%"
            },
            {
                "name": "Kiểm soát huyết áp",
                "target": "<140/90 mmHg (tốt nhất <130/80 nếu có tiểu đường)",
                "benefit": "Giảm nguy cơ 40%"
            },
            {
                "name": "Uống đủ nước",
                "amount": "1.5-2L/ngày (nếu không hạn chế nước)",
                "benefit": "Giúp thận lọc tốt, giảm sỏi thận"
            },
            {
                "name": "Ăn ít muối",
                "target": "<5g muối/ngày (<1 thìa cà phê)",
                "benefit": "Giảm huyết áp, bảo vệ thận"
            },
            {
                "name": "Tránh thuốc giảm đau lâu dài",
                "warning": "NSAIDs (Ibuprofen, Naproxen) → Tổn thương thận",
                "action": "Chỉ dùng khi cần, không dùng lâu dài"
            },
            {
                "name": "Khám sàng lọc định kỳ",
                "tests": [
                    "Xét nghiệm máu: Creatinine, Ure",
                    "Xét nghiệm nước tiểu: Protein, máu",
                    "Siêu âm thận (nếu có yếu tố nguy cơ)"
                ],
                "frequency": "Mỗi năm 1 lần (nếu có yếu tố nguy cơ)"
            }
        ]
    }
}

