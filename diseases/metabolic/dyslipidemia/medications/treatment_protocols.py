"""
Treatment Protocols - Phác đồ điều trị mỡ máu theo mức độ
"""

TREATMENT_PROTOCOLS = {
    "mild": {
        "level": "Nhẹ: LDL 2.6-3.3 mmol/L (100-130 mg/dL)",
        "first_line": [
            "🍽️ Ăn kiêng 3-6 tháng (ưu tiên)",
            "🏃 Tập thể dục thường xuyên",
            "🚭 Bỏ thuốc lá",
            "⚖️ Giảm cân nếu thừa cân"
        ],
        "if_not_enough": "Nếu sau 6 tháng chưa đạt mục tiêu → Cân nhắc Statin liều thấp"
    },
    
    "moderate": {
        "level": "Trung bình: LDL 3.4-4.8 mmol/L (130-190 mg/dL)",
        "treatment": [
            "💊 Statin liều trung bình (Atorvastatin 10-20mg hoặc Rosuvastatin 5-10mg)",
            "🍽️ Ăn kiêng nghiêm ngặt",
            "🏃 Tập thể dục ≥30 phút, 5 ngày/tuần"
        ],
        "target": "LDL < 2.6 mmol/L (100 mg/dL)"
    },
    
    "high": {
        "level": "Cao: LDL ≥ 4.9 mmol/L (190 mg/dL)",
        "treatment": [
            "💊 Statin liều cao (Atorvastatin 40-80mg hoặc Rosuvastatin 20-40mg) - BẮT BUỘC",
            "💊 Nếu chưa đủ → Thêm Ezetimibe",
            "🍽️ Ăn kiêng NGHIÊM NGẶT",
            "🏃 Tập thể dục đều đặn"
        ],
        "target": "LDL < 2.6 mmol/L (100 mg/dL), tốt hơn < 1.8 mmol/L"
    },
    
    "very_high_risk": {
        "level": "Nguy cơ RẤT CAO (đã nhồi máu tim, đột quỵ, tiểu đường)",
        "treatment": [
            "💊 Statin LIỀU CAO - BẮT BUỘC suốt đời",
            "💊 Thêm Ezetimibe nếu LDL vẫn cao",
            "💊 PCSK9 inhibitor nếu cần thiết (hiếm)",
            "🎯 MỤC TIÊU: LDL < 1.4 mmol/L (55 mg/dL)"
        ],
        "note": "Người này đã bị biến cố tim mạch → PHẢI điều trị tích cực!"
    },
    
    "high_triglycerides": {
        "level": "Triglyceride cao ≥ 2.3 mmol/L (200 mg/dL)",
        "treatment": [
            "🚫 CẮT GIẢM đường, rượu, tinh bột tinh chế",
            "⚖️ GIẢM CÂN",
            "🐟 TĂNG Omega-3 (ăn cá béo)",
            "💊 Nếu TG ≥ 5.7 mmol/L (500 mg/dL) → Fibrate hoặc Omega-3 liều cao"
        ],
        "note": "TG rất cao → Nguy cơ VIÊM TỤY cấp!"
    }
}

