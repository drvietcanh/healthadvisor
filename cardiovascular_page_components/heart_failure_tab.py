"""
Tab 2: Suy Tim
Hiển thị thông tin về bệnh suy tim
"""

import streamlit as st
from diseases.cardiovascular import heart_failure

def render_heart_failure_tab():
    """Render tab Suy Tim"""
    st.header("Suy Tim")
    
    with st.expander("📖 Suy tim là gì?", expanded=True):
        st.markdown(heart_failure.DISEASE_INFO["simple_explanation_vn"])
    
    with st.expander("🚨 5 dấu hiệu chính - 5 chữ H"):
        signs = heart_failure.SYMPTOMS_SIMPLE["main_signs_vn"]
        st.subheader(signs["title"])
        
        for sign in signs["signs"]:
            st.markdown(f"### {sign['letter']}")
            st.markdown(f"**{sign['description']}**")
            for detail in sign['details']:
                st.markdown(detail)
            st.divider()
    
    with st.expander("💊 Thuốc điều trị (giải thích đơn giản)"):
        st.warning(heart_failure.MEDICATIONS_SIMPLE["warning_vn"])
        
        for drug in heart_failure.MEDICATIONS_SIMPLE["common_drugs_simple"][:2]:  # 2 thuốc đầu
            st.subheader(f"{drug['type']}")
            st.caption(drug['street_name'])
            st.markdown(f"**Tác dụng:** {drug['what_it_does']}")
            
            st.markdown("**Lợi ích:**")
            for benefit in drug['benefits']:
                st.markdown(benefit)
    
    with st.expander("🍽️ Chế độ ăn cho người suy tim"):
        st.markdown(heart_failure.NUTRITION_SIMPLE["main_rule_vn"])
        st.info(heart_failure.NUTRITION_SIMPLE["salt_restriction_simple"]["why_vn"])

