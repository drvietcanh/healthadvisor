"""
Suy Thận Mạn Tab Component
Hiển thị thông tin về bệnh Suy Thận Mạn
"""

import streamlit as st
from diseases.renal import chronic_kidney_disease as ckd


def render_ckd_tab():
    """Render tab Suy Thận Mạn với đầy đủ thông tin"""
    st.header("🫘 Suy Thận Mạn (Chronic Kidney Disease)")
    
    # Thông tin cơ bản
    with st.expander("📖 Suy thận mạn là gì?", expanded=True):
        if hasattr(ckd, 'CKD_INFO') and ckd.CKD_INFO:
            info = ckd.CKD_INFO
            st.markdown(info.get("simple_explanation", ""))
            if info.get("why_dangerous"):
                st.error(info.get("why_dangerous"))
            
            # Các giai đoạn
            if "stages" in info:
                stages = info["stages"]
                st.markdown(f"### {stages.get('title', '')}")
                st.caption(stages.get('description', ''))
                
                if "stages" in stages:
                    for stage in stages["stages"]:
                        if isinstance(stage, dict):
                            st.markdown(f"**Giai đoạn {stage.get('stage', '')}** - {stage.get('egfr', '')}")
                            st.caption(stage.get('name', ''))
                            st.markdown(f"Mô tả: {stage.get('description', '')}")
                            st.info(f"Hành động: {stage.get('action', '')}")
                            if stage.get('warning'):
                                st.error(stage['warning'])
                            st.divider()
    
    # Triệu chứng
    with st.expander("🔍 Triệu chứng", expanded=True):
        if hasattr(ckd, 'SYMPTOMS') and ckd.SYMPTOMS:
            symptoms = ckd.SYMPTOMS
            
            # Giai đoạn sớm
            if "early_stage" in symptoms:
                early = symptoms["early_stage"]
                st.error(f"### {early.get('title', '')}")
                st.warning(early.get('description', ''))
                if "symptoms" in early:
                    for symptom in early["symptoms"][:3]:
                        if isinstance(symptom, dict):
                            st.markdown(f"**{symptom.get('icon', '')} {symptom.get('name', '')}**")
                            st.caption(symptom.get('description', ''))
                            if symptom.get('warning'):
                                st.error(symptom['warning'])
                            st.divider()
            
            # Giai đoạn trung bình-nặng
            if "moderate_stage" in symptoms:
                moderate = symptoms["moderate_stage"]
                st.markdown(f"### {moderate.get('title', '')}")
                if "symptoms" in moderate:
                    for symptom in moderate["symptoms"][:5]:
                        if isinstance(symptom, dict):
                            st.markdown(f"**{symptom.get('icon', '')} {symptom.get('name', '')}**")
                            st.caption(symptom.get('description', ''))
                            if "details" in symptom:
                                for detail in symptom["details"]:
                                    st.markdown(f"- {detail}")
                            st.divider()
    
    # Nguyên nhân
    with st.expander("🔍 Nguyên nhân"):
        if hasattr(ckd, 'CAUSES') and ckd.CAUSES:
            causes = ckd.CAUSES
            
            if "main_causes" in causes:
                main = causes["main_causes"]
                st.markdown(f"### {main.get('title', '')}")
                st.caption(main.get('description', ''))
                
                if "causes" in main:
                    for cause in main["causes"][:2]:
                        if isinstance(cause, dict):
                            st.markdown(f"**{cause.get('name', '')}** ({cause.get('prevalence', '')})")
                            st.caption(cause.get('simple', ''))
                            if cause.get('prevention'):
                                st.success(f"Phòng ngừa: {cause['prevention']}")
                            st.divider()
    
    # Điều trị
    with st.expander("💊 Điều trị"):
        if hasattr(ckd, 'TREATMENT') and ckd.TREATMENT:
            treatment = ckd.TREATMENT
            
            if "goal" in treatment:
                goal = treatment["goal"]
                st.markdown(f"### {goal.get('title', '')}")
                st.caption(goal.get('description', ''))
                if "objectives" in goal:
                    for obj in goal["objectives"]:
                        st.markdown(f"- {obj}")
                if goal.get('key'):
                    st.success(goal['key'])
            
            if "medications" in treatment:
                meds = treatment["medications"]
                st.markdown(f"### {meds.get('title', '')}")
                if "drugs" in meds:
                    for drug_group in meds["drugs"][:2]:
                        if isinstance(drug_group, dict):
                            st.markdown(f"**{drug_group.get('name', '')}**")
                            st.caption(drug_group.get('description', ''))
                            if "drugs" in drug_group:
                                for drug in drug_group["drugs"][:1]:
                                    if isinstance(drug, dict):
                                        st.markdown(f"- **{drug.get('name', '')}**")
                                        if drug.get('benefit'):
                                            st.success(f"Lợi ích: {drug['benefit']}")
    
    # Chạy thận
    with st.expander("🔬 Chạy thận nhân tạo"):
        if hasattr(ckd, 'DIALYSIS') and ckd.DIALYSIS:
            dialysis = ckd.DIALYSIS
            
            if "when_needed" in dialysis:
                when = dialysis["when_needed"]
                st.markdown(f"### {when.get('title', '')}")
                st.caption(when.get('description', ''))
                if "indicators" in when:
                    for indicator in when["indicators"][:2]:
                        if isinstance(indicator, dict):
                            st.markdown(f"**{indicator.get('name', '')}**")
                            if "symptoms" in indicator:
                                for symptom in indicator["symptoms"]:
                                    st.markdown(f"- {symptom}")
            
            if "types" in dialysis:
                types = dialysis["types"]
                if "hemodialysis" in types:
                    hd = types["hemodialysis"]
                    st.markdown(f"### {hd.get('name', '')}")
                    st.caption(f"{hd.get('description', '')} - {hd.get('frequency', '')}")
    
    # Chế độ ăn
    with st.expander("🍽️ Chế độ ăn"):
        if hasattr(ckd, 'DIET') and ckd.DIET:
            diet = ckd.DIET
            
            if "salt_restriction" in diet:
                salt = diet["salt_restriction"]
                st.markdown(f"### {salt.get('title', '')}")
                st.caption("Quan trọng nhất!")
                if "avoid" in salt:
                    st.warning("**Tránh:**")
                    for item in salt["avoid"][:3]:
                        st.markdown(f"- {item}")

