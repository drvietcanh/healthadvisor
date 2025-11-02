"""Nocturia Tab Component"""

import streamlit as st
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

from diseases.renal.nocturia import NOCTURIA_INFO, CAUSES, TREATMENT

def render_nocturia_tab():
    """Render tab Tiểu Đêm"""
    st.header("🌙 Tiểu Đêm (Nocturia)")
    
    with st.expander("📖 Tiểu đêm là gì?", expanded=True):
        if NOCTURIA_INFO:
            st.markdown(NOCTURIA_INFO.get("simple_explanation", ""))
            if NOCTURIA_INFO.get("why_important"):
                st.warning(NOCTURIA_INFO["why_important"])
            if "statistics" in NOCTURIA_INFO:
                stats = NOCTURIA_INFO["statistics"]
                st.info(f"📊 **Thống kê:** {stats.get('prevalence', '')}")
    
    with st.expander("🔍 Nguyên nhân"):
        if CAUSES:
            if "common" in CAUSES:
                common = CAUSES["common"]
                for key in ["overproduction", "storage", "other"]:
                    if key in common:
                        st.markdown(f"### {common[key]['title']}")
                        for cause in common[key]["causes"]:
                            st.markdown(f"- {cause}")
                        st.divider()
    
    with st.expander("💊 Điều trị"):
        if TREATMENT:
            if "lifestyle" in TREATMENT:
                st.markdown(f"### {TREATMENT['lifestyle']['title']}")
                lifestyle = TREATMENT["lifestyle"]
                if "fluid_management" in lifestyle:
                    st.markdown(f"**{lifestyle['fluid_management']['title']}**")
                    for tip in lifestyle["fluid_management"]["tips"]:
                        st.markdown(tip)
                
                if "sleep_hygiene" in lifestyle:
                    st.markdown(f"**{lifestyle['sleep_hygiene']['title']}**")
                    for tip in lifestyle["sleep_hygiene"]["tips"]:
                        st.markdown(f"- {tip}")
            
            if "medications" in TREATMENT:
                st.divider()
                st.markdown(f"### {TREATMENT['medications']['title']}")
                meds = TREATMENT["medications"]
                if "overactive_bladder" in meds:
                    st.markdown(f"**{meds['overactive_bladder']['title']}**")
                    for item in meds["overactive_bladder"].get("examples", []):
                        st.markdown(f"- {item}")
    
    with st.expander("🏥 Khi nào cần khám bác sĩ"):
        if TREATMENT and "when_to_see_doctor" in TREATMENT:
            doctor = TREATMENT["when_to_see_doctor"]
            col1, col2 = st.columns(2)
            with col1:
                st.warning("**📋 KHÁM SỚM:**")
                for item in doctor.get("soon", []):
                    st.markdown(f"- {item}")
            with col2:
                st.error("**🚨 KHẨN CẤP:**")
                for item in doctor.get("urgent", []):
                    st.markdown(f"- {item}")

