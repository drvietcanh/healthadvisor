# 📋 CÁC BƯỚC BẠN CẦN LÀM TIẾP

## ✅ ĐÃ HOÀN THÀNH (tự động):
- [x] Git đã khởi tạo
- [x] 26 files đã commit (5080 dòng code)
- [x] Branch main đã sẵn sàng

---

## 🚀 CÁC BƯỚC TIẾP THEO (Cần bạn làm):

### BƯỚC 1: Tạo GitHub Repository

1. **Mở trình duyệt:** https://github.com/new

2. **Đăng nhập GitHub** (nếu chưa đăng nhập)

3. **Điền thông tin:**
   - **Repository name:** `healthadvisor`
   - **Description:** `Ứng dụng tư vấn sức khỏe AI cho người Việt`
   - **Visibility:** Chọn **Public** ✅
   - **KHÔNG tích:** ❌ Add a README file
   - **KHÔNG tích:** ❌ Add .gitignore
   - **KHÔNG tích:** ❌ Choose a license

4. **Click:** Nút **Create repository** (màu xanh)

✅ **Kết quả:** Bạn sẽ thấy màn hình hướng dẫn với URL repository

---

### BƯỚC 2: Push Code lên GitHub

**Mở PowerShell/Terminal tại `D:\1app\ask` và chạy từng lệnh:**

#### 2.1. Thay `YOUR_USERNAME` bằng username GitHub của bạn:

```bash
git remote add origin https://github.com/YOUR_USERNAME/healthadvisor.git
```

**Ví dụ:** Nếu username của bạn là `viethealth`:
```bash
git remote add origin https://github.com/viethealth/healthadvisor.git
```

#### 2.2. Push code:

```bash
git push -u origin main
```

**GitHub sẽ yêu cầu xác thực:**

#### 🔐 Cách lấy Personal Access Token:

1. Mở: https://github.com/settings/tokens
2. Click: **Generate new token** → **Generate new token (classic)**
3. Đặt tên: `healthadvisor-deploy`
4. Chọn quyền: **Tích vào `repo`** (tích hết các ô con bên dưới)
5. Click: **Generate token**
6. **COPY TOKEN NGAY!** (Bắt đầu bằng `ghp_...`, chỉ hiện 1 lần!)
7. Khi Git hỏi password: **DÁN TOKEN vào** (không phải password GitHub!)

✅ **Kết quả:** `Branch 'main' set up to track remote branch 'main' from 'origin'`

#### 2.3. Kiểm tra:

Mở: `https://github.com/YOUR_USERNAME/healthadvisor`

Bạn sẽ thấy 26 files đã upload! 🎉

---

### BƯỚC 3: Deploy trên Streamlit Cloud

#### 3.1. Truy cập Streamlit Cloud:

Mở: https://share.streamlit.io

#### 3.2. Đăng nhập:

Click: **Continue with GitHub**

#### 3.3. Deploy App:

1. Click: **New app** (hoặc **Create app**)

2. **Điền thông tin:**

   ![Deploy Form](https://docs.streamlit.io/images/streamlit-community-cloud/deploy-empty-form.png)

   - **Repository:** Chọn `YOUR_USERNAME/healthadvisor`
   - **Branch:** `main`
   - **Main file path:** `app.py`
   - **App URL (optional):** 
     - Để mặc định HOẶC
     - Đặt tên: `healthadvisor-vn` 
     - → URL: `healthadvisor-vn.streamlit.app`

3. Click: **Deploy!** (nút đỏ)

#### 3.4. Chờ Deploy:

- Streamlit tự động:
  1. ✅ Clone repository
  2. ✅ Cài đặt requirements.txt
  3. ✅ Chạy app.py
  
- ⏱️ Thời gian: **2-5 phút**

✅ **Kết quả:** App đã LIVE! 🌍

---

### BƯỚC 4: Thêm OpenAI API Key (TÙY CHỌN)

**Nếu muốn dùng AI Chatbot thật:**

#### 4.1. Lấy OpenAI API Key:

1. Mở: https://platform.openai.com
2. Đăng ký/Đăng nhập
3. Click: **API keys** (sidebar)
4. Click: **Create new secret key**
5. Đặt tên: `healthadvisor`
6. **COPY KEY** (bắt đầu `sk-...`)

#### 4.2. Thêm vào Streamlit Cloud:

1. Vào app trên Streamlit Cloud
2. Click: **Settings** ⚙️ (góc phải)
3. Click: **Secrets** 🔒
4. Paste vào:

```toml
OPENAI_API_KEY = "sk-your-actual-api-key-here"
```

5. Click: **Save**

✅ **Kết quả:** AI Chatbot hoạt động! 🤖

**Lưu ý:**
- OpenAI tính phí: ~$0.002/1000 tokens (rất rẻ)
- Nạp tối thiểu: $5
- **KHÔNG có API key:** Chatbot vẫn hoạt động với câu trả lời mẫu

---

## 🎯 CHECKLIST HOÀN THÀNH

- [ ] GitHub repository đã tạo
- [ ] Code đã push lên GitHub
- [ ] App đã deploy trên Streamlit Cloud
- [ ] Mở được link app
- [ ] Các trang hoạt động OK
- [ ] Chatbot hoạt động
- [ ] (Tùy chọn) API Key đã thêm

---

## 🔄 CẬP NHẬT APP (Sau này)

Khi sửa code:

```bash
git add .
git commit -m "Mo ta thay doi"
git push
```

→ Streamlit tự động deploy lại sau 1-2 phút!

---

## 🆘 XỬ LÝ LỖI

### Lỗi: "remote origin already exists"

```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/healthadvisor.git
```

### Lỗi: "authentication failed"

- Kiểm tra đã dùng **Personal Access Token** chưa (KHÔNG phải password)
- Xem lại BƯỚC 2.2 để lấy token

### Lỗi: "App is taking too long" (Streamlit)

- Đợi thêm vài phút
- Reload lại trang

### Lỗi deploy khác:

Xem **Manage app** → **Logs** để biết lỗi cụ thể

---

## 📞 HỖ TRỢ

- **GitHub:** https://docs.github.com
- **Streamlit:** https://docs.streamlit.io
- **Community:** https://discuss.streamlit.io

---

## 🎉 CHÚC MỪNG!

Làm theo các bước trên, app của bạn sẽ LIVE trong **10 phút**!

URL app: `https://YOUR-APP-NAME.streamlit.app`

**Chia sẻ ngay cho bạn bè và gia đình!** ❤️🏥

