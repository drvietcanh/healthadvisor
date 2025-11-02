"""IBS Tab Component"""

import streamlit as st

from diseases.digestive.ibs import IBS_INFO, SYMPTOMS, TREATMENT

def render_ibs_tab():
    """Render tab Hội Chứng Ruột Kích Thích"""
    st.header("🫀 Hội Chứng Ruột Kích Thích (IBS)")
    
    with st.expander("📖 Hội chứng ruột kích thích là gì?", expanded=True):
        if IBS_INFO:
            st.markdown(IBS_INFO.get("simple_explanation", ""))
            if IBS_INFO.get("why_important"):
                st.warning(IBS_INFO["why_important"])
    
    with st.expander("🔍 Triệu chứng"):
        if SYMPTOMS:
            if "common" in SYMPTOMS:
                common = SYMPTOMS["common"]
                if "abdominal_pain" in common:
                    st.markdown(f"### {common['abdominal_pain']['title']}")
                    for c in common["abdominal_pain"]["characteristics"]:
                        st.markdown(f"- {c}")
                
                if "bowel_changes" in common:
                    st.divider()
                    st.markdown(f"### {common['bowel_changes']['title']}")
                    for bowel_type in common["bowel_changes"]["types"]:
                        st.markdown(f"**{bowel_type['name']}**")
                        for s in bowel_type["symptoms"]:
                            st.markdown(f"- {s}")
                        st.divider()
            
            if "red_flags" in SYMPTOMS:
                st.divider()
                st.error(f"### {SYMPTOMS['red_flags']['title']}")
                for sign in SYMPTOMS["red_flags"]["signs"]:
                    st.markdown(f"**{sign}**")
                if SYMPTOMS["red_flags"].get("note"):
                    st.warning(SYMPTOMS["red_flags"]["note"])
    
    with st.expander("💊 Điều trị"):
        if TREATMENT:
            if "diet" in TREATMENT:
                st.markdown(f"### {TREATMENT['diet']['title']}")
                diet = TREATMENT["diet"]
                if "fodmap" in diet:
                    st.markdown(f"**{diet['fodmap']['title']}**")
                    st.caption(diet["fodmap"]["description"])
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("**Tránh:**")
                        for item in diet["fodmap"].get("avoid", []):
                            st.markdown(item)
                    with col2:
                        st.markdown("**Có thể ăn:**")
                        for item in diet["fodmap"].get("can_eat", []):
                            st.markdown(f"- {item}")
            
            if "stress_management" in TREATMENT:
                st.divider()
                st.markdown(f"### {TREATMENT['stress_management']['title']}")
                st.caption(f"**Lý do:** {TREATMENT['stress_management']['why']}")
                for method in TREATMENT["stress_management"]["methods"]:
                    st.markdown(method)
    
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
            if doctor.get("note"):
                st.info(doctor["note"])

