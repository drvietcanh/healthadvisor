"""
Bệnh Tiền Liệt Tuyến Tab
"""
import streamlit as st

def render_prostate_tab():
    st.header("🔷 Bệnh Tiền Liệt Tuyến - Nam giới trung niên")
    st.markdown("""
    <div class="info-box">
        <b>💡 Hiểu đơn giản:</b><br>
        Tiền liệt tuyến to ra theo tuổi → Chèn ép bàng quang, tiểu khó.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("🔍 Triệu chứng", expanded=True):
        st.markdown("""
        **Dấu hiệu:**
        - Tiểu đêm nhiều lần
        - Tiểu khó, dòng nhỏ
        - Tiểu không hết
        - Đau rát khi tiểu
        """)
    
    with st.expander("💊 Điều trị"):
        st.markdown("""
        **1. Thuốc:**
        - Finasteride, Tamsulosin
        
        **2. Phẫu thuật:**
        - Nếu thuốc không hiệu quả
        
        **Lưu ý:** Khám bác sĩ để chẩn đoán chính xác
        """)
    
    st.markdown("""
    ---
    <div class="warning-box">
        <b>⚠️ QUAN TRỌNG:</b><br>
        • Khám bác sĩ ngay khi có triệu chứng<br>
        • Thông tin chỉ mang tính <b>THAM KHẢO</b>
    </div>
    """, unsafe_allow_html=True)

