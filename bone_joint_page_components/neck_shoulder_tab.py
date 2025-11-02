"""
Đau Cổ Vai Gáy Tab Component
"""

import streamlit as st
import sys
sys.path.append('..')
from diseases.bone_joint import neck_shoulder_pain


def render_neck_shoulder_tab():
    """Render tab Đau Cổ Vai Gáy"""
    st.header("💆 Đau Cổ Vai Gáy")
    
    if hasattr(neck_shoulder_pain, 'NECK_SHOULDER_PAIN_INFO'):
        info = neck_shoulder_pain.NECK_SHOULDER_PAIN_INFO
        with st.expander("📖 Đau cổ vai gáy là gì?", expanded=True):
            st.markdown(info.get("simple_explanation", ""))
    
    if hasattr(neck_shoulder_pain, 'SYMPTOMS'):
        symptoms = neck_shoulder_pain.SYMPTOMS
        with st.expander("🔍 Triệu chứng"):
            if "pain" in symptoms:
                st.markdown("**Triệu chứng:**")
                for symptom in symptoms["pain"]["symptoms"]:
                    st.markdown(f"- {symptom}")
    
    if hasattr(neck_shoulder_pain, 'TREATMENT'):
        treatment = neck_shoulder_pain.TREATMENT
        with st.expander("💊 Điều trị"):
            if "self_care" in treatment:
                st.markdown("**Tự chăm sóc:**")
                for method in treatment["self_care"]["methods"]:
                    st.markdown(f"- {method}")
            if "prevention" in treatment:
                st.markdown("**Phòng ngừa:**")
                for method in treatment["prevention"]["methods"]:
                    st.markdown(f"- {method}")

