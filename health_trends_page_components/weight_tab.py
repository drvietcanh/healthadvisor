"""
Weight Tab for Health Trends Page
Phân tích xu hướng cân nặng
"""

import streamlit as st
from datetime import datetime, timedelta
from health_trends import create_trend_chart


def render_weight_tab(weight_analysis, df, analysis_days):
    """Render tab cân nặng với biểu đồ"""
    
    if weight_analysis:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Cân nặng hiện tại",
                f"{weight_analysis['current']} kg"
            )
        
        with col2:
            st.metric(
                "Thay đổi",
                f"{weight_analysis['change']:+.1f} kg",
                delta=weight_analysis['message']
            )
        
        with col3:
            st.metric(
                "Trung bình",
                f"{weight_analysis['avg']} kg"
            )
        
        # Biểu đồ
        df_filtered = df[df['Ngày'] >= (datetime.now() - timedelta(days=analysis_days))]
        df_filtered = df_filtered.sort_values('Ngày')
        
        if len(df_filtered) > 0 and 'Cân nặng (kg)' in df_filtered.columns:
            fig_weight = create_trend_chart(
                df_filtered[df_filtered['Cân nặng (kg)'].notna()],
                'Cân nặng (kg)',
                'Xu hướng Cân nặng',
                'kg'
            )
            st.plotly_chart(fig_weight, use_container_width=True)
    else:
        st.info("📝 Chưa có đủ dữ liệu cân nặng để phân tích")

