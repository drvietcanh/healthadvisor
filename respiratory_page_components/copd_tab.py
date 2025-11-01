"""
COPD Tab Component
Hiển thị thông tin về bệnh COPD
"""

import streamlit as st
import sys
sys.path.append('..')
from diseases.respiratory import copd


def render_copd_tab():
    """Render tab COPD với đầy đủ thông tin"""
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
    with st.expander("💊 Điều trị COPD", expanded=True):
        st.markdown("### Nguyên tắc điều trị")
        if hasattr(copd, 'TREATMENT_PRINCIPLES') and copd.TREATMENT_PRINCIPLES:
            principles = copd.TREATMENT_PRINCIPLES
            if isinstance(principles, dict):
                st.markdown(principles.get("overview", ""))
        
        # Thuốc giãn phế quản - Chi tiết
        if hasattr(copd, 'BRONCHODILATORS') and copd.BRONCHODILATORS:
            st.markdown("### Thuốc giãn phế quản")
            bronchodilators = copd.BRONCHODILATORS
            st.markdown(bronchodilators.get("simple_explanation", ""))
            
            # Thuốc ngắn hạn
            if "short_acting" in bronchodilators:
                st.markdown("#### ⚡ Thuốc Ngắn Hạn (Dùng KHI CẦN)")
                short = bronchodilators["short_acting"]
                st.info(f"**{short.get('name', '')}** - {short.get('use', '')}")
                
                if "saba" in short:
                    saba = short["saba"]
                    st.markdown(f"**{saba.get('name', '')}:**")
                    if "examples_vietnam" in saba:
                        for ex in saba["examples_vietnam"][:2]:
                            st.markdown(f"- **{ex.get('name', '')}** ({ex.get('brand', '')})")
                            st.caption(f"  → Liều: {ex.get('dose', '')} | Tác dụng: {ex.get('onset', '')} - {ex.get('duration', '')}")
                            st.caption(f"  → Giá: {ex.get('price', '')}")
                
                if "when_to_use" in short:
                    st.markdown("**Khi nào dùng:**")
                    for when in short["when_to_use"][:4]:
                        st.markdown(f"- {when}")
                if "warning" in short:
                    st.warning(short["warning"])
                st.divider()
            
            # Thuốc dài hạn
            if "long_acting" in bronchodilators:
                st.markdown("#### 🛡️ Thuốc Dài Hạn (Dùng HÀNG NGÀY)")
                long_act = bronchodilators["long_acting"]
                st.info(f"**{long_act.get('name', '')}** - {long_act.get('use', '')}")
                
                if "lama" in long_act:
                    lama = long_act["lama"]
                    st.markdown(f"**{lama.get('name', '')}:**")
                    if "examples_vietnam" in lama:
                        for ex in lama["examples_vietnam"][:2]:
                            st.markdown(f"- **{ex.get('name', '')}** ({ex.get('brand', '')})")
                            st.caption(f"  → Liều: {ex.get('dose', '')} | Tác dụng: {ex.get('duration', '')}")
                            st.caption(f"  → Giá: {ex.get('price', '')}")
                            if ex.get('note'):
                                st.success(f"💡 {ex['note']}")
    
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
                # Thở môi
                if "pursed_lip" in techniques:
                    tech = techniques["pursed_lip"]
                    st.markdown(f"**{tech.get('name', 'Thở Môi')}**")
                    st.caption(tech.get('when', ''))
                    if "how" in tech:
                        st.markdown("**Cách tập:**")
                        for step in tech["how"][:5]:
                            st.markdown(f"- {step}")
                    if "benefit" in tech:
                        st.success("**Lợi ích:** " + " | ".join(tech["benefit"][:3]))
                    st.caption(f"💡 {tech.get('practice', '')}")
                    st.divider()
                
                # Thở bụng
                if "diaphragmatic_breathing" in techniques:
                    tech = techniques["diaphragmatic_breathing"]
                    st.markdown(f"**{tech.get('name', 'Thở Bụng')}**")
                    st.caption(tech.get('when', ''))
                    if "how" in tech:
                        st.markdown("**Cách tập:**")
                        for step in tech["how"][:5]:
                            st.markdown(f"- {step}")
                    if "benefit" in tech:
                        st.success("**Lợi ích:** " + " | ".join(tech["benefit"][:3]))
                    st.caption(f"💡 {tech.get('practice', '')}")
    
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

