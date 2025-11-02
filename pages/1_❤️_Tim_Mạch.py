"""
Trang tư vấn về bệnh Tim Mạch

File này tổng hợp từ cardiovascular_page_components/
"""
import streamlit as st
import sys
sys.path.append('..')

from cardiovascular_page_components import (
    render_hypertension_tab,
    render_heart_failure_tab,
    render_dyslipidemia_tab,
    render_blood_pressure_tab,
    render_arrhythmia_tab,
    render_myocardial_infarction_tab,
    render_atherosclerosis_tab
)
from core.ui_config import get_custom_css
from core.sidebar_menu import render_sidebar_menu, hide_default_nav

st.set_page_config(page_title="Tim Mạch", page_icon="❤️", layout="wide")

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

st.title("❤️ Tư vấn Tim Mạch")

# Tự động thêm vào recent
from core.recent_pages import add_to_recent
add_to_recent("1_❤️_Tim_Mạch", "❤️ Tim Mạch")

# Nút yêu thích
from core.favorites_manager import render_favorite_button
col_title, col_fav = st.columns([4, 1])
with col_fav:
    render_favorite_button("1_❤️_Tim_Mạch", "❤️ Tim Mạch")

# Tabs cho các bệnh tim mạch
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🩺 Tăng Huyết Áp", 
    "💔 Suy Tim", 
    "🧈 Rối Loạn Lipid Máu", 
    "❤️‍🩹 Rối Loạn Nhịp Tim",
    "💔 Nhồi Máu Cơ Tim",
    "🫀 Xơ Vữa Động Mạch",
    "📊 Đo Huyết Áp"
])

with tab1:
    render_hypertension_tab()

with tab2:
    render_heart_failure_tab()

with tab3:
    render_dyslipidemia_tab()

with tab4:
    render_arrhythmia_tab()

with tab5:
    render_myocardial_infarction_tab()

with tab6:
    render_atherosclerosis_tab()

with tab7:
    render_blood_pressure_tab()

# Nút quay lại
st.divider()
if st.button("⬅️ Quay lại trang chính"):
    st.switch_page("app.py")
