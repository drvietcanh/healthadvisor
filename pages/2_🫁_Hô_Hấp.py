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
render_sidebar_menu()

# Áp dụng Dark Mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
extra_large_font = st.session_state.get('extra_large_font', False)
css_content = get_custom_css(dark_mode=st.session_state.dark_mode, extra_large_font=extra_large_font)
if css_content:
    st.markdown(css_content, unsafe_allow_html=True)

st.title("🫁 Tư vấn Hô Hấp")

# Tự động thêm vào recent
from core.recent_pages import add_to_recent
add_to_recent("2_🫁_Hô_Hấp", "🫁 Hô Hấp")

# Nút yêu thích
from core.favorites_manager import render_favorite_button
col_title, col_fav = st.columns([4, 1])
with col_fav:
    render_favorite_button("2_🫁_Hô_Hấp", "🫁 Hô Hấp")

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
if st.button("⬅️ Quay lại trang chính"):
    st.switch_page("app.py")
