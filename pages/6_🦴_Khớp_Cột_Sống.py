"""
Trang tư vấn về bệnh Khớp - Cột sống
"""

import streamlit as st
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bone_joint_page_components import (
    render_osteoarthritis_tab,
    render_rheumatoid_arthritis_tab,
    render_back_pain_tab,
    render_herniated_disc_tab,
    render_gout_tab,
    render_joint_exercises_tab,
    render_osteoporosis_tab
)
from core.ui_config import get_custom_css

st.set_page_config(
    page_title="Khớp - Cột sống",
    page_icon="🦴",
    layout="wide"
)

# Áp dụng Dark Mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)

st.title("🦴 Tư vấn Khớp - Cột sống")

st.markdown("""
<div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            padding: 20px; border-radius: 10px; color: white; margin-bottom: 20px;'>
    <h3 style='margin:0; color: white;'>💡 Thông tin về bệnh khớp và cột sống</h3>
    <p style='margin: 10px 0 0 0; opacity: 0.9;'>
        Hướng dẫn đầy đủ về thoái hóa khớp, viêm khớp, đau lưng, gút và cách tập luyện.
    </p>
</div>
""", unsafe_allow_html=True)

# Tabs cho các bệnh
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🦴 Thoái hóa khớp",
    "🔴 Viêm khớp dạng thấp",
    "🫁 Đau thắt lưng",
    "💔 Thoát vị đĩa đệm",
    "🦶 Bệnh Gút",
    "🦴 Loãng Xương",
    "🏃 Bài tập khớp"
])

with tab1:
    render_osteoarthritis_tab()

with tab2:
    render_rheumatoid_arthritis_tab()

with tab3:
    render_back_pain_tab()

with tab4:
    render_herniated_disc_tab()

with tab5:
    render_gout_tab()

with tab6:
    render_osteoporosis_tab()

with tab7:
    render_joint_exercises_tab()

# Nút quay lại
st.divider()
if st.button("⬅️ Quay lại trang chính"):
    st.switch_page("app.py")

