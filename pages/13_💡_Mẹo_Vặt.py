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
from core.ui_config import get_custom_css

st.set_page_config(
    page_title="Mẹo Vặt Y Tế",
    page_icon="💡",
    layout="wide"
)

# Áp dụng Dark Mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)

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
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💊 Máy tính Paracetamol",
    "🌡️ Xử trí sốt",
    "💊 Thuốc & Thức ăn",
    "🌱 Chăm sóc hàng ngày",
    "🛡️ Phòng bệnh"
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
    
    from health_tips.paracetamol_calculator import get_paracetamol_guidelines
    st.markdown(get_paracetamol_guidelines())

# Tab 2: Xử trí sốt
with tab2:
    render_fever_tips()
    
    st.divider()
    
    render_temperature_guide()

# Tab 3: Thuốc & Thức ăn
with tab3:
    render_medicine_tips()

# Tab 4: Chăm sóc hàng ngày
with tab4:
    render_daily_health_tips()

# Tab 5: Phòng bệnh
with tab5:
    render_preventive_care()

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

