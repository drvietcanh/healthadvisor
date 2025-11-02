"""
Nhồi Máu Cơ Tim Tab Component
Hiển thị thông tin về bệnh Nhồi Máu Cơ Tim
"""

import streamlit as st
import sys
sys.path.append('..')
from diseases.cardiovascular import myocardial_infarction as mi


def render_myocardial_infarction_tab():
    """Render tab Nhồi Máu Cơ Tim với đầy đủ thông tin"""
    st.header("💔 Nhồi Máu Cơ Tim (Heart Attack)")
    
    # Thông tin cơ bản
    with st.expander("📖 Nhồi máu cơ tim là gì?", expanded=True):
        if hasattr(mi, 'MI_INFO') and mi.MI_INFO:
            info = mi.MI_INFO
            st.markdown(info.get("simple_explanation", ""))
            if info.get("why_dangerous"):
                st.error(info.get("why_dangerous"))
    
    # Triệu chứng
    with st.expander("🔍 Triệu chứng nhồi máu cơ tim", expanded=True):
        if hasattr(mi, 'SYMPTOMS') and mi.SYMPTOMS:
            symptoms = mi.SYMPTOMS
            
            # Triệu chứng điển hình
            if "classic_symptoms" in symptoms:
                classic = symptoms["classic_symptoms"]
                st.subheader(f"{classic.get('title', '')}")
                st.caption(classic.get('description', ''))
                if "symptoms" in classic:
                    for symptom in classic["symptoms"]:
                        if isinstance(symptom, dict):
                            st.markdown(f"### {symptom.get('icon', '')} {symptom.get('name', '')}")
                            st.caption(symptom.get('description', ''))
                            if "details" in symptom:
                                for detail in symptom["details"]:
                                    st.markdown(f"- {detail}")
                            if symptom.get('warning'):
                                st.warning(symptom['warning'])
                            st.divider()
            
            # Triệu chứng không điển hình
            if "atypical_symptoms" in symptoms:
                atypical = symptoms["atypical_symptoms"]
                st.error(f"### {atypical.get('title', '')}")
                st.warning(atypical.get('warning', ''))
                if "common" in atypical:
                    for item in atypical["common"]:
                        if isinstance(item, dict):
                            st.markdown(f"**{item.get('name', '')}**")
                            st.caption(item.get('description', ''))
                            if item.get('risk'):
                                st.error(f"⚠️ {item['risk']}")
                            if item.get('note'):
                                st.info(item['note'])
                            st.divider()
            
            # Dấu hiệu đỏ
            if "red_flags" in symptoms:
                red_flags = symptoms["red_flags"]
                st.error(f"### {red_flags.get('title', '')}")
                st.error(red_flags.get('description', ''))
                if "symptoms" in red_flags:
                    for symptom in red_flags["symptoms"]:
                        if isinstance(symptom, dict):
                            st.markdown(f"**{symptom.get('name', '')}**")
                            st.caption(symptom.get('description', ''))
                if red_flags.get('action'):
                    st.error(f"🚨 {red_flags['action']}")
    
    # Khung giờ vàng
    with st.expander("⏰ Khung Giờ Vàng - QUAN TRỌNG NHẤT!", expanded=True):
        if hasattr(mi, 'EMERGENCY_MANAGEMENT') and mi.EMERGENCY_MANAGEMENT:
            emergency = mi.EMERGENCY_MANAGEMENT
            
            if "golden_time" in emergency:
                golden = emergency["golden_time"]
                st.error(f"### {golden.get('title', '')}")
                st.caption(golden.get('description', ''))
                
                if "time_windows" in golden:
                    for window in golden["time_windows"]:
                        if isinstance(window, dict):
                            st.markdown(f"### {window.get('time', '')} - {window.get('name', '')}")
                            st.caption(window.get('description', ''))
                            
                            if "treatment" in window:
                                st.markdown("**Điều trị:**")
                                for tx in window["treatment"]:
                                    st.markdown(f"- {tx}")
                            
                            if window.get('benefit'):
                                st.success(f"Lợi ích: {window['benefit']}")
                            
                            if window.get('mortality'):
                                st.warning(f"Tỷ lệ tử vong: {window['mortality']}")
                            
                            if window.get('warning'):
                                st.error(window['warning'])
                            
                            st.divider()
                
                if golden.get('summary'):
                    st.success(golden['summary'])
            
            # Xử trí ngay
            if "first_aid" in emergency:
                first_aid = emergency["first_aid"]
                st.error(f"### {first_aid.get('title', '')}")
                if "steps" in first_aid:
                    for step in first_aid["steps"]:
                        if isinstance(step, dict):
                            st.markdown(f"**{step.get('step', '')}**")
                            st.caption(step.get('description', ''))
                            if "why" in step:
                                if isinstance(step["why"], list):
                                    for reason in step["why"]:
                                        st.markdown(f"- {reason}")
                                else:
                                    st.caption(step["why"])
                            if step.get('warning'):
                                st.warning(step['warning'])
                            st.divider()
    
    # Điều trị
    with st.expander("💊 Điều trị nhồi máu cơ tim"):
        if hasattr(mi, 'TREATMENT') and mi.TREATMENT:
            treatment = mi.TREATMENT
            
            if "acute_treatment" in treatment:
                acute = treatment["acute_treatment"]
                st.markdown(f"### {acute.get('title', '')}")
                st.caption(acute.get('description', ''))
                
                if "methods" in acute:
                    for method in acute["methods"]:
                        if isinstance(method, dict):
                            st.markdown(f"**{method.get('name', '')}**")
                            st.caption(method.get('description', ''))
                            if "benefit" in method:
                                st.success("Lợi ích:")
                                for benefit in method["benefit"]:
                                    st.markdown(f"- {benefit}")
                            st.divider()
            
            # Chăm sóc sau nhồi máu
            if "post_mi_care" in treatment:
                post_care = treatment["post_mi_care"]
                st.markdown(f"### {post_care.get('title', '')}")
                
                if "medications" in post_care:
                    meds = post_care["medications"]
                    st.error(f"### {meds.get('title', '')}")
                    if "must_take" in meds:
                        for med in meds["must_take"]:
                            if isinstance(med, dict):
                                st.markdown(f"**{med.get('name', '')}** - {med.get('frequency', '')}")
                                st.caption(f"Lý do: {med.get('why', '')}")
                                if med.get('warning'):
                                    st.error(med['warning'])
                                st.divider()
    
    # Phòng ngừa
    with st.expander("🛡️ Phòng ngừa nhồi máu cơ tim"):
        if hasattr(mi, 'PREVENTION') and mi.PREVENTION:
            prev = mi.PREVENTION
            
            if "primary_prevention" in prev:
                primary = prev["primary_prevention"]
                st.markdown(f"### {primary.get('title', '')}")
                st.caption(primary.get('description', ''))
                
                if "methods" in primary:
                    for method in primary["methods"]:
                        if isinstance(method, dict):
                            st.markdown(f"### {method.get('name', '')}")
                            if method.get('priority'):
                                st.error(f"**{method['priority']}**")
                            if method.get('benefit'):
                                st.success(f"Lợi ích: {method['benefit']}")
                            if "should_eat" in method:
                                st.success("**Nên ăn:**")
                                for item in method["should_eat"]:
                                    st.markdown(f"- {item}")
                            if "should_limit" in method:
                                st.warning("**Hạn chế:**")
                                for item in method["should_limit"]:
                                    st.markdown(f"- {item}")
                            st.divider()

