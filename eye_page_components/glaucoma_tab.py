"""Tăng Nhãn Áp Tab Component"""

import streamlit as st
import sys
sys.path.append('..')
from diseases.eye import glaucoma


def render_glaucoma_tab():
    """Render tab Tăng Nhãn Áp"""
    st.header("👁️ Tăng Nhãn Áp (Glaucoma)")
    
    if hasattr(glaucoma, 'GLAUCOMA_INFO'):
        info = glaucoma.GLAUCOMA_INFO
        with st.expander("📖 Tăng nhãn áp là gì?", expanded=True):
            st.markdown(info.get("simple_explanation", ""))
            st.error("⚠️ Mất thị lực KHÔNG HỒI PHỤC được - Phải điều trị sớm!")
    
    if hasattr(glaucoma, 'TREATMENT'):
        treatment = glaucoma.TREATMENT
        with st.expander("💊 Điều trị"):
            if "medications" in treatment:
                st.markdown("**Thuốc:**")
                for drug in treatment["medications"]["drugs"]:
                    st.markdown(f"- {drug}")
                if treatment["medications"].get("warning"):
                    st.error(treatment["medications"]["warning"])

