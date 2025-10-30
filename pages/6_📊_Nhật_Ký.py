"""
Trang Nhật ký Sức khỏe - Theo dõi huyết áp, đường huyết, cân nặng
REFACTORED VERSION - Sử dụng modular components
"""
import streamlit as st
import pandas as pd
from datetime import datetime
import sys
import os

# Thêm thư mục gốc vào path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.ui_config import get_custom_css
from pages.diary_components import (
    render_instructions, render_bp_guide, render_file_guide,
    load_csv_data, save_csv_data, initialize_health_data,
    render_input_form, render_charts, render_data_table, render_statistics
)

# Cấu hình trang
st.set_page_config(page_title="Nhật ký Sức khỏe", page_icon="📊", layout="wide")

# Áp dụng Dark Mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)

# Title
st.title("📊 Nhật ký Sức khỏe của Tôi")
st.markdown("### Theo dõi huyết áp, đường huyết, cân nặng hàng ngày")

# Khởi tạo dữ liệu
if 'health_data' not in st.session_state:
    st.session_state.health_data = initialize_health_data()

# ==================== HƯỚNG DẪN ====================
render_instructions()
render_bp_guide()
render_file_guide()

st.divider()

# ==================== TẢI LÊN DỮ LIỆU CŨ ====================
st.subheader("📥 Bước 1: Tải lên dữ liệu cũ (nếu có)")

col1, col2 = st.columns([3, 1])

with col1:
    uploaded_file = st.file_uploader(
        "👉 Click đây để chọn file CSV đã lưu trước đó",
        type=['csv'],
        help="Chọn file 'nhat_ky_suc_khoe_*.csv' ở thư mục Downloads của bạn"
    )

with col2:
    if uploaded_file is not None:
        st.success(f"✅ Đã chọn file:\n`{uploaded_file.name}`")

if uploaded_file is not None:
    success, data, message = load_csv_data(uploaded_file)
    if success:
        st.session_state.health_data = data
        st.success(f"🎉 {message}")
        st.balloons()
    else:
        st.error(f"❌ {message}")
else:
    st.info("💡 **Lần đầu sử dụng?** Bỏ qua bước này, xuống dưới nhập dữ liệu mới!")

st.divider()

# ==================== NHẬP DỮ LIỆU MỚI ====================
render_input_form()

st.divider()

# ==================== HIỂN THỊ DỮ LIỆU ====================
if len(st.session_state.health_data) > 0:
    st.subheader("📋 Bước 3: Xem dữ liệu của bạn")
    
    tab1, tab2, tab3 = st.tabs(["📊 Biểu đồ", "📋 Bảng dữ liệu", "📈 Thống kê"])
    
    with tab1:
        render_charts(st.session_state.health_data)
    
    with tab2:
        render_data_table(st.session_state.health_data)
    
    with tab3:
        render_statistics(st.session_state.health_data)
else:
    st.info("📊 **Chưa có dữ liệu.** Hãy thêm dữ liệu mới ở trên! ⬆️")

st.divider()

# ==================== TẢI XUỐNG ====================
st.subheader("💾 Bước 4: LƯU DỮ LIỆU VÀO MÁY (QUAN TRỌNG!)")

col1, col2 = st.columns([3, 1])

with col1:
    if len(st.session_state.health_data) > 0:
        csv_data, filename = save_csv_data(st.session_state.health_data)
        
        st.download_button(
            label="📥 TẢI XUỐNG FILE CSV (Click đây để lưu!)",
            data=csv_data,
            file_name=filename,
            mime="text/csv",
            use_container_width=True,
            type="primary",
            help="File sẽ tự động lưu vào thư mục Downloads"
        )
        
        st.success("✅ Click nút trên → File tự động lưu vào **Downloads**")
    else:
        st.warning("⚠️ Chưa có dữ liệu để tải xuống. Hãy thêm dữ liệu trước!")

with col2:
    st.info(f"📊 **Đã có:**\n\n{len(st.session_state.health_data)} bản ghi")

st.warning("""
⚠️ **QUAN TRỌNG:**

1. **MỖI LẦN** thêm dữ liệu mới, nhớ click **"TẢI XUỐNG"** để cập nhật file!
2. File sẽ lưu vào thư mục **Downloads** của bạn
3. **Lần sau** mở app, click **"Chọn file"** ở Bước 1 để tải lại dữ liệu
4. Nếu **không tải xuống**, dữ liệu sẽ **MẤT** khi đóng trình duyệt!
""")

st.divider()

# ==================== MẸO SỬ DỤNG ====================
st.subheader("💡 Mẹo sử dụng hiệu quả")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### ✅ NÊN LÀM:
    
    - ✅ Đo **cùng giờ** mỗi ngày (sáng sau khi thức dậy)
    - ✅ Đo **trước khi** uống thuốc, ăn sáng
    - ✅ **Nghỉ ngơi 5 phút** trước khi đo
    - ✅ Ngồi yên, không nói chuyện khi đo
    - ✅ Click **"Tải xuống"** mỗi lần nhập xong
    - ✅ Sao lưu file CSV vào **USB** hoặc **Email**
    - ✅ Đem file cho **bác sĩ** xem khi khám
    """)

with col2:
    st.markdown("""
    ### ❌ TRÁNH:
    
    - ❌ Đo ngay sau khi ăn/uống cà phê
    - ❌ Đo khi đang căng thẳng/vừa vận động
    - ❌ Quên click "Tải xuống" (sẽ mất dữ liệu!)
    - ❌ Nhập sai đơn vị (mmol/L vs mg/dL)
    - ❌ Xóa file CSV (sẽ mất hết!)
    - ❌ Lo lắng nếu 1-2 lần cao (quan trọng là **xu hướng**)
    """)

st.divider()

# Footer
st.markdown("""
<div style='text-align: center; color: gray; margin-top: 2rem;'>
    <p>💡 <b>Mẹo:</b> Lưu file CSV vào <b>Desktop</b> hoặc gửi Email cho chính bạn để không bao giờ mất!</p>
    <p>📧 Có thắc mắc? Hỏi <b>🤖 AI Bác Sĩ</b>!</p>
</div>
""", unsafe_allow_html=True)

