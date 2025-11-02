"""Xơ Vữa Động Mạch Tab Component"""

import streamlit as st
import sys
sys.path.append('..')
from diseases.cardiovascular import atherosclerosis


def render_atherosclerosis_tab():
    """Render tab Xơ Vữa Động Mạch"""
    st.header("🫀 Xơ Vữa Động Mạch")
    
    if hasattr(atherosclerosis, 'ATHEROSCLEROSIS_INFO'):
        info = atherosclerosis.ATHEROSCLEROSIS_INFO
        with st.expander("📖 Xơ vữa động mạch là gì?", expanded=True):
            st.markdown(info.get("simple_explanation", ""))
    
    if hasattr(atherosclerosis, 'PREVENTION'):
        prev = atherosclerosis.PREVENTION
        with st.expander("🛡️ Phòng ngừa"):
            for method in prev["methods"]:
                st.markdown(f"- {method}")

