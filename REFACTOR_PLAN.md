# 🔧 KẾ HOẠCH REFACTOR - GIẢM KHỔ FILE QUÁ DÀI

**Ngày:** 30/10/2025  
**Quy tắc:** MAX 300 dòng/file  
**Trạng thái:** 9/29 files CẦN refactor!

---

## 🔴 ƯU TIÊN CAO (> 500 dòng - NGUY HIỂM!)

### 1. `pages/6_📊_Nhật_Ký.py` - **1070 dòng** ⚠️ CỰC KỲ NGUY HIỂM!

**Phương án:** Tách thành 4 module nhỏ

```
pages/
├── 6_📊_Nhật_Ký.py (Main - 200 dòng)
│   ├── Điều hướng tabs
│   ├── Upload/Download CSV
│   └── Tích hợp các module con
│
└── diary_components/
    ├── __init__.py
    ├── input_form.py (250 dòng)
    │   ├── Form nhập huyết áp, đường huyết
    │   ├── Form nhập xét nghiệm (HbA1c, mỡ máu...)
    │   └── Validation
    │
    ├── charts.py (250 dòng)
    │   ├── Biểu đồ huyết áp
    │   ├── Biểu đồ đường huyết
    │   ├── Biểu đồ cân nặng
    │   └── Thống kê
    │
    ├── instructions.py (300 dòng)
    │   ├── Hướng dẫn đo huyết áp
    │   ├── Hướng dẫn lưu/tải file
    │   └── Mẹo sử dụng
    │
    └── data_manager.py (70 dòng)
        ├── Load CSV
        ├── Save CSV
        └── Data validation
```

**Lợi ích:**
- ✅ 1070 dòng → 4 files < 300 dòng
- ✅ Dễ maintain, debug
- ✅ Code reusable

---

### 2. `diseases/metabolic/diabetes/nutrition.py` - **672 dòng**

**Phương án:** Tách thành 3 module

```
diseases/metabolic/diabetes/
├── nutrition/
│   ├── __init__.py
│   ├── basics.py (200 dòng)
│   │   ├── Nguyên tắc cơ bản
│   │   ├── Đếm carb
│   │   └── Phương pháp đĩa ăn
│   │
│   ├── glycemic.py (250 dòng)
│   │   ├── GI & GL giải thích
│   │   ├── Bảng GI/GL thực phẩm VN (60+ món)
│   │   └── So sánh, ví dụ thực tế
│   │
│   └── recommendations.py (222 dòng)
│       ├── Thực phẩm nên ăn
│       ├── Thực phẩm tránh
│       └── Thực đơn mẫu
```

**Lợi ích:**
- ✅ Logic rõ ràng
- ✅ Dễ thêm thực phẩm mới
- ✅ Import dễ dàng

---

### 3. `diseases/cardiovascular/hypertension.py` - **609 dòng**

**Phương án:** Tách thành module

```
diseases/cardiovascular/hypertension/
├── __init__.py (Export all)
├── info.py (150 dòng)
│   ├── Định nghĩa
│   ├── Phân loại
│   └── Triệu chứng
│
├── medications.py (300 dòng)
│   ├── 5 nhóm thuốc
│   ├── Tên VN brands
│   ├── Tác dụng phụ
│   └── Thuốc phối hợp
│
└── lifestyle.py (159 dòng)
    ├── Dinh dưỡng DASH
    ├── Giảm muối
    └── Vận động
```

---

### 4. `diseases/cardiovascular/heart_failure.py` - **597 dòng**

**Phương án:** Tương tự hypertension

```
diseases/cardiovascular/heart_failure/
├── __init__.py
├── info.py (200 dòng)
├── medications.py (250 dòng)
└── management.py (147 dòng)
```

---

## 🟡 ƯU TIÊN TRUNG BÌNH (300-500 dòng)

### 5. `core/chatbot_enhanced.py` - **396 dòng**

**Phương án:** Tách logic AI & prompts

```
core/
├── chatbot/
│   ├── __init__.py
│   ├── base.py (150 dòng) - Base chatbot class
│   ├── gemini_handler.py (100 dòng) - Gemini integration
│   ├── openai_handler.py (100 dòng) - OpenAI integration
│   └── context_manager.py (46 dòng) - Manage conversation context
```

---

### 6. `pages/0_📖_Hướng_Dẫn.py` - **393 dòng**

**Phương án:** Tách nội dung hướng dẫn

```
pages/
├── 0_📖_Hướng_Dẫn.py (Main - 100 dòng)
└── guide_content/
    ├── __init__.py
    ├── quickstart.py (100 dòng)
    ├── detailed_guide.py (100 dòng)
    ├── faq.py (50 dòng)
    └── tips.py (43 dòng)
```

---

### 7. `core/ui_config.py` - **388 dòng**

**Phương án:** Tách CSS Light/Dark

```
core/ui/
├── __init__.py
├── config.py (50 dòng) - Main config
├── dark_mode.py (169 dòng) - Dark CSS
├── light_mode.py (169 dòng) - Light CSS
└── animations.py (50 dòng) - CSS animations
```

---

### 8. `core/simple_explanations.py` - **341 dòng**

**Phương án:** Tách theo loại giải thích

```
core/education/
├── __init__.py
├── everyday_examples.py (150 dòng)
├── memory_tricks.py (100 dòng)
└── comparisons.py (91 dòng)
```

---

### 9. `pages/5_🎓_Học_Dễ.py` - **319 dòng**

**Phương án:** OK, gần giới hạn nhưng chấp nhận được  
**Hành động:** Giữ nguyên (KHÔNG refactor ngay)

---

## 📋 KẾ HOẠCH THỰC HIỆN

### **Giai đoạn 1: NGUY HIỂM (Làm NGAY!) - 2-3 giờ**

✅ **Bước 1:** Refactor `Nhật_Ký.py` (1070 → 4 files < 300)
- Priority: ⭐⭐⭐⭐⭐ CRITICAL!
- Impact: 🔥🔥🔥🔥🔥
- Effort: ⏱️⏱️⏱️

✅ **Bước 2:** Refactor `nutrition.py` (672 → 3 files)
- Priority: ⭐⭐⭐⭐⭐
- Impact: 🔥🔥🔥🔥
- Effort: ⏱️⏱️

✅ **Bước 3:** Refactor `hypertension.py` (609 → 3 files)
- Priority: ⭐⭐⭐⭐
- Impact: 🔥🔥🔥🔥
- Effort: ⏱️⏱️

✅ **Bước 4:** Refactor `heart_failure.py` (597 → 3 files)
- Priority: ⭐⭐⭐⭐
- Impact: 🔥🔥🔥🔥
- Effort: ⏱️⏱️

---

### **Giai đoạn 2: TRUNG BÌNH (Sau vài ngày) - 2 giờ**

- [ ] Refactor `chatbot_enhanced.py`
- [ ] Refactor `Hướng_Dẫn.py`
- [ ] Refactor `ui_config.py`
- [ ] Refactor `simple_explanations.py`

---

### **Giai đoạn 3: GIÁM SÁT (Ongoing)**

Các file 200-300 dòng (CẢNH BÁO):
- `AI_Bác_Sĩ.py` - 279 dòng (OK, giữ nguyên)
- `Thần_Kinh.py` - 249 dòng (OK)
- `models.py` - 241 dòng (OK)
- `rules.py` - 229 dòng (OK)
- `app.py` - 220 dòng (OK)

→ **KHÔNG cần refactor ngay**, chỉ giám sát khi thêm code mới!

---

## 🎯 MỤC TIÊU

**Hiện tại:**
- 9/29 files > 300 dòng (31%)
- File lớn nhất: 1070 dòng

**Sau refactor:**
- 0/~40 files > 300 dòng (0%)
- File lớn nhất: < 300 dòng

---

## 💡 NGUYÊN TẮC REFACTOR

### ✅ NÊN:
- Tách theo chức năng logic rõ ràng
- Mỗi file = 1 responsibility
- Tên file rõ nghĩa (descriptive)
- Export qua `__init__.py` để import đơn giản
- Test sau khi refactor

### ❌ TRÁNH:
- Tách quá nhỏ (< 50 dòng/file) - phản tác dụng
- Tách giữa chừng function/class
- Import circular
- Duplicate code

---

## 📊 TRACKING PROGRESS

| File | Dòng hiện tại | Mục tiêu | Status | ETA |
|------|--------------|----------|--------|-----|
| Nhật_Ký.py | 1070 | 4 files < 300 | 🔴 TODO | 1h |
| nutrition.py | 672 | 3 files < 300 | 🔴 TODO | 30m |
| hypertension.py | 609 | 3 files < 300 | 🔴 TODO | 30m |
| heart_failure.py | 597 | 3 files < 300 | 🔴 TODO | 30m |
| chatbot_enhanced.py | 396 | 4 files < 150 | 🟡 LATER | 30m |
| Hướng_Dẫn.py | 393 | 5 files < 100 | 🟡 LATER | 20m |
| ui_config.py | 388 | 4 files < 170 | 🟡 LATER | 20m |
| simple_explanations.py | 341 | 3 files < 150 | 🟡 LATER | 20m |
| Học_Dễ.py | 319 | KEEP (OK) | ✅ OK | - |

---

## 🚀 BẮTĐẦU NGAY?

**Câu hỏi cho user:**
> Bạn muốn tôi bắt đầu refactor từ file nào?
> 
> **Đề xuất:** Bắt đầu từ **Nhật_Ký.py** (1070 dòng - nguy hiểm nhất!)

---

**Updated:** 30/10/2025  
**Next review:** Sau khi hoàn thành Giai đoạn 1

