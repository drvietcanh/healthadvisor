"""
Trang tư vấn về bệnh Tiêu Hóa
"""
import streamlit as st
import sys
sys.path.append('..')

from core.ui_config import get_custom_css
from core.sidebar_menu import render_sidebar_menu, hide_default_nav
from digestive_page_components import render_gerd_tab, render_constipation_tab

st.set_page_config(page_title="Tiêu Hóa", page_icon="🌡️", layout="wide")

# Ẩn menu mặc định của Streamlit - PHẢI GỌI TRƯỚC
hide_default_nav()

# Render menu sidebar tùy chỉnh
render_sidebar_menu()

if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
extra_large_font = st.session_state.get('extra_large_font', False)
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode, extra_large_font=extra_large_font), unsafe_allow_html=True)

st.title("🌡️ Tư vấn Tiêu Hóa")

tab1, tab2 = st.tabs(["🌡️ Trào Ngược Dạ Dày", "🚽 Táo Bón"])

with tab1:
    render_gerd_tab()

with tab2:
    render_constipation_tab()

st.divider()
if st.button("⬅️ Quay lại trang chính"):
    st.switch_page("app.py")

