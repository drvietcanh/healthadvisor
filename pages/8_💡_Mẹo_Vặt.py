"""
Trang Mẹo Vặt Y Tế
Tổng hợp các mẹo vặt hữu ích hàng ngày về thuốc, chăm sóc sức khỏe
"""
import streamlit as st
import sys
import os

# Thêm thư mục gốc vào path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from health_tips import (
    render_paracetamol_calculator,
    render_fever_tips,
    render_temperature_guide,
    render_medicine_tips
)
from health_tips.daily_tips import (
    render_daily_health_tips,
    render_preventive_care
)
from health_tips.exercise_guide import (
    render_general_exercise_tips,
    render_disease_specific_exercises
)
from core.ui_config import get_custom_css
from core.sidebar_menu import render_sidebar_menu, hide_default_nav

st.set_page_config(
    page_title="Mẹo Vặt Y Tế",
    page_icon="💡",
    layout="wide"
)

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

# Header
st.title("💡 Mẹo Vặt Y Tế - Kiến thức hữu ích hàng ngày")
st.markdown("""
<div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            padding: 20px; border-radius: 10px; color: white; margin-bottom: 20px;'>
    <h3 style='margin:0; color: white;'>📚 Tổng hợp mẹo vặt từ chuyên gia y tế</h3>
    <p style='margin: 10px 0 0 0; opacity: 0.9;'>
        Các mẹo về thuốc, chăm sóc sức khỏe được tổng hợp từ các nguồn uy tín quốc tế.
        Áp dụng đúng cách để bảo vệ sức khỏe bạn và gia đình.
    </p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "💊 Máy tính Paracetamol",
    "🌡️ Xử trí sốt",
    "💊 Thuốc & Thức ăn",
    "🏃 Bài tập thể thao",
    "🌱 Chăm sóc hàng ngày",
    "🛡️ Phòng bệnh",
    "🍽️ Dinh dưỡng"
])

# Tab 1: Máy tính Paracetamol
with tab1:
    render_paracetamol_calculator()
    
    st.divider()
    
    st.markdown("""
    ### 📚 Thông tin thêm về Paracetamol
    
    Paracetamol là một trong những thuốc hạ sốt, giảm đau an toàn nhất, 
    nhưng cần dùng ĐÚNG CÁCH để tránh nguy hiểm.
    """)
    
    from health_tips.paracetamol import get_paracetamol_guidelines
    st.markdown(get_paracetamol_guidelines())

# Tab 2: Xử trí sốt
with tab2:
    render_fever_tips()
    
    st.divider()
    
    render_temperature_guide()

# Tab 3: Thuốc & Thức ăn
with tab3:
    render_medicine_tips()

# Tab 4: Bài tập thể thao
with tab4:
    render_general_exercise_tips()
    st.divider()
    render_disease_specific_exercises()

# Tab 5: Chăm sóc hàng ngày
with tab5:
    render_daily_health_tips()

# Tab 6: Phòng bệnh
with tab6:
    render_preventive_care()

# Tab 7: Dinh dưỡng
with tab7:
    from health_tips.daily_tips import render_nutrition_bone_health, render_nutrition_cholesterol
    
    st.markdown("### 🍽️ Mẹo Dinh Dưỡng")
    st.info("💡 Chọn một trong hai mẹo dinh dưỡng dưới đây:")
    
    sub_tab1, sub_tab2 = st.tabs(["🦴 Xương chắc khỏe", "❤️ Giảm Cholesterol"])
    
    with sub_tab1:
        render_nutrition_bone_health()
    
    with sub_tab2:
        render_nutrition_cholesterol()

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: gray; padding: 1rem;'>
    <p><small>
    ⚠️ <b>Lưu ý:</b> Các mẹo vặt này chỉ mang tính chất tham khảo. 
    Với các vấn đề sức khỏe nghiêm trọng, vui lòng tham khảo ý kiến bác sĩ.<br>
    HealthAdvisor - Vì sức khỏe cộng đồng
    </small></p>
</div>
""", unsafe_allow_html=True)

# Nút quay lại
st.divider()
if st.button("⬅️ Quay lại trang chính"):
    st.switch_page("app.py")

