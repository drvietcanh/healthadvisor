"""Thoái Hóa Hoàng Điểm Tab Component"""

import streamlit as st
from diseases.eye import amd


def render_amd_tab():
    """Render tab Thoái Hóa Hoàng Điểm"""
    st.header("👁️ Thoái Hóa Hoàng Điểm (AMD)")
    
    if hasattr(amd, 'AMD_INFO'):
        info = amd.AMD_INFO
        with st.expander("📖 Thoái hóa hoàng điểm là gì?", expanded=True):
            st.markdown(info.get("simple_explanation", ""))
            st.error("⚠️ Nguyên nhân mù hàng đầu ở người già!")
    
    if hasattr(amd, 'TREATMENT'):
        treatment = amd.TREATMENT
        with st.expander("🛡️ Phòng ngừa"):
            if "prevention" in treatment:
                prev = treatment["prevention"]
                st.markdown("**Vitamin:**")
                for vitamin in prev["vitamins"]:
                    st.markdown(f"- {vitamin}")

