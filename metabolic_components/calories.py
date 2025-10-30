"""
Tab Calories & Vận Động - Database thực phẩm và tính toán calories
"""
import streamlit as st
import pandas as pd
from diseases.metabolic import obesity


def render_calories_tab():
    """Render tab calories & vận động"""
    
    st.header("🍽️ Calories & Vận Động")
    
    # Sub-tabs
    subtab1, subtab2, subtab3 = st.tabs(["🍚 Thực Phẩm VN", "🏃 Vận Động", "📝 Tính Calories"])
    
    # Subtab 1: Vietnamese Foods
    with subtab1:
        _render_vietnamese_foods()
    
    # Subtab 2: Exercise
    with subtab2:
        _render_exercise_calories()
    
    # Subtab 3: Meal Calculator
    with subtab3:
        _render_meal_calculator()


def _render_vietnamese_foods():
    """Hiển thị database thực phẩm Việt Nam"""
    
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


def _render_exercise_calories():
    """Hiển thị tính toán calories đốt cháy qua vận động"""
    
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
        duration = st.number_input("Thời gian (phút)", min_value=5, max_value=300, value=30)
    with col3:
        weight_ex = st.number_input("Cân nặng (kg)", min_value=30.0, max_value=200.0, value=70.0)
    
    if st.button("Tính toán", type="primary"):
        result = obesity.calculate_calories_burned(activity, duration, weight_ex)
        
        col1, col2 = st.columns(2)
        with col1:
            st.success(f"""
            ### 🔥 {result['calories_burned']:.0f} cal
            **Đã đốt cháy**
            """)
            st.caption(f"💡 {result['note']}")
        
        with col2:
            st.info(f"""
            **Tương đương:**
            
            • {result['equivalent_foods'][0]}
            • {result['equivalent_foods'][1]}
            """)
    
    # Show all exercises
    st.markdown("---")
    st.subheader("📊 Bảng Calories Các Hoạt Động")
    
    for cat_id, cat_data in obesity.EXERCISES_CALORIES.items():
        with st.expander(f"{cat_data['name']}"):
            exercises_list = []
            for activity_name, met in cat_data['activities'].items():
                # Tính cho người 70kg, 30 phút
                calories = met * 70 * 0.5
                exercises_list.append({
                    "Hoạt động": activity_name,
                    "MET": met,
                    "Cal/30p (70kg)": f"{calories:.0f}"
                })
            
            df = pd.DataFrame(exercises_list)
            st.dataframe(df, use_container_width=True, hide_index=True)


def _render_meal_calculator():
    """Hiển thị tính toán calories bữa ăn"""
    
    st.subheader("📝 Tính Calories Bữa Ăn")
    
    st.info("Nhập các món bạn đã ăn, app sẽ tính tổng calories!")
    
    # Input meals
    foods_input = st.text_area(
        "Nhập tên món ăn (mỗi dòng 1 món)",
        placeholder="VD:\nCơm trắng\nThịt kho\nCanh rau",
        height=150
    )
    
    if st.button("Tính Tổng Calories", type="primary"):
        if foods_input:
            foods_list = [f.strip() for f in foods_input.split('\n') if f.strip()]
            result = obesity.calculate_meal_calories(foods_list)
            
            if result['found']:
                st.success(f"### 🍽️ Tổng: {result['total_calories']} cal")
                
                # Show details
                st.markdown("**Chi tiết:**")
                df = pd.DataFrame(result['details'])
                st.dataframe(df, use_container_width=True, hide_index=True)
                
                # Macros
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("🥩 Protein", f"{result['total_protein']}g")
                with col2:
                    st.metric("🍚 Carbs", f"{result['total_carbs']}g")
                with col3:
                    st.metric("🥑 Fat", f"{result['total_fat']}g")
            
            if result['not_found']:
                st.warning(f"Không tìm thấy: {', '.join(result['not_found'])}")

