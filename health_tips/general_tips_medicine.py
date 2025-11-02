"""
General Health Tips - Medicine
Mẹo vặt về thuốc
DEPRECATED: Import từ health_tips.medicine_tips thay vì dùng trực tiếp
"""

import streamlit as st

from health_tips.medicine_tips import (
    render_storage_tab,
    render_taking_tab,
    render_food_interactions_tab,
    render_drug_interactions_tab,
    render_missed_dose_tab,
    render_reading_labels_tab
)


def render_medicine_tips():
    """Mẹo vặt về thuốc"""
    st.subheader("💊 Mẹo vặt về thuốc")
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📅 Bảo quản thuốc",
        "💧 Cách uống thuốc",
        "🍽️ Thuốc & Thức ăn",
        "🔄 Tương tác thuốc",
        "⏰ Quên uống thuốc",
        "📋 Đọc nhãn thuốc"
    ])
    
    with tab1:
        render_storage_tab()
    
    with tab2:
        render_taking_tab()
    
    with tab3:
        render_food_interactions_tab()
    
    with tab4:
        render_drug_interactions_tab()
    
    with tab5:
        render_missed_dose_tab()
    
    with tab6:
        render_reading_labels_tab()

