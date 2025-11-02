# 📋 DANH SÁCH MODULES CẦN TÁCH (File > 300 dòng)

**Cập nhật:** 03/01/2025  
**Tiêu chuẩn:** File > 300 dòng cần tách theo quy trình trong `QUY_TRINH_TACH_MODULE.md`

---

## 🔴 **ƯU TIÊN CAO - File > 500 dòng** (BẮT BUỘC TÁCH)

| # | File | Dòng | Mô tả | Ưu tiên |
|---|------|------|-------|---------|
| 1 | `emergency_contacts/first_aid_additional3.py` | **570** | Hướng dẫn sơ cứu bổ sung (tình huống 3) | 🔴 Rất cao |
| 2 | `emergency_contacts/first_aid_additional4.py` | **512** | Hướng dẫn sơ cứu bổ sung (tình huống 4) | 🔴 Rất cao |
| 3 | `health_tips/daily_tips.py` | **467** | Mẹo vặt hàng ngày | 🔴 Rất cao |

**Hành động:** Cần tách NGAY - vi phạm nghiêm trọng quy tắc 300 dòng

---

## 🟡 **ƯU TIÊN TRUNG BÌNH - File 400-500 dòng**

| # | File | Dòng | Mô tả | Ưu tiên |
|---|------|------|-------|---------|
| 4 | `health_tips/general_tips.py` | **434** | Mẹo vặt tổng quát | 🟡 Cao |
| 5 | `pages/4_🧠_Thần_Kinh.py` | **418** | Trang Thần Kinh | 🟡 Cao |
| 6 | `respiratory_page_components/asthma_tab.py` | **399** | Tab Hen suyễn | 🟡 Trung bình |
| 7 | `emergency_contacts/first_aid_trauma.py` | **397** | Sơ cứu chấn thương | 🟡 Trung bình |
| 8 | `bone_joint_page_components/osteoporosis_tab.py` | **383** | Tab Loãng xương | 🟡 Trung bình |

**Hành động:** Nên tách trong 1-2 tuần tới

---

## 🟢 **ƯU TIÊN THẤP - File 300-400 dòng** (THEO DÕI)

| # | File | Dòng | Mô tả | Ghi chú |
|---|------|------|-------|---------|
| 9 | `core/dark_mode_css.py` | **399** | CSS Dark Mode | ⚪ Giữ nguyên (CSS) |
| 10 | `core/light_mode_css.py` | **382** | CSS Light Mode | ⚪ Giữ nguyên (CSS) |
| 11 | `health_trends/analyzer.py` | **348** | Phân tích xu hướng | 🟢 Theo dõi |
| 12 | `diseases/metabolic/dyslipidemia/nutrition/vietnamese_foods.py` | **334** | Thực phẩm Việt Nam | 🟢 Theo dõi |
| 13 | `diseases/metabolic/diabetes/nutrition/vietnamese_foods_gl.py` | **333** | Thực phẩm GL | 🟢 Theo dõi |
| 14 | `pages/7_🎓_Học_Dễ.py` | **317** | Trang Học Dễ | 🟢 OK (gần 300) |
| 15 | `respiratory_page_components/pneumonia_tab.py` | **309** | Tab Viêm phổi | 🟢 OK (gần 300) |

**Hành động:** Theo dõi, chỉ tách khi thêm code mới vượt 350 dòng

---

## 📊 **TỔNG KẾT**

### Phân loại theo mức độ:

- 🔴 **Rất cao (3 files):** > 500 dòng - Cần tách NGAY
- 🟡 **Cao (5 files):** 400-500 dòng - Tách trong 1-2 tuần
- 🟢 **Thấp (7 files):** 300-400 dòng - Theo dõi, tách khi cần

### Loại trừ:

- ✅ **CSS files (2):** `dark_mode_css.py`, `light_mode_css.py` - Giữ nguyên (CSS thường dài)

### Kế hoạch tách:

1. **Tuần 1:** Tách 3 file > 500 dòng (ưu tiên cao nhất)
2. **Tuần 2-3:** Tách 5 file 400-500 dòng
3. **Tuần 4+:** Theo dõi 7 file 300-400 dòng

---

## 💡 **GỢI Ý TÁCH FILE**

### 1. `first_aid_additional3.py` (570 dòng)
**Đề xuất tách thành:**
- `first_aid_additional3a.py` - Tình huống 1-2
- `first_aid_additional3b.py` - Tình huống 3-4
- `first_aid_additional3c.py` - Tình huống 5-6

### 2. `first_aid_additional4.py` (512 dòng)
**Đề xuất tách thành:**
- `first_aid_additional4a.py` - Tình huống 1-3
- `first_aid_additional4b.py` - Tình huống 4-5

### 3. `daily_tips.py` (467 dòng)
**Đề xuất tách thành:**
- `daily_tips_nutrition.py` - Mẹo dinh dưỡng
- `daily_tips_exercise.py` - Mẹo vận động
- `daily_tips_general.py` - Mẹo tổng quát

### 4. `pages/4_🧠_Thần_Kinh.py` (418 dòng)
**Đề xuất tách thành:**
- `neurological_page_components/` (đã có sẵn)
- Tách các tab thành components riêng nếu chưa có

---

## 🎯 **KẾT LUẬN**

**Tổng số file cần tách:** 15 files (không tính CSS)

**Ưu tiên ngay:**
- 3 files > 500 dòng
- 5 files 400-500 dòng

**Theo dõi:**
- 7 files 300-400 dòng

**Giữ nguyên:**
- 2 CSS files

