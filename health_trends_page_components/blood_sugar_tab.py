"""
Blood Sugar Tab for Health Trends Page
Phân tích xu hướng đường huyết
"""

import streamlit as st
from datetime import datetime, timedelta
from health_trends import create_trend_chart


def render_blood_sugar_tab(bs_analysis, df, analysis_days):
    """Render tab đường huyết với biểu đồ"""
    
    if bs_analysis:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Đường huyết TB",
                f"{bs_analysis['avg']} mmol/L",
                delta=f"{bs_analysis['trend']['change_percent']}%"
            )
        
        with col2:
            st.metric(
                "Phân loại",
                bs_analysis['category']
            )
        
        with col3:
            if bs_analysis['low_count'] > 0:
                st.metric("⚠️ Hạ đường huyết", f"{bs_analysis['low_count']} lần")
            else:
                st.metric("Cao (>7.0)", f"{bs_analysis['high_count']} lần")
        
        # Biểu đồ
        df_filtered = df[df['Ngày'] >= (datetime.now() - timedelta(days=analysis_days))]
        df_filtered = df_filtered.sort_values('Ngày')
        
        if len(df_filtered) > 0 and 'Đường huyết' in df_filtered.columns:
            fig_bs = create_trend_chart(
                df_filtered[df_filtered['Đường huyết'].notna()],
                'Đường huyết',
                'Xu hướng Đường huyết',
                'mmol/L',
                reference_lines={
                    'Bình thường': (5.6, 'normal'),
                    'Tiền ĐTĐ': (7.0, 'warning'),
                    'Hạ': (3.9, 'danger')
                }
            )
            st.plotly_chart(fig_bs, use_container_width=True)
    else:
        st.info("📝 Chưa có đủ dữ liệu đường huyết để phân tích")

