"""
Trang tư vấn về bệnh Ký Sinh Trùng
"""
import streamlit as st

st.set_page_config(page_title="Ký Sinh Trùng", page_icon="🐛", layout="wide")

import sys
import os

# Thêm thư mục gốc vào path để imports hoạt động trên Streamlit Cloud
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.ui_config import get_custom_css
from core.sidebar_menu import render_sidebar_menu, hide_default_nav
from parasitology_page_components import (
    render_ascarid_tab,
    render_hookworm_tab,
    render_pinworm_tab,
    render_tapeworm_tab,
    render_liver_fluke_tab,
    render_amoebic_dysentery_tab,
    render_giardiasis_tab,
    render_toxoplasmosis_tab,
    render_malaria_tab
)

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

# Header
st.title("🐛 Ký Sinh Trùng")
st.markdown("### Các bệnh do giun, sán, đơn bào phổ biến ở Việt Nam")

# Giới thiệu ngắn
st.markdown("""
<div class="info-box">
    <b>📊 Thống kê tại Việt Nam:</b><br>
    • >40% trẻ em nhiễm giun đũa<br>
    • >30% dân số nhiễm giun móc<br>
    • Phổ biến ở nông thôn, miền núi<br>
    • Nguyên nhân: Vệ sinh kém, ăn rau sống, nguồn nước ô nhiễm
</div>
""", unsafe_allow_html=True)

st.divider()

# Tabs cho các bệnh
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
    "🐛 Giun Đũa",
    "🪱 Giun Móc",
    "🪲 Giun Kim", 
    "🐍 Sán Dây",
    "🪲 Sán Lá Gan",
    "🦠 Lỵ Amip",
    "💧 Nhiễm Ký Sinh Giardia",
    "🐱 Toxoplasma",
    "🦟 Sốt Rét"
])

with tab1:
    render_ascarid_tab()

with tab2:
    render_hookworm_tab()

with tab3:
    render_pinworm_tab()

with tab4:
    render_tapeworm_tab()

with tab5:
    render_liver_fluke_tab()

with tab6:
    render_amoebic_dysentery_tab()

with tab7:
    render_giardiasis_tab()

with tab8:
    render_toxoplasmosis_tab()

with tab9:
    render_malaria_tab()

# Lưu ý cuối
st.divider()
st.markdown("""
<div class="warning-box">
    <b>⚠️ LƯU Ý QUAN TRỌNG:</b><br>
    • Thông tin chỉ mang tính <b>THAM KHẢO</b><br>
    • <b>KHÔNG THAY THẾ</b> tư vấn của bác sĩ<br>
    • Triệu chứng nặng: <b>KHÁM BÁC SĨ NGAY</b><br>
    • Thuốc tẩy giun cần <b>CHỈ ĐỊNH BÁC SĨ</b>
</div>
""", unsafe_allow_html=True)

