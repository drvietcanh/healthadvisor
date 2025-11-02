"""
Trang tư vấn về bệnh Hô Hấp
COPD và Hen Suyễn
"""

import streamlit as st
import sys
sys.path.append('..')

from core.ui_config import get_custom_css
from core.sidebar_menu import render_sidebar_menu, hide_default_nav
from respiratory_page_components import render_copd_tab, render_asthma_tab, render_pneumonia_tab, render_chronic_cough_tab

st.set_page_config(page_title="Hô Hấp", page_icon="🫁", layout="wide")

# Ẩn menu mặc định của Streamlit - PHẢI GỌI TRƯỚC
hide_default_nav()

# Render menu sidebar tùy chỉnh
# TẠM ẨN - Sẽ phát triển thêm chức năng sau
# render_sidebar_menu()

# Áp dụng Dark Mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)

st.title("🫁 Tư vấn Hô Hấp")

# Tabs cho các bệnh hô hấp
tab1, tab2, tab3, tab4 = st.tabs(["🫁 COPD (Phổi Tắc Nghẽn)", "🌬️ Hen Suyễn", "🫁 Viêm phổi", "🤧 Ho Mãn Tính"])

with tab1:
    render_copd_tab()

with tab2:
    render_asthma_tab()

with tab3:
    render_pneumonia_tab()

with tab4:
    render_chronic_cough_tab()

# Nút quay lại
st.divider()
if st.button("🏠 Về Trang Chủ"):
    st.switch_page("app.py")
