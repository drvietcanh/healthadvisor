"""
Trang tư vấn về bệnh Thận-Tiết Niệu
"""
import streamlit as st
import sys
sys.path.append('..')

from core.ui_config import get_custom_css
from core.sidebar_menu import render_sidebar_menu, hide_default_nav
from renal_page_components import render_ckd_tab, render_kidney_stones_tab

st.set_page_config(page_title="Thận-Tiết Niệu", page_icon="🧪", layout="wide")

# Ẩn menu mặc định của Streamlit - PHẢI GỌI TRƯỚC
hide_default_nav()

# Render menu sidebar tùy chỉnh
render_sidebar_menu()

# Áp dụng Dark Mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)

st.title("🧪 Tư vấn Thận-Tiết Niệu")

# Tabs
tab1, tab2 = st.tabs(["🫘 Suy Thận Mạn", "🪨 Sỏi Thận"])

# ============= TAB SUY THẬN MẠN =============
with tab1:
    render_ckd_tab()

# ============= TAB SỎI THẬN =============
with tab2:
    render_kidney_stones_tab()

# Nút quay lại
st.divider()
if st.button("⬅️ Quay lại trang chính"):
    st.switch_page("app.py")

