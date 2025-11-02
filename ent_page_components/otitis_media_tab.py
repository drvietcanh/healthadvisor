"""
Otitis Media Tab Component
Tab Viêm Tai Giữa
"""

import streamlit as st
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from diseases.ent import OTITIS_MEDIA_INFO


def render_otitis_media_tab():
    """Tab Viêm Tai Giữa"""
    st.header("🦻 Viêm Tai Giữa (Otitis Media)")
    
    info = OTITIS_MEDIA_INFO
    
    # Thông tin cơ bản
    with st.expander("📖 Viêm tai giữa là gì?", expanded=True):
        st.markdown(info.get("simple_explanation", ""))
        
        if "what_happens" in info:
            st.markdown(info["what_happens"])
    
    # Triệu chứng
    with st.expander("⚠️ Triệu chứng", expanded=True):
        if "symptoms" in info:
            symptoms = info["symptoms"]
            
            if "acute" in symptoms:
                st.markdown("**Viêm tai giữa cấp:**")
                for symptom in symptoms["acute"]:
                    st.markdown(f"- {symptom}")
            
            if "chronic" in symptoms:
                st.markdown("\n**Viêm tai giữa mạn:**")
                for symptom in symptoms["chronic"]:
                    st.markdown(f"- {symptom}")
            
            if "in_children" in symptoms:
                st.markdown("\n")
                for item in symptoms["in_children"]:
                    st.markdown(item)
    
    # Nguyên nhân
    with st.expander("🔍 Nguyên nhân", expanded=False):
        if "causes" in info:
            causes = info["causes"]
            
            if "main" in causes:
                for cause in causes["main"]:
                    st.markdown(cause)
            
            if "chronic" in causes:
                st.markdown("\n**Nguyên nhân chuyển mạn:**")
                for cause in causes["chronic"]:
                    st.markdown(f"- {cause}")
    
    # Điều trị
    with st.expander("💊 Điều trị", expanded=False):
        if "treatment" in info:
            treatment = info["treatment"]
            
            if "acute" in treatment:
                acute = treatment["acute"]
                st.markdown(f"### {acute.get('title', '')}")
                
                if "medications" in acute:
                    for med in acute["medications"]:
                        st.markdown(med)
                
                if "when_to_see_doctor" in acute:
                    st.markdown("\n**Khi nào cần đi khám:**")
                    for item in acute["when_to_see_doctor"]:
                        st.markdown(item)
                st.divider()
            
            if "chronic" in treatment:
                chronic = treatment["chronic"]
                st.markdown(f"### {chronic.get('title', '')}")
                
                if "treatment" in chronic:
                    for item in chronic["treatment"]:
                        st.markdown(item)
                st.divider()
            
            if "complications" in treatment:
                comp = treatment["complications"]
                st.error(f"### {comp.get('title', '')}")
                
                if "list" in comp:
                    for item in comp["list"]:
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

