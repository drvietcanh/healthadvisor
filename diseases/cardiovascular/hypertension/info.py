"""
Hypertension Information
Disease info, BP classification, symptoms, and diagnostic steps
"""

# ============= THÔNG TIN BỆNH =============

DISEASE_INFO = {
    "name_vn": "Tăng Huyết Áp",
    "name_en": "Hypertension",
    "description_vn": """
Tăng huyết áp là tình trạng huyết áp trong động mạch cao hơn bình thường (≥140/90 mmHg).
Đây là yếu tố nguy cơ chính gây đột quỵ, nhồi máu cơ tim, suy tim và bệnh thận.
""",
    "description_en": """
Hypertension is a condition where blood pressure in arteries is higher than normal (≥140/90 mmHg).
It's a major risk factor for stroke, heart attack, heart failure, and kidney disease.
""",
    "prevalence_vn": "~25% dân số Việt Nam (khoảng 25 triệu người)",
    "risk_factors_vn": [
        "Tuổi cao (>50 tuổi)",
        "Tiền sử gia đình",
        "Béo phì (BMI ≥25)",
        "Ăn mặn (>5g muối/ngày)",
        "Ít vận động",
        "Căng thẳng, stress",
        "Hút thuốc, uống rượu",
        "Ngủ không đủ giấc"
    ]
}

# ============= PHÂN LOẠI HUYẾT ÁP =============

BP_CLASSIFICATION = {
    "normal": {
        "range": "< 120/80 mmHg",
        "name_vn": "Bình thường",
        "advice_vn": "Duy trì lối sống lành mạnh. Kiểm tra huyết áp mỗi năm."
    },
    "elevated": {
        "range": "120-129/<80 mmHg",
        "name_vn": "Huyết áp cao bình thường",
        "advice_vn": "Thay đổi lối sống ngay. Giảm muối, tăng vận động. Kiểm tra sau 3-6 tháng."
    },
    "stage1": {
        "range": "130-139/80-89 mmHg",
        "name_vn": "Tăng huyết áp giai đoạn 1",
        "advice_vn": "Thay đổi lối sống + có thể cần thuốc. Tái khám sau 1 tháng."
    },
    "stage2": {
        "range": "≥140/90 mmHg",
        "name_vn": "Tăng huyết áp giai đoạn 2",
        "advice_vn": "Cần dùng thuốc + thay đổi lối sống. Khám bác sĩ trong 1 tuần."
    },
    "crisis": {
        "range": "≥180/≥120 mmHg",
        "name_vn": "CƠN TĂNG HUYẾT ÁP - CẤP CỨU",
        "advice_vn": "🚨 GỌI 115 NGAY! Nguy cơ đột quỵ, nhồi máu tim cao!"
    }
}

# ============= TRIỆU CHỨNG =============

SYMPTOMS = {
    "common_vn": [
        "Hầu hết KHÔNG có triệu chứng (bệnh thầm lặng)",
        "Đau đầu (đặc biệt vùng gáy)",
        "Chóng mặt, hoa mắt",
        "Mệt mỏi",
        "Khó thở khi gắng sức",
        "Chảy máu cam",
        "Nhìn mờ"
    ],
    "emergency_vn": [
        "🚨 Đau đầu dữ dội đột ngột",
        "🚨 Đau ngực",
        "🚨 Khó thở nghiêm trọng",
        "🚨 Yếu liệt nửa người",
        "🚨 Nói khó, méo miệng",
        "🚨 Co giật"
    ]
}

# ============= CHẨN ĐOÁN =============

DIAGNOSTIC_STEPS = {
    "screening_vn": [
        "Đo huyết áp tại nhà (sáng và tối, 7 ngày liên tiếp)",
        "Đo huyết áp tại phòng khám (ít nhất 2 lần, cách nhau 1-2 tuần)",
        "Đo huyết áp 24 giờ (nếu cần)"
    ],
    "tests_vn": [
        "Điện tâm đồ (ECG)",
        "Xét nghiệm máu: Glucose, Creatinine, Lipid, Kali",
        "Xét nghiệm nước tiểu",
        "Siêu âm tim (nếu nghi ngờ tổn thương cơ tim)",
        "Siêu âm động mạch cảnh (nếu nghi ngờ xơ vữa)"
    ]
}

