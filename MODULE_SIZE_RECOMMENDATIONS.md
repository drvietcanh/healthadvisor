# 📏 KHUYẾN NGHỊ SỐ DÒNG HỢP LÝ CHO TỪNG LOẠI MODULE

**Cập nhật:** 03/01/2025  
**Mục đích:** Xác định số dòng tối ưu cho từng loại module trong HealthAdvisor

---

## 🎯 **NGUYÊN TẮC CHUNG**

### **Luật vàng (Từ QUY_TRINH_TACH_MODULE.md):**
- ✅ **Mỗi file ≤ 300 dòng** (tối đa 250 dòng là lý tưởng)
- ✅ **Tối thiểu ≥ 50 dòng** (tránh tách quá nhỏ - phản tác dụng)
- ✅ **Tách theo CHỨC NĂNG**, không tách theo số dòng đều nhau

### **Best Practices (Từ Python Community):**
- 📚 Module > 500 dòng → Nên tách
- 📚 Module 300-500 dòng → Theo dõi, tách khi cần
- 📚 Module < 300 dòng → OK (lý tưởng 150-250 dòng)

---

## 📊 **PHÂN LOẠI THEO TỪNG LOẠI MODULE**

### **1. 🔵 UI COMPONENTS (Streamlit Pages & Components)**

**Ví dụ:**
- `pages/4_🧠_Thần_Kinh.py`
- `respiratory_page_components/asthma_tab.py`
- `cardiovascular_page_components/*.py`

**Khuyến nghị:**
- ✅ **Lý tưởng: 100-200 dòng**
- ✅ **Chấp nhận được: 200-300 dòng**
- ⚠️ **Cần xem xét: 300-400 dòng**
- ❌ **Bắt buộc tách: > 400 dòng**

**Lý do:**
- UI thường dài do nhiều `st.markdown()`, `st.columns()`, `st.tabs()`
- Nhưng vẫn nên giữ < 300 dòng để dễ maintain
- Nếu > 400 dòng → Tách theo tabs hoặc sections

**Thực tế từ codebase:**
- `medication_reminder/` - ~172 dòng/file ✅ XUẤT SẮC
- `diary_components/` - ~156 dòng/file ✅ TỐT
- `pages/4_🧠_Thần_Kinh.py` - 418 dòng ❌ CẦN TÁCH

---

### **2. 🟢 LOGIC/UTILS (Business Logic, Utilities)**

**Ví dụ:**
- `core/chatbot_enhanced.py`
- `diseases/metabolic/dyslipidemia/framingham_calculator.py`
- `health_trends/analyzer.py`

**Khuyến nghị:**
- ✅ **Lý tưởng: 150-250 dòng**
- ✅ **Chấp nhận được: 250-300 dòng**
- ⚠️ **Cần xem xét: 300-350 dòng**
- ❌ **Bắt buộc tách: > 350 dòng**

**Lý do:**
- Logic code cần ngắn gọn, dễ test
- File dài → Khó debug, khó test
- Function/Class nên < 50 dòng mỗi cái

**Thực tế từ codebase:**
- `emergency_contacts/` - ~115 dòng/file ✅ TỐT
- `health_trends/analyzer.py` - 348 dòng ⚠️ THEO DÕI

---

### **3. 🟡 DATA/CONTENT (Data Structures, Content Data)**

**Ví dụ:**
- `emergency_contacts/first_aid_additional3.py` (570 dòng)
- `diseases/metabolic/dyslipidemia/nutrition/vietnamese_foods.py` (334 dòng)
- `health_tips/daily_tips.py` (467 dòng)

**Khuyến nghị:**
- ✅ **Lý tưởng: 200-300 dòng**
- ✅ **Chấp nhận được: 300-400 dòng** (đặc biệt cho data)
- ⚠️ **Cần xem xét: 400-500 dòng**
- ❌ **Bắt buộc tách: > 500 dòng**

**Lý do:**
- Data files thường dài do dictionaries/lists lớn
- Nhưng vẫn nên tách nếu > 500 dòng để dễ quản lý
- Tách theo nhóm logic (ví dụ: theo category, theo severity)

**Thực tế từ codebase:**
- `first_aid_additional3.py` - 570 dòng ❌ CẦN TÁCH NGAY
- `first_aid_additional4.py` - 512 dòng ❌ CẦN TÁCH NGAY
- `daily_tips.py` - 467 dòng ⚠️ NÊN TÁCH

---

### **4. ⚪ CSS/CONFIG (Configuration, Styling)**

**Ví dụ:**
- `core/dark_mode_css.py` (399 dòng)
- `core/light_mode_css.py` (382 dòng)
- `core/ui_config.py` (152 dòng)

**Khuyến nghị:**
- ✅ **Lý tưởng: 200-400 dòng** (CSS thường dài)
- ✅ **Chấp nhận được: 400-500 dòng**
- ⚠️ **Cần xem xét: > 500 dòng**
- ❌ **Giữ nguyên nếu: < 500 dòng** (CSS khó tách)

**Lý do:**
- CSS strings thường rất dài
- Tách CSS có thể làm phức tạp việc maintain
- Chấp nhận file CSS dài hơn một chút

**Thực tế từ codebase:**
- `dark_mode_css.py` - 399 dòng ✅ OK (CSS)
- `light_mode_css.py` - 382 dòng ✅ OK (CSS)

---

### **5. 🔴 INIT/EXPORT (__init__.py files)**

**Ví dụ:**
- `diseases/metabolic/__init__.py`
- `core/__init__.py`

**Khuyến nghị:**
- ✅ **Lý tưởng: 10-50 dòng**
- ✅ **Chấp nhận được: 50-100 dòng**
- ⚠️ **Cần xem xét: > 100 dòng**

**Lý do:**
- `__init__.py` chỉ nên chứa exports
- File dài → Quá nhiều imports/exports

---

## 📈 **THỐNG KÊ TỪ CODEBASE**

### **Modules đã refactor thành công:**

| Module | Số files | Trung bình | Kết quả |
|--------|----------|------------|---------|
| `medication_reminder/` | 4 | ~172 dòng/file | ✅ XUẤT SẮC |
| `diary_components/` | 5 | ~156 dòng/file | ✅ TỐT |
| `emergency_contacts/` | 4 | ~115 dòng/file | ✅ TỐT |
| `diabetes/nutrition/` | 3 | ~100 dòng/file | ✅ XUẤT SẮC |

**→ Kết luận: 100-200 dòng/file là LÝ TƯỞNG nhất!**

---

## 🎯 **KHUYẾN NGHỊ TỔNG HỢP**

### **Theo loại file:**

| Loại | Tối thiểu | Lý tưởng | Tối đa | Cảnh báo |
|------|-----------|----------|--------|----------|
| **UI Components** | 50 | 100-200 | 300 | > 400 |
| **Logic/Utils** | 50 | 150-250 | 300 | > 350 |
| **Data/Content** | 50 | 200-300 | 400 | > 500 |
| **CSS/Config** | 50 | 200-400 | 500 | > 600 |
| **__init__.py** | 1 | 10-50 | 100 | > 100 |

### **Theo độ ưu tiên tách:**

1. 🔴 **Tách NGAY:** > 500 dòng (mọi loại file, trừ CSS < 600)
2. 🟡 **Tách trong 1-2 tuần:** 400-500 dòng
3. 🟢 **Theo dõi:** 300-400 dòng
4. ⚪ **OK:** < 300 dòng (hoặc CSS < 500)

---

## 💡 **QUY TẮC THỰC HÀNH**

### **✅ KHI NÀO NÊN TÁCH:**
- File > 500 dòng (trừ CSS)
- File > 400 dòng (UI Components, Logic)
- File > 350 dòng (Logic/Utils - ưu tiên cao)
- File có > 10 functions/classes
- File quá phức tạp, khó đọc

### **❌ KHI NÀO KHÔNG NÊN TÁCH:**
- File < 300 dòng (trừ khi quá phức tạp)
- CSS files < 500 dòng (chấp nhận được)
- Data files < 400 dòng (nếu là pure data)
- File chỉ có 1-2 functions đơn giản

### **⚠️ NGOẠI LỆ:**
- **CSS files:** Chấp nhận đến 500 dòng
- **Pure data files (dicts/lists lớn):** Chấp nhận đến 400 dòng
- **Page files (Streamlit):** Chấp nhận đến 350 dòng nếu chỉ là UI

---

## 📝 **KẾT LUẬN**

### **Số dòng LÝ TƯỞNG cho HealthAdvisor:**

**🎯 MỤC TIÊU:**
- ✅ **Trung bình: 150-200 dòng/file**
- ✅ **Tối đa: 300 dòng/file** (cho mọi loại trừ CSS)
- ✅ **CSS: Tối đa 500 dòng/file**

**📊 HIỆN TRẠNG:**
- ✅ 85% files đã < 300 dòng
- ❌ 15% files (15 files) cần tách
- 🎯 Đang tiến tới mục tiêu 100% < 300 dòng

---

**Nguyên tắc vàng:** 
> **"Mỗi file chỉ làm MỘT việc, và làm tốt việc đó - trong vòng 300 dòng!"**

