"""
Trang HỌC DỄ - Giải thích bằng hình ảnh, ví dụ đời thường

REFACTORED: Tách tabs thành components
"""
import streamlit as st
import sys
import os

# Thêm thư mục gốc vào path để imports hoạt động trên Streamlit Cloud
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.ui_config import get_custom_css
from core.sidebar_menu import render_sidebar_menu, hide_default_nav
from pages.hoc_de_tabs import (
    render_explanations_tab,
    render_memory_tricks_tab,
    render_comparisons_tab,
    render_quiz_tab
)

st.set_page_config(page_title="Học Dễ", page_icon="🎓", layout="wide")

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

st.title("🎓 Học Y Khoa Siêu Dễ!")
st.markdown("### Giải thích bằng hình ảnh - Ai cũng hiểu! 😊")

# Tabs
tabs = st.tabs([
    "💡 Giải Thích Đơn Giản",
    "🧠 Mẹo Nhớ",
    "📏 So Sánh",
    "🎮 Trắc Nghiệm"
])

# Render tabs
with tabs[0]:
    render_explanations_tab()

with tabs[1]:
    render_memory_tricks_tab()

with tabs[2]:
    render_comparisons_tab()

with tabs[3]:
    render_quiz_tab()

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; padding: 1rem;">
    💡 <b>MẸO HỌC HIỆU QUẢ:</b><br>
    1. Đọc → 2. Xem hình → 3. Kể lại → 4. Làm quiz → 5. Nhớ lâu!
</div>
""", unsafe_allow_html=True)

if st.button("⬅️ Quay lại trang chính"):
    st.switch_page("app.py")
