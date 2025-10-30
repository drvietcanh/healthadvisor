# 🌟 Hướng dẫn lấy Gemini API và tích hợp vào HealthAdvisor

## Bước 1: Lấy Gemini API Key (MIỄN PHÍ!)

### Cách lấy API Key:

1. **Truy cập Google AI Studio:**
   - Mở trình duyệt, vào: https://aistudio.google.com/app/apikey
   - Đăng nhập bằng tài khoản Google của bạn

2. **Tạo API Key:**
   - Click vào nút **"Get API key"** hoặc **"Create API key"**
   - Chọn **"Create API key in new project"**
   - Sao chép API key (dạng: `AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`)

3. **Lưu API Key:**
   - 🚨 **QUAN TRỌNG:** KHÔNG chia sẻ API key này với ai!
   - Lưu vào nơi an toàn (notepad, file riêng)

---

## Bước 2: Cài đặt thư viện Gemini

Mở Terminal/PowerShell trong thư mục dự án và chạy:

```bash
pip install google-generativeai
```

---

## Bước 3: Cập nhật file `requirements.txt`

Thêm dòng này vào cuối file `requirements.txt`:

```
google-generativeai>=0.3.0
```

---

## Bước 4: Tạo file chatbot hỗ trợ cả OpenAI và Gemini

### File mới: `core/chatbot_multi.py`

Tôi sẽ tạo chatbot có thể dùng cả OpenAI VÀ Gemini!

---

## Bước 5: Cập nhật trang AI Bác Sĩ

Trang `pages/4_🤖_AI_Bác_Sĩ.py` sẽ cho phép bạn chọn:
- ✅ **Gemini** (MIỄN PHÍ, tốt cho người Việt!)
- ✅ **OpenAI** (Nếu bạn có API key)

---

## Ưu điểm Gemini cho dự án này:

| Tiêu chí | Gemini Pro | OpenAI GPT-3.5/4 |
|----------|------------|------------------|
| **Giá** | ✅ MIỄN PHÍ (60 requests/phút) | ❌ Trả phí |
| **Tiếng Việt** | ✅ Rất tốt | ✅ Tốt |
| **Tốc độ** | ✅ Nhanh | ✅ Nhanh |
| **Độ chính xác** | ✅ Cao | ✅ Rất cao |
| **Giới hạn** | 60 requests/phút (đủ cho bệnh nhân dùng) | Theo gói trả phí |

---

## Cách sử dụng trong app:

1. **Mở app Streamlit**
2. **Vào trang "🤖 AI Bác Sĩ"**
3. **Sidebar → Chọn "AI Provider":**
   - Chọn **Gemini** (khuyến nghị!)
   - Nhập API key vào ô
4. **Bắt đầu chat!**

---

## Lưu API Key an toàn trên Streamlit Cloud:

### Khi deploy lên Streamlit Cloud:

1. Vào **Streamlit Cloud Dashboard**
2. Click vào app của bạn
3. Click **"Settings"** (⚙️)
4. Click **"Secrets"**
5. Thêm dòng này:

```toml
GEMINI_API_KEY = "AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
```

6. Click **"Save"**

Sau đó app sẽ tự động dùng API key này, người dùng không cần nhập!

---

## Kiểm tra API Key có hoạt động không:

Chạy lệnh này trong Python:

```python
import google.generativeai as genai

# Thay YOUR_API_KEY bằng key thật của bạn
genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Xin chào! Huyết áp bao nhiêu là bình thường?")
print(response.text)
```

Nếu có kết quả → ✅ API key hoạt động!

---

## Troubleshooting:

### Lỗi: "API key not valid"
- Kiểm tra lại API key đã copy đúng chưa
- Đảm bảo không có khoảng trắng thừa

### Lỗi: "Resource exhausted"
- Bạn đã vượt quá 60 requests/phút
- Đợi 1 phút rồi thử lại

### Lỗi: "Module not found: google.generativeai"
- Chạy lại: `pip install google-generativeai`

---

## 🎉 Kết luận:

✅ Gemini API **MIỄN PHÍ**, rất phù hợp cho dự án y tế  
✅ Tiếng Việt tự nhiên  
✅ Dễ tích hợp  
✅ Không lo hết tiền như OpenAI  

**Khuyến nghị:** Dùng Gemini cho dự án này! 🚀

