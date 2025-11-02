"""
Tab 4: Đo Huyết Áp
Công cụ đánh giá và phân loại huyết áp
"""

import streamlit as st
from core.utils import classify_blood_pressure

def render_blood_pressure_tab():
    """Render tab Đo Huyết Áp"""
    st.header("📊 Công cụ đánh giá huyết áp")
    
    st.markdown("Nhập huyết áp của bạn để xem phân loại:")
    
    col1, col2 = st.columns(2)
    with col1:
        systolic = st.number_input(
            "Huyết áp tâm thu (số trên)",
            min_value=70,
            max_value=250,
            value=120,
            step=1
        )
    with col2:
        diastolic = st.number_input(
            "Huyết áp tâm trương (số dưới)",
            min_value=40,
            max_value=150,
            value=80,
            step=1
        )
    
    if st.button("Đánh giá", type="primary"):
        result = classify_blood_pressure(systolic, diastolic)
        
        if result["color"] == "red":
            st.error(f"### {result['name_vn']}")
            st.error(f"**Huyết áp: {systolic}/{diastolic} mmHg**")
            st.error(f"**{result['action_vn']}**")
        elif result["color"] == "orange":
            st.warning(f"### {result['name_vn']}")
            st.warning(f"**Huyết áp: {systolic}/{diastolic} mmHg**")
            st.warning(f"**{result['action_vn']}**")
        elif result["color"] == "yellow":
            st.info(f"### {result['name_vn']}")
            st.info(f"**Huyết áp: {systolic}/{diastolic} mmHg**")
            st.info(f"**{result['action_vn']}**")
        else:
            st.success(f"### {result['name_vn']}")
            st.success(f"**Huyết áp: {systolic}/{diastolic} mmHg**")
            st.success(f"**{result['action_vn']}**")
        
        # Hiển thị bảng phân loại
        st.subheader("Bảng phân loại huyết áp:")
        st.table({
            "Phân loại": ["Bình thường", "Cao bình thường", "THA Độ 1", "THA Độ 2", "Cơn tăng huyết áp"],
            "Tâm thu (mmHg)": ["< 120", "120-129", "130-139", "≥ 140", "≥ 180"],
            "Tâm trương (mmHg)": ["< 80", "< 80", "80-89", "≥ 90", "≥ 120"]
        })

