"""
Gingivitis Tab Component
"""

import streamlit as st
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from diseases.dental import GINGIVITIS_INFO


def render_gingivitis_tab():
    """Tab Viêm Nướu"""
    st.header("🦷 Viêm Nướu (Gingivitis)")
    
    info = GINGIVITIS_INFO
    
    # Thông tin cơ bản
    with st.expander("📖 Viêm nướu là gì?", expanded=True):
        st.markdown(info.get("simple_explanation", ""))
        
        if "what_happens" in info:
            st.markdown("### Chuyện gì xảy ra:")
            st.markdown(info["what_happens"])
    
    # Triệu chứng
    with st.expander("⚠️ Triệu chứng", expanded=False):
        if "symptoms" in info:
            symptoms = info["symptoms"]
            if "common" in symptoms:
                st.markdown("**Dấu hiệu thường gặp:**")
                for symptom in symptoms["common"]:
                    st.markdown(f"- {symptom}")
            if "note" in symptoms:
                st.warning(symptoms["note"])
    
    # Nguyên nhân
    with st.expander("🔍 Nguyên nhân", expanded=False):
        if "causes" in info:
            causes = info["causes"]
            if "main" in causes:
                for cause in causes["main"]:
                    st.markdown(f"- {cause}")
    
    # Điều trị
    with st.expander("💊 Điều trị", expanded=False):
        if "treatment" in info:
            treatment = info["treatment"]
            
            if "professional" in treatment:
                prof = treatment["professional"]
                st.markdown(f"### {prof.get('title', '')}")
                for step in prof.get("steps", []):
                    st.markdown(step)
            
            st.divider()
            
            if "home_care" in treatment:
                home = treatment["home_care"]
                st.markdown(f"### {home.get('title', '')}")
                for step in home.get("steps", []):
                    st.markdown(step)
    
    # Phòng ngừa
    with st.expander("💡 Phòng ngừa", expanded=False):
        if "prevention" in info:
            prevention = info["prevention"]
            st.markdown(f"### {prevention.get('title', '')}")
            for item in prevention.get("items", []):
                st.markdown(item)
    
    # Khi nào cần khám
    if "when_see_dentist" in info:
        st.divider()
        st.markdown(f"### {info['when_see_dentist'].get('title', '')}")
        for item in info["when_see_dentist"].get("items", []):
            st.markdown(item)
    
    # Lưu ý
    if "note" in info:
        st.info(info["note"])

