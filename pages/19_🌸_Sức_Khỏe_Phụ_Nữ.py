"""
Trang Sức Khỏe Phụ Nữ
"""
import streamlit as st

st.set_page_config(page_title="Sức Khỏe Phụ Nữ", page_icon="🌸", layout="wide")

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.ui_config import get_custom_css
from core.sidebar_menu import render_sidebar_menu, hide_default_nav
from women_health_page_components import (
    render_menopause_tab,
    render_menstruation_tab
)

hide_default_nav()
render_sidebar_menu()

try:
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
    pass

st.title("🌸 Sức Khỏe Phụ Nữ")
st.markdown("### Chăm sóc sức khỏe phụ nữ")

st.markdown("""
<div class="info-box">
    <b>💡 Thông tin:</b><br>
    • Mãn kinh, kinh nguyệt<br>
    • Sức khỏe sinh sản<br>
    • Thời kỳ thay đổi tự nhiên
</div>
""", unsafe_allow_html=True)

st.divider()

tab1, tab2 = st.tabs(["🔄 Mãn Kinh", "🩸 Rối Loạn Kinh Nguyệt"])

with tab1:
    render_menopause_tab()

with tab2:
    render_menstruation_tab()

st.divider()
st.markdown("""
<div class="warning-box">
    <b>⚠️ LƯU Ý:</b><br>
    • Thông tin chỉ mang tính <b>THAM KHẢO</b><br>
    • Khám bác sĩ để được tư vấn chuyên sâu
</div>
""", unsafe_allow_html=True)

