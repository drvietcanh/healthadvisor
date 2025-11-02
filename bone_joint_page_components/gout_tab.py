"""
Gout Tab Component
Hiển thị bệnh Gút
"""

import streamlit as st


try:
    from diseases.bone_joint.gout import (
        GOUT_INFO,
        GOUT_SYMPTOMS,
        GOUT_CAUSES,
        GOUT_DIET,
        GOUT_TREATMENT,
        GOUT_MEDICATIONS,
        GOUT_PREVENTION
    )
except ImportError:
    st.error("Không thể tải module Gút. Vui lòng kiểm tra lại.")
    st.stop()


def render_gout_tab():
    """Tab Bệnh Gút"""
    st.header("🦶 Bệnh Gút (Gout)")
    
    # Thông tin cơ bản
    with st.expander("📖 Bệnh Gút là gì?", expanded=True):
        if GOUT_INFO:
            st.markdown(GOUT_INFO.get("simple_explanation", ""))
            
            # Tăng acid uric chưa phải gút
            if "hyperuricemia" in GOUT_INFO:
                hyper = GOUT_INFO["hyperuricemia"]
                st.markdown("---")
                st.markdown(f"### {hyper.get('title', '')}")
                st.markdown(hyper.get("explanation", ""))
                
                if "when_to_treat" in hyper:
                    when = hyper["when_to_treat"]
                    
                    # Không cần thuốc
                    if "no_medication" in when:
                        no_med = when["no_medication"]
                        st.success(f"**{no_med.get('title', '')}**")
                        st.markdown("**Khi nào:**")
                        for condition in no_med.get('conditions', []):
                            st.markdown(f"- {condition}")
                        st.markdown("**Làm gì:**")
                        for action in no_med.get('actions', []):
                            st.markdown(f"- {action}")
                    
                    st.divider()
                    
                    # Cân nhắc thuốc
                    if "consider_medication" in when:
                        consider = when["consider_medication"]
                        st.warning(f"**{consider.get('title', '')}**")
                        st.markdown("**Khi nào:**")
                        for condition in consider.get('conditions', []):
                            st.markdown(f"- {condition}")
                        st.info(consider.get('note', ''))
    
    # Triệu chứng
    with st.expander("🔍 Triệu chứng", expanded=False):
        if GOUT_SYMPTOMS:
            symptoms = GOUT_SYMPTOMS
            
            st.markdown("### Cơn Gút Cấp:")
            if "acute_attack" in symptoms:
                attack = symptoms["acute_attack"]
                st.markdown("**Đặc điểm:**")
                for char in attack.get("characteristics", []):
                    st.markdown(f"- {char}")
                
                if "timeline" in attack:
                    st.markdown("**Diễn biến:**")
                    for stage in attack["timeline"]:
                        st.markdown(f"- {stage}")
            
            if "red_flags" in symptoms:
                st.error("**🚨 Dấu hiệu cần đi khám ngay:**")
                for flag in symptoms["red_flags"]:
                    st.markdown(f"- {flag}")
    
    # Nguyên nhân
    with st.expander("🔍 Nguyên nhân", expanded=False):
        if GOUT_CAUSES:
            st.markdown(GOUT_CAUSES.get("mechanism", ""))
            
            if "risk_factors" in GOUT_CAUSES:
                factors = GOUT_CAUSES["risk_factors"]
                if "diet" in factors:
                    diet = factors["diet"]
                    st.markdown(f"### {diet.get('title', '')}")
                    if "high_purine" in diet:
                        st.markdown("**Thức ăn nhiều purine:**")
                        for food in diet["high_purine"]:
                            st.markdown(f"- {food}")
                    if "alcohol" in diet:
                        st.markdown("**Rượu bia:**")
                        for item in diet["alcohol"]:
                            st.markdown(f"- {item}")
    
    # Chế độ ăn
    with st.expander("🍽️ Chế độ ăn", expanded=False):
        if GOUT_DIET:
            diet = GOUT_DIET
            
            if "avoid" in diet:
                st.error("**❌ TRÁNH:**")
                avoid = diet["avoid"]
                if "foods" in avoid:
                    for food_item in avoid["foods"]:
                        if isinstance(food_item, dict):
                            st.markdown(f"**{food_item.get('category', food_item.get('examples', ''))}**")
                            if food_item.get('examples'):
                                st.markdown(f"- {food_item['examples']}")
                            if food_item.get('purine_level'):
                                st.caption(f"Mức purine: {food_item['purine_level']}")
                            st.warning(f"⚠️ {food_item.get('note', '')}")
                            st.divider()
            
            if "recommended" in diet:
                st.success("**✅ NÊN ĂN:**")
                rec = diet["recommended"]
                if "foods" in rec:
                    for food_item in rec["foods"]:
                        if isinstance(food_item, dict):
                            st.markdown(f"**{food_item.get('food', '')}**")
                            if food_item.get('examples'):
                                st.markdown(f"- {food_item['examples']}")
                            st.caption(f"💡 {food_item.get('why', '')}")
                            if food_item.get('note'):
                                st.info(f"📌 {food_item['note']}")
                            st.divider()
            
            if "drinking" in diet:
                drinking = diet["drinking"]
                st.markdown("### 💧 Uống nước:")
                st.markdown(f"**Tầm quan trọng:** {drinking.get('importance', '')}")
                st.markdown(f"**Lượng:** {drinking.get('amount', '')}")
                st.markdown(f"**Loại:** {drinking.get('what', '')}")
                st.warning(f"**Tránh:** {drinking.get('avoid', '')}")
    
    # Điều trị
    with st.expander("💊 Điều trị", expanded=False):
        if GOUT_TREATMENT:
            treatment = GOUT_TREATMENT
            
            if "acute_attack" in treatment:
                st.markdown("### 1️⃣ Điều trị cơn gút cấp:")
                acute = treatment["acute_attack"]
                st.markdown(f"**Mục tiêu:** {acute.get('goal', '')}")
                
                if "medications" in acute:
                    for med in acute["medications"]:
                        if isinstance(med, dict):
                            st.markdown(f"#### {med.get('drug', '')}")
                            st.markdown(f"**Liều:** {med.get('dose', '')}")
                            st.caption(f"💡 {med.get('when', '')}")
                            st.info(med.get('note', ''))
                            st.divider()
            
            if "long_term" in treatment:
                st.markdown("### 2️⃣ Điều trị lâu dài (Ngăn tái phát):")
                long_term = treatment["long_term"]
                st.markdown(f"**Mục tiêu:** {long_term.get('goal', '')}")
                
                st.markdown("**Khi nào bắt đầu:**")
                if "when_start" in long_term:
                    for when in long_term["when_start"]:
                        st.markdown(f"- {when}")
                
                if "medications" in long_term:
                    meds = long_term["medications"]
                    for med_key, med_info in meds.items():
                        if isinstance(med_info, dict):
                            st.markdown(f"#### {med_info.get('drug', med_key)}")
                            st.markdown(f"**Liều:** {med_info.get('dose', '')}")
                            st.caption(f"**Cơ chế:** {med_info.get('mechanism', '')}")
                            st.info(med_info.get('note', ''))
                            st.divider()
                
                if "important" in long_term:
                    st.warning(long_term["important"])
    
    # Phòng ngừa
    with st.expander("🛡️ Phòng ngừa", expanded=False):
        if GOUT_PREVENTION:
            prevention = GOUT_PREVENTION
            
            if "lifestyle" in prevention:
                st.markdown("### Thay đổi lối sống:")
                for item in prevention["lifestyle"]:
                    st.markdown(f"- {item}")
            
            if "medication_adherence" in prevention:
                st.markdown("### Dùng thuốc đều đặn:")
                for item in prevention["medication_adherence"]:
                    st.markdown(f"- {item}")
            
            if "warning" in prevention:
                st.error(prevention["warning"])

