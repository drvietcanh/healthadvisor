"""
Thông tin về Béo phì (Obesity)
==============================

Béo phì là bệnh mạn tính do mất cân bằng năng lượng,
khi lượng calories tiêu thụ vượt quá lượng đốt cháy.
"""

OBESITY_INFO = {
    "name": "Béo phì",
    "name_en": "Obesity",
    "definition": """
Béo phì là tình trạng tích tụ mỡ quá mức trong cơ thể, 
gây ảnh hưởng xấu đến sức khỏe. Được đánh giá chủ yếu 
qua chỉ số BMI (Body Mass Index - Chỉ số khối cơ thể).
    """,
    
    "statistics_vietnam": {
        "prevalence": "25% dân số VN (2014)",
        "growth_rate": "38% - Nhanh nhất Đông Nam Á",
        "children_5_19": "19% (tăng gấp đôi trong 10 năm)",
        "urban": "26.8% khu vực thành thị"
    },
    
    "key_points": [
        "Béo phì là GỐC RỄ của Hội chứng Chuyển hóa",
        "Tăng nguy cơ tiểu đường type 2 lên 80%",
        "Tăng nguy cơ cao huyết áp lên 70%",
        "Giảm 5-10% cân nặng cải thiện sức khỏe đáng kể",
        "Có thể phòng ngừa và kiểm soát được"
    ]
}

# Phân loại BMI theo chuẩn VIỆT NAM / CHÂU Á 
# Theo Bộ Y Tế VN và WHO Western Pacific Region (2000)
# KHÁC VỚI CHUẨN WHO TOÀN CẦU!
#
# So sánh:
# - Thừa cân: Châu Á ≥23, WHO ≥25
# - Béo phì: Châu Á ≥25, WHO ≥30
# 
# Lý do: Người Châu Á có % mỡ cơ thể cao hơn ở cùng BMI
# → Nguy cơ bệnh cao hơn ở BMI thấp hơn

BMI_CATEGORIES_ASIAN = {
    "underweight": {
        "range": (0, 18.5),
        "label": "Thiếu cân",
        "icon": "😟",
        "color": "#FFA726",
        "risk": "Thấp",
        "advice": "Tăng cân lành mạnh, ăn đủ dinh dưỡng"
    },
    "normal": {
        "range": (18.5, 23.0),
        "label": "Bình thường",
        "icon": "✅",
        "color": "#66BB6A",
        "risk": "Thấp nhất",
        "advice": "Duy trì cân nặng hiện tại"
    },
    "overweight": {
        "range": (23.0, 25.0),
        "label": "Thừa cân",
        "icon": "⚠️",
        "color": "#FFEB3B",
        "risk": "Trung bình",
        "advice": "Giảm 2-5kg để về mức bình thường"
    },
    "obese_1": {
        "range": (25.0, 30.0),
        "label": "Béo phì độ I",
        "icon": "🔴",
        "color": "#FF9800",
        "risk": "Cao",
        "advice": "Cần giảm cân ngay, tham khảo bác sĩ"
    },
    "obese_2": {
        "range": (30.0, 100),
        "label": "Béo phì độ II",
        "icon": "🚨",
        "color": "#F44336",
        "risk": "Rất cao",
        "advice": "Cần can thiệp y tế, có thể cần thuốc/phẫu thuật"
    }
}

# Lưu ý: Châu Á dùng 23 và 25, còn WHO dùng 25 và 30

CAUSES = {
    "primary": [
        {
            "name": "Ăn quá nhiều calories",
            "detail": "Ăn nhiều hơn đốt cháy → Tích tụ mỡ",
            "examples": [
                "Đồ ăn nhanh, chiên rán",
                "Đồ ngọt, nước ngọt",
                "Ăn nhiều bữa tối",
                "Ăn vặt không kiểm soát"
            ]
        },
        {
            "name": "Ít vận động",
            "detail": "Ngồi nhiều, ít hoạt động thể chất",
            "examples": [
                "Làm việc văn phòng 8-10 giờ/ngày",
                "Xem TV, điện thoại nhiều",
                "Đi xe máy, ô tô thay vì đi bộ",
                "Không tập thể dục"
            ]
        }
    ],
    
    "secondary": [
        {
            "name": "Di truyền",
            "detail": "Cha mẹ béo → Con có nguy cơ cao hơn 50-80%"
        },
        {
            "name": "Tuổi tác",
            "detail": "Sau 30 tuổi, chuyển hóa chậm lại"
        },
        {
            "name": "Giới tính",
            "detail": "Nữ dễ tích mỡ hơn nam (hormone)"
        },
        {
            "name": "Thuốc",
            "detail": "Corticoid, thuốc chống trầm cảm, insulin..."
        },
        {
            "name": "Bệnh lý",
            "detail": "Suy giáp, PCOS, Cushing..."
        },
        {
            "name": "Stress & Thiếu ngủ",
            "detail": "Tăng hormone cortisol → Thèm ăn → Béo"
        }
    ]
}

HEALTH_RISKS = {
    "cardiovascular": {
        "name": "Bệnh Tim Mạch",
        "icon": "❤️",
        "risk_increase": "2-3 lần",
        "diseases": [
            "Cao huyết áp (70% nguy cơ)",
            "Bệnh mạch vành",
            "Suy tim",
            "Đột quỵ",
            "Rối loạn lipid máu"
        ]
    },
    
    "metabolic": {
        "name": "Rối loạn Chuyển hóa",
        "icon": "🩸",
        "risk_increase": "5-10 lần",
        "diseases": [
            "Tiểu đường type 2 (80% nguy cơ)",
            "Hội chứng chuyển hóa",
            "Gan nhiễm mỡ",
            "Sỏi mật"
        ]
    },
    
    "respiratory": {
        "name": "Bệnh Hô Hấp",
        "icon": "🫁",
        "risk_increase": "3-4 lần",
        "diseases": [
            "Ngưng thở khi ngủ (Sleep apnea)",
            "Hen phế quản",
            "COPD",
            "Khó thở khi gắng sức"
        ]
    },
    
    "musculoskeletal": {
        "name": "Bệnh Xương Khớp",
        "icon": "🦴",
        "risk_increase": "4-5 lần",
        "diseases": [
            "Thoái hóa khớp gối",
            "Thoái hóa khớp háng",
            "Gút (axit uric cao)",
            "Đau lưng mãn tính"
        ]
    },
    
    "cancer": {
        "name": "Ung thư",
        "icon": "🎗️",
        "risk_increase": "1.5-2 lần",
        "diseases": [
            "Ung thư đại trực tràng",
            "Ung thư vú (sau mãn kinh)",
            "Ung thư tử cung",
            "Ung thư gan",
            "Ung thư tụy"
        ]
    },
    
    "reproductive": {
        "name": "Sinh Sản",
        "icon": "👶",
        "risk_increase": "2-3 lần",
        "diseases": [
            "Vô sinh ở nữ (PCOS)",
            "Giảm testosterone ở nam",
            "Biến chứng thai kỳ",
            "Rối loạn kinh nguyệt"
        ]
    },
    
    "psychological": {
        "name": "Tâm Lý",
        "icon": "🧠",
        "risk_increase": "2 lần",
        "diseases": [
            "Trầm cảm",
            "Lo âu",
            "Tự ti, mặc cảm",
            "Giảm chất lượng cuộc sống"
        ]
    }
}

PREVENTION = {
    "diet": {
        "title": "🍽️ Chế độ ăn",
        "tips": [
            "Ăn đúng giờ, đủ 3 bữa chính",
            "Giảm đồ chiên rán, béo mỡ",
            "Tăng rau xanh, trái cây",
            "Hạn chế đường, nước ngọt",
            "Uống đủ nước 1.5-2 lít/ngày",
            "Ăn chậm, nhai kỹ",
            "Dùng đĩa nhỏ để kiểm soát khẩu phần"
        ]
    },
    
    "exercise": {
        "title": "🏃 Vận động",
        "tips": [
            "Tập thể dục ít nhất 150 phút/tuần",
            "Đi bộ 30 phút mỗi ngày",
            "Leo cầu thang thay vì thang máy",
            "Đứng dậy vận động mỗi 1 giờ ngồi",
            "Chơi thể thao với gia đình",
            "Làm việc nhà, làm vườn",
            "Bắt đầu từ nhẹ, tăng dần"
        ]
    },
    
    "lifestyle": {
        "title": "🛌 Lối sống",
        "tips": [
            "Ngủ đủ 7-8 giờ/đêm",
            "Quản lý stress: thiền, yoga",
            "Tránh ăn khuya",
            "Hạn chế rượu bia",
            "Cân nặng thường xuyên (1 tuần/lần)",
            "Ghi chép nhật ký ăn uống",
            "Tìm bạn đồng hành giảm cân"
        ]
    },
    
    "medical": {
        "title": "🏥 Y tế",
        "tips": [
            "Khám sức khỏe định kỳ 6 tháng/lần",
            "Xét nghiệm: đường máu, lipid máu",
            "Tham khảo bác sĩ dinh dưỡng",
            "Dùng thuốc theo chỉ định (nếu cần)",
            "Cân nhắc phẫu thuật nếu BMI >35 và có biến chứng"
        ]
    }
}

# Liên kết với các bệnh khác trong app
RELATED_DISEASES = {
    "direct_consequences": {
        "diabetes": {
            "name": "Tiểu đường Type 2",
            "risk": "80%",
            "mechanism": "Béo phì → Kháng insulin → Tiểu đường",
            "page": "2_🩸_Tiểu_Đường"
        },
        "hypertension": {
            "name": "Cao huyết áp",
            "risk": "70%",
            "mechanism": "Béo phì → Tăng khối lượng máu → Tăng huyết áp",
            "page": "1_❤️_Tim_Mạch"
        },
        "dyslipidemia": {
            "name": "Rối loạn lipid máu",
            "risk": "65%",
            "mechanism": "Béo phì → Tăng LDL, giảm HDL, tăng triglyceride",
            "page": "1_❤️_Tim_Mạch"  # Tab 3
        }
    },
    
    "complications": {
        "heart_failure": {
            "name": "Suy tim",
            "risk": "2x",
            "mechanism": "Cao huyết áp lâu năm → Suy tim",
            "page": "1_❤️_Tim_Mạch"
        },
        "copd": {
            "name": "COPD",
            "risk": "3x",
            "mechanism": "Béo phì → Khó thở → Giảm chức năng phổi",
            "page": "11_🫁_Hô_Hấp"  # Sẽ tạo
        },
        "osteoarthritis": {
            "name": "Thoái hóa khớp",
            "risk": "4x",
            "mechanism": "Béo phì → Áp lực lên khớp → Mòn sụn",
            "page": "12_🦴_Xương_Khớp"  # Sẽ tạo
        },
        "gout": {
            "name": "Gút",
            "risk": "3x",
            "mechanism": "Béo phì → Axit uric cao → Gút",
            "page": "12_🦴_Xương_Khớp"  # Sẽ tạo
        }
    }
}

# Các mốc giảm cân quan trọng
WEIGHT_LOSS_BENEFITS = {
    "5_percent": {
        "weight_loss": "5% cân nặng",
        "example": "Nếu 80kg → Giảm 4kg",
        "benefits": [
            "Giảm đường huyết rõ rệt",
            "Giảm huyết áp 5-10 mmHg",
            "Giảm triglyceride 20-30%",
            "Cải thiện chất lượng ngủ"
        ]
    },
    "10_percent": {
        "weight_loss": "10% cân nặng",
        "example": "Nếu 80kg → Giảm 8kg",
        "benefits": [
            "Giảm nguy cơ tiểu đường 50%",
            "Giảm huyết áp 10-20 mmHg",
            "Cải thiện lipid máu đáng kể",
            "Giảm đau khớp gối rõ rệt",
            "Tăng năng lượng, sức khỏe tốt hơn"
        ]
    },
    "15_percent": {
        "weight_loss": "15% cân nặng",
        "example": "Nếu 80kg → Giảm 12kg",
        "benefits": [
            "Đảo ngược tiền tiểu đường",
            "Có thể ngừng thuốc huyết áp (theo bác sĩ)",
            "Cải thiện đáng kể sức khỏe tim mạch",
            "Tăng tuổi thọ 2-5 năm",
            "Cải thiện sức khỏe tâm lý"
        ]
    }
}

