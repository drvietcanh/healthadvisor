# 🚀 Hướng dẫn Chi tiết: Thêm Gemini API vào HealthAdvisor

## ⭐ BƯỚC 1: Lấy Gemini API Key (MIỄN PHÍ!)

### 1.1. Truy cập Google AI Studio:
1. Mở trình duyệt, vào: https://aistudio.google.com/app/apikey
2. Đăng nhập bằng **Gmail** của bạn

### 1.2. Tạo API Key:
1. Click vào nút **"Get API key"** hoặc **"Create API key"**
2. Chọn **"Create API key in new project"**
3. Đợi vài giây → API key sẽ hiện ra
4. **SAO CHÉP** API key (dạng: `AIzaSy...`)

### 1.3. Lưu API Key:
📝 Lưu vào file notepad hoặc ghi lại (ĐỪNG CHIA SẺ với ai!)

---

## ⚙️ BƯỚC 2: Cài đặt thư viện Gemini

Mở PowerShell trong thư mục dự án và chạy:

```bash
pip install google-generativeai
```

---

## 📝 BƯỚC 3: Cập nhật requirements.txt

Thêm dòng này vào file `requirements.txt`:

```
google-generativeai>=0.3.0
```

---

## 💻 BƯỚC 4: Tích hợp Gemini vào Chatbot

File `core/chatbot_enhanced.py` đã được cập nhật để hỗ trợ cả OpenAI và Gemini!

---

## 🧪 BƯỚC 5: Test trên máy local

### 5.1. Chạy app:
```bash
streamlit run app.py
```

### 5.2. Test Gemini:
1. Vào trang **"🤖 AI Bác Sĩ"**
2. Ở **Sidebar**:
   - Chọn **"AI Provider" → Gemini**
   - Nhập API key vừa lấy
   - Click **"💾 Lưu API Key"**
3. Hỏi thử: "Huyết áp bao nhiêu là bình thường?"

Nếu có câu trả lời → ✅ Thành công!

---

## 🌐 BƯỚC 6: Deploy lên Streamlit Cloud

### 6.1. Push code lên GitHub:
```bash
git add .
git commit -m "Add Gemini API support"
git push
```

### 6.2. Lưu API Key trên Streamlit Cloud:
1. Vào https://share.streamlit.io/
2. Click vào app của bạn
3. Click **"Settings"** (⚙️)
4. Click **"Secrets"**
5. Thêm vào:

```toml
GEMINI_API_KEY = "AIzaSy_YOUR_API_KEY_HERE"
```

6. Click **"Save"**
7. App sẽ tự động restart

---

## ✅ Kiểm tra

### Test API key có hoạt động:
```python
import google.generativeai as genai

# Thay YOUR_API_KEY bằng key thật
genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Xin chào!")
print(response.text)
```

Nếu có kết quả → ✅ API key hoạt động!

---

## 🆚 So sánh: Gemini vs OpenAI

| Tiêu chí | Gemini Pro | OpenAI GPT-3.5/4 |
|----------|------------|------------------|
| **Giá** | ✅ MIỄN PHÍ | ❌ Trả phí |
| **Giới hạn** | 60 requests/phút | Theo gói |
| **Tiếng Việt** | ✅ Rất tốt | ✅ Tốt |
| **Tốc độ** | ✅ Nhanh | ✅ Nhanh |
| **Dễ dùng** | ✅ Đơn giản | ⚠️ Phức tạp hơn |

**Khuyến nghị:** Dùng Gemini cho dự án này! 🌟

---

## 🐛 Xử lý lỗi

### Lỗi: "API key not valid"
✅ Kiểm tra lại API key đã copy đúng chưa
✅ Đảm bảo không có khoảng trắng thừa

### Lỗi: "Resource exhausted"
✅ Bạn đã vượt quá 60 requests/phút
✅ Đợi 1 phút rồi thử lại

### Lỗi: "Module not found"
✅ Chạy lại: `pip install google-generativeai`

---

## 📚 Tài liệu tham khảo

- Google AI Studio: https://aistudio.google.com/
- Gemini API Docs: https://ai.google.dev/docs
- Code mẫu: `core/chatbot_enhanced.py`

---

**Cập nhật:** 30/10/2025  
**Người hướng dẫn:** AI Assistant

