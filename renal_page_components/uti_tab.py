"""
UTI Tab Component
"""

import streamlit as st
from diseases.renal.uti import UTI_INFO, SYMPTOMS, TREATMENT


def render_uti_tab():
    """Render tab Nhiễm Trùng Tiết Niệu"""
    st.header("🦠 Nhiễm Trùng Tiết Niệu (UTI)")
    
    # Thông tin cơ bản
    with st.expander("📖 Nhiễm trùng tiết niệu là gì?", expanded=True):
        if UTI_INFO:
            st.markdown(UTI_INFO.get("simple_explanation", ""))
            
            # Các loại
            if "types" in UTI_INFO:
                types = UTI_INFO["types"]
                col1, col2 = st.columns(2)
                with col1:
                    st.info(f"**{types['lower_uti']['name']}**\n\n{types['lower_uti']['common_name']} - {types['lower_uti']['severity']}")
                with col2:
                    st.warning(f"**{types['upper_uti']['name']}**\n\n{types['upper_uti']['common_name']} - {types['upper_uti']['severity']}")
    
    # Triệu chứng
    with st.expander("🔍 Triệu chứng"):
        if SYMPTOMS:
            if "common" in SYMPTOMS:
                st.markdown(f"### {SYMPTOMS['common']['title']}")
                for symptom in SYMPTOMS["common"]["symptoms"]:
                    st.markdown(f"- {symptom}")
            
            st.divider()
            
            if "serious" in SYMPTOMS:
                st.error(f"### {SYMPTOMS['serious']['title']}")
                for symptom in SYMPTOMS["serious"]["symptoms"]:
                    st.markdown(f"**{symptom}**")
                if SYMPTOMS["serious"].get("warning"):
                    st.warning(SYMPTOMS["serious"]["warning"])
            
            st.divider()
            
            if "elderly" in SYMPTOMS:
                elderly = SYMPTOMS["elderly"]
                st.markdown(f"### {elderly['title']}")
                st.caption(elderly.get("note", ""))
                for symptom in elderly.get("atypical_symptoms", []):
                    st.markdown(f"- {symptom}")
                if elderly.get("warning"):
                    st.info(elderly["warning"])
    
    # Điều trị
    with st.expander("💊 Điều trị"):
        if TREATMENT:
            # Thuốc
            if "medications" in TREATMENT:
                meds = TREATMENT["medications"]
                if "antibiotics" in meds:
                    st.markdown(f"### {meds['antibiotics']['title']}")
                    for ab in meds["antibiotics"]["common"]:
                        st.markdown(f"**{ab['name']}:**")
                        st.caption(f"Liều: {ab['dose']} - Dùng {ab['duration']}")
                        st.caption(f"💡 {ab['note']}")
                        st.divider()
                    if meds["antibiotics"].get("warning"):
                        st.warning(meds["antibiotics"]["warning"])
                
                if "pain_relief" in meds:
                    st.markdown(f"### {meds['pain_relief']['title']}")
                    for option in meds["pain_relief"]["options"]:
                        st.markdown(f"- {option}")
            
            st.divider()
            
            # Chăm sóc tại nhà
            if "self_care" in TREATMENT:
                care = TREATMENT["self_care"]
                st.markdown(f"### {care['title']}")
                
                if "drink_water" in care:
                    water = care["drink_water"]
                    st.markdown(f"**{water['title']}**")
                    st.caption(f"Lượng: {water['amount']}")
                    st.caption(f"Lý do: {water['why']}")
                    st.caption(f"💡 {water.get('tip', '')}")
                
                if "hygiene" in care:
                    st.markdown(f"**{care['hygiene']['title']}**")
                    for tip in care["hygiene"]["tips"]:
                        st.markdown(f"- {tip}")
                
                if "avoid" in care:
                    st.markdown(f"**{care['avoid']['title']}**")
                    for item in care["avoid"]["items"]:
                        st.markdown(f"- {item}")
    
    # Khi nào khám bác sĩ
    with st.expander("🏥 Khi nào cần khám bác sĩ"):
        if TREATMENT and "when_to_see_doctor" in TREATMENT:
            doctor = TREATMENT["when_to_see_doctor"]
            col1, col2 = st.columns(2)
            with col1:
                st.error("**🚨 KHẨN CẤP:**")
                for item in doctor.get("urgent", []):
                    st.markdown(f"- {item}")
            with col2:
                st.warning("**📋 SỚM:**")
                for item in doctor.get("soon", []):
                    st.markdown(f"- {item}")
    
    # Phòng ngừa
    with st.expander("✅ Phòng ngừa"):
        if TREATMENT and "prevention" in TREATMENT:
            st.markdown(f"### {TREATMENT['prevention']['title']}")
            for tip in TREATMENT["prevention"]["tips"]:
                st.markdown(f"- {tip}")

