# 🏥 HealthAdvisor - Trợ lý Sức khỏe Thông minh

> **Ứng dụng tư vấn y tế đa bệnh, thân thiện với người Việt Nam**  
> Hỗ trợ: Tim mạch, Tiểu đường, Thần kinh + AI Chatbot miễn phí

**Live Demo:** [healthadvisor.streamlit.app](https://healthadvisor.streamlit.app) *(Coming soon)*  
**GitHub:** [github.com/drvietcanh/healthadvisor](https://github.com/drvietcanh/healthadvisor)

---

## 🎯 Giới thiệu

**HealthAdvisor** là ứng dụng web giúp người dân:
- ✅ **Kiểm tra** huyết áp, đường huyết, BMI
- ✅ **Tìm hiểu** về các bệnh phổ biến (tăng huyết áp, tiểu đường, đột quỵ...)
- ✅ **Nhận tư vấn** về thuốc, dinh dưỡng, vận động
- ✅ **Chat với AI Bác sĩ** miễn phí (Google Gemini)
- ✅ **Theo dõi** nhật ký sức khỏe hàng ngày

### 🌟 Đặc điểm nổi bật:

- 🇻🇳 **Tiếng Việt 100%** - Ngôn ngữ đơn giản, dễ hiểu
- 💰 **Hoàn toàn MIỄN PHÍ** - Không quảng cáo, không ẩn phí
- 🌙 **Dark Mode** - Dễ nhìn ban đêm, tiết kiệm pin
- 📱 **Responsive** - Dùng được trên điện thoại, máy tính bảng
- 🤖 **AI Chatbot** - Hỏi đáp thông minh với Gemini Pro (miễn phí!)
- 📊 **Nhật ký sức khỏe** - Theo dõi huyết áp, đường huyết theo thời gian

---

## 🚀 Quick Start

### 1. Chạy local

```bash
# Clone repository
git clone https://github.com/drvietcanh/healthadvisor.git
cd healthadvisor

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy app
streamlit run app.py
```

Mở trình duyệt: `http://localhost:8501`

### 2. Deploy lên Streamlit Cloud

1. Fork repo này về GitHub của bạn
2. Vào [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect GitHub → Chọn repo `healthadvisor`
4. Deploy! (1 click)

**Chi tiết:** Xem [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

---

## 📚 Tính năng chính

### ❤️ **1. Tim Mạch**
- Đánh giá huyết áp (Bình thường → Nguy hiểm)
- Thông tin về tăng huyết áp, suy tim
- 5 nhóm thuốc huyết áp phổ biến tại Việt Nam
- Chế độ ăn DASH, giảm muối
- Vận động phù hợp

### 🩸 **2. Tiểu Đường**
- Chuyển đổi đơn vị: mmol/L ↔ mg/dL
- Thuốc uống + Insulin đầy đủ (5 loại)
- **GI & GL** - 60+ thực phẩm Việt Nam
- Đếm carb, phương pháp đĩa ăn
- Phòng ngừa hạ đường huyết

### 🧠 **3. Thần Kinh**
- **BE-FAST** - Nhận biết đột quỵ
- ⚠️ **GỌI 115 NGAY** khi có dấu hiệu
- Động kinh - Xử trí cơn co giật
- Phòng ngừa tái phát

### 🤖 **4. AI Bác Sĩ**
- Chat thông minh với Google Gemini Pro
- Hỗ trợ cả OpenAI (ChatGPT) nếu có API key
- Tư vấn theo chuyên khoa: Tim mạch, Tiểu đường, Thần kinh
- Quick replies & Suggested questions
- **MIỄN PHÍ 100%** (nếu dùng Gemini)

### 🎓 **5. Học Dễ**
- Giải thích y khoa bằng hình ảnh, ví dụ đời thường
- Mẹo nhớ dễ dàng
- So sánh trực quan
- Không dùng từ chuyên môn quá sâu

### 📊 **6. Nhật Ký Sức Khỏe** ⭐ MỚI!
**Tính năng:**
- ✅ Nhập đầy đủ: Huyết áp, Mạch, Đường huyết, HbA1c, Mỡ máu, Acid Uric, Chức năng thận, Cân nặng
- ✅ Biểu đồ đẹp theo thời gian (Plotly)
- ✅ Thống kê tổng quan
- ✅ Export/Import CSV (tương thích Excel)
- ✅ Hướng dẫn đo huyết áp đúng chuẩn (WHO/AHA)
- ✅ Hướng dẫn lưu/tải file chi tiết

**Cách dùng:**
1. Nhập dữ liệu hàng ngày
2. Xem biểu đồ xu hướng
3. Tải xuống CSV để backup
4. Lần sau tải lên để xem lại

---

## 🏗️ Cấu trúc dự án

```
healthadvisor/
├── app.py                          # Main entry point
├── requirements.txt                # Dependencies
├── README.md                       # File này
├── PROGRESS.md                     # Tiến độ dự án
├── ROADMAP_PHAT_TRIEN.md          # Lộ trình phát triển
│
├── core/                           # Core utilities
│   ├── ui_config.py               # Dark mode CSS
│   ├── chatbot_enhanced.py        # AI chatbot (Gemini + OpenAI)
│   ├── utils.py                   # Helper functions
│   ├── models.py                  # Pydantic models
│   ├── prompts.py                 # AI prompts
│   └── simple_explanations.py     # Easy learning content
│
├── pages/                          # Streamlit pages
│   ├── 0_📖_Hướng_Dẫn.py          # User guide
│   ├── 1_❤️_Tim_Mạch.py           # Cardiovascular
│   ├── 2_🩸_Tiểu_Đường.py         # Diabetes
│   ├── 3_🧠_Thần_Kinh.py          # Neurological
│   ├── 4_🤖_AI_Bác_Sĩ.py          # AI Chatbot
│   ├── 5_🎓_Học_Dễ.py             # Easy learning
│   ├── 6_📊_Nhật_Ký.py            # Health diary (REFACTORED!)
│   └── diary_components/          # Modular components
│       ├── input_form.py
│       ├── charts.py
│       ├── instructions.py
│       └── data_manager.py
│
└── diseases/                       # Disease modules
    ├── cardiovascular/
    │   ├── hypertension.py        # Tăng huyết áp
    │   └── heart_failure.py       # Suy tim
    │
    ├── metabolic/
    │   └── diabetes/              # Modular diabetes
    │       ├── info.py
    │       ├── medications.py
    │       ├── insulin.py
    │       ├── nutrition/         # (Đang refactor)
    │       └── exercise.py
    │
    └── neurological/
        ├── stroke.py              # Đột quỵ
        └── epilepsy.py            # Động kinh
```

---

## 🛠️ Tech Stack

- **Framework:** [Streamlit](https://streamlit.io/) 1.38+
- **Language:** Python 3.10+
- **AI:** Google Gemini Pro / OpenAI GPT-3.5+
- **Charts:** Plotly
- **Data:** Pandas
- **Validation:** Pydantic

---

## 📖 Tài liệu

### Cho người dùng:
- **[Hướng dẫn sử dụng](pages/0_📖_Hướng_Dẫn.py)** - Trong app
- **[Hướng dẫn lấy Gemini API](HUONG_DAN_GEMINI.md)** - Chi tiết từng bước

### Cho developer:
- **[PROGRESS.md](PROGRESS.md)** - Tiến độ & roadmap
- **[REFACTOR_PLAN.md](REFACTOR_PLAN.md)** - Kế hoạch refactor
- **[ROADMAP_PHAT_TRIEN.md](ROADMAP_PHAT_TRIEN.md)** - Tính năng tương lai
- **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)** - Hướng dẫn deploy

---

## 🎨 Screenshots

### 🏠 Trang chủ với Dark Mode
![Home](docs/screenshots/home.png) *(Coming soon)*

### 📊 Nhật ký Sức khỏe
![Diary](docs/screenshots/diary.png) *(Coming soon)*

### 🤖 AI Chatbot
![Chatbot](docs/screenshots/chatbot.png) *(Coming soon)*

---

## 🚧 Tình trạng phát triển

### ✅ Hoàn thành:
- [x] Dark Mode & UI responsive
- [x] Trang Hướng dẫn đầy đủ
- [x] Gemini API integration
- [x] Nhật ký Sức khỏe (modular, 170 dòng)
- [x] 60+ thực phẩm VN với GI/GL
- [x] Thuốc VN brands (Huyết áp + Tiểu đường)
- [x] Hướng dẫn đo huyết áp chuẩn WHO/AHA

### 🔄 Đang làm:
- [ ] Refactor nutrition.py (672 → 3 files)
- [ ] Refactor hypertension.py (609 → 3 files)
- [ ] Refactor heart_failure.py (597 → 3 files)

### 📝 Kế hoạch:
- [ ] Tìm bác sĩ/bệnh viện gần nhất
- [ ] Kiểm tra tương tác thuốc
- [ ] Gamification (điểm, streaks)
- [ ] Nhắc nhở uống thuốc

**Chi tiết:** Xem [ROADMAP_PHAT_TRIEN.md](ROADMAP_PHAT_TRIEN.md)

---

## 🤝 Đóng góp

Chúng tôi rất hoan nghênh mọi đóng góp! 

### Cách đóng góp:
1. Fork repo
2. Tạo branch mới: `git checkout -b feature/TenTinhNang`
3. Commit: `git commit -m "Thêm tính năng X"`
4. Push: `git push origin feature/TenTinhNang`
5. Tạo Pull Request

### Có thể giúp:
- 🐛 Báo lỗi (Issues)
- 💡 Đề xuất tính năng
- 📝 Cải thiện tài liệu
- 🌐 Dịch nội dung
- 🩺 Thêm thông tin y khoa
- 💊 Cập nhật database thuốc VN

---

## ⚠️ Lưu ý quan trọng

### Disclaimer:

> **App này CHỈ dùng để TƯ VẤN và GIÁO DỤC.**  
> **KHÔNG THAY THẾ** bác sĩ hoặc khám bệnh chuyên nghiệp.
>
> - ❌ KHÔNG tự ý thay đổi thuốc
> - ❌ KHÔNG tự chẩn đoán bệnh
> - ✅ LUÔN tham khảo ý kiến bác sĩ khi có bệnh
> - ✅ Gọi 115 khi có dấu hiệu nguy hiểm

### Nguồn thông tin:
- American Heart Association (AHA)
- American Diabetes Association (ADA)
- World Health Organization (WHO)
- Bộ Y tế Việt Nam
- Các bệnh viện uy tín (Mayo Clinic, Cleveland Clinic...)

---

## 📞 Liên hệ

- **GitHub Issues:** [github.com/drvietcanh/healthadvisor/issues](https://github.com/drvietcanh/healthadvisor/issues)
- **Email:** *(Thêm email nếu muốn)*
- **Facebook:** *(Thêm fanpage nếu có)*

---

## 📜 License

- **Code:** MIT License
- **Content:** CC BY-NC 4.0 (Attribution-NonCommercial)

---

## 🙏 Credits

**Được phát triển với ❤️ cho cộng đồng Việt Nam**

### Công nghệ sử dụng:
- [Streamlit](https://streamlit.io/) - Web framework
- [Google Gemini](https://ai.google.dev/) - AI chatbot
- [Plotly](https://plotly.com/) - Interactive charts
- [Pandas](https://pandas.pydata.org/) - Data processing

### Nguồn y khoa:
- AHA/ASA Guidelines
- ADA Standards of Care
- WHO Health Topics
- Dược điển Việt Nam

---

## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/drvietcanh/healthadvisor?style=social)
![GitHub forks](https://img.shields.io/github/forks/drvietcanh/healthadvisor?style=social)
![GitHub issues](https://img.shields.io/github/issues/drvietcanh/healthadvisor)
![GitHub license](https://img.shields.io/github/license/drvietcanh/healthadvisor)

---

**Made with ❤️ for Vietnamese Healthcare**  
© 2025 HealthAdvisor Contributors
