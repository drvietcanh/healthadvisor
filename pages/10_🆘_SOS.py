"""
Trang SOS - Số điện thoại khẩn cấp và Hướng dẫn sơ cứu
Thiết kế đặc biệt cho người già: Font to, nút lớn, màu rõ ràng

File này tổng hợp từ emergency_page_components/
"""
import streamlit as st
import sys
import os

# Thêm thư mục gốc vào path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from emergency_page_components import (
    get_emergency_css,
    render_emergency_numbers_tab,
    render_first_aid_tab,
    render_contacts_tab,
    render_medical_info_tab
)
from core.ui_config import get_custom_css

st.set_page_config(
    page_title="SOS - Cấp Cứu",
    page_icon="🆘",
    layout="wide"
)

# Áp dụng Dark Mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)

# CSS đặc biệt cho trang SOS
st.markdown(get_emergency_css(), unsafe_allow_html=True)

# Header
st.title("🆘 SOS - SỐ ĐIỆN THOẠI CẤP CỨU")

st.info("""
    ⚠️ **Trong trường hợp khẩn cấp, hãy gọi ngay:**
    - **115** - Cấp cứu y tế
    - **113** - Công an  
    - **114** - Phòng cháy chữa cháy
    
    Mỗi giây đều quan trọng. Đừng ngần ngại gọi cấp cứu khi cần!
""")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📞 SỐ CẤP CỨU",
    "🏥 Hướng dẫn Sơ cứu",
    "👥 Danh bạ Cá nhân",
    "📋 Thông tin Y tế"
])

# ===== TAB 1: SỐ CẤP CỨU =====
with tab1:
    render_emergency_numbers_tab()

# ===== TAB 2: HƯỚNG DẪN SƠ CỨU =====
with tab2:
    render_first_aid_tab()

# ===== TAB 3: DANH BẠ CÁ NHÂN =====
with tab3:
    render_contacts_tab()

# ===== TAB 4: THÔNG TIN Y TẾ =====
with tab4:
    render_medical_info_tab()

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; padding: 1rem;'>
    <p><strong>🆘 Nhớ: Mỗi giây đều có giá trị trong cấp cứu!</strong></p>
    <p style='color: gray;'>Lưu số này vào danh bạ điện thoại của bạn để dùng khi cần</p>
</div>
""", unsafe_allow_html=True)

# Nút quay lại
if st.button("🏠 Về Trang Chủ", use_container_width=True):
    st.switch_page("app.py")

