"""
Trang tư vấn về bệnh Nhi Khoa
"""
import streamlit as st

st.set_page_config(page_title="Nhi Khoa", page_icon="👶", layout="wide")

import sys
import os

# Thêm thư mục gốc vào path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.ui_config import get_custom_css
from core.sidebar_menu import render_sidebar_menu, hide_default_nav
from pediatrics_page_components import (
    render_fever_tab,
    render_diarrhea_tab,
    render_seizure_tab
)

# Ẩn menu mặc định
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

st.title("👶 Nhi Khoa")
st.markdown("### Chăm sóc sức khỏe trẻ em")

st.markdown("""
<div class="info-box">
    <b>💡 Thông tin:</b><br>
    • Hướng dẫn xử trí bệnh thường gặp ở trẻ em<br>
    • Sốt, tiêu chảy, co giật<br>
    • Phòng ngừa và điều trị tại nhà
</div>
""", unsafe_allow_html=True)

st.divider()

# Tabs
tab1, tab2, tab3 = st.tabs([
    "🌡️ Sốt",
    "💩 Tiêu Chảy",
    "⚡ Co Giật/Động Kinh"
])

with tab1:
    render_fever_tab()

with tab2:
    render_diarrhea_tab()

with tab3:
    render_seizure_tab()

st.divider()
st.markdown("""
<div class="warning-box">
    <b>⚠️ LƯU Ý:</b><br>
    • Trẻ <3 tháng: Khám bác sĩ NGAY khi sốt >38°C<br>
    • Mất nước nặng: Truyền dịch ngay<br>
    • Co giật kéo dài: Gọi 115<br>
    • Thông tin chỉ mang tính <b>THAM KHẢO</b>
</div>
""", unsafe_allow_html=True)

