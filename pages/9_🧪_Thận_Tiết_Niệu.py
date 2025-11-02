"""
Trang tư vấn về bệnh Thận-Tiết Niệu
"""
import streamlit as st
import sys
sys.path.append('..')

from core.ui_config import get_custom_css
from core.sidebar_menu import render_sidebar_menu, hide_default_nav
from renal_page_components import render_ckd_tab, render_kidney_stones_tab, render_uti_tab, render_nocturia_tab, render_bph_tab

st.set_page_config(page_title="Thận-Tiết Niệu", page_icon="🧪", layout="wide")

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

st.title("🧪 Tư vấn Thận-Tiết Niệu")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🫘 Suy Thận Mạn", "🪨 Sỏi Thận", "🦠 Nhiễm Trùng Tiết Niệu", "🌙 Tiểu Đêm", "🫀 Phì Đại Tuyến Tiền Liệt"])

# ============= TAB SUY THẬN MẠN =============
with tab1:
    render_ckd_tab()

# ============= TAB SỎI THẬN =============
with tab2:
    render_kidney_stones_tab()

# ============= TAB NHIỄM TRÙNG TIẾT NIỆU =============
with tab3:
    render_uti_tab()

# ============= TAB TIỂU ĐÊM =============
with tab4:
    render_nocturia_tab()

# ============= TAB PHÌ ĐẠI TUYẾN TIỀN LIỆT =============
with tab5:
    render_bph_tab()

# Nút quay lại
st.divider()
if st.button("⬅️ Quay lại trang chính"):
    st.switch_page("app.py")

