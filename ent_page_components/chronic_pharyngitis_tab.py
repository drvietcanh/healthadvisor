"""
Chronic Pharyngitis Tab Component
Tab Viêm Họng Mạn Tính
"""

import streamlit as st
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from diseases.ent import CHRONIC_PHARYNGITIS_INFO


def render_chronic_pharyngitis_tab():
    """Tab Viêm Họng Mạn Tính"""
    st.header("🫁 Viêm Họng Mạn Tính (Chronic Pharyngitis)")
    
    info = CHRONIC_PHARYNGITIS_INFO
    
    # Thông tin cơ bản
    with st.expander("📖 Viêm họng mạn tính là gì?", expanded=True):
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
            
            if "appearance" in symptoms:
                st.markdown("\n**Nhìn thấy gì trong họng:**")
                for appear in symptoms["appearance"]:
                    st.markdown(appear)
    
    # Nguyên nhân
    with st.expander("🔍 Nguyên nhân", expanded=False):
        if "causes" in info:
            causes = info["causes"]
            
            if "main" in causes:
                for cause in causes["main"]:
                    st.markdown(cause)
            
            if "other" in causes:
                st.markdown("\n**Nguyên nhân khác:**")
                for other in causes["other"]:
                    st.markdown(f"- {other}")
    
    # Điều trị
    with st.expander("💊 Điều trị", expanded=False):
        if "treatment" in info:
            treatment = info["treatment"]
            
            if "lifestyle" in treatment:
                lifestyle = treatment["lifestyle"]
                st.markdown(f"### {lifestyle.get('title', '')}")
                
                for key in ["stop_smoking", "reduce_alcohol", "manage_reflux", "humidify", "gargle"]:
                    if key in lifestyle:
                        for item in lifestyle[key]:
                            st.markdown(item)
                        st.divider()
            
            if "medications" in treatment:
                meds = treatment["medications"]
                st.markdown(f"### {meds.get('title', '')}")
                
                if "anti_inflammatory" in meds:
                    for item in meds["anti_inflammatory"]:
                        st.markdown(item)
                
                if "antibiotics" in meds:
                    for item in meds["antibiotics"]:
                        st.markdown(item)
                
                if "when_to_see_doctor" in meds:
                    st.markdown("\n**Khi nào cần đi khám:**")
                    for item in meds["when_to_see_doctor"]:
                        st.markdown(item)
            
            if "doctor_treatment" in treatment:
                st.divider()
                doctor = treatment["doctor_treatment"]
                st.markdown(f"### {doctor.get('title', '')}")
                
                if "examination" in doctor:
                    for exam in doctor["examination"]:
                        st.markdown(exam)
                
                if "procedures" in doctor:
                    for proc in doctor["procedures"]:
                        st.markdown(proc)
                
                if "referral" in doctor:
                    for ref in doctor["referral"]:
                        st.markdown(ref)
    
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

