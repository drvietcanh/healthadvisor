"""
Statins - Thuốc Statin điều trị cholesterol cao
"""

STATINS = {
    "title": "💊 STATINS - Thuốc Hạ Cholesterol (Nhóm Chính)",
    "description": "Statins là nhóm thuốc QUAN TRỌNG NHẤT giảm cholesterol, cứu sống hàng triệu người mỗi năm",
    
    "how_it_works": {
        "mechanism": "Ức chế enzyme HMG-CoA reductase → Gan sản xuất ít cholesterol hơn",
        "simple": "Ngăn gan tạo cholesterol → Giảm LDL trong máu",
        "effects": [
            "↓ LDL (mỡ xấu): 30-50%",
            "↓ Triglyceride: 10-20%",
            "↑ HDL (mỡ tốt): 5-10%",
            "Giảm nguy cơ đột quỵ, nhồi máu cơ tim 25-45%"
        ]
    },
    
    "common_statins": [
        {
            "name": "Atorvastatin (Lipitor, Sortis)",
            "vietnamese_brands": ["Sortis", "Atorvastatin Stella", "Lipitin"],
            "strength": "Mạnh",
            "dosage": "10-80 mg/ngày, uống tối",
            "ldl_reduction": "↓ LDL 30-50%",
            "cost": "50,000-200,000đ/tháng",
            "note": "Phổ biến nhất tại VN, hiệu quả cao"
        },
        {
            "name": "Rosuvastatin (Crestor)",
            "vietnamese_brands": ["Crestor", "Rosuvastatin Stella", "Rosuvas"],
            "strength": "Rất mạnh (mạnh nhất)",
            "dosage": "5-40 mg/ngày, uống tối",
            "ldl_reduction": "↓ LDL 45-55%",
            "cost": "100,000-300,000đ/tháng",
            "note": "Mạnh nhất, cho LDL rất cao"
        },
        {
            "name": "Simvastatin (Zocor)",
            "vietnamese_brands": ["Simvastatin", "Simvacor"],
            "strength": "Trung bình",
            "dosage": "10-40 mg/ngày, uống tối",
            "ldl_reduction": "↓ LDL 25-40%",
            "cost": "30,000-100,000đ/tháng",
            "note": "Rẻ nhất, phù hợp kinh tế"
        },
        {
            "name": "Pravastatin (Pravachol)",
            "vietnamese_brands": ["Pravastatin"],
            "strength": "Nhẹ-Trung bình",
            "dosage": "10-40 mg/ngày",
            "ldl_reduction": "↓ LDL 20-30%",
            "cost": "50,000-150,000đ/tháng",
            "note": "Ít tác dụng phụ, an toàn"
        },
        {
            "name": "Pitavastatin (Livalo)",
            "vietnamese_brands": ["Livalo", "Pitavastatin"],
            "strength": "Mạnh",
            "dosage": "1-4 mg/ngày",
            "ldl_reduction": "↓ LDL 30-45%",
            "cost": "100,000-250,000đ/tháng",
            "note": "Ít tương tác thuốc, tốt cho người dùng nhiều thuốc"
        }
    ],
    
    "side_effects": {
        "common": [
            "Đau cơ (5-10%) - thường nhẹ",
            "Mệt mỏi",
            "Đau đầu",
            "Rối loạn tiêu hóa"
        ],
        "serious": [
            "Tổn thương cơ nghiêm trọng (rhabdomyolysis) - HIẾM (<0.1%)",
            "Tổn thương gan - HIẾM (1-2%)",
            "Tiểu đường mới phát (tăng 10-20%) - nhưng lợi ích > tác hại"
        ],
        "warning_signs": [
            "🚨 Đau cơ NHIỀU, yếu cơ → BÁO BÁC SĨ NGAY",
            "Nước tiểu sẫm màu",
            "Vàng da, vàng mắt"
        ],
        "myth_busting": "🔍 THỰC TẾ: Statins rất AN TOÀN! Chỉ <5% người bỏ vì tác dụng phụ. Lợi ích CỨU SỐNG >> tác hại!"
    },
    
    "when_to_use": [
        "LDL ≥ 4.9 mmol/L (190 mg/dL) - BẮT BUỘC dùng",
        "LDL 2.6-4.9 mmol/L + tiểu đường",
        "LDL 2.6-4.9 mmol/L + cao huyết áp",
        "LDL 2.6-4.9 mmol/L + hút thuốc",
        "Đã bị nhồi máu cơ tim, đột quỵ - BẮT BUỘC dùng suốt đời",
        "Tuổi 40-75 + rủi ro tim mạch ≥7.5%"
    ],
    
    "important_notes": [
        "✅ Uống BUỔI TỐI (gan tạo cholesterol nhiều lúc đêm)",
        "✅ Uống HÀNG NGÀY, đều đặn",
        "✅ Kết hợp ĂN KIÊNG + TẬP THỂ DỤC",
        "⚠️ TRÁNH bưởi (grapefruit) - tăng nồng độ thuốc",
        "⚠️ KHÔNG TỰ Ý NGƯNG thuốc",
        "📊 Xét nghiệm gan sau 3 tháng đầu",
        "🤰 TUYỆT ĐỐI tránh thai khi dùng Statin"
    ]
}

