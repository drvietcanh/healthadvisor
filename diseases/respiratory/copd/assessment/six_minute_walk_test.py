"""
Six Minute Walk Test - Test 6 Phút Đi Bộ cho COPD
"""

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

