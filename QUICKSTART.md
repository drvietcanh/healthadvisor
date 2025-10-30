# 🚀 Hướng dẫn Chạy Nhanh - HealthAdvisor

## Bước 1: Cài đặt thư viện

```bash
pip install -r requirements.txt
```

## Bước 2: Chạy ứng dụng

```bash
streamlit run app.py
```

## Bước 3: Mở trình duyệt

Tự động mở tại: `http://localhost:8501`

Nếu không tự mở, copy link trên vào trình duyệt.

---

## 💡 Sử dụng AI Chatbot (Tùy chọn)

Nếu muốn dùng AI Chatbot thật (cần OpenAI API):

1. Tạo file `.streamlit/secrets.toml`
2. Thêm API key:
```toml
OPENAI_API_KEY = "sk-your-openai-api-key-here"
```
3. Lưu và khởi động lại app

> Nếu không có API key, chatbot vẫn hoạt động với câu trả lời mẫu.

---

## 🎯 Tính năng chính

✅ Tư vấn **Tim Mạch** (Tăng huyết áp, Suy tim)  
✅ Tư vấn **Tiểu Đường** (Típ 1, Típ 2)  
✅ Tư vấn **Thần Kinh** (Đột quỵ, Động kinh)  
✅ **AI Bác sĩ** trò chuyện 24/7  
✅ Công cụ đo huyết áp, chuyển đổi đường huyết, tính BMI  

---

## ⚠️ Lưu ý

- App chỉ **tham khảo**, không thay thế bác sĩ
- Triệu chứng cấp cứu → **GỌI 115 NGAY**

---

Chúc bạn sử dụng app hiệu quả! 😊

