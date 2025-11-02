"""
Neurological Page Components - Headache Tab
Tab Đau Đầu
"""

import streamlit as st
import sys
import os

# Thêm thư mục gốc vào path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

from diseases.neurological import headache


def render_headache_tab():
    """Render tab Đau Đầu"""
    st.header("💆 Đau Đầu & Đau Nửa Đầu")
    
    # Thông tin cơ bản
    with st.expander("📖 Đau đầu là gì?", expanded=True):
        if hasattr(headache, 'HEADACHE_INFO') and headache.HEADACHE_INFO:
            info = headache.HEADACHE_INFO
            st.markdown(info.get("simple_explanation", ""))
            if info.get("why_important"):
                st.warning(info.get("why_important"))
    
    # Dấu hiệu nguy hiểm
    with st.expander("🚨 Dấu hiệu đau đầu nguy hiểm - Cần cấp cứu ngay!", expanded=True):
        if hasattr(headache, 'DANGEROUS_SIGNS') and headache.DANGEROUS_SIGNS:
            dangerous = headache.DANGEROUS_SIGNS
            st.error(f"### {dangerous.get('title', '')}")
            
            for key in ["thunderclap", "first_severe", "progressive", "with_fever_stiff_neck", "after_head_injury", "with_visual_changes"]:
                if key in dangerous:
                    sign = dangerous[key]
                    st.markdown(f"**{sign.get('name', '')}**")
                    st.caption(sign.get('description', ''))
                    if "causes" in sign:
                        for cause in sign["causes"]:
                            st.markdown(f"- {cause}")
                    if "accompanying" in sign:
                        for acc in sign["accompanying"]:
                            st.markdown(f"- {acc}")
                    if sign.get("action"):
                        st.error(f"🚨 {sign['action']}")
                    st.divider()
    
    # Các loại đau đầu
    with st.expander("🔍 Các loại đau đầu thường gặp"):
        if hasattr(headache, 'HEADACHE_TYPES') and headache.HEADACHE_TYPES:
            types = headache.HEADACHE_TYPES
            
            # Đau đầu căng thẳng
            if "tension" in types:
                tension = types["tension"]
                st.markdown(f"### {tension.get('name', '')}")
                st.caption(tension.get('description', ''))
                if "characteristics" in tension:
                    char = tension["characteristics"]
                    if "pain" in char:
                        st.markdown(f"**Đặc điểm đau:** {char['pain'].get('type', '')}")
                        st.markdown(f"- Vị trí: {char['pain'].get('location', '')}")
                        st.markdown(f"- Mức độ: {char['pain'].get('severity', '')}")
                    if "triggers" in char:
                        st.markdown("**Yếu tố kích phát:**")
                        for trigger in char["triggers"]:
                            st.markdown(f"- {trigger}")
                    if "treatment" in char:
                        treat = char["treatment"]
                        st.markdown("**Điều trị:**")
                        if "mild" in treat:
                            st.success(f"Nhẹ: {treat['mild']}")
                        if "prevention" in treat:
                            st.info(f"Phòng ngừa: {treat['prevention']}")
                st.divider()
            
            # Đau nửa đầu
            if "migraine" in types:
                mig = types["migraine"]
                st.markdown(f"### {mig.get('name', '')}")
                st.caption(mig.get('description', ''))
                if "characteristics" in mig:
                    char = mig["characteristics"]
                    if "pain" in char:
                        st.markdown(f"**Đặc điểm đau:** {char['pain'].get('type', '')}")
                        st.markdown(f"- Vị trí: {char['pain'].get('location', '')}")
                        st.markdown(f"- Mức độ: {char['pain'].get('severity', '')}")
                        st.markdown(f"- Thời gian: {char['pain'].get('duration', '')}")
                    if "aura" in char:
                        aura = char["aura"]
                        st.markdown(f"**Triệu chứng báo trước (Aura):** {aura.get('description', '')}")
                        for symptom in aura.get("symptoms", [])[:3]:
                            st.markdown(f"- {symptom}")
                        if aura.get("warning"):
                            st.warning(aura["warning"])
                    if "accompanying" in char:
                        acc = char["accompanying"]
                        if "common" in acc:
                            st.markdown("**Triệu chứng kèm theo:**")
                            for symptom in acc["common"]:
                                st.markdown(f"- {symptom}")
                st.divider()
    
    # Điều trị
    with st.expander("💊 Điều trị đau đầu", expanded=True):
        if hasattr(headache, 'TREATMENT') and headache.TREATMENT:
            treat = headache.TREATMENT
            
            # Đau đầu căng thẳng
            if "tension_headache" in treat:
                tension_tx = treat["tension_headache"]
                st.markdown(f"### {tension_tx.get('title', 'Đau đầu căng thẳng')}")
                
                if "acute" in tension_tx:
                    acute = tension_tx["acute"]
                    st.markdown(f"**{acute.get('name', 'Cắt cơn đau')}:**")
                    if "medications" in acute:
                        for med in acute["medications"][:2]:
                            st.markdown(f"- **{med.get('name', '')}:** {med.get('dosage', '')}")
                            if med.get('note'):
                                st.caption(med['note'])
                            if med.get('warning'):
                                st.warning(med['warning'])
                    if "non_medication" in acute:
                        st.markdown("**Không dùng thuốc:**")
                        for method in acute["non_medication"][:3]:
                            st.markdown(f"- {method}")
                    st.divider()
                
                if "prevention" in tension_tx:
                    prev = tension_tx["prevention"]
                    st.markdown(f"**{prev.get('name', 'Phòng ngừa')}:**")
                    for method in prev.get("methods", [])[:5]:
                        st.markdown(f"- {method}")
            
            # Đau nửa đầu
            if "migraine" in treat:
                mig_tx = treat["migraine"]
                st.markdown(f"### {mig_tx.get('title', 'Đau nửa đầu')}")
                
                if "acute" in mig_tx:
                    acute = mig_tx["acute"]
                    if "moderate_severe" in acute:
                        st.markdown("**Đau trung bình-nặng:**")
                        for option in acute["moderate_severe"]:
                            if "name" in option:
                                st.markdown(f"**{option['name']}**")
                                if "examples" in option:
                                    for ex in option["examples"][:2]:
                                        st.markdown(f"- {ex}")
                                if option.get('warning'):
                                    st.error(option['warning'])
                                st.divider()
                
                if "prevention" in mig_tx:
                    prev = mig_tx["prevention"]
                    st.markdown(f"### {prev.get('name', 'Phòng ngừa')}")
                    if "medications" in prev:
                        st.markdown("**Thuốc (theo chỉ định bác sĩ):**")
                        for med in prev["medications"][:2]:
                            st.markdown(f"- **{med.get('name', '')}:** {med.get('dosage', '')}")
                            st.caption(med.get('note', ''))
                    if "lifestyle" in prev:
                        st.markdown("**Lối sống:**")
                        for method in prev["lifestyle"][:5]:
                            st.markdown(f"- {method}")
            
            # Khi nào cần khám bác sĩ
            if "when_to_see_doctor" in treat:
                see_doc = treat["when_to_see_doctor"]
                st.error("### 👨‍⚕️ Khi nào cần đi khám bác sĩ?")
                
                if "urgent" in see_doc:
                    urgent = see_doc["urgent"]
                    st.error(f"**{urgent.get('name', 'Cấp cứu ngay (GỌI 115):')}**")
                    for sign in urgent.get("signs", [])[:4]:
                        st.markdown(f"- {sign}")
                    st.divider()
                
                if "soon" in see_doc:
                    soon = see_doc["soon"]
                    st.warning(f"**{soon.get('name', 'Khám trong vài ngày:')}**")
                    for sign in soon.get("signs", [])[:4]:
                        st.markdown(f"- {sign}")

