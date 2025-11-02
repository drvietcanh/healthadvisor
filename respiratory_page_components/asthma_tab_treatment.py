"""
Asthma Tab Treatment Functions
Các hàm về điều trị hen suyễn
"""

import streamlit as st
from diseases.respiratory import asthma


def render_asthma_treatment():
    """Render phần điều trị hen suyễn"""
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


def render_asthma_management():
    """Render phần quản lý hen suyễn"""
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

