"""
Everyday Examples - Ví dụ đời thường để giải thích bệnh
"""

EVERYDAY_EXAMPLES = {
    "blood_pressure": {
        "simple_vn": """
## 💓 Huyết áp là gì? (Giải thích như kể chuyện)

Tưởng tượng tim bạn là **cái bơm nước**:
- Mỗi lần tim đập = bơm đẩy nước (máu) vào ống (mạch máu)
- **Huyết áp** = **áp lực** của nước trong ống

### 📊 2 Con số huyết áp:

**Số trên (120)** = Áp lực khi tim ĐANG BƠM (co lại)
- Giống như bạn vặn vòi nước MẠNH

**Số dưới (80)** = Áp lực khi tim NGHỈ (giãn ra)  
- Giống như bạn vặn vòi nước NHẸ

### 🔴 Huyết áp cao = Gì?

**Ống nước (mạch máu) bị:**
- Hẹp lại (như ống bị vôi)
- Nước chảy khó → Áp lực tăng
- Tim phải bơm MẠNH HƠN
- Tim mệt → Hỏng sớm

**Giống như:**
- Bạn phải bóp bóng bay hơi bị xì → Mỏi tay!
- Máy bơm nước làm việc 24/7 → Hỏng nhanh!
""",
        "visual": """
┌─────────────────────────────────┐
│   TIM = BƠM NƯỚC               │
│                                 │
│   ♥️ → 💨💨 → 🩸🩸🩸 → 💪       │
│   Tim   Bơm    Máu    Cơ thể   │
│                                 │
│   Huyết áp BÌNH THƯỜNG:        │
│   Ống rộng ══════► Máu chảy dễ │
│                                 │
│   Huyết áp CAO:                │
│   Ống hẹp ═══► Máu chảy khó ⚠️  │
└─────────────────────────────────┘
"""
    },
    
    "diabetes": {
        "simple_vn": """
## 🍬 Tiểu đường là gì? (Giải thích bằng hình ảnh)

### Bình thường:
1. Ăn cơm/bánh → Thành **đường** trong máu
2. Tụy tiết ra **insulin** (chìa khóa 🔑)
3. Insulin MỞ CỬA tế bào
4. Đường VÀO tế bào → Làm năng lượng ⚡

```
Cơm 🍚 → Đường 🍬 → Insulin 🔑 → Tế bào 🏠
                        MỞ CỬA ✓
         Đường vào nhà → Năng lượng ⚡
```

### Tiểu đường:
**Vấn đề:** Không có chìa khóa hoặc chìa khóa HỎNG!

```
Cơm 🍚 → Đường 🍬 → Không có 🔑 → Tế bào 🏠
                                  Cửa ĐÓNG ✗
         Đường ĐỨNG NGOÀI → Tích trong máu 📈
```

**Kết quả:**
- Đường tích trong máu → Cao
- Tế bào không có đường → Đói
- Cơ thể mệt, không có năng lượng

**Giống như:**
- Có nhiều tiền (đường) nhưng quên chìa khóa → Vào nhà không được!
- Đứng ngoài cửa với túi đồ ăn → Đói mà không ăn được!
""",
        "visual": """
┌────────────────────────────────┐
│ BÌNH THƯỜNG vs TIỂU ĐƯỜNG     │
│                                │
│ Bình thường:                   │
│ 🍚 → 🍬 → 🔑 → 🏠[OPEN] → ⚡   │
│              Vào được!         │
│                                │
│ Tiểu đường:                    │
│ 🍚 → 🍬 → ❌ → 🏠[LOCKED] → 😫 │
│         Không có chìa!         │
│         Đường tích ngoài 📈    │
└────────────────────────────────┘
"""
    },
    
    "heart_failure": {
        "simple_vn": """
## 💔 Suy tim là gì? (Ví dụ dễ hiểu)

**Suy tim ≠ Tim ngừng đập!**

Suy tim = Tim **YẾU**, bơm **KHÔNG ĐỦ MẠNH**

### So sánh:

**Tim khỏe** = Bơm nước mới, mạnh mẽ
```
Bơm 💪 → Nước phun xa 💦💦💦 → Tưới được cả vườn 🌳
```

**Tim suy** = Bơm nước cũ, yếu
```
Bơm 😔 → Nước rỉ rả 💧 → Chỉ tưới được gốc cây 🌱
```

### Điều gì xảy ra?

1. **Tim bơm yếu** → Máu đến cơ thể ít
2. **Máu ứ lại** → Phù chân, phù phổi
3. **Cơ thể thiếu máu** → Mệt, khó thở

**Giống như:**
- Điện thoại pin yếu → Sạc hoài không đủ dùng
- Quạt cũ → Quay chậm, gió nhỏ
- Xe máy yếu → Leo dốc khó, chạy chậm
""",
        "visual": """
┌─────────────────────────────┐
│   TIM KHỎE vs TIM SUY      │
│                             │
│ Tim khỏe:                   │
│ ❤️💪 → 💨💨💨 → Cơ thể tràn │
│         Bơm mạnh   năng lượng│
│                             │
│ Tim suy:                    │
│ 💔😔 → 💧 → Cơ thể mệt 😴   │
│       Bơm yếu               │
│       + Máu ứ → Phù 🦶      │
└─────────────────────────────┘
"""
    },
    
    "stroke": {
        "simple_vn": """
## 🧠 Đột quỵ là gì? (Giải thích đơn giản)

**Đột quỵ = "Cơn đau tim" của NÃO**

Não cũng cần máu nuôi, giống như tim!

### 2 loại:

**1. Đột quỵ THIẾU MÁU (80%)** = Ống tắc
```
Mạch máu não → Bị cục máu đông TẮC 🚫
→ Máu không lên não
→ Não thiếu oxy → Tế bào não CHẾT
```
**Giống như:** Ống nước tắc → Cây khô

**2. Đột quỵ CHẢY MÁU (20%)** = Ống vỡ
```
Mạch máu não → VỠ 💥
→ Máu chảy tràn lan
→ Não bị ÉP → Tế bào não CHẾT
```
**Giống như:** Ống nước vỡ → Ngập nhà

### ⏰ TẠI SAO PHẢI NHANH?

**Mỗi phút trì hoãn = 2 TRIỆU tế bào não chết!**

```
Thời gian = Não
Time = Brain

Trong 4.5 giờ → Tiêm thuốc tan cục máu đông
Trong 24 giờ → Lấy cục máu đông ra

Càng sớm = Não càng sống
```

**Giống như:**
- Cháy nhà → Gọi 114 NGAY (không đợi cháy hết mới gọi!)
- Vòi nước vỡ → Tắt van NGAY (không đợi ngập nhà!)
"""
    }
}

