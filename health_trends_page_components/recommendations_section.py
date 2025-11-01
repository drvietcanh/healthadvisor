"""
Recommendations Section for Health Trends Page
Hiển thị gợi ý cải thiện
"""

import streamlit as st


def render_recommendations_section(recommendations):
    """Render phần gợi ý cải thiện"""
    
    if not recommendations:
        return
    
    st.header("💡 Gợi ý Cải thiện")
    
    cols = st.columns(2)
    
    for idx, rec in enumerate(recommendations):
        with cols[idx % 2]:
            st.markdown(f"""
            <div style='padding: 20px; background: #f8f9fa; border-radius: 10px; 
                        border-left: 4px solid #4CAF50; margin-bottom: 15px;'>
                <h4 style='margin: 0 0 10px 0;'>{rec['icon']} {rec['title']}</h4>
                <p style='margin: 0;'>{rec['message']}</p>
            </div>
            """, unsafe_allow_html=True)

