"""
Tab Mục Tiêu - Đặt mục tiêu giảm cân và theo dõi tiến trình
"""
import streamlit as st
from diseases.metabolic import obesity


def render_goals_tab():
    """Render tab mục tiêu & kế hoạch"""
    
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
        _display_goal_details()
    
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


def _display_goal_details():
    """Hiển thị chi tiết mục tiêu"""
    
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
            
            # Next milestone
            if progress['next_milestone']:
                nm = progress['next_milestone']
                st.success(f"🎯 **Mốc tiếp theo:** {nm['percentage']}% ({nm['weight']} kg)")

