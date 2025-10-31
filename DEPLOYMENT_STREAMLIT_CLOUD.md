# 🚀 Hướng dẫn Deploy lên Streamlit Cloud

## 📋 Yêu cầu trước khi deploy

### 1. File cấu hình cần có

- ✅ `app.py` - File chính (đã có)
- ✅ `requirements.txt` - Dependencies (đã có)
- ✅ `.streamlit/config.toml` - Cấu hình Streamlit (đã có)

### 2. Cấu trúc thư mục

Streamlit Cloud sẽ tự động tìm `app.py` trong thư mục gốc của repo.

```
healthadvisor/
├── app.py                    # ← File chính
├── requirements.txt          # ← Dependencies
├── .streamlit/
│   └── config.toml          # ← Cấu hình
└── pages/                    # ← Các trang
```

## 🔗 Kết nối Streamlit Cloud

### Bước 1: Đăng nhập Streamlit Cloud

1. Truy cập: https://share.streamlit.io/
2. Đăng nhập bằng GitHub account
3. Authorize Streamlit Cloud để truy cập GitHub repos

### Bước 2: Deploy App mới

1. Click **"New app"**
2. Chọn repository: `drvietcanh/healthadvisor`
3. Branch: `main`
4. Main file path: `app.py` (mặc định, không cần sửa)
5. Click **"Deploy!"**

### Bước 3: Chờ deploy

- Streamlit Cloud sẽ tự động:
  - Cài đặt dependencies từ `requirements.txt`
  - Chạy `app.py`
  - Hiển thị URL app của bạn

## 🔑 Secrets (Nếu cần API Keys)

Nếu app cần API keys (OpenAI, Gemini), thêm vào Streamlit Cloud Secrets:

1. Vào app trên Streamlit Cloud
2. Click menu ☰ → **Settings**
3. Chọn tab **Secrets**
4. Thêm secrets theo format:

```toml
OPENAI_API_KEY = "sk-..."
GEMINI_API_KEY = "AIza..."
```

Sau đó trong code, sử dụng:
```python
import streamlit as st
openai_key = st.secrets.get("OPENAI_API_KEY")
```

## 📝 Lưu ý

### 1. Branch protection

- Mỗi khi push lên `main`, Streamlit Cloud sẽ tự động redeploy
- Có thể deploy từ branch khác để test

### 2. Logs

- Xem logs tại menu ☰ → **Manage app** → **Logs**
- Giúp debug khi có lỗi

### 3. Cập nhật

- Sau mỗi commit + push, Streamlit Cloud sẽ tự động cập nhật
- Mất khoảng 1-2 phút để deploy

## 🎯 URL App

Sau khi deploy xong, URL sẽ có dạng:
```
https://healthadvisor-xxxxx.streamlit.app
```

Hoặc custom domain (nếu có):
```
https://healthadvisor.vn
```

## ✅ Checklist

- [x] Repository đã push lên GitHub
- [x] File `app.py` ở thư mục gốc
- [x] File `requirements.txt` đầy đủ dependencies
- [x] File `.streamlit/config.toml` cấu hình đúng
- [ ] Đăng nhập Streamlit Cloud
- [ ] Deploy app
- [ ] Test app trên Streamlit Cloud
- [ ] (Nếu cần) Thêm Secrets cho API keys

## 🔗 Links

- Streamlit Cloud: https://share.streamlit.io/
- GitHub Repo: https://github.com/drvietcanh/healthadvisor
- Streamlit Docs: https://docs.streamlit.io/streamlit-community-cloud

