"""
Trang tư vấn về bệnh Hô Hấp
COPD và Hen Suyễn
"""

import streamlit as st
import sys
sys.path.append('..')

from diseases.respiratory import copd, asthma
from core.ui_config import get_custom_css

st.set_page_config(page_title="Hô Hấp", page_icon="🫁", layout="wide")

# Áp dụng Dark Mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)

st.title("🫁 Tư vấn Hô Hấp")

# Tabs cho các bệnh hô hấp
tab1, tab2 = st.tabs(["🫁 COPD (Phổi Tắc Nghẽn)", "🌬️ Hen Suyễn"])

with tab1:
    st.header("🫁 COPD - Bệnh Phổi Tắc Nghẽn Mạn Tính")
    
    # Thông tin cơ bản
    with st.expander("📖 COPD là gì?", expanded=True):
        if hasattr(copd, 'COPD_INFO') and copd.COPD_INFO:
            info_dict = copd.COPD_INFO
            if isinstance(info_dict, dict):
                st.markdown(info_dict.get("what_is_it", info_dict.get("simple_explanation", "")))
                if info_dict.get("why_dangerous"):
                    st.warning(info_dict.get("why_dangerous"))
    
    # Nguyên nhân
    with st.expander("🔍 Nguyên nhân COPD"):
        if hasattr(copd, 'CAUSES') and copd.CAUSES:
            if isinstance(copd.CAUSES, dict):
                for cause_key, cause_info in list(copd.CAUSES.items())[:5]:
                    if isinstance(cause_info, dict):
                        st.markdown(f"**{cause_info.get('name', cause_key)}**")
                        st.caption(cause_info.get('description', ''))
                        st.divider()
    
    # Triệu chứng
    with st.expander("🩺 Triệu chứng COPD"):
        if hasattr(copd, 'SYMPTOMS') and copd.SYMPTOMS:
            for symptom_key, symptom_info in copd.SYMPTOMS.items():
                if isinstance(symptom_info, dict):
                    st.markdown(f"**{symptom_info.get('name', symptom_key)}:**")
                    st.caption(symptom_info.get('description', ''))
                    st.divider()
    
    # Điều trị
    with st.expander("💊 Điều trị COPD"):
        st.markdown("### Nguyên tắc điều trị")
        if hasattr(copd, 'TREATMENT_PRINCIPLES') and copd.TREATMENT_PRINCIPLES:
            principles = copd.TREATMENT_PRINCIPLES
            if isinstance(principles, dict):
                st.markdown(principles.get("overview", ""))
        
        st.markdown("### Thuốc giãn phế quản")
        if hasattr(copd, 'BRONCHODILATORS') and copd.BRONCHODILATORS:
            for med_key, med_info in list(copd.BRONCHODILATORS.items())[:3]:
                if isinstance(med_info, dict):
                    st.markdown(f"**{med_info.get('name', med_key)}**")
                    st.caption(med_info.get('description', ''))
    
    # Vận động và tập luyện
    with st.expander("🏃 Vận động & Tập luyện"):
        if hasattr(copd, 'EXERCISE_BENEFITS') and copd.EXERCISE_BENEFITS:
            benefits = copd.EXERCISE_BENEFITS
            if isinstance(benefits, dict):
                st.markdown(benefits.get("overview", ""))
        
        st.markdown("### Kỹ thuật thở")
        if hasattr(copd, 'BREATHING_TECHNIQUES') and copd.BREATHING_TECHNIQUES:
            techniques = copd.BREATHING_TECHNIQUES
            if isinstance(techniques, dict):
                for tech_key, tech_info in list(techniques.items())[:2]:
                    if isinstance(tech_info, dict):
                        st.markdown(f"**{tech_info.get('name', tech_key)}**")
                        st.caption(tech_info.get('description', ''))

with tab2:
    st.header("🌬️ Hen Suyễn (Asthma)")
    
    # Thông tin cơ bản
    with st.expander("📖 Hen suyễn là gì?", expanded=True):
        if hasattr(asthma, 'ASTHMA_INFO') and asthma.ASTHMA_INFO:
            info_dict = asthma.ASTHMA_INFO
            if isinstance(info_dict, dict):
                st.markdown(info_dict.get("simple_explanation", info_dict.get("what_is_it", "")))
                if info_dict.get("what_happens"):
                    what_happens = info_dict.get("what_happens", {})
                    if isinstance(what_happens, dict):
                        st.markdown(f"### {what_happens.get('title', '')}")
                        mechanisms = what_happens.get("mechanisms", [])
                        for mech in mechanisms[:3]:
                            if isinstance(mech, dict):
                                st.markdown(f"**{mech.get('step', '')}**")
                                st.caption(f"{mech.get('analogy', '')} → {mech.get('result', '')}")
    
    # Nguyên nhân
    with st.expander("🔍 Nguyên nhân hen suyễn"):
        if hasattr(asthma, 'CAUSES') and asthma.CAUSES:
            causes = asthma.CAUSES
            if isinstance(causes, dict):
                for cause_key, cause_info in list(causes.items())[:5]:
                    if isinstance(cause_info, dict):
                        st.markdown(f"**{cause_info.get('name', cause_key)}**")
                        st.caption(cause_info.get('description', ''))
                        st.divider()
    
    # Triệu chứng
    with st.expander("🩺 Triệu chứng hen suyễn"):
        if hasattr(asthma, 'SYMPTOMS') and asthma.SYMPTOMS:
            symptoms = asthma.SYMPTOMS
            if isinstance(symptoms, dict):
                for symptom_key, symptom_info in symptoms.items():
                    if isinstance(symptom_info, dict):
                        st.markdown(f"**{symptom_info.get('name', symptom_key)}:**")
                        st.caption(symptom_info.get('description', ''))
                        st.divider()
    
    # Yếu tố kích phát
    with st.expander("⚠️ Yếu tố kích phát"):
        if hasattr(asthma, 'TRIGGERS') and asthma.TRIGGERS:
            triggers = asthma.TRIGGERS
            if isinstance(triggers, dict):
                for trigger_key, trigger_info in list(triggers.items())[:5]:
                    if isinstance(trigger_info, dict):
                        st.markdown(f"**{trigger_info.get('name', trigger_key)}**")
                        st.caption(trigger_info.get('description', ''))
                        st.divider()
    
    # Phân loại mức độ
    with st.expander("📊 Phân loại mức độ hen suyễn"):
        if hasattr(asthma, 'SEVERITY_CLASSIFICATION') and asthma.SEVERITY_CLASSIFICATION:
            severity = asthma.SEVERITY_CLASSIFICATION
            if isinstance(severity, dict):
                for severity_key, severity_info in severity.items():
                    if isinstance(severity_info, dict):
                        st.markdown(f"**{severity_info.get('name', severity_key)}**")
                        st.caption(severity_info.get('description', ''))
                        st.divider()

# Nút quay lại
st.divider()
if st.button("🏠 Về Trang Chủ"):
    st.switch_page("app.py")

