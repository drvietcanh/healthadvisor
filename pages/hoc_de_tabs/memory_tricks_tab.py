"""
Học Dễ Page - Memory Tricks Tab
Tab Mẹo nhớ
"""

import streamlit as st
from core.simple_explanations import MEMORY_TRICKS


def render_memory_tricks_tab():
    """Render tab Mẹo nhớ"""
    st.header("🧠 Mẹo nhớ siêu dễ")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Nhớ BE-FAST")
        st.markdown(MEMORY_TRICKS["befast_easy"])
        
        # Test ngay
        if st.button("🎮 Test ngay!", key="test_befast"):
            st.success("""
**HÃY THỬ NGAY:**

1. **CƯỜI** → Xem gương → Lệch miệng không?
2. **GIƠ 2 TAY** → 1 tay sa xuống không?
3. **NÓI**: "Hôm nay trời đẹp" → Nói rõ không?

✅ Tất cả OK = Bình thường
❌ Có 1 dấu hiệu = GỌI 115!
""")
    
    with col2:
        st.subheader("📊 Nhớ đường huyết")
        st.markdown(MEMORY_TRICKS["blood_sugar_levels"])
        
        # Quiz
        if st.button("❓ Câu hỏi kiểm tra", key="quiz_sugar"):
            st.info("""
**Đường huyết đói 6.5 mmol/L là gì?**

A. Bình thường ✅
B. Tiền tiểu đường ⚠️
C. Tiểu đường 🔴

**Đáp án:** B - Tiền tiểu đường (6 nằm giữa 5 và 7!)
""")
    
    st.divider()
    
    st.subheader("🧂 Mẹo giảm muối")
    st.markdown(MEMORY_TRICKS["salt_reduction"])

