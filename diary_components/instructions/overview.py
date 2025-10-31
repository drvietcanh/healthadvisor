"""
Overview Instructions - Hướng dẫn tổng quan sử dụng Nhật ký
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

