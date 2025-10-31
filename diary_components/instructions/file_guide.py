"""
File Guide - Hướng dẫn lưu/tải file CSV
"""

import streamlit as st


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

