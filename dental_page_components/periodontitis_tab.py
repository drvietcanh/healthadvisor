"""
Periodontitis Tab Component
"""

import streamlit as st
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from diseases.dental import PERIODONTITIS_INFO


def render_periodontitis_tab():
    """Tab Viêm Quanh Răng"""
    st.header("🦷 Viêm Quanh Răng (Periodontitis)")
    
    info = PERIODONTITIS_INFO
    
    # Thông tin cơ bản
    with st.expander("📖 Viêm quanh răng là gì?", expanded=True):
        st.markdown(info.get("simple_explanation", ""))
        
        if "what_happens" in info:
            st.markdown("### Chuyện gì xảy ra:")
            st.markdown(info["what_happens"])
    
    # Triệu chứng
    with st.expander("⚠️ Triệu chứng", expanded=False):
        if "symptoms" in info:
            symptoms = info["symptoms"]
            if "early" in symptoms:
                st.markdown("**Giai đoạn sớm:**")
                for symptom in symptoms["early"]:
                    st.markdown(f"- {symptom}")
            if "advanced" in symptoms:
                st.markdown("**Giai đoạn nặng:**")
                for symptom in symptoms["advanced"]:
                    st.markdown(f"- {symptom}")
    
    # Giai đoạn
    if "stages" in info:
        with st.expander("📊 Giai đoạn bệnh", expanded=False):
            stages = info["stages"]
            for key, stage in stages.items():
                st.markdown(f"**{stage['name']}**")
                st.markdown(stage["description"])
                st.divider()
    
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
    if "prevention" in info:
        with st.expander("💡 Phòng ngừa", expanded=False):
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
        st.warning(info["note"])

