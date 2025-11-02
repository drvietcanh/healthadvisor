"""
Trang Da Liễu
==================
Dermatology Page
"""

import streamlit as st
import sys
import os

# Thêm thư mục gốc vào path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

# Cấu hình trang - PHẢI ĐẶT TRƯỚC IMPORT
st.set_page_config(
    page_title="Da Liễu - HealthAdvisor",
    page_icon="🦋",
    layout="wide"
)

from dermatology_page_components import (
    render_tinea_tab,
    render_onychomycosis_tab,
    render_eczema_tab,
    render_pruritus_tab,
    render_pressure_ulcer_tab,
    render_psoriasis_tab
)
from core.ui_config import get_custom_css
from core.sidebar_menu import render_sidebar_menu, hide_default_nav

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

# Tự động thêm vào recent
from core.recent_pages import add_to_recent
add_to_recent("14_🦋_Da_Liễu", "🦋 Da Liễu")

# Header
st.title("🦋 Da Liễu")
st.markdown("""
<div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            padding: 20px; border-radius: 10px; color: white; margin-bottom: 20px;'>
    <h3 style='margin:0; color: white;'>💡 Thông tin về các bệnh da phổ biến</h3>
    <p style='margin: 10px 0 0 0; opacity: 0.9;'>
        Hướng dẫn đầy đủ về nấm da, nấm móng, chàm khô, ngứa da và loét tì đè.
    </p>
</div>
""", unsafe_allow_html=True)

# Nút yêu thích
from core.favorites_manager import render_favorite_button
col_title, col_fav = st.columns([4, 1])
with col_fav:
    render_favorite_button("14_🦋_Da_Liễu", "🦋 Da Liễu")

# Tabs cho các bệnh
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🦶 Nấm Da",
    "💅 Nấm Móng",
    "🌿 Chàm Khô",
    "🔴 Ngứa Da",
    "🛏️ Loét Tì Đè",
    "🦠 Vảy Nến"
])

with tab1:
    render_tinea_tab()

with tab2:
    render_onychomycosis_tab()

with tab3:
    render_eczema_tab()

with tab4:
    render_pruritus_tab()

with tab5:
    render_pressure_ulcer_tab()

with tab6:
    render_psoriasis_tab()

# Nút quay lại
st.divider()
if st.button("⬅️ Quay lại trang chính"):
    st.switch_page("app.py")

