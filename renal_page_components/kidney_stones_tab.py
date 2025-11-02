"""Sỏi Thận Tab Component"""

import streamlit as st
from diseases.renal import kidney_stones


def render_kidney_stones_tab():
    """Render tab Sỏi Thận"""
    st.header("🪨 Sỏi Thận")
    
    if hasattr(kidney_stones, 'KIDNEY_STONES_INFO'):
        info = kidney_stones.KIDNEY_STONES_INFO
        with st.expander("📖 Sỏi thận là gì?", expanded=True):
            st.markdown(info.get("simple_explanation", ""))
    
    if hasattr(kidney_stones, 'SYMPTOMS'):
        symptoms = kidney_stones.SYMPTOMS
        with st.expander("🔍 Triệu chứng"):
            if "pain" in symptoms:
                for symptom in symptoms["pain"]["symptoms"]:
                    st.markdown(f"- {symptom}")
    
    if hasattr(kidney_stones, 'TREATMENT'):
        treatment = kidney_stones.TREATMENT
        with st.expander("💊 Điều trị"):
            if "prevention" in treatment:
                st.markdown("**Phòng ngừa:**")
                for method in treatment["prevention"]["methods"]:
                    st.markdown(f"- {method}")

