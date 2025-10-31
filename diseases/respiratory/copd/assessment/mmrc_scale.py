"""
mMRC Scale - Thang Điểm Khó Thở cho COPD
"""

MMRC_SCALE = {
    "name": "mMRC - Thang Điểm Khó Thở",
    "full_name": "Modified Medical Research Council Dyspnea Scale",
    "description": "Đánh giá mức độ khó thở ảnh hưởng đến sinh hoạt hàng ngày",
    
    "simple_explanation": """
💡 Thang điểm mMRC là gì?

Đơn giản: Hỏi xem bạn khó thở khi làm gì?
- Chỉ khó thở khi chạy → Nhẹ (0 điểm)
- Khó thở khi đi bộ → Nặng hơn (1-2 điểm)  
- Khó thở ngay cả khi nghỉ → Rất nặng (4 điểm)

→ Càng ít cử động mà đã khó thở = Càng NẶNG
    """,
    
    "grades": [
        {
            "grade": 0,
            "icon": "🏃",
            "description": "Chỉ khó thở khi GẮN SỨC MẠNH",
            "examples": [
                "Chạy nhanh",
                "Leo dốc cao",
                "Vác đồ nặng"
            ],
            "daily_life": "Sinh hoạt BÌNH THƯỜNG, không bị hạn chế",
            "severity": "Rất nhẹ"
        },
        {
            "grade": 1,
            "icon": "🚶‍♂️💨",
            "description": "Khó thở khi ĐI BỘ NHANH hoặc LEO DỐC NHẸ",
            "examples": [
                "Đi bộ nhanh trên mặt phẳng",
                "Leo cầu thang 1-2 tầng",
                "Đi dốc nhẹ"
            ],
            "daily_life": "Sinh hoạt gần như bình thường, hạn chế ít",
            "severity": "Nhẹ"
        },
        {
            "grade": 2,
            "icon": "🚶‍♂️😮‍💨",
            "description": "Khó thở khiến ĐI BỘ CHẬM HƠN người cùng tuổi",
            "examples": [
                "Đi bộ chậm hơn bạn bè",
                "Phải dừng nghỉ khi đi bộ trên mặt phẳng",
                "Không theo kịp người khác"
            ],
            "daily_life": "Bắt đầu ảnh hưởng sinh hoạt",
            "severity": "Trung bình"
        },
        {
            "grade": 3,
            "icon": "🛑😤",
            "description": "Phải DỪNG NGHỈ sau khi đi bộ khoảng 100 MÉT",
            "examples": [
                "Đi bộ 100m (khoảng 2 phút) là phải nghỉ",
                "Không đi bộ xa được",
                "Khó leo cầu thang"
            ],
            "daily_life": "Ảnh hưởng NHIỀU đến sinh hoạt",
            "severity": "Nặng"
        },
        {
            "grade": 4,
            "icon": "🏠😰",
            "description": "Khó thở quá KHÔNG RA KHỎI NHÀ, hoặc khó thở ngay khi THAY ĐỒ",
            "examples": [
                "Khó thở ngay cả khi ngồi yên",
                "Khó thở khi mặc quần áo",
                "Không thể ra khỏi nhà",
                "Tắm rửa cũng khó thở"
            ],
            "daily_life": "KHÔNG tự chăm sóc được, cần người giúp",
            "severity": "Rất nặng"
        }
    ],
    
    "interpretation": {
        "0-1": "Nhẹ - Ảnh hưởng ít đến sinh hoạt",
        "2": "Trung bình - Bắt đầu ảnh hưởng sinh hoạt",
        "3-4": "Nặng - Ảnh hưởng nghiêm trọng đến sinh hoạt"
    },
    
    "clinical_use": "mMRC ≥2 → Nguy cơ đợt cấp cao, cần điều trị tích cực hơn"
}

