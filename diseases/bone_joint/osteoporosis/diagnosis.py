"""
Osteoporosis Diagnosis - Chẩn Đoán Loãng Xương
"""

DIAGNOSIS = {
    "title": "📊 Chẩn Đoán Loãng Xương",
    
    "method": {
        "title": "Phương Pháp Chính:",
        "dxa_scan": {
            "name": "Đo Mật Độ Xương (DEXA Scan)",
            "description": "Xét nghiệm CHUẨN vàng, không đau",
            "what_is_it": "Dùng tia X mức độ thấp đo xương",
            "where": "Cột sống, cổ xương đùi",
            "duration": "10-15 phút",
            "price": "300,000-500,000đ/lần",
            "frequency": "1-2 năm/lần để theo dõi"
        }
    },
    
    "t_score": {
        "title": "Chỉ Số T-Score (Kết Quả):",
        "explanation": "So sánh mật độ xương với người trẻ 30 tuổi",
        "levels": [
            {
                "range": "T-score ≥ -1.0",
                "interpretation": "Bình thường",
                "description": "Xương chắc, không loãng"
            },
            {
                "range": "T-score -1.0 đến -2.5",
                "interpretation": "Giảm mật độ xương (Tiền loãng xương)",
                "description": "Xương yếu hơn bình thường, chưa loãng",
                "action": "Phòng ngừa ngay: Bổ sung canxi, vitamin D, vận động"
            },
            {
                "range": "T-score < -2.5",
                "interpretation": "LOÃNG XƯƠNG",
                "description": "Xương yếu, dễ gãy",
                "action": "Điều trị ngay: Thuốc + Canxi + Vitamin D"
            }
        ]
    },
    
    "other_tests": {
        "title": "Xét Nghiệm Khác:",
        "blood_tests": [
            "Canxi máu",
            "Vitamin D",
            "Phospho",
            "Hormone tuyến cận giáp",
            "Chức năng thận"
        ],
        "purpose": "Tìm nguyên nhân (nếu có bệnh khác)"
    },
    
    "who_should_test": {
        "title": "Ai Nên Đo Mật Độ Xương:",
        "criteria": [
            "Phụ nữ ≥65 tuổi",
            "Nam giới ≥70 tuổi",
            "Phụ nữ 50-64 tuổi có yếu tố nguy cơ",
            "Đã gãy xương sau 50 tuổi",
            "Dùng Corticosteroid >3 tháng",
            "Có bệnh gây loãng xương (cường giáp, suy thận...)"
        ]
    }
}

