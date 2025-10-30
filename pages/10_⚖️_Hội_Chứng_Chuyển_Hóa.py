"""
Trang: Hội Chứng Chuyển Hóa & Béo Phì
=====================================

Metabolic Syndrome & Obesity Management
Quản lý cân nặng, calories, vận động, mục tiêu giảm cân
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import sys
import os

# Add parent directory to path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

from diseases.metabolic import obesity
from core.ui_config import apply_custom_css

# Page config
st.set_page_config(
    page_title="Hội Chứng Chuyển Hóa - HealthAdvisor",
    page_icon="⚖️",
    layout="wide"
)

# Apply custom CSS
apply_custom_css()

# Title
st.title("⚖️ Hội Chứng Chuyển Hóa & Quản Lý Cân Nặng")
st.markdown("**Metabolic Syndrome & Weight Management**")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Tổng Quan",
    "⚖️ Béo Phì & Đánh Giá", 
    "🔗 Bệnh Liên Quan",
    "🍽️ Calories & Vận Động",
    "🎯 Mục Tiêu & Kế Hoạch"
])

# ============================================================================
# TAB 1: TỔNG QUAN HỘI CHỨNG CHUYỂN HÓA
# ============================================================================
with tab1:
    st.header("📊 Hội Chứng Chuyển Hóa (Metabolic Syndrome)")
    
    # Giới thiệu
    st.info("""
    **Hội chứng Chuyển hóa** là cụm 5 bệnh lý liên quan chặt chẽ, có chung gốc rễ là **BÉO PHÌ**.
    
    Nếu có ≥3 trong 5 yếu tố sau, bạn có Hội chứng Chuyển hóa:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🎯 5 Thành Phần Chính:
        
        1. **⚖️ Béo bụng (Béo phì trung tâm)**
           - Nam: Vòng eo ≥ 90 cm
           - Nữ: Vòng eo ≥ 80 cm
        
        2. **🩸 Đường huyết cao**
           - Đói ≥ 5.6 mmol/L (100 mg/dL)
           - Hoặc đang điều trị tiểu đường
        
        3. **💉 Huyết áp cao**
           - ≥ 130/85 mmHg
           - Hoặc đang điều trị huyết áp
        
        4. **🧪 Triglyceride cao**
           - ≥ 1.7 mmol/L (150 mg/dL)
        
        5. **💙 HDL-C thấp (cholesterol tốt)**
           - Nam: < 1.0 mmol/L (40 mg/dL)
           - Nữ: < 1.3 mmol/L (50 mg/dL)
        """)
    
    with col2:
        st.markdown("""
        ### ⚠️ Tại Sao Nguy Hiểm?
        
        **Tăng nguy cơ:**
        - 🫀 Bệnh tim mạch: **3 lần**
        - 💔 Đột quỵ: **2-3 lần**
        - 🩸 Tiểu đường type 2: **5 lần**
        - 🫘 Bệnh thận mãn: **2 lần**
        - 🎗️ Một số loại ung thư
        
        ### ✅ Tin Tốt: CÓ THỂ ĐẢO NGƯỢC!
        
        - Giảm 5-10% cân nặng
        - Ăn uống lành mạnh
        - Vận động 150 phút/tuần
        - Kiểm soát stress
        - Ngủ đủ giấc
        
        → **Có thể đảo ngược hoàn toàn!**
        """)
    
    # Sơ đồ mối liên hệ
    st.markdown("---")
    st.subheader("🔗 Mối Liên Hệ Giữa Các Bệnh")
    
    st.markdown("""
    ```
    ┌─────────────────────────────────┐
    │     ⚖️ BÉO PHÌ (Gốc rễ)         │
    └────────────┬────────────────────┘
                 │
         ┌───────┼───────┐
         ▼       ▼       ▼
    ┌─────┐ ┌─────┐ ┌─────┐
    │🩸ĐTĐ│ │💉HA │ │🧪Lipid│
    └──┬──┘ └──┬──┘ └──┬──┘
       └───────┼───────┘
               ▼
         ┌─────────┐
         │ ❤️ Tim   │
         │  Mạch   │
         └─────────┘
               │
         ┌─────┼─────┐
         ▼     ▼     ▼
     Nhồi máu Đột quỵ Suy tim
    ```
    
    **Vòng luẩn quẩn:**
    - Béo phì → Kháng insulin → Tiểu đường
    - Béo phì → Tăng huyết áp → Tim mạch
    - Tiểu đường + Cao HA → Đột quỵ, Suy thận
    
    **PHÁ VỠ VÒNG LẶP:** Giảm cân là chìa khóa! ✨
    """)
    
    # Statistics VN
    st.markdown("---")
    st.subheader("📈 Thống Kê Việt Nam")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Béo phì", "25%", "↑38%/năm", help="Tốc độ tăng nhanh nhất ĐNA")
    with col2:
        st.metric("Tiểu đường", "6.5%", "↑2x trong 10 năm")
    with col3:
        st.metric("Cao huyết áp", "25-30%", "↑ theo tuổi")
    with col4:
        st.metric("Lipid máu cao", "~30%", "Đo ở người >40 tuổi")

# ============================================================================
# TAB 2: BÉO PHÌ & ĐÁNH GIÁ
# ============================================================================
with tab2:
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
        st.markdown("---")
        st.subheader("📊 KẾT QUẢ ĐÁNH GIÁ")
        
        # 1. BMI
        bmi = obesity.calculate_bmi(weight, height)
        bmi_cat = obesity.get_bmi_category(bmi)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            ### {bmi_cat['icon']} BMI: {bmi}
            **{bmi_cat['label']}**
            """)
            st.markdown(f"<div style='background-color: {bmi_cat['color']}; padding: 10px; border-radius: 5px; color: #000;'>Nguy cơ: <b>{bmi_cat['risk']}</b></div>", unsafe_allow_html=True)
            st.info(f"💡 {bmi_cat['advice']}")
        
        # 2. TDEE
        tdee_result = obesity.calculate_tdee(weight, height, age, gender, activity_level)
        
        with col2:
            st.markdown(f"""
            ### 🔥 TDEE: {tdee_result['tdee']:.0f} cal
            **Calories cần mỗi ngày**
            """)
            st.markdown(f"BMR: {tdee_result['bmr']:.0f} cal (nghỉ ngơi)")
            st.success(f"Giảm cân: {tdee_result['lose_moderate']:.0f} cal/ngày")
        
        # 3. WHR
        whr_result = obesity.calculate_whr(waist, hip, gender)
        
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

# ============================================================================
# TAB 3: BỆNH LIÊN QUAN
# ============================================================================
with tab3:
    st.header("🔗 Các Bệnh Liên Quan Béo Phì")
    
    st.info("""
    Béo phì là **gốc rễ** của nhiều bệnh mãn tính. Dưới đây là các bệnh có trong app 
    mà bạn có thể tìm hiểu thêm.
    """)
    
    # Direct consequences
    st.subheader("⚡ Hậu Quả Trực Tiếp (Nguy cơ rất cao)")
    
    for disease_id, disease_data in obesity.RELATED_DISEASES["direct_consequences"].items():
        with st.expander(f"{disease_data['name']} - Nguy cơ: {disease_data['risk']}"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"""
                **Cơ chế:**
                
                {disease_data['mechanism']}
                
                **Phòng ngừa:**
                - Giảm cân 5-10%
                - Ăn uống lành mạnh
                - Vận động đều đặn
                - Kiểm tra sức khỏe định kỳ
                """)
            
            with col2:
                if st.button(f"Đi tới trang {disease_data['name']}", key=f"btn_{disease_id}"):
                    st.info(f"📖 Xem thêm tại: {disease_data['page']}")
    
    # Complications
    st.markdown("---")
    st.subheader("🌀 Biến Chứng (Nguy cơ cao)")
    
    for disease_id, disease_data in obesity.RELATED_DISEASES["complications"].items():
        with st.expander(f"{disease_data['name']} - Nguy cơ tăng {disease_data['risk']}"):
            st.markdown(f"""
            **Cơ chế:**
            
            {disease_data['mechanism']}
            
            **Dấu hiệu cảnh báo:**
            """)
            
            # Specific symptoms based on disease
            if "copd" in disease_id:
                st.markdown("""
                - Khó thở khi gắng sức
                - Ho mãn tính
                - Đờm nhiều
                - Thở khò khè
                """)
            elif "osteoarthritis" in disease_id:
                st.markdown("""
                - Đau khớp gối, háng
                - Cứng khớp buổi sáng
                - Khó đi lại
                - Sưng khớp
                """)
            elif "gout" in disease_id:
                st.markdown("""
                - Đau khớp ngón chân cái đột ngột
                - Sưng đỏ, nóng
                - Đau dữ dội ban đêm
                - Axit uric cao
                """)
    
    # Prevention summary
    st.markdown("---")
    st.success("""
    ### ✅ Phòng Ngừa Tất Cả Các Bệnh Trên:
    
    **1️⃣ Giảm cân:** Chỉ cần giảm 5-10% cân nặng đã giảm nguy cơ đáng kể!
    
    **2️⃣ Ăn uống:**
    - Giảm cơm, tăng rau
    - Tránh đồ chiên rán, ngọt
    - Ăn đủ protein
    
    **3️⃣ Vận động:**
    - 150 phút/tuần (30 phút x 5 ngày)
    - Đi bộ, tập nhẹ
    
    **4️⃣ Khám định kỳ:**
    - 6 tháng/lần
    - Xét nghiệm: Đường máu, lipid máu, huyết áp
    """)

# ============================================================================
# TAB 4: CALORIES & VẬN ĐỘNG
# ============================================================================
with tab4:
    st.header("🍽️ Calories & Vận Động")
    
    # Sub-tabs
    subtab1, subtab2, subtab3 = st.tabs(["🍚 Thực Phẩm VN", "🏃 Vận Động", "📝 Tính Calories"])
    
    # Subtab 1: Vietnamese Foods
    with subtab1:
        st.subheader("🍚 Database Thực Phẩm Việt Nam")
        
        # Search food
        search = st.text_input("🔍 Tìm món ăn", placeholder="VD: phở, cơm, bánh mì...")
        
        if search:
            result = obesity.find_food_calories(search)
            if result:
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.success(f"**{result['name']}**")
                    st.metric("Calories", f"{result['calories']} cal")
                with col2:
                    st.markdown(f"**Danh mục:** {result['category']}")
                    col_p, col_c, col_f = st.columns(3)
                    with col_p:
                        st.caption(f"Protein: {result['protein']}g")
                    with col_c:
                        st.caption(f"Carbs: {result['carbs']}g")
                    with col_f:
                        st.caption(f"Fat: {result['fat']}g")
            else:
                st.warning("Không tìm thấy. Thử món khác!")
        
        # Show all foods
        st.markdown("---")
        
        for category_id, category_data in obesity.VIETNAMESE_FOODS.items():
            with st.expander(f"{category_data['name']} ({len(category_data['foods'])} món)"):
                # Create dataframe
                foods_list = []
                for food, nutrition in category_data['foods'].items():
                    foods_list.append({
                        "Món ăn": food,
                        "Calories": nutrition['calories'],
                        "Protein (g)": nutrition['protein'],
                        "Carbs (g)": nutrition['carbs'],
                        "Fat (g)": nutrition['fat']
                    })
                
                df = pd.DataFrame(foods_list)
                st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Food categories
        st.markdown("---")
        st.subheader("📋 Phân Loại Thực Phẩm")
        
        for cat_id, cat_data in obesity.FOOD_CATEGORIES.items():
            with st.expander(cat_data['name']):
                for food in cat_data['foods']:
                    st.markdown(f"• {food}")
                st.info(f"💡 **Tip:** {cat_data['tip']}")
    
    # Subtab 2: Exercise
    with subtab2:
        st.subheader("🏃 Vận Động & Đốt Cháy Calories")
        
        # Calculator
        st.markdown("#### 🔥 Tính Calories Đốt Cháy")
        
        col1, col2, col3 = st.columns(3)
        
        # Get all activities
        all_activities = {}
        for cat_id, cat_data in obesity.EXERCISES_CALORIES.items():
            all_activities.update(cat_data['activities'])
        
        with col1:
            activity = st.selectbox("Chọn hoạt động", list(all_activities.keys()))
        with col2:
            duration = st.number_input("Thời gian (phút)", min_value=1, max_value=300, value=30)
        with col3:
            ex_weight = st.number_input("Cân nặng (kg)", min_value=30.0, max_value=200.0, value=70.0)
        
        if st.button("Tính ngay", type="primary"):
            result = obesity.calculate_calories_burned(activity, duration, ex_weight)
            
            col1, col2 = st.columns(2)
            with col1:
                st.success(f"""
                ### 🔥 Đốt cháy: {result['calories_burned']} calories
                
                **Hoạt động:** {result['activity']}  
                **Thời gian:** {result['duration_minutes']} phút  
                **Cân nặng:** {result['weight_kg']} kg
                """)
            
            with col2:
                if result['food_equivalents']:
                    st.info(f"""
                    **Tương đương với:**
                    
                    {chr(10).join('✅ ' + eq for eq in result['food_equivalents'])}
                    """)
        
        # Show all exercises
        st.markdown("---")
        
        for cat_id, cat_data in obesity.EXERCISES_CALORIES.items():
            with st.expander(f"{cat_data['name']} ({len(cat_data['activities'])} hoạt động)"):
                for activity, cal_per_hour in cat_data['activities'].items():
                    st.markdown(f"**{activity}:** {cal_per_hour} cal/giờ (người 70kg)")
        
        # Exercise plans
        st.markdown("---")
        st.subheader("📅 Kế Hoạch Tập Luyện Tuần")
        
        level = st.selectbox(
            "Chọn mức độ",
            ["beginner", "intermediate", "advanced"],
            format_func=lambda x: {
                "beginner": "🐢 Người mới / Người già",
                "intermediate": "🚶 Trung bình",
                "advanced": "🏃 Nâng cao"
            }[x]
        )
        
        plan = obesity.get_exercise_plan(level, "lose_weight", 30)
        
        st.info(f"""
        **Mức độ:** {plan['level']}  
        **Tổng thời gian:** {plan['total_minutes_per_week']} phút/tuần  
        **Ước tính đốt:** ~{plan['estimated_calories_burned']} calories/tuần
        """)
        
        # Weekly plan table
        plan_list = []
        for day, details in plan['weekly_plan'].items():
            plan_list.append({
                "Thứ": day.capitalize(),
                "Hoạt động": details['activity'],
                "Thời gian": f"{details['duration']} phút",
                "Ghi chú": details.get('note', '')
            })
        
        df_plan = pd.DataFrame(plan_list)
        st.dataframe(df_plan, use_container_width=True, hide_index=True)
    
    # Subtab 3: Calculator
    with subtab3:
        st.subheader("📝 Tính Tổng Calories Bữa Ăn")
        
        st.markdown("Nhập các món ăn (mỗi dòng 1 món):")
        
        foods_input = st.text_area(
            "Món ăn",
            placeholder="VD:\nPhở bò\nCà phê sữa\nBánh mì thịt",
            height=150
        )
        
        if st.button("Tính tổng calories", type="primary"):
            if foods_input:
                foods_list = [f.strip() for f in foods_input.split('\n') if f.strip()]
                result = obesity.calculate_meal_calories(foods_list)
                
                st.success(f"### 🍽️ Tổng: {result['total_calories']} calories")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Protein", f"{result['macros']['protein']}g")
                with col2:
                    st.metric("Carbs", f"{result['macros']['carbs']}g")
                with col3:
                    st.metric("Fat", f"{result['macros']['fat']}g")
                
                if result['foods']:
                    st.markdown("**Chi tiết:**")
                    for food in result['foods']:
                        st.markdown(f"- {food['name']}: {food['calories']} cal")
                
                if result['not_found']:
                    st.warning(f"Không tìm thấy: {', '.join(result['not_found'])}")

# ============================================================================
# TAB 5: MỤC TIÊU & KẾ HOẠCH
# ============================================================================
with tab5:
    st.header("🎯 Đặt Mục Tiêu & Theo Dõi Tiến Trình")
    
    # Create goal
    st.subheader("📋 Tạo Mục Tiêu Giảm Cân")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        current_w = st.number_input("Cân nặng hiện tại (kg)", min_value=30.0, max_value=200.0, value=75.0, key="goal_current")
    with col2:
        target_w = st.number_input("Cân nặng mục tiêu (kg)", min_value=30.0, max_value=200.0, value=65.0, key="goal_target")
    with col3:
        weekly_loss = st.slider("Giảm/tuần (kg)", min_value=0.3, max_value=1.0, value=0.5, step=0.1)
    
    if st.button("🎯 Tạo Mục Tiêu", type="primary", use_container_width=True):
        goal = obesity.create_weight_loss_goal(current_w, target_w, None, weekly_loss)
        
        if 'error' not in goal:
            st.session_state['weight_goal'] = goal
            st.success("✅ Đã tạo mục tiêu thành công!")
        else:
            st.error(f"❌ {goal['error']}")
            if 'suggestion' in goal:
                st.info(goal['suggestion'])
    
    # Display goal
    if 'weight_goal' in st.session_state:
        goal = st.session_state['weight_goal']
        
        st.markdown("---")
        st.subheader("📊 Mục Tiêu Của Bạn")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Hiện tại", f"{goal['current_weight']} kg")
        with col2:
            st.metric("Mục tiêu", f"{goal['target_weight']} kg")
        with col3:
            st.metric("Cần giảm", f"{goal['total_loss_needed']} kg")
        with col4:
            st.metric("Thời gian", f"{goal['weeks_needed']} tuần")
        
        st.info(f"🎯 Dự kiến đạt mục tiêu: **{goal['target_date_display']}**")
        st.caption(f"💡 {goal['recommendation']}")
        
        # Milestones
        st.markdown("---")
        st.subheader("🏆 Các Mốc Quan Trọng")
        
        for milestone in goal['milestones']:
            with st.expander(f"{milestone['percentage']}% - {milestone['weight']} kg (Tuần {milestone['weeks']})"):
                st.markdown(f"**Giảm được:** {milestone['loss_from_start']} kg")
                st.markdown(f"**Ngày dự kiến:** {milestone['date']}")
                st.markdown("**Lợi ích:**")
                for benefit in milestone['benefits']:
                    st.markdown(f"{benefit}")
        
        # Progress tracking
        st.markdown("---")
        st.subheader("📈 Cập Nhật Tiến Trình")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            new_weight = st.number_input(
                "Cân nặng hiện tại (kg)",
                min_value=30.0,
                max_value=200.0,
                value=goal['current_weight'],
                step=0.1,
                key="progress_weight"
            )
            
            if st.button("Cập nhật", type="primary"):
                progress = obesity.calculate_progress(goal, new_weight)
                st.session_state['progress'] = progress
        
        if 'progress' in st.session_state:
            progress = st.session_state['progress']
            
            with col2:
                st.markdown(f"<div style='background-color: {progress['color']}; padding: 20px; border-radius: 10px; color: #000;'>", unsafe_allow_html=True)
                st.markdown(f"### {progress['message']}")
                st.markdown(f"**Tiến độ:** {progress['progress_percentage']}%")
                st.markdown(f"**Đã giảm:** {progress['weight_lost']} kg")
                st.markdown(f"**Còn lại:** {progress['weight_remaining']} kg")
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Progress bar
                st.progress(min(progress['progress_percentage'] / 100, 1.0))
                
                st.info(f"💬 {progress['motivation']}")
                
                if progress['next_milestone']:
                    nm = progress['next_milestone']
                    st.success(f"🎯 **Mốc tiếp theo:** {nm['percentage']}% ({nm['weight']} kg)")
    
    # Tips
    st.markdown("---")
    st.subheader("💡 Lời Khuyên Hàng Tuần")
    
    tips = obesity.get_weekly_tips()
    
    col1, col2 = st.columns(2)
    for idx, tip in enumerate(tips):
        with col1 if idx % 2 == 0 else col2:
            st.info(tip)
    
    # Daily affirmations
    st.markdown("---")
    st.subheader("✨ Khẳng Định Tích Cực")
    
    affirmations = obesity.get_daily_affirmations()
    
    cols = st.columns(2)
    for idx, affirmation in enumerate(affirmations[:6]):
        with cols[idx % 2]:
            st.success(affirmation)

# Footer
st.markdown("---")
st.caption("""
💡 **Lưu ý:** Thông tin chỉ mang tính tham khảo. Hãy tham khảo bác sĩ trước khi bắt đầu chương trình giảm cân,
đặc biệt nếu bạn có bệnh nền hoặc >60 tuổi.
""")

