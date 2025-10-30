# 🏥 HealthAdvisor - Ứng dụng Tư vấn Sức khỏe Đa Bệnh

> **Mục đích**: Ứng dụng tư vấn y tế thông minh sử dụng AI, giúp người dân hiểu rõ về bệnh lý, chế độ ăn uống, sinh hoạt và theo dõi sức khỏe tại nhà.

> **Đối tượng**: Bệnh nhân, người nhà, người quan tâm đến sức khỏe

> **An toàn**: **KHÔNG THAY THẾ** bác sĩ - Chỉ tham khảo. Triệu chứng cấp cứu → **GỌI 115 NGAY**

---

## 🚀 Chạy ứng dụng nhanh

```bash
# Cài đặt thư viện
pip install -r requirements.txt

# Chạy app
streamlit run app.py
```

Mở trình duyệt tại: `http://localhost:8501`

---

## 📁 Cấu trúc dự án

```
healthadvisor/
├── app.py                          # Trang chính
├── pages/
│   ├── 1_❤️_Tim_Mạch.py           # Trang tư vấn tim mạch
│   ├── 2_🩸_Tiểu_Đường.py          # Trang tư vấn tiểu đường
│   ├── 3_🧠_Thần_Kinh.py           # Trang tư vấn thần kinh
│   └── 4_🤖_AI_Bác_Sĩ.py           # Chatbot AI tư vấn
├── core/
│   ├── models.py                    # Pydantic models
│   ├── chatbot.py                   # AI Chatbot engine
│   ├── prompts.py                   # System prompts cho AI
│   ├── utils.py                     # Hàm tiện ích
│   └── rules.py                     # Logic phân loại (nếu cần)
├── diseases/
│   ├── cardiovascular/
│   │   ├── hypertension.py         # Module tăng huyết áp
│   │   └── heart_failure.py        # Module suy tim
│   ├── metabolic/
│   │   └── diabetes.py             # Module tiểu đường
│   └── neurological/
│       └── (các module thần kinh)
├── .streamlit/
│   └── config.toml                  # Cấu hình Streamlit
├── requirements.txt                 # Thư viện Python
├── .gitignore
└── README.md
```

---

## 🎯 Tính năng chính

### 1. ❤️ Tư vấn Tim Mạch
- **Tăng huyết áp**: 
  - Phân loại huyết áp
  - Thuốc điều trị (giải thích đơn giản)
  - Chế độ ăn DASH (ít muối)
  - Vận động an toàn
  
- **Suy tim**:
  - 5 dấu hiệu nhận biết (5 chữ H)
  - Hướng dẫn thuốc (ngôn ngữ dễ hiểu)
  - Hạn chế muối/nước
  - Theo dõi tại nhà

- **Công cụ đo huyết áp**: Nhập số liệu → Phân loại tự động

### 2. 🩸 Tư vấn Tiểu Đường
- **Kiến thức cơ bản**:
  - Típ 1, Típ 2, Tiền tiểu đường
  - Dấu hiệu 3 chữ "NHIỀU"
  - Chỉ số đường huyết (mmol/L và mg/dL)
  
- **Thuốc điều trị**:
  - Metformin, Sulfonylurea, DPP-4i, SGLT-2i
  - Insulin: Các loại, cách tiêm
  - Xử trí hạ đường huyết
  
- **Chế độ ăn**:
  - Phương pháp đĩa ăn
  - Đếm carb (tinh bột)
  - Chỉ số GI
  - Thực đơn mẫu
  
- **Công cụ**:
  - Chuyển đổi mmol/L ↔ mg/dL
  - Tính BMI
  - Bảng đường huyết tham khảo

### 3. 🧠 Tư vấn Thần Kinh
- **Đột quỵ**:
  - BE-FAST: Nhận biết triệu chứng
  - Thời gian vàng điều trị
  - Phòng ngừa đột quỵ
  - **Công cụ kiểm tra BE-FAST**
  
- **Động kinh**:
  - Triệu chứng co giật
  - Xử trí cơn co giật (5 bước)
  - Khi nào gọi cấp cứu

### 4. 🤖 AI Bác Sĩ - Chatbot Thông Minh
- **Tính năng**:
  - Trò chuyện tư nhiên như bác sĩ thật
  - Trả lời câu hỏi theo chuyên khoa
  - Giải thích bằng ngôn ngữ dễ hiểu
  - Hỗ trợ 24/7
  
- **Chuyên khoa**:
  - 🏥 Tổng quát
  - ❤️ Tim mạch
  - 🩸 Tiểu đường
  - 🧠 Thần kinh
  
- **An toàn**:
  - Không chẩn đoán, không kê đơn
  - Luôn nhắc gọi 115 khi nguy hiểm
  - Khuyến khích gặp bác sĩ khi cần

---

## 🔧 Cài đặt chi tiết

### 1. Yêu cầu hệ thống
- Python 3.10 - 3.12
- pip

### 2. Cài đặt
```bash
# Clone repository
git clone <repo-url>
cd healthadvisor

# Tạo virtual environment (khuyên dùng)
python -m venv venv

# Kích hoạt venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Cài đặt thư viện
pip install -r requirements.txt
```

### 3. Cấu hình (Tùy chọn)

Nếu muốn dùng AI Chatbot, tạo file `.streamlit/secrets.toml`:

```toml
OPENAI_API_KEY = "sk-your-openai-api-key-here"
```

> **Lưu ý**: Nếu không có API key, chatbot sẽ dùng câu trả lời mẫu.

### 4. Chạy ứng dụng
```bash
streamlit run app.py
```

---

## 🌐 Triển khai lên Streamlit Cloud

### Bước 1: Đẩy code lên GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-github-repo-url>
git push -u origin main
```

### Bước 2: Triển khai trên Streamlit Cloud
1. Truy cập: https://share.streamlit.io
2. Đăng nhập bằng GitHub
3. Chọn repository vừa tạo
4. Chọn branch: `main`
5. Main file: `app.py`
6. Click **Deploy!**

### Bước 3: Thêm API Key (nếu dùng AI)
1. Vào app đã deploy
2. Settings > Secrets
3. Thêm:
```toml
OPENAI_API_KEY = "sk-your-key"
```
4. Save

---

## 📚 Nội dung y khoa

### Nguồn tham khảo
- Bộ Y tế Việt Nam (2024): Hướng dẫn chẩn đoán và điều trị các bệnh phổ biến
- AHA/ASA 2024: Hướng dẫn phòng ngừa đột quỵ, tim mạch
- WHO Guidelines: Tiểu đường, tăng huyết áp
- Các nghiên cứu y khoa uy tín (PubMed, Cochrane)

### Ngôn ngữ
- **Ưu tiên tiếng Việt** - Ngôn ngữ đơn giản, dễ hiểu
- Tránh thuật ngữ y khoa phức tạp
- Giải thích bằng ví dụ thực tế
- Cả 2 đơn vị: mmol/L và mg/dL (đường huyết)

---

## ⚠️ Tuyên bố miễn trách nhiệm

**QUAN TRỌNG - VUI LÒNG ĐỌC:**

1. Ứng dụng này chỉ cung cấp **thông tin tham khảo**, **KHÔNG THAY THẾ** bác sĩ hoặc chuyên gia y tế.

2. **KHÔNG tự ý chẩn đoán** hoặc **tự điều trị** dựa trên thông tin từ app.

3. Với các triệu chứng cấp cứu (đau ngực, khó thở, yếu liệt, co giật...): 
   **GỌI 115 NGAY** - Không trì hoãn!

4. Mọi quyết định điều trị phải được bác sĩ chỉ định.

5. Thông tin y khoa có thể thay đổi theo thời gian - Luôn tham khảo nguồn mới nhất.

6. Nhà phát triển **KHÔNG CHỊU TRÁCH NHIỆM** cho bất kỳ quyết định y tế nào dựa trên app.

---

## 🤝 Đóng góp

Mọi đóng góp đều được hoan nghênh! 

- Báo lỗi: Tạo Issue
- Đề xuất tính năng: Tạo Issue
- Sửa lỗi/cải tiến: Tạo Pull Request

---

## 📄 Giấy phép

MIT License - Xem file LICENSE

**Mục tiêu**: Nâng cao sức khỏe cộng đồng thông qua công nghệ

---

## 📞 Liên hệ cấp cứu (Việt Nam)

- **Cấp cứu**: 115
- **Tư vấn sức khỏe**: 1900 9095
- **Bệnh viện**: 114

---

© 2025 HealthAdvisor | Phát triển với ❤️ và AI

