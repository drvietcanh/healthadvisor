"""Chronic Sinusitis Tab Component"""

import streamlit as st

from diseases.ent.chronic_sinusitis import CHRONIC_SINUSITIS_INFO, SYMPTOMS, TREATMENT

def render_chronic_sinusitis_tab():
    """Render tab Viêm Xoang Mạn"""
    st.header("👃 Viêm Xoang Mạn (Chronic Sinusitis)")
    
    with st.expander("📖 Viêm xoang mạn là gì?", expanded=True):
        if CHRONIC_SINUSITIS_INFO:
            st.markdown(CHRONIC_SINUSITIS_INFO.get("simple_explanation", ""))
            if CHRONIC_SINUSITIS_INFO.get("why_important"):
                st.warning(CHRONIC_SINUSITIS_INFO["why_important"])
    
    with st.expander("🔍 Triệu chứng"):
        if SYMPTOMS:
            if "common" in SYMPTOMS:
                common = SYMPTOMS["common"]
                for key in ["nasal", "facial_pain", "other"]:
                    if key in common:
                        st.markdown(f"### {common[key]['title']}")
                        for s in common[key]["symptoms"]:
                            st.markdown(f"- {s}")
                        st.divider()
    
    with st.expander("💊 Điều trị"):
        if TREATMENT:
            if "medications" in TREATMENT:
                meds = TREATMENT["medications"]
                if "nasal_spray" in meds:
                    st.markdown(f"### {meds['nasal_spray']['title']}")
                    st.caption(f"**Cách hoạt động:** {meds['nasal_spray']['how_it_works']}")
                    st.markdown("**Cách dùng:**")
                    for tip in meds["nasal_spray"].get("how_to_use", []):
                        st.markdown(f"- {tip}")
                    if meds["nasal_spray"].get("note"):
                        st.warning(meds["nasal_spray"]["note"])
                
                if "nasal_rinse" in meds:
                    st.divider()
                    st.markdown(f"### {meds['nasal_rinse']['title']}")
                    st.markdown("**Lợi ích:**")
                    for benefit in meds["nasal_rinse"].get("benefits", []):
                        st.markdown(benefit)
            
            if "lifestyle" in TREATMENT:
                st.divider()
                st.markdown(f"### {TREATMENT['lifestyle']['title']}")
                for tip in TREATMENT["lifestyle"]["tips"]:
                    st.markdown(tip)
    
    with st.expander("🏥 Khi nào cần khám bác sĩ"):
        if SYMPTOMS and "when_to_see_doctor" in SYMPTOMS:
            doctor = SYMPTOMS["when_to_see_doctor"]
            col1, col2 = st.columns(2)
            with col1:
                st.warning("**📋 KHÁM SỚM:**")
                for item in doctor.get("soon", []):
                    st.markdown(f"- {item}")
            with col2:
                st.error("**🚨 KHẨN CẤP:**")
                for item in doctor.get("urgent", []):
                    st.markdown(f"- {item}")

