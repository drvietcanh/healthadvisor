"""
Quick Answers
Câu trả lời nhanh cho câu hỏi phổ biến
"""


def get_quick_answers(question_type: str) -> str:
    """Câu trả lời nhanh cho câu hỏi phổ biến"""
    
    answers = {
        "huyết áp bình thường": """
📊 **Huyết áp bình thường:**

**< 120/80 mmHg** = ✅ Bình thường tuyệt vời!
**120-129/<80** = ⚠️ Hơi cao (cần thay đổi lối sống)
**130-139/80-89** = 🔴 Tăng huyết áp độ 1
**≥ 140/90** = 🚨 Tăng huyết áp độ 2

**Ví dụ dễ hiểu:**
- 115/75 = Hoàn hảo! 🎉
- 125/78 = OK nhưng cẩn thận
- 145/95 = Cần điều trị
""",
        "dấu hiệu đột quỵ": """
🚨 **Dấu hiệu đột quỵ - Nhớ BE-FAST:**

**B** = **B**alance - Mất thăng bằng
**E** = **E**yes - Nhìn mờ, nhìn đôi  
**F** = **F**ace - Xệ mặt, méo miệng
**A** = **A**rm - Yếu tay/chân (1 bên)
**S** = **S**peech - Nói khó, nói lắp
**T** = **T**ime - GỌI 115 NGAY!

**Test nhanh 10 giây:**
1. CƯỜI → Lệch miệng? ❌
2. GIƠ 2 TAY → 1 tay sa? ❌
3. NÓI 1 CÂU → Khó nói? ❌

→ CÓ 1 dấu hiệu = GỌI 115 NGAY!
⏰ Mỗi phút = 2 triệu tế bào não chết!
""",
        "đường cao": """
🍬 **Đường huyết cao - Làm gì ngay:**

**Nếu > 13 mmol/L (>250 mg/dL):**
1. ✅ Uống nhiều nước
2. ✅ Đo tiếp sau 2 giờ
3. ⚠️ Nếu vẫn cao → Gọi bác sĩ
4. 🚨 Nếu buồn nôn, đau bụng → GỌI 115

**Nếu 7-13 mmol/L (126-250):**
1. ✅ Vận động nhẹ 15 phút
2. ✅ Ăn ít carb bữa sau
3. ✅ Uống thuốc đúng giờ
4. 📝 Ghi lại để báo bác sĩ

**Phòng ngừa:**
- Ăn đúng giờ
- Đo đường thường xuyên
- Uống thuốc đủ liều
""",
        "ăn giảm huyết áp": """
🥗 **Ăn gì để giảm huyết áp:**

**✅ NÊN ĂN:**
- 🥬 Rau xanh (cải, rau ngót, rau muống)
- 🍌 Chuối (giàu kali - hạ huyết áp)
- 🥛 Sữa ít béo
- 🐟 Cá (omega-3 rất tốt)
- 🥔 Khoai lang luộc
- 🍊 Cam, quýt (vitamin C)

**🚫 TRÁNH:**
- Đồ MẶN (muối, mắm, tương)
- Đồ CHIÊN RÁN
- Đồ HỘP/ĐÓNG GÓI
- Rượu, bia

**Mẹo:**
Thay muối = Chanh + Gừng + Tỏi + Rau thơm
→ Vừa ngon vừa khỏe!
""",
        "gọi 115": """
🚨 **Khi nào GỌI CẤP CỨU 115:**

**TIM MẠCH:**
⛔ Đau ngực dữ dội
⛔ Khó thở nghiêm trọng
⛔ Huyết áp > 180/120

**THẦN KINH:**
⛔ Yếu liệt đột ngột
⛔ Méo mặt, nói khó
⛔ Đau đầu dữ dội

**TIỂU ĐƯỜNG:**
⛔ Đường > 22 mmol/L (400 mg/dL)
⛔ Hôn mê, co giật
⛔ Buồn nôn nhiều + đau bụng

**KHÁC:**
⛔ Ngất xỉu
⛔ Chảy máu không cầm được
⛔ Bất kỳ tình trạng NGHIÊM TRỌNG đột ngột

**⏰ ĐỪNG TRÌ HOÃN - Gọi ngay!**
Tốt hơn GỌI NHẦM còn hơn BỎ LỠ!
"""
    }
    
    return answers.get(question_type, "")

