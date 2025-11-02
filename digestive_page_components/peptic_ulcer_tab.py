"""Peptic Ulcer Tab Component"""

import streamlit as st
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

from diseases.digestive.peptic_ulcer import PEPTIC_ULCER_INFO, SYMPTOMS, TREATMENT

def render_peptic_ulcer_tab():
    """Render tab Loét Dạ Dày"""
    st.header("🩸 Loét Dạ Dày (Peptic Ulcer)")
    
    with st.expander("📖 Loét dạ dày là gì?", expanded=True):
        if PEPTIC_ULCER_INFO:
            st.markdown(PEPTIC_ULCER_INFO.get("simple_explanation", ""))
    
    with st.expander("🔍 Triệu chứng"):
        if SYMPTOMS:
            if "pain" in SYMPTOMS:
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"### {SYMPTOMS['pain']['gastric_ulcer']['title']}")
                    for s in SYMPTOMS["pain"]["gastric_ulcer"]["characteristics"]:
                        st.markdown(f"- {s}")
                with col2:
                    st.markdown(f"### {SYMPTOMS['pain']['duodenal_ulcer']['title']}")
                    for s in SYMPTOMS["pain"]["duodenal_ulcer"]["characteristics"]:
                        st.markdown(f"- {s}")
            
            if "complications" in SYMPTOMS:
                st.divider()
                st.error("### ⚠️ Biến chứng nguy hiểm:")
                for comp_key in ["bleeding", "perforation"]:
                    if comp_key in SYMPTOMS["complications"]:
                        comp = SYMPTOMS["complications"][comp_key]
                        st.markdown(f"**{comp['title']}**")
                        for s in comp["symptoms"]:
                            st.markdown(f"**{s}**")
                        if comp.get("warning"):
                            st.warning(comp["warning"])
                        st.divider()
    
    with st.expander("💊 Điều trị"):
        if TREATMENT:
            if "medications" in TREATMENT:
                meds = TREATMENT["medications"]
                if "ppi" in meds:
                    st.markdown(f"### {meds['ppi']['title']}")
                    for item in meds["ppi"].get("examples", []):
                        st.markdown(f"- {item}")
                    st.divider()
                
                if "h_pylori" in meds:
                    st.markdown(f"### {meds['h_pylori']['title']}")
                    st.caption(meds["h_pylori"].get("protocol", ""))
                    for item in meds["h_pylori"].get("examples", []):
                        st.markdown(f"- {item}")
                    if meds["h_pylori"].get("note"):
                        st.warning(meds["h_pylori"]["note"])
                    st.divider()
                
                if "stop_nsaids" in meds:
                    st.markdown(f"### {meds['stop_nsaids']['title']}")
                    st.error(meds["stop_nsaids"].get("warning", ""))
                    st.caption(meds["stop_nsaids"].get("alternative", ""))
    
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

