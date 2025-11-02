"""
Asthma Tab Helper Functions
Các hàm helper cho asthma_tab
"""

import streamlit as st
from diseases.respiratory import asthma


def render_asthma_info_and_symptoms():
    """Render thông tin cơ bản, nguyên nhân và triệu chứng"""
    # Thông tin cơ bản
    with st.expander("📖 Hen suyễn là gì?", expanded=True):
        if hasattr(asthma, 'ASTHMA_INFO') and asthma.ASTHMA_INFO:
            info_dict = asthma.ASTHMA_INFO
            if isinstance(info_dict, dict):
                st.markdown(info_dict.get("simple_explanation", info_dict.get("what_is_it", "")))
                if info_dict.get("what_happens"):
                    what_happens = info_dict.get("what_happens", {})
                    if isinstance(what_happens, dict):
                        st.markdown(f"### {what_happens.get('title', '')}")
                        mechanisms = what_happens.get("mechanisms", [])
                        for mech in mechanisms[:3]:
                            if isinstance(mech, dict):
                                st.markdown(f"**{mech.get('step', '')}**")
                                st.caption(f"{mech.get('analogy', '')} → {mech.get('result', '')}")
    
    # Nguyên nhân
    with st.expander("🔍 Nguyên nhân hen suyễn"):
        if hasattr(asthma, 'CAUSES') and asthma.CAUSES:
            causes = asthma.CAUSES
            if isinstance(causes, dict):
                for cause_key, cause_info in list(causes.items())[:5]:
                    if isinstance(cause_info, dict):
                        st.markdown(f"**{cause_info.get('name', cause_key)}**")
                        st.caption(cause_info.get('description', ''))
                        st.divider()
    
    # Triệu chứng
    with st.expander("🩺 Triệu chứng hen suyễn", expanded=True):
        if hasattr(asthma, 'SYMPTOMS') and asthma.SYMPTOMS:
            symptoms_dict = asthma.SYMPTOMS
            
            # 1. Triệu chứng chính
            if "main_symptoms" in symptoms_dict:
                main = symptoms_dict["main_symptoms"]
                st.subheader(f"{main.get('title', '🔍 Triệu Chứng Chính')}")
                if "symptoms" in main:
                    for symptom in main["symptoms"]:
                        if isinstance(symptom, dict):
                            st.markdown(f"### {symptom.get('icon', '')} {symptom.get('name', '')}")
                            if "description" in symptom:
                                st.markdown(f"*{symptom['description']}*")
                            if "characteristics" in symptom:
                                st.markdown("**Đặc điểm:**")
                                for char in symptom["characteristics"]:
                                    st.markdown(f"- {char}")
                            if "details" in symptom:
                                st.markdown("**Chi tiết:**")
                                for detail in symptom["details"]:
                                    st.markdown(f"- {detail}")
                            if "patterns" in symptom:
                                st.markdown("**Kiểu ho:**")
                                for pattern in symptom["patterns"]:
                                    st.markdown(f"- {pattern}")
                            if "feelings" in symptom:
                                st.markdown("**Cảm giác:**")
                                for feeling in symptom["feelings"]:
                                    st.markdown(f"- {feeling}")
                            if "key" in symptom:
                                st.success(symptom["key"])
                            if "note" in symptom:
                                st.info(symptom["note"])
                            if "common_mistake" in symptom:
                                st.warning(f"⚠️ {symptom['common_mistake']}")
                            st.divider()
            
            # 2. Khi nào hay hen
            if "timing_patterns" in symptoms_dict:
                timing = symptoms_dict["timing_patterns"]
                st.subheader(f"{timing.get('title', '⏰ Khi Nào Hay Hen?')}")
                if "patterns" in timing:
                    for pattern in timing["patterns"]:
                        if isinstance(pattern, dict):
                            st.markdown(f"**{pattern.get('time', '')}**")
                            if "reason" in pattern:
                                st.caption(f"Lý do: {pattern['reason']}")
                            if "examples" in pattern:
                                st.markdown("Ví dụ:")
                                for ex in pattern["examples"]:
                                    st.markdown(f"- {ex}")
                            if "triggers" in pattern:
                                st.markdown("Yếu tố:")
                                for trigger in pattern["triggers"]:
                                    st.markdown(f"- {trigger}")
                            if "tip" in pattern:
                                st.info(f"💡 {pattern['tip']}")
                            if "note" in pattern:
                                st.caption(pattern["note"])
                            st.divider()
            
            # 3. Cơn hen nặng
            if "severe_attack_signs" in symptoms_dict:
                severe = symptoms_dict["severe_attack_signs"]
                st.error(f"### {severe.get('title', '🚨 Cơn Hen NẶNG')}")
                if "danger_signs" in severe:
                    for sign in severe["danger_signs"]:
                        st.markdown(f"- {sign}")
                if "action" in severe:
                    st.error(f"**{severe['action']}**")
                if "while_waiting" in severe:
                    st.warning("**Trong lúc chờ xe cấp cứu:**")
                    for step in severe["while_waiting"]:
                        st.markdown(f"- {step}")
                st.divider()
            
            # 4. Triệu chứng ở trẻ em
            if "children_specific" in symptoms_dict:
                children = symptoms_dict["children_specific"]
                st.subheader(f"{children.get('title', '👶 Triệu Chứng Ở Trẻ Em')}")
                if "signs" in children:
                    for sign in children["signs"]:
                        st.markdown(f"- {sign}")
                if "note" in children:
                    st.warning(children["note"])


def render_asthma_triggers_and_severity():
    """Render yếu tố kích phát và phân loại mức độ"""
    # Yếu tố kích phát
    with st.expander("⚠️ Yếu tố kích phát", expanded=True):
        if hasattr(asthma, 'TRIGGERS') and asthma.TRIGGERS:
            triggers = asthma.TRIGGERS
            st.markdown(f"### {triggers.get('title', 'Yếu tố kích phát')}")
            st.info(triggers.get('description', ''))
            
            if "allergens" in triggers:
                allergens = triggers["allergens"]
                st.markdown(f"#### {allergens.get('name', 'Dị Nguyên')}")
                if "items" in allergens:
                    for item in allergens["items"][:3]:
                        st.markdown(f"**{item.get('trigger', '')}**")
                        if "how_to_avoid" in item:
                            st.markdown("**Cách tránh:**")
                            for method in item["how_to_avoid"][:3]:
                                st.markdown(f"- {method}")
                        st.divider()
            
            if "irritants" in triggers:
                irritants = triggers["irritants"]
                st.markdown(f"#### {irritants.get('name', 'Chất Kích Thích')}")
                if "items" in irritants:
                    for item in irritants["items"][:3]:
                        st.markdown(f"**{item.get('trigger', '')}**")
                        if item.get('danger'):
                            st.error(item['danger'])
                        if "how_to_avoid" in item:
                            st.markdown("**Cách tránh:**")
                            for method in item["how_to_avoid"][:2]:
                                st.markdown(f"- {method}")
                        if item.get('action'):
                            st.warning(item['action'])
                        st.divider()
            
            if "weather" in triggers:
                weather = triggers["weather"]
                st.markdown(f"#### {weather.get('name', 'Thời Tiết')}")
                if "triggers" in weather:
                    for trigger in weather["triggers"][:2]:
                        st.markdown(f"**{trigger.get('condition', '')}**")
                        if trigger.get('when'):
                            st.caption(f"Khi: {trigger['when']}")
                        if "how_to_avoid" in trigger:
                            st.markdown("**Cách tránh:**")
                            for method in trigger["how_to_avoid"][:2]:
                                st.markdown(f"- {method}")
                        st.divider()
    
    # Phân loại mức độ
    with st.expander("📊 Phân loại mức độ hen suyễn", expanded=True):
        if hasattr(asthma, 'SEVERITY_CLASSIFICATION') and asthma.SEVERITY_CLASSIFICATION:
            severity = asthma.SEVERITY_CLASSIFICATION
            st.markdown(f"### {severity.get('title', 'Phân Loại Mức Độ Hen')}")
            
            if "intermittent" in severity:
                s = severity["intermittent"]
                st.markdown(f"#### {s.get('icon', '🟢')} {s.get('name', '')}")
                st.markdown(f"**Tần suất triệu chứng:** {s.get('symptoms_frequency', '')}")
                st.markdown(f"**Ban đêm:** {s.get('nighttime', '')}")
                st.markdown(f"**Ảnh hưởng:** {s.get('daily_life', '')}")
                st.caption(f"💡 Ví dụ: {s.get('example', '')}")
                st.divider()
            
            if "mild_persistent" in severity:
                s = severity["mild_persistent"]
                st.markdown(f"#### {s.get('icon', '🟡')} {s.get('name', '')}")
                st.markdown(f"**Tần suất triệu chứng:** {s.get('symptoms_frequency', '')}")
                st.markdown(f"**Ban đêm:** {s.get('nighttime', '')}")
                st.markdown(f"**Ảnh hưởng:** {s.get('daily_life', '')}")
                st.caption(f"💡 Ví dụ: {s.get('example', '')}")
                st.divider()
            
            if "moderate_persistent" in severity:
                s = severity["moderate_persistent"]
                st.markdown(f"#### {s.get('icon', '🟠')} {s.get('name', '')}")
                st.markdown(f"**Tần suất triệu chứng:** {s.get('symptoms_frequency', '')}")
                st.markdown(f"**Ban đêm:** {s.get('nighttime', '')}")
                st.markdown(f"**Ảnh hưởng:** {s.get('daily_life', '')}")
                st.caption(f"💡 Ví dụ: {s.get('example', '')}")
                st.divider()
            
            if "severe_persistent" in severity:
                s = severity["severe_persistent"]
                st.error(f"#### {s.get('icon', '🔴')} {s.get('name', '')}")
                st.markdown(f"**Tần suất triệu chứng:** {s.get('symptoms_frequency', '')}")
                st.markdown(f"**Ban đêm:** {s.get('nighttime', '')}")
                st.markdown(f"**Ảnh hưởng:** {s.get('daily_life', '')}")
                st.caption(f"💡 Ví dụ: {s.get('example', '')}")

