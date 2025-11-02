"""
Hearing Loss Tab Component
Tab Điếc/Lãng Tai
"""

import streamlit as st
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from diseases.ent import HEARING_LOSS_INFO


def render_hearing_loss_tab():
    """Tab Điếc/Lãng Tai"""
    st.header("👂 Điếc/Lãng Tai (Hearing Loss)")
    
    info = HEARING_LOSS_INFO
    
    # Thông tin cơ bản
    with st.expander("📖 Điếc/Lãng tai là gì?", expanded=True):
        st.markdown(info.get("simple_explanation", ""))
        
        if "what_happens" in info:
            st.markdown(info["what_happens"])
    
    # Triệu chứng
    with st.expander("⚠️ Triệu chứng", expanded=True):
        if "symptoms" in info:
            symptoms = info["symptoms"]
            if "common" in symptoms:
                st.markdown("**Dấu hiệu thường gặp:**")
                for symptom in symptoms["common"]:
                    st.markdown(f"- {symptom}")
            
            if "warning_signs" in symptoms:
                st.markdown("\n**⚠️ CẢNH BÁO:**")
                for sign in symptoms["warning_signs"]:
                    st.markdown(sign)
    
    # Nguyên nhân
    with st.expander("🔍 Nguyên nhân", expanded=False):
        if "causes" in info:
            causes = info["causes"]
            
            if "age_related" in causes:
                age = causes["age_related"]
                st.markdown(f"### {age.get('title', '')}")
                st.caption(age.get('description', ''))
                if "why" in age:
                    for reason in age["why"]:
                        st.markdown(f"- {reason}")
                st.divider()
            
            if "noise_induced" in causes:
                noise = causes["noise_induced"]
                st.markdown(f"### {noise.get('title', '')}")
                st.caption(noise.get('description', ''))
                if "sources" in noise:
                    for source in noise["sources"]:
                        st.markdown(f"- {source}")
                st.divider()
            
            if "sudden_hearing_loss" in causes:
                sudden = causes["sudden_hearing_loss"]
                st.error(f"### {sudden.get('title', '')}")
                st.caption(sudden.get('description', ''))
                if "causes" in sudden:
                    for cause in sudden["causes"]:
                        st.markdown(f"- {cause}")
                if "urgent" in sudden:
                    st.error(sudden["urgent"])
                st.divider()
            
            if "other" in causes:
                st.markdown("**Nguyên nhân khác:**")
                for other in causes["other"]:
                    st.markdown(f"- {other}")
    
    # Điều trị
    with st.expander("💊 Điều trị", expanded=False):
        if "treatment" in info:
            treatment = info["treatment"]
            
            if "sudden_hearing_loss" in treatment:
                sudden = treatment["sudden_hearing_loss"]
                st.error(f"### {sudden.get('title', '')}")
                if "urgency" in sudden:
                    st.error(sudden["urgency"])
                if "why_urgent" in sudden:
                    for reason in sudden["why_urgent"]:
                        st.markdown(f"- {reason}")
                if "do_not" in sudden:
                    st.markdown("\n**❌ KHÔNG NÊN:**")
                    for item in sudden["do_not"]:
                        st.markdown(item)
                st.divider()
            
            if "age_related" in treatment:
                age = treatment["age_related"]
                st.markdown(f"### {age.get('title', '')}")
                for option in age.get("options", []):
                    st.markdown(option)
                st.divider()
            
            if "noise_induced" in treatment:
                noise = treatment["noise_induced"]
                st.markdown(f"### {noise.get('title', '')}")
                if "prevention" in noise:
                    for tip in noise["prevention"]:
                        st.markdown(tip)
                st.divider()
            
            if "other" in treatment:
                other = treatment["other"]
                if "when_to_see_doctor" in other:
                    st.markdown("**Khi nào cần đi khám bác sĩ:**")
                    for item in other["when_to_see_doctor"]:
                        st.markdown(item)
    
    # Máy trợ thính
    if "hearing_aids" in info:
        with st.expander("👂 Máy trợ thính", expanded=False):
            aids = info["hearing_aids"]
            st.markdown(f"### {aids.get('title', '')}")
            if "when_needed" in aids:
                st.info(aids["when_needed"])
            if "types" in aids:
                for type_item in aids["types"]:
                    st.markdown(type_item)
            if "note" in aids:
                st.warning(aids["note"])
    
    # Phòng ngừa
    with st.expander("🛡️ Phòng ngừa", expanded=False):
        if "prevention" in info:
            prevention = info["prevention"]
            st.markdown(f"### {prevention.get('title', '')}")
            for tip in prevention.get("tips", []):
                st.markdown(tip)
    
    # Lưu ý
    if "note" in info:
        st.divider()
        st.warning(info["note"])

