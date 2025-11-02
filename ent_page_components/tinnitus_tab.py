"""
Tinnitus Tab Component
Tab Ù Tai
"""

import streamlit as st


from diseases.ent import TINNITUS_INFO


def render_tinnitus_tab():
    """Tab Ù Tai"""
    st.header("🔊 Ù Tai (Tinnitus)")
    
    info = TINNITUS_INFO
    
    # Thông tin cơ bản
    with st.expander("📖 Ù tai là gì?", expanded=True):
        st.markdown(info.get("simple_explanation", ""))
        
        if "what_happens" in info:
            st.markdown(info["what_happens"])
    
    # Triệu chứng
    with st.expander("⚠️ Triệu chứng", expanded=True):
        if "symptoms" in info:
            symptoms = info["symptoms"]
            
            if "sounds" in symptoms:
                st.markdown("**Tiếng nghe được:**")
                for sound in symptoms["sounds"]:
                    st.markdown(sound)
            
            if "when_noticed" in symptoms:
                st.markdown("\n**Khi nào nghe rõ:**")
                for when in symptoms["when_noticed"]:
                    st.markdown(f"- {when}")
            
            if "severity" in symptoms:
                sev = symptoms["severity"]
                st.markdown("\n**Mức độ:**")
                if "mild" in sev:
                    st.info(f"Nhẹ: {sev['mild']}")
                if "moderate" in sev:
                    st.warning(f"Vừa: {sev['moderate']}")
                if "severe" in sev:
                    st.error(f"Nặng: {sev['severe']}")
    
    # Nguyên nhân
    with st.expander("🔍 Nguyên nhân", expanded=False):
        if "causes" in info:
            causes = info["causes"]
            
            if "common" in causes:
                st.markdown("**Nguyên nhân thường gặp:**")
                for cause in causes["common"]:
                    st.markdown(cause)
            
            if "less_common" in causes:
                st.markdown("\n**Nguyên nhân ít gặp hơn:**")
                for cause in causes["less_common"]:
                    st.markdown(f"- {cause}")
    
    # Điều trị
    with st.expander("💊 Điều trị", expanded=False):
        if "treatment" in info:
            treatment = info["treatment"]
            
            if "when_to_see_doctor" in treatment:
                when = treatment["when_to_see_doctor"]
                st.markdown(f"### {when.get('title', '')}")
                
                if "urgent" in when:
                    st.error("**🚨 Cấp cứu ngay:**")
                    for item in when["urgent"]:
                        st.markdown(item)
                    st.divider()
                
                if "soon" in when:
                    st.warning("**Khám trong vài ngày:**")
                    for item in when["soon"]:
                        st.markdown(item)
            
            st.divider()
            
            if "doctor_treatment" in treatment:
                doctor = treatment["doctor_treatment"]
                st.markdown(f"### {doctor.get('title', '')}")
                
                if "examination" in doctor:
                    for exam in doctor["examination"]:
                        st.markdown(exam)
                
                if "medications" in doctor:
                    for med in doctor["medications"]:
                        st.markdown(med)
            
            st.divider()
            
            if "home_care" in treatment:
                home = treatment["home_care"]
                st.markdown(f"### {home.get('title', '')}")
                
                if "masking" in home:
                    for tip in home["masking"]:
                        st.markdown(tip)
                
                if "relaxation" in home:
                    st.markdown("\n")
                    for tip in home["relaxation"]:
                        st.markdown(tip)
                
                if "protect_ears" in home:
                    st.markdown("\n")
                    for tip in home["protect_ears"]:
                        st.markdown(tip)
    
    # Phòng ngừa
    with st.expander("🛡️ Phòng ngừa", expanded=False):
        if "prevention" in info:
            prevention = info["prevention"]
            st.markdown(f"### {prevention.get('title', '')}")
            for tip in prevention.get("tips", []):
                st.markdown(tip)
    
    # Lưu ý
    if "note" in info:
        st.divider()
        st.warning(info["note"])

