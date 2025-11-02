"""Diarrhea Tab Component"""

import streamlit as st
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

from diseases.digestive.diarrhea import DIARRHEA_INFO, SYMPTOMS, TREATMENT

def render_diarrhea_tab():
    """Render tab Tiêu Chảy Cấp"""
    st.header("💧 Tiêu Chảy Cấp (Acute Diarrhea)")
    
    with st.expander("📖 Tiêu chảy cấp là gì?", expanded=True):
        if DIARRHEA_INFO:
            st.markdown(DIARRHEA_INFO.get("simple_explanation", ""))
    
    with st.expander("🔍 Triệu chứng"):
        if SYMPTOMS:
            if "common" in SYMPTOMS:
                st.markdown(f"### {SYMPTOMS['common']['title']}")
                for s in SYMPTOMS["common"]["symptoms"]:
                    st.markdown(f"- {s}")
            
            if "dehydration" in SYMPTOMS:
                st.divider()
                dehyd = SYMPTOMS["dehydration"]
                if "severe" in dehyd:
                    st.error(f"### {dehyd['severe']['title']}")
                    for s in dehyd["severe"]["signs"]:
                        st.markdown(f"**{s}**")
                    if dehyd["severe"].get("warning"):
                        st.warning(dehyd["severe"]["warning"])
    
    with st.expander("💊 Điều trị"):
        if TREATMENT:
            if "hydration" in TREATMENT:
                st.markdown(f"### {TREATMENT['hydration']['title']}")
                st.caption(f"Lượng: {TREATMENT['hydration'].get('amount', '')}")
                st.markdown("**Nên uống:**")
                for item in TREATMENT["hydration"]["what_to_drink"].get("recommended", []):
                    st.markdown(item)
                if TREATMENT["hydration"].get("warning"):
                    st.warning(TREATMENT["hydration"]["warning"])
                st.divider()
            
            if "diet" in TREATMENT:
                st.markdown(f"### {TREATMENT['diet']['title']}")
                if "when_acute" in TREATMENT["diet"]:
                    st.markdown(f"**{TREATMENT['diet']['when_acute']['title']}**")
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("**Nên ăn:**")
                        for item in TREATMENT["diet"]["when_acute"].get("foods", []):
                            st.markdown(f"- {item}")
                    with col2:
                        st.markdown("**Tránh:**")
                        for item in TREATMENT["diet"]["when_acute"].get("avoid", []):
                            st.markdown(item)
    
    with st.expander("✅ Phòng ngừa"):
        if TREATMENT and "prevention" in TREATMENT:
            prev = TREATMENT["prevention"]
            if "hygiene" in prev:
                st.markdown(f"**{prev['hygiene']['title']}**")
                for tip in prev["hygiene"]["tips"]:
                    st.markdown(f"- {tip}")
            if "food_safety" in prev:
                st.markdown(f"**{prev['food_safety']['title']}**")
                for tip in prev["food_safety"]["tips"]:
                    st.markdown(f"- {tip}")
    
    with st.expander("🏥 Khi nào cần khám bác sĩ"):
        if TREATMENT and "when_to_see_doctor" in TREATMENT:
            doctor = TREATMENT["when_to_see_doctor"]
            col1, col2 = st.columns(2)
            with col1:
                st.error("**🚨 KHẨN CẤP:**")
                for item in doctor.get("urgent", []):
                    st.markdown(f"- {item}")
            with col2:
                st.warning("**📋 SỚM:**")
                for item in doctor.get("soon", []):
                    st.markdown(f"- {item}")

