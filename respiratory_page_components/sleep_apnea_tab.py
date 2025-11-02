"""Sleep Apnea Tab Component"""

import streamlit as st
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

from diseases.respiratory.sleep_apnea import SLEEP_APNEA_INFO, SYMPTOMS, TREATMENT

def render_sleep_apnea_tab():
    """Render tab Ngưng Thở Khi Ngủ"""
    st.header("😴 Ngưng Thở Khi Ngủ (Sleep Apnea)")
    
    st.error("⚠️ **NGUY HIỂM:** Ngưng thở khi ngủ làm tăng nguy cơ đột quỵ, tim mạch 2-4 lần!")
    
    with st.expander("📖 Ngưng thở khi ngủ là gì?", expanded=True):
        if SLEEP_APNEA_INFO:
            st.markdown(SLEEP_APNEA_INFO.get("simple_explanation", ""))
            if SLEEP_APNEA_INFO.get("why_important"):
                st.warning(SLEEP_APNEA_INFO["why_important"])
            if "statistics" in SLEEP_APNEA_INFO:
                stats = SLEEP_APNEA_INFO["statistics"]
                st.info(f"📊 **Thống kê:** {stats.get('prevalence', '')}")
    
    with st.expander("🔍 Triệu chứng"):
        if SYMPTOMS:
            col1, col2 = st.columns(2)
            with col1:
                if "nighttime" in SYMPTOMS:
                    st.markdown(f"### {SYMPTOMS['nighttime']['title']}")
                    for s in SYMPTOMS["nighttime"]["symptoms"]:
                        st.markdown(f"- {s}")
                    if SYMPTOMS["nighttime"].get("note"):
                        st.info(SYMPTOMS["nighttime"]["note"])
            with col2:
                if "daytime" in SYMPTOMS:
                    st.markdown(f"### {SYMPTOMS['daytime']['title']}")
                    for s in SYMPTOMS["daytime"]["symptoms"]:
                        st.markdown(f"- {s}")
            
            if "risk_factors" in SYMPTOMS:
                st.divider()
                st.markdown(f"### {SYMPTOMS['risk_factors']['title']}")
                for factor in SYMPTOMS["risk_factors"]["factors"]:
                    st.markdown(f"- {factor}")
    
    with st.expander("💊 Điều trị"):
        if TREATMENT:
            if "cpap" in TREATMENT:
                st.markdown(f"### {TREATMENT['cpap']['title']}")
                st.caption(f"**Cách hoạt động:** {TREATMENT['cpap']['how_it_works']}")
                st.markdown("**Lợi ích:**")
                for benefit in TREATMENT["cpap"].get("benefits", []):
                    st.markdown(benefit)
                if TREATMENT["cpap"].get("note"):
                    st.warning(TREATMENT["cpap"]["note"])
            
            if "lifestyle" in TREATMENT:
                st.divider()
                st.markdown(f"### {TREATMENT['lifestyle']['title']}")
                lifestyle = TREATMENT["lifestyle"]
                if "weight_loss" in lifestyle:
                    st.markdown(f"**{lifestyle['weight_loss']['title']}**")
                    st.caption(lifestyle["weight_loss"]["benefit"])
                    st.caption(lifestyle["weight_loss"]["how"])
    
    with st.expander("🏥 Khi nào cần khám bác sĩ"):
        if SYMPTOMS and "when_to_see_doctor" in SYMPTOMS:
            doctor = SYMPTOMS["when_to_see_doctor"]
            st.error("**🚨 KHẨN CẤP:**")
            for item in doctor.get("urgent", []):
                st.markdown(f"- {item}")
            if doctor.get("note"):
                st.warning(doctor["note"])

