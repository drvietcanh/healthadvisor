"""Psoriasis Tab Component"""

import streamlit as st
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

from diseases.dermatology.psoriasis import PSORIASIS_INFO, SYMPTOMS, TREATMENT

def render_psoriasis_tab():
    """Render tab Vảy Nến"""
    st.header("🦠 Vảy Nến (Psoriasis)")
    
    st.info("💡 **Lưu ý:** Vảy nến KHÔNG LÂY NHIỄM. Không lây từ người này sang người khác.")
    
    with st.expander("📖 Vảy nến là gì?", expanded=True):
        if PSORIASIS_INFO:
            st.markdown(PSORIASIS_INFO.get("simple_explanation", ""))
            if PSORIASIS_INFO.get("why_important"):
                st.warning(PSORIASIS_INFO["why_important"])
    
    with st.expander("🔍 Triệu chứng"):
        if SYMPTOMS:
            if "skin" in SYMPTOMS:
                st.markdown(f"### {SYMPTOMS['skin']['title']}")
                st.markdown("**Biểu hiện:**")
                for s in SYMPTOMS["skin"]["appearance"]:
                    st.markdown(f"- {s}")
                st.markdown("**Vị trí hay gặp:**")
                for loc in SYMPTOMS["skin"]["locations"]:
                    st.markdown(f"- {loc}")
            
            if "joint" in SYMPTOMS:
                st.divider()
                st.error(f"### {SYMPTOMS['joint']['title']}")
                for s in SYMPTOMS["joint"]["symptoms"]:
                    st.markdown(f"**{s}**")
                if SYMPTOMS["joint"].get("warning"):
                    st.warning(SYMPTOMS["joint"]["warning"])
    
    with st.expander("💊 Điều trị"):
        if TREATMENT:
            if "topical" in TREATMENT:
                st.markdown(f"### {TREATMENT['topical']['title']}")
                topical = TREATMENT["topical"]
                if "corticosteroids" in topical:
                    st.markdown(f"**{topical['corticosteroids']['title']}**")
                    for item in topical["corticosteroids"].get("examples", []):
                        st.markdown(f"- {item}")
                    if topical["corticosteroids"].get("warning"):
                        st.warning(topical["corticosteroids"]["warning"])
            
            if "lifestyle" in TREATMENT:
                st.divider()
                st.markdown(f"### {TREATMENT['lifestyle']['title']}")
                for tip in TREATMENT["lifestyle"]["tips"]:
                    st.markdown(tip)
    
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

