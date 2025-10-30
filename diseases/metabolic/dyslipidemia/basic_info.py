"""
Thông tin cơ bản về Rối loạn Lipid Máu
Basic information about Dyslipidemia
"""

DYSLIPIDEMIA_INFO = {
    "name": "Rối loạn Lipid Máu",
    "name_en": "Dyslipidemia",
    
    "what_is_it": """
💡 **Rối loạn Lipid Máu là gì?**

Là tình trạng **MỠ TRONG MÁU** (cholesterol, triglyceride) cao hoặc thấp bất thường.

Bao gồm:
- **LDL (mỡ xấu)** quá CAO → Bám vào mạch máu → Tắc nghẽn
- **HDL (mỡ tốt)** quá THẤP → Không dọn sạch mỡ
- **Triglyceride** quá CAO → Tích mỡ trong máu

→ Nguy cơ: Nhồi máu tim, đột quỵ, viêm tụy
    """,
    
    "why_dangerous": """
⚠️ **Tại sao nguy hiểm?**

Rối loạn lipid máu là **"SÁT THỦ IM LẶNG"**:
- KHÔNG có triệu chứng ban đầu
- Âm thầm GÂY TẮC mạch máu
- Khi có triệu chứng = ĐÃ MUỘN (nhồi máu, đột quỵ)

📊 **Tại Việt Nam:**
- 30-40% người trưởng thành có rối loạn lipid máu
- 70% bệnh nhân tim mạch có lipid máu cao
- Chỉ 20% biết mình bị bệnh!
    """,
    
    "lipid_types": {
        "total_cholesterol": {
            "name": "Cholesterol Toàn Phần (TC)",
            "abbreviation": "TC",
            "simple_explanation": "Tổng tất cả cholesterol trong máu (tốt + xấu)"
        },
        "ldl": {
            "name": "LDL - Mỡ XẤU",
            "abbreviation": "LDL-C",
            "simple_explanation": "Xe tải chở mỡ ĐẾN mạch máu → Gây tắc nghẽn"
        },
        "hdl": {
            "name": "HDL - Mỡ TỐT",
            "abbreviation": "HDL-C",
            "simple_explanation": "Xe quét dọn mỡ KHỎI mạch máu → Bảo vệ tim"
        },
        "triglyceride": {
            "name": "Triglyceride (TG)",
            "abbreviation": "TG",
            "simple_explanation": "Mỡ dự trữ từ đường, rượu ăn vào"
        }
    },
    
    "definition": """
Rối loạn lipid máu là tình trạng một hoặc nhiều thành phần mỡ trong máu 
(cholesterol toàn phần, LDL-C, HDL-C, triglyceride) cao hoặc thấp bất thường.
    """,
    
    "simple_explanation": {
        "title": "💡 Giải thích đơn giản: Mỡ Xấu vs Mỡ Tốt",
        "analogy": """
Tưởng tượng mạch máu như con đường:

🚚 LDL (Mỡ XẤU) = Xe tải chở rác:
- Chở cholesterol ĐẾN thành mạch máu
- Đổ rác (mỡ) xuống đường → tắc nghẽn
- Càng nhiều xe tải → càng nhiều rác → đường càng hẹp
- → Nguy cơ tắc nghẽn (nhồi máu, đột quỵ)

🧹 HDL (Mỡ TỐT) = Xe quét rác:
- Hút mỡ TỪ thành mạch máu
- Chở về gan để xử lý, thải ra ngoài
- Càng nhiều xe quét → đường càng sạch
- → Bảo vệ tim mạch

🎯 MỤC TIÊU:
- GIẢM xe tải rác (LDL) ↓
- TĂNG xe quét rác (HDL) ↑
        """,
        
        "ldl_bad": {
            "name": "LDL - Mỡ XẤU (Low-Density Lipoprotein)",
            "why_bad": [
                "Dễ BÁM vào thành mạch máu",
                "Tạo MẢNG XƠ VỮA (giống cặn bẩn)",
                "Làm mạch máu HẸP dần",
                "Mảng vỡ → TẮC mạch → NHỒI MÁU"
            ],
            "example": """
Ví dụ: Ống nước bị cặn bẩn bám
- Ban đầu: Nước chảy tốt
- Lâu ngày: Cặn bám → ống hẹp → nước chảy yếu
- Cuối cùng: Cặn nhiều quá → TẮC → không chảy được
            """,
            "goal": "LDL càng THẤP càng TỐT (mục tiêu <100 mg/dL)"
        },
        
        "hdl_good": {
            "name": "HDL - Mỡ TỐT (High-Density Lipoprotein)",
            "why_good": [
                "HÚT mỡ RA khỏi thành mạch máu",
                "Chở về gan để phá hủy",
                "LÀM SẠCH mạch máu",
                "NGĂN CHẶN xơ vữa động mạch"
            ],
            "example": """
Ví dụ: Đội vệ sinh làm sạch đường
- Hút rác (mỡ) trên đường (mạch máu)
- Chở về bãi rác (gan) để xử lý
- Đường sạch → xe chạy tốt → tim khỏe
            """,
            "goal": "HDL càng CAO càng TỐT (mục tiêu ≥60 mg/dL)"
        },
        
        "triglyceride": {
            "name": "Triglyceride - Mỡ Dự trữ",
            "simple": """
Triglyceride = Mỡ THỪA từ ăn uống

- Ăn nhiều đường, tinh bột, rượu
- → Cơ thể chuyển thành mỡ để dự trữ
- → Triglyceride tăng trong máu
- → Tích tụ ở gan, mạch máu

Giống như: Ăn nhiều quá → mỡ bụng
            """,
            "danger": [
                "TG >150: Tăng nguy cơ tim mạch",
                "TG >500: Nguy cơ VIÊM TỤY - cấp cứu!"
            ],
            "solution": [
                "Giảm đường, tinh bột",
                "Bỏ rượu bia",
                "Tập thể dục",
                "Giảm cân"
            ]
        }
    },
    
    "statistics_vietnam": {
        "prevalence": "~30% dân số >40 tuổi",
        "stroke_patients": "68.6% bệnh nhân đột quỵ có rối loạn lipid",
        "awareness": "Chỉ 20% biết mình có bệnh",
        "treatment": "< 10% được điều trị đúng cách"
    },
    
    "key_points": [
        "Rối loạn lipid là thành phần của Hội chứng Chuyển hóa",
        "Nguyên nhân chính gây xơ vữa động mạch",
        "Tăng nguy cơ nhồi máu cơ tim, đột quỵ",
        "65% liên quan với béo phì",
        "Có thể kiểm soát bằng chế độ ăn + thuốc"
    ]
}

# Mục tiêu lipid máu theo hướng dẫn của Hội Tim Mạch Việt Nam & ESC/EAS
LIPID_TARGETS = {
    "cholesterol_total": {
        "name": "Cholesterol toàn phần",
        "unit": "mg/dL",
        "optimal": "<200",
        "borderline": "200-239",
        "high": "≥240",
        "note": "Tổng của LDL + HDL + VLDL"
    },
    
    "ldl_cholesterol": {
        "name": "LDL-C (Cholesterol xấu)",
        "unit": "mg/dL",
        "optimal": "<100",
        "near_optimal": "100-129",
        "borderline": "130-159",
        "high": "160-189",
        "very_high": "≥190",
        "targets": {
            "low_risk": "<116",
            "moderate_risk": "<100",
            "high_risk": "<70",
            "very_high_risk": "<55"
        },
        "note": "Mục tiêu khác nhau tùy nguy cơ tim mạch"
    },
    
    "hdl_cholesterol": {
        "name": "HDL-C (Cholesterol tốt)",
        "unit": "mg/dL",
        "low_male": "<40",
        "low_female": "<50",
        "optimal": "≥60",
        "note": "Cao hơn là tốt hơn - bảo vệ tim mạch"
    },
    
    "triglyceride": {
        "name": "Triglyceride (Mỡ máu)",
        "unit": "mg/dL",
        "optimal": "<150",
        "borderline": "150-199",
        "high": "200-499",
        "very_high": "≥500",
        "note": "Liên quan với tiểu đường, béo phì"
    },
    
    "non_hdl": {
        "name": "Non-HDL-C",
        "unit": "mg/dL",
        "formula": "TC - HDL-C",
        "optimal": "<130",
        "high": "≥160",
        "note": "Chỉ số tốt hơn LDL đơn thuần"
    },
    
    "tc_hdl_ratio": {
        "name": "Tỷ lệ TC/HDL-C",
        "optimal": "<3.5",
        "average": "3.5-5.0",
        "high_risk": ">5.0",
        "note": "Dự đoán nguy cơ tim mạch"
    }
}

