"""
Trang tư vấn về bệnh Tim Mạch
"""
import streamlit as st
import sys
sys.path.append('..')

from diseases.cardiovascular import hypertension, heart_failure
from core.utils import classify_blood_pressure
from core.ui_config import get_custom_css

st.set_page_config(page_title="Tim Mạch", page_icon="❤️", layout="wide")

# Áp dụng Dark Mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)

st.title("❤️ Tư vấn Tim Mạch")

# Tabs cho các bệnh tim mạch
tab1, tab2, tab3 = st.tabs(["🩺 Tăng Huyết Áp", "💔 Suy Tim", "📊 Đo Huyết Áp"])

# ============= TAB TĂNG HUYẾT ÁP =============
with tab1:
    st.header("Tăng Huyết Áp (Cao huyết áp)")
    
    # Giới thiệu
    with st.expander("📖 Tăng huyết áp là gì?", expanded=True):
        st.markdown(hypertension.DISEASE_INFO["description_vn"])
        st.info(f"**Phổ biến:** {hypertension.DISEASE_INFO['prevalence_vn']}")
    
    # Triệu chứng
    with st.expander("🔍 Dấu hiệu nhận biết"):
        st.subheader("Triệu chứng thường gặp:")
        for symptom in hypertension.SYMPTOMS["common_vn"]:
            st.markdown(f"- {symptom}")
        
        st.error("**⚠️ TRIỆU CHỨNG NGUY HIỂM - GỌI 115:**")
        for symptom in hypertension.SYMPTOMS["emergency_vn"]:
            st.markdown(f"**{symptom}**")
    
    # Thuốc
    with st.expander("💊 Thuốc điều trị"):
        st.warning(hypertension.MEDICATIONS["overview_vn"])
        
        for drug_key, drug_info in hypertension.MEDICATIONS["drug_classes"].items():
            st.subheader(drug_info["name_vn"])
            st.markdown(f"**Ví dụ:** {', '.join(drug_info['examples_vn'])}")
            st.markdown(f"**Cơ chế:** {drug_info['mechanism_vn']}")
            st.markdown(f"💡 {drug_info['note_vn']}")
            st.divider()
    
    # Chế độ ăn
    with st.expander("🍽️ Chế độ ăn DASH"):
        st.markdown(hypertension.NUTRITION_PLAN["overview_vn"])
        
        col1, col2 = st.columns(2)
        with col1:
            st.success("**✅ NÊN ĂN:**")
            for category, foods in hypertension.NUTRITION_PLAN["recommended_foods"].items():
                if category != "healthy_fats_vn":
                    st.markdown(f"**{category.replace('_vn', '').title()}:**")
                    for food in foods[:3]:  # Chỉ hiển thị 3 món đầu
                        st.markdown(f"- {food}")
        
        with col2:
            st.error("**🚫 TRÁNH:**")
            for category, foods in hypertension.NUTRITION_PLAN["foods_to_avoid"].items():
                for food in foods[:4]:
                    st.markdown(f"{food}")
        
        st.info(hypertension.NUTRITION_PLAN["sodium_limit_vn"])
    
    # Vận động
    with st.expander("🏃 Vận động & Luyện tập"):
        st.markdown(hypertension.EXERCISE_PLAN["overview_vn"])
        
        for exercise_type, details in hypertension.EXERCISE_PLAN["recommended_exercises"].items():
            st.subheader(f"{details['name']}")
            st.markdown(f"**Ví dụ:** {', '.join(details['examples'][:3])}")
            st.markdown(f"**Tần suất:** {details['frequency']}")
            st.markdown(f"**Thời gian:** {details['duration']}")

# ============= TAB SUY TIM =============
with tab2:
    st.header("Suy Tim")
    
    with st.expander("📖 Suy tim là gì?", expanded=True):
        st.markdown(heart_failure.DISEASE_INFO["simple_explanation_vn"])
    
    with st.expander("🚨 5 dấu hiệu chính - 5 chữ H"):
        signs = heart_failure.SYMPTOMS_SIMPLE["main_signs_vn"]
        st.subheader(signs["title"])
        
        for sign in signs["signs"]:
            st.markdown(f"### {sign['letter']}")
            st.markdown(f"**{sign['description']}**")
            for detail in sign['details']:
                st.markdown(detail)
            st.divider()
    
    with st.expander("💊 Thuốc điều trị (giải thích đơn giản)"):
        st.warning(heart_failure.MEDICATIONS_SIMPLE["warning_vn"])
        
        for drug in heart_failure.MEDICATIONS_SIMPLE["common_drugs_simple"][:2]:  # 2 thuốc đầu
            st.subheader(f"{drug['type']}")
            st.caption(drug['street_name'])
            st.markdown(f"**Tác dụng:** {drug['what_it_does']}")
            
            st.markdown("**Lợi ích:**")
            for benefit in drug['benefits']:
                st.markdown(benefit)
    
    with st.expander("🍽️ Chế độ ăn cho người suy tim"):
        st.markdown(heart_failure.NUTRITION_SIMPLE["main_rule_vn"])
        st.info(heart_failure.NUTRITION_SIMPLE["salt_restriction_simple"]["why_vn"])

# ============= TAB ĐO HUYẾT ÁP =============
with tab3:
    st.header("📊 Công cụ đánh giá huyết áp")
    
    st.markdown("Nhập huyết áp của bạn để xem phân loại:")
    
    col1, col2 = st.columns(2)
    with col1:
        systolic = st.number_input(
            "Huyết áp tâm thu (số trên)",
            min_value=70,
            max_value=250,
            value=120,
            step=1
        )
    with col2:
        diastolic = st.number_input(
            "Huyết áp tâm trương (số dưới)",
            min_value=40,
            max_value=150,
            value=80,
            step=1
        )
    
    if st.button("Đánh giá", type="primary"):
        result = classify_blood_pressure(systolic, diastolic)
        
        if result["color"] == "red":
            st.error(f"### {result['name_vn']}")
            st.error(f"**Huyết áp: {systolic}/{diastolic} mmHg**")
            st.error(f"**{result['action_vn']}**")
        elif result["color"] == "orange":
            st.warning(f"### {result['name_vn']}")
            st.warning(f"**Huyết áp: {systolic}/{diastolic} mmHg**")
            st.warning(f"**{result['action_vn']}**")
        elif result["color"] == "yellow":
            st.info(f"### {result['name_vn']}")
            st.info(f"**Huyết áp: {systolic}/{diastolic} mmHg**")
            st.info(f"**{result['action_vn']}**")
        else:
            st.success(f"### {result['name_vn']}")
            st.success(f"**Huyết áp: {systolic}/{diastolic} mmHg**")
            st.success(f"**{result['action_vn']}**")
        
        # Hiển thị bảng phân loại
        st.subheader("Bảng phân loại huyết áp:")
        st.table({
            "Phân loại": ["Bình thường", "Cao bình thường", "THA Độ 1", "THA Độ 2", "Cơn tán"],
            "Tâm thu (mmHg)": ["< 120", "120-129", "130-139", "≥ 140", "≥ 180"],
            "Tâm trương (mmHg)": ["< 80", "< 80", "80-89", "≥ 90", "≥ 120"]
        })

# Nút quay lại
st.divider()
if st.button("⬅️ Quay lại trang chính"):
    st.switch_page("app.py")

