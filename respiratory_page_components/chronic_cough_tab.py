"""Ho Mãn Tính Tab Component"""

import streamlit as st
import sys
sys.path.append('..')
from diseases.respiratory import chronic_cough


def render_chronic_cough_tab():
    """Render tab Ho Mãn Tính"""
    st.header("🤧 Ho Mãn Tính")
    
    if hasattr(chronic_cough, 'CHRONIC_COUGH_INFO'):
        info = chronic_cough.CHRONIC_COUGH_INFO
        with st.expander("📖 Ho mãn tính là gì?", expanded=True):
            st.markdown(info.get("simple_explanation", ""))
    
    if hasattr(chronic_cough, 'CAUSES'):
        causes = chronic_cough.CAUSES
        with st.expander("🔍 Nguyên nhân"):
            for cause in causes["common"]:
                st.markdown(f"- {cause}")

