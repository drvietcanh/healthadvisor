"""
Viêm phổi - Chẩn đoán
Diagnosis of Pneumonia
"""

from typing import Dict, List

DIAGNOSIS = {
    "clinical": {
        "title": "🔍 Chẩn đoán lâm sàng",
        "description": "Bác sĩ khám và hỏi triệu chứng:",
        "methods": [
            {
                "name": "Khám lâm sàng",
                "steps": [
                    "Nghe phổi: Rale ẩm, rale nổ (tiếng nổ bong bóng)",
                    "Gõ phổi: Đục (do đầy dịch)",
                    "Đo nhịp thở: >20 lần/phút (người lớn)",
                    "Đo SpO2: <95% (thiếu oxy)"
                ]
            },
            {
                "name": "Triệu chứng điển hình",
                "criteria": [
                    "Ho + Sốt + Khó thở",
                    "Đau ngực bên bị viêm",
                    "Mệt mỏi, không muốn ăn"
                ]
            }
        ]
    },
    
    "tests": {
        "title": "📋 Xét nghiệm chẩn đoán",
        "common": [
            {
                "name": "X-quang ngực",
                "description": "Tiêu chuẩn vàng - Thấy hình ảnh viêm phổi",
                "findings": [
                    "Mờ một vùng phổi (do đầy dịch)",
                    "Tổn thương 1 hoặc 2 bên",
                    "Có thể thấy áp xe phổi (hốc rỗng trong phổi)"
                ],
                "note": "⚠️ X-quang BÌNH THƯỜNG không loại trừ viêm phổi (sớm, nhẹ)"
            },
            {
                "name": "Xét nghiệm máu",
                "description": "Đánh giá mức độ nhiễm trùng",
                "tests": [
                    "Công thức máu: Bạch cầu tăng (nhiễm trùng)",
                    "CRP, Procalcitonin: Tăng cao (nhiễm trùng nặng)",
                    "Cấy máu: Tìm vi khuẩn trong máu (nhiễm trùng máu)"
                ]
            },
            {
                "name": "Xét nghiệm đờm",
                "description": "Tìm vi khuẩn gây bệnh",
                "tests": [
                    "Soi đờm: Thấy bạch cầu, vi khuẩn",
                    "Cấy đờm: Xác định loại vi khuẩn, kháng sinh nhạy cảm",
                    "Nhuộm Gram: Phân biệt vi khuẩn nhanh"
                ],
                "note": "Quan trọng để chọn kháng sinh đúng"
            },
            {
                "name": "Test nhanh",
                "description": "Test tại nhà/cơ sở y tế",
                "tests": [
                    "Test COVID-19: Nếu nghi ngờ COVID-19",
                    "Test cúm: Nếu nghi ngờ cúm",
                    "SpO2 (đo bằng máy kẹp ngón tay): <95% = Thiếu oxy"
                ]
            }
        ]
    },
    
    "severity_assessment": {
        "title": "📊 Đánh giá mức độ nặng",
        "description": "CURB-65 Score (người lớn) hoặc CRB-65:",
        "criteria": {
            "C": "Lú lẫn (Confusion) - Không tỉnh táo",
            "U": "Ure máu tăng (BUN >7 mmol/L) - Chức năng thận kém",
            "R": "Thở nhanh (RR ≥30/phút)",
            "B": "Huyết áp tụt (BP <90/60 mmHg)",
            "65": "Tuổi ≥65"
        },
        "scores": [
            {
                "score": "0-1 điểm",
                "severity": "Nhẹ",
                "treatment": "Điều trị tại nhà, uống kháng sinh",
                "mortality": "Tỷ lệ tử vong <2%"
            },
            {
                "score": "2 điểm",
                "severity": "Trung bình",
                "treatment": "Cân nhắc nhập viện",
                "mortality": "Tỷ lệ tử vong 6-9%"
            },
            {
                "score": "≥3 điểm",
                "severity": "NẶNG",
                "treatment": "NHẬP VIỆN NGAY, có thể vào ICU",
                "mortality": "Tỷ lệ tử vong 15-40%"
            }
        ],
        "note": "⚠️ Score ≥3 = Nguy hiểm tính mạng, cần cấp cứu!"
    },
    
    "differential_diagnosis": {
        "title": "🔍 Phân biệt với bệnh khác",
        "diseases": [
            {
                "name": "Cảm cúm thông thường",
                "difference": "Cúm: Sốt, đau cơ, mệt mỏi, ho khan (KHÔNG khó thở nặng)",
                "key": "Viêm phổi: Có khó thở, đau ngực, rale ẩm khi nghe phổi"
            },
            {
                "name": "Viêm phế quản",
                "difference": "Viêm phế quản: Ho có đờm, KHÔNG sốt cao, KHÔNG khó thở nặng",
                "key": "Viêm phổi: Sốt cao, khó thở, có tổn thương phổi trên X-quang"
            },
            {
                "name": "Ung thư phổi",
                "difference": "Ung thư: Ho ra máu, sụt cân, đau ngực dai dẳng",
                "key": "Viêm phổi: Sốt, nhiễm trùng, đáp ứng kháng sinh"
            },
            {
                "name": "Suy tim",
                "difference": "Suy tim: Khó thở khi nằm, phù chân, tiền sử bệnh tim",
                "key": "Viêm phổi: Sốt, nhiễm trùng, rale ẩm một bên"
            }
        ]
    }
}

COMPLICATIONS = {
    "respiratory": {
        "name": "Hô Hấp",
        "complications": [
            {
                "name": "Suy hô hấp",
                "description": "Phổi không trao đổi được oxy → Thiếu oxy nặng",
                "treatment": "Thở máy, thở oxy cao áp"
            },
            {
                "name": "Áp xe phổi",
                "description": "Ổ mủ trong phổi (thường do tụ cầu)",
                "treatment": "Dẫn lưu mủ, kháng sinh dài ngày"
            },
            {
                "name": "Tràn dịch màng phổi",
                "description": "Dịch tích tụ giữa phổi và thành ngực",
                "treatment": "Chọc hút dịch, kháng sinh"
            }
        ]
    },
    
    "systemic": {
        "name": "Toàn thân",
        "complications": [
            {
                "name": "Nhiễm trùng máu (Sepsis)",
                "description": "Vi khuẩn từ phổi vào máu → Nhiễm trùng toàn thân",
                "symptoms": "Sốc nhiễm khuẩn: Huyết áp tụt, mạch nhanh, lơ mơ",
                "mortality": "Tỷ lệ tử vong 30-50% nếu không điều trị kịp thời",
                "warning": "⚠️ RẤT NGUY HIỂM - TỬ VONG NHANH!"
            },
            {
                "name": "Suy đa cơ quan",
                "description": "Thiếu oxy → Tổn thương não, tim, thận",
                "organs": [
                    "Suy thận: Tiểu ít, urê máu tăng",
                    "Suy gan: Men gan tăng",
                    "Tổn thương não: Lơ mơ, co giật"
                ]
            }
        ]
    },
    
    "long_term": {
        "name": "Biến chứng lâu dài",
        "complications": [
            "Xơ phổi: Phổi tổn thương vĩnh viễn → Khó thở mạn tính",
            "Giảm chức năng phổi: Ho, khó thở kéo dài",
            "Tăng nguy cơ tái phát: Phổi yếu → Dễ viêm phổi lần sau"
        ]
    }
}

