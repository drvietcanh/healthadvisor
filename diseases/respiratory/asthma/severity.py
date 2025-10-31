"""
Asthma Severity Classification - Phân loại mức độ hen suyễn
============================================================

Theo tiêu chuẩn GINA (Global Initiative for Asthma)
"""

SEVERITY_CLASSIFICATION = {
    "title": "📊 Phân Loại Mức Độ Hen",
    
    "intermittent": {
        "name": "Hen Nhẹ Không Thường Xuyên",
        "symptoms_frequency": "< 2 ngày/tuần",
        "nighttime": "< 2 đêm/tháng",
        "daily_life": "KHÔNG ảnh hưởng",
        "example": "Chỉ hen khi gặp mèo, còn lại khỏe hẳn",
        "icon": "🟢"
    },
    
    "mild_persistent": {
        "name": "Hen Nhẹ Dai Dẳng",
        "symptoms_frequency": "> 2 ngày/tuần (NHƯNG không mỗi ngày)",
        "nighttime": "3-4 đêm/tháng",
        "daily_life": "Ảnh hưởng CHÚT ÍT",
        "example": "Khó thở vài lần/tuần, đôi khi thức giấc ban đêm",
        "icon": "🟡"
    },
    
    "moderate_persistent": {
        "name": "Hen Trung Bình Dai Dẳng",
        "symptoms_frequency": "MỖI NGÀY có triệu chứng",
        "nighttime": "> 1 đêm/tuần",
        "daily_life": "Ảnh hưởng NHIỀU (giới hạn vận động)",
        "example": "Phải xịt thuốc mỗi ngày, hay thức giấc đêm",
        "icon": "🟠"
    },
    
    "severe_persistent": {
        "name": "Hen Nặng Dai Dẳng",
        "symptoms_frequency": "Triệu chứng SUỐT NGÀY",
        "nighttime": "Hầu như MỖI ĐÊM",
        "daily_life": "Ảnh hưởng NGHIÊM TRỌNG",
        "example": "Khó thở liên tục, thường xuyên nhập viện",
        "icon": "🔴"
    }
}

