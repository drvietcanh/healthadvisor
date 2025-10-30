"""
COPD - Phòng ngừa và so sánh
Prevention and comparison information
"""

# Phòng ngừa
PREVENTION = {
    "primary": {
        "name": "Phòng Ngừa Sơ Cấp (Chưa Bệnh)",
        "actions": [
            "🚫 KHÔNG HÚT THUỐC LÁ - Quan trọng nhất!",
            "🚫 Tránh khói thuốc thụ động",
            "😷 Đeo khẩu trang khi ô nhiễm cao",
            "🏠 Thông gió tốt khi nấu ăn (dùng quạt hút mùi)",
            "👷 Bảo hộ lao động (nếu tiếp xúc bụi, hóa chất)",
            "💉 Tiêm vắc-xin cúm, phế cầu (người >65 tuổi)"
        ]
    },
    
    "secondary": {
        "name": "Phòng Ngừa Thứ Cấp (Đã Bệnh → Ngăn Nặng)",
        "actions": [
            "✅ BỎ THUỐC LÁ ngay lập tức",
            "💊 Uống thuốc đều đặn",
            "🏃 Tập phục hồi chức năng phổi",
            "💉 Tiêm vắc-xin đầy đủ",
            "🏥 Tái khám định kỳ",
            "⚠️ Nhận biết sớm đợt cấp"
        ]
    }
}

# Phân biệt COPD vs Hen Suyễn
COPD_VS_ASTHMA = {
    "title": "🔍 PHÂN BIỆT COPD VÀ HEN SUYỄN - Dễ Nhầm Lẫn!",
    "introduction": """
Cả 2 bệnh đều khó thở, thở khò khè → Rất dễ nhầm!
NHƯNG: Khác nhau về nguyên nhân, tuổi mắc, điều trị, tiên lượng
    """,
    
    "comparison_table": {
        "age_onset": {
            "feature": "Tuổi khởi phát",
            "copd": "🧓 >40 tuổi (thường >50 tuổi)",
            "asthma": "👶 Thường <20 tuổi (trẻ em, thanh thiếu niên)",
            "key_point": "Hen = bệnh TRẺ, COPD = bệnh GIÀ"
        },
        
        "cause": {
            "feature": "Nguyên nhân",
            "copd": "🚬 Hút thuốc lá (85-90%)",
            "asthma": "🤧 Dị ứng (phấn hoa, bụi, lông thú...)",
            "key_point": "COPD do THUỐC LÁ, Hen do DỊ ỨNG"
        },
        
        "symptom_pattern": {
            "feature": "Triệu chứng",
            "copd": "⏱️ Tiến triển CHẬM, MÃI MÃI có (hàng ngày)",
            "asthma": "⚡ ĐỢT KỊCH PHÁT (có lúc khỏe, có lúc khó thở)",
            "key_point": "COPD = Khó thở MÃI, Hen = Khó thở CƠN"
        },
        
        "time_of_symptoms": {
            "feature": "Thời gian nặng",
            "copd": "🌅 Buổi sáng thường nặng hơn (ho, đờm nhiều)",
            "asthma": "🌙 Ban đêm/sáng sớm thường nặng hơn",
            "key_point": "Cả 2 đều nặng buổi sáng, nhưng hen nặng cả đêm"
        },
        
        "triggers": {
            "feature": "Yếu tố kích thích",
            "copd": "Nhiễm trùng, ô nhiễm, thời tiết lạnh",
            "asthma": "Dị nguyên (phấn, lông, thuốc, thức ăn), gắng sức, khí lạnh, cảm xúc",
            "key_point": "Hen có NHIỀU yếu tố kích phát hơn"
        },
        
        "reversibility": {
            "feature": "Hồi phục",
            "copd": "❌ KHÔNG thể hồi phục hoàn toàn (tổn thương vĩnh viễn)",
            "asthma": "✅ CÓ THỂ hồi phục hoàn toàn (nếu điều trị tốt)",
            "key_point": "⭐ KHÁC BIỆT QUAN TRỌNG NHẤT!"
        },
        
        "bronchodilator_response": {
            "feature": "Đáp ứng thuốc giãn phế quản",
            "copd": "Cải thiện ÍT (<12% FEV1)",
            "asthma": "Cải thiện NHIỀU (≥12% FEV1)",
            "key_point": "Dùng xịt hen → Hen đỡ nhanh, COPD đỡ chậm"
        },
        
        "family_history": {
            "feature": "Tiền sử gia đình",
            "copd": "❌ Thường KHÔNG (trừ thiếu AAT hiếm)",
            "asthma": "✅ Thường CÓ (di truyền)",
            "key_point": "Bố mẹ hen → Con dễ hen, KHÔNG dễ COPD"
        },
        
        "allergy_history": {
            "feature": "Tiền sử dị ứng",
            "copd": "❌ Thường không",
            "asthma": "✅ Thường có (viêm mũi dị ứng, chàm...)",
            "key_point": "Hen thường đi kèm các bệnh dị ứng khác"
        },
        
        "sputum": {
            "feature": "Đờm",
            "copd": "💧 Nhiều đờm (trắng/vàng/xanh), hàng ngày",
            "asthma": "💧 Ít đờm (hoặc đờm nhầy trong)",
            "key_point": "COPD = Đờm nhiều, Hen = Đờm ít"
        },
        
        "smoking": {
            "feature": "Hút thuốc lá",
            "copd": "🚬 Hầu hết có tiền sử hút thuốc",
            "asthma": "🚭 Đa số KHÔNG hút thuốc",
            "key_point": "COPD gần như LUÔN có hút thuốc"
        },
        
        "prognosis": {
            "feature": "Tiên lượng",
            "copd": "⚠️ Tiến triển nặng dần, giảm tuổi thọ",
            "asthma": "✅ Kiểm soát tốt → Sống bình thường",
            "key_point": "Hen kiểm soát được, COPD chỉ làm chậm"
        }
    },
    
    "simple_comparison": {
        "title": "📊 So Sánh Đơn Giản",
        "copd_summary": {
            "icon": "🧓🚬",
            "profile": "Ông già hút thuốc 30 năm",
            "typical": [
                "65 tuổi, hút thuốc 30 năm",
                "Ho, đờm nhiều MỖI SÁNG",
                "Khó thở khi đi bộ, leo cầu thang",
                "Triệu chứng MÃI MÃI có, không biến mất",
                "Xịt thuốc → Đỡ một chút nhưng không hết",
                "Càng ngày càng nặng, không thể hồi phục"
            ]
        },
        
        "asthma_summary": {
            "icon": "👦🤧",
            "profile": "Cậu bé dị ứng",
            "typical": [
                "15 tuổi, không hút thuốc",
                "Có lúc KHỎE HOÀN TOÀN, có lúc khó thở",
                "Khó thở KHI: Gặp mèo, hít phấn hoa, chạy",
                "Ban đêm/sáng sớm thở khò khè",
                "Xịt thuốc hen → Đỡ NGAY",
                "Điều trị tốt → Có thể sống bình thường"
            ]
        }
    },
    
    "confusion_cases": {
        "title": "❓ Trường Hợp Dễ Nhầm",
        "cases": [
            {
                "scenario": "👴 Người già có HEN từ nhỏ + Hút thuốc",
                "answer": "→ Có thể CÓ CẢ HEN VÀ COPD (15-20% trường hợp)",
                "note": "Gọi là ACOS (Asthma-COPD Overlap Syndrome)"
            },
            {
                "scenario": "🧑 Người trẻ <40 tuổi khó thở, hút thuốc",
                "answer": "→ Có thể là HEN NẶNG hoặc COPD hiếm (thiếu AAT)",
                "note": "Cần làm xét nghiệm đặc biệt"
            },
            {
                "scenario": "👵 Bà già ho lâu, không hút thuốc",
                "answer": "→ Có thể là COPD do khói bếp, không chỉ thuốc lá!",
                "note": "Phụ nữ nấu bếp than/củi nhiều năm"
            }
        ]
    },
    
    "when_to_suspect": {
        "suspect_copd": {
            "title": "🤔 Nghĩ Đến COPD Khi:",
            "criteria": [
                "Tuổi >40",
                "Hút thuốc (hoặc hút thuốc lá trước đây)",
                "Ho, đờm MẠN TÍNH (>3 tháng)",
                "Khó thở TIẾN TRIỂN CHẬM (nhiều năm)",
                "Triệu chứng HÀNG NGÀY, không biến mất"
            ]
        },
        
        "suspect_asthma": {
            "title": "🤔 Nghĩ Đến HEN Khi:",
            "criteria": [
                "Tuổi trẻ (<40, đặc biệt trẻ em)",
                "Tiền sử dị ứng (mũi, da, thức ăn...)",
                "Khó thở KỊCH PHÁT, có lúc khỏe hẳn",
                "Thở khò khè, đặc biệt ban đêm",
                "Đáp ứng TỐT với thuốc xịt hen"
            ]
        }
    },
    
    "diagnostic_difference": {
        "title": "🔬 Chẩn Đoán Phân Biệt",
        "spirometry": {
            "test": "Đo chức năng hô hấp (Spirometry)",
            "copd": "FEV1/FVC <0.7, đáp ứng ÍT với giãn phế quản (<12%)",
            "asthma": "FEV1/FVC có thể <0.7, đáp ứng TỐT với giãn phế quản (≥12%)",
            "key": "⭐ Xét nghiệm QUYẾT ĐỊNH để phân biệt!"
        }
    },
    
    "treatment_difference": {
        "title": "💊 Điều Trị Khác Nhau",
        "copd": [
            "Mục tiêu: LÀM CHẬM tiến triển, giảm triệu chứng",
            "Thuốc chính: Giãn phế quản dài hạn",
            "Corticoid: Chỉ dùng khi nặng",
            "Quan trọng nhất: BỎ THUỐC LÁ + Phục hồi chức năng"
        ],
        "asthma": [
            "Mục tiêu: KIỂM SOÁT hoàn toàn, không triệu chứng",
            "Thuốc chính: Corticoid hít (ICS) hàng ngày",
            "Thuốc cấp cứu: Xịt giãn phế quản ngắn hạn",
            "Quan trọng nhất: TRÁNH DỊ NGUYÊN + Dùng thuốc đều"
        ]
    },
    
    "key_message": {
        "title": "🎯 Điểm Quan Trọng Nhất",
        "message": """
HEN vs COPD - Nhớ 3 điểm:

1️⃣ TUỔI: Hen = TRẺ, COPD = GIÀ
2️⃣ NGUYÊN NHÂN: Hen = DỊ ỨNG, COPD = THUỐC LÁ  
3️⃣ HỒI PHỤC: Hen = ĐƯỢC, COPD = KHÔNG

⚠️ Nếu không chắc → ĐI KHÁM, làm đo chức năng hô hấp!
        """
    }
}

# Liên quan đến bệnh khác
RELATED_DISEASES = {
    "common_comorbidities": [
        {
            "disease": "Bệnh Tim Mạch",
            "prevalence": "20-30% bệnh nhân COPD",
            "note": "Cùng nguyên nhân: Hút thuốc, viêm"
        },
        {
            "disease": "Cao Huyết Áp",
            "prevalence": "30-50%",
            "note": "Thiếu oxy mạn tính → tăng huyết áp phổi"
        },
        {
            "disease": "Tiểu Đường Type 2",
            "prevalence": "10-20%",
            "note": "Corticoid → tăng đường huyết"
        },
        {
            "disease": "Loãng Xương",
            "prevalence": "35-70%",
            "note": "Ít vận động + corticoid + thiếu oxy"
        },
        {
            "disease": "Ung Thư Phổi",
            "risk": "Tăng 2-5 lần",
            "note": "Cùng yếu tố nguy cơ: Hút thuốc"
        }
    ]
}

