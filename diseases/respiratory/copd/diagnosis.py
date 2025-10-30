"""
COPD - Chẩn đoán và biến chứng
Diagnosis and complications of COPD
"""

# Biến chứng
COMPLICATIONS = {
    "respiratory": {
        "name": "Hô Hấp",
        "complications": [
            "Suy hô hấp mạn tính → phải thở oxy",
            "Nhiễm trùng phổi tái đi tái lại",
            "Viêm phổi nặng, áp xe phổi",
            "Tràn khí màng phổi (bóng khí vỡ)"
        ]
    },
    
    "cardiovascular": {
        "name": "Tim Mạch",
        "complications": [
            "Cor pulmonale (tim phổi): Tim phải phì đại, suy tim",
            "Tăng áp phổi",
            "Rối loạn nhịp tim",
            "Tăng nguy cơ nhồi máu cơ tim"
        ],
        "note": "COPD + bệnh tim = Rất nguy hiểm!"
    },
    
    "other": {
        "name": "Khác",
        "complications": [
            "Loãng xương (do corticoid, ít vận động)",
            "Trầm cảm, lo âu (40-70% bệnh nhân)",
            "Suy dinh dưỡng, sụt cân",
            "Yếu cơ",
            "Tăng nguy cơ ung thư phổi (hút thuốc)"
        ]
    }
}

# Chẩn đoán
DIAGNOSIS = {
    "spirometry": {
        "name": "🫁 Đo Chức Năng Hô Hấp (Spirometry) - XÉT NGHIỆM QUYẾT ĐỊNH",
        "description": "Đo lượng và tốc độ khí thở vào/ra",
        "criteria": "FEV1/FVC < 0.7 SAU khi dùng thuốc giãn phế quản",
        "interpretation": {
            "FEV1": "Thể tích khí thở ra mạnh trong 1 giây đầu",
            "FVC": "Tổng thể tích khí thở ra tối đa",
            "ratio": "FEV1/FVC < 0.7 → Tắc nghẽn"
        },
        "note": "⚠️ CẦN LÀM nếu: >40 tuổi + hút thuốc + ho/khó thở mạn tính"
    },
    
    "imaging": {
        "name": "📷 Chụp X-quang/CT Phổi",
        "findings": [
            "Phổi căng phồng quá mức",
            "Hoành cơ dẹt (bình thường là vòm)",
            "Phế nang bị phá hủy (khí phế thũng)",
            "Thành phế quản dày"
        ],
        "note": "Không dùng để chẩn đoán chính, nhưng loại trừ bệnh khác"
    },
    
    "other_tests": {
        "name": "Xét Nghiệm Khác",
        "tests": [
            "Khí máu động mạch: Đo mức oxy, CO2",
            "Đo SpO2: Nồng độ oxy máu (bình thường >95%)",
            "Xét nghiệm Alpha-1 Antitrypsin (nếu <45 tuổi)",
            "Công thức máu: Phát hiện nhiễm trùng",
            "ECG, siêu âm tim: Đánh giá tim phổi"
        ]
    }
}


