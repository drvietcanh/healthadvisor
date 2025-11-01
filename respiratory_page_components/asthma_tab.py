"""
Asthma Tab Component
Hiển thị thông tin về bệnh Hen Suyễn
"""

import streamlit as st
import sys
sys.path.append('..')
from diseases.respiratory import asthma


def render_asthma_tab():
    """Render tab Asthma với đầy đủ thông tin"""
    st.header("🌬️ Hen Suyễn (Asthma)")
    
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
    
    # Điều trị
    with st.expander("💊 Điều trị hen suyễn", expanded=True):
        # Thuốc cắt cơn
        if hasattr(asthma, 'QUICK_RELIEF_MEDICATIONS') and asthma.QUICK_RELIEF_MEDICATIONS:
            st.subheader("⚡ Thuốc Cắt Cơn (Cấp Cứu)")
            relief = asthma.QUICK_RELIEF_MEDICATIONS
            st.markdown(relief.get("description", ""))
            if "salbutamol" in relief:
                sal = relief["salbutamol"]
                st.markdown(f"### {sal.get('name', 'Salbutamol')}")
                st.caption(sal.get('how_it_works', ''))
                st.markdown(f"**Tác dụng:** {sal.get('onset', '')} - {sal.get('duration', '')}")
                st.markdown("**Khi nào dùng:**")
                for when in sal.get("when_to_use", []):
                    st.markdown(f"- {when}")
                st.markdown(f"**Liều:** {sal.get('dosage', {}).get('adult', '')}")
                st.divider()
        
        # Thuốc kiểm soát
        if hasattr(asthma, 'CONTROLLER_MEDICATIONS') and asthma.CONTROLLER_MEDICATIONS:
            st.subheader("🛡️ Thuốc Kiểm Soát (Dự Phòng)")
            controller = asthma.CONTROLLER_MEDICATIONS
            st.markdown(controller.get("description", ""))
            
            if "ics" in controller:
                ics = controller["ics"]
                st.markdown(f"### {ics.get('title', '')}")
                st.caption(ics.get('description', ''))
                if "medications" in ics:
                    for med in ics["medications"][:2]:
                        st.markdown(f"**{med.get('name', '')}** - {med.get('dose', '')}")
                        st.caption(f"Giá: {med.get('price', '')}")
                st.markdown("**Tác dụng phụ:**")
                for se in ics.get("side_effects", [])[:3]:
                    st.markdown(f"- {se}")
                st.divider()
        
        # Kỹ thuật xịt thuốc
        if hasattr(asthma, 'INHALER_TECHNIQUE') and asthma.INHALER_TECHNIQUE:
            st.subheader("🎯 Cách Xịt Thuốc Đúng")
            technique = asthma.INHALER_TECHNIQUE
            st.warning(technique.get("importance", ""))
            if "steps" in technique:
                for step_info in technique["steps"]:
                    st.markdown(f"**Bước {step_info.get('step', '')}:** {step_info.get('action', '')}")
                    if step_info.get('note'):
                        st.caption(step_info['note'])
            st.divider()
        
        # Kế hoạch hành động
        if hasattr(asthma, 'ACTION_PLAN') and asthma.ACTION_PLAN:
            st.subheader("📋 Kế Hoạch Hành Động")
            plan = asthma.ACTION_PLAN
            for zone_key in ["green_zone", "yellow_zone", "red_zone"]:
                if zone_key in plan:
                    zone = plan[zone_key]
                    st.markdown(f"### {zone.get('name', '')}")
                    if "signs" in zone:
                        for sign in zone["signs"]:
                            st.markdown(f"- {sign}")
                    if "action" in zone:
                        if isinstance(zone["action"], list):
                            for act in zone["action"]:
                                st.markdown(f"- {act}")
                        else:
                            st.markdown(f"- {zone['action']}")
                    st.divider()
    
    # Quản lý
    with st.expander("🛡️ Quản lý hen suyễn", expanded=True):
        # Phòng ngừa
        if hasattr(asthma, 'PREVENTION') and asthma.PREVENTION:
            prevention = asthma.PREVENTION
            st.subheader("🛡️ Phòng Ngừa Đợt Cấp")
            
            if "avoid_triggers" in prevention:
                triggers_section = prevention["avoid_triggers"]
                st.markdown(f"**{triggers_section.get('title', 'Tránh Yếu Tố Kích Phát')}**")
                for method in triggers_section.get("methods", [])[:6]:
                    st.markdown(f"- {method}")
            
            if "regular_medication" in prevention:
                med_section = prevention["regular_medication"]
                st.markdown(f"**{med_section.get('title', '')}**")
                st.info(med_section.get("importance", ""))
                if "tips" in med_section:
                    for tip in med_section["tips"][:4]:
                        st.markdown(f"- {tip}")
            
            if "vaccination" in prevention:
                vacc_section = prevention["vaccination"]
                st.markdown(f"### {vacc_section.get('title', '💉 Vắc-xin')}")
                if "influenza" in vacc_section:
                    flu = vacc_section["influenza"]
                    st.markdown(f"**{flu.get('vaccine', '')}** - {flu.get('frequency', '')}")
                    st.caption(f"Lợi ích: {flu.get('benefit', '')} | Giá: {flu.get('price', '')}")
            st.divider()
        
        # Theo dõi tại nhà
        if hasattr(asthma, 'HOME_MONITORING') and asthma.HOME_MONITORING:
            st.subheader("📊 Theo Dõi Tại Nhà")
            monitoring = asthma.HOME_MONITORING
            
            if "peak_flow_meter" in monitoring:
                peak_flow = monitoring["peak_flow_meter"]
                st.markdown(f"### {peak_flow.get('title', '')}")
                st.caption(peak_flow.get('what_is_it', ''))
                if "benefit" in peak_flow:
                    st.markdown("**Lợi ích:**")
                    for benefit in peak_flow["benefit"][:3]:
                        st.markdown(f"- {benefit}")
                if "zones" in peak_flow:
                    zones = peak_flow["zones"]
                    st.markdown("**Vùng:**")
                    st.success(f"🟢 {zones.get('green', '')}")
                    st.warning(f"🟡 {zones.get('yellow', '')}")
                    st.error(f"🔴 {zones.get('red', '')}")
            
            if "symptom_diary" in monitoring:
                diary = monitoring["symptom_diary"]
                st.markdown(f"### {diary.get('title', '📝 Nhật Ký Triệu Chứng')}")
                st.markdown("**Ghi lại:**")
                for item in diary.get("what_to_record", [])[:5]:
                    st.markdown(f"- {item}")
            st.divider()
        
        # Lối sống
        if hasattr(asthma, 'LIFESTYLE') and asthma.LIFESTYLE:
            lifestyle = asthma.LIFESTYLE
            st.subheader("🏃 Lối Sống Tốt Cho Hen Suyễn")
            
            if "exercise" in lifestyle:
                ex = lifestyle["exercise"]
                st.markdown(f"### {ex.get('title', 'Tập Thể Dục')}")
                st.info(ex.get('benefit', ''))
                st.markdown("**Khuyến nghị:**")
                for rec in ex.get("recommended", [])[:4]:
                    st.markdown(f"- {rec}")
                st.markdown("**Lưu ý:**")
                for prec in ex.get("precautions", [])[:3]:
                    st.markdown(f"- {prec}")
            
            if "diet" in lifestyle:
                diet = lifestyle["diet"]
                st.markdown(f"### {diet.get('title', 'Chế Độ Ăn')}")
                st.markdown("**Nên ăn:**")
                for food in diet.get("foods_to_eat", [])[:4]:
                    st.markdown(f"- {food}")
                st.markdown("**Nên tránh:**")
                for food in diet.get("foods_to_avoid", [])[:3]:
                    st.markdown(f"- {food}")
            st.divider()
        
        # Xử trí đợt cấp
        if hasattr(asthma, 'EXACERBATION_MANAGEMENT') and asthma.EXACERBATION_MANAGEMENT:
            st.subheader("🚨 Xử Trí Đợt Cấp")
            exac = asthma.EXACERBATION_MANAGEMENT
            
            if "mild_moderate" in exac:
                mild = exac["mild_moderate"]
                st.markdown(f"### {mild.get('title', 'Cơn Hen Nhẹ → Vừa')}")
                st.markdown("**Dấu hiệu:**")
                for sign in mild.get("signs", [])[:4]:
                    st.markdown(f"- {sign}")
                st.markdown("**Xử lý:**")
                for action in mild.get("action", [])[:5]:
                    st.markdown(f"- {action}")
                st.divider()
            
            if "severe" in exac:
                severe = exac["severe"]
                st.error(f"### {severe.get('title', 'Cơn Hen Nặng')}")
                st.markdown("**Dấu hiệu:**")
                for sign in severe.get("signs", [])[:5]:
                    st.markdown(f"- {sign}")
                st.markdown("**Xử lý:**")
                for action in severe.get("action", [])[:6]:
                    st.markdown(f"- {action}")
                if "while_waiting" in severe:
                    st.warning("**Trong lúc chờ xe cấp cứu:**")
                    for step in severe["while_waiting"][:4]:
                        st.markdown(f"- {step}")

