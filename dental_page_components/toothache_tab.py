"""
Toothache Tab Component
"""

import streamlit as st


from diseases.dental import TOOTHACHE_INFO


def render_toothache_tab():
    """Tab Đau Răng Cấp"""
    st.header("🦷 Đau Răng Cấp (Toothache)")
    
    info = TOOTHACHE_INFO
    
    # Thông tin cơ bản
    with st.expander("📖 Đau răng cấp là gì?", expanded=True):
        st.markdown(info.get("simple_explanation", ""))
    
    # Nguyên nhân
    if "common_causes" in info:
        with st.expander("🔍 Nguyên nhân", expanded=False):
            causes = info["common_causes"]
            for cause in causes.get("causes", []):
                st.markdown(f"**{cause['name']}**")
                st.markdown(cause["description"])
                st.divider()
    
    # Triệu chứng
    if "symptoms" in info:
        with st.expander("⚠️ Triệu chứng", expanded=False):
            symptoms = info["symptoms"]
            if "pain" in symptoms:
                pain = symptoms["pain"]
                st.markdown(f"### {pain.get('title', '')}")
                for ptype in pain.get("types", []):
                    st.markdown(ptype)
            if "other" in symptoms:
                st.markdown("**Triệu chứng khác:**")
                for symptom in symptoms["other"]:
                    st.markdown(f"- {symptom}")
    
    # Giảm đau tạm thời
    if "immediate_relief" in info:
        with st.expander("⚡ Giảm đau tạm thời", expanded=True):
            relief = info["immediate_relief"]
            st.markdown(f"### {relief.get('title', '')}")
            for step in relief.get("steps", []):
                st.markdown(step)
            if "warning" in relief:
                st.warning(relief["warning"])
    
    # Điều trị
    if "treatment" in info:
        with st.expander("💊 Điều trị tại nha sĩ", expanded=False):
            treatment = info["treatment"]
            st.markdown(f"### {treatment.get('title', '')}")
            for step in treatment.get("steps", []):
                st.markdown(step)
    
    # Khi nào cần khám cấp cứu
    if "when_see_dentist_urgent" in info:
        st.divider()
        st.markdown(f"### {info['when_see_dentist_urgent'].get('title', '')}")
        for item in info["when_see_dentist_urgent"].get("items", []):
            st.markdown(item)
    
    # Khi nào cần khám sớm
    if "when_see_dentist_soon" in info:
        st.markdown(f"### {info['when_see_dentist_soon'].get('title', '')}")
        for item in info["when_see_dentist_soon"].get("items", []):
            st.markdown(item)
    
    # Phòng ngừa
    if "prevention" in info:
        with st.expander("💡 Phòng ngừa", expanded=False):
            prevention = info["prevention"]
            st.markdown(f"### {prevention.get('title', '')}")
            for item in prevention.get("items", []):
                st.markdown(item)
    
    # Lưu ý
    if "note" in info:
        st.warning(info["note"])

