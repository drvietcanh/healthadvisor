"""BPH Tab Component"""

import streamlit as st
from diseases.renal.bph import BPH_INFO, SYMPTOMS, TREATMENT

def render_bph_tab():
    """Render tab Phì Đại Tuyến Tiền Liệt"""
    st.header("🫀 Phì Đại Tuyến Tiền Liệt (BPH)")
    
    st.info("⚠️ **Lưu ý:** Chỉ xảy ra ở NAM GIỚI. Phụ nữ không có tuyến tiền liệt.")
    
    with st.expander("📖 Phì đại tuyến tiền liệt là gì?", expanded=True):
        if BPH_INFO:
            st.markdown(BPH_INFO.get("simple_explanation", ""))
            if BPH_INFO.get("why_important"):
                st.warning(BPH_INFO["why_important"])
            if "statistics" in BPH_INFO:
                stats = BPH_INFO["statistics"]
                st.info(f"📊 **Thống kê:** {stats.get('prevalence', '')}")
    
    with st.expander("🔍 Triệu chứng"):
        if SYMPTOMS:
            if "obstructive" in SYMPTOMS:
                st.markdown(f"### {SYMPTOMS['obstructive']['title']}")
                for s in SYMPTOMS["obstructive"]["symptoms"]:
                    st.markdown(f"- {s}")
            
            if "irritative" in SYMPTOMS:
                st.divider()
                st.markdown(f"### {SYMPTOMS['irritative']['title']}")
                for s in SYMPTOMS["irritative"]["symptoms"]:
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
                if "alpha_blockers" in meds:
                    st.markdown(f"### {meds['alpha_blockers']['title']}")
                    st.caption(f"**Cách hoạt động:** {meds['alpha_blockers']['how_it_works']}")
                    for item in meds["alpha_blockers"].get("examples", []):
                        st.markdown(f"- {item}")
                    st.markdown("**Lợi ích:**")
                    for benefit in meds["alpha_blockers"].get("benefits", []):
                        st.markdown(benefit)
                    if meds["alpha_blockers"].get("note"):
                        st.warning(meds["alpha_blockers"]["note"])
                
                if "5_alpha_reductase" in meds:
                    st.divider()
                    st.markdown(f"### {meds['5_alpha_reductase']['title']}")
                    for item in meds["5_alpha_reductase"].get("examples", []):
                        st.markdown(f"- {item}")
                    if meds["5_alpha_reductase"].get("note"):
                        st.warning(meds["5_alpha_reductase"]["note"])
            
            if "lifestyle" in TREATMENT:
                st.divider()
                st.markdown(f"### {TREATMENT['lifestyle']['title']}")
                for tip in TREATMENT["lifestyle"]["tips"]:
                    st.markdown(tip)
    
    with st.expander("🏥 Khi nào cần khám bác sĩ"):
        if SYMPTOMS and "when_to_see_doctor" in SYMPTOMS:
            doctor = SYMPTOMS["when_to_see_doctor"]
            col1, col2 = st.columns(2)
            with col1:
                st.warning("**📋 KHÁM SỚM:**")
                for item in doctor.get("soon", []):
                    st.markdown(f"- {item}")
            with col2:
                st.error("**🚨 KHẨN CẤP:**")
                for item in doctor.get("urgent", []):
                    st.markdown(f"- {item}")

