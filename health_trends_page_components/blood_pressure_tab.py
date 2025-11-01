"""
Blood Pressure Tab for Health Trends Page
Phân tích xu hướng huyết áp
"""

import streamlit as st
from datetime import datetime, timedelta
from health_trends import create_trend_chart


def render_blood_pressure_tab(bp_analysis, df, analysis_days):
    """Render tab huyết áp với biểu đồ"""
    
    if bp_analysis:
        # Thông tin tổng quan
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Huyết áp trung bình",
                f"{bp_analysis['avg_systolic']}/{bp_analysis['avg_diastolic']}",
                delta=f"{bp_analysis['systolic_trend']['change_percent']}%"
            )
        
        with col2:
            st.metric(
                "Phân loại",
                bp_analysis['category']
            )
        
        with col3:
            trend_emoji = {"increasing": "📈", "decreasing": "📉", "stable": "➡️"}
            st.metric(
                "Xu hướng 7 ngày",
                trend_emoji.get(bp_analysis['systolic_trend']['trend'], "➡️") + 
                " " + bp_analysis['systolic_trend']['trend'].capitalize()
            )
        
        # Biểu đồ xu hướng huyết áp tâm thu
        df_filtered = df[df['Ngày'] >= (datetime.now() - timedelta(days=analysis_days))]
        df_filtered = df_filtered.sort_values('Ngày')
        
        if len(df_filtered) > 0:
            fig_bp = create_trend_chart(
                df_filtered[df_filtered['Huyết áp tâm thu'].notna()],
                'Huyết áp tâm thu',
                'Xu hướng Huyết áp Tâm thu',
                'mmHg',
                reference_lines={
                    'Bình thường': (120, 'normal'),
                    'Cao': (140, 'danger')
                }
            )
            st.plotly_chart(fig_bp, use_container_width=True)
            
            # Biểu đồ tâm trương
            fig_bp_dia = create_trend_chart(
                df_filtered[df_filtered['Huyết áp tâm trương'].notna()],
                'Huyết áp tâm trương',
                'Xu hướng Huyết áp Tâm trương',
                'mmHg',
                reference_lines={
                    'Bình thường': (80, 'normal'),
                    'Cao': (90, 'danger')
                }
            )
            st.plotly_chart(fig_bp_dia, use_container_width=True)
    else:
        st.info("📝 Chưa có đủ dữ liệu huyết áp để phân tích")

