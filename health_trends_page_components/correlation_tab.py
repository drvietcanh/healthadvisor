"""
Correlation Tab for Health Trends Page
Phân tích mối liên hệ giữa các chỉ số
"""

import streamlit as st
from health_trends import create_correlation_chart


def render_correlation_tab(df):
    """Render tab mối liên hệ với biểu đồ tương quan"""
    
    st.markdown("### 🔗 Mối liên hệ giữa các chỉ số")
    st.info("💡 Cân nặng và huyết áp thường có mối liên hệ với nhau. Giảm cân có thể giúp giảm huyết áp.")
    
    fig_corr = create_correlation_chart(df)
    
    if fig_corr:
        st.plotly_chart(fig_corr, use_container_width=True)
        
        # Giải thích
        st.markdown("""
        **Cách đọc biểu đồ:**
        - Mỗi điểm = 1 lần đo
        - Màu đỏ = Huyết áp cao
        - Màu vàng/xanh = Huyết áp tốt hơn
        - Nếu điểm tập trung theo đường chéo lên → Cân nặng tăng, huyết áp cũng tăng
        """)
    else:
        st.info("📝 Cần thêm dữ liệu để phân tích mối liên hệ")

