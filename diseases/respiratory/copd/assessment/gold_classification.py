"""
GOLD Classification - Phân Loại Độ Nặng COPD
"""

GOLD_CLASSIFICATION = {
    "name": "GOLD - Phân Loại Độ Nặng COPD",
    "full_name": "Global Initiative for Chronic Obstructive Lung Disease",
    
    "simple_explanation": """
💡 GOLD là gì?

Chia COPD thành 4 độ nặng dựa trên FEV1 (thể tích thở ra):
- GOLD 1: Nhẹ (≥80% bình thường)
- GOLD 2: Trung bình (50-79%)
- GOLD 3: Nặng (30-49%)
- GOLD 4: Rất nặng (<30%)

→ FEV1 càng THẤP = Phổi càng NẶNG
    """,
    
    "grades": [
        {
            "grade": "GOLD 1",
            "name": "Nhẹ",
            "fev1_percent": "≥80%",
            "description": "Chức năng phổi gần bình thường",
            "symptoms": "Có thể không có triệu chứng hoặc ho, đờm ít",
            "note": "Nhiều người chưa biết mình có COPD"
        },
        {
            "grade": "GOLD 2",
            "name": "Trung Bình",
            "fev1_percent": "50-79%",
            "description": "Chức năng phổi giảm vừa",
            "symptoms": "Khó thở khi gắng sức, ho đờm nhiều hơn",
            "note": "Thường bắt đầu đến khám ở giai đoạn này"
        },
        {
            "grade": "GOLD 3",
            "name": "Nặng",
            "fev1_percent": "30-49%",
            "description": "Chức năng phổi giảm nhiều",
            "symptoms": "Khó thở rõ, ảnh hưởng sinh hoạt, đợt cấp thường xuyên",
            "note": "Cần điều trị tích cực, theo dõi sát"
        },
        {
            "grade": "GOLD 4",
            "name": "Rất Nặng",
            "fev1_percent": "<30%",
            "description": "Suy phổi nghiêm trọng",
            "symptoms": "Khó thở nghỉ ngơi, suy tim phổi, cần thở oxy",
            "note": "Nguy cơ tử vong cao, chất lượng sống rất kém"
        }
    ],
    
    "abcd_assessment": {
        "name": "Phân Nhóm ABCD (GOLD 2017)",
        "description": "Kết hợp triệu chứng + đợt cấp để phân loại",
        
        "groups": {
            "A": {
                "name": "Nhóm A - Ít Triệu Chứng, Ít Đợt Cấp",
                "criteria": [
                    "mMRC 0-1 hoặc CAT <10",
                    "Đợt cấp 0-1 lần/năm (không nhập viện)"
                ],
                "risk": "Nguy cơ THẤP",
                "treatment": "Thuốc giãn phế quản khi cần"
            },
            "B": {
                "name": "Nhóm B - Nhiều Triệu Chứng, Ít Đợt Cấp",
                "criteria": [
                    "mMRC ≥2 hoặc CAT ≥10",
                    "Đợt cấp 0-1 lần/năm (không nhập viện)"
                ],
                "risk": "Triệu chứng ảnh hưởng cuộc sống",
                "treatment": "Thuốc giãn phế quản dài hạn"
            },
            "C": {
                "name": "Nhóm C - Ít Triệu Chứng, Nhiều Đợt Cấp",
                "criteria": [
                    "mMRC 0-1 hoặc CAT <10",
                    "Đợt cấp ≥2 lần/năm HOẶC ≥1 lần nhập viện"
                ],
                "risk": "Nguy cơ CAO",
                "treatment": "Điều trị tích cực để giảm đợt cấp"
            },
            "D": {
                "name": "Nhóm D - Nhiều Triệu Chứng, Nhiều Đợt Cấp",
                "criteria": [
                    "mMRC ≥2 hoặc CAT ≥10",
                    "Đợt cấp ≥2 lần/năm HOẶC ≥1 lần nhập viện"
                ],
                "risk": "Nguy cơ RẤT CAO",
                "treatment": "Điều trị tối đa, theo dõi sát"
            }
        }
    }
}

