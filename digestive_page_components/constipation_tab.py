"""Táo Bón Tab Component"""

import streamlit as st
import sys
sys.path.append('..')
from diseases.digestive import constipation


def render_constipation_tab():
    """Render tab Táo Bón"""
    st.header("🚽 Táo Bón")
    
    if hasattr(constipation, 'CONSTIPATION_INFO'):
        info = constipation.CONSTIPATION_INFO
        with st.expander("📖 Táo bón là gì?", expanded=True):
            st.markdown(info.get("simple_explanation", ""))
    
    if hasattr(constipation, 'TREATMENT'):
        treatment = constipation.TREATMENT
        with st.expander("💊 Điều trị"):
            if "diet" in treatment:
                st.markdown("**Chế độ ăn:**")
                for food in treatment["diet"]["foods"]:
                    st.markdown(f"- {food}")

