"""
Học Dễ Page - Explanations Tab
Tab Giải thích đơn giản
"""

import streamlit as st
from core.simple_explanations import EVERYDAY_EXAMPLES


def render_explanations_tab():
    """Render tab Giải thích đơn giản"""
    st.header("💡 Giải thích bệnh bằng ví dụ đời thường")
    
    topic = st.selectbox(
        "Chọn chủ đề muốn tìm hiểu:",
        [
            "💓 Huyết áp cao là gì?",
            "🍬 Tiểu đường là gì?",
            "💔 Suy tim là gì?",
            "🧠 Đột quỵ là gì?"
        ]
    )
    
    topic_map = {
        "💓 Huyết áp cao là gì?": "blood_pressure",
        "🍬 Tiểu đường là gì?": "diabetes",
        "💔 Suy tim là gì?": "heart_failure",
        "🧠 Đột quỵ là gì?": "stroke"
    }
    
    selected_topic = topic_map[topic]
    
    # Hiển thị giải thích
    st.markdown(EVERYDAY_EXAMPLES[selected_topic]["simple_vn"])
    
    # Hiển thị visual
    if "visual" in EVERYDAY_EXAMPLES[selected_topic]:
        st.code(EVERYDAY_EXAMPLES[selected_topic]["visual"], language="")
    
    st.divider()
    
    # Video giải thích (giả lập)
    st.info("💡 **MẸO HỌC:** Đọc lại 3 lần → Kể lại cho người thân → Nhớ lâu!")

