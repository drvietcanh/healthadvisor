"""
Spine Tab Components
Hiển thị đau thắt lưng và thoát vị đĩa đệm
"""

import streamlit as st


try:
    from diseases.bone_joint.spine import (
        BACK_PAIN_INFO,
        BACK_PAIN_CAUSES,
        BACK_PAIN_MANAGEMENT,
        BACK_PAIN_EXERCISES
    )
    from diseases.bone_joint.spine import (
        HERNIATED_DISC_INFO,
        HERNIATED_DISC_SYMPTOMS,
        HERNIATED_DISC_TREATMENT
    )
    from diseases.bone_joint.spine import (
        SPINAL_POSTURE,
        SPINAL_EXERCISES,
        SPINAL_PROTECTION
    )
except ImportError:
    st.error("Không thể tải module cột sống. Vui lòng kiểm tra lại.")
    st.stop()


def render_back_pain_tab():
    """Tab Đau thắt lưng"""
    st.header("🫁 Đau Thắt Lưng")
    
    # Thông tin cơ bản
    with st.expander("📖 Đau thắt lưng là gì?", expanded=True):
        if BACK_PAIN_INFO:
            st.markdown(BACK_PAIN_INFO.get("simple_explanation", ""))
            
            if "types" in BACK_PAIN_INFO:
                types = BACK_PAIN_INFO["types"]
                col1, col2 = st.columns(2)
                with col1:
                    if "acute" in types:
                        acute = types["acute"]
                        st.info(f"""
                        **{acute.get('name', '')}**
                        
                        {acute.get('characteristics', '')}
                        
                        {acute.get('prognosis', '')}
                        """)
                with col2:
                    if "chronic" in types:
                        chronic = types["chronic"]
                        st.warning(f"""
                        **{chronic.get('name', '')}**
                        
                        {chronic.get('characteristics', '')}
                        
                        {chronic.get('prognosis', '')}
                        """)
    
    # Nguyên nhân
    with st.expander("🔍 Nguyên nhân", expanded=False):
        if BACK_PAIN_CAUSES:
            causes = BACK_PAIN_CAUSES
            
            if "mechanical" in causes:
                mech = causes["mechanical"]
                st.markdown(f"### {mech.get('title', '')}")
                if "causes" in mech:
                    for cause_item in mech["causes"]:
                        if isinstance(cause_item, dict):
                            st.markdown(f"**{cause_item.get('cause', '')}**")
                            st.caption(f"**Tại sao:** {cause_item.get('why', '')}")
                            st.markdown(f"**Đặc điểm:** {cause_item.get('characteristics', '')}")
                            st.divider()
            
            if "risk_factors" in causes:
                st.markdown("### Yếu tố nguy cơ:")
                for factor in causes["risk_factors"]:
                    st.markdown(f"- {factor}")
    
    # Điều trị
    with st.expander("💊 Điều trị", expanded=False):
        if BACK_PAIN_MANAGEMENT:
            mgmt = BACK_PAIN_MANAGEMENT
            
            if "acute_stage" in mgmt:
                st.markdown("### Giai đoạn cấp (<6 tuần):")
                acute = mgmt["acute_stage"]
                if "principles" in acute:
                    st.markdown("**Nguyên tắc:**")
                    for principle in acute["principles"]:
                        st.markdown(f"- {principle}")
                
                if "medications" in acute:
                    st.markdown("**Thuốc:**")
                    for med in acute["medications"]:
                        if isinstance(med, dict):
                            st.markdown(f"- **{med.get('drug', '')}:** {med.get('dose', '')}")
                            st.caption(med.get('note', ''))
            
            if "red_flags" in mgmt:
                st.error("**🚨 Dấu hiệu cần đi khám ngay:**")
                for flag in mgmt["red_flags"]:
                    st.markdown(f"- {flag}")
    
    # Bài tập
    with st.expander("🏃 Bài tập", expanded=False):
        if BACK_PAIN_EXERCISES:
            exercises = BACK_PAIN_EXERCISES
            
            if "acute_phase" in exercises:
                st.markdown("### Khi đau cấp:")
                acute_ex = exercises["acute_phase"]
                if "exercises" in acute_ex:
                    for ex in acute_ex["exercises"]:
                        if isinstance(ex, dict):
                            st.markdown(f"**{ex.get('name', '')}**")
                            st.markdown(f"Cách làm: {ex.get('how', '')}")
                            st.caption(f"Số lần: {ex.get('frequency', '')}")
                            st.divider()
            
            if "important" in exercises:
                st.warning(exercises["important"])


def render_herniated_disc_tab():
    """Tab Thoát vị đĩa đệm"""
    st.header("🫁 Thoát Vị Đĩa Đệm")
    
    # Thông tin cơ bản
    with st.expander("📖 Thoát vị đĩa đệm là gì?", expanded=True):
        if HERNIATED_DISC_INFO:
            st.markdown(HERNIATED_DISC_INFO.get("simple_explanation", ""))
            
            if "common_locations" in HERNIATED_DISC_INFO:
                st.markdown("### Vị trí thường gặp:")
                locations = HERNIATED_DISC_INFO["common_locations"]
                for loc_key, loc_info in locations.items():
                    if isinstance(loc_info, dict):
                        st.markdown(f"#### {loc_info.get('name', loc_key)}")
                        if loc_info.get('symptoms'):
                            st.markdown("**Triệu chứng:**")
                            for symptom in loc_info['symptoms']:
                                st.markdown(f"- {symptom}")
                        st.divider()
    
    # Triệu chứng
    with st.expander("🔍 Triệu chứng", expanded=False):
        if HERNIATED_DISC_SYMPTOMS:
            symptoms = HERNIATED_DISC_SYMPTOMS
            
            st.markdown("### Triệu chứng chính:")
            if "main_symptoms" in symptoms:
                for symptom in symptoms["main_symptoms"]:
                    st.markdown(f"- {symptom}")
            
            if "severity" in symptoms:
                sev = symptoms["severity"]
                st.markdown("### Mức độ:")
                for key, level_info in sev.items():
                    if isinstance(level_info, dict):
                        st.markdown(f"#### {level_info.get('level', key)}")
                        if level_info.get('symptoms'):
                            st.markdown("**Triệu chứng:**")
                            for s in level_info['symptoms']:
                                st.markdown(f"- {s}")
                        st.markdown(f"**Điều trị:** {level_info.get('treatment', '')}")
                        st.divider()
            
            if "red_flags" in symptoms:
                st.error("**🚨 Dấu hiệu cần đi khám ngay:**")
                for flag in symptoms["red_flags"]:
                    st.markdown(f"- {flag}")
    
    # Điều trị
    with st.expander("💊 Điều trị", expanded=False):
        if HERNIATED_DISC_TREATMENT:
            treatment = HERNIATED_DISC_TREATMENT
            
            if "conservative" in treatment:
                st.markdown("### 1️⃣ Điều trị bảo tồn (90% trường hợp):")
                conservative = treatment["conservative"]
                st.success(f"**Tỷ lệ thành công:** {conservative.get('success_rate', '')}")
                
                if "methods" in conservative:
                    for method in conservative["methods"]:
                        if isinstance(method, dict):
                            st.markdown(f"**{method.get('method', '')}**")
                            st.caption(f"Thời gian: {method.get('duration', '')}")
                            st.markdown(f"💡 {method.get('note', '')}")
                            st.divider()
            
            if "prevention" in treatment:
                st.markdown("### 🛡️ Phòng ngừa:")
                for tip in treatment["prevention"]:
                    st.markdown(f"- {tip}")

