"""
Tooth Loss Tab Component
"""

import streamlit as st
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from diseases.dental import TOOTH_LOSS_INFO


def render_tooth_loss_tab():
    """Tab Răng Lung Lay / Rụng Răng"""
    st.header("🦷 Răng Lung Lay / Rụng Răng")
    
    info = TOOTH_LOSS_INFO
    
    # Thông tin cơ bản
    with st.expander("📖 Răng lung lay là gì?", expanded=True):
        st.markdown(info.get("simple_explanation", ""))
    
    # Nguyên nhân
    if "common_causes" in info:
        with st.expander("🔍 Nguyên nhân", expanded=False):
            causes = info["common_causes"]
            for cause in causes.get("causes", []):
                st.markdown(f"**{cause['name']}**")
                st.markdown(cause["description"])
                st.divider()
    
    # Giai đoạn
    if "stages" in info:
        with st.expander("📊 Giai đoạn", expanded=False):
            stages = info["stages"]
            for key, stage in stages.items():
                st.markdown(f"**{stage['name']}**")
                st.markdown(stage["description"])
                st.divider()
    
    # Hậu quả
    if "consequences" in info:
        with st.expander("⚠️ Hậu quả khi mất răng", expanded=False):
            consequences = info["consequences"]
            st.markdown(f"### {consequences.get('title', '')}")
            for item in consequences.get("items", []):
                st.markdown(f"- {item}")
    
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
    
    # Thay thế răng
    if "tooth_replacement" in info:
        with st.expander("🦷 Các phương án thay thế răng", expanded=False):
            replacement = info["tooth_replacement"]
            for option in replacement.get("options", []):
                st.markdown(f"**{option['name']}**")
                st.markdown(option["description"])
                st.divider()
    
    # Phòng ngừa
    if "prevention" in info:
        with st.expander("💡 Phòng ngừa", expanded=False):
            prevention = info["prevention"]
            st.markdown(f"### {prevention.get('title', '')}")
            for item in prevention.get("items", []):
                st.markdown(item)
    
    # Khi nào cần khám
    if "when_see_dentist_urgent" in info:
        st.divider()
        st.markdown(f"### {info['when_see_dentist_urgent'].get('title', '')}")
        for item in info["when_see_dentist_urgent"].get("items", []):
            st.markdown(item)
    
    # Lưu ý
    if "note" in info:
        st.info(info["note"])

