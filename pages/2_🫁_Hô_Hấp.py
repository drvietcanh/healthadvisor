"""
Trang tư vấn về bệnh Hô Hấp
COPD và Hen Suyễn
"""

import streamlit as st
import sys
sys.path.append('..')

from diseases.respiratory import copd, asthma
from core.ui_config import get_custom_css

st.set_page_config(page_title="Hô Hấp", page_icon="🫁", layout="wide")

# Áp dụng Dark Mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)

st.title("🫁 Tư vấn Hô Hấp")

# Tabs cho các bệnh hô hấp
tab1, tab2 = st.tabs(["🫁 COPD (Phổi Tắc Nghẽn)", "🌬️ Hen Suyễn"])

with tab1:
    st.header("🫁 COPD - Bệnh Phổi Tắc Nghẽn Mạn Tính")
    
    # Thông tin cơ bản
    with st.expander("📖 COPD là gì?", expanded=True):
        if hasattr(copd, 'COPD_INFO') and copd.COPD_INFO:
            info_dict = copd.COPD_INFO
            if isinstance(info_dict, dict):
                st.markdown(info_dict.get("what_is_it", info_dict.get("simple_explanation", "")))
                if info_dict.get("why_dangerous"):
                    st.warning(info_dict.get("why_dangerous"))
    
    # Nguyên nhân
    with st.expander("🔍 Nguyên nhân COPD"):
        if hasattr(copd, 'CAUSES') and copd.CAUSES:
            if isinstance(copd.CAUSES, dict):
                for cause_key, cause_info in list(copd.CAUSES.items())[:5]:
                    if isinstance(cause_info, dict):
                        st.markdown(f"**{cause_info.get('name', cause_key)}**")
                        st.caption(cause_info.get('description', ''))
                        st.divider()
    
    # Triệu chứng
    with st.expander("🩺 Triệu chứng COPD", expanded=True):
        if hasattr(copd, 'SYMPTOMS') and copd.SYMPTOMS:
            symptoms_dict = copd.SYMPTOMS
            
            # 1. Triệu chứng chính
            if "main_symptoms" in symptoms_dict:
                main = symptoms_dict["main_symptoms"]
                st.subheader(f"{main.get('title', '🔍 Triệu Chứng Chính')}")
                if "symptoms" in main:
                    for symptom in main["symptoms"]:
                        if isinstance(symptom, dict):
                            st.markdown(f"### {symptom.get('icon', '')} {symptom.get('name', '')}")
                            if "details" in symptom:
                                for detail in symptom["details"]:
                                    st.markdown(f"- {detail}")
                            if "progression" in symptom:
                                st.info(f"💡 {symptom['progression']}")
                            if "note" in symptom:
                                st.caption(f"⚠️ {symptom['note']}")
                            st.divider()
            
            # 2. Dấu hiệu sớm
            if "early_warning_signs" in symptoms_dict:
                early = symptoms_dict["early_warning_signs"]
                st.subheader(f"{early.get('title', '⚠️ Dấu Hiệu Sớm')}")
                if "signs" in early:
                    for sign in early["signs"]:
                        st.markdown(f"- {sign}")
                if "action" in early:
                    st.warning(early["action"])
                st.divider()
            
            # 3. Triệu chứng nặng
            if "severe_symptoms" in symptoms_dict:
                severe = symptoms_dict["severe_symptoms"]
                st.error(f"### {severe.get('title', '🚨 Triệu Chứng NẶNG')}")
                if "symptoms" in severe:
                    for symptom in severe["symptoms"]:
                        st.markdown(f"- {symptom}")
                if "action" in severe:
                    st.error(f"**{severe['action']}**")
                st.divider()
            
            # 4. Yếu tố kích phát đợt cấp
            if "exacerbation_triggers" in symptoms_dict:
                triggers = symptoms_dict["exacerbation_triggers"]
                st.subheader(f"{triggers.get('title', '🔥 Yếu Tố Kích Phát')}")
                if "triggers" in triggers:
                    st.markdown("**Các yếu tố khiến bệnh nặng lên:**")
                    for trigger in triggers["triggers"]:
                        st.markdown(f"- {trigger}")
                if "prevention" in triggers:
                    st.success("**Cách phòng ngừa:**")
                    for prev in triggers["prevention"]:
                        st.markdown(f"- {prev}")
    
    # Điều trị
    with st.expander("💊 Điều trị COPD"):
        st.markdown("### Nguyên tắc điều trị")
        if hasattr(copd, 'TREATMENT_PRINCIPLES') and copd.TREATMENT_PRINCIPLES:
            principles = copd.TREATMENT_PRINCIPLES
            if isinstance(principles, dict):
                st.markdown(principles.get("overview", ""))
        
        st.markdown("### Thuốc giãn phế quản")
        if hasattr(copd, 'BRONCHODILATORS') and copd.BRONCHODILATORS:
            for med_key, med_info in list(copd.BRONCHODILATORS.items())[:3]:
                if isinstance(med_info, dict):
                    st.markdown(f"**{med_info.get('name', med_key)}**")
                    st.caption(med_info.get('description', ''))
    
    # Vận động và tập luyện
    with st.expander("🏃 Vận động & Tập luyện"):
        if hasattr(copd, 'EXERCISE_BENEFITS') and copd.EXERCISE_BENEFITS:
            benefits = copd.EXERCISE_BENEFITS
            if isinstance(benefits, dict):
                st.markdown(benefits.get("overview", ""))
        
        st.markdown("### Kỹ thuật thở")
        if hasattr(copd, 'BREATHING_TECHNIQUES') and copd.BREATHING_TECHNIQUES:
            techniques = copd.BREATHING_TECHNIQUES
            if isinstance(techniques, dict):
                for tech_key, tech_info in list(techniques.items())[:2]:
                    if isinstance(tech_info, dict):
                        st.markdown(f"**{tech_info.get('name', tech_key)}**")
                        st.caption(tech_info.get('description', ''))
    
    # Quản lý COPD
    with st.expander("🛡️ Quản lý COPD", expanded=True):
        # Bỏ thuốc lá
        if hasattr(copd, 'SMOKING_CESSATION') and copd.SMOKING_CESSATION:
            st.subheader("🚭 Bỏ Thuốc Lá - QUAN TRỌNG NHẤT!")
            smoking = copd.SMOKING_CESSATION
            st.markdown(smoking.get("importance", ""))
            if "benefits_timeline" in smoking:
                st.markdown("### Lợi ích theo thời gian:")
                for benefit_item in smoking["benefits_timeline"][:4]:
                    if isinstance(benefit_item, dict):
                        st.markdown(f"**{benefit_item.get('time', '')}:** {benefit_item.get('benefit', '')}")
            if "methods" in smoking:
                st.markdown("### Phương pháp bỏ thuốc:")
                for method in smoking["methods"][:2]:
                    if isinstance(method, dict):
                        st.markdown(f"**{method.get('method', '')}** - Tỷ lệ thành công: {method.get('success_rate', '')}")
            st.divider()
        
        # Phục hồi chức năng phổi
        if hasattr(copd, 'PULMONARY_REHABILITATION') and copd.PULMONARY_REHABILITATION:
            st.subheader("🏃 Phục Hồi Chức Năng Phổi")
            rehab = copd.PULMONARY_REHABILITATION
            st.markdown(rehab.get("what_is_it", ""))
            if "benefits" in rehab:
                st.markdown("### Lợi ích:")
                for benefit in rehab["benefits"][:4]:
                    st.markdown(f"- {benefit}")
            if "home_program" in rehab:
                home = rehab["home_program"]
                st.markdown(f"### {home.get('title', 'Chương trình tại nhà:')}")
                for exercise in home.get("exercises", [])[:4]:
                    st.markdown(f"- {exercise}")
            st.divider()
        
        # Dinh dưỡng
        if hasattr(copd, 'NUTRITION') and copd.NUTRITION:
            st.subheader("🍽️ Dinh Dưỡng")
            nutrition = copd.NUTRITION
            st.warning(nutrition.get("importance", ""))
            if "recommendations" in nutrition:
                for rec in nutrition["recommendations"][:3]:
                    if isinstance(rec, dict):
                        st.markdown(f"**{rec.get('principle', '')}**")
                        st.caption(f"{rec.get('reason', '')}")
                        st.markdown(f"→ {rec.get('advice', rec.get('target', ''))}")
            st.divider()
        
        # Vắc-xin
        if hasattr(copd, 'VACCINATION') and copd.VACCINATION:
            st.subheader("💉 Vắc-xin Phòng Đợt Cấp")
            vacc = copd.VACCINATION
            if "influenza_vaccine" in vacc:
                flu = vacc["influenza_vaccine"]
                st.markdown(f"**{flu.get('name', '')}** - {flu.get('frequency', '')}")
                st.caption(f"Lợi ích: {flu.get('benefit', '')} | Giá: {flu.get('price', '')}")
            if "pneumococcal_vaccine" in vacc:
                pneumo = vacc["pneumococcal_vaccine"]
                st.markdown(f"**{pneumo.get('name', '')}**")
                if "types" in pneumo:
                    for vax_type in pneumo["types"][:1]:
                        st.caption(f"{vax_type.get('type', '')} - Giá: {vax_type.get('price', '')}")
            st.divider()
        
        # Xử trí đợt cấp
        if hasattr(copd, 'EXACERBATION_MANAGEMENT') and copd.EXACERBATION_MANAGEMENT:
            st.subheader("🚨 Xử Trí Đợt Cấp")
            exac = copd.EXACERBATION_MANAGEMENT
            st.markdown(exac.get("what_is_exacerbation", ""))
            if "warning_signs" in exac:
                st.markdown("### Dấu hiệu cảnh báo:")
                for sign in exac["warning_signs"][:4]:
                    st.markdown(f"- {sign}")
            if "action_plan" in exac:
                plan = exac["action_plan"]
                for zone_key in ["green_zone", "yellow_zone", "red_zone"]:
                    if zone_key in plan:
                        zone = plan[zone_key]
                        st.markdown(f"### {zone.get('name', '')}")
                        if isinstance(zone.get("signs"), list):
                            for sign in zone.get("signs", [])[:2]:
                                st.markdown(f"- {sign}")
                        else:
                            st.markdown(f"- {zone.get('signs', '')}")
                        if "action" in zone:
                            if isinstance(zone["action"], list):
                                for act in zone["action"][:3]:
                                    st.markdown(f"- {act}")
                            else:
                                st.markdown(f"- {zone['action']}")
                        st.divider()

with tab2:
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
    with st.expander("⚠️ Yếu tố kích phát"):
        if hasattr(asthma, 'TRIGGERS') and asthma.TRIGGERS:
            triggers = asthma.TRIGGERS
            if isinstance(triggers, dict):
                for trigger_key, trigger_info in list(triggers.items())[:5]:
                    if isinstance(trigger_info, dict):
                        st.markdown(f"**{trigger_info.get('name', trigger_key)}**")
                        st.caption(trigger_info.get('description', ''))
                        st.divider()
    
    # Phân loại mức độ
    with st.expander("📊 Phân loại mức độ hen suyễn"):
        if hasattr(asthma, 'SEVERITY_CLASSIFICATION') and asthma.SEVERITY_CLASSIFICATION:
            severity = asthma.SEVERITY_CLASSIFICATION
            if isinstance(severity, dict):
                for severity_key, severity_info in severity.items():
                    if isinstance(severity_info, dict):
                        st.markdown(f"**{severity_info.get('name', severity_key)}**")
                        st.caption(severity_info.get('description', ''))
                        st.divider()
    
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

# Nút quay lại
st.divider()
if st.button("🏠 Về Trang Chủ"):
    st.switch_page("app.py")

