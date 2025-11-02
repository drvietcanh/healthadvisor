"""Parkinson Tab Component"""

import streamlit as st
from diseases.neurological.parkinson import PARKINSON_INFO, SYMPTOMS, TREATMENT

def render_parkinson_tab():
    """Render tab Bệnh Parkinson"""
    st.header("🧠 Bệnh Parkinson")
    
    with st.expander("📖 Bệnh Parkinson là gì?", expanded=True):
        if PARKINSON_INFO:
            st.markdown(PARKINSON_INFO.get("simple_explanation", ""))
            if PARKINSON_INFO.get("why_important"):
                st.warning(PARKINSON_INFO["why_important"])
            if "statistics" in PARKINSON_INFO:
                stats = PARKINSON_INFO["statistics"]
                st.info(f"📊 **Thống kê:** {stats.get('prevalence', '')}")
    
    with st.expander("🔍 Triệu chứng"):
        if SYMPTOMS:
            if "early" in SYMPTOMS:
                st.markdown(f"### {SYMPTOMS['early']['title']}")
                for s in SYMPTOMS["early"]["symptoms"]:
                    st.markdown(f"- {s}")
                if SYMPTOMS["early"].get("note"):
                    st.info(SYMPTOMS["early"]["note"])
            
            if "classic" in SYMPTOMS:
                st.divider()
                st.markdown(f"### {SYMPTOMS['classic']['title']}")
                classic = SYMPTOMS["classic"]
                for key in ["tremor", "rigidity", "bradykinesia", "postural"]:
                    if key in classic:
                        st.markdown(f"**{classic[key]['name']}**")
                        for c in classic[key]["characteristics"]:
                            st.markdown(f"- {c}")
                        if classic[key].get("note"):
                            st.warning(classic[key]["note"])
                        st.divider()
    
    with st.expander("💊 Điều trị"):
        if TREATMENT:
            if "medications" in TREATMENT:
                meds = TREATMENT["medications"]
                if "levodopa" in meds:
                    st.markdown(f"### {meds['levodopa']['title']}")
                    st.caption(f"**Cách hoạt động:** {meds['levodopa']['how_it_works']}")
                    for item in meds["levodopa"].get("examples", []):
                        st.markdown(f"- {item}")
                    st.caption(f"**Liều:** {meds['levodopa'].get('dosing', '')}")
                    if meds["levodopa"].get("important"):
                        st.warning(meds["levodopa"]["important"])
                
                if "important_notes" in meds:
                    st.divider()
                    st.markdown(f"### {meds['important_notes']['title']}")
                    for rule in meds["important_notes"].get("rules", []):
                        st.markdown(rule)
            
            if "lifestyle" in TREATMENT:
                st.divider()
                st.markdown(f"### {TREATMENT['lifestyle']['title']}")
                lifestyle = TREATMENT["lifestyle"]
                if "exercise" in lifestyle:
                    st.markdown(f"**{lifestyle['exercise']['title']}**")
                    st.markdown("**Lợi ích:**")
                    for benefit in lifestyle["exercise"].get("benefits", []):
                        st.markdown(benefit)
                    st.markdown("**Khuyến nghị:**")
                    for rec in lifestyle["exercise"].get("recommended", []):
                        st.markdown(f"- {rec}")
    
    with st.expander("🏥 Khi nào cần khám bác sĩ"):
        if SYMPTOMS and "when_to_see_doctor" in SYMPTOMS:
            doctor = SYMPTOMS["when_to_see_doctor"]
            st.error("**🚨 KHẨN CẤP:**")
            for item in doctor.get("urgent", []):
                st.markdown(f"- {item}")
            if doctor.get("note"):
                st.info(doctor["note"])

