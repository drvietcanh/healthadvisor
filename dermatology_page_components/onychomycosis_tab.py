"""Onychomycosis Tab Component"""
import streamlit as st
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from diseases.dermatology import ONYCHOMYCOSIS_INFO

def render_onychomycosis_tab():
    """Tab Nấm Móng"""
    st.header("💅 Nấm Móng (Onychomycosis)")
    info = ONYCHOMYCOSIS_INFO
    
    with st.expander("📖 Nấm móng là gì?", expanded=True):
        st.markdown(info.get("simple_explanation", ""))
        if "what_happens" in info:
            st.markdown(info["what_happens"])
    
    with st.expander("⚠️ Triệu chứng", expanded=False):
        if "symptoms" in info:
            s = info["symptoms"]
            if "common" in s:
                st.markdown("**Dấu hiệu thường gặp:**")
                for x in s["common"]:
                    st.markdown(f"- {x}")
            if "where_common" in s:
                st.markdown("\n**Vị trí thường gặp:**")
                for x in s["where_common"]:
                    st.markdown(x)
            if "progression" in s:
                st.markdown("\n**Diễn tiến:**")
                for x in s["progression"]:
                    st.markdown(x)
    
    with st.expander("🔍 Nguyên nhân", expanded=False):
        if "causes" in info:
            c = info["causes"]
            if "main" in c:
                for x in c["main"]:
                    st.markdown(f"- {x}")
            if "risk_factors" in c:
                st.markdown("\n**Yếu tố nguy cơ:**")
                for x in c["risk_factors"]:
                    st.markdown(x)
    
    with st.expander("💊 Điều trị", expanded=False):
        if "treatment" in info:
            t = info["treatment"]
            if "home_care" in t:
                h = t["home_care"]
                st.markdown(f"### {h.get('title', '')}")
                for x in h.get("steps", []):
                    st.markdown(x)
                if "duration" in h:
                    st.info(h["duration"])
                if "note" in h:
                    st.warning(h["note"])
            
            st.divider()
            if "when_to_see_doctor" in t:
                w = t["when_to_see_doctor"]
                st.markdown(f"### {w.get('title', '')}")
                for x in w.get("reasons", []):
                    st.markdown(x)
            
            st.divider()
            if "doctor_treatment" in t:
                d = t["doctor_treatment"]
                st.markdown(f"### {d.get('title', '')}")
                for x in d.get("options", []):
                    st.markdown(x)
                if "success_rate" in d:
                    st.markdown(f"\n### {d['success_rate']}")
                    for x in d.get("success_details", []):
                        st.markdown(x)
    
    with st.expander("🛡️ Phòng ngừa", expanded=False):
        if "prevention" in info:
            p = info["prevention"]
            st.markdown(f"### {p.get('title', '')}")
            for x in p.get("tips", []):
                st.markdown(x)
    
    if "note" in info:
        st.divider()
        st.warning(info["note"])

