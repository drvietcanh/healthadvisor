# 🚀 GIAI ĐOẠN 1 - QUICK WINS (Tuần 1-2)

**Mục tiêu:** Cải thiện nhanh trải nghiệm người dùng với các tính năng dễ triển khai, hiệu quả cao

---

## ✅ DANH SÁCH CÔNG VIỆC

### **1. 📂 SẮP XẾP LẠI MENU THEO PRIORITY**

#### **1.1. Tạo menu nhóm theo mức độ ưu tiên**
**File cần chỉnh:** `core/sidebar_menu.py`

**Cấu trúc đề xuất:**
```
📂 MENU CHÍNH (Priority 1 - Quan trọng nhất)
├── 🆘 SOS - Cấp Cứu (ĐƯA LÊN ĐẦU)
├── ❤️ Tim Mạch
├── 🩸 Tiểu Đường  
├── 🧠 Thần Kinh
└── 🫁 Hô Hấp

📂 CHUYÊN KHOA (Priority 2)
├── 🦴 Khớp - Cột Sống
├── ⚖️ Hội Chứng Chuyển Hóa
├── 🧪 Thận-Tiết Niệu
├── 👁️ Mắt
└── 🌡️ Tiêu Hóa

📂 HỖ TRỢ (Priority 3)
├── 💡 Mẹo Vặt
├── 🎓 Học Dễ
├── 📖 Hướng Dẫn
└── 🤖 AI Bác Sĩ

📂 CÔNG CỤ (Priority 4)
├── 💊 Nhắc Thuốc
├── 📊 Nhật Ký
└── 📈 Xu Hướng
```

**Công việc:**
- [ ] Chia menu thành 4 nhóm với tiêu đề rõ ràng
- [ ] Thêm divider giữa các nhóm
- [ ] Thêm icon 📂 cho mỗi nhóm
- [ ] Đảm bảo mobile responsive
- [ ] Test trên mobile

**Thời gian ước tính:** 1-2 giờ

---

#### **1.2. Thêm nút "Nhảy đến SOS" nhanh ở trang chủ**
**File cần chỉnh:** `app.py`

**Mô tả:** Thêm nút lớn, nổi bật ở trang chủ để truy cập nhanh SOS

**Công việc:**
- [ ] Thêm nút "🆘 SOS - Cấp Cứu" ở phần Quick Actions
- [ ] Làm nút to, màu đỏ, dễ nhìn
- [ ] Đặt ở vị trí đầu tiên trong Quick Actions

**Thời gian ước tính:** 30 phút

---

### **2. 🔍 THÊM SEARCH BAR (Tìm kiếm thông minh)**

#### **2.1. Tạo component Search Bar**
**File cần tạo:** `core/search_component.py`

**Chức năng:**
- Search bar ở top của sidebar (hoặc top bar)
- Tìm kiếm theo:
  - Tên bệnh
  - Triệu chứng
  - Tên trang
  - Mẹo vặt
- Autocomplete với gợi ý
- Lịch sử tìm kiếm (5 mục gần nhất)

**Công việc:**
- [ ] Tạo file `core/search_component.py`
- [ ] Tạo hàm `render_search_bar()` 
- [ ] Tạo dictionary/lookup table cho tất cả bệnh, triệu chứng
- [ ] Implement fuzzy search (hoặc exact match)
- [ ] Hiển thị kết quả với link đến trang tương ứng
- [ ] Lưu lịch sử vào session_state
- [ ] Thêm vào sidebar_menu.py

**Thời gian ước tính:** 4-6 giờ

---

#### **2.2. Tạo trang kết quả tìm kiếm**
**File cần tạo:** `pages/_🔍_Tìm_Kiếm.py`

**Mô tả:** Trang hiển thị kết quả tìm kiếm chi tiết

**Công việc:**
- [ ] Tạo trang mới
- [ ] Hiển thị kết quả theo loại (Bệnh, Mẹo, SOS...)
- [ ] Highlight từ khóa tìm kiếm
- [ ] Nút "Quay lại tìm kiếm"

**Thời gian ước tính:** 2-3 giờ

---

### **3. ⭐ THÊM FAVORITES/BOOKMARKS (Yêu thích)**

#### **3.1. Tạo hệ thống Favorites**
**File cần tạo:** `core/favorites_manager.py`

**Chức năng:**
- Nút "⭐ Đánh dấu" ở mỗi trang bệnh
- Lưu danh sách trang yêu thích
- Hiển thị trong sidebar hoặc trang chủ
- Quick access từ sidebar

**Công việc:**
- [ ] Tạo `core/favorites_manager.py`
- [ ] Lưu favorites vào session_state (hoặc localStorage với JavaScript)
- [ ] Thêm nút "⭐ Thêm vào Yêu thích" / "⭐ Bỏ yêu thích" ở mỗi trang
- [ ] Tạo section "⭐ Yêu thích của tôi" trong sidebar
- [ ] Hiển thị danh sách favorites (tối đa 10 mục)
- [ ] Thêm vào sidebar_menu.py

**Thời gian ước tính:** 3-4 giờ

---

#### **3.2. Thêm Quick Access từ trang chủ**
**File cần chỉnh:** `app.py`

**Mô tả:** Hiển thị favorites ở trang chủ nếu có

**Công việc:**
- [ ] Thêm section "⭐ Trang của tôi" ở trang chủ
- [ ] Hiển thị danh sách favorites với link
- [ ] Chỉ hiển thị nếu có favorites

**Thời gian ước tính:** 1 giờ

---

### **4. 📋 THÊM RECENT (Gần đây)**

#### **4.1. Theo dõi lịch sử xem trang**
**File cần tạo:** `core/recent_pages.py`

**Chức năng:**
- Tự động lưu trang đã xem vào session_state
- Lưu tối đa 10 trang gần nhất
- Hiển thị trong sidebar

**Công việc:**
- [ ] Tạo `core/recent_pages.py`
- [ ] Hàm `add_to_recent(page_name, page_label)`
- [ ] Hàm `get_recent_pages()` - trả về 5-10 trang gần nhất
- [ ] Tạo hàm `render_recent_pages()` để hiển thị
- [ ] Gọi `add_to_recent()` ở mỗi trang khi load
- [ ] Thêm section "📋 Đã xem gần đây" vào sidebar

**Thời gian ước tính:** 2-3 giờ

---

### **5. 🔤 THÊM FONT SIÊU LỚN MODE (Extra Large Font)**

#### **5.1. Tạo toggle Font siêu lớn**
**File cần chỉnh:** 
- `core/ui_config.py`
- `core/dark_mode_css.py`
- `core/light_mode_css.py`

**Mô tả:** Tăng font lên 22-24px (thay vì 18-20px hiện tại)

**Công việc:**
- [ ] Thêm state `extra_large_font` vào session_state
- [ ] Tạo toggle trong sidebar (bên cạnh Dark Mode)
- [ ] Tạo CSS riêng cho font siêu lớn:
  - p, li, span: 22-24px
  - h1: 2.5rem
  - h2: 2rem
  - h3: 1.75rem
- [ ] Áp dụng cho cả dark và light mode
- [ ] Test trên mobile

**Thời gian ước tính:** 2-3 giờ

---

### **6. 💡 BỔ SUNG 5 MẸO VẶT MỚI**

#### **6.1. Mẹo về thuốc (3 mẹo)**
**File cần chỉnh:** `health_tips/daily_tips.py` hoặc tạo file mới

**Nội dung cần bổ sung:**

**Mẹo 1: Cách nhớ uống thuốc đúng giờ**
- Dùng hộp thuốc 7 ngày (chia sáng/trưa/chiều/tối)
- Đặt báo thức điện thoại
- Dán nhãn màu trên hộp thuốc
- Đặt thuốc ở nơi dễ nhìn (cạnh giường, bàn ăn)

**Mẹo 2: Cách uống thuốc đúng cách**
- Uống trước ăn: 30-60 phút trước ăn (ví dụ: Omeprazole)
- Uống sau ăn: 30 phút sau ăn (ví dụ: Aspirin, Paracetamol)
- Uống với nước: Ít nhất 1 cốc nước (200ml)
- Không uống với nước trái cây, sữa (trừ khi bác sĩ chỉ định)

**Mẹo 3: Thuốc nào không uống chung**
- Không uống kháng sinh với sữa (giảm hấp thu)
- Không uống sắt với trà/cà phê (giảm hấp thu)
- Không uống thuốc với rượu bia
- Hỏi bác sĩ trước khi uống nhiều thuốc cùng lúc

**Công việc:**
- [ ] Tạo section mới "Mẹo về Thuốc"
- [ ] Thêm 3 mẹo trên vào `health_tips/daily_tips.py`
- [ ] Format đẹp, dễ đọc
- [ ] Thêm icon phù hợp

**Thời gian ước tính:** 2 giờ

---

#### **6.2. Mẹo dinh dưỡng (2 mẹo)**
**File cần chỉnh:** `health_tips/daily_tips.py`

**Nội dung cần bổ sung:**

**Mẹo 4: Thực đơn cho người già dễ nhai**
- Nấu chín mềm (luộc, hầm)
- Cắt nhỏ, xay nhuyễn (cho người răng yếu)
- Tránh thức ăn cứng, dai (thịt gà, bánh mì khô)
- Ưu tiên: Cá, đậu phụ, trứng, rau luộc mềm

**Mẹo 5: Cách nấu ăn ít muối nhưng vẫn ngon**
- Dùng gia vị thay muối: Chanh, tỏi, hành, gừng, ớt
- Nêm nhạt khi nấu, để người ăn tự thêm nếu cần
- Dùng nước mắm thay muối (nhưng cũng có muối)
- Ăn nhiều rau củ tự nhiên (có vị ngọt tự nhiên)

**Công việc:**
- [ ] Tạo section "Mẹo Dinh Dưỡng"
- [ ] Thêm 2 mẹo trên
- [ ] Thêm ví dụ cụ thể

**Thời gian ước tính:** 1.5 giờ

---

## 📊 TỔNG KẾT GIAI ĐOẠN 1

### **Số lượng công việc:** 10 tasks
### **Thời gian ước tính:** 20-26 giờ (~2.5-3.5 ngày làm việc)

### **Thứ tự ưu tiên đề xuất:**

**Nhóm 1 - Quan trọng nhất (Làm trước):**
1. ✅ Sắp xếp lại menu theo priority (1-2h)
2. ✅ Thêm nút SOS nhanh ở trang chủ (30 phút)
3. ✅ Thêm Font siêu lớn mode (2-3h)

**Nhóm 2 - Cải thiện trải nghiệm (Làm tiếp):**
4. ✅ Thêm Search Bar (4-6h)
5. ✅ Thêm Favorites (3-4h)
6. ✅ Thêm Recent pages (2-3h)

**Nhóm 3 - Nội dung (Làm cuối):**
7. ✅ Bổ sung 5 mẹo vặt mới (3.5h)

---

## 🎯 LỢI ÍCH SAU GIAI ĐOẠN 1

- ✅ Menu dễ điều hướng hơn, rõ ràng hơn
- ✅ Tìm kiếm nhanh chóng
- ✅ Truy cập nhanh các trang thường dùng
- ✅ Font lớn hơn cho người già mắt kém
- ✅ Thêm nhiều mẹo vặt hữu ích

---

## 📝 LƯU Ý KHI THỰC HIỆN

1. **Commit sau mỗi task:** Hoàn thành task → commit → push
2. **Test trên mobile:** Mọi thay đổi cần test trên mobile
3. **Giữ đơn giản:** Không làm phức tạp quá
4. **Giữ font lớn:** Đảm bảo vẫn dễ đọc cho người già
5. **Backward compatible:** Không phá vỡ chức năng hiện có

---

## ✅ CHECKLIST HOÀN THÀNH GIAI ĐOẠN 1

- [ ] Menu đã sắp xếp lại theo priority
- [ ] Nút SOS nhanh ở trang chủ
- [ ] Search Bar hoạt động tốt
- [ ] Favorites lưu và hiển thị đúng
- [ ] Recent pages hoạt động
- [ ] Font siêu lớn mode hoạt động
- [ ] 5 mẹo vặt mới đã thêm
- [ ] Test trên desktop
- [ ] Test trên mobile
- [ ] Commit và push tất cả thay đổi

---

**Sẵn sàng bắt đầu! Chọn task bạn muốn làm trước.** 🚀

