"""
Trang: Hội Chứng Chuyển Hóa & Béo Phì
=====================================

Metabolic Syndrome & Obesity Management
Quản lý cân nặng, calories, vận động, mục tiêu giảm cân

REFACTORED: Đã tách thành 5 components để dễ quản lý
"""

import streamlit as st
import sys
import os

# Add parent directory to path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

# Import components
from metabolic_components import (
    render_overview_tab,
    render_assessment_tab,
    render_diseases_tab,
    render_calories_tab,
    render_goals_tab
)
from core.ui_config import get_custom_css

# Page config
st.set_page_config(
    page_title="Hội Chứng Chuyển Hóa - HealthAdvisor",
    page_icon="⚖️",
    layout="wide"
)

# Apply custom CSS
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)

# Title
st.title("⚖️ Hội Chứng Chuyển Hóa & Quản Lý Cân Nặng")
st.markdown("**Metabolic Syndrome & Weight Management**")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Tổng Quan",
    "⚖️ Béo Phì & Đánh Giá", 
    "🔗 Bệnh Liên Quan",
    "🍽️ Calories & Vận Động",
    "🎯 Mục Tiêu & Kế Hoạch"
])

# Render each tab using components
with tab1:
    render_overview_tab()

with tab2:
    render_assessment_tab()

with tab3:
    render_diseases_tab()

with tab4:
    render_calories_tab()

with tab5:
    render_goals_tab()

# Footer
st.markdown("---")
st.caption("""
💡 **Lưu ý:** Thông tin chỉ mang tính tham khảo. Hãy tham khảo bác sĩ trước khi bắt đầu chương trình giảm cân,
đặc biệt nếu bạn có bệnh nền hoặc >60 tuổi.
""")
