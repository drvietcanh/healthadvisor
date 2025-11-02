"""
Osteoporosis Tab - Info, Causes, Symptoms
Thông tin cơ bản, nguyên nhân, triệu chứng
"""

import streamlit as st
from diseases.bone_joint.osteoporosis import OSTEOPOROSIS_INFO, CAUSES, SYMPTOMS


def render_osteoporosis_info():
    """Render thông tin cơ bản"""
    with st.expander("📖 Loãng xương là gì?", expanded=True):
        if OSTEOPOROSIS_INFO:
            st.markdown(OSTEOPOROSIS_INFO.get("simple_explanation", ""))
            
            # Chuyện gì xảy ra
            if "what_happens" in OSTEOPOROSIS_INFO:
                what_happens = OSTEOPOROSIS_INFO["what_happens"]
                st.markdown(f"### {what_happens.get('title', '')}")
                st.markdown(what_happens.get("explanation", ""))
            
            st.divider()
            
            # Phổ biến
            if "prevalence" in OSTEOPOROSIS_INFO:
                st.markdown("### 📊 Phổ biến ở Việt Nam:")
                prevalence = OSTEOPOROSIS_INFO["prevalence"]
                st.markdown(f"- **Tổng dân số:** {prevalence.get('vietnam', '')}")
                st.markdown(f"- **Phụ nữ sau 50 tuổi:** {prevalence.get('women_50', '')}")
                st.markdown(f"- **Nam giới sau 60 tuổi:** {prevalence.get('men_50', '')}")
            
            # Vị trí thường gãy
            if "common_sites" in OSTEOPOROSIS_INFO:
                st.markdown("### 🔍 Vị trí thường gãy:")
                for site in OSTEOPOROSIS_INFO["common_sites"]:
                    st.markdown(f"- {site}")
            
            # Hậu quả
            if "impact" in OSTEOPOROSIS_INFO:
                impact = OSTEOPOROSIS_INFO["impact"]
                st.markdown(f"### {impact.get('title', '')}")
                for item in impact.get("items", []):
                    st.markdown(f"- {item}")


def render_osteoporosis_causes():
    """Render nguyên nhân"""
    with st.expander("🔍 Nguyên nhân", expanded=False):
        if CAUSES:
            # Không tránh được
            if "unavoidable" in CAUSES:
                unavoidable = CAUSES["unavoidable"]
                st.markdown(f"### {unavoidable.get('title', '')}")
                for factor in unavoidable.get("factors", []):
                    if isinstance(factor, dict):
                        st.markdown(f"**{factor.get('name', '')}:** {factor.get('description', '')}")
                    else:
                        st.markdown(f"- {factor}")
            
            st.divider()
            
            # Có thể thay đổi
            if "modifiable" in CAUSES:
                modifiable = CAUSES["modifiable"]
                st.markdown(f"### {modifiable.get('title', '')}")
                for factor in modifiable.get("factors", []):
                    if isinstance(factor, dict):
                        st.markdown(f"**{factor.get('name', '')}:** {factor.get('description', '')}")
                    else:
                        st.markdown(f"- {factor}")


def render_osteoporosis_symptoms():
    """Render triệu chứng"""
    with st.expander("⚠️ Triệu chứng", expanded=False):
        if SYMPTOMS:
            # Giai đoạn sớm
            if "early_stage" in SYMPTOMS:
                early = SYMPTOMS["early_stage"]
                st.markdown(f"### {early.get('title', '')}")
                st.markdown(f"**{early.get('description', '')}**")
                if early.get("note"):
                    st.info(early["note"])
            
            st.divider()
            
            # Giai đoạn muộn
            if "advanced_stage" in SYMPTOMS:
                advanced = SYMPTOMS["advanced_stage"]
                st.markdown(f"### {advanced.get('title', '')}")
                for symptom in advanced.get("symptoms", []):
                    if isinstance(symptom, dict):
                        st.markdown(f"**{symptom.get('name', '')}:**")
                        st.markdown(f"  {symptom.get('description', '')}")
                        if symptom.get("location"):
                            st.caption(f"📍 {symptom['location']}")
                        if symptom.get("example"):
                            st.caption(f"💡 {symptom['example']}")
                        if symptom.get("common_sites"):
                            st.markdown("Vị trí thường gãy:")
                            for site in symptom["common_sites"]:
                                st.markdown(f"  - {site}")
            
            # Cảnh báo gãy xương
            if "fracture_warning" in SYMPTOMS:
                warning = SYMPTOMS["fracture_warning"]
                st.warning(f"### {warning.get('title', '')}")
                for sign in warning.get("signs", []):
                    st.markdown(f"- {sign}")
                if warning.get("action"):
                    st.error(f"**{warning['action']}**")
            
            # Khi nào nên đi khám
            if "when_to_see_doctor" in SYMPTOMS:
                when_to_see = SYMPTOMS["when_to_see_doctor"]
                st.markdown(f"### {when_to_see.get('title', '')}")
                for indicator in when_to_see.get("indicators", []):
                    st.markdown(f"- {indicator}")

