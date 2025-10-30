"""
Trang tư vấn về bệnh Tim Mạch
"""
import streamlit as st
import sys
sys.path.append('..')

from diseases.cardiovascular import hypertension, heart_failure
from diseases.metabolic import dyslipidemia
from core.utils import classify_blood_pressure
from core.ui_config import get_custom_css

st.set_page_config(page_title="Tim Mạch", page_icon="❤️", layout="wide")

# Áp dụng Dark Mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)

st.title("❤️ Tư vấn Tim Mạch")

# Tabs cho các bệnh tim mạch
tab1, tab2, tab3, tab4 = st.tabs(["🩺 Tăng Huyết Áp", "💔 Suy Tim", "🧈 Rối Loạn Lipid Máu", "📊 Đo Huyết Áp"])

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

# ============= TAB RỐI LOẠN LIPID MÁU =============
with tab3:
    st.header("🧈 Rối Loạn Lipid Máu (Cholesterol & Triglyceride)")
    
    # Giới thiệu
    with st.expander("📖 Rối loạn lipid máu là gì?", expanded=True):
        st.markdown(dyslipidemia.DYSLIPIDEMIA_INFO["what_is_it"])
        st.warning(dyslipidemia.DYSLIPIDEMIA_INFO["why_dangerous"])
        
        st.subheader("🔬 Các chỉ số Lipid:")
        for lipid_key, lipid_info in dyslipidemia.DYSLIPIDEMIA_INFO["lipid_types"].items():
            with st.container():
                st.markdown(f"**{lipid_info['name']}** ({lipid_info['abbreviation']})")
                st.caption(lipid_info["simple_explanation"])
                st.divider()
    
    # Phân loại thực phẩm Traffic Light
    with st.expander("🚦 PHÂN LOẠI THỰC PHẨM - Dễ Hiểu, Dễ Nhớ", expanded=True):
        st.markdown("### Hệ thống màu sắc giúp bạn biết ngay thực phẩm nào an toàn!")
        
        # Đỏ - Nguy hiểm
        st.error("### 🔴 ĐỎ - NGUY HIỂM: TRÁNH HOÀN TOÀN")
        st.markdown(dyslipidemia.FOOD_SAFETY_CLASSIFICATION["red_danger"]["rule"])
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**Trans Fat:**")
            for food in dyslipidemia.FOOD_SAFETY_CLASSIFICATION["red_danger"]["foods"]["trans_fat_foods"][:3]:
                st.markdown(food)
        with col2:
            st.markdown("**Cholesterol Cực Cao:**")
            for food in dyslipidemia.FOOD_SAFETY_CLASSIFICATION["red_danger"]["foods"]["very_high_cholesterol"][:3]:
                st.markdown(food)
        with col3:
            st.markdown("**Mỡ Bão Hòa Cao:**")
            for food in dyslipidemia.FOOD_SAFETY_CLASSIFICATION["red_danger"]["foods"]["very_high_saturated_fat"][:3]:
                st.markdown(food)
        
        # Cam - Hạn chế
        st.warning("### 🟠 CAM - HẠN CHẾ: Ăn ít, < 2-3 lần/tuần")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Thịt Nhiều Mỡ:**")
            for food in dyslipidemia.FOOD_SAFETY_CLASSIFICATION["orange_limit"]["foods"]["fatty_meat"][:4]:
                st.markdown(food)
        with col2:
            st.markdown("**Thịt Chế Biến:**")
            for food in dyslipidemia.FOOD_SAFETY_CLASSIFICATION["orange_limit"]["foods"]["processed_meat"][:4]:
                st.markdown(food)
        
        # Xanh - An toàn
        st.success("### 🟢 XANH LÁ - AN TOÀN: Ăn tự do")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**Rau:**")
            for food in dyslipidemia.FOOD_SAFETY_CLASSIFICATION["green_safe"]["foods"]["vegetables"][:4]:
                st.markdown(food)
        with col2:
            st.markdown("**Trái Cây:**")
            for food in dyslipidemia.FOOD_SAFETY_CLASSIFICATION["green_safe"]["foods"]["fruits"][:4]:
                st.markdown(food)
        with col3:
            st.markdown("**Ngũ Cốc:**")
            for food in dyslipidemia.FOOD_SAFETY_CLASSIFICATION["green_safe"]["foods"]["whole_grains"][:4]:
                st.markdown(food)
        
        # Xanh đậm - Rất tốt
        st.success("### 🟩 XANH ĐẬM - RẤT TỐT: Nên ăn nhiều!")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Cá Giàu Omega-3:**")
            for food in dyslipidemia.FOOD_SAFETY_CLASSIFICATION["dark_green_excellent"]["foods"]["omega3_fish"]:
                st.markdown(food)
        with col2:
            st.markdown("**Hạt:**")
            for food in dyslipidemia.FOOD_SAFETY_CLASSIFICATION["dark_green_excellent"]["foods"]["nuts_seeds"]:
                st.markdown(food)
        
        st.info("💡 **Mẹo:** Càng XANH càng TỐT - càng ĐỎ càng NGUY HIỂM!")
    
    # Bảng tra cứu nhanh
    with st.expander("📊 BẢNG TRA CỨU NHANH - Món Phổ Biến VN"):
        category = st.selectbox(
            "Chọn loại món:",
            ["Món Sáng", "Bữa Chính", "Đồ Ăn Vặt", "Protein", "Dầu Nấu Ăn", "Đồ Uống"]
        )
        
        if category == "Món Sáng":
            data = dyslipidemia.QUICK_REFERENCE_TABLE["breakfast_foods"]
        elif category == "Bữa Chính":
            data = dyslipidemia.QUICK_REFERENCE_TABLE["lunch_dinner"]
        elif category == "Đồ Ăn Vặt":
            data = dyslipidemia.QUICK_REFERENCE_TABLE["snacks"]
        elif category == "Protein":
            data = dyslipidemia.QUICK_REFERENCE_TABLE["proteins"]
        elif category == "Dầu Nấu Ăn":
            data = dyslipidemia.QUICK_REFERENCE_TABLE["cooking_oils"]
        else:  # Đồ Uống
            data = dyslipidemia.QUICK_REFERENCE_TABLE["beverages"]
        
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.error("**🔴 ĐỎ**")
            for item in data["red"]:
                st.markdown(f"- {item}")
        with col2:
            st.warning("**🟠 CAM**")
            for item in data["orange"]:
                st.markdown(f"- {item}")
        with col3:
            st.info("**🟡 VÀNG**")
            for item in data["yellow"]:
                st.markdown(f"- {item}")
        with col4:
            st.success("**🟢 XANH**")
            for item in data["green"]:
                st.markdown(f"- {item}")
        with col5:
            st.success("**🟩 XANH ĐẬM**")
            for item in data["dark_green"]:
                st.markdown(f"- {item}")
    
    # Giải thích về các loại mỡ
    with st.expander("🧈 Các Loại Chất Béo - Tốt và Xấu"):
        st.subheader("☠️ Trans Fat - MỠ CHUYỂN HÓA (XẤU NHẤT!)")
        st.markdown(dyslipidemia.FAT_TYPES_EXPLANATION["trans_fat"]["simple"])
        st.error("**Tại sao nguy hiểm:**")
        for reason in dyslipidemia.FAT_TYPES_EXPLANATION["trans_fat"]["why_dangerous"][:3]:
            st.markdown(f"- {reason}")
        st.markdown("**Có trong:** " + ", ".join(dyslipidemia.FAT_TYPES_EXPLANATION["trans_fat"]["sources"][:5]))
        
        st.divider()
        
        st.subheader("🥩 Mỡ Bão Hòa (XẤU)")
        st.markdown(dyslipidemia.FAT_TYPES_EXPLANATION["saturated_fat"]["simple"])
        st.markdown("**Có trong:** " + ", ".join(dyslipidemia.FAT_TYPES_EXPLANATION["saturated_fat"]["sources"][:5]))
        st.warning(dyslipidemia.FAT_TYPES_EXPLANATION["saturated_fat"]["recommendation"])
        
        st.divider()
        
        st.subheader("🫒 Mỡ Không Bão Hòa Đơn (TỐT)")
        st.markdown(dyslipidemia.FAT_TYPES_EXPLANATION["monounsaturated_fat"]["simple"])
        st.success("**Lợi ích:** " + ", ".join(dyslipidemia.FAT_TYPES_EXPLANATION["monounsaturated_fat"]["why_good"][:2]))
        st.markdown("**Có trong:** " + ", ".join(dyslipidemia.FAT_TYPES_EXPLANATION["monounsaturated_fat"]["sources"]))
        
        st.divider()
        
        st.subheader("🐟 Omega-3 (RẤT TỐT!)")
        st.markdown(dyslipidemia.FAT_TYPES_EXPLANATION["polyunsaturated_fat"]["types"]["omega3"]["name"])
        st.success("**Lợi ích:** " + ", ".join(dyslipidemia.FAT_TYPES_EXPLANATION["polyunsaturated_fat"]["types"]["omega3"]["benefits"][:2]))
        st.markdown("**Có trong:** " + ", ".join(dyslipidemia.FAT_TYPES_EXPLANATION["polyunsaturated_fat"]["types"]["omega3"]["sources"]))
        st.info(dyslipidemia.FAT_TYPES_EXPLANATION["polyunsaturated_fat"]["types"]["omega3"]["recommendation"])
    
    # Thuốc điều trị
    with st.expander("💊 Thuốc Điều Trị"):
        st.subheader("💊 STATINS - Thuốc Hạ Cholesterol (Nhóm Chính)")
        st.markdown(dyslipidemia.STATINS["description"])
        st.info("**Cơ chế:** " + dyslipidemia.STATINS["how_it_works"]["simple"])
        
        st.markdown("**Hiệu quả:**")
        for effect in dyslipidemia.STATINS["how_it_works"]["effects"]:
            st.markdown(f"- {effect}")
        
        st.markdown("### Các loại Statin phổ biến tại VN:")
        for statin in dyslipidemia.STATINS["common_statins"][:3]:
            with st.container():
                st.markdown(f"**{statin['name']}**")
                st.caption(f"Nhãn VN: {', '.join(statin['vietnamese_brands'])}")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Liều", statin["dosage"])
                with col2:
                    st.metric("Hiệu quả", statin["ldl_reduction"])
                with col3:
                    st.metric("Giá", statin["cost"])
                st.caption(f"💡 {statin['note']}")
                st.divider()
        
        st.warning("**Tác dụng phụ thường gặp:**")
        for se in dyslipidemia.STATINS["side_effects"]["common"]:
            st.markdown(f"- {se}")
        
        st.success(dyslipidemia.STATINS["side_effects"]["myth_busting"])
        
        st.divider()
        
        st.subheader("💊 FIBRATES - Hạ Triglyceride")
        st.markdown(dyslipidemia.FIBRATES["description"])
        st.markdown("**Hiệu quả:**")
        for effect in dyslipidemia.FIBRATES["how_it_works"]["effects"]:
            st.markdown(f"- {effect}")
    
    # Công cụ phân loại lipid
    with st.expander("🧪 Công Cụ Phân Loại Chỉ Số Lipid"):
        st.markdown("Nhập kết quả xét nghiệm của bạn:")
        
        col1, col2 = st.columns(2)
        with col1:
            total_chol = st.number_input(
                "Cholesterol toàn phần (mmol/L)",
                min_value=2.0,
                max_value=15.0,
                value=5.0,
                step=0.1,
                help="Bình thường: < 5.2 mmol/L"
            )
            ldl = st.number_input(
                "LDL - Mỡ xấu (mmol/L)",
                min_value=1.0,
                max_value=10.0,
                value=3.0,
                step=0.1,
                help="Mục tiêu: < 2.6 mmol/L"
            )
        
        with col2:
            hdl = st.number_input(
                "HDL - Mỡ tốt (mmol/L)",
                min_value=0.5,
                max_value=3.0,
                value=1.3,
                step=0.1,
                help="Nam: > 1.0, Nữ: > 1.3 mmol/L"
            )
            tg = st.number_input(
                "Triglyceride (mmol/L)",
                min_value=0.5,
                max_value=20.0,
                value=1.5,
                step=0.1,
                help="Bình thường: < 1.7 mmol/L"
            )
        
        if st.button("Phân loại & Tư vấn", type="primary"):
            classification = dyslipidemia.classify_lipid_levels(total_chol, ldl, hdl, tg)
            
            st.subheader("📊 Kết quả phân loại:")
            
            # Total Cholesterol
            if classification["total_cholesterol"]["level"] == "Tối ưu":
                st.success(f"**Cholesterol toàn phần:** {total_chol} mmol/L - {classification['total_cholesterol']['level']}")
            elif classification["total_cholesterol"]["level"] in ["Cao", "Rất cao"]:
                st.error(f"**Cholesterol toàn phần:** {total_chol} mmol/L - {classification['total_cholesterol']['level']}")
            else:
                st.warning(f"**Cholesterol toàn phần:** {total_chol} mmol/L - {classification['total_cholesterol']['level']}")
            
            # LDL
            if classification["ldl"]["level"] == "Tối ưu":
                st.success(f"**LDL (mỡ xấu):** {ldl} mmol/L - {classification['ldl']['level']}")
            elif classification["ldl"]["level"] in ["Cao", "Rất cao"]:
                st.error(f"**LDL (mỡ xấu):** {ldl} mmol/L - {classification['ldl']['level']}")
            else:
                st.warning(f"**LDL (mỡ xấu):** {ldl} mmol/L - {classification['ldl']['level']}")
            st.caption(classification["ldl"]["recommendation"])
            
            # HDL
            if classification["hdl"]["level"] == "Cao (Tốt)":
                st.success(f"**HDL (mỡ tốt):** {hdl} mmol/L - {classification['hdl']['level']}")
            else:
                st.warning(f"**HDL (mỡ tốt):** {hdl} mmol/L - {classification['hdl']['level']}")
            st.caption(classification["hdl"]["recommendation"])
            
            # Triglyceride
            if classification["triglyceride"]["level"] == "Bình thường":
                st.success(f"**Triglyceride:** {tg} mmol/L - {classification['triglyceride']['level']}")
            elif classification["triglyceride"]["level"] in ["Cao", "Rất cao"]:
                st.error(f"**Triglyceride:** {tg} mmol/L - {classification['triglyceride']['level']}")
            else:
                st.warning(f"**Triglyceride:** {tg} mmol/L - {classification['triglyceride']['level']}")
            st.caption(classification["triglyceride"]["recommendation"])

# ============= TAB ĐO HUYẾT ÁP =============
with tab4:
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

