"""
Đục Thủy Tinh Thể Tab Component
"""

import streamlit as st
from diseases.eye import cataract


def render_cataract_tab():
    """Render tab Đục Thủy Tinh Thể"""
    st.header("👁️ Đục Thủy Tinh Thể (Cataract)")
    
    with st.expander("📖 Đục thủy tinh thể là gì?", expanded=True):
        if hasattr(cataract, 'CATARACT_INFO') and cataract.CATARACT_INFO:
            info = cataract.CATARACT_INFO
            st.markdown(info.get("simple_explanation", ""))
    
    with st.expander("🔍 Triệu chứng", expanded=True):
        if hasattr(cataract, 'SYMPTOMS') and cataract.SYMPTOMS:
            symptoms = cataract.SYMPTOMS
            if "common_symptoms" in symptoms:
                common = symptoms["common_symptoms"]
                st.markdown(f"### {common.get('title', '')}")
                if "symptoms" in common:
                    for symptom in common["symptoms"][:4]:
                        if isinstance(symptom, dict):
                            st.markdown(f"**{symptom.get('icon', '')} {symptom.get('name', '')}**")
                            st.caption(symptom.get('description', ''))
                            st.divider()
    
    with st.expander("🔪 Điều trị"):
        if hasattr(cataract, 'TREATMENT') and cataract.TREATMENT:
            treatment = cataract.TREATMENT
            if "surgery" in treatment:
                surgery = treatment["surgery"]
                st.markdown(f"### {surgery.get('title', '')}")
                st.caption(surgery.get('description', ''))
                if "when_to_operate" in surgery:
                    when = surgery["when_to_operate"]
                    st.markdown(f"### {when.get('title', '')}")
                    if "indicators" in when:
                        for indicator in when["indicators"][:2]:
                            if isinstance(indicator, dict):
                                st.markdown(f"**{indicator.get('name', '')}**")
                                st.caption(indicator.get('description', ''))
    
    with st.expander("🛡️ Phòng ngừa"):
        if hasattr(cataract, 'PREVENTION') and cataract.PREVENTION:
            prev = cataract.PREVENTION
            if "sun_protection" in prev:
                sun = prev["sun_protection"]
                st.markdown(f"### {sun.get('title', '')}")
                st.caption(sun.get('description', ''))
                if "methods" in sun:
                    for method in sun["methods"]:
                        if isinstance(method, dict):
                            st.markdown(f"**{method.get('name', '')}**")
                            if method.get('benefit'):
                                st.success(f"Lợi ích: {method['benefit']}")

