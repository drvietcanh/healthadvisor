"""
Suy Thận Mạn (Chronic Kidney Disease) - Thông tin cơ bản
Basic information about CKD
"""

from typing import Dict

CKD_INFO = {
    "name": "Suy Thận Mạn",
    "name_en": "Chronic Kidney Disease (CKD)",
    
    "simple_explanation": """
💡 Suy thận mạn là gì? (Giải thích đơn giản)

Tưởng tượng thận như bộ lọc nước:
- Thận BÌNH THƯỜNG: Lọc máu sạch, loại bỏ chất độc, giữ nước và muối đúng mức
- Thận SUY: Bộ lọc HỎNG, không lọc được → Chất độc tích tụ trong máu

🫘 Chuyện gì xảy ra:
1. Thận MẤT DẦN chức năng lọc máu (không hồi phục được)
2. Chất độc tích tụ trong máu → Nhiễm độc toàn thân
3. Nước, muối dư thừa → Phù, tăng huyết áp
4. Mất cân bằng điện giải → Loạn nhịp tim, yếu cơ
5. Giai đoạn cuối → Phải chạy thận (lọc máu nhân tạo) hoặc ghép thận

⚠️ ĐẶC ĐIỂM:
- Bệnh TIẾN TRIỂN, KHÔNG HỒI PHỤC
- Nhưng có thể LÀM CHẬM tiến triển bằng điều trị
- Phát hiện SỚM → Điều trị SỚM → Chậm đến giai đoạn chạy thận
- Quan trọng: Kiểm soát nguyên nhân (tiểu đường, huyết áp cao)
    """,
    
    "definition": """
Suy thận mạn là tình trạng thận mất dần chức năng lọc máu theo thời gian,
không thể loại bỏ chất độc và nước dư thừa ra khỏi máu một cách hiệu quả.
    """,
    
    "statistics_vietnam": {
        "prevalence": "~10% dân số trưởng thành (khoảng 10 triệu người)",
        "increase": "Đang tăng nhanh do tiểu đường, tăng huyết áp tăng",
        "awareness": "Chỉ 10% biết mình bị suy thận (90% không biết!)",
        "dialysis": "Khoảng 50.000 người đang chạy thận nhân tạo",
        "cost": "Chi phí chạy thận: 100-200 triệu đồng/năm/người",
        "mortality": "Chạy thận không đầy đủ → Tử vong cao"
    },
    
    "why_dangerous": """
⚠️ TẠI SAO SUY THẬN NGUY HIỂM?

1. **Chất độc tích tụ:**
   - Ure, creatinine trong máu tăng cao
   - → Nhiễm độc toàn thân: Mệt mỏi, buồn nôn, lơ mơ
   - → Tử vong nếu không điều trị

2. **Mất cân bằng nước, muối:**
   - Phù (mặt, chân, phổi)
   - Tăng huyết áp → Đột quỵ, nhồi máu cơ tim
   - Rối loạn điện giải → Loạn nhịp tim nguy hiểm

3. **Biến chứng nghiêm trọng:**
   - Thiếu máu (thận không sản xuất hormone tạo máu)
   - Loãng xương (thận không chuyển vitamin D)
   - Bệnh tim mạch (nguy cơ tăng 10-20 lần)

4. **Giai đoạn cuối:**
   - Phải chạy thận nhân tạo 3 lần/tuần (mỗi lần 4 giờ)
   - Hoặc ghép thận (rất khó, thiếu thận ghép)
   - Chi phí rất cao, chất lượng sống giảm
   - → Phòng ngừa, làm chậm tiến triển là QUAN TRỌNG NHẤT!
    """,
    
    "stages": {
        "title": "📊 Các Giai Đoạn Suy Thận (5 giai đoạn)",
        "description": "Dựa trên mức độ lọc máu (eGFR - độ lọc cầu thận):",
        "stages": [
            {
                "stage": "Giai đoạn 1",
                "egfr": "≥90 mL/phút",
                "name": "Tổn thương thận nhưng chức năng còn tốt",
                "description": "Thận vẫn lọc tốt, nhưng có dấu hiệu tổn thương (protein trong nước tiểu)",
                "action": "Theo dõi, kiểm soát nguyên nhân",
                "goal": "Ngăn tiến triển"
            },
            {
                "stage": "Giai đoạn 2",
                "egfr": "60-89 mL/phút",
                "name": "Giảm chức năng nhẹ",
                "description": "Chức năng giảm nhẹ, nhưng vẫn đủ lọc",
                "action": "Theo dõi, kiểm soát tốt",
                "goal": "Làm chậm tiến triển"
            },
            {
                "stage": "Giai đoạn 3",
                "egfr": "30-59 mL/phút",
                "name": "Giảm chức năng trung bình",
                "description": "Chức năng giảm rõ, bắt đầu có triệu chứng",
                "action": "Điều trị tích cực, chuẩn bị tâm lý",
                "goal": "Làm chậm đến giai đoạn cuối",
                "note": "⚠️ Giai đoạn này cần điều trị nghiêm túc!"
            },
            {
                "stage": "Giai đoạn 4",
                "egfr": "15-29 mL/phút",
                "name": "Giảm chức năng nặng",
                "description": "Chức năng giảm nhiều, triệu chứng rõ",
                "action": "Chuẩn bị chạy thận, giáo dục",
                "goal": "Chuẩn bị cho chạy thận",
                "warning": "🚨 Gần đến giai đoạn cuối - Cần chuẩn bị!"
            },
            {
                "stage": "Giai đoạn 5",
                "egfr": "<15 mL/phút",
                "name": "SUY THẬN GIAI ĐOẠN CUỐI",
                "description": "Thận không còn lọc được → Phải chạy thận hoặc ghép thận",
                "action": "Chạy thận nhân tạo, ghép thận",
                "goal": "Duy trì sự sống",
                "warning": "🚨 Không chạy thận → TỬ VONG trong vài tuần!"
            }
        ],
        "note": "💡 Mục tiêu: Phát hiện SỚM (giai đoạn 1-2) → Làm chậm tiến triển → Tránh đến giai đoạn 5!"
    }
}

