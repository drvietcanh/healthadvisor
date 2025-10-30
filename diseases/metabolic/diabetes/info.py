"""
Thông tin cơ bản về Bệnh Tiểu Đường
Bao gồm: Định nghĩa, Phân loại, Chỉ số đường huyết, Triệu chứng
"""

# ============= TIỂU ĐƯỜNG LÀ GÌ? =============

DISEASE_INFO = {
    "name_vn": "Bệnh Tiểu Đường",
    "name_en": "Diabetes Mellitus",
    "simple_explanation_vn": """
🍬 TIỂU ĐƯỜNG LÀ GÌ?

Tiểu đường là bệnh đường huyết (đường trong máu) cao hơn bình thường.

Tưởng tượng đơn giản:
- Bạn ăn cơm, bánh → thành đường trong máu
- Đường cần vào tế bào để làm năng lượng
- Insulin (do tụy tiết ra) giống như "chìa khóa" mở cửa cho đường vào tế bào
- Tiểu đường = Không đủ chìa khóa HOẶC chìa khóa không vặn được
→ Đường tích trong máu, không vào tế bào được
""",
    "types_simple_vn": {
        "type1": {
            "name": "Típ 1 (Type 1)",
            "explanation": "Tụy không sản xuất được insulin (không có chìa khóa)",
            "who": "Thường gặp ở trẻ em, thanh thiếu niên",
            "treatment": "Phải tiêm insulin suốt đời"
        },
        "type2": {
            "name": "Típ 2 (Type 2)",
            "explanation": "Tụy vẫn tiết insulin nhưng cơ thể kháng insulin (chìa khóa không vặn)",
            "who": "Thường gặp ở người trên 40 tuổi, béo phì",
            "treatment": "Thay đổi lối sống + thuốc uống (có thể cần insulin sau này)"
        },
        "gestational": {
            "name": "Tiểu đường thai kỳ",
            "explanation": "Đường huyết cao trong khi mang thai",
            "who": "Phụ nữ mang thai",
            "treatment": "Thường khỏi sau sinh, nhưng tăng nguy cơ típ 2 sau này"
        }
    }
}

# ============= CHỈ SỐ ĐƯỜNG HUYẾT =============

BLOOD_SUGAR_LEVELS = {
    "units_note_vn": """
📊 ĐƠN VỊ ĐO ĐƯỜNG HUYẾT:

Có 2 đơn vị phổ biến:
- mmol/L (Việt Nam, Châu Âu)
- mg/dL (Mỹ, một số nước Á)

Quy đổi: 1 mmol/L = 18 mg/dL
Ví dụ: 5 mmol/L = 90 mg/dL
""",
    "normal_ranges": {
        "fasting": {
            "name_vn": "Đường huyết đói (8 giờ không ăn)",
            "normal_mmol": "< 5.6 mmol/L",
            "normal_mg": "< 100 mg/dL",
            "prediabetes_mmol": "5.6 - 6.9 mmol/L",
            "prediabetes_mg": "100 - 125 mg/dL",
            "diabetes_mmol": "≥ 7.0 mmol/L",
            "diabetes_mg": "≥ 126 mg/dL"
        },
        "random": {
            "name_vn": "Đường huyết bất kỳ (bất cứ lúc nào)",
            "normal_mmol": "< 7.8 mmol/L",
            "normal_mg": "< 140 mg/dL",
            "diabetes_mmol": "≥ 11.1 mmol/L",
            "diabetes_mg": "≥ 200 mg/dL (kèm triệu chứng)"
        },
        "after_meal": {
            "name_vn": "Đường huyết sau ăn (2 giờ sau ăn)",
            "normal_mmol": "< 7.8 mmol/L",
            "normal_mg": "< 140 mg/dL",
            "prediabetes_mmol": "7.8 - 11.0 mmol/L",
            "prediabetes_mg": "140 - 199 mg/dL",
            "diabetes_mmol": "≥ 11.1 mmol/L",
            "diabetes_mg": "≥ 200 mg/dL"
        },
        "hba1c": {
            "name_vn": "HbA1c (đường huyết trung bình 3 tháng)",
            "normal": "< 5.7%",
            "prediabetes": "5.7% - 6.4%",
            "diabetes": "≥ 6.5%",
            "target_vn": "Mục tiêu điều trị: < 7% (tốt nhất < 6.5%)"
        }
    },
    "target_for_diabetics": {
        "fasting_mmol": "4.4 - 7.2 mmol/L",
        "fasting_mg": "80 - 130 mg/dL",
        "after_meal_mmol": "< 10 mmol/L",
        "after_meal_mg": "< 180 mg/dL",
        "hba1c": "< 7% (tốt nhất < 6.5%)"
    }
}

# ============= TRIỆU CHỨNG =============

SYMPTOMS = {
    "common_vn": [
        "🚰 Khát nước nhiều (uống mãi vẫn khát)",
        "🚽 Tiểu nhiều (đặc biệt ban đêm)",
        "😋 Đói bất thường (ăn nhiều vẫn đói)",
        "📉 Giảm cân không rõ nguyên nhân (dù ăn nhiều)",
        "😴 Mệt mỏi, uể oải",
        "👀 Nhìn mờ",
        "🩹 Vết thương lâu lành",
        "🦠 Hay bị nhiễm trùng (nấm vùng kín, nhiễm da)"
    ],
    "type1_specific_vn": [
        "Triệu chứng xuất hiện ĐỘT NGỘT (vài tuần)",
        "Buồn nôn, nôn",
        "Đau bụng",
        "Hơi thở có mùi trái cây lạ (dấu hiệu nguy hiểm)"
    ],
    "type2_specific_vn": [
        "Triệu chứng xuất hiện TỪTỪ (vài tháng đến vài năm)",
        "Có thể KHÔNG có triệu chứng (phát hiện qua xét nghiệm định kỳ)",
        "Da sẫm màu ở nếp gấp (cổ, nách)"
    ],
    "emergency_vn": {
        "title": "🚨 DẤU HIỆU NGUY HIỂM - GỌI CẤP CỨU 115 NGAY:",
        "signs": [
            "⛔ Đường huyết RẤT CAO (> 16.7 mmol/L / > 300 mg/dL)",
            "⛔ Hơi thở có mùi trái cây lạ (dấu hiệu nhiễm toan)",
            "⛔ Thở nhanh, thở gấp",
            "⛔ Buồn nôn, nôn nhiều",
            "⛔ Đau bụng",
            "⛔ Lơ mơ, ngất",
            "",
            "⛔ Đường huyết RẤT THẤP (< 3.3 mmol/L / < 60 mg/dL):",
            "   - Vã mồ hôi lạnh",
            "   - Run rẩy",
            "   - Chóng mặt, lảo đảo",
            "   - Lú lẫn",
            "   - Co giật"
        ]
    }
}

# ============= YẾU TỐ NGUY CƠ =============

RISK_FACTORS = {
    "type1_vn": [
        "Tiền sử gia đình (anh chị em, bố mẹ bị típ 1)",
        "Một số bệnh tự miễn",
        "Yếu tố di truyền"
    ],
    "type2_vn": [
        "⚠️ Béo phì (BMI ≥ 25)",
        "⚠️ Ít vận động",
        "⚠️ Tiền sử gia đình (bố mẹ, anh chị em bị típ 2)",
        "⚠️ Tuổi ≥ 45",
        "⚠️ Tiền sử tiểu đường thai kỳ",
        "⚠️ Tiền sử tiền tiểu đường",
        "⚠️ Huyết áp cao (≥140/90 mmHg)",
        "⚠️ Mỡ máu bất thường (HDL thấp, Triglyceride cao)",
        "⚠️ Hội chứng buồng trứng đa nang (PCOS)"
    ]
}

# ============= BIẾN CHỨNG NẾU KHÔNG ĐIỀU TRỊ =============

COMPLICATIONS = {
    "short_term_vn": {
        "hypoglycemia": {
            "name": "Hạ đường huyết (Đường < 3.9 mmol/L / 70 mg/dL)",
            "danger": "NGUY HIỂM - Có thể gây hôn mê, tử vong",
            "symptoms": "Run, vã mồ hôi, chóng mặt, lú lẫn, co giật"
        },
        "hyperglycemia": {
            "name": "Tăng đường huyết cấp (Đường > 16.7 mmol/L / 300 mg/dL)",
            "danger": "NGUY HIỂM - Có thể gây hôn mê",
            "symptoms": "Khát dữ dội, tiểu nhiều, buồn nôn, thở nhanh"
        }
    },
    "long_term_vn": [
        "💔 Bệnh tim mạch (nhồi máu cơ tim, đột quỵ) - Nguy cơ gấp 2-4 lần",
        "👁️ Bệnh mắt (võng mạc) - Có thể mù",
        "🦶 Tổn thương thần kinh chân → Loét chân → Cắt cụt",
        "🩺 Bệnh thận - Có thể suy thận cần lọc máu",
        "🦷 Bệnh nướu răng",
        "🧠 Sa sút trí tuệ",
        "🦴 Viêm khớp, loãng xương"
    ]
}

