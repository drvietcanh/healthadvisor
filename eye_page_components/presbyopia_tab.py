"""Presbyopia Tab Component"""

import streamlit as st

from diseases.eye.presbyopia import PRESBYOPIA_INFO, SYMPTOMS, TREATMENT

def render_presbyopia_tab():
    """Render tab Lão Thị"""
    st.header("👓 Lão Thị (Presbyopia)")
    
    st.info("💡 **Lưu ý:** Lão thị là quá trình lão hóa tự nhiên, không phải bệnh. Ai cũng sẽ bị sau 40-45 tuổi.")
    
    with st.expander("📖 Lão thị là gì?", expanded=True):
        if PRESBYOPIA_INFO:
            st.markdown(PRESBYOPIA_INFO.get("simple_explanation", ""))
            if PRESBYOPIA_INFO.get("why_important"):
                st.warning(PRESBYOPIA_INFO["why_important"])
            if "statistics" in PRESBYOPIA_INFO:
                stats = PRESBYOPIA_INFO["statistics"]
                st.info(f"📊 **Thống kê:** {stats.get('prevalence', '')}")
    
    with st.expander("🔍 Triệu chứng"):
        if SYMPTOMS:
            if "common" in SYMPTOMS:
                st.markdown(f"### {SYMPTOMS['common']['title']}")
                for s in SYMPTOMS["common"]["symptoms"]:
                    st.markdown(f"- {s}")
            
            if "vs_other" in SYMPTOMS:
                st.divider()
                st.markdown(f"### {SYMPTOMS['vs_other']['title']}")
                for diff in SYMPTOMS["vs_other"]["differences"]:
                    st.markdown(f"- {diff}")
    
    with st.expander("💊 Điều trị"):
        if TREATMENT:
            if "glasses" in TREATMENT:
                st.markdown(f"### {TREATMENT['glasses']['title']}")
                glasses = TREATMENT["glasses"]
                if "reading_glasses" in glasses:
                    st.markdown(f"**{glasses['reading_glasses']['title']}**")
                    st.caption(glasses["reading_glasses"]["description"])
                    st.markdown("**Cách chọn:**")
                    for tip in glasses["reading_glasses"].get("how_to_choose", []):
                        st.markdown(f"- {tip}")
                    if glasses["reading_glasses"].get("note"):
                        st.warning(glasses["reading_glasses"]["note"])
            
            if "lifestyle" in TREATMENT:
                st.divider()
                st.markdown(f"### {TREATMENT['lifestyle']['title']}")
                for tip in TREATMENT["lifestyle"]["tips"]:
                    st.markdown(tip)
    
    with st.expander("🏥 Khi nào cần khám bác sĩ"):
        if TREATMENT and "when_to_see_doctor" in TREATMENT:
            doctor = TREATMENT["when_to_see_doctor"]
            for item in doctor.get("soon", []):
                st.markdown(f"- {item}")
            if doctor.get("note"):
                st.info(doctor["note"])

