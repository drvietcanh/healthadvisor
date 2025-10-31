"""
Trang Cấp Cứu - Số điện thoại khẩn cấp và Hướng dẫn sơ cứu
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
    page_title="Số Cấp Cứu",
    page_icon="🚨",
    layout="wide"
)

# Áp dụng Dark Mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)

# Custom CSS cho trang này
st.markdown(get_emergency_css(), unsafe_allow_html=True)

# Header
st.title("🚨 SỐ ĐIỆN THOẠI CẤP CỨU")

st.markdown("""
<div style='background: linear-gradient(135deg, #ff4444 0%, #cc0000 100%); 
            padding: 25px; border-radius: 15px; color: white; margin-bottom: 25px;
            box-shadow: 0 8px 20px rgba(255,0,0,0.3);'>
    <h2 style='margin:0; color: white; font-size: 32px;'>⚡ KHẨN CẤP - GỌI NGAY!</h2>
    <p style='margin: 15px 0 0 0; font-size: 22px; opacity: 0.95;'>
        Mỗi giây đều quan trọng. Đừng ngần ngại gọi cấp cứu khi cần!
    </p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📞 SỐ CẤP CỨU",
    "🏥 SƠ CỨU",
    "👥 DANH BẠ",
    "📋 THÔNG TIN Y TẾ"
])

with tab1:
    render_emergency_numbers_tab()

with tab2:
    render_first_aid_tab()

with tab3:
    render_contacts_tab()

with tab4:
    render_medical_info_tab()

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; padding: 20px; background: #fff3cd; border-radius: 10px; margin-top: 20px;'>
    <h3 style='color: #cc0000; margin: 0;'>⚠️ LƯU Ý QUAN TRỌNG</h3>
    <p style='font-size: 20px; margin: 10px 0; color: #333;'>
        <b>KHI NGHI NGỜ - HÃY GỌI 115!</b><br>
        Tốt hơn gọi nhầm còn hơn không gọi.<br>
        Mỗi giây đều có giá trị trong cấp cứu!
    </p>
</div>
""", unsafe_allow_html=True)

if st.button("⬅️ Quay lại trang chính", use_container_width=True):
    st.switch_page("app.py")
