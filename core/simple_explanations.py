"""
Giải thích CỰC KỲ ĐƠN GIẢN - Ai cũng hiểu!
Dùng ví dụ đời thường, hình ảnh, so sánh
"""

# ============= VÍ DỤ ĐỜI THƯỜNG =============

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

# ============= MẸO NHỚ DỄ =============

MEMORY_TRICKS = {
    "befast_easy": """
## 🎯 CÁCH NHỚ BE-FAST (Siêu dễ!)

Nhớ câu: **"Bé Ế, Phải Áp, Sợ Thời gian"**

**B**é = **B**alance (Mất thăng bằng)
**Ế** = **E**yes (Mắt - nhìn mờ) 
**F**ải = **F**ace (Mặt - xệ méo)
**Á**p = **A**rm (Áp tay - yếu liệt)
**S**ợ = **S**peech (Sợ nói - nói khó)
**T**hời gian = **T**ime (Gọi 115!)

### Test nhanh 10 giây:

1. **Cười** → Lệch miệng? ✗
2. **Giơ 2 tay** → 1 tay sa? ✗
3. **Nói 1 câu** → Nói khó? ✗

→ CÓ 1 dấu hiệu = GỌI 115!
""",
    
    "blood_sugar_levels": """
## 📊 CÁCH NHỚ ĐƯỜNG HUYẾT (Dễ ợt!)

### Quy tắc **5-7-10** (mmol/L):

**< 5.6** = **5** ✅ Bình thường (vui vẻ)
**5.6-6.9** = **6** ⚠️ Tiền tiểu đường (cẩn thận!)  
**≥ 7.0** = **7** 🔴 Tiểu đường (nguy hiểm!)

### Sau ăn 2h:

**< 7.8** = **8** ✅ OK
**> 11** = **11** 🔴 Cao!

### Nhớ nhanh:

**Đói:** Nhớ số **5-6-7** (tăng dần = xấu dần)
**No:** Nhớ số **8** và **11**

**Mẹo:** Số càng cao = Càng nguy hiểm!
""",
    
    "salt_reduction": """
## 🧂 CÁCH GIẢM MUỐI (Mẹo hay!)

### Quy tắc 3 KHÔNG:

❌ **KHÔNG** muối/mắm/tương trên bàn ăn
❌ **KHÔNG** đồ hộp/đóng gói
❌ **KHÔNG** ăn ngoài quá 3 lần/tuần

### Thay thế 3 CÓ:

✅ **CÓ** chanh/giấm/gừng
✅ **CÓ** rau thơm (ngò, rau răm)
✅ **CÓ** tỏi/hành/ớt (ít)

### Mẹo kiểm tra:

**Lưỡi bạn = Máy đo muối!**
- Ăn mà thấy MẶN = Quá nhiều muối!
- Ăn mà thấy VỪA = OK!
- Nhạt 3 ngày → Quen!
"""
}

# ============= SO SÁNH DỄ HIỂU =============

COMPARISONS = {
    "medications_simple": {
        "title": "Thuốc giống như gì?",
        "examples": [
            {
                "drug": "Thuốc lợi tiểu",
                "like": "Như MỞ VÒI NƯỚC",
                "explain": "Giúp cơ thể đào thải nước ra ngoài → Giảm áp lực",
                "emoji": "🚰💧"
            },
            {
                "drug": "Thuốc giãn mạch",
                "like": "Như MỞ RỘNG ỐNG NƯỚC",
                "explain": "Mạch máu giãn → Máu chảy dễ → Tim bớt vất vả",
                "emoji": "🔧📏"
            },
            {
                "drug": "Insulin",
                "like": "Như CHÌA KHÓA MỞ CỬA",
                "explain": "Mở cửa tế bào → Đường vào được → Giảm đường máu",
                "emoji": "🔑🚪"
            },
            {
                "drug": "Thuốc chống đông",
                "like": "Như CHO NƯỚC SÔI THÊM CHÚT ĐÁ",
                "explain": "Máu loãng hơn → Không đông cục → Giảm nguy cơ tắc mạch",
                "emoji": "🧊💉"
            }
        ]
    },
    
    "portion_sizes": {
        "title": "Khẩu phần ăn = So với đồ vật",
        "examples": [
            "🍚 Cơm: 1 nắm tay CỤP = 1 khẩu phần",
            "🍗 Thịt/cá: Bằng 1 BỘ BÀI = 100g",
            "🥗 Rau: 2 nắm tay = Ăn thoải mái",
            "🍎 Trái cây: 1 QUẢ NẮM TAY vừa = 1 khẩu phần",
            "🥜 Hạt: 1 NẮM TAY NHỎ = 30g (đủ!)",
            "🧈 Dầu: 1 NGÓN CVCÁI = 1 thìa",
            "🧂 Muối: Đầu NGÓN CVCÁI = 1/4 thìa (cả ngày!)"
        ]
    }
}

# ============= CÔNG CỤ SO SÁNH =============

def compare_to_daily_items(medical_value: float, value_type: str) -> str:
    """So sánh giá trị y tế với đồ vật hàng ngày"""
    
    comparisons_map = {
        "blood_pressure_high": {
            "120": "Như áp lực 1 cái BƠM TAY bóng đá 🏀",
            "140": "Như áp lực BƠM HƠI xe đạp 🚲",
            "160": "Như áp lực BƠM HƠI xe máy 🏍️",
            "180": "Như áp lực NỒI ÁP SUẤT đang sôi 🍲⚠️"
        },
        "blood_sugar_mgdl": {
            "100": "1 thìa cà phê đường = Bình thường ✅",
            "150": "1.5 thìa đường = Hơi cao ⚠️",
            "200": "2 thìa đường = Cao 🔴",
            "300": "3 thìa đường = Rất cao 🚨"
        },
        "salt_grams": {
            "1": "1/5 thìa cà phê = Rất ít ✅",
            "3": "3/5 thìa cà phê = Giới hạn người THA ⚠️",
            "5": "1 thìa cà phê = Giới hạn người bình thường",
            "10": "2 thìa cà phê = QUÁ NHIỀU! 🚫"
        }
    }
    
    return comparisons_map.get(value_type, {})

