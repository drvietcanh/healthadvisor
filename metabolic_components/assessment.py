"""
Tab Đánh Giá - Béo Phì & Sức Khỏe
"""
import streamlit as st
from diseases.metabolic import obesity


def render_assessment_tab():
    """Render tab đánh giá béo phì"""
    
    st.header("⚖️ Đánh Giá Béo Phì & Sức Khỏe")
    
    # Input form
    st.subheader("📝 Nhập Thông Tin")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        weight = st.number_input("Cân nặng (kg)", min_value=30.0, max_value=200.0, value=70.0, step=0.1)
        height = st.number_input("Chiều cao (cm)", min_value=100.0, max_value=220.0, value=165.0, step=0.1)
    
    with col2:
        age = st.number_input("Tuổi", min_value=18, max_value=100, value=50)
        gender = st.selectbox("Giới tính", ["male", "female"], format_func=lambda x: "Nam" if x == "male" else "Nữ")
    
    with col3:
        waist = st.number_input("Vòng eo (cm)", min_value=50.0, max_value=200.0, value=80.0, step=0.1, help="Đo ngang rốn")
        hip = st.number_input("Vòng hông (cm)", min_value=50.0, max_value=200.0, value=95.0, step=0.1, help="Phần rộng nhất")
    
    activity_level = st.select_slider(
        "Mức độ vận động",
        options=["sedentary", "light", "moderate", "active", "very_active"],
        value="light",
        format_func=lambda x: {
            "sedentary": "😴 Ít vận động (ngồi nhiều)",
            "light": "🚶 Nhẹ (tập 1-3 ngày/tuần)",
            "moderate": "🏃 Trung bình (tập 3-5 ngày/tuần)",
            "active": "💪 Năng động (tập 6-7 ngày/tuần)",
            "very_active": "🔥 Rất năng động (vận động viên)"
        }[x]
    )
    
    # Calculate button
    if st.button("🔍 Đánh Giá Ngay", type="primary", use_container_width=True):
        _display_assessment_results(weight, height, age, gender, waist, hip, activity_level)


def _display_assessment_results(weight, height, age, gender, waist, hip, activity_level):
    """Hiển thị kết quả đánh giá"""
    
    st.markdown("---")
    st.subheader("📊 KẾT QUẢ ĐÁNH GIÁ")
    
    # 1. BMI
    bmi = obesity.calculate_bmi(weight, height)
    bmi_cat = obesity.get_bmi_category(bmi)
    
    # 2. TDEE
    tdee_result = obesity.calculate_tdee(weight, height, age, gender, activity_level)
    
    # 3. WHR
    whr_result = obesity.calculate_whr(waist, hip, gender)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        ### {bmi_cat['icon']} BMI: {bmi}
        **{bmi_cat['label']}**
        """)
        st.markdown(f"<div style='background-color: {bmi_cat['color']}; padding: 10px; border-radius: 5px; color: #000;'>Nguy cơ: <b>{bmi_cat['risk']}</b></div>", unsafe_allow_html=True)
        st.info(f"💡 {bmi_cat['advice']}")
    
    with col2:
        st.markdown(f"""
        ### 🔥 TDEE: {tdee_result['tdee']:.0f} cal
        **Calories cần mỗi ngày**
        """)
        st.markdown(f"BMR: {tdee_result['bmr']:.0f} cal (nghỉ ngơi)")
        st.success(f"Giảm cân: {tdee_result['lose_moderate']:.0f} cal/ngày")
    
    with col3:
        st.markdown(f"""
        ### {whr_result['icon']} WHR: {whr_result['whr']}
        **Tỷ lệ Eo/Hông**
        """)
        st.markdown(f"<div style='background-color: {whr_result['color']}; padding: 10px; border-radius: 5px; color: #000;'>Nguy cơ tim mạch: <b>{whr_result['risk']}</b></div>", unsafe_allow_html=True)
        st.caption(whr_result['note'])
    
    # 4. Body Fat %
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    bodyfat_result = obesity.calculate_body_fat_percentage(bmi, age, gender)
    
    with col1:
        st.markdown(f"""
        ### 📊 % Mỡ Cơ Thể: {bodyfat_result['body_fat_percentage']}%
        **{bodyfat_result['category']}**
        """)
        
        # Progress bar for body fat
        st.progress(min(bodyfat_result['body_fat_percentage'] / 50, 1.0))
        st.caption(bodyfat_result['note'])
    
    # 5. Ideal Weight
    ideal_result = obesity.calculate_ideal_weight(height, gender)
    
    with col2:
        st.markdown(f"""
        ### 🎯 Cân Nặng Lý Tưởng
        **{ideal_result['ideal']} kg**
        """)
        st.markdown(f"Phạm vi khỏe mạnh: **{ideal_result['range'][0]}-{ideal_result['range'][1]} kg**")
        st.caption(f"BMI {ideal_result['bmi_range'][0]}-{ideal_result['bmi_range'][1]} (chuẩn Việt Nam)")
        
        # So sánh
        diff = weight - ideal_result['ideal']
        if diff > 0:
            st.warning(f"⚠️ Nặng hơn {diff:.1f} kg so với lý tưởng")
        elif diff < -5:
            st.info(f"⚖️ Nhẹ hơn {abs(diff):.1f} kg so với lý tưởng")
        else:
            st.success(f"✅ Gần với cân nặng lý tưởng!")
    
    # 6. Calories Breakdown
    st.markdown("---")
    st.subheader("🍽️ Phân Bổ Calories Theo Bữa")
    
    daily_cal = obesity.calculate_daily_calories(tdee_result['tdee'], "lose_moderate")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🌅 Sáng", f"{daily_cal['breakfast']:.0f} cal", "30%")
    with col2:
        st.metric("☀️ Trưa", f"{daily_cal['lunch']:.0f} cal", "40%")
    with col3:
        st.metric("🌙 Tối", f"{daily_cal['dinner']:.0f} cal", "25%")
    with col4:
        st.metric("🍪 Vặt", f"{daily_cal['snacks']:.0f} cal", "5%")
    
    # Macros
    st.markdown("**Đại lượng dinh dưỡng (Macros):**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(f"🥩 Protein: {daily_cal['macros']['protein']:.0f}g")
    with col2:
        st.info(f"🍚 Carbs: {daily_cal['macros']['carbs']:.0f}g")
    with col3:
        st.info(f"🥑 Fat: {daily_cal['macros']['fat']:.0f}g")
    
    # 7. Health Risks
    if bmi >= 25:  # Béo phì
        st.markdown("---")
        st.subheader("⚠️ Nguy Cơ Sức Khỏe")
        
        risks = obesity.HEALTH_RISKS
        
        cols = st.columns(3)
        for idx, (risk_id, risk_data) in enumerate(list(risks.items())[:6]):
            with cols[idx % 3]:
                st.warning(f"""
                **{risk_data['icon']} {risk_data['name']}**
                
                Tăng nguy cơ: {risk_data['risk_increase']}
                
                Bệnh liên quan:
                {chr(10).join('• ' + d for d in risk_data['diseases'][:3])}
                """)
    
    # 8. Weight Loss Benefits
    st.markdown("---")
    st.subheader("✨ Lợi Ích Khi Giảm Cân")
    
    for pct_id, benefits in obesity.WEIGHT_LOSS_BENEFITS.items():
        with st.expander(f"{benefits['weight_loss']} - {benefits['example']}"):
            for benefit in benefits['benefits']:
                st.markdown(f"✅ {benefit}")

