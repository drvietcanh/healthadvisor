"""
Arthritis Tab Components
Hiển thị thoái hóa khớp và viêm khớp dạng thấp
"""

import streamlit as st
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

try:
    from diseases.bone_joint.arthritis import (
        OSTEOARTHRITIS_INFO,
        OSTEOARTHRITIS_SYMPTOMS,
        OSTEOARTHRITIS_TREATMENT,
        OSTEOARTHRITIS_MANAGEMENT
    )
    from diseases.bone_joint.arthritis import (
        RHEUMATOID_ARTHRITIS_INFO,
        RHEUMATOID_ARTHRITIS_SYMPTOMS,
        RHEUMATOID_ARTHRITIS_TREATMENT,
        RHEUMATOID_ARTHRITIS_MEDICATIONS
    )
    from diseases.bone_joint.arthritis import (
        JOINT_EXERCISES,
        JOINT_NUTRITION,
        JOINT_PROTECTION
    )
except ImportError:
    st.error("Không thể tải module khớp. Vui lòng kiểm tra lại.")
    st.stop()


def render_osteoarthritis_tab():
    """Tab Thoái hóa khớp"""
    st.header("🦴 Thoái Hóa Khớp (Osteoarthritis)")
    
    # Thông tin cơ bản
    with st.expander("📖 Thoái hóa khớp là gì?", expanded=True):
        if OSTEOARTHRITIS_INFO:
            st.markdown(OSTEOARTHRITIS_INFO.get("simple_explanation", ""))
            
            # Khớp thường bị
            if "common_joints" in OSTEOARTHRITIS_INFO:
                st.markdown("### 🔍 Khớp thường bị:")
                joints = OSTEOARTHRITIS_INFO["common_joints"]
                for joint_key, joint_info in joints.items():
                    if isinstance(joint_info, dict):
                        st.markdown(f"#### {joint_info.get('name', joint_key)}")
                        st.markdown(f"**Tần suất:** {joint_info.get('frequency', '')}")
                        if joint_info.get('why'):
                            st.caption(f"**Tại sao:** {joint_info['why']}")
                        if joint_info.get('symptoms'):
                            st.markdown("**Triệu chứng:**")
                            for symptom in joint_info['symptoms']:
                                st.markdown(f"- {symptom}")
                        st.divider()
    
    # Triệu chứng
    with st.expander("🔍 Triệu chứng", expanded=False):
        if OSTEOARTHRITIS_SYMPTOMS:
            symptoms = OSTEOARTHRITIS_SYMPTOMS
            
            st.markdown("### Giai đoạn sớm:")
            if "early_stage" in symptoms:
                for symptom in symptoms["early_stage"]:
                    st.markdown(f"- {symptom}")
            
            st.divider()
            
            st.markdown("### Giai đoạn nặng:")
            if "advanced_stage" in symptoms:
                for symptom in symptoms["advanced_stage"]:
                    st.markdown(f"- {symptom}")
            
            if "red_flags" in symptoms:
                st.warning("**⚠️ Dấu hiệu cần đi khám ngay:**")
                for flag in symptoms["red_flags"]:
                    st.markdown(f"- {flag}")
    
    # Điều trị
    with st.expander("💊 Điều trị", expanded=False):
        if OSTEOARTHRITIS_TREATMENT:
            treatment = OSTEOARTHRITIS_TREATMENT
            
            # Không dùng thuốc
            if "non_drug" in treatment:
                non_drug = treatment["non_drug"]
                st.markdown(f"### {non_drug.get('title', '')}")
                if "methods" in non_drug:
                    for method in non_drug["methods"]:
                        if isinstance(method, dict):
                            st.markdown(f"**{method.get('method', '')}**")
                            if method.get('explanation'):
                                st.caption(f"💡 {method['explanation']}")
                            if method.get('types'):
                                st.markdown("Loại bài tập:")
                                for ex_type in method['types']:
                                    st.markdown(f"- {ex_type}")
                            if method.get('how'):
                                st.markdown(f"Cách làm: {method['how']}")
                            st.divider()
            
            # Thuốc
            if "medications" in treatment:
                meds = treatment["medications"]
                st.markdown(f"### {meds.get('title', '')}")
                
                # Thuốc bôi
                if "topical" in meds:
                    topical = meds["topical"]
                    st.markdown(f"#### {topical.get('type', '')}")
                    if topical.get('examples'):
                        st.markdown("**Ví dụ:** " + ", ".join(topical['examples']))
                    st.markdown(f"**Cách dùng:** {topical.get('how', '')}")
                    st.info(topical.get('note', ''))
                
                # Thuốc uống
                if "oral" in meds:
                    oral = meds["oral"]
                    st.markdown("#### Thuốc uống:")
                    if "mild" in oral:
                        st.markdown(f"- **{oral['mild'].get('drug', '')}:** {oral['mild'].get('dose', '')}")
                        st.caption(f"💡 {oral['mild'].get('note', '')}")
                    if "moderate" in oral:
                        st.markdown(f"- **{oral['moderate'].get('drug', '')}:** {oral['moderate'].get('dose', '')}")
                        st.warning(oral['moderate'].get('note', ''))
                
                # Tiêm khớp
                if "injections" in meds:
                    st.markdown("#### Tiêm khớp:")
                    injections = meds["injections"]
                    if "corticosteroid" in injections:
                        cort = injections["corticosteroid"]
                        st.markdown(f"- **{cort.get('what', '')}:** {cort.get('duration', '')}")
                        st.caption(cort.get('note', ''))
                    if "hyaluronic_acid" in injections:
                        ha = injections["hyaluronic_acid"]
                        st.markdown(f"- **{ha.get('what', '')}:** {ha.get('duration', '')}")
                        st.caption(f"💰 {ha.get('note', '')}")
    
    # Quản lý
    with st.expander("📋 Quản lý hàng ngày", expanded=False):
        if OSTEOARTHRITIS_MANAGEMENT:
            mgmt = OSTEOARTHRITIS_MANAGEMENT
            
            if "daily_tips" in mgmt:
                st.markdown("### Mẹo hàng ngày:")
                for tip in mgmt["daily_tips"]:
                    st.markdown(f"- {tip}")
            
            if "exercises" in mgmt:
                st.markdown("### Bài tập:")
                exercises = mgmt["exercises"]
                for joint, ex_list in exercises.items():
                    st.markdown(f"#### {joint.upper()}:")
                    for ex in ex_list:
                        st.markdown(f"- {ex}")
            
            if "nutrition" in mgmt:
                nutrition = mgmt["nutrition"]
                st.markdown("### Dinh dưỡng:")
                if "good_foods" in nutrition:
                    st.markdown("**✅ Nên ăn:**")
                    for food in nutrition["good_foods"]:
                        st.markdown(f"- {food}")
                if "avoid_foods" in nutrition:
                    st.markdown("**❌ Tránh:**")
                    for food in nutrition["avoid_foods"]:
                        st.markdown(f"- {food}")


def render_rheumatoid_arthritis_tab():
    """Tab Viêm khớp dạng thấp"""
    st.header("🔴 Viêm Khớp Dạng Thấp (Rheumatoid Arthritis)")
    
    # Thông tin cơ bản
    with st.expander("📖 Viêm khớp dạng thấp là gì?", expanded=True):
        if RHEUMATOID_ARTHRITIS_INFO:
            st.markdown(RHEUMATOID_ARTHRITIS_INFO.get("simple_explanation", ""))
            
            # Phân biệt với thoái hóa
            if "key_differences" in RHEUMATOID_ARTHRITIS_INFO:
                st.markdown("### 🔍 Phân biệt với thoái hóa khớp:")
                diff = RHEUMATOID_ARTHRITIS_INFO["key_differences"]
                st.info(f"**Thoái hóa:** {diff.get('osteoarthritis', '')}")
                st.error(f"**Viêm dạng thấp:** {diff.get('rheumatoid', '')}")
    
    # Triệu chứng
    with st.expander("🔍 Triệu chứng", expanded=False):
        if RHEUMATOID_ARTHRITIS_SYMPTOMS:
            symptoms = RHEUMATOID_ARTHRITIS_SYMPTOMS
            
            st.markdown("### Triệu chứng sớm:")
            if "early_symptoms" in symptoms:
                for symptom in symptoms["early_symptoms"]:
                    st.markdown(f"- {symptom}")
            
            st.divider()
            
            st.markdown("### Triệu chứng nặng:")
            if "advanced_symptoms" in symptoms:
                for symptom in symptoms["advanced_symptoms"]:
                    st.markdown(f"- {symptom}")
            
            if "red_flags" in symptoms:
                st.error("**🚨 Dấu hiệu cần đi khám ngay:**")
                for flag in symptoms["red_flags"]:
                    st.markdown(f"- {flag}")
    
    # Điều trị
    with st.expander("💊 Điều trị", expanded=False):
        if RHEUMATOID_ARTHRITIS_TREATMENT:
            treatment = RHEUMATOID_ARTHRITIS_TREATMENT
            
            st.warning(treatment.get("importance", ""))
            
            if "medications" in treatment:
                meds = treatment["medications"]
                
                # DMARDs
                if "dmards" in meds:
                    dmards = meds["dmards"]
                    st.markdown(f"### {dmards.get('title', '')}")
                    st.markdown(f"**Cơ chế:** {dmards.get('explanation', '')}")
                    
                    if "examples" in dmards:
                        st.markdown("**Các thuốc:**")
                        for drug in dmards["examples"]:
                            if isinstance(drug, dict):
                                st.markdown(f"#### {drug.get('drug', '')}")
                                st.markdown(f"**Liều:** {drug.get('dose', '')}")
                                st.caption(drug.get('note', ''))
                                st.divider()
                    
                    st.info(f"**Quan trọng:** {dmards.get('duration', '')}")
                
                # Thuốc sinh học
                if "biologicals" in meds:
                    bio = meds["biologicals"]
                    st.markdown(f"### {bio.get('title', '')}")
                    st.markdown(f"**Cơ chế:** {bio.get('explanation', '')}")
                    if "examples" in bio:
                        for example in bio["examples"]:
                            st.markdown(f"- {example}")
                    st.warning(f"**💰 Giá:** {bio.get('cost', '')}")
                    st.caption(f"**Khi nào dùng:** {bio.get('when', '')}")
                    st.info(bio.get('note', ''))
    
    # Thuốc và theo dõi
    with st.expander("📊 Phác đồ điều trị", expanded=False):
        if RHEUMATOID_ARTHRITIS_MEDICATIONS:
            meds_info = RHEUMATOID_ARTHRITIS_MEDICATIONS
            
            if "dmard_regimens" in meds_info:
                regimens = meds_info["dmard_regimens"]
                
                if "first_line" in regimens:
                    st.markdown("### 1️⃣ Điều trị đầu tiên:")
                    fl = regimens["first_line"]
                    st.markdown(f"**Thuốc:** {fl.get('drug', '')}")
                    st.markdown(f"**Liều:** {fl.get('dose', '')}")
                    st.markdown(f"**Thời gian:** {fl.get('duration', '')}")
                    st.caption(f"💡 {fl.get('if_fail', '')}")
                
                if "combination" in regimens:
                    st.markdown("### 2️⃣ Phối hợp thuốc:")
                    combo = regimens["combination"]
                    st.markdown(f"**Ví dụ:** {combo.get('example', '')}")
                    st.caption(combo.get('note', ''))
            
            if "monitoring" in meds_info:
                st.markdown("### 📊 Theo dõi:")
                for item in meds_info["monitoring"]:
                    st.markdown(f"- {item}")
            
            if "important_notes" in meds_info:
                st.markdown("### ⚠️ Lưu ý quan trọng:")
                for note in meds_info["important_notes"]:
                    st.markdown(f"- {note}")

