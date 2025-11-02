"""Pressure Ulcer Tab Component"""
import streamlit as st
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from diseases.dermatology import PRESSURE_ULCER_INFO

def render_pressure_ulcer_tab():
    """Tab Loét Tì Đè"""
    st.header("🛏️ Loét Tì Đè (Pressure Ulcer/Bedsores)")
    info = PRESSURE_ULCER_INFO
    
    with st.expander("📖 Loét tì đè là gì?", expanded=True):
        st.markdown(info.get("simple_explanation", ""))
        if "what_happens" in info:
            st.markdown(info["what_happens"])
        if "stages" in info:
            st.markdown("\n### Phân độ loét tì đè:")
            stages = info["stages"]
            for key, stage in stages.items():
                st.markdown(f"**{stage['name']}:** {stage['description']}")
                st.info(f"Hành động: {stage['action']}")
                st.divider()
    
    with st.expander("⚠️ Triệu chứng", expanded=False):
        if "symptoms" in info:
            s = info["symptoms"]
            if "common" in s:
                st.markdown("**Dấu hiệu thường gặp:**")
                for x in s["common"]:
                    st.markdown(f"- {x}")
            if "common_locations" in s:
                st.markdown("\n**Vị trí thường gặp:**")
                for x in s["common_locations"]:
                    st.markdown(x)
            if "warning_signs" in s:
                st.markdown("\n**Dấu hiệu cảnh báo:**")
                for x in s["warning_signs"]:
                    st.markdown(x)
    
    with st.expander("🔍 Nguyên nhân", expanded=False):
        if "causes" in info:
            c = info["causes"]
            if "main" in c:
                st.markdown("**Nguyên nhân chính:**")
                for x in c["main"]:
                    st.markdown(f"- {x}")
            if "risk_factors" in c:
                st.markdown("\n**Yếu tố nguy cơ:**")
                for x in c["risk_factors"]:
                    st.markdown(x)
    
    with st.expander("💊 Điều trị", expanded=False):
        if "treatment" in info:
            t = info["treatment"]
            if "prevention_first" in t:
                p = t["prevention_first"]
                st.success(f"### {p.get('title', '')}")
                for x in p.get("steps", []):
                    st.markdown(x)
            
            st.divider()
            if "stage_2_3" in t:
                s = t["stage_2_3"]
                st.markdown(f"### {s.get('title', '')}")
                for x in s.get("steps", []):
                    st.markdown(x)
            
            st.divider()
            if "when_to_see_doctor" in t:
                w = t["when_to_see_doctor"]
                st.error(f"### {w.get('title', '')}")
                for x in w.get("reasons", []):
                    st.markdown(x)
            
            st.divider()
            if "doctor_treatment" in t:
                d = t["doctor_treatment"]
                st.markdown(f"### {d.get('title', '')}")
                for x in d.get("options", []):
                    st.markdown(x)
    
    with st.expander("🛡️ Phòng ngừa", expanded=False):
        if "prevention" in info:
            p = info["prevention"]
            st.markdown(f"### {p.get('title', '')}")
            for x in p.get("tips", []):
                st.markdown(x)
    
    if "note" in info:
        st.divider()
        st.error(info["note"])

