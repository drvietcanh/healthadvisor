"""
Sa Sút Trí Tuệ Tab Component
Hiển thị thông tin về bệnh Sa Sút Trí Tuệ
"""

import streamlit as st
import sys
import os

# Thêm thư mục gốc vào path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

from diseases.neurological import dementia


def render_dementia_tab():
    """Render tab Sa Sút Trí Tuệ với đầy đủ thông tin"""
    st.header("🧠 Sa Sút Trí Tuệ (Dementia)")
    
    # Thông tin cơ bản
    with st.expander("📖 Sa sút trí tuệ là gì?", expanded=True):
        if hasattr(dementia, 'DEMENTIA_INFO') and dementia.DEMENTIA_INFO:
            info = dementia.DEMENTIA_INFO
            st.markdown(info.get("simple_explanation", ""))
            if info.get("why_important"):
                st.warning(info.get("why_important"))
    
    # Triệu chứng
    with st.expander("🔍 Dấu hiệu nhận biết", expanded=True):
        if hasattr(dementia, 'SYMPTOMS') and dementia.SYMPTOMS:
            symptoms = dementia.SYMPTOMS
            
            # Dấu hiệu sớm
            if "early_signs" in symptoms:
                early = symptoms["early_signs"]
                st.subheader(f"{early.get('title', '')}")
                st.caption(early.get('description', ''))
                if "signs" in early:
                    for sign in early["signs"]:
                        if isinstance(sign, dict):
                            st.markdown(f"### {sign.get('icon', '')} {sign.get('name', '')}")
                            st.caption(sign.get('description', ''))
                            if "examples" in sign:
                                st.markdown("**Ví dụ:**")
                                for ex in sign["examples"]:
                                    st.markdown(f"- {ex}")
                            if sign.get('vs_normal'):
                                st.info(f"💡 {sign['vs_normal']}")
                            st.divider()
                
                if early.get('note'):
                    st.error(early['note'])
            
            # Phân biệt với quên bình thường
            if "vs_normal_forgetfulness" in symptoms:
                vs_normal = symptoms["vs_normal_forgetfulness"]
                st.markdown(f"### {vs_normal.get('title', '')}")
                st.caption(vs_normal.get('description', ''))
                
                col1, col2 = st.columns(2)
                with col1:
                    if "normal" in vs_normal:
                        normal = vs_normal["normal"]
                        st.success(f"**{normal.get('name', '')}**")
                        if "examples" in normal:
                            for ex in normal["examples"]:
                                st.markdown(f"- {ex}")
                
                with col2:
                    if "dementia" in vs_normal:
                        dem = vs_normal["dementia"]
                        st.error(f"**{dem.get('name', '')}**")
                        if "examples" in dem:
                            for ex in dem["examples"]:
                                st.markdown(f"- {ex}")
                
                if vs_normal.get('note'):
                    st.warning(vs_normal['note'])
    
    # Nguyên nhân và yếu tố nguy cơ
    with st.expander("🔍 Nguyên nhân và yếu tố nguy cơ"):
        if hasattr(dementia, 'CAUSES') and dementia.CAUSES:
            causes = dementia.CAUSES
            
            if "risk_factors" in causes:
                risks = causes["risk_factors"]
                st.markdown(f"### {risks.get('title', '')}")
                st.caption(risks.get('description', ''))
                
                # Yếu tố không thay đổi được
                if "cannot_change" in risks:
                    st.markdown("**Yếu tố không thay đổi được:**")
                    for risk in risks["cannot_change"]:
                        if isinstance(risk, dict):
                            st.markdown(f"- **{risk.get('name', '')}**")
                            if risk.get('description'):
                                st.caption(risk['description'])
                            if "facts" in risk:
                                for fact in risk["facts"]:
                                    st.markdown(f"  - {fact}")
                
                # Yếu tố có thể thay đổi
                if "can_change" in risks:
                    st.success("**Yếu tố CÓ THỂ thay đổi (phòng ngừa được!):**")
                    for risk in risks["can_change"][:5]:
                        if isinstance(risk, dict):
                            st.markdown(f"- **{risk.get('name', '')}**")
                            st.caption(f"{risk.get('description', '')} - {risk.get('action', '')}")
                            if risk.get('benefit'):
                                st.success(f"Lợi ích: {risk['benefit']}")
            
            # Yếu tố bảo vệ
            if "protective_factors" in causes:
                protective = causes["protective_factors"]
                st.markdown(f"### {protective.get('title', '')}")
                st.caption(protective.get('description', ''))
                
                if "factors" in protective:
                    for factor in protective["factors"][:3]:
                        if isinstance(factor, dict):
                            st.markdown(f"**{factor.get('name', '')}**")
                            if factor.get('benefit'):
                                st.success(f"Lợi ích: {factor['benefit']}")
                            if "activities" in factor:
                                for activity in factor["activities"]:
                                    st.markdown(f"- {activity}")
                            st.divider()
    
    # Điều trị
    with st.expander("💊 Điều trị"):
        if hasattr(dementia, 'TREATMENT') and dementia.TREATMENT:
            treatment = dementia.TREATMENT
            
            if "medications" in treatment:
                meds = treatment["medications"]
                st.markdown(f"### {meds.get('title', '')}")
                st.caption(meds.get('description', ''))
                
                if "drugs" in meds:
                    for drug in meds["drugs"][:2]:
                        if isinstance(drug, dict):
                            st.markdown(f"**{drug.get('name', '')}** - {drug.get('dosage', '')}")
                            st.caption(drug.get('how_it_works', ''))
                            if "benefit" in drug:
                                st.success("Lợi ích:")
                                for benefit in drug["benefit"]:
                                    st.markdown(f"- {benefit}")
                            if drug.get('note'):
                                st.warning(drug['note'])
                            st.divider()
            
            if "when_to_see_doctor" in treatment:
                see_doc = treatment["when_to_see_doctor"]
                st.error(f"### {see_doc.get('title', '')}")
                st.caption(see_doc.get('description', ''))
                if "signs" in see_doc:
                    for sign in see_doc["signs"]:
                        if isinstance(sign, dict):
                            st.markdown(f"**{sign.get('name', '')}**")
                            if "items" in sign:
                                for item in sign["items"]:
                                    st.markdown(f"- {item}")
    
    # Chăm sóc
    with st.expander("🏠 Chăm sóc người sa sút trí tuệ"):
        if hasattr(dementia, 'CARE') and dementia.CARE:
            care = dementia.CARE
            
            if "communication" in care:
                comm = care["communication"]
                st.markdown(f"### {comm.get('title', '')}")
                st.caption(comm.get('description', ''))
                
                if "principles" in comm:
                    for principle in comm["principles"][:2]:
                        if isinstance(principle, dict):
                            st.markdown(f"**{principle.get('name', '')}**")
                            if "how" in principle:
                                st.success("Nên làm:")
                                for item in principle["how"]:
                                    st.markdown(f"- {item}")
                            if "avoid" in principle:
                                st.warning("Tránh:")
                                for item in principle["avoid"]:
                                    st.markdown(f"- {item}")
                            st.divider()
            
            if "daily_care" in care:
                daily = care["daily_care"]
                st.markdown(f"### {daily.get('title', '')}")
                
                if "areas" in daily:
                    for area in daily["areas"][:3]:
                        if isinstance(area, dict):
                            st.markdown(f"**{area.get('name', '')}**")
                            if "critical" in area:
                                for item in area["critical"]:
                                    st.markdown(f"- {item}")
                            if area.get('warning'):
                                st.error(area['warning'])
                            st.divider()
    
    # Phòng ngừa
    with st.expander("🛡️ Phòng ngừa sa sút trí tuệ"):
        if hasattr(dementia, 'PREVENTION') and dementia.PREVENTION:
            prev = dementia.PREVENTION
            
            if "lifestyle" in prev:
                lifestyle = prev["lifestyle"]
                st.markdown(f"### {lifestyle.get('title', '')}")
                st.caption(lifestyle.get('description', ''))
                
                if "methods" in lifestyle:
                    for method in lifestyle["methods"][:5]:
                        if isinstance(method, dict):
                            st.markdown(f"**{method.get('name', '')}**")
                            if method.get('priority'):
                                st.error(f"{method['priority']}")
                            if method.get('benefit'):
                                st.success(f"Lợi ích: {method['benefit']}")
                            if "activities" in method:
                                for activity in method["activities"]:
                                    st.markdown(f"- {activity}")
                            st.divider()

