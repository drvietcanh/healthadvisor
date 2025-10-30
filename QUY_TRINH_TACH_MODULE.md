# 📚 QUY TRÌNH TÁCH MODULE TỐI ƯU

**Mục đích:** Tách file Python lớn (>300 dòng) thành các module nhỏ dễ quản lý  
**Áp dụng:** Streamlit apps, Django, FastAPI, hoặc bất kỳ Python project nào  
**Ngôn ngữ:** Dễ hiểu, giọng bình dân

---

## 🎯 MỤC TIÊU

- **Mỗi file ≤ 300 dòng** (tối đa 250 dòng là lý tưởng)
- **Không làm hỏng code đang chạy tốt**
- **Tách nhanh, ít sai sót**
- **Dễ maintain sau này**

---

## 📋 QUY TRÌNH 6 BƯỚC

### **BƯỚC 1: NGHIÊN CỨU KỸ FILE GỐC** 🔍

**Mục đích:** Hiểu rõ file trước khi tách

**Làm gì:**

1. **Đọc file từ đầu đến cuối** (quan trọng!)
   ```bash
   # Đếm số dòng
   wc -l <file.py>
   
   # Hoặc dùng Python
   python -c "print(sum(1 for _ in open('<file.py>', encoding='utf-8')))"
   ```

2. **Vẽ sơ đồ cấu trúc** trên giấy hoặc ghi chú:
   ```
   Ví dụ:
   
   file.py (732 dòng)
   ├── Imports & Setup (dòng 1-50)
   ├── Tab 1: Overview (dòng 51-160)  → ~110 dòng
   ├── Tab 2: Calculator (dòng 161-350) → ~190 dòng
   ├── Tab 3: Results (dòng 351-500)   → ~150 dòng
   ├── Tab 4: Export (dòng 501-650)    → ~150 dòng
   └── Footer (dòng 651-732)           → ~80 dòng
   ```

3. **Liệt kê IMPORTS:**
   ```python
   # Tìm tất cả imports
   import streamlit as st          # ← Tất cả files cần
   import pandas as pd             # ← Chỉ Tab 2, 4 cần
   from mymodule import func1      # ← Chỉ Tab 1 cần
   ```

4. **Tìm SESSION STATE:**
   ```python
   # Tìm tất cả st.session_state
   st.session_state['user_data']   # ← Tab 2 set, Tab 3 dùng
   st.session_state['results']     # ← Tab 3 set, Tab 4 dùng
   ```

5. **Tìm HARDCODED PATHS:**
   ```python
   sys.path.insert(0, '../..')     # ← Cần sửa!
   ```

**Checklist:**
- [ ] Đã đọc toàn bộ file
- [ ] Đã vẽ sơ đồ cấu trúc
- [ ] Đã liệt kê imports
- [ ] Đã liệt kê session state keys
- [ ] Đã tìm hardcoded paths

---

### **BƯỚC 2: LẬP KẾ HOẠCH TÁCH** 📝

**Mục đích:** Quyết định tách thành bao nhiêu files, tên files là gì

**Nguyên tắc tách:**

1. **Theo CHỨC NĂNG:**
   ```
   ❌ SAI: Tách theo số dòng đều nhau
   ✅ ĐÚNG: Tách theo logic rõ ràng
   
   Ví dụ:
   - overview.py    → Giới thiệu tổng quan
   - calculator.py  → Tính toán
   - results.py     → Hiển thị kết quả
   - export.py      → Xuất file
   ```

2. **Theo TABS (nếu là Streamlit):**
   ```python
   # File gốc có 5 tabs → Tách thành 5 files
   tab1, tab2, tab3, tab4, tab5 = st.tabs([...])
   
   with tab1:  → overview.py
   with tab2:  → assessment.py
   with tab3:  → diseases.py
   ...
   ```

3. **Theo DICTIONARY lớn (nếu là data file):**
   ```python
   # File info.py có 3 phần lớn
   DISEASE_INFO = {
       "definition": {...},      → basic_info.py
       "symptoms": {...},        → symptoms.py
       "complications": {...}    → complications.py
   }
   ```

**Đặt tên files:**

✅ **TỐT:**
- `overview.py`, `assessment.py`, `calculator.py`
- `basic_info.py`, `symptoms.py`, `diagnosis.py`
- `dark_mode_css.py`, `light_mode_css.py`

❌ **TRÁNH:**
- `utils.py`, `helpers.py`, `misc.py` (quá chung chung)
- `part1.py`, `part2.py` (không rõ nghĩa)
- `new.py`, `temp.py` (tạm bợ)

**Checklist:**
- [ ] Đã quyết định số lượng files (2-6 files là hợp lý)
- [ ] Đã đặt tên rõ ràng cho từng file
- [ ] Mỗi file dự kiến ≤ 300 dòng
- [ ] Logic được tách rõ ràng, không chồng chéo

---

### **BƯỚC 3: TẠO THỦ CÔNG 1 COMPONENT THỬ** ✍️

**Mục đích:** Test quy trình với 1 file trước khi làm hàng loạt

**Làm gì:**

1. **Tạo thư mục components:**
   ```bash
   mkdir <tên>_components
   ```

2. **Tạo file đầu tiên (component nhỏ nhất):**
   ```python
   # Ví dụ: overview.py
   """
   Tab Tổng Quan
   """
   import streamlit as st
   # ... imports khác cần thiết
   
   def render_overview_tab():
       """Hiển thị tab tổng quan"""
       # Copy code từ file gốc dòng 51-160
       st.header("Tổng Quan")
       # ... code ...
   ```

3. **Copy code CHÍNH XÁC:**
   - Copy nguyên xi từ file gốc
   - GIỮ NGUYÊN indent
   - GIỮ NGUYÊN logic
   - KHÔNG sửa gì cả!

4. **Thêm imports cần thiết:**
   ```python
   # Chỉ import những gì cần
   import streamlit as st           # ← Luôn cần
   from diseases.metabolic import obesity  # ← Nếu dùng
   ```

5. **Test riêng file này:**
   ```python
   # Tạo file test_overview.py
   import sys
   sys.path.insert(0, '..')
   from metabolic_components.overview import render_overview_tab
   
   render_overview_tab()
   ```

**Checklist:**
- [ ] File component đã tạo
- [ ] Code đã copy chính xác
- [ ] Imports đã thêm đủ
- [ ] Đã test import (không bị lỗi)

---

### **BƯỚC 4: TẠO CÁC COMPONENTS CÒN LẠI** 🔄

**Mục đích:** Nhân bản quy trình cho các components khác

**Làm gì:**

1. **Tạo từng file một, TEST ngay:**
   ```bash
   # KHÔNG tạo hết rồi mới test!
   
   ✅ ĐÚNG:
   - Tạo file 1 → Test → OK
   - Tạo file 2 → Test → OK
   - Tạo file 3 → Test → OK
   
   ❌ SAI:
   - Tạo file 1, 2, 3, 4, 5
   - Test tất cả → Lỗi ở đâu không biết!
   ```

2. **Dùng template:**
   ```python
   """
   <Mô tả ngắn gọn>
   """
   import streamlit as st
   # imports khác...
   
   def render_<tên>_tab():
       """Docstring mô tả hàm"""
       # Code từ file gốc
       pass
   ```

3. **Tạo `__init__.py`:**
   ```python
   """
   <Tên Module> Components
   
   Tách từ <file gốc> để dễ quản lý
   """
   
   from .overview import render_overview_tab
   from .assessment import render_assessment_tab
   # ... các imports khác
   
   __all__ = [
       'render_overview_tab',
       'render_assessment_tab',
       # ... các exports khác
   ]
   ```

**Checklist:**
- [ ] Tất cả component files đã tạo
- [ ] Mỗi file có docstring rõ ràng
- [ ] `__init__.py` đã export đủ functions
- [ ] Mỗi file đã test imports

---

### **BƯỚC 5: TẠO FILE MAIN MỚI** 🏗️

**Mục đích:** File chính gọi các components

**2 Cách làm:**

#### **Cách 1: Tạo file mới, giữ file cũ** (AN TOÀN hơn)

```python
# Tạo: pages/4_NEW_Hội_Chứng_Chuyển_Hóa.py

import streamlit as st
import sys
import os

# Setup paths
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

# Import components
from metabolic_components import (
    render_overview_tab,
    render_assessment_tab,
    render_diseases_tab,
    render_calories_tab,
    render_goals_tab
)
from core.ui_config import get_custom_css

# Page config
st.set_page_config(
    page_title="Hội Chứng Chuyển Hóa",
    page_icon="⚖️",
    layout="wide"
)

# Apply CSS
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)

# Title
st.title("⚖️ Hội Chứng Chuyển Hóa & Quản Lý Cân Nặng")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Tổng Quan",
    "⚖️ Béo Phì & Đánh Giá",
    "🔗 Bệnh Liên Quan",
    "🍽️ Calories & Vận Động",
    "🎯 Mục Tiêu & Kế Hoạch"
])

with tab1:
    render_overview_tab()

with tab2:
    render_assessment_tab()

with tab3:
    render_diseases_tab()

with tab4:
    render_calories_tab()

with tab5:
    render_goals_tab()

# Footer
st.markdown("---")
st.caption("💡 Thông tin chỉ mang tính tham khảo...")
```

#### **Cách 2: Sửa file cũ trực tiếp** (NHANH hơn nhưng rủi ro)

```bash
# Backup file cũ trước
cp pages/4_file.py pages/4_file.py.backup

# Sửa file cũ
# Xóa hết code cũ, thay bằng code mới như Cách 1
```

**Checklist:**
- [ ] File main đã tạo/sửa
- [ ] Imports đầy đủ
- [ ] Page config giống y hệt file cũ
- [ ] Tabs structure giống file cũ
- [ ] Gọi đúng thứ tự các render functions

---

### **BƯỚC 6: TEST TOÀN BỘ & COMMIT** ✅

**Mục đích:** Đảm bảo mọi thứ hoạt động, không bị lỗi

**Test kỹ lưỡng:**

1. **Chạy app:**
   ```bash
   streamlit run pages/4_NEW_Hội_Chứng_Chuyển_Hóa.py
   ```

2. **Test TỪNG TAB:**
   - [ ] Tab 1: Click vào, xem có lỗi không
   - [ ] Tab 2: Click vào, nhập form, bấm nút
   - [ ] Tab 3: Click vào, xem expanders
   - [ ] Tab 4: Click vào, test search, calculator
   - [ ] Tab 5: Click vào, test tạo mục tiêu

3. **Test SESSION STATE:**
   - [ ] Tạo mục tiêu ở Tab 5 → Chuyển tab khác → Quay lại → Còn không?
   - [ ] Nhập form ở Tab 2 → Xem kết quả → OK?

4. **So sánh với file cũ:**
   ```bash
   # Chạy file cũ và file mới cạnh nhau
   # So sánh UI, chức năng
   ```

5. **Kiểm tra linter:**
   ```bash
   # Nếu có pylint, flake8
   pylint metabolic_components/*.py
   ```

6. **Đếm dòng:**
   ```bash
   wc -l metabolic_components/*.py
   
   # Kết quả mong đợi: Tất cả <300 dòng
   ```

**Commit:**

```bash
# 1. Xóa file cũ (nếu chắc chắn OK)
git rm pages/4_Hội_Chứng_Chuyển_Hóa.py

# 2. Thêm files mới
git add metabolic_components/
git add pages/4_NEW_Hội_Chứng_Chuyển_Hóa.py

# 3. Commit với message rõ ràng
git commit -m "refactor: Tách 4_Hội_Chứng_Chuyển_Hóa.py (732 dòng) thành 5 components

- Tạo metabolic_components/ với 5 files (~150 dòng/file)
- File main còn 50 dòng
- Tested: Tất cả tabs hoạt động OK
- No breaking changes"

# 4. Push
git push
```

**Checklist:**
- [ ] App chạy không lỗi
- [ ] Tất cả tabs hoạt động
- [ ] Session state OK
- [ ] UI giống y hệt file cũ
- [ ] Linter không có errors
- [ ] Tất cả files ≤300 dòng
- [ ] Đã commit với message rõ ràng
- [ ] Đã push lên GitHub

---

## 🎓 CÁC TRƯỜNG HỢP ĐẶC BIỆT

### **Case 1: File chỉ có DICTIONARIES (info.py)**

**Ví dụ:**
```python
# diseases/copd/info.py (546 dòng)
COPD_INFO = {
    "definition": {...},      # 150 dòng
    "symptoms": {...},        # 150 dòng
    "diagnosis": {...},       # 150 dòng
    "complications": {...}    # 100 dòng
}
```

**Cách tách:**
```python
# basic_info.py
COPD_DEFINITION = {...}
COPD_STATISTICS = {...}

# symptoms.py
COPD_SYMPTOMS = {...}
COPD_DIAGNOSIS = {...}

# complications.py
COPD_COMPLICATIONS = {...}
COPD_PREVENTION = {...}

# __init__.py
from .basic_info import COPD_DEFINITION, COPD_STATISTICS
from .symptoms import COPD_SYMPTOMS, COPD_DIAGNOSIS
from .complications import COPD_COMPLICATIONS, COPD_PREVENTION

COPD_INFO = {
    "definition": COPD_DEFINITION,
    "statistics": COPD_STATISTICS,
    "symptoms": COPD_SYMPTOMS,
    "diagnosis": COPD_DIAGNOSIS,
    "complications": COPD_COMPLICATIONS,
    "prevention": COPD_PREVENTION
}
```

---

### **Case 2: File CSS (ui_config.py)**

**Ví dụ:**
```python
# core/ui_config.py (730 dòng)
def get_custom_css(dark_mode=False):
    if dark_mode:
        return DARK_MODE_CSS  # 350 dòng
    else:
        return LIGHT_MODE_CSS  # 350 dòng
```

**Cách tách:**
```python
# dark_mode_css.py
DARK_MODE_CSS = """
<style>
...
</style>
"""

# light_mode_css.py
LIGHT_MODE_CSS = """
<style>
...
</style>
"""

# ui_config.py (30 dòng)
from .dark_mode_css import DARK_MODE_CSS
from .light_mode_css import LIGHT_MODE_CSS

def get_custom_css(dark_mode=False):
    return DARK_MODE_CSS if dark_mode else LIGHT_MODE_CSS
```

---

### **Case 3: File có nhiều FUNCTIONS (calculator.py)**

**Ví dụ:**
```python
# risk_calculator.py (513 dòng)
def calculate_risk(...):        # 200 dòng
def get_recommendations(...):   # 200 dòng
def generate_report(...):       # 100 dòng
```

**Cách tách:**
```python
# calculator.py (250 dòng)
def calculate_risk(...):
    ...

def _helper_function(...):
    ...

# recommendations.py (250 dòng)
def get_recommendations(...):
    ...

def generate_report(...):
    ...

# __init__.py
from .calculator import calculate_risk
from .recommendations import get_recommendations, generate_report

__all__ = ['calculate_risk', 'get_recommendations', 'generate_report']
```

---

## ⚠️ LỖI THƯỜNG GẶP & CÁCH TRÁNH

### **Lỗi 1: Import Error**

```python
# ❌ SAI
from overview import render_overview_tab  # ModuleNotFoundError!

# ✅ ĐÚNG
from metabolic_components.overview import render_overview_tab
# HOẶC
from metabolic_components import render_overview_tab
```

**Cách tránh:** Test import ngay sau khi tạo file

---

### **Lỗi 2: Circular Import**

```python
# ❌ SAI
# overview.py
from .assessment import calculate_bmi

# assessment.py
from .overview import show_intro  # ← Lỗi vòng tròn!
```

**Cách tránh:** Các components KHÔNG import lẫn nhau, chỉ import từ `diseases.metabolic.obesity`

---

### **Lỗi 3: Session State Conflict**

```python
# ❌ SAI
# overview.py
st.session_state['data'] = 123

# assessment.py
st.session_state['data'] = 456  # ← Đè lên!
```

**Cách tránh:** Dùng prefix rõ ràng:
```python
st.session_state['overview_data'] = 123
st.session_state['assessment_data'] = 456
```

---

### **Lỗi 4: Quên Export trong `__init__.py`**

```python
# ❌ SAI
# __init__.py chỉ có:
from .overview import render_overview_tab

# Khi dùng:
from metabolic_components import render_assessment_tab  # ← Lỗi!
```

**Cách tránh:** Luôn update `__all__` trong `__init__.py`

---

## 📊 CHECKLIST TỔNG HỢP

### Trước khi bắt đầu:
- [ ] Đã đọc toàn bộ file gốc
- [ ] Đã vẽ sơ đồ cấu trúc
- [ ] Đã lập kế hoạch tách (số files, tên files)
- [ ] Đã backup file gốc

### Khi tách:
- [ ] Tạo 1 component test trước
- [ ] Test import component đó
- [ ] Tạo các components còn lại từng cái một
- [ ] Tạo `__init__.py` với exports đầy đủ
- [ ] Tạo file main mới

### Sau khi tách:
- [ ] Chạy app không lỗi
- [ ] Test từng tab/section
- [ ] Session state hoạt động OK
- [ ] UI giống y hệt file cũ
- [ ] Tất cả files ≤300 dòng
- [ ] Không có linter errors
- [ ] Đã commit với message rõ ràng
- [ ] Đã push lên GitHub

---

## 🚀 MẸO TĂNG TỐC

1. **Dùng Find & Replace thông minh:**
   ```
   Tìm:    with tab1:\n        st.header
   Thay:   def render_overview_tab():\n    st.header
   ```

2. **Copy cả block với số dòng:**
   ```
   Ví dụ: Muốn copy dòng 100-250
   → Dùng editor hỗ trợ "Go to line"
   → Select từ dòng 100 đến 250
   → Copy nguyên xi
   ```

3. **Test parallel:**
   ```bash
   # Terminal 1: File cũ
   streamlit run pages/4_old.py --server.port 8501
   
   # Terminal 2: File mới
   streamlit run pages/4_new.py --server.port 8502
   
   # So sánh 2 tabs browser
   ```

4. **Dùng template generator (nếu có nhiều files):**
   ```python
   # generate_components.py
   components = ['overview', 'assessment', 'diseases']
   
   for name in components:
       with open(f'{name}.py', 'w') as f:
           f.write(f'''"""
{name.title()} Component
"""
import streamlit as st

def render_{name}_tab():
    """Render {name} tab"""
    pass
''')
   ```

---

## 💾 LƯU VÀO MEMORY

**Để AI nhớ lâu dài:**

Quy trình 6 bước:
1. **NGHIÊN CỨU** - Đọc file, vẽ sơ đồ, liệt kê imports/session state
2. **LẬP KẾ HOẠCH** - Quyết định số files, tên files, tách theo logic
3. **TEST 1 COMPONENT** - Tạo 1 file thử, test import
4. **TẠO CÁC COMPONENTS** - Nhân bản quy trình, test từng file
5. **TẠO FILE MAIN** - Import components, giữ nguyên structure
6. **TEST & COMMIT** - Test kỹ, so sánh với file cũ, commit

**Nguyên tắc vàng:**
- Mỗi file ≤ 300 dòng
- Test ngay sau mỗi bước
- Không sửa logic, chỉ di chuyển code
- Commit sau mỗi file hoàn thành

---

**Ngày tạo:** 30/10/2025  
**Version:** 1.0  
**Tác giả:** AI Assistant  
**Sử dụng:** Cho mọi dự án Python cần refactor

