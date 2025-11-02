"""
Comparisons - So sánh dễ hiểu
"""

COMPARISONS = {
    "medications_simple": {
        "title": "Thuốc giống như gì?",
        "examples": [
            {
                "drug": "Thuốc lợi tiểu",
                "like": "Như MỞ VÒI NƯỚC",
                "explain": "Giúp cơ thể đào thải nước ra ngoài → Giảm áp lực",
                "emoji": "🚰💧"
            },
            {
                "drug": "Thuốc giãn mạch",
                "like": "Như MỞ RỘNG ỐNG NƯỚC",
                "explain": "Mạch máu giãn → Máu chảy dễ → Tim bớt vất vả",
                "emoji": "🔧📏"
            },
            {
                "drug": "Insulin",
                "like": "Như CHÌA KHÓA MỞ CỬA",
                "explain": "Mở cửa tế bào → Đường vào được → Giảm đường máu",
                "emoji": "🔑🚪"
            },
            {
                "drug": "Thuốc chống đông",
                "like": "Như CHO NƯỚC SÔI THÊM CHÚT ĐÁ",
                "explain": "Máu loãng hơn → Không đông cục → Giảm nguy cơ tắc mạch",
                "emoji": "🧊💉"
            }
        ]
    },
    
    "portion_sizes": {
        "title": "Khẩu phần ăn = So với đồ vật",
        "examples": [
            "🍚 Cơm: 1 nắm tay CỤP = 1 khẩu phần",
            "🍗 Thịt/cá: Bằng 1 BỘ BÀI = 100g",
            "🥗 Rau: 2 nắm tay = Ăn thoải mái",
            "🍎 Trái cây: 1 QUẢ NẮM TAY vừa = 1 khẩu phần",
            "🥜 Hạt: 1 NẮM TAY NHỎ = 30g (đủ!)",
            "🧈 Dầu: 1 NGÓN CVCÁI = 1 thìa",
            "🧂 Muối: Đầu NGÓN CVCÁI = 1/4 thìa (cả ngày!)"
        ]
    }
}


def compare_to_daily_items(medical_value: float, value_type: str) -> str:
    """So sánh giá trị y tế với đồ vật hàng ngày"""
    
    comparisons_map = {
        "blood_pressure_high": {
            "120": "Như áp lực 1 cái BƠM TAY bóng đá 🏀",
            "140": "Như áp lực BƠM HƠI xe đạp 🚲",
            "160": "Như áp lực BƠM HƠI xe máy 🏍️",
            "180": "Như áp lực NỒI ÁP SUẤT đang sôi 🍲⚠️"
        },
        "blood_sugar_mgdl": {
            "100": "1 thìa cà phê đường = Bình thường ✅",
            "150": "1.5 thìa đường = Hơi cao ⚠️",
            "200": "2 thìa đường = Cao 🔴",
            "300": "3 thìa đường = Rất cao 🚨"
        },
        "salt_grams": {
            "1": "1/5 thìa cà phê = Rất ít ✅",
            "3": "3/5 thìa cà phê = Giới hạn người THA ⚠️",
            "5": "1 thìa cà phê = Giới hạn người bình thường",
            "10": "2 thìa cà phê = QUÁ NHIỀU! 🚫"
        }
    }
    
    return comparisons_map.get(value_type, {})

