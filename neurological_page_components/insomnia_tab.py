"""
Mất Ngủ Tab Component
"""

import streamlit as st
import sys
sys.path.append('..')
from diseases.neurological import insomnia


def render_insomnia_tab():
    """Render tab Mất Ngủ"""
    st.header("😴 Mất Ngủ (Insomnia)")
    
    with st.expander("📖 Mất ngủ là gì?", expanded=True):
        if hasattr(insomnia, 'INSOMNIA_INFO') and insomnia.INSOMNIA_INFO:
            info = insomnia.INSOMNIA_INFO
            st.markdown(info.get("simple_explanation", ""))
    
    with st.expander("🔍 Triệu chứng", expanded=True):
        if hasattr(insomnia, 'SYMPTOMS') and insomnia.SYMPTOMS:
            symptoms = insomnia.SYMPTOMS
            if "sleep_symptoms" in symptoms:
                sleep = symptoms["sleep_symptoms"]
                st.markdown(f"### {sleep.get('title', '')}")
                if "symptoms" in sleep:
                    for symptom in sleep["symptoms"][:3]:
                        if isinstance(symptom, dict):
                            st.markdown(f"**{symptom.get('icon', '')} {symptom.get('name', '')}**")
                            st.caption(symptom.get('description', ''))
                            st.divider()
    
    with st.expander("💊 Điều trị", expanded=True):
        if hasattr(insomnia, 'TREATMENT') and insomnia.TREATMENT:
            treatment = insomnia.TREATMENT
            if "non_medication" in treatment:
                non_med = treatment["non_medication"]
                st.markdown(f"### {non_med.get('title', '')}")
                st.caption(non_med.get('description', ''))
                if "methods" in non_med:
                    for method in non_med["methods"][:2]:
                        if isinstance(method, dict):
                            st.markdown(f"**{method.get('name', '')}**")
                            if "rules" in method:
                                for rule in method["rules"][:5]:
                                    st.markdown(f"- {rule}")
                            st.divider()

