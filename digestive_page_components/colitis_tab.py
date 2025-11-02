"""Colitis Tab Component"""

import streamlit as st

from diseases.digestive.colitis import COLITIS_INFO, SYMPTOMS, TREATMENT

def render_colitis_tab():
    """Render tab Viêm Đại Tràng"""
    st.header("🫀 Viêm Đại Tràng (Colitis)")
    
    with st.expander("📖 Viêm đại tràng là gì?", expanded=True):
        if COLITIS_INFO:
            st.markdown(COLITIS_INFO.get("simple_explanation", ""))
            if "types" in COLITIS_INFO:
                for type_key in ["infectious", "ibd", "ischemic"]:
                    if type_key in COLITIS_INFO["types"]:
                        t = COLITIS_INFO["types"][type_key]
                        st.info(f"**{t['name']}:** {t.get('cause', '')} - {t.get('severity', '')}")
    
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
    
    with st.expander("💊 Điều trị"):
        if TREATMENT:
            if "ibd_colitis" in TREATMENT:
                st.markdown(f"### {TREATMENT['ibd_colitis']['title']}")
                for severity in ["mild", "moderate", "severe"]:
                    if severity in TREATMENT["ibd_colitis"]["medications"]:
                        meds = TREATMENT["ibd_colitis"]["medications"][severity]
                        st.markdown(f"**{meds['title']}**")
                        for item in meds.get("meds", []):
                            st.markdown(f"- {item}")
                        st.divider()
    
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

