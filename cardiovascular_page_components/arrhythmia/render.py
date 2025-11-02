"""
Render Function - Hiển thị tab Rối Loạn Nhịp Tim
"""

import streamlit as st

from cardiovascular_page_components.arrhythmia.data import (
    DISEASE_INFO,
    SYMPTOMS,
    TYPES,
    COMMON_CAUSES,
    ACTIONS,
    WHEN_TO_SEE_DOCTOR,
    MEDICATIONS
)


def render_arrhythmia_tab():
    """Render tab Rối Loạn Nhịp Tim"""
    
    st.header("❤️‍🩹 Rối Loạn Nhịp Tim")
    
    # Cảnh báo quan trọng
    st.error("""
    **⚠️ QUAN TRỌNG:** Rối loạn nhịp tim có thể nguy hiểm!
    - Nếu có triệu chứng **NGẶT XỈU**, **ĐAU NGỰC**, **KHÓ THỞ NẶNG** → **GỌI 115 NGAY!**
    """)
    
    # Giới thiệu
    with st.expander("📖 Rối loạn nhịp tim là gì?", expanded=True):
        st.markdown(DISEASE_INFO["description_vn"])
        st.info(f"**Phổ biến:** {DISEASE_INFO['prevalence_vn']}")
    
    # Triệu chứng
    with st.expander("🔍 Dấu hiệu nhận biết"):
        st.subheader("Triệu chứng thường gặp:")
        for symptom in SYMPTOMS["common_vn"]:
            st.markdown(f"- {symptom}")
        
        st.divider()
        st.error("**⚠️ TRIỆU CHỨNG NGUY HIỂM - GỌI 115:**")
        for symptom in SYMPTOMS["serious_vn"]:
            st.markdown(f"**{symptom}**")
    
    # Các loại rối loạn nhịp tim
    with st.expander("📋 Các loại rối loạn nhịp tim phổ biến"):
        for type_key, type_info in TYPES.items():
            st.subheader(type_info["name"])
            st.markdown(f"**Mô tả:** {type_info['description']}")
            
            st.markdown("**Ví dụ:**")
            for example in type_info["examples"]:
                st.markdown(f"- {example}")
            
            st.markdown(f"**💡 {type_info['treatment']}**")
            st.warning(f"⚠️ **Khi nào lo:** {type_info['when_worry']}")
            st.divider()
    
    # Nguyên nhân
    with st.expander("🤔 Nguyên nhân thường gặp"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("**✅ Nguyên nhân có thể khắc phục:**")
            for cause in COMMON_CAUSES["reversible"]:
                st.markdown(f"- {cause}")
        
        with col2:
            st.warning("**⚠️ Nguyên nhân do bệnh tim:**")
            for cause in COMMON_CAUSES["heart_disease"]:
                st.markdown(f"- {cause}")
        
        st.divider()
        st.info("**💡 Nguyên nhân khác:** " + ", ".join(COMMON_CAUSES["other"]))
    
    # Xử trí
    with st.expander("⚡ Xử trí tại nhà"):
        st.markdown("**KHI TIM ĐẬP BẤT THƯỜNG:**")
        for action in ACTIONS["immediate"]:
            if action == "":
                st.divider()
            else:
                st.markdown(action)
        
        st.divider()
        
        st.markdown("**PHÒNG NGỪA:**")
        for prevention in ACTIONS["prevention"]:
            st.markdown(f"- {prevention}")
    
    # Khi nào khám bác sĩ
    with st.expander("🏥 Khi nào cần khám bác sĩ"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.error("\n".join(WHEN_TO_SEE_DOCTOR["urgent"]))
        
        with col2:
            st.warning("\n".join(WHEN_TO_SEE_DOCTOR["soon"]))
    
    # Thuốc điều trị
    with st.expander("💊 Thuốc & Điều trị"):
        st.subheader("📋 Thuốc chống loạn nhịp")
        for med_info in [MEDICATIONS["antiarrhythmic"], MEDICATIONS["anticoagulation"]]:
            st.markdown(f"**{med_info['name']}**")
            for example in med_info["examples"]:
                st.markdown(f"- {example}")
            st.markdown(f"💡 {med_info['note']}")
            st.divider()
        
        st.subheader("🔋 Máy tạo nhịp tim")
        st.markdown(f"**{MEDICATIONS['pacemaker']['description']}**")
        st.markdown("**Các loại:**")
        for ptype in MEDICATIONS["pacemaker"]["types"]:
            st.markdown(f"- {ptype}")
        
        st.markdown("**💡 Sau phẫu thuật:**")
        for after in MEDICATIONS["pacemaker"]["after_surgery"]:
            st.markdown(f"- {after}")
    
    # Lưu ý
    st.info("""
    💡 **LƯU Ý:** 
    - Rối loạn nhịp tim cần **điện tâm đồ (ECG)** để chẩn đoán chính xác
    - Nhiều trường hợp **không cần điều trị**, chỉ theo dõi
    - **Quan trọng nhất:** Phát hiện sớm và xử trí kịp thời khi nguy hiểm
    """)

