# 🔄 HƯỚNG DẪN RESTART STREAMLIT

## 💡 Restart Streamlit là gì?

**Restart Streamlit** = Khởi động lại ứng dụng Streamlit của bạn.

### Tại sao cần restart?

1. **Thay đổi cấu hình** (như `.streamlit/config.toml`)
   - Streamlit chỉ đọc file config khi khởi động
   - Thay đổi config → Phải restart mới có hiệu lực

2. **Thay đổi CSS/JavaScript**
   - Một số thay đổi CSS chỉ áp dụng khi reload trang
   - Thay đổi lớn về UI → Nên restart

3. **Import modules mới**
   - Khi thêm file Python mới, Streamlit cần reload
   - Thường Streamlit tự reload, nhưng đôi khi cần restart

4. **Cài đặt package mới**
   - Cài pip package mới → Phải restart

---

## 🖥️ CÁCH RESTART STREAMLIT

### **Cách 1: Trong Terminal (Khuyến nghị)**

1. **Dừng Streamlit:**
   - Nhấn `Ctrl + C` trong terminal đang chạy Streamlit
   - Hoặc đóng terminal

2. **Chạy lại:**
   ```bash
   streamlit run app.py
   ```

### **Cách 2: Nút Restart trong Streamlit**

1. Mở menu Settings (⚙️) ở góc trên bên phải
2. Click **"Rerun"** hoặc **"Always rerun"**
3. Hoặc nhấn phím `R` trong Streamlit

### **Cách 3: Reload Browser**

1. Nhấn `F5` hoặc `Ctrl + R` trong trình duyệt
2. Hoặc click nút reload trên trình duyệt

---

## 🎯 KHI NÀO CẦN RESTART?

### ✅ **Cần restart:**
- Thay đổi `.streamlit/config.toml`
- Thay đổi CSS trong file config (một số trường hợp)
- Cài đặt package mới (`pip install`)
- Thay đổi biến môi trường (`.env`)

### ⚠️ **Không cần restart (Streamlit tự reload):**
- Sửa code Python trong `.py` files
- Thay đổi nội dung markdown
- Thêm/xóa comments
- Streamlit tự động phát hiện và reload

---

## 📝 VÍ DỤ THỰC TẾ

### **Ví dụ 1: Thay đổi config.toml**

**Trước khi restart:**
```toml
# .streamlit/config.toml
showSidebarNavigation = true  # Menu sidebar hiện
```

**Sửa thành:**
```toml
showSidebarNavigation = false  # Ẩn menu sidebar
```

**→ Phải restart Streamlit để có hiệu lực!**

**Cách làm:**
1. `Ctrl + C` để dừng Streamlit
2. Chạy lại: `streamlit run app.py`

### **Ví dụ 2: Cài package mới**

```bash
pip install pandas
```

**→ Phải restart Streamlit!**

**Cách làm:**
1. `Ctrl + C`
2. `streamlit run app.py`

### **Ví dụ 3: Sửa code Python**

**Sửa file `app.py`:**
```python
st.title("Xin chào")  # Thay đổi text
```

**→ Không cần restart! Streamlit tự reload khi bạn save file.**

---

## 🔍 KIỂM TRA STREAMLIT CÓ CHẠY KHÔNG?

### **Cách 1: Xem Terminal**
- Nếu thấy dòng: `You can now view your Streamlit app in your browser.`
- → Streamlit đang chạy

### **Cách 2: Xem Browser**
- Mở trình duyệt: `http://localhost:8501`
- Nếu thấy app → Đang chạy
- Nếu không thấy → Chưa chạy hoặc đã dừng

### **Cách 3: Kiểm tra Process**

**Windows (PowerShell):**
```powershell
Get-Process | Where-Object {$_.ProcessName -like "*python*" -or $_.ProcessName -like "*streamlit*"}
```

**Nếu không thấy → Streamlit chưa chạy hoặc đã dừng**

---

## 🛠️ XỬ LÝ KHI GẶP LỖI

### **Lỗi: Port 8501 đã được sử dụng**

**Nguyên nhân:** Streamlit cũ chưa tắt hẳn

**Giải pháp:**
```bash
# Windows (PowerShell)
netstat -ano | findstr :8501
# Lấy PID (số cuối cùng)
taskkill /PID <PID> /F

# Sau đó chạy lại:
streamlit run app.py
```

### **Lỗi: ModuleNotFoundError**

**Nguyên nhân:** Package chưa được cài hoặc chưa restart sau khi cài

**Giải pháp:**
1. Cài package: `pip install <package_name>`
2. **Restart Streamlit** (quan trọng!)

### **Lỗi: Thay đổi không hiển thị**

**Nguyên nhân:** Chưa restart hoặc cache trình duyệt

**Giải pháp:**
1. Restart Streamlit
2. Hard refresh trình duyệt: `Ctrl + Shift + R` (hoặc `Ctrl + F5`)

---

## 📌 TÓM TẮT

| Tình huống | Cần restart? |
|------------|--------------|
| Sửa code Python (.py) | ❌ Không (auto reload) |
| Sửa config.toml | ✅ Có |
| Cài pip package | ✅ Có |
| Sửa CSS/JS | ⚠️ Tùy (thường không) |
| Thay đổi .env | ✅ Có |

**Nguyên tắc vàng:** Khi không chắc → **Restart lại cho chắc!** 😊

---

## 🎯 QUY TRÌNH RESTART CHUẨN

1. **Lưu tất cả files** (Ctrl + S)
2. **Dừng Streamlit:** `Ctrl + C` trong terminal
3. **Chạy lại:** `streamlit run app.py`
4. **Mở browser:** `http://localhost:8501`
5. **Kiểm tra:** Xem thay đổi đã có hiệu lực chưa

---

**Chúc bạn thành công! 🚀**

