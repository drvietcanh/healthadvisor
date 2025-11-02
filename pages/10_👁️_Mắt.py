"""
Trang tư vấn về bệnh Mắt
"""
import streamlit as st
import sys
import os

# Thêm thư mục gốc vào path để imports hoạt động trên Streamlit Cloud
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.ui_config import get_custom_css
from core.sidebar_menu import render_sidebar_menu, hide_default_nav
from eye_page_components import render_cataract_tab, render_glaucoma_tab, render_amd_tab, render_dry_eye_tab, render_presbyopia_tab

st.set_page_config(page_title="Mắt", page_icon="👁️", layout="wide")

# Ẩn menu mặc định của Streamlit - PHẢI GỌI TRƯỚC
hide_default_nav()

# Render menu sidebar tùy chỉnh
render_sidebar_menu()


try:
    # Kiểm tra session_state có tồn tại và là dict
    if hasattr(st, 'session_state') and st.session_state is not None:
        if 'dark_mode' not in st.session_state:
            st.session_state.dark_mode = False
        if 'extra_large_font' not in st.session_state:
            st.session_state.extra_large_font = False
        css_content = get_custom_css(
            dark_mode=st.session_state.dark_mode, 
            extra_large_font=st.session_state.extra_large_font
        )
        if css_content:
            st.markdown(css_content, unsafe_allow_html=True)
except Exception:
    # Nếu có lỗi, bỏ qua CSS - app vẫn chạy được
    pass

st.title("👁️ Tư vấn Mắt")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["👁️ Đục Thủy Tinh Thể", "👁️ Tăng Nhãn Áp", "👁️ Thoái Hóa Hoàng Điểm", "👁️ Khô Mắt", "👓 Lão Thị"])

with tab1:
    render_cataract_tab()

with tab2:
    render_glaucoma_tab()

with tab3:
    render_amd_tab()

with tab4:
    render_dry_eye_tab()

with tab5:
    render_presbyopia_tab()

st.divider()
if st.button("⬅️ Quay lại trang chính"):
    st.switch_page("app.py")

