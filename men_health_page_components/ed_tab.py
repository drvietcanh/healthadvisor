"""
Rối Loạn Cương Dương Tab
"""
import streamlit as st

def render_ed_tab():
    st.header("🔧 Rối Loạn Cương Dương - Vấn đề phổ biến ở nam giới")
    st.markdown("""
    <div class="info-box">
        <b>💡 Hiểu đơn giản:</b><br>
        Không cương được hoặc cương không đủ để quan hệ. 
        Rất phổ biến, có thể điều trị được.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("🔍 Nguyên nhân", expanded=True):
        st.markdown("""
        **1. Tim mạch (thường gặp):**
        - Cao huyết áp, mỡ máu cao
        - Xơ vữa mạch máu
        
        **2. Tâm lý:**
        - Stress, lo lắng
        - Căng thẳng công việc
        
        **3. Thuốc:**
        - Thuốc huyết áp, trầm cảm
        - Thuốc tiêu hóa
        
        **4. Lối sống:**
        - Hút thuốc, rượu bia
        - Ít vận động
        """)
    
    with st.expander("💊 Điều trị"):
        st.markdown("""
        **1. Viagra (Sildenafil):**
        - 50-100mg, uống 30-60 phút trước
        - Hiệu quả 70-85%
        
        **2. Cialis (Tadalafil):**
        - 10-20mg, tác dụng lâu hơn
        
        **Lưu ý:**
        - Uống theo chỉ định bác sĩ
        - Không uống với rượu
        - Tác dụng phụ: Đau đầu, chóng mặt
        """)
    
    st.markdown("""
    ---
    <div class="warning-box">
        <b>⚠️ QUAN TRỌNG:</b><br>
        • Đây là bệnh có thể điều trị<br>
        • Không tự ti, khám bác sĩ<br>
        • Thông tin chỉ mang tính <b>THAM KHẢO</b>
    </div>
    """, unsafe_allow_html=True)

