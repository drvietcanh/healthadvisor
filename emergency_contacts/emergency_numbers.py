"""
Số điện thoại cấp cứu Việt Nam
"""

VIETNAM_EMERGENCY_NUMBERS = {
    "115": {
        "name": "Cấp cứu 115",
        "name_en": "Emergency Medical Services",
        "description": "Cứu thương, cấp cứu y tế khẩn cấp",
        "when_to_call": [
            "Đau tim, đột quỵ",
            "Tai nạn nghiêm trọng",
            "Hôn mê, không tỉnh táo",
            "Khó thở, ngừng thở",
            "Chảy máu không cầm được",
            "Ngộ độc thuốc/thực phẩm nghiêm trọng"
        ],
        "icon": "🚑",
        "color": "red",
        "priority": 1
    },
    "114": {
        "name": "Y tế dự phòng 114",
        "name_en": "Preventive Health",
        "description": "Tư vấn y tế, phòng bệnh",
        "when_to_call": [
            "Tư vấn y tế qua điện thoại",
            "Hỏi về triệu chứng bệnh",
            "Hướng dẫn phòng bệnh",
            "Thông tin dịch bệnh"
        ],
        "icon": "📞",
        "color": "blue",
        "priority": 3
    },
    "113": {
        "name": "Công an 113",
        "name_en": "Police",
        "description": "Cảnh sát, an ninh",
        "when_to_call": [
            "Mất trật tự, ẩu đả",
            "Tai nạn giao thông",
            "Mất cắp, trộm cướp",
            "Khẩn cấp cần cảnh sát"
        ],
        "icon": "👮",
        "color": "blue",
        "priority": 2
    },
    "114-chay": {
        "name": "Phòng cháy chữa cháy 114",
        "name_en": "Fire Department",
        "description": "Cứu hỏa, cứu nạn",
        "when_to_call": [
            "Hỏa hoạn",
            "Cháy nhà, cháy rừng",
            "Sự cố cần cứu nạn"
        ],
        "icon": "🚒",
        "color": "orange",
        "priority": 2
    },
    "1900-54-54-58": {
        "name": "Trung tâm chống độc BV Bạch Mai",
        "name_en": "Poison Control Center",
        "description": "Tư vấn và điều trị ngộ độc",
        "when_to_call": [
            "Ngộ độc thức ăn",
            "Ngộ độc thuốc",
            "Nuốt phải hóa chất",
            "Cần tư vấn khẩn về độc chất"
        ],
        "icon": "☠️",
        "color": "purple",
        "priority": 3
    }
}

def get_emergency_number_by_type(emergency_type):
    """
    Lấy số điện thoại cấp cứu theo loại
    
    Args:
        emergency_type: "medical", "police", "fire", "poison"
    """
    mapping = {
        "medical": "115",
        "police": "113",
        "fire": "114-chay",
        "poison": "1900-54-54-58",
        "health": "114"
    }
    
    number = mapping.get(emergency_type)
    if number:
        return VIETNAM_EMERGENCY_NUMBERS.get(number)
    return None

