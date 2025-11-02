"""
Trang tư vấn về bệnh Tiêu Hóa
"""
import streamlit as st
import sys
import os

# Thêm thư mục gốc vào path để imports hoạt động trên Streamlit Cloud
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

st.set_page_config(page_title="Tiêu Hóa", page_icon="🌡️", layout="wide")

from core.ui_config import get_custom_css
from core.sidebar_menu import render_sidebar_menu, hide_default_nav
from digestive_page_components import (
    render_gerd_tab, render_constipation_tab,
    render_gastritis_tab, render_peptic_ulcer_tab,
    render_diarrhea_tab, render_colitis_tab,
    render_ibs_tab
)

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

st.title("🌡️ Tư vấn Tiêu Hóa")

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🌡️ Trào Ngược Dạ Dày",
    "🚽 Táo Bón",
    "🔥 Viêm Dạ Dày",
    "🩸 Loét Dạ Dày",
    "💧 Tiêu Chảy Cấp",
    "🫀 Viêm Đại Tràng",
    "🫀 Hội Chứng Ruột Kích Thích"
])

with tab1:
    render_gerd_tab()

with tab2:
    render_constipation_tab()

with tab3:
    render_gastritis_tab()

with tab4:
    render_peptic_ulcer_tab()

with tab5:
    render_diarrhea_tab()

with tab6:
    render_colitis_tab()

with tab7:
    render_ibs_tab()

st.divider()
if st.button("⬅️ Quay lại trang chính"):
    st.switch_page("app.py")

