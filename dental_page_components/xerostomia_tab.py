"""
Xerostomia Tab Component
"""

import streamlit as st


from diseases.dental import XEROSTOMIA_INFO


def render_xerostomia_tab():
    """Tab Khô Miệng"""
    st.header("🦷 Khô Miệng (Xerostomia)")
    
    info = XEROSTOMIA_INFO
    
    # Thông tin cơ bản
    with st.expander("📖 Khô miệng là gì?", expanded=True):
        st.markdown(info.get("simple_explanation", ""))
        
        if "what_happens" in info:
            st.markdown("### Chuyện gì xảy ra:")
            st.markdown(info["what_happens"])
    
    # Triệu chứng
    if "symptoms" in info:
        with st.expander("⚠️ Triệu chứng", expanded=False):
            symptoms = info["symptoms"]
            if "common" in symptoms:
                for symptom in symptoms["common"]:
                    st.markdown(f"- {symptom}")
    
    # Nguyên nhân
    if "common_causes" in info:
        with st.expander("🔍 Nguyên nhân", expanded=False):
            causes = info["common_causes"]
            for cause in causes.get("causes", []):
                st.markdown(f"**{cause['name']}**")
                if "items" in cause:
                    for item in cause["items"]:
                        st.markdown(f"- {item}")
                elif "description" in cause:
                    st.markdown(cause["description"])
                st.divider()
    
    # Điều trị
    with st.expander("💊 Điều trị", expanded=False):
        if "treatment" in info:
            treatment = info["treatment"]
            
            if "immediate" in treatment:
                immediate = treatment["immediate"]
                st.markdown(f"### {immediate.get('title', '')}")
                for step in immediate.get("steps", []):
                    st.markdown(step)
            
            st.divider()
            
            if "professional" in treatment:
                prof = treatment["professional"]
                st.markdown(f"### {prof.get('title', '')}")
                for step in prof.get("steps", []):
                    st.markdown(step)
    
    # Chăm sóc tại nhà
    if "home_care" in info:
        with st.expander("🏠 Chăm sóc tại nhà", expanded=False):
            home = info["home_care"]
            st.markdown(f"### {home.get('title', '')}")
            for item in home.get("items", []):
                st.markdown(item)
    
    # Biến chứng
    if "complications" in info:
        with st.expander("⚠️ Biến chứng", expanded=False):
            complications = info["complications"]
            st.markdown(f"### {complications.get('title', '')}")
            for item in complications.get("items", []):
                st.markdown(f"- {item}")
    
    # Phòng ngừa
    if "prevention" in info:
        with st.expander("💡 Phòng ngừa", expanded=False):
            prevention = info["prevention"]
            st.markdown(f"### {prevention.get('title', '')}")
            for item in prevention.get("items", []):
                st.markdown(item)
    
    # Khi nào cần khám
    if "when_see_doctor" in info:
        st.divider()
        st.markdown(f"### {info['when_see_doctor'].get('title', '')}")
        for item in info["when_see_doctor"].get("items", []):
            st.markdown(item)
    
    # Lưu ý
    if "note" in info:
        st.info(info["note"])

