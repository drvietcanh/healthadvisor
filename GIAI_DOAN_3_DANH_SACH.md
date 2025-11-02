# 🚀 GIAI ĐOẠN 3 - DANH SÁCH CÔNG VIỆC

**Cập nhật:** 03/01/2025  
**Mục tiêu:** Mở rộng tính năng và nội dung  
**Thời gian ước tính:** 40-50 giờ

---

## 📋 **DANH SÁCH CÔNG VIỆC GIAI ĐOẠN 3**

### **3.1. 🤔 Symptom Checker (Đánh giá triệu chứng)**

**Mô tả:** Hệ thống hỏi đáp các triệu chứng và đề xuất khả năng bệnh (với disclaimer rõ ràng)

**Tính năng:**
- ✅ Hỏi đáp các triệu chứng (multi-step form)
- ✅ Đề xuất khả năng bệnh (với disclaimer "CHỈ THAM KHẢO")
- ✅ Gợi ý nên đi khám chuyên khoa nào
- ✅ Lưu lịch sử đánh giá
- ✅ Hiển thị mức độ khẩn cấp (không khẩn cấp / cần khám sớm / cần cấp cứu)

**Files cần tạo:**
- `symptom_checker/` - Module chính
  - `symptom_questions.py` - Database câu hỏi triệu chứng
  - `symptom_analyzer.py` - Logic phân tích và đề xuất
  - `specialist_recommender.py` - Gợi ý chuyên khoa
  - `render_ui.py` - UI cho symptom checker
- `pages/_🔍_Đánh_Giá_Triệu_Chứng.py` - Trang chính

**Ước tính:** 8-10 giờ  
**Độ khó:** ⭐⭐⭐ Trung bình

---

### **3.2. ⏰ Nhắc thuốc nâng cao**

**Mô tả:** Nâng cấp tính năng nhắc thuốc hiện tại với các tính năng mới

**Tính năng mới:**
- ✅ Nhắc nhở nhiều lần/ngày (hiện tại chỉ 1 lần)
- ✅ Thống kê uống thuốc đúng giờ (% tuân thủ)
- ✅ Cảnh báo tương tác thuốc (drug interactions)
- ✅ Gợi ý liều lượng dựa trên cân nặng/tuổi
- ✅ Nhắc nhở khi sắp hết thuốc (dựa trên số viên còn lại)
- ✅ Xuất báo cáo tuân thủ thuốc (PDF/CSV)

**Files cần sửa/thêm:**
- `medication_reminder/` - Module hiện tại
  - `drug_interactions.py` - Database tương tác thuốc (MỚI)
  - `dose_calculator.py` - Tính liều lượng (MỚI)
  - `compliance_analyzer.py` - Phân tích tuân thủ (MỚI)
  - `scheduler.py` - Cần nâng cấp (hỗ trợ nhiều lần/ngày)
  - `medication_manager.py` - Cần thêm tính năng hết thuốc

**Ước tính:** 10-12 giờ  
**Độ khó:** ⭐⭐⭐⭐ Khó (cần database tương tác thuốc)

---

### **3.3. 📅 Lịch khám bệnh**

**Mô tả:** Quản lý lịch khám bệnh, nhắc nhở, lưu thông tin bác sĩ/bệnh viện

**Tính năng:**
- ✅ Tạo lịch khám (ngày, giờ, bác sĩ, bệnh viện)
- ✅ Nhắc nhở trước 1 ngày, 1 giờ
- ✅ Lưu địa chỉ bác sĩ/bệnh viện (có thể tích hợp Google Maps sau)
- ✅ Ghi chú triệu chứng trước khi khám
- ✅ Lưu kết quả khám (sau khi đi khám về)
- ✅ Lịch sử khám bệnh (xem lại)
- ✅ Xuất lịch khám (PDF/CSV)

**Files cần tạo:**
- `appointment_scheduler/` - Module mới
  - `appointment_manager.py` - Quản lý lịch khám
  - `reminder_system.py` - Hệ thống nhắc nhở
  - `doctor_directory.py` - Danh sách bác sĩ/bệnh viện
  - `visit_history.py` - Lịch sử khám
  - `render_ui.py` - UI
- `pages/_📅_Lịch_Khám.py` - Trang chính

**Ước tính:** 8-10 giờ  
**Độ khó:** ⭐⭐ Dễ-Trung bình

---

### **3.4. 🦋 Tạo trang Da Liễu (5 bệnh)**

**Mô tả:** Tạo trang chuyên khoa Da Liễu với 5 bệnh phổ biến

**Danh sách bệnh:**
1. **Nấm da (Tinea/Dermatophytosis)**
   - Nấm da chân, nấm da đùi, nấm da tay
   - Nguyên nhân, triệu chứng, điều trị
   - Phòng ngừa

2. **Nấm móng (Onychomycosis)**
   - Nấm móng tay, móng chân
   - Điều trị tại nhà vs cần bác sĩ
   - Mẹo phòng ngừa

3. **Chàm khô (Eczema/Dermatitis)**
   - Chàm thể tạng, viêm da tiếp xúc
   - Nguyên nhân (dị ứng, kích ứng)
   - Chăm sóc da, thuốc bôi

4. **Ngứa da (Pruritus)**
   - Ngứa không có tổn thương da
   - Nguyên nhân (da khô, bệnh nội khoa)
   - Xử trí tại nhà

5. **Vết loét do nằm lâu (Pressure Ulcer/Bedsores)**
   - Loét tì đè ở người già nằm liệt
   - Phân độ (1-4)
   - Chăm sóc, phòng ngừa
   - Khi nào cần bác sĩ

**Files cần tạo:**
- `diseases/dermatology/` - Module bệnh da liễu
  - `tinea.py` - Nấm da
  - `onychomycosis.py` - Nấm móng
  - `eczema.py` - Chàm khô
  - `pruritus.py` - Ngứa da
  - `pressure_ulcer.py` - Loét tì đè
  - `__init__.py`
- `dermatology_page_components/` - UI components
  - `tinea_tab.py`
  - `onychomycosis_tab.py`
  - `eczema_tab.py`
  - `pruritus_tab.py`
  - `pressure_ulcer_tab.py`
  - `__init__.py`
- `pages/14_🦋_Da_Liễu.py` - Trang chính

**Ước tính:** 10-12 giờ  
**Độ khó:** ⭐⭐⭐ Trung bình

---

### **3.5. 👂 Tạo trang Tai Mũi Họng (5 bệnh)**

**Mô tả:** Tạo trang chuyên khoa Tai Mũi Họng với 5 bệnh phổ biến

**Danh sách bệnh:**
1. **Điếc/Lãng tai (Hearing Loss)**
   - Điếc tuổi già (Presbycusis)
   - Điếc do tiếng ồn
   - Dấu hiệu nhận biết
   - Máy trợ thính
   - Phòng ngừa

2. **Ù tai (Tinnitus)**
   - Ù tai đơn thuần (không kèm điếc)
   - Nguyên nhân (nhiễm trùng, tiếng ồn, bệnh nền)
   - Xử trí tại nhà
   - Khi nào cần bác sĩ

3. **Viêm họng mạn tính (Chronic Pharyngitis)**
   - Viêm họng hạt
   - Nguyên nhân (hút thuốc, môi trường, trào ngược)
   - Điều trị, phòng ngừa

4. **Chóng mặt/Vertigo (Dizziness)**
   - Chóng mặt tư thế (BPPV)
   - Viêm tiền đình
   - Phân biệt chóng mặt vs choáng váng
   - Xử trí tại nhà
   - Khi nào cần cấp cứu

5. **Viêm tai giữa (Otitis Media)**
   - Viêm tai giữa cấp (trẻ em)
   - Viêm tai giữa mạn (người lớn)
   - Triệu chứng, điều trị
   - Phòng ngừa

**Files cần tạo:**
- `diseases/ent/` - Module Tai Mũi Họng
  - `hearing_loss.py` - Điếc/Lãng tai
  - `tinnitus.py` - Ù tai
  - `chronic_pharyngitis.py` - Viêm họng mạn
  - `vertigo.py` - Chóng mặt
  - `otitis_media.py` - Viêm tai giữa
  - `__init__.py`
- `ent_page_components/` - UI components
  - `hearing_loss_tab.py`
  - `tinnitus_tab.py`
  - `chronic_pharyngitis_tab.py`
  - `vertigo_tab.py`
  - `otitis_media_tab.py`
  - `__init__.py`
- `pages/15_👂_Tai_Mũi_Họng.py` - Trang chính

**Ước tính:** 10-12 giờ  
**Độ khó:** ⭐⭐⭐ Trung bình

---

## 📊 **TỔNG KẾT**

| # | Task | Thời gian | Độ khó | Ưu tiên |
|---|------|-----------|--------|---------|
| 3.1 | 🤔 Symptom Checker | 8-10h | ⭐⭐⭐ | Cao |
| 3.2 | ⏰ Nhắc thuốc nâng cao | 10-12h | ⭐⭐⭐⭐ | Cao |
| 3.3 | 📅 Lịch khám bệnh | 8-10h | ⭐⭐ | Trung bình |
| 3.4 | 🦋 Trang Da Liễu (5 bệnh) | 10-12h | ⭐⭐⭐ | Trung bình |
| 3.5 | 👂 Trang Tai Mũi Họng (5 bệnh) | 10-12h | ⭐⭐⭐ | Trung bình |

**Tổng thời gian:** 46-56 giờ (~6-7 ngày làm việc)

---

## 🎯 **KHUYẾN NGHỊ THỨ TỰ THỰC HIỆN**

### **Lựa chọn 1: Theo tính năng (Ưu tiên cho người dùng)**
1. ⏰ **Nhắc thuốc nâng cao** - Nâng cấp tính năng hiện có, người dùng dùng nhiều
2. 📅 **Lịch khám bệnh** - Tính năng mới hữu ích, dễ làm
3. 🦋 **Trang Da Liễu** - Bổ sung nội dung
4. 👂 **Trang Tai Mũi Họng** - Bổ sung nội dung
5. 🤔 **Symptom Checker** - Tính năng phức tạp, làm cuối cùng

### **Lựa chọn 2: Theo độ khó (Dễ → Khó)**
1. 📅 **Lịch khám bệnh** - Dễ nhất (⭐⭐)
2. 🦋 **Trang Da Liễu** - Trung bình (⭐⭐⭐)
3. 👂 **Trang Tai Mũi Họng** - Trung bình (⭐⭐⭐)
4. 🤔 **Symptom Checker** - Trung bình (⭐⭐⭐)
5. ⏰ **Nhắc thuốc nâng cao** - Khó nhất (⭐⭐⭐⭐)

### **Lựa chọn 3: Bổ sung nội dung trước (Nhanh gọn)**
1. 🦋 **Trang Da Liễu** - Bổ sung nội dung
2. 👂 **Trang Tai Mũi Họng** - Bổ sung nội dung
3. 📅 **Lịch khám bệnh** - Tính năng mới
4. ⏰ **Nhắc thuốc nâng cao** - Nâng cấp
5. 🤔 **Symptom Checker** - Tính năng phức tạp

---

## 💡 **LƯU Ý**

1. **Có thể làm từng phần:** Không cần làm hết tất cả, có thể chọn 1-2 task để bắt đầu
2. **Commit thường xuyên:** Sau mỗi task hoàn thành
3. **Test kỹ:** Đặc biệt trên mobile (người già dùng điện thoại nhiều)
4. **Giữ đơn giản:** Ngôn ngữ dễ hiểu, tránh thuật ngữ y học phức tạp
5. **Disclaimers:** Đặc biệt cho Symptom Checker - Phải có cảnh báo rõ ràng

---

**File này sẽ được cập nhật khi bắt đầu làm từng task.**

