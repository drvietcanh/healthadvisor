"""
Viêm phổi (Pneumonia) - Thông tin cơ bản
Basic information about Pneumonia
"""

from typing import Dict

PNEUMONIA_INFO = {
    "name": "Viêm phổi",
    "name_en": "Pneumonia",
    
    "simple_explanation": """
💡 Viêm phổi là gì? (Giải thích đơn giản)

Tưởng tượng phổi như bộ lọc không khí:
- Phổi BÌNH THƯỜNG: Bộ lọc sạch, lọc tốt khí vào
- Phổi VIÊM PHỔI: Bộ lọc BỊ VIÊM, ĐẦY DỊCH → Không lọc được khí

🫁 Chuyện gì xảy ra:
1. Phế nang (túi khí) BỊ VIÊM, ĐẦY MỦ/DỊCH
2. Oxy không vào được máu → THIẾU OXY
3. Cơ thể phải thở NHANH, GẮNG SỨC để lấy oxy
4. → HO, SỐT, KHÓ THỞ

⚠️ ĐẶC ĐIỂM:
- Bệnh NHIỄM TRÙNG cấp tính (vi khuẩn, virus, nấm)
- CÓ THỂ HỒI PHỤC hoàn toàn nếu điều trị đúng, kịp thời
- NGUY HIỂM nếu không điều trị → Suy hô hấp, tử vong
    """,
    
    "definition": """
Viêm phổi là tình trạng nhiễm trùng cấp tính ở phổi,
gây viêm và tích tụ dịch trong phế nang (túi khí),
làm giảm khả năng trao đổi oxy của phổi.
    """,
    
    "statistics_vietnam": {
        "prevalence": "Phổ biến, đặc biệt ở trẻ em và người già",
        "age_group": "Trẻ <5 tuổi, người >65 tuổi dễ mắc",
        "mortality": "Nguyên nhân tử vong hàng đầu ở trẻ em và người già",
        "risk": "Mùa lạnh, thay đổi thời tiết → Tăng nguy cơ",
        "hospitalization": "80% ca nặng cần nhập viện"
    },
    
    "why_dangerous": """
⚠️ VIÊM PHỔI NGUY HIỂM NHƯ THẾ NÀO?

1. **Thiếu oxy nặng:**
   - Phế nang đầy dịch → Không trao đổi được oxy
   - → Cơ thể THIẾU OXY → Tổn thương não, tim, thận

2. **Nhiễm trùng lan rộng:**
   - Vi khuẩn từ phổi vào MÁU → Nhiễm trùng máu (Sepsis)
   - → SỐC NHIỄM KHUẨN → TỬ VONG nhanh

3. **Nguy hiểm với người già:**
   - Miễn dịch yếu → Dễ biến chứng
   - Triệu chứng MƠ HỒ (không sốt cao, chỉ mệt) → Chậm phát hiện
   - → Dễ chuyển nặng, tử vong

4. **Nguy hiểm với trẻ nhỏ:**
   - Đường thở NHỎ → Dễ tắc nghẽn
   - → Suy hô hấp nhanh, nguy hiểm tính mạng
    """,
    
    "types": {
        "community_acquired": {
            "name": "Viêm phổi cộng đồng",
            "description": "Mắc phải ngoài bệnh viện (phổ biến nhất)",
            "pathogens": "Vi khuẩn: Phế cầu, Haemophilus; Virus: Cúm, COVID-19"
        },
        "hospital_acquired": {
            "name": "Viêm phổi bệnh viện",
            "description": "Mắc phải khi đang nằm viện (nguy hiểm hơn)",
            "pathogens": "Vi khuẩn kháng thuốc: MRSA, Klebsiella"
        },
        "aspiration": {
            "name": "Viêm phổi hít sặc",
            "description": "Hít phải dịch dạ dày, nước bọt vào phổi",
            "risk_groups": "Người già, người đột quỵ, người mất phản xạ ho"
        },
        "viral": {
            "name": "Viêm phổi do virus",
            "description": "COVID-19, cúm, RSV",
            "characteristics": "Thường nhẹ hơn vi khuẩn, nhưng có thể nặng"
        }
    }
}

