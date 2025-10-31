"""
Tab 1: Tăng Huyết Áp
Hiển thị thông tin về bệnh tăng huyết áp
"""

import streamlit as st
from diseases.cardiovascular import hypertension

def render_hypertension_tab():
    """Render tab Tăng Huyết Áp"""
    st.header("Tăng Huyết Áp (Cao huyết áp)")
    
    # Giới thiệu
    with st.expander("📖 Tăng huyết áp là gì?", expanded=True):
        st.markdown(hypertension.DISEASE_INFO["description_vn"])
        st.info(f"**Phổ biến:** {hypertension.DISEASE_INFO['prevalence_vn']}")
    
    # Triệu chứng
    with st.expander("🔍 Dấu hiệu nhận biết"):
        st.subheader("Triệu chứng thường gặp:")
        for symptom in hypertension.SYMPTOMS["common_vn"]:
            st.markdown(f"- {symptom}")
        
        st.error("**⚠️ TRIỆU CHỨNG NGUY HIỂM - GỌI 115:**")
        for symptom in hypertension.SYMPTOMS["emergency_vn"]:
            st.markdown(f"**{symptom}**")
    
    # Thuốc
    with st.expander("💊 Thuốc điều trị"):
        st.warning(hypertension.MEDICATIONS["overview_vn"])
        
        for drug_key, drug_info in hypertension.MEDICATIONS["drug_classes"].items():
            st.subheader(drug_info["name_vn"])
            st.markdown(f"**Ví dụ:** {', '.join(drug_info['examples_vn'])}")
            st.markdown(f"**Cơ chế:** {drug_info['mechanism_vn']}")
            st.markdown(f"💡 {drug_info['note_vn']}")
            st.divider()
    
    # Chế độ ăn
    with st.expander("🍽️ Chế độ ăn DASH"):
        st.markdown(hypertension.NUTRITION_PLAN["overview_vn"])
        
        col1, col2 = st.columns(2)
        with col1:
            st.success("**✅ NÊN ĂN:**")
            for category, foods in hypertension.NUTRITION_PLAN["recommended_foods"].items():
                if category != "healthy_fats_vn":
                    st.markdown(f"**{category.replace('_vn', '').title()}:**")
                    for food in foods[:3]:  # Chỉ hiển thị 3 món đầu
                        st.markdown(f"- {food}")
        
        with col2:
            st.error("**🚫 TRÁNH:**")
            for category, foods in hypertension.NUTRITION_PLAN["foods_to_avoid"].items():
                for food in foods[:4]:
                    st.markdown(f"{food}")
        
        st.info(hypertension.NUTRITION_PLAN["sodium_limit_vn"])
    
    # Vận động
    with st.expander("🏃 Vận động & Luyện tập"):
        st.markdown(hypertension.EXERCISE_PLAN["overview_vn"])
        
        for exercise_type, details in hypertension.EXERCISE_PLAN["recommended_exercises"].items():
            st.subheader(f"{details['name']}")
            st.markdown(f"**Ví dụ:** {', '.join(details['examples'][:3])}")
            st.markdown(f"**Tần suất:** {details['frequency']}")
            st.markdown(f"**Thời gian:** {details['duration']}")

