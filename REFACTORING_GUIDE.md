# 🏗️ Hướng dẫn Cấu trúc Code - HealthAdvisor App

## 📋 Nguyên tắc quan trọng

### ⚠️ LUẬT VÀNG: MỖI FILE TỐI ĐA 300 DÒNG

**TẠI SAO?**
- ✅ Dễ đọc, dễ hiểu
- ✅ Dễ tìm kiếm, debug
- ✅ Dễ bảo trì, sửa lỗi
- ✅ Nhiều người làm việc cùng lúc không conflict
- ❌ File > 500 dòng = KHÓ quản lý!

---

## 📁 Cấu trúc thư mục

```
diseases/
├── metabolic/
│   ├── diabetes/           ✅ MODULE NHỎ (Mẫu chuẩn!)
│   │   ├── __init__.py     # Export tất cả
│   │   ├── info.py         # ~150 dòng - Thông tin bệnh
│   │   ├── medications.py  # ~200 dòng - Thuốc uống
│   │   ├── insulin.py      # ~150 dòng - Insulin
│   │   ├── nutrition.py    # ~200 dòng - Dinh dưỡng
│   │   └── exercise.py     # ~100 dòng - Vận động
│   └── __init__.py
│
├── cardiovascular/
│   ├── hypertension.py     ⚠️ 443 dòng (Chấp nhận được)
│   ├── heart_failure.py    ⚠️ 541 dòng (Nên tách sau)
│   └── __init__.py
│
└── neurological/
    └── __init__.py
```

---

## ✅ MẪU CHUẨN: Module Diabetes (đã refactor)

### Trước khi refactor:
```
diabetes.py  ❌ 962 dòng - QUÁ DÀI!
```

### Sau khi refactor:
```
diabetes/
├── __init__.py      (35 dòng)
├── info.py          (150 dòng)  ✅
├── medications.py   (200 dòng)  ✅
├── insulin.py       (150 dòng)  ✅
├── nutrition.py     (200 dòng)  ✅
└── exercise.py      (100 dòng)  ✅
```

### Cách sử dụng (Tương thích ngược 100%):

```python
# Import như cũ - KHÔNG CẦN SỬA CODE CŨ!
from diseases.metabolic import diabetes

# Sử dụng như bình thường
diabetes.DISEASE_INFO
diabetes.MEDICATIONS_SIMPLE
diabetes.INSULIN_INFO
diabetes.NUTRITION_SIMPLE
diabetes.EXERCISE_SIMPLE
```

---

## 🎯 Khi nào nên tách module?

### Tách NGAY khi:
- ❌ File > 500 dòng
- ❌ Khó tìm nội dung cần sửa
- ❌ Scroll mãi mới thấy hàm/biến
- ❌ Nhiều người sửa cùng file → conflict git

### Tạm chấp nhận khi:
- ⚠️ File 300-500 dòng
- ⚠️ Nội dung liên quan chặt chẽ
- ⚠️ Chưa có thời gian refactor

### Không cần tách:
- ✅ File < 300 dòng
- ✅ Logic đơn giản, rõ ràng
- ✅ Ít thay đổi

---

## 📝 Quy tắc đặt tên file

### 1. Mô tả rõ ràng:
```
✅ info.py           - Thông tin bệnh
✅ medications.py    - Thuốc điều trị
✅ insulin.py        - Insulin (tách riêng vì nhiều)
✅ nutrition.py      - Dinh dưỡng
✅ exercise.py       - Vận động

❌ data.py           - Quá chung chung
❌ utils.py          - Không rõ chứa gì
❌ helpers.py        - Không mô tả
```

### 2. Nhóm theo chức năng:
```
medications/
├── oral_drugs.py      # Thuốc uống
├── insulin.py         # Insulin
└── injections.py      # Thuốc tiêm khác
```

---

## 🛠️ Cách tách module (Step-by-step)

### Bước 1: Tạo thư mục
```bash
mkdir diseases/metabolic/diabetes
```

### Bước 2: Tạo các file nhỏ
```python
# info.py
"""
Thông tin cơ bản về bệnh
"""
DISEASE_INFO = {...}
SYMPTOMS = {...}
```

```python
# medications.py
"""
Thuốc điều trị
"""
MEDICATIONS_SIMPLE = {...}
```

### Bước 3: Tạo `__init__.py` để export
```python
# __init__.py
from .info import DISEASE_INFO, SYMPTOMS
from .medications import MEDICATIONS_SIMPLE
from .nutrition import NUTRITION_SIMPLE

__all__ = [
    'DISEASE_INFO',
    'SYMPTOMS',
    'MEDICATIONS_SIMPLE',
    'NUTRITION_SIMPLE',
]
```

### Bước 4: Cập nhật import (nếu cần)
```python
# Trước:
from diseases.metabolic import diabetes

# Sau: KHÔNG ĐỔI! Vẫn import như cũ
from diseases.metabolic import diabetes
```

### Bước 5: Test
```bash
python -c "from diseases.metabolic import diabetes; print('OK')"
```

### Bước 6: Xóa file cũ
```bash
rm diseases/metabolic/diabetes.py
```

---

## 🎨 Best Practices

### 1. Docstring rõ ràng:
```python
"""
Thuốc điều trị Tiểu Đường - Thuốc uống
Bao gồm: Metformin, Sulfonylureas, DPP-4i, SGLT-2i, GLP-1
"""
```

### 2. Comments hữu ích:
```python
# ============= THUỐC ĐIỀU TRỊ =============
# Phân chia rõ ràng các phần

MEDICATIONS_SIMPLE = {
    # Tổng quan
    "overview_vn": """...""",
    
    # Danh sách thuốc uống
    "oral_medications": [...]
}
```

### 3. Tương thích ngược:
```python
# Luôn export để code cũ không bị lỗi
from .old_module import *
```

---

## 📊 Checklist Refactor

Trước khi refactor:
- [ ] Đo độ dài file (`wc -l filename.py`)
- [ ] Xác định các phần có thể tách
- [ ] Backup code (git commit)

Trong khi refactor:
- [ ] Tạo thư mục con
- [ ] Tách từng phần vào file riêng
- [ ] Mỗi file < 300 dòng
- [ ] Có docstring đầy đủ
- [ ] Tạo `__init__.py`

Sau khi refactor:
- [ ] Test import
- [ ] Test app chạy
- [ ] Kiểm tra linter errors
- [ ] Git commit
- [ ] Cập nhật tài liệu

---

## 🚀 Kế hoạch tiếp theo

### Đã hoàn thành ✅:
- [x] Diabetes module (962 → 5 files < 250 dòng mỗi file)

### Dự kiến refactor tiếp:
- [ ] Heart Failure (541 dòng → 4 files)
- [ ] Hypertension (443 dòng → 4 files nếu cần)

### Nguyên tắc:
- Refactor khi file > 500 dòng
- File 300-500 dòng: tùy tình hình
- File < 300 dòng: giữ nguyên

---

## 💡 Tips

1. **Đừng vội!** Refactor từng bước, test kỹ
2. **Git commit thường xuyên** để dễ rollback
3. **Tách theo logic** không phải theo số dòng máy móc
4. **Tương thích ngược** để code cũ vẫn chạy
5. **Document ngay** khi refactor xong

---

## 🔗 Tham khảo

- Mẫu chuẩn: `diseases/metabolic/diabetes/`
- File này: `REFACTORING_GUIDE.md`
- Python PEP 8: https://pep8.org/

---

**Cập nhật:** 30/10/2025  
**Tác giả:** AI Assistant với sự hỗ trợ của User

