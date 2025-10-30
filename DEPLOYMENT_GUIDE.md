# 🚀 Hướng Dẫn Deploy HealthAdvisor lên Streamlit Cloud

## 📋 Mục lục
1. [Chuẩn bị](#bước-1-chuẩn-bị)
2. [Push lên GitHub](#bước-2-push-lên-github)
3. [Deploy trên Streamlit Cloud](#bước-3-deploy-trên-streamlit-cloud)
4. [Cấu hình API Key (Tùy chọn)](#bước-4-cấu-hình-api-key-tùy-chọn)
5. [Kiểm tra và sử dụng](#bước-5-kiểm-tra-và-sử-dụng)

---

## Bước 1: Chuẩn bị

### 1.1. Kiểm tra Git đã cài chưa

Mở PowerShell/Terminal và chạy:

```bash
git --version
```

**Nếu chưa có Git:**
- Tải tại: https://git-scm.com/download/win
- Cài đặt với cấu hình mặc định
- Khởi động lại Terminal

### 1.2. Tạo tài khoản GitHub (nếu chưa có)

1. Truy cập: https://github.com
2. Click **Sign up**
3. Điền thông tin:
   - Username (ví dụ: `viethealth`)
   - Email
   - Password
4. Xác thực email

---

## Bước 2: Push lên GitHub

### 2.1. Khởi tạo Git trong project

Mở Terminal tại thư mục `D:\1app\ask`:

```bash
# Di chuyển vào thư mục project
cd D:\1app\ask

# Khởi tạo Git repository
git init
```

✅ **Kết quả:** `Initialized empty Git repository in D:/1app/ask/.git/`

### 2.2. Cấu hình Git (lần đầu)

```bash
# Đặt tên người dùng
git config --global user.name "Tên của bạn"

# Đặt email (giống GitHub)
git config --global user.email "email@example.com"
```

### 2.3. Tạo Repository trên GitHub

1. Truy cập: https://github.com
2. Đăng nhập
3. Click nút **+** (góc trên bên phải) → **New repository**
4. Điền thông tin:
   - **Repository name:** `healthadvisor` (hoặc tên bạn thích)
   - **Description:** `Ứng dụng tư vấn sức khỏe AI cho người Việt`
   - Chọn: **Public** (để deploy miễn phí trên Streamlit Cloud)
   - **KHÔNG** tích: Add README, .gitignore (ta đã có rồi)
5. Click **Create repository**

✅ **Kết quả:** Bạn sẽ thấy màn hình hướng dẫn với URL repository

### 2.4. Thêm tất cả file vào Git

Quay lại Terminal:

```bash
# Thêm tất cả file
git add .

# Kiểm tra file đã thêm
git status
```

✅ **Kết quả:** Thấy danh sách file màu xanh

### 2.5. Commit (lưu thay đổi)

```bash
git commit -m "Initial commit - HealthAdvisor v1.0"
```

✅ **Kết quả:** Thấy thông báo `X files changed`

### 2.6. Kết nối với GitHub và Push

**Thay `YOUR_USERNAME` bằng username GitHub của bạn:**

```bash
# Đổi tên nhánh thành main
git branch -M main

# Kết nối với GitHub repository
git remote add origin https://github.com/YOUR_USERNAME/healthadvisor.git

# Push code lên GitHub
git push -u origin main
```

**Lần đầu push, GitHub sẽ yêu cầu đăng nhập:**

#### Cách 1: Dùng Personal Access Token (Khuyên dùng)

1. Truy cập: https://github.com/settings/tokens
2. Click **Generate new token** → **Generate new token (classic)**
3. Đặt tên: `healthadvisor-deploy`
4. Chọn quyền: **repo** (tích hết)
5. Click **Generate token**
6. **COPY TOKEN NGAY** (chỉ hiện 1 lần!)
7. Khi Git yêu cầu password, dán token vào

#### Cách 2: Dùng GitHub Desktop (Dễ hơn)

1. Tải GitHub Desktop: https://desktop.github.com
2. Đăng nhập GitHub
3. File → Add Local Repository → Chọn `D:\1app\ask`
4. Click **Publish repository**

✅ **Kết quả:** Code đã lên GitHub!

### 2.7. Kiểm tra

Truy cập: `https://github.com/YOUR_USERNAME/healthadvisor`

Bạn sẽ thấy tất cả file đã upload!

---

## Bước 3: Deploy trên Streamlit Cloud

### 3.1. Truy cập Streamlit Cloud

1. Mở: https://share.streamlit.io
2. Click **Sign up** hoặc **Continue with GitHub**
3. Cho phép Streamlit truy cập GitHub

### 3.2. Deploy App

1. Click **New app** (hoặc **Create app**)

2. Điền thông tin:

   **Repository:**
   - Chọn repository: `YOUR_USERNAME/healthadvisor`

   **Branch:**
   - Chọn: `main`

   **Main file path:**
   - Nhập: `app.py`

   **App URL (optional):**
   - Để mặc định hoặc đặt tên: `healthadvisor-vn`
   - URL sẽ là: `healthadvisor-vn.streamlit.app`

3. Click **Deploy!** (nút màu đỏ)

### 3.3. Chờ Deploy

- Streamlit sẽ tự động:
  1. Clone repository
  2. Cài đặt requirements.txt
  3. Chạy ứng dụng
  
- Thời gian: **2-5 phút**

✅ **Kết quả:** Ứng dụng đã LIVE trên Internet!

### 3.4. Lưu ý nếu có lỗi

Nếu deploy lỗi, xem log bên dưới:

**Lỗi thường gặp:**

1. **ModuleNotFoundError**
   - Nguyên nhân: Thiếu thư viện trong `requirements.txt`
   - Sửa: Thêm thư viện vào `requirements.txt`, commit và push

2. **Import Error**
   - Nguyên nhân: Import sai đường dẫn
   - Sửa: Kiểm tra lại import trong code

3. **File not found**
   - Nguyên nhân: Thiếu file `__init__.py`
   - Sửa: Đã có đủ rồi, reload lại

---

## Bước 4: Cấu hình API Key (Tùy chọn)

Nếu muốn dùng AI Chatbot thật (OpenAI):

### 4.1. Lấy OpenAI API Key

1. Truy cập: https://platform.openai.com
2. Đăng ký/Đăng nhập
3. Click **API keys** (bên trái)
4. Click **Create new secret key**
5. Đặt tên: `healthadvisor`
6. **COPY KEY** (bắt đầu bằng `sk-...`)

### 4.2. Thêm vào Streamlit Cloud

1. Vào app trên Streamlit Cloud
2. Click **Settings** (góc phải)
3. Click **Secrets**
4. Paste vào:

```toml
OPENAI_API_KEY = "sk-your-actual-api-key-here"
```

5. Click **Save**

✅ **Kết quả:** AI Chatbot đã hoạt động!

**Lưu ý:**
- OpenAI tính phí theo usage (~$0.002/1000 tokens)
- Nạp tối thiểu $5 để dùng
- Nếu không có API key, chatbot vẫn hoạt động với câu trả lời mẫu

---

## Bước 5: Kiểm tra và sử dụng

### 5.1. Truy cập App

URL của bạn: `https://YOUR-APP-NAME.streamlit.app`

Ví dụ: `https://healthadvisor-vn.streamlit.app`

### 5.2. Chia sẻ

Copy link và chia sẻ cho mọi người! 🎉

### 5.3. Theo dõi

Xem analytics tại:
- Streamlit Cloud Dashboard
- Số lượt truy cập
- Lỗi (nếu có)

---

## 🔄 Cập nhật App

Khi bạn sửa code:

```bash
# 1. Lưu thay đổi
git add .

# 2. Commit
git commit -m "Mô tả thay đổi"

# 3. Push lên GitHub
git push

# 4. Streamlit tự động deploy lại (1-2 phút)
```

---

## 🎯 Checklist Deploy thành công

- [ ] Code đã trên GitHub
- [ ] App đã deploy trên Streamlit Cloud
- [ ] Mở được link app
- [ ] Các trang điều hướng OK
- [ ] Chatbot hoạt động (có hoặc không API key)
- [ ] Công cụ tính toán hoạt động
- [ ] Không có lỗi trên màn hình

---

## 💡 Tips

### Tăng tốc độ app
Thêm vào `.streamlit/config.toml`:
```toml
[server]
runOnSave = true
maxUploadSize = 200
```

### Custom domain (Tùy chọn)
Nếu có domain riêng:
1. Settings → Custom domain
2. Thêm CNAME record
3. Chờ DNS propagate

### Giới hạn miễn phí
- Streamlit Cloud Free:
  - 1 private app
  - 3 public apps
  - Unlimited visitors
  - 1 GB RAM

---

## ❓ Xử lý lỗi

### Lỗi: "App is taking too long"
**Nguyên nhân:** App chạy quá chậm (>10s)
**Giải pháp:**
- Thêm `@st.cache_data` cho hàm nặng
- Giảm import không cần thiết

### Lỗi: "Out of memory"
**Nguyên nhân:** App dùng >1GB RAM
**Giải pháp:**
- Tối ưu code
- Xóa data không dùng
- Nâng cấp plan

### Lỗi: "File not found"
**Nguyên nhân:** Đường dẫn file sai
**Giải pháp:**
- Dùng đường dẫn tương đối
- Kiểm tra `sys.path.append('..')`

---

## 🆘 Cần trợ giúp?

1. **Streamlit Community:** https://discuss.streamlit.io
2. **GitHub Issues:** Tạo issue trong repo
3. **Documentation:** https://docs.streamlit.io

---

## 🎉 Chúc mừng!

App của bạn đã LIVE trên Internet! 🌍

**Chia sẻ ngay:** `https://your-app.streamlit.app`

Giúp hàng triệu người chăm sóc sức khỏe tốt hơn! 💪❤️

