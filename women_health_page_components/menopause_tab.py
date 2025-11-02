"""
Mãn Kinh Tab - Women's Health
"""
import streamlit as st

def render_menopause_tab():
    """Render tab Mãn Kinh"""
    st.header("🔄 Mãn Kinh - Giai đoạn tự nhiên của phụ nữ")
    
    st.markdown("""
    <div class="info-box">
        <b>💡 Hiểu đơn giản:</b><br>
        Mãn kinh = Hết kinh vĩnh viễn. Tuổi thường gặp: 45-55 tuổi.
        Đây là giai đoạn TỰ NHIÊN, không phải bệnh. Nhưng triệu chứng có thể khó chịu.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("🔍 Mãn kinh là gì?", expanded=True):
        st.markdown("""
        ### 🩸 Định nghĩa:
        - **Mãn kinh:** Hết kinh 12 tháng liên tục
        - **Tuổi thường gặp:** 45-55 tuổi
        - **Trung bình:** 51 tuổi
        
        ### 🔄 Giai đoạn:
        **1. Tiền mãn kinh (2-8 năm):**
        - Kinh nguyệt thất thường
        - Bắt đầu triệu chứng
        - Tuổi: 45-50
        
        **2. Mãn kinh:**
        - Hết kinh 12 tháng
        - Triệu chứng mạnh nhất
        
        **3. Sau mãn kinh:**
        - Triệu chứng giảm dần
        - Tăng nguy cơ loãng xương
    """)
    
    with st.expander("⚕️ Triệu chứng"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🔴 Triệu chứng phổ biến:
            - **Nóng bừng:** Đỏ mặt, ra mồ hôi
            - **Đổ mồ hôi đêm**
            - **Tim đập nhanh**
            - **Mất ngủ**
            - **Tâm trạng thay đổi**
            """)
        
        with col2:
            st.markdown("""
            ### 🟡 Triệu chứng khác:
            - **Khô âm đạo**
            - **Đau khi quan hệ**
            - **Da khô, tóc rụng**
            - **Tăng cân**
            - **Loãng xương**
            """)
    
    with st.expander("💊 Điều trị"):
        st.markdown("""
        ### ✅ Liệu pháp hormone (HRT):
        
        **Khi nào dùng:**
        - Triệu chứng nặng (nóng bừng)
        - Nguy cơ loãng xương
        - Không có chống chỉ định
        
        **Lưu ý:**
        - Chỉ uống theo chỉ định bác sĩ
        - Theo dõi tác dụng phụ
        - Tăng nguy cơ ung thư vú
        
        ### 🌿 Biện pháp tự nhiên:
        - Tập thể dục thường xuyên
        - Ăn uống đủ dinh dưỡng
        - Tránh rượu bia, thuốc lá
        - Thư giãn, giảm stress
    """)
    
    st.markdown("""
    ---
    <div class="warning-box">
        <b>⚠️ QUAN TRỌNG:</b><br>
        • Mãn kinh là tự nhiên, không phải bệnh<br>
        • Triệu chứng có thể điều trị được<br>
        • Khám bác sĩ để được tư vấn<br>
        • Thông tin chỉ mang tính <b>THAM KHẢO</b>
    </div>
    """, unsafe_allow_html=True)

