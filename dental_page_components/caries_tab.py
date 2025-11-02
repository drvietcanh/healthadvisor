"""Caries Tab Component"""

import streamlit as st

from diseases.dental.caries import CARIES_INFO, SYMPTOMS, TREATMENT

def render_caries_tab():
    """Render tab Sâu Răng"""
    st.header("🦷 Sâu Răng (Dental Caries)")
    
    st.info("💡 **Thông tin:** Sâu răng là bệnh răng PHỔ BIẾN NHẤT. 90% người bị ít nhất 1 lần trong đời.")
    
    with st.expander("📖 Sâu răng là gì?", expanded=True):
        if CARIES_INFO:
            st.markdown(CARIES_INFO.get("simple_explanation", ""))
            if CARIES_INFO.get("why_important"):
                st.warning(CARIES_INFO["why_important"])
    
    with st.expander("🔍 Triệu chứng"):
        if SYMPTOMS:
            col1, col2, col3 = st.columns(3)
            with col1:
                if "early" in SYMPTOMS:
                    st.markdown(f"### {SYMPTOMS['early']['title']}")
                    for s in SYMPTOMS["early"]["symptoms"]:
                        st.markdown(f"- {s}")
                    if SYMPTOMS["early"].get("note"):
                        st.info(SYMPTOMS["early"]["note"])
            with col2:
                if "moderate" in SYMPTOMS:
                    st.markdown(f"### {SYMPTOMS['moderate']['title']}")
                    for s in SYMPTOMS["moderate"]["symptoms"]:
                        st.markdown(f"- {s}")
            with col3:
                if "severe" in SYMPTOMS:
                    st.markdown(f"### {SYMPTOMS['severe']['title']}")
                    for s in SYMPTOMS["severe"]["symptoms"]:
                        st.markdown(f"**{s}**")
    
    with st.expander("💊 Điều trị"):
        if TREATMENT:
            if "moderate" in TREATMENT:
                st.markdown(f"### {TREATMENT['moderate']['title']}")
                filling = TREATMENT["moderate"]["filling"]
                st.markdown(f"**{filling['title']}**")
                st.caption(filling["description"])
                st.markdown("**Quy trình:**")
                for step in filling.get("process", []):
                    st.markdown(f"- {step}")
                if filling.get("note"):
                    st.success(filling["note"])
            
            if "prevention" in TREATMENT:
                st.divider()
                st.markdown(f"### {TREATMENT['prevention']['title']}")
                prev = TREATMENT["prevention"]
                if "oral_hygiene" in prev:
                    st.markdown(f"**{prev['oral_hygiene']['title']}**")
                    for tip in prev["oral_hygiene"]["tips"]:
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
            if doctor.get("note"):
                st.info(doctor["note"])

