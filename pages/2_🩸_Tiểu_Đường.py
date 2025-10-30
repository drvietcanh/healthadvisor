"""
Trang tư vấn về bệnh Tiểu Đường
"""
import streamlit as st
import sys
sys.path.append('..')

from diseases.metabolic import diabetes
from core.utils import convert_blood_sugar, calculate_bmi

st.set_page_config(page_title="Tiểu Đường", page_icon="🩸", layout="wide")

st.title("🩸 Tư vấn Tiểu Đường")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📖 Giới thiệu",
    "💊 Thuốc",
    "🍽️ Ăn uống", 
    "📊 Công cụ"
])

# ============= TAB GIỚI THIỆU =============
with tab1:
    st.header("Tiểu đường là gì?")
    
    with st.expander("🍬 Giải thích đơn giản", expanded=True):
        st.markdown(diabetes.DISEASE_INFO["simple_explanation_vn"])
    
    with st.expander("📊 Các loại tiểu đường"):
        for type_key, type_info in diabetes.DISEASE_INFO["types_simple_vn"].items():
            st.subheader(type_info["name"])
            st.markdown(f"**Giải thích:** {type_info['explanation']}")
            st.markdown(f"**Ai hay gặp:** {type_info['who']}")
            st.markdown(f"**Điều trị:** {type_info['treatment']}")
            st.divider()
    
    with st.expander("🔍 Dấu hiệu nhận biết - 3 chữ NHIỀU"):
        st.markdown(diabetes.SYMPTOMS_SIMPLE["classic_3P_vn"]["title"])
        
        for symptom in diabetes.SYMPTOMS_SIMPLE["classic_3P_vn"]["symptoms"]:
            st.markdown(f"### {symptom['name']}")
            st.markdown(f"**{symptom['description']}**")
            for detail in symptom['details']:
                st.markdown(detail)
            st.divider()
        
        st.subheader("Triệu chứng khác:")
        for symptom in diabetes.SYMPTOMS_SIMPLE["other_symptoms_vn"][:5]:
            st.markdown(f"- {symptom}")
    
    with st.expander("🚨 Khi nào GỌI CẤP CỨU 115?"):
        emergency = diabetes.SYMPTOMS_SIMPLE["emergency_vn"]
        st.error(f"### {emergency['title']}")
        for sign in emergency['signs']:
            st.markdown(f"**{sign}**")

# ============= TAB THUỐC =============
with tab2:
    st.header("💊 Thuốc điều trị")
    
    st.warning(diabetes.MEDICATIONS_SIMPLE["overview_vn"])
    
    st.subheader("Thuốc uống phổ biến:")
    for drug in diabetes.MEDICATIONS_SIMPLE["oral_medications"][:3]:  # 3 thuốc đầu
        with st.expander(f"{drug['class']} - {drug['street_name']}"):
            st.markdown(f"**Ví dụ:** {drug['brand_names']}")
            st.markdown(f"**Tác dụng:** {drug['what_it_does']}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.success("**Lợi ích:**")
                for benefit in drug['benefits_vn']:
                    st.markdown(benefit)
            with col2:
                st.info("**Cách dùng:**")
                for instruction in drug['how_to_take']:
                    st.markdown(instruction)
            
            if 'warning_vn' in drug:
                st.error(drug['warning_vn'])
    
    st.divider()
    st.subheader("💉 Insulin")
    with st.expander("Khi nào cần tiêm insulin?"):
        st.markdown(diabetes.MEDICATIONS_SIMPLE["insulin_simple"]["when_vn"])
    
    with st.expander("⚠️ Hạ đường huyết - QUAN TRỌNG!"):
        st.error(diabetes.MEDICATIONS_SIMPLE["insulin_simple"]["hypoglycemia_vn"])

# ============= TAB ĂN UỐNG =============
with tab3:
    st.header("🍽️ Chế độ ăn uống")
    
    with st.expander("✨ Nguyên tắc vàng", expanded=True):
        st.markdown(diabetes.NUTRITION_SIMPLE["basic_principles_vn"])
    
    with st.expander("🍚 Phương pháp đĩa ăn (Đơn giản nhất!)"):
        st.markdown(diabetes.NUTRITION_SIMPLE["meal_plate_method_vn"])
    
    with st.expander("🔢 Đếm Carb (Tinh bột)"):
        st.markdown(diabetes.NUTRITION_SIMPLE["carb_counting_simple"]["what_vn"])
        
        st.subheader("1 phần carb (15g) = ")
        for example in diabetes.NUTRITION_SIMPLE["carb_counting_simple"]["examples_15g_carb"][:6]:
            st.markdown(example)
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("**✅ NÊN ĂN:**")
        foods = diabetes.NUTRITION_SIMPLE["what_to_eat_vn"]
        for category_key, category in foods.items():
            if category_key != "fats":
                st.markdown(f"**{category['title']}**")
                for food in category['foods'][:4]:
                    st.markdown(f"- {food}")
    
    with col2:
        st.error("**🚫 TRÁNH:**")
        for food in diabetes.NUTRITION_SIMPLE["foods_to_avoid_vn"][:8]:
            st.markdown(food)

# ============= TAB CÔNG CỤ =============
with tab4:
    st.header("📊 Công cụ hữu ích")
    
    # Chuyển đổi đường huyết
    st.subheader("🔄 Chuyển đổi đơn vị đường huyết")
    st.info(diabetes.BLOOD_SUGAR_LEVELS["units_note_vn"])
    
    col_a, col_b = st.columns(2)
    with col_a:
        input_value = st.number_input("Nhập giá trị", min_value=0.0, value=7.0, step=0.1)
        unit = st.radio("Đơn vị", ["mmol/L", "mg/dL"])
    
    with col_b:
        from_unit = "mmol" if unit == "mmol/L" else "mg"
        mmol, mg = convert_blood_sugar(input_value, from_unit)
        
        st.metric("Kết quả mmol/L", f"{mmol}")
        st.metric("Kết quả mg/dL", f"{int(mg)}")
    
    st.divider()
    
    # Tính BMI
    st.subheader("⚖️ Tính chỉ số BMI")
    col_x, col_y = st.columns(2)
    with col_x:
        weight = st.number_input("Cân nặng (kg)", min_value=20.0, max_value=200.0, value=65.0)
    with col_y:
        height = st.number_input("Chiều cao (cm)", min_value=100.0, max_value=250.0, value=165.0)
    
    if st.button("Tính BMI"):
        result = calculate_bmi(weight, height)
        
        if result["color"] == "green":
            st.success(f"### BMI: {result['bmi']}")
            st.success(f"**{result['category_vn']}** - {result['risk_vn']}")
        elif result["color"] in ["yellow", "orange"]:
            st.warning(f"### BMI: {result['bmi']}")
            st.warning(f"**{result['category_vn']}** - {result['risk_vn']}")
        else:
            st.error(f"### BMI: {result['bmi']}")
            st.error(f"**{result['category_vn']}** - {result['risk_vn']}")
    
    st.divider()
    
    # Bảng tham khảo đường huyết
    st.subheader("📋 Bảng đường huyết tham khảo")
    
    normal = diabetes.BLOOD_SUGAR_LEVELS["normal_ranges"]["fasting"]
    st.markdown(f"**{normal['name_vn']}:**")
    st.table({
        "Phân loại": ["Bình thường", "Tiền tiểu đường", "Tiểu đường"],
        "mmol/L": [normal['normal']['mmol'], normal['prediabetes']['mmol'], normal['diabetes']['mmol']],
        "mg/dL": [normal['normal']['mg'], normal['prediabetes']['mg'], normal['diabetes']['mg']],
        "Trạng thái": [normal['normal']['status'], normal['prediabetes']['status'], normal['diabetes']['status']]
    })

# Nút quay lại
st.divider()
if st.button("⬅️ Quay lại trang chính"):
    st.switch_page("app.py")

