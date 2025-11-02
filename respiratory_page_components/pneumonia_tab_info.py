"""
Pneumonia Tab - Info, Causes, Symptoms
Thông tin cơ bản, nguyên nhân, triệu chứng
"""

import streamlit as st
from diseases.respiratory import pneumonia


def render_pneumonia_info():
    """Render thông tin cơ bản"""
    with st.expander("📖 Viêm phổi là gì?", expanded=True):
        if hasattr(pneumonia, 'PNEUMONIA_INFO') and pneumonia.PNEUMONIA_INFO:
            info_dict = pneumonia.PNEUMONIA_INFO
            if isinstance(info_dict, dict):
                st.markdown(info_dict.get("simple_explanation", ""))
                if info_dict.get("why_dangerous"):
                    st.warning(info_dict.get("why_dangerous"))


def render_pneumonia_causes():
    """Render nguyên nhân"""
    with st.expander("🔍 Nguyên nhân viêm phổi"):
        if hasattr(pneumonia, 'CAUSES') and pneumonia.CAUSES:
            causes = pneumonia.CAUSES
            if isinstance(causes, dict):
                # Vi khuẩn
                if "bacteria" in causes:
                    bacteria = causes["bacteria"]
                    st.markdown(f"### {bacteria.get('name', 'Vi khuẩn')}")
                    st.caption(bacteria.get('description', ''))
                    if "common" in bacteria:
                        for b in bacteria["common"][:2]:
                            st.markdown(f"**{b.get('name', '')}**")
                            st.caption(b.get('description', ''))
                            if b.get('prevention'):
                                st.success(f"💡 {b['prevention']}")
                    st.divider()
                
                # Virus
                if "viruses" in causes:
                    viruses = causes["viruses"]
                    st.markdown(f"### {viruses.get('name', 'Virus')}")
                    st.caption(viruses.get('description', ''))
                    if "common" in viruses:
                        for v in viruses["common"][:3]:
                            st.markdown(f"**{v.get('name', '')}**")
                            st.caption(v.get('description', ''))
                            if v.get('prevention'):
                                st.success(f"💡 {v['prevention']}")
                            if v.get('warning'):
                                st.warning(v['warning'])
                    st.divider()
                
                # Yếu tố nguy cơ
                if "risk_factors" in causes:
                    risks = causes["risk_factors"]
                    st.markdown(f"### {risks.get('name', 'Yếu tố nguy cơ')}")
                    st.caption(risks.get('description', ''))
                    for key in ["age", "chronic_diseases", "lifestyle"]:
                        if key in risks:
                            risk_item = risks[key]
                            st.markdown(f"**{risk_item.get('name', key)}**")
                            if "diseases" in risk_item:
                                for d in risk_item["diseases"][:3]:
                                    st.markdown(f"- {d}")
                            elif "factors" in risk_item:
                                for f in risk_item["factors"][:3]:
                                    st.markdown(f"- {f}")
                            elif "reason" in risk_item:
                                st.caption(risk_item["reason"])


def render_pneumonia_symptoms():
    """Render triệu chứng"""
    with st.expander("🩺 Triệu chứng viêm phổi", expanded=True):
        if hasattr(pneumonia, 'SYMPTOMS') and pneumonia.SYMPTOMS:
            symptoms_dict = pneumonia.SYMPTOMS
            
            # Triệu chứng chính
            if "main_symptoms" in symptoms_dict:
                main = symptoms_dict["main_symptoms"]
                st.subheader(f"{main.get('title', '🔍 Triệu Chứng Chính')}")
                if "symptoms" in main:
                    for symptom in main["symptoms"]:
                        if isinstance(symptom, dict):
                            st.markdown(f"### {symptom.get('icon', '')} {symptom.get('name', '')}")
                            st.caption(symptom.get('description', ''))
                            if "details" in symptom:
                                for detail in symptom["details"]:
                                    st.markdown(f"- {detail}")
                            st.divider()
            
            # Triệu chứng nặng
            if "severe_symptoms" in symptoms_dict:
                severe = symptoms_dict["severe_symptoms"]
                st.error(f"### {severe.get('title', '🚨 Triệu Chứng Nặng')}")
                st.warning(severe.get('warning', ''))
                if "symptoms" in severe:
                    for symptom in severe["symptoms"]:
                        if isinstance(symptom, dict):
                            st.markdown(f"**{symptom.get('name', '')}**")
                            if "signs" in symptom:
                                for sign in symptom["signs"]:
                                    st.markdown(f"- {sign}")
                            st.divider()
            
            # Triệu chứng ở người già
            if "elderly_symptoms" in symptoms_dict:
                elderly = symptoms_dict["elderly_symptoms"]
                st.warning(f"### {elderly.get('title', '👴 Triệu Chứng Ở Người Già')}")
                st.error(elderly.get('warning', ''))
                if "common" in elderly:
                    for item in elderly["common"]:
                        st.markdown(f"- {item}")
                if "note" in elderly:
                    st.error(elderly["note"])

