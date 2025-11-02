"""Pruritus Tab Component"""
import streamlit as st
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from diseases.dermatology import PRURITUS_INFO

def render_pruritus_tab():
    """Tab Ngứa Da"""
    st.header("🔴 Ngứa Da (Pruritus)")
    info = PRURITUS_INFO
    
    with st.expander("📖 Ngứa da là gì?", expanded=True):
        st.markdown(info.get("simple_explanation", ""))
        if "what_happens" in info:
            w = info["what_happens"]
            if "with_skin_lesion" in w:
                st.markdown(f"**{w['with_skin_lesion']}**")
            if "without_skin_lesion" in w:
                st.error(f"**{w['without_skin_lesion']}**")
    
    with st.expander("⚠️ Triệu chứng", expanded=False):
        if "symptoms" in info:
            s = info["symptoms"]
            if "common" in s:
                st.markdown("**Dấu hiệu thường gặp:**")
                for x in s["common"]:
                    st.markdown(f"- {x}")
            if "when_concerning" in s:
                st.markdown("\n**Khi nào đáng lo ngại:**")
                for x in s["when_concerning"]:
                    st.markdown(x)
    
    with st.expander("🔍 Nguyên nhân", expanded=False):
        if "causes" in info:
            c = info["causes"]
            if "skin_related" in c:
                st.markdown(f"### {c['skin_related']['title']}")
                for x in c["skin_related"]["items"]:
                    st.markdown(f"- {x}")
            st.divider()
            if "internal_diseases" in c:
                st.markdown(f"### {c['internal_diseases']['title']}")
                for x in c["internal_diseases"]["items"]:
                    st.markdown(x)
            st.divider()
            if "other" in c:
                st.markdown(f"### {c['other']['title']}")
                for x in c["other"]["items"]:
                    st.markdown(f"- {x}")
    
    with st.expander("💊 Điều trị", expanded=False):
        if "treatment" in info:
            t = info["treatment"]
            if "home_care" in t:
                h = t["home_care"]
                st.markdown(f"### {h.get('title', '')}")
                for x in h.get("steps", []):
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
                if "investigation" in d:
                    for x in d["investigation"]:
                        st.markdown(x)
                st.divider()
                if "specific_treatment" in d:
                    for x in d["specific_treatment"]:
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

