"""Khô Mắt Tab Component"""

import streamlit as st
import sys
sys.path.append('..')
from diseases.eye import dry_eye


def render_dry_eye_tab():
    """Render tab Khô Mắt"""
    st.header("👁️ Khô Mắt")
    
    if hasattr(dry_eye, 'DRY_EYE_INFO'):
        info = dry_eye.DRY_EYE_INFO
        with st.expander("📖 Khô mắt là gì?", expanded=True):
            st.markdown(info.get("simple_explanation", ""))
    
    if hasattr(dry_eye, 'TREATMENT'):
        treatment = dry_eye.TREATMENT
        with st.expander("💊 Điều trị"):
            if "self_care" in treatment:
                st.markdown("**Tự chăm sóc:**")
                for method in treatment["self_care"]["methods"]:
                    st.markdown(f"- {method}")

