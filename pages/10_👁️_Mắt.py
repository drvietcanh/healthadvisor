"""
Trang tư vấn về bệnh Mắt
"""
import streamlit as st
import sys
sys.path.append('..')

from core.ui_config import get_custom_css
from core.sidebar_menu import render_sidebar_menu, hide_default_nav
from eye_page_components import render_cataract_tab, render_glaucoma_tab, render_amd_tab, render_dry_eye_tab

st.set_page_config(page_title="Mắt", page_icon="👁️", layout="wide")

hide_default_nav()

if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)

st.title("👁️ Tư vấn Mắt")

tab1, tab2, tab3, tab4 = st.tabs(["👁️ Đục Thủy Tinh Thể", "👁️ Tăng Nhãn Áp", "👁️ Thoái Hóa Hoàng Điểm", "👁️ Khô Mắt"])

with tab1:
    render_cataract_tab()

with tab2:
    render_glaucoma_tab()

with tab3:
    render_amd_tab()

with tab4:
    render_dry_eye_tab()

st.divider()
if st.button("⬅️ Quay lại trang chính"):
    st.switch_page("app.py")

