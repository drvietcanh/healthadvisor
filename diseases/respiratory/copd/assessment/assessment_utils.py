"""
Assessment Utilities - Các hàm tính toán cho đánh giá COPD
"""

from typing import Dict, List


def calculate_cat_score(answers: List[int]) -> Dict:
    """Tính điểm CAT từ 8 câu trả lời (0-5 mỗi câu)"""
    if len(answers) != 8:
        return {"error": "Cần đủ 8 câu trả lời"}
    
    total = sum(answers)
    
    if total <= 10:
        level = "Tác động NHẸ"
        meaning = "COPD ảnh hưởng ít đến cuộc sống"
        color = "green"
        advice = "Tiếp tục điều trị hiện tại, tái khám 6-12 tháng/lần"
    elif total <= 20:
        level = "Tác động TRUNG BÌNH"
        meaning = "COPD bắt đầu ảnh hưởng đến sinh hoạt"
        color = "yellow"
        advice = "Cân nhắc tăng cường điều trị, tái khám 3-6 tháng/lần"
    elif total <= 30:
        level = "Tác động NẶNG"
        meaning = "COPD ảnh hưởng nhiều đến cuộc sống"
        color = "orange"
        advice = "Cần điều trị tích cực, tái khám 1-3 tháng/lần"
    else:
        level = "Tác động RẤT NẶNG"
        meaning = "COPD ảnh hưởng nghiêm trọng đến cuộc sống"
        color = "red"
        advice = "Cần điều trị tối đa, theo dõi sát, có thể cần phục hồi chức năng"
    
    return {
        "total_score": total,
        "level": level,
        "meaning": meaning,
        "color": color,
        "advice": advice
    }


def get_mmrc_grade(description: str) -> int:
    """Xác định mức mMRC từ mô tả"""
    descriptions = {
        0: ["chỉ khó thở khi gắn sức mạnh", "chạy nhanh", "leo dốc cao"],
        1: ["khó thở khi đi bộ nhanh", "leo dốc nhẹ", "leo cầu thang 1-2 tầng"],
        2: ["đi bộ chậm hơn người cùng tuổi", "phải dừng nghỉ khi đi bộ", "không theo kịp"],
        3: ["phải dừng nghỉ sau 100 mét", "không đi bộ xa được", "khó leo cầu thang"],
        4: ["khó thở ngay cả khi nghỉ", "khó thở khi thay đồ", "không thể ra khỏi nhà", "tắm rửa cũng khó thở"]
    }
    
    description_lower = description.lower()
    
    # Tìm grade phù hợp nhất
    for grade, keywords in descriptions.items():
        if any(keyword in description_lower for keyword in keywords):
            return grade
    
    return 0  # Mặc định nếu không tìm thấy

