"""
Rối Loạn Kinh Nguyệt Tab - Women's Health
"""
import streamlit as st

def render_menstruation_tab():
    """Render tab Rối Loạn Kinh Nguyệt"""
    st.header("🩸 Rối Loạn Kinh Nguyệt - Chu kỳ bất thường")
    
    st.markdown("""
    <div class="info-box">
        <b>💡 Hiểu đơn giản:</b><br>
        Kinh nguyệt bình thường: 28-35 ngày, kéo dài 3-7 ngày.
        Bất thường: Quá ngắn/dài, quá ít/nhiều, không đều.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("🔍 Phân loại rối loạn", expanded=True):
        st.markdown("""
        ### 🩸 Các loại:
        
        **1. Kinh nguyệt không đều:**
        - Chu kỳ <21 ngày hoặc >35 ngày
        - Không đều từng tháng
        
        **2. Kinh nguyệt quá nhiều:**
        - >7 ngày
        - Ra máu nhiều (>80ml)
        - Thiếu máu
        
        **3. Kinh nguyệt quá ít:**
        - <3 ngày
        - Ra máu ít (<20ml)
        
        **4. Vô kinh:**
        - Không có kinh >3 tháng
    """)
    
    with st.expander("💊 Nguyên nhân"):
        st.markdown("""
        ### 🦠 Nguyên nhân:
        - **Hormone:** Rối loạn nội tiết
        - **Buồng trứng:** U nang, PCOS
        - **Stress:** Căng thẳng
        - **Thay đổi cân nặng:** Béo phì, gầy
        - **Tập luyện:** Gắng sức quá
        """)
    
    st.markdown("""
    ---
    <div class="warning-box">
        <b>⚠️ QUAN TRỌNG:</b><br>
        • Khám bác sĩ nếu bất thường kéo dài<br>
        • Uống thuốc theo chỉ định<br>
        • Theo dõi chu kỳ thường xuyên<br>
        • Thông tin chỉ mang tính <b>THAM KHẢO</b>
    </div>
    """, unsafe_allow_html=True)

