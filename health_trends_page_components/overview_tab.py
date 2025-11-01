"""
Overview Tab for Health Trends Page
Hiển thị điểm sức khỏe tổng thể và cảnh báo
"""

import streamlit as st


def render_overview_tab(bp_analysis, bs_analysis, weight_analysis, overall, all_alerts):
    """Render phần tổng quan: điểm sức khỏe và cảnh báo"""
    
    # =============== ĐIỂM SỨC KHỎE TỔNG THỂ ===============
    st.header("🎯 Điểm Sức khỏe Tổng thể")
    
    col_score1, col_score2, col_score3 = st.columns([2, 2, 3])
    
    with col_score1:
        # Điểm số lớn
        st.markdown(f"""
        <div style='text-align: center; padding: 30px; 
                    background: linear-gradient(135deg, #{overall['color']}44 0%, #{overall['color']}22 100%);
                    border-radius: 15px; border: 3px solid {overall['color']};'>
            <h1 style='font-size: 72px; margin: 0; color: {overall['color']};'>
                {overall['score']}
            </h1>
            <p style='font-size: 24px; margin: 10px 0 0 0;'>/ 100 điểm</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_score2:
        st.markdown(f"""
        <div style='text-align: center; padding: 30px;'>
            <p style='font-size: 64px; margin: 0;'>{overall['emoji']}</p>
            <h2 style='margin: 10px 0;'>{overall['rating']}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col_score3:
        st.markdown("### 📊 Phân tích:")
        if overall['positive_trends'] > 0:
            st.success(f"✅ {overall['positive_trends']} chỉ số đang cải thiện")
        if overall['negative_trends'] > 0:
            st.warning(f"⚠️ {overall['negative_trends']} chỉ số đang xấu đi")
        
        if overall['issues']:
            st.markdown("**Vấn đề cần chú ý:**")
            for issue in overall['issues'][:3]:  # Hiển thị tối đa 3
                st.markdown(f"- {issue}")
    
    st.divider()
    
    # =============== CẢNH BÁO ===============
    if all_alerts:
        st.header("🚨 Cảnh báo")
        
        for alert in all_alerts[:5]:  # Hiển thị tối đa 5 cảnh báo
            if alert['type'] == 'danger':
                st.error(f"### {alert['title']}\n{alert['message']}")
            elif alert['type'] == 'warning':
                st.warning(f"### {alert['title']}\n{alert['message']}")
            else:
                st.info(f"### {alert['title']}\n{alert['message']}")
        
        st.divider()

