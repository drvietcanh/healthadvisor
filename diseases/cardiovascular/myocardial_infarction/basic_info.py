"""
Nhồi Máu Cơ Tim (Myocardial Infarction) - Thông tin cơ bản
Basic information about Heart Attack
"""

from typing import Dict

MI_INFO = {
    "name": "Nhồi Máu Cơ Tim",
    "name_en": "Myocardial Infarction (Heart Attack)",
    
    "simple_explanation": """
💡 Nhồi máu cơ tim là gì? (Giải thích đơn giản)

Tưởng tượng tim như động cơ xe:
- Tim BÌNH THƯỜNG: Động cơ chạy tốt, có nhiên liệu (máu) liên tục
- Tim NHỒI MÁU: Động cơ bị TẮC ỐNG DẪN NHIÊN LIỆU → Không có nhiên liệu → Tắt máy

🫀 Chuyện gì xảy ra:
1. Mạch máu nuôi tim BỊ TẮC (do cục máu đông, mảng xơ vữa)
2. Cơ tim KHÔNG được nuôi bằng máu → THIẾU OXY
3. Cơ tim BỊ CHẾT (hoại tử) → Tim không bơm máu được
4. → SUY TIM, LOẠN NHỊP, TỬ VONG

⚠️ ĐẶC ĐIỂM:
- CẤP CỨU - Nguy hiểm tính mạng!
- Có KHUNG GIỜ VÀNG (Golden Time) để điều trị
- Càng điều trị SỚM = Càng ít tổn thương cơ tim
- Mỗi phút trì hoãn = Hàng triệu tế bào cơ tim chết!
    """,
    
    "definition": """
Nhồi máu cơ tim là tình trạng một phần cơ tim bị chết do tắc nghẽn hoàn toàn 
mạch máu vành (động mạch nuôi tim), khiến cơ tim không nhận được máu giàu oxy.
    """,
    
    "statistics_vietnam": {
        "prevalence": "Nguyên nhân tử vong hàng đầu ở VN",
        "mortality": "50% tử vong trong 1 giờ đầu nếu không điều trị",
        "age_group": "Chủ yếu >50 tuổi (nam > nữ trước 65 tuổi)",
        "risk": "30% có tiền sử đau tim trước đó",
        "survival": "Điều trị trong 2 giờ đầu → Tỷ lệ sống 95%"
    },
    
    "why_dangerous": """
⚠️ TẠI SAO NHỒI MÁU CƠ TIM NGUY HIỂM?

1. **Tử vong nhanh:**
   - 50% tử vong trong 1 GIỜ ĐẦU nếu không điều trị
   - Cơ tim chết → Tim không bơm máu → Cơ thể không có oxy
   - → TỬ VONG do sốc tim, rối loạn nhịp nguy hiểm

2. **Tổn thương vĩnh viễn:**
   - Cơ tim chết KHÔNG HỒI PHỤC được
   - → Suy tim mạn tính, giảm chất lượng sống
   - → Phải uống thuốc suốt đời

3. **Biến chứng nguy hiểm:**
   - Suy tim cấp → Phù phổi → Chết đuối trên cạn
   - Rối loạn nhịp nguy hiểm (rung thất) → Ngừng tim đột ngột
   - Vỡ tim → Tử vong tức thì

4. **Khung giờ vàng:**
   - Trong 2 giờ đầu: Có thể cứu được 90% cơ tim
   - Sau 6 giờ: Chỉ cứu được 50% cơ tim
   - Sau 12 giờ: Cơ tim đã chết hết → Không thể cứu
   - → MỖI PHÚT ĐỀU QUÝ GIÁ!
    """,
    
    "types": {
        "stemi": {
            "name": "STEMI (Nhồi máu có ST chênh)",
            "description": "Tắc nghẽn HOÀN TOÀN mạch máu vành",
            "severity": "NGUY HIỂM NHẤT - Cần điều trị NGAY trong 2 giờ",
            "treatment": "Tiêu sợi huyết (thrombolysis) hoặc can thiệp mạch vành (PCI)"
        },
        "nstemi": {
            "name": "NSTEMI (Nhồi máu không ST chênh)",
            "description": "Tắc nghẽn MỘT PHẦN mạch máu vành",
            "severity": "Nghiêm trọng nhưng có thể cho phép điều trị trong 24-48h",
            "treatment": "Thuốc chống đông, có thể can thiệp mạch vành"
        },
        "unstable_angina": {
            "name": "Đau Thắt Ngực Không Ổn Định",
            "description": "Chưa nhồi máu nhưng có nguy cơ cao",
            "severity": "Cảnh báo - Có thể chuyển thành nhồi máu",
            "treatment": "Điều trị tích cực để tránh nhồi máu"
        }
    }
}

