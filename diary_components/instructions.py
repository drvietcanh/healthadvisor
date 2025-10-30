"""
Instructions - Các hướng dẫn sử dụng cho Nhật ký
"""
import streamlit as st


def render_instructions():
    """Hiển thị hướng dẫn tổng quan"""
    with st.expander("📖 Hướng dẫn sử dụng - ĐỌC TRƯỚC KHI DÙNG!", expanded=False):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🆕 LẦN ĐẦU SỬ DỤNG:
            
            1. **Nhập dữ liệu** ở mục "➕ Thêm dữ liệu mới"
            2. **Xem biểu đồ** tự động hiện ra
            3. **Click nút 💾 TẢI XUỐNG** (quan trọng!)
            4. File sẽ tự lưu vào thư mục **Downloads**
            
            ⚠️ **QUAN TRỌNG:** Nhớ click "Tải xuống" để lưu dữ liệu!
            Nếu không, khi đóng trình duyệt sẽ **MẤT HẾT**!
            """)
        
        with col2:
            st.markdown("""
            ### 🔄 LẦN SAU SỬ DỤNG:
            
            1. **Click nút 📥 CHỌN FILE** ở mục "Tải lên dữ liệu cũ"
            2. Chọn file `nhat_ky_suc_khoe_*.csv` ở thư mục Downloads
            3. **Dữ liệu cũ tự động hiện ra!**
            4. Nhập thêm dữ liệu mới
            5. **Click 💾 TẢI XUỐNG** lại để cập nhật file
            
            💡 **Mẹo:** Lưu file vào Desktop để dễ tìm!
            """)


def render_bp_guide():
    """Hiển thị hướng dẫn đo huyết áp đúng chuẩn"""
    with st.expander("🩺 Hướng dẫn ĐO HUYẾT ÁP ĐÚNG CHUẨN (WHO/AHA)", expanded=False):
        st.markdown("""
        ## 🩺 CÁCH ĐO HUYẾT ÁP CHÍNH XÁC
        
        ### 📋 CHUẨN BỊ TRƯỚC KHI ĐO (30 phút trước):
        
        ❌ **TRÁNH:**
        - Uống cà phê, trà, thuốc lá
        - Ăn no
        - Vận động mạnh
        - Căng thẳng, lo lắng
        - Nín đi tiểu (nên đi vệ sinh trước khi đo)
        
        ✅ **NÊN:**
        - Ngồi nghỉ yên 5-10 phút
        - Thư giãn, hít thở đều
        - Trong phòng ấm áp, yên tĩnh
        
        ---
        
        ### 🪑 TƯ THẾ ĐO ĐÚNG:
        
        ```
        👤 Ngồi thẳng lưng, dựa vào ghế
        💪 Cánh tay đo đặt trên bàn (ngang tim)
        🦵 Hai chân đặt phẳng sàn, không gác chân
        ✋ Lòng bàn tay ngửa lên
        🤐 Không nói chuyện khi đang đo
        ```
        
        **HÌNH ẢNH:**
        ```
             👤 Đầu thẳng
             |
        💪---+---💪  Tay trên bàn (ngang tim)
             |
            🪑 Ngồi thẳng
             |
        🦵   |   🦵  Chân phẳng sàn
        ```
        
        ---
        
        ### 📏 QUẤN BĂNG ĐO:
        
        1. **Vị trí:** Quấn quanh cánh tay trái (nếu thuận tay phải)
        2. **Độ cao:** Cách khuỷu tay 2-3 cm
        3. **Độ chặt:** Lọt 2 ngón tay vào giữa băng và da
        4. **Ống nghe:** Đặt đúng vị trí động mạch (bên trong khuỷu tay)
        
        ⚠️ **LƯU Ý:**
        - Cởi áo dài tay (không đo qua áo)
        - Không quấn quá chặt hoặc quá lỏng
        - Băng phải ngang mức tim
        
        ---
        
        ### 🔢 ĐO THẾ NÀO:
        
        **Máy điện tử (Tự động):**
        1. Bật máy
        2. Quấn băng đúng vị trí
        3. Ngồi yên, không cử động
        4. Nhấn nút Start
        5. Chờ máy đo xong (1-2 phút)
        6. Ghi lại kết quả
        
        **Máy thủy ngân (Cần người đo):**
        1. Quấn băng
        2. Bơm căng băng đến 180-200 mmHg
        3. Từ từ xả khí, nghe động mạch
        4. Tiếng đầu tiên = Tâm thu
        5. Tiếng cuối cùng = Tâm trương
        
        ---
        
        ### 🔁 ĐO BAO NHIÊU LẦN:
        
        ✅ **ĐÚNG CHUẨN:**
        - Đo **2-3 lần** (cách nhau 1-2 phút)
        - Lấy kết quả **TRUNG BÌNH** của 2-3 lần
        - Nếu chênh lệch > 10 mmHg → Đo lại
        
        ✅ **THỜI ĐIỂM ĐO:**
        - **Sáng:** Sau khi thức dậy, trước khi uống thuốc/ăn sáng
        - **Tối:** Trước khi đi ngủ
        - Đo **cùng giờ** mỗi ngày
        
        ---
        
        ### 📊 GHI CHÉP KẾT QUẢ:
        
        ✅ **Ghi rõ:**
        - Ngày giờ đo
        - Kết quả (ví dụ: 130/85)
        - Mạch (nếu máy có)
        - Thời điểm (sáng/tối, trước/sau ăn)
        - Cảm giác (đau đầu, chóng mặt...)
        
        → **Nhập vào app này để theo dõi xu hướng!**
        
        ---
        
        ### ⚠️ SAI LẦM THƯỜNG GẶP:
        
        | Sai lầm | Hậu quả | Cách khắc phục |
        |---------|---------|----------------|
        | Quấn băng qua áo | Kết quả cao hơn | Cởi áo |
        | Tay thòng xuống | Kết quả cao hơn | Đặt tay lên bàn |
        | Nói chuyện khi đo | Kết quả cao hơn | Im lặng |
        | Gác chân lên chân | Kết quả cao hơn | 2 chân phẳng sàn |
        | Đo 1 lần | Không chính xác | Đo 2-3 lần |
        | Băng quá chặt/lỏng | Sai số lớn | Lọt 2 ngón tay |
        
        ---
        
        ### 🚨 KHI NÀO CẦN GỌI BÁC SĨ:
        
        🚨 **NGAY LẬP TỨC - GỌI 115 (CẤP CỨU):**
        - Huyết áp ≥ 180/120 + đau đầu dữ dội
        - Huyết áp ≥ 180/120 + đau ngực
        - Huyết áp ≥ 180/120 + khó thở
        - Huyết áp ≥ 180/120 + mờ mắt
        - Huyết áp ≥ 180/120 + buồn nôn/nôn
        - Huyết áp ≥ 180/120 + tê tay chân
        
        📞 **HẸN GẶP BÁC SĨ (trong vài ngày):**
        - Huyết áp ≥ 140/90 liên tục 3-5 ngày
        - Dao động nhiều (100/60 → 160/100)
        - Có triệu chứng: chóng mặt, đau đầu, mệt...
        
        ---
        
        ### 📚 NGUỒN THAM KHẢO:
        - American Heart Association (AHA)
        - World Health Organization (WHO)
        - European Society of Hypertension (ESH)
        """)


def render_file_guide():
    """Hiển thị hướng dẫn lưu/tải file CSV"""
    with st.expander("💾 Hướng dẫn LƯU/TẢI FILE CSV - TỪNG BƯỚC CHI TIẾT", expanded=False):
        st.markdown("""
        ## 💾 HƯỚNG DẪN LƯU VÀ TẢI FILE CSV
        
        ### 📥 PHẦN 1: LẦN ĐẦU SỬ DỤNG - LƯU FILE
        
        #### Bước 1: Nhập dữ liệu
        ✅ Kéo xuống mục **"➕ Bước 2: Thêm dữ liệu mới"**  
        ✅ Nhập huyết áp, đường huyết, v.v.  
        ✅ Click nút **"💾 LƯU VÀO NHẬT KÝ"**
        
        #### Bước 2: Tải xuống file
        ✅ Kéo xuống mục **"💾 Bước 4: LƯU DỮ LIỆU VÀO MÁY"**  
        ✅ Click nút to màu xanh **"📥 TẢI XUỐNG FILE CSV"**  
        ✅ File tự động lưu vào thư mục **Downloads**
        
        #### Bước 3: Tìm file đã tải (QUAN TRỌNG!)
        
        **Trên Windows:**
        ```
        1. Mở File Explorer (Biểu tượng thư mục trên taskbar)
        2. Click vào "Downloads" bên trái
        3. Tìm file tên "nhat_ky_suc_khoe_30102025_1430.csv"
        4. (Tùy chọn) Kéo file ra Desktop để dễ tìm
        ```
        
        **Trên Mac:**
        ```
        1. Mở Finder
        2. Click "Downloads" bên trái
        3. Tìm file "nhat_ky_suc_khoe_*.csv"
        4. (Tùy chọn) Kéo ra Desktop
        ```
        
        **Trên điện thoại (Android):**
        ```
        1. Mở app "Files" hoặc "My Files"
        2. Vào thư mục "Downloads"
        3. Tìm file CSV
        ```
        
        **Trên iPhone/iPad:**
        ```
        1. Mở app "Files" (Tệp tin)
        2. Vào "On My iPhone" → "Downloads"
        3. Tìm file CSV
        ```
        
        ---
        
        ### 📤 PHẦN 2: LẦN SAU - TẢI FILE LÊN
        
        #### Bước 1: Mở app lại
        ✅ Mở trình duyệt  
        ✅ Vào lại trang Nhật ký Sức khỏe này
        
        #### Bước 2: Tải file lên
        ✅ Tìm mục **"📥 Bước 1: Tải lên dữ liệu cũ"**  
        ✅ Click nút **"Browse files"** (hoặc "Chọn file")
        
        **Windows sẽ mở cửa sổ chọn file:**
        ```
        1. Cửa sổ tự động mở thư mục "Downloads"
        2. Tìm file "nhat_ky_suc_khoe_*.csv"
        3. Click chọn file
        4. Click nút "Open" (Mở)
        ```
        
        ✅ **Ngay lập tức:** Dữ liệu cũ hiện ra!  
        ✅ **Thấy biểu đồ** của tất cả ngày trước!
        
        #### Bước 3: Thêm dữ liệu mới
        ✅ Nhập thêm dữ liệu hôm nay  
        ✅ Kéo xuống click **"TẢI XUỐNG"** lại để cập nhật file
        
        ---
        
        ### 💡 MẸO QUAN TRỌNG:
        
        #### 🎯 Để không bao giờ mất dữ liệu:
        
        **Mẹo 1: Đặt tên file dễ nhớ**
        ```
        Sau khi tải xuống, đổi tên file thành:
        "nhat_ky_BA_NGUYEN.csv"
        hoặc
        "huyet_ap_cua_toi.csv"
        ```
        
        **Mẹo 2: Lưu ở Desktop (Màn hình chính)**
        ```
        1. Mở Downloads
        2. Kéo file ra Desktop
        3. Lần sau dễ tìm hơn!
        ```
        
        **Mẹo 3: Gửi Email cho chính bạn**
        ```
        1. Mở Gmail/Outlook
        2. Soạn email gửi cho chính bạn
        3. Đính kèm file CSV
        4. Gửi!
        → Lưu trên cloud, không bao giờ mất!
        ```
        
        **Mẹo 4: Sao lưu vào USB**
        ```
        1. Cắm USB vào máy
        2. Copy file CSV vào USB
        3. Rút USB cất cẩn thận
        ```
        
        **Mẹo 5: Lưu vào Google Drive/OneDrive**
        ```
        1. Mở Google Drive (drive.google.com)
        2. Click "Upload" (Tải lên)
        3. Chọn file CSV
        → Truy cập từ mọi thiết bị!
        ```
        
        ---
        
        ### 🔄 CÁCH SỬ DỤNG NHIỀU THIẾT BỊ:
        
        **Ví dụ: Nhập ở điện thoại, xem ở máy tính**
        
        1. **Ở điện thoại:**
           - Nhập dữ liệu
           - Tải xuống file CSV
           - Gửi file qua Email cho chính bạn
        
        2. **Ở máy tính:**
           - Mở Email
           - Tải file CSV về
           - Mở app này, tải file lên
           - Thấy ngay dữ liệu từ điện thoại!
        
        ---
        
        ### ❓ TROUBLESHOOTING (Gặp vấn đề):
        
        **Vấn đề 1: Không tìm thấy file đã tải**
        ```
        Giải pháp:
        - Mở File Explorer
        - Gõ "nhat_ky" vào ô tìm kiếm
        - Windows sẽ tìm file cho bạn
        ```
        
        **Vấn đề 2: Tải file lên bị lỗi**
        ```
        Giải pháp:
        - Kiểm tra file có đuôi .csv không
        - Không được mở file bằng Excel rồi sửa
        - Tải file gốc từ app này
        ```
        
        **Vấn đề 3: Dữ liệu bị mất sau khi đóng trình duyệt**
        ```
        Nguyên nhân: Quên click "Tải xuống"
        Giải pháp: Luôn click "Tải xuống" sau khi nhập xong!
        ```
        
        ---
        
        ### 📞 CẦN GIÚP ĐỠ?
        
        - Hỏi con cháu giúp lần đầu
        - Xem lại hướng dẫn này
        - Hỏi AI Bác Sĩ: "Hướng dẫn tôi lưu file"
        """)

