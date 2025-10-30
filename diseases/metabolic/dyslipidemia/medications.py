"""
Medications - Thuốc điều trị rối loạn lipid máu
================================================

Thông tin về các loại thuốc giảm mỡ máu
"""

from typing import Dict, List

# STATINS - Nhóm thuốc chính
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

# FIBRATES - Hạ Triglyceride
FIBRATES = {
    "title": "💊 FIBRATES - Hạ Triglyceride",
    "description": "Nhóm thuốc đặc biệt tốt cho TRIGLYCERIDE cao",
    
    "how_it_works": {
        "mechanism": "Kích hoạt PPAR-alpha → Tăng phân giải triglyceride",
        "effects": [
            "↓ Triglyceride: 30-50% (MẠNH!)",
            "↑ HDL (mỡ tốt): 10-20%",
            "↓ LDL: 5-20% (ít hơn Statin)"
        ]
    },
    
    "common_fibrates": [
        {
            "name": "Fenofibrate (Lipanthyl, Fenotard)",
            "vietnamese_brands": ["Lipanthyl", "Fenotard", "Fenofibrate Stella"],
            "dosage": "145-160 mg/ngày, uống với bữa ăn",
            "cost": "80,000-200,000đ/tháng",
            "note": "Phổ biến nhất"
        },
        {
            "name": "Gemfibrozil",
            "vietnamese_brands": ["Gemfibrozil"],
            "dosage": "600 mg x 2 lần/ngày, trước ăn",
            "cost": "60,000-150,000đ/tháng",
            "note": "Cũ hơn, ít dùng"
        },
        {
            "name": "Bezafibrate",
            "vietnamese_brands": ["Bezalip"],
            "dosage": "400 mg/ngày",
            "cost": "50,000-120,000đ/tháng"
        }
    ],
    
    "when_to_use": [
        "Triglyceride RẤT CAO (≥500 mg/dL hay 5.7 mmol/L) - nguy cơ viêm tụy",
        "Triglyceride cao + HDL thấp",
        "Kết hợp với Statin nếu cần (cẩn thận)"
    ],
    
    "side_effects": [
        "Rối loạn tiêu hóa",
        "Sỏi mật (tăng nguy cơ)",
        "Đau cơ (đặc biệt khi kết hợp Statin)",
        "Tổn thương thận nhẹ"
    ],
    
    "important_notes": [
        "⚠️ THẬN YẾU: Giảm liều hoặc không dùng",
        "⚠️ SỎI MẬT: Không nên dùng",
        "⚠️ Kết hợp Statin: Tăng nguy cơ tổn thương cơ",
        "📊 Kiểm tra chức năng gan, thận định kỳ"
    ]
}

# Các thuốc khác
OTHER_MEDICATIONS = {
    "ezetimibe": {
        "name": "Ezetimibe (Ezetrol, Zetia)",
        "vietnamese_brands": ["Ezetrol", "Ezetimibe"],
        "type": "Ức chế hấp thu cholesterol",
        "how_it_works": "Ngăn ruột hấp thu cholesterol từ thức ăn",
        "dosage": "10 mg/ngày",
        "effects": [
            "↓ LDL thêm 15-20% (khi kết hợp Statin)",
            "↓ LDL 18% (đơn độc)"
        ],
        "cost": "150,000-300,000đ/tháng",
        "when_to_use": [
            "LDL vẫn cao dù đã dùng Statin liều cao",
            "Kết hợp Statin để tăng hiệu quả",
            "Không dung nạp Statin liều cao"
        ],
        "side_effects": "Ít tác dụng phụ, an toàn",
        "note": "Thường KẾT HỢP Statin, ít khi dùng đơn độc"
    },
    
    "omega3": {
        "name": "Omega-3 (EPA/DHA)",
        "vietnamese_brands": ["Dầu cá Omega-3", "EPA-E"],
        "type": "Bổ sung dầu cá",
        "dosage": "2-4 gram EPA+DHA/ngày",
        "effects": [
            "↓ Triglyceride: 20-30% (liều cao)",
            "↑ HDL nhẹ",
            "Chống viêm, chống huyết khối"
        ],
        "cost": "100,000-400,000đ/tháng",
        "when_to_use": [
            "Triglyceride cao (>200 mg/dL hay 2.3 mmol/L)",
            "Bổ sung cho Statin/Fibrate"
        ],
        "note": "ĂN CÁ BÉO (cá thu, hồi) TỰ NHIÊN TỐT HƠN! Viên uống chỉ là bổ sung."
    },
    
    "pcsk9_inhibitors": {
        "name": "PCSK9 Inhibitors (Evolocumab, Alirocumab)",
        "type": "Thuốc tiêm sinh học (rất đắt)",
        "effects": [
            "↓ LDL: 50-60% (MẠNH!)"
        ],
        "cost": "20-50 TRIỆU đồng/tháng (CỰC ĐẮT!)",
        "when_to_use": [
            "LDL CỰC CAO (gia đình tăng cholesterol di truyền)",
            "Đã nhồi máu tim + LDL vẫn cao dù dùng Statin liều cao",
            "Không dung nạp Statin"
        ],
        "availability": "Rất ít tại VN, chỉ bệnh viện lớn",
        "note": "CHỈ cho trường hợp đặc biệt, rất nặng"
    }
}

# Phác đồ điều trị theo mức độ
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


def get_medication_info(medication_name: str) -> Dict:
    """Lấy thông tin chi tiết về thuốc"""
    # Implement search logic
    medication_name = medication_name.lower()
    
    # Search in Statins
    for statin in STATINS["common_statins"]:
        if medication_name in statin["name"].lower():
            return {
                "type": "Statin",
                "details": statin,
                "general_info": STATINS
            }
    
    # Search in Fibrates
    for fibrate in FIBRATES["common_fibrates"]:
        if medication_name in fibrate["name"].lower():
            return {
                "type": "Fibrate",
                "details": fibrate,
                "general_info": FIBRATES
            }
    
    # Search in others
    for key, med in OTHER_MEDICATIONS.items():
        if medication_name in med["name"].lower():
            return {
                "type": "Other",
                "details": med
            }
    
    return {"error": "Không tìm thấy thông tin thuốc"}


def get_side_effects(medication_type: str = "statin") -> List[str]:
    """Lấy danh sách tác dụng phụ"""
    if medication_type.lower() == "statin":
        return STATINS["side_effects"]
    elif medication_type.lower() == "fibrate":
        return FIBRATES["side_effects"]
    else:
        return ["Vui lòng chọn loại thuốc: statin hoặc fibrate"]


def get_treatment_recommendation(ldl: float, has_diabetes: bool = False, 
                                 has_cvd: bool = False, triglyceride: float = 0) -> Dict:
    """Đề xuất phác đồ điều trị dựa trên LDL và yếu tố nguy cơ
    
    Args:
        ldl: LDL cholesterol (mmol/L)
        has_diabetes: Có tiểu đường không
        has_cvd: Đã có bệnh tim mạch không (nhồi máu tim, đột quỵ)
        triglyceride: Triglyceride (mmol/L)
    """
    
    # Nguy cơ rất cao
    if has_cvd:
        return TREATMENT_PROTOCOLS["very_high_risk"]
    
    # LDL rất cao
    if ldl >= 4.9:
        return TREATMENT_PROTOCOLS["high"]
    
    # Triglyceride rất cao
    if triglyceride >= 5.7:
        return TREATMENT_PROTOCOLS["high_triglycerides"]
    
    # LDL cao + tiểu đường
    if ldl >= 2.6 and has_diabetes:
        return TREATMENT_PROTOCOLS["moderate"]
    
    # LDL trung bình
    if 3.4 <= ldl < 4.9:
        return TREATMENT_PROTOCOLS["moderate"]
    
    # LDL nhẹ
    if 2.6 <= ldl < 3.4:
        return TREATMENT_PROTOCOLS["mild"]
    
    return {
        "level": "Bình thường",
        "treatment": ["✅ Duy trì lối sống lành mạnh", "📊 Xét nghiệm lại sau 1 năm"]
    }

