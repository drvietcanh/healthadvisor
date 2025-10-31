"""
Trang Hướng dẫn sử dụng HealthAdvisor

File này tổng hợp từ guide_components/
"""
import streamlit as st
import sys
import os

sys.path.append('..')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.ui_config import get_custom_css
from guide_components import (
    render_quick_start_tab,
    render_detailed_guide_tab,
    render_faq_tab,
    render_tips_tab
)

st.set_page_config(page_title="Hướng dẫn", page_icon="📖", layout="wide")

# Áp dụng Dark Mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)

st.title("📖 Hướng dẫn sử dụng HealthAdvisor")

st.success("👋 **Chào mừng bạn đến với HealthAdvisor!** Chỉ cần 3 phút để biết cách dùng app này.")

# Tab hướng dẫn
tab1, tab2, tab3, tab4 = st.tabs([
    "🚀 Bắt đầu nhanh",
    "📚 Hướng dẫn chi tiết",
    "❓ Câu hỏi thường gặp",
    "💡 Mẹo & Thủ thuật"
])

# ===== TAB 1: BẮT ĐẦU NHANH =====
with tab1:
    render_quick_start_tab()

# ===== TAB 2: HƯỚNG DẪN CHI TIẾT =====
with tab2:
    render_detailed_guide_tab()

# ===== TAB 3: FAQ =====
with tab3:
    render_faq_tab()

# ===== TAB 4: MẸO & THỦTHUẬT =====
with tab4:
    render_tips_tab()

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>📧 Góp ý? Liên hệ: <a href='https://github.com/drvietcanh/healthadvisor'>GitHub</a></p>
    <p>Made with ❤️ for Vietnamese Healthcare</p>
</div>
""", unsafe_allow_html=True)
