"""Trào Ngược Dạ Dày Tab Component"""

import streamlit as st
from diseases.digestive import gerd


def render_gerd_tab():
    """Render tab Trào Ngược Dạ Dày"""
    st.header("🌡️ Trào Ngược Dạ Dày-Thực Quản (GERD)")
    
    if hasattr(gerd, 'GERD_INFO'):
        info = gerd.GERD_INFO
        with st.expander("📖 Trào ngược dạ dày là gì?", expanded=True):
            st.markdown(info.get("simple_explanation", ""))
    
    if hasattr(gerd, 'SYMPTOMS'):
        symptoms = gerd.SYMPTOMS
        with st.expander("🔍 Triệu chứng"):
            for symptom in symptoms["common"]:
                st.markdown(f"- {symptom}")
    
    if hasattr(gerd, 'TREATMENT'):
        treatment = gerd.TREATMENT
        with st.expander("💊 Điều trị"):
            if "lifestyle" in treatment:
                st.markdown("**Thay đổi lối sống:**")
                for method in treatment["lifestyle"]["methods"]:
                    st.markdown(f"- {method}")

