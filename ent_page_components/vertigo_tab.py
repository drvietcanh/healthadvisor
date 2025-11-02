"""
Vertigo Tab Component
Tab Chóng Mặt/Vertigo
"""

import streamlit as st
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from diseases.ent import VERTIGO_INFO


def render_vertigo_tab():
    """Tab Chóng Mặt/Vertigo"""
    st.header("🌀 Chóng Mặt/Vertigo")
    
    info = VERTIGO_INFO
    
    # Thông tin cơ bản
    with st.expander("📖 Chóng mặt là gì?", expanded=True):
        st.markdown(info.get("simple_explanation", ""))
        
        if "what_happens" in info:
            st.markdown(info["what_happens"])
    
    # Triệu chứng
    with st.expander("⚠️ Triệu chứng", expanded=True):
        if "symptoms" in info:
            symptoms = info["symptoms"]
            
            if "vertigo" in symptoms:
                st.markdown("**Chóng mặt (Vertigo):**")
                for symptom in symptoms["vertigo"]:
                    st.markdown(f"- {symptom}")
            
            if "dizziness" in symptoms:
                st.markdown("\n**Choáng váng (Dizziness):**")
                for symptom in symptoms["dizziness"]:
                    st.markdown(f"- {symptom}")
            
            if "when_occurs" in symptoms:
                st.markdown("\n**Khi nào xảy ra:**")
                for when in symptoms["when_occurs"]:
                    st.markdown(f"- {when}")
    
    # Nguyên nhân
    with st.expander("🔍 Nguyên nhân", expanded=False):
        if "causes" in info:
            causes = info["causes"]
            
            if "bppv" in causes:
                bppv = causes["bppv"]
                st.markdown(f"### {bppv.get('title', '')}")
                st.caption(bppv.get('description', ''))
                if "why" in bppv:
                    for reason in bppv["why"]:
                        st.markdown(f"- {reason}")
                st.divider()
            
            if "vestibular_neuronitis" in causes:
                vn = causes["vestibular_neuronitis"]
                st.markdown(f"### {vn.get('title', '')}")
                st.caption(vn.get('description', ''))
                if "why" in vn:
                    for reason in vn["why"]:
                        st.markdown(f"- {reason}")
                st.divider()
            
            if "meniere" in causes:
                meniere = causes["meniere"]
                st.markdown(f"### {meniere.get('title', '')}")
                st.caption(meniere.get('description', ''))
                if "why" in meniere:
                    for reason in meniere["why"]:
                        st.markdown(f"- {reason}")
                st.divider()
            
            if "other" in causes:
                st.markdown("**Nguyên nhân khác:**")
                for other in causes["other"]:
                    st.markdown(f"- {other}")
    
    # Điều trị
    with st.expander("💊 Điều trị", expanded=False):
        if "treatment" in info:
            treatment = info["treatment"]
            
            if "bppv" in treatment:
                bppv = treatment["bppv"]
                st.markdown(f"### {bppv.get('title', '')}")
                for item in bppv.get("maneuver", []):
                    st.markdown(item)
                if "medications" in bppv:
                    st.markdown("\n")
                    for med in bppv["medications"]:
                        st.markdown(med)
                st.divider()
            
            if "vestibular_neuronitis" in treatment:
                vn = treatment["vestibular_neuronitis"]
                st.markdown(f"### {vn.get('title', '')}")
                for item in vn.get("treatment", []):
                    st.markdown(item)
                st.divider()
            
            if "meniere" in treatment:
                meniere = treatment["meniere"]
                st.markdown(f"### {meniere.get('title', '')}")
                for item in meniere.get("treatment", []):
                    st.markdown(item)
                st.divider()
            
            if "when_to_see_doctor" in treatment:
                when = treatment["when_to_see_doctor"]
                st.markdown("**Khi nào cần đi khám:**")
                
                if "urgent" in when:
                    st.error("**🚨 Cấp cứu ngay:**")
                    for item in when["urgent"]:
                        st.markdown(item)
                
                if "soon" in when:
                    st.warning("**Khám trong vài ngày:**")
                    for item in when["soon"]:
                        st.markdown(item)
    
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

