"""Gastritis Tab Component"""

import streamlit as st
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

from diseases.digestive.gastritis import GASTRITIS_INFO, SYMPTOMS, TREATMENT

def render_gastritis_tab():
    """Render tab Viêm Dạ Dày"""
    st.header("🔥 Viêm Dạ Dày (Gastritis)")
    
    with st.expander("📖 Viêm dạ dày là gì?", expanded=True):
        if GASTRITIS_INFO:
            st.markdown(GASTRITIS_INFO.get("simple_explanation", ""))
            if "types" in GASTRITIS_INFO:
                col1, col2 = st.columns(2)
                with col1:
                    acute = GASTRITIS_INFO["types"]["acute"]
                    st.info(f"**{acute['name']}:** {acute['duration']}\n\n{', '.join(acute['causes'])}")
                with col2:
                    chronic = GASTRITIS_INFO["types"]["chronic"]
                    st.warning(f"**{chronic['name']}:** {chronic['duration']}\n\n{', '.join(chronic['causes'])}")
    
    with st.expander("🔍 Triệu chứng"):
        if SYMPTOMS:
            if "common" in SYMPTOMS:
                st.markdown(f"### {SYMPTOMS['common']['title']}")
                for s in SYMPTOMS["common"]["symptoms"]:
                    st.markdown(f"- {s}")
            if "severe" in SYMPTOMS:
                st.divider()
                st.error(f"### {SYMPTOMS['severe']['title']}")
                for s in SYMPTOMS["severe"]["symptoms"]:
                    st.markdown(f"**{s}**")
                if SYMPTOMS["severe"].get("warning"):
                    st.warning(SYMPTOMS["severe"]["warning"])
    
    with st.expander("💊 Điều trị"):
        if TREATMENT:
            if "medications" in TREATMENT:
                meds = TREATMENT["medications"]
                for key in ["antacids", "h2_blockers", "ppi", "antibiotics", "protection"]:
                    if key in meds:
                        st.markdown(f"### {meds[key]['title']}")
                        for item in meds[key].get("examples", []):
                            st.markdown(f"- {item}")
                        if meds[key].get("note"):
                            st.caption(f"💡 {meds[key]['note']}")
                        st.divider()
            
            if "lifestyle" in TREATMENT:
                st.markdown(f"### {TREATMENT['lifestyle']['title']}")
                if "diet" in TREATMENT["lifestyle"]:
                    diet = TREATMENT["lifestyle"]["diet"]
                    st.markdown(f"**{diet['title']}**")
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("**Tránh:**")
                        for item in diet.get("avoid", []):
                            st.markdown(item)
                    with col2:
                        st.markdown("**Nên ăn:**")
                        for item in diet.get("recommend", []):
                            st.markdown(item)
    
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

