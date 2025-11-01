"""
Trang tư vấn về bệnh Tim Mạch

File này tổng hợp từ cardiovascular_page_components/
"""
import streamlit as st
import sys
sys.path.append('..')

from cardiovascular_page_components import (
    render_hypertension_tab,
    render_heart_failure_tab,
    render_dyslipidemia_tab,
    render_blood_pressure_tab
)
from core.ui_config import get_custom_css
from core.sidebar_menu import render_sidebar_menu, hide_default_nav

st.set_page_config(page_title="Tim Mạch", page_icon="❤️", layout="wide")

# Ẩn menu mặc định của Streamlit - PHẢI GỌI TRƯỚC
hide_default_nav()

# Render menu sidebar tùy chỉnh
# TẠM ẨN - Sẽ phát triển thêm chức năng sau
# render_sidebar_menu()

# Áp dụng Dark Mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)

st.title("❤️ Tư vấn Tim Mạch")

# Tabs cho các bệnh tim mạch
tab1, tab2, tab3, tab4 = st.tabs(["🩺 Tăng Huyết Áp", "💔 Suy Tim", "🧈 Rối Loạn Lipid Máu", "📊 Đo Huyết Áp"])

with tab1:
    render_hypertension_tab()

with tab2:
    render_heart_failure_tab()

with tab3:
    render_dyslipidemia_tab()

with tab4:
    render_blood_pressure_tab()

# Nút quay lại
st.divider()
if st.button("⬅️ Quay lại trang chính"):
    st.switch_page("app.py")
