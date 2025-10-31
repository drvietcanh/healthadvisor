"""
Disease Info - Thông tin cơ bản về béo phì
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


__all__ = ['OBESITY_INFO', 'BMI_CATEGORIES_ASIAN', 'CAUSES']
