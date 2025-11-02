"""
Trang tư vấn về bệnh Thần Kinh (Đột quỵ, Động kinh...)

REFACTORED: Tách tabs thành components
"""
import streamlit as st
import sys
import os

# Thêm thư mục gốc vào path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

from core.ui_config import get_custom_css
from core.sidebar_menu import render_sidebar_menu, hide_default_nav
from neurological_page_components import (
    render_stroke_tab,
    render_epilepsy_tab,
    render_headache_tab,
    render_dementia_tab,
    render_insomnia_tab,
    render_befast_check_tab,
    render_parkinson_tab
)

st.set_page_config(page_title="Thần Kinh", page_icon="🧠", layout="wide")

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

st.title("🧠 Tư vấn Thần Kinh")

# Tự động thêm vào recent
from core.recent_pages import add_to_recent
add_to_recent("4_🧠_Thần_Kinh", "🧠 Thần Kinh")

# Nút yêu thích
from core.favorites_manager import render_favorite_button
col_title, col_fav = st.columns([4, 1])
with col_fav:
    render_favorite_button("4_🧠_Thần_Kinh", "🧠 Thần Kinh")

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["🚨 Đột Quỵ", "⚡ Động Kinh", "💆 Đau Đầu", "🧠 Sa Sút Trí Tuệ", "😴 Mất Ngủ", "🧠 Bệnh Parkinson", "📊 Kiểm Tra BE-FAST"])

# Render tabs
with tab1:
    render_stroke_tab()

with tab2:
    render_epilepsy_tab()

with tab3:
    render_headache_tab()

with tab4:
    render_dementia_tab()

with tab5:
    render_insomnia_tab()

with tab6:
    render_parkinson_tab()

with tab7:
    render_befast_check_tab()

# Nút quay lại
st.divider()
if st.button("⬅️ Quay lại trang chính"):
    st.switch_page("app.py")
