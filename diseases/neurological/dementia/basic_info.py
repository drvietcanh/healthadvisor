"""
Sa Sút Trí Tuệ (Dementia) - Thông tin cơ bản
Basic information about Dementia
"""

from typing import Dict

DEMENTIA_INFO = {
    "name": "Sa Sút Trí Tuệ",
    "name_en": "Dementia",
    
    "simple_explanation": """
💡 Sa sút trí tuệ là gì? (Giải thích đơn giản)

Tưởng tượng não như một thư viện:
- Não BÌNH THƯỜNG: Sách ngăn nắp, tìm sách dễ dàng
- Não SA SÚT TRÍ TUỆ: Sách rơi vãi, mất mất, không tìm được sách

🧠 Chuyện gì xảy ra:
1. Tế bào não BỊ TỔN THƯƠNG, CHẾT DẦN
2. Não MẤT KHẢ NĂNG lưu trữ, nhớ lại thông tin
3. Mất dần: Trí nhớ → Suy nghĩ → Ngôn ngữ → Khả năng tự chăm sóc
4. → Không nhớ được gì, không nhận ra người thân, không tự ăn uống

⚠️ ĐẶC ĐIỂM:
- Bệnh TIẾN TRIỂN, KHÔNG THỂ HỒI PHỤC
- Nhưng có thể LÀM CHẬM tiến triển bằng điều trị
- Người bệnh KHÔNG TỰ BIẾT mình bị bệnh (gia đình phát hiện trước)
- Gia đình là người quan trọng nhất trong chăm sóc
    """,
    
    "definition": """
Sa sút trí tuệ là tình trạng suy giảm nghiêm trọng và tiến triển của chức năng nhận thức
(trí nhớ, suy nghĩ, ngôn ngữ, định hướng, phán đoán), 
ảnh hưởng đến khả năng thực hiện các hoạt động hàng ngày.
    """,
    
    "statistics_vietnam": {
        "prevalence": "~5-8% người >65 tuổi (khoảng 500.000-800.000 người)",
        "increase": "Tăng gấp đôi mỗi 5 năm sau 65 tuổi",
        "alzheimer": "60-70% sa sút trí tuệ là Alzheimer",
        "vascular": "20-30% sa sút trí tuệ do mạch máu (sau đột quỵ)",
        "caregiver_burden": "Gia đình chăm sóc rất vất vả, căng thẳng cao"
    },
    
    "why_important": """
⚠️ TẠI SAO CẦN QUAN TÂM SA SÚT TRÍ TUỆ?

1. **Ảnh hưởng nghiêm trọng:**
   - Mất trí nhớ → Không nhớ được gì
   - Mất định hướng → Đi lạc, không biết về nhà
   - Mất khả năng tự chăm sóc → Phải có người chăm
   - Thay đổi tính cách → Dễ giận dữ, nghi ngờ

2. **Gánh nặng cho gia đình:**
   - Phải chăm sóc 24/24 → Rất vất vả
   - Chi phí điều trị, chăm sóc cao
   - Căng thẳng, trầm cảm ở người chăm sóc

3. **Phát hiện sớm:**
   - Điều trị SỚM → Làm chậm tiến triển
   - Chăm sóc tốt → Cải thiện chất lượng sống
   - Người bệnh vẫn có thể sống có ý nghĩa nhiều năm

4. **Phòng ngừa:**
   - Một số yếu tố nguy cơ CÓ THỂ phòng ngừa được
   - Rèn luyện trí não, vận động → Giảm nguy cơ 30-50%
    """,
    
    "types": {
        "alzheimer": {
            "name": "Alzheimer (Bệnh quên)",
            "description": "Phổ biến nhất (60-70%), do tích tụ protein bất thường trong não",
            "progression": "Tiến triển từ từ, mất trí nhớ trước tiên",
            "age": "Thường >65 tuổi, tăng theo tuổi"
        },
        "vascular": {
            "name": "Sa sút trí tuệ mạch máu",
            "description": "Sau đột quỵ, do tổn thương mạch máu não",
            "progression": "Tiến triển theo từng bước (sau mỗi đột quỵ)",
            "prevention": "Kiểm soát huyết áp, tiểu đường → Phòng đột quỵ"
        },
        "mixed": {
            "name": "Sa sút trí tuệ hỗn hợp",
            "description": "Kết hợp Alzheimer + Mạch máu",
            "prevalence": "Khá phổ biến ở người già"
        },
        "lewy_body": {
            "name": "Sa sút trí tuệ thể Lewy",
            "description": "Kèm theo triệu chứng Parkinson (run, cứng)",
            "hallucinations": "Thường có ảo giác (nhìn thấy người không có)"
        },
        "frontotemporal": {
            "name": "Sa sút trí tuệ thùy trán-thái dương",
            "description": "Hiếm, thường <65 tuổi",
            "symptoms": "Thay đổi tính cách, hành vi (không phải mất trí nhớ trước)"
        }
    }
}

