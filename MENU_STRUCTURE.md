# 📋 CẤU TRÚC MENU SIDEBAR - HEALTHADVISOR

**Cập nhật:** 02/01/2025  
**Mục đích:** Tài liệu ghi chú đầy đủ về menu sidebar và các trang

---

## 🎯 MỤC ĐÍCH

Menu sidebar được tạo **TÙY CHỈNH** bằng Streamlit components (st.sidebar), không dùng sidebar navigation mặc định của Streamlit để:
- Kiểm soát hoàn toàn menu hiển thị
- Tránh lỗi CSS/JS không ổn định
- Dễ dàng thêm/xóa/sửa menu

---

## 📂 DANH SÁCH TẤT CẢ CÁC TRANG

### ✅ **TRANG HIỂN THỊ TRONG MENU** (10 trang):

| Số | Tên File | Icon | Tên Hiển Thị | Mô Tả |
|---|---|---|---|---|
| 0 | `0_📖_Hướng_Dẫn.py` | 📖 | Hướng Dẫn | Hướng dẫn sử dụng app, FAQ, tips |
| 1 | `1_❤️_Tim_Mạch.py` | ❤️ | Tim Mạch | Tăng huyết áp, suy tim, bệnh mạch vành |
| 2 | `2_🫁_Hô_Hấp.py` | 🫁 | Hô Hấp | COPD, hen suyễn, kỹ thuật thở |
| 3 | `3_🩸_Tiểu_Đường.py` | 🩸 | Tiểu Đường | Type 1, Type 2, tiền tiểu đường, insulin |
| 4 | `4_🧠_Thần_Kinh.py` | 🧠 | Thần Kinh | Đột quỵ, động kinh, Parkinson |
| 5 | `5_⚖️_Hội_Chứng_Chuyển_Hóa.py` | ⚖️ | Hội Chứng Chuyển Hóa | Rối loạn lipid, béo phì, tiểu đường |
| 6 | `6_🦴_Khớp_Cột_Sống.py` | 🦴 | Khớp - Cột Sống | Thoái hóa khớp, viêm khớp, đau lưng, gút, loãng xương |
| 7 | `7_🎓_Học_Dễ.py` | 🎓 | Học Dễ | Học y khoa bằng hình ảnh, mẹo nhớ |
| 8 | `8_💡_Mẹo_Vặt.py` | 💡 | Mẹo Vặt | Máy tính Paracetamol, nhiệt độ, hướng dẫn uống thuốc |
| 12 | `12_🆘_SOS.py` | 🆘 | SOS | Số cấp cứu, sơ cứu, danh bạ cá nhân |

**Tổng:** 10 trang hiển thị trong menu

---

### 🔒 **TRANG PHỤ TRỢ - ẨN KHỎI MENU** (4 trang):

Các trang này **KHÔNG** hiển thị trong menu sidebar, nhưng vẫn có thể truy cập qua:
- Nút Quick Actions trong trang chủ
- Liên kết trực tiếp

| Số | Tên File | Icon | Tên Hiển Thị | Mô Tả | Cách Truy Cập |
|---|---|---|---|---|---|
| - | `_🤖_AI_Bác_Sĩ.py` | 🤖 | AI Bác Sĩ | Chatbot AI (Gemini/OpenAI) | Nút "Hỏi AI Bác Sĩ" ở trang chủ |
| - | `_📊_Nhật_Ký.py` | 📊 | Nhật Ký | Nhật ký sức khỏe, biểu đồ | Nút "Nhật Ký" ở trang chủ (sẽ thêm) |
| - | `_💊_Nhắc_Thuốc.py` | 💊 | Nhắc Thuốc | Lịch nhắc uống thuốc | Nút "Nhắc Thuốc" ở trang chủ (sẽ thêm) |
| - | `_📈_Xu_Hướng.py` | 📈 | Xu Hướng | Phân tích xu hướng sức khỏe | Nút "Xu Hướng" ở trang chủ (sẽ thêm) |

**Lý do ẩn:** Đây là các trang công cụ phụ trợ, không phải nội dung chính. Người dùng sẽ truy cập qua các nút chức năng cụ thể.

---

## 🎨 THỨ TỰ MENU SIDEBAR

Menu sidebar hiển thị theo thứ tự sau:

1. **⚙️ Cài đặt Giao diện** (Dark Mode toggle)
2. --- (Divider)
3. **📖 Hướng Dẫn**
4. **❤️ Tim Mạch**
5. **🫁 Hô Hấp**
6. **🩸 Tiểu Đường**
7. **🧠 Thần Kinh**
8. **⚖️ Hội Chứng Chuyển Hóa**
9. **🦴 Khớp - Cột Sống**
10. **🎓 Học Dễ**
11. **💡 Mẹo Vặt**
12. **🆘 SOS** (Quan trọng - luôn hiển thị)

---

## 🔧 CẤU TRÚC CODE

### File: `app.py`

**Phần sidebar tùy chỉnh:**
```python
with st.sidebar:
    # 1. Dark Mode Toggle
    st.markdown("### ⚙️ Cài đặt Giao diện")
    dark_mode = st.toggle(...)
    
    st.divider()
    
    # 2. Menu Navigation (Tùy chỉnh)
    st.markdown("### 📂 Điều hướng")
    
    # Menu items với st.page_link hoặc st.button + st.switch_page
    if st.button("📖 Hướng Dẫn", use_container_width=True):
        st.switch_page("pages/0_📖_Hướng_Dẫn.py")
    
    # ... các menu khác
    
    st.divider()
    
    # 3. Quick Actions (tùy chọn)
    st.markdown("### 🚀 Truy cập nhanh")
    # Nút cho các trang phụ trợ
```

### File: `.streamlit/config.toml`

```toml
[client]
showSidebarNavigation = false  # TẮT menu mặc định của Streamlit
```

---

## 📝 QUY TẮC ĐẶT TÊN FILE

### File hiển thị trong menu:
- Format: `{số}_{icon}_{Tên}.py`
- Ví dụ: `0_📖_Hướng_Dẫn.py`
- Số prefix quyết định thứ tự trong menu (nếu Streamlit tự động tạo menu)

### File ẩn khỏi menu:
- Format: `_{icon}_{Tên}.py`
- Ví dụ: `_🤖_AI_Bác_Sĩ.py`
- Prefix `_` (underscore) để Streamlit không tự động thêm vào menu
- KHÔNG có số prefix

---

## ✅ CHECKLIST KHI THÊM TRANG MỚI

- [ ] Tạo file trong `pages/` với format đúng
- [ ] Thêm vào MENU_STRUCTURE.md
- [ ] Thêm menu item vào `app.py` sidebar
- [ ] Test điều hướng
- [ ] Kiểm tra dark mode hoạt động
- [ ] Commit với message rõ ràng

---

## 🔄 LỊCH SỬ THAY ĐỔI

### 02/01/2025 - Refactor menu sidebar
- ✅ Xóa CSS/JS ẩn menu (không ổn định)
- ✅ Tắt sidebar navigation mặc định
- ✅ Tạo menu tùy chỉnh bằng st.sidebar
- ✅ Ghi chú đầy đủ trong MENU_STRUCTURE.md

---

**Note:** File này cần được cập nhật mỗi khi thêm/xóa/sửa menu hoặc trang.

