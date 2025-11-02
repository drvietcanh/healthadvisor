"""
Tinea Tab Component
Tab Nấm Da
"""

import streamlit as st


from diseases.dermatology import TINEA_INFO


def render_tinea_tab():
    """Tab Nấm Da"""
    st.header("🦶 Nấm Da (Tinea/Dermatophytosis)")
    
    info = TINEA_INFO
    
    # Thông tin cơ bản
    with st.expander("📖 Nấm da là gì?", expanded=True):
        st.markdown(info.get("simple_explanation", ""))
        
        if "what_happens" in info:
            st.markdown(info["what_happens"])
    
    # Triệu chứng
    with st.expander("⚠️ Triệu chứng", expanded=False):
        if "symptoms" in info:
            symptoms = info["symptoms"]
            if "common" in symptoms:
                st.markdown("**Dấu hiệu thường gặp:**")
                for symptom in symptoms["common"]:
                    st.markdown(f"- {symptom}")
            if "where_common" in symptoms:
                st.markdown("\n**Vị trí thường gặp:**")
                for location in symptoms["where_common"]:
                    st.markdown(location)
    
    # Nguyên nhân
    with st.expander("🔍 Nguyên nhân", expanded=False):
        if "causes" in info:
            causes = info["causes"]
            if "main" in causes:
                st.markdown("**Nguyên nhân chính:**")
                for cause in causes["main"]:
                    st.markdown(f"- {cause}")
            if "risk_factors" in causes:
                st.markdown("\n**Yếu tố nguy cơ:**")
                for factor in causes["risk_factors"]:
                    st.markdown(f"- {factor}")
    
    # Điều trị
    with st.expander("💊 Điều trị", expanded=False):
        if "treatment" in info:
            treatment = info["treatment"]
            
            if "home_care" in treatment:
                home = treatment["home_care"]
                st.markdown(f"### {home.get('title', '')}")
                for step in home.get("steps", []):
                    st.markdown(step)
                if "duration" in home:
                    st.info(home["duration"])
            
            st.divider()
            
            if "when_to_see_doctor" in treatment:
                when = treatment["when_to_see_doctor"]
                st.markdown(f"### {when.get('title', '')}")
                for reason in when.get("reasons", []):
                    st.markdown(reason)
            
            st.divider()
            
            if "doctor_treatment" in treatment:
                doctor = treatment["doctor_treatment"]
                st.markdown(f"### {doctor.get('title', '')}")
                for option in doctor.get("options", []):
                    st.markdown(option)
    
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

