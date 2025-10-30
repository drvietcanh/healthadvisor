"""
COPD Assessment - Đánh giá mức độ COPD
=======================================

Các bảng hỏi và thang điểm đánh giá mức độ nặng của COPD
"""

from typing import Dict, List

# Thang điểm mMRC - Đánh giá khó thở
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

# Bảng hỏi CAT - Đánh giá tác động của COPD
CAT_QUESTIONNAIRE = {
    "name": "CAT - Bảng Đánh Giá COPD",
    "full_name": "COPD Assessment Test",
    "description": "8 câu hỏi đánh giá tác động của COPD đến cuộc sống",
    
    "simple_explanation": """
💡 Bảng CAT là gì?

8 câu hỏi đơn giản về:
- Ho nhiều không?
- Có đờm không?
- Ngực tức không?
- Khó thở khi leo cầu thang?
- Làm việc nhà có khó không?
- Ra khỏi nhà có tự tin không?
- Ngủ có ngon không?
- Có còn sức lực không?

→ Điểm càng CAO = COPD ảnh hưởng càng NHIỀU
    """,
    
    "questions": [
        {
            "number": 1,
            "question": "Tôi không bao giờ ho ←→ Tôi ho liên tục",
            "aspect": "Ho",
            "scale": "0 (không ho) đến 5 (ho liên tục)"
        },
        {
            "number": 2,
            "question": "Tôi không có đờm ←→ Lồng ngực tôi đầy đờm",
            "aspect": "Đờm",
            "scale": "0 (không đờm) đến 5 (đầy đờm)"
        },
        {
            "number": 3,
            "question": "Ngực tôi không tức ←→ Ngực tôi rất tức",
            "aspect": "Ngực tức",
            "scale": "0 (không tức) đến 5 (rất tức)"
        },
        {
            "number": 4,
            "question": "Leo cầu thang không khó thở ←→ Leo cầu thang rất khó thở",
            "aspect": "Khó thở khi gắng sức",
            "scale": "0 (không khó thở) đến 5 (rất khó thở)"
        },
        {
            "number": 5,
            "question": "Làm việc nhà không hạn chế ←→ Làm việc nhà rất hạn chế",
            "aspect": "Hoạt động trong nhà",
            "scale": "0 (không hạn chế) đến 5 (rất hạn chế)"
        },
        {
            "number": 6,
            "question": "Tự tin ra khỏi nhà ←→ Không tự tin ra khỏi nhà",
            "aspect": "Sự tự tin",
            "scale": "0 (rất tự tin) đến 5 (không tự tin)"
        },
        {
            "number": 7,
            "question": "Ngủ rất ngon ←→ Không ngủ được vì COPD",
            "aspect": "Giấc ngủ",
            "scale": "0 (ngủ ngon) đến 5 (không ngủ được)"
        },
        {
            "number": 8,
            "question": "Tràn đầy sức lực ←→ Hoàn toàn mệt mỏi",
            "aspect": "Sức lực",
            "scale": "0 (tràn đầy sức lực) đến 5 (hoàn toàn mệt)"
        }
    ],
    
    "scoring": {
        "range": "0-40 điểm",
        "interpretation": {
            "0-10": {
                "level": "Tác động NHẸ",
                "meaning": "COPD ảnh hưởng ít đến cuộc sống",
                "color": "green"
            },
            "11-20": {
                "level": "Tác động TRUNG BÌNH",
                "meaning": "COPD bắt đầu ảnh hưởng đến sinh hoạt",
                "color": "yellow"
            },
            "21-30": {
                "level": "Tác động NẶNG",
                "meaning": "COPD ảnh hưởng nhiều đến cuộc sống",
                "color": "orange"
            },
            "31-40": {
                "level": "Tác động RẤT NẶNG",
                "meaning": "COPD ảnh hưởng nghiêm trọng đến cuộc sống",
                "color": "red"
            }
        }
    },
    
    "clinical_use": [
        "Theo dõi tiến triển bệnh",
        "Đánh giá hiệu quả điều trị",
        "Quyết định thay đổi phác đồ",
        "Đo lường chất lượng cuộc sống"
    ],
    
    "note": "⚠️ Sự thay đổi ≥2 điểm CAT = Có ý nghĩa lâm sàng"
}

# Phân loại GOLD - Độ nặng COPD
GOLD_CLASSIFICATION = {
    "name": "GOLD - Phân Loại Độ Nặng COPD",
    "full_name": "Global Initiative for Chronic Obstructive Lung Disease",
    
    "simple_explanation": """
💡 GOLD là gì?

Chia COPD thành 4 độ nặng dựa trên FEV1 (thể tích thở ra):
- GOLD 1: Nhẹ (≥80% bình thường)
- GOLD 2: Trung bình (50-79%)
- GOLD 3: Nặng (30-49%)
- GOLD 4: Rất nặng (<30%)

→ FEV1 càng THẤP = Phổi càng NẶNG
    """,
    
    "grades": [
        {
            "grade": "GOLD 1",
            "name": "Nhẹ",
            "fev1_percent": "≥80%",
            "description": "Chức năng phổi gần bình thường",
            "symptoms": "Có thể không có triệu chứng hoặc ho, đờm ít",
            "note": "Nhiều người chưa biết mình có COPD"
        },
        {
            "grade": "GOLD 2",
            "name": "Trung Bình",
            "fev1_percent": "50-79%",
            "description": "Chức năng phổi giảm vừa",
            "symptoms": "Khó thở khi gắng sức, ho đờm nhiều hơn",
            "note": "Thường bắt đầu đến khám ở giai đoạn này"
        },
        {
            "grade": "GOLD 3",
            "name": "Nặng",
            "fev1_percent": "30-49%",
            "description": "Chức năng phổi giảm nhiều",
            "symptoms": "Khó thở rõ, ảnh hưởng sinh hoạt, đợt cấp thường xuyên",
            "note": "Cần điều trị tích cực, theo dõi sát"
        },
        {
            "grade": "GOLD 4",
            "name": "Rất Nặng",
            "fev1_percent": "<30%",
            "description": "Suy phổi nghiêm trọng",
            "symptoms": "Khó thở nghỉ ngơi, suy tim phổi, cần thở oxy",
            "note": "Nguy cơ tử vong cao, chất lượng sống rất kém"
        }
    ],
    
    "abcd_assessment": {
        "name": "Phân Nhóm ABCD (GOLD 2017)",
        "description": "Kết hợp triệu chứng + đợt cấp để phân loại",
        
        "groups": {
            "A": {
                "name": "Nhóm A - Ít Triệu Chứng, Ít Đợt Cấp",
                "criteria": [
                    "mMRC 0-1 hoặc CAT <10",
                    "Đợt cấp 0-1 lần/năm (không nhập viện)"
                ],
                "risk": "Nguy cơ THẤP",
                "treatment": "Thuốc giãn phế quản khi cần"
            },
            "B": {
                "name": "Nhóm B - Nhiều Triệu Chứng, Ít Đợt Cấp",
                "criteria": [
                    "mMRC ≥2 hoặc CAT ≥10",
                    "Đợt cấp 0-1 lần/năm (không nhập viện)"
                ],
                "risk": "Triệu chứng ảnh hưởng cuộc sống",
                "treatment": "Thuốc giãn phế quản dài hạn"
            },
            "C": {
                "name": "Nhóm C - Ít Triệu Chứng, Nhiều Đợt Cấp",
                "criteria": [
                    "mMRC 0-1 hoặc CAT <10",
                    "Đợt cấp ≥2 lần/năm HOẶC ≥1 lần nhập viện"
                ],
                "risk": "Nguy cơ CAO",
                "treatment": "Điều trị tích cực để giảm đợt cấp"
            },
            "D": {
                "name": "Nhóm D - Nhiều Triệu Chứng, Nhiều Đợt Cấp",
                "criteria": [
                    "mMRC ≥2 hoặc CAT ≥10",
                    "Đợt cấp ≥2 lần/năm HOẶC ≥1 lần nhập viện"
                ],
                "risk": "Nguy cơ RẤT CAO",
                "treatment": "Điều trị tối đa, theo dõi sát"
            }
        }
    }
}

# Test 6 phút đi bộ
SIX_MINUTE_WALK_TEST = {
    "name": "Test 6 Phút Đi Bộ (6MWT)",
    "description": "Đo quãng đường đi bộ được trong 6 phút",
    
    "simple_explanation": """
💡 Test 6 phút đi bộ là gì?

Đơn giản: Đi bộ NHANH NHẤT có thể trong 6 phút
- Đo xem đi được bao nhiêu mét
- Đo SpO2 (nồng độ oxy máu) trước và sau

→ Đi được càng XA = Thể lực càng TỐT
→ SpO2 giảm nhiều = Thiếu oxy nghiêm trọng
    """,
    
    "interpretation": {
        "normal": ">400 mét",
        "moderate_impairment": "300-400 mét",
        "severe_impairment": "150-300 mét",
        "very_severe": "<150 mét"
    },
    
    "clinical_significance": [
        "Đánh giá thể lực tổng thể",
        "Tiên lượng bệnh (đi <350m → Nguy cơ tử vong cao)",
        "Theo dõi hiệu quả điều trị",
        "Quyết định phục hồi chức năng"
    ],
    
    "note": "⚠️ Giảm SpO2 <88% khi đi bộ → Cần bổ sung oxy"
}

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
        0: "chỉ khó thở khi gắn sức mạnh",
        1: "khó thở khi đi bộ nhanh hoặc leo dốc",
        2: "đi bộ chậm hơn người cùng tuổi",
        3: "phải dừng nghỉ sau 100 mét",
        4: "khó thở ngay cả khi nghỉ hoặc thay đồ"
    }
    # Implement matching logic
    return 0  # Placeholder

