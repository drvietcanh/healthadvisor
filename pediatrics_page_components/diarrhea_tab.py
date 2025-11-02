"""
Tiêu Chảy ở Trẻ Em (Diarrhea in Children) Tab
"""
import streamlit as st

def render_diarrhea_tab():
    """Render tab Tiêu Chảy ở Trẻ Em"""
    st.header("💩 Tiêu Chảy ở Trẻ Em - Phòng ngừa mất nước")
    
    st.markdown("""
    <div class="info-box">
        <b>💡 Hiểu đơn giản:</b><br>
        Tiêu chảy = Đi ngoài nhiều lần, phân lỏng. Nguy hiểm nhất là MẤT NƯỚC.
        Quan trọng: Cho uống Oresol đúng cách để tránh mất nước nặng.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("🔍 Nguyên nhân & Triệu chứng", expanded=True):
        st.markdown("""
        ### 🦠 Nguyên nhân:
        **1. Virus (Rotavirus - 80%):**
        - Lây qua tay, thức ăn
        - Đi ngoài nhiều, nước
        
        **2. Vi khuẩn (E.coli, Salmonella):**
        - Ăn thực phẩm nhiễm bẩn
        - Có thể có máu
        
        **3. Ký sinh trùng:**
        - Giardia, Amip
        - Kéo dài nhiều ngày
        
        ### ⚕️ Triệu chứng:
        - **Đi ngoài >3 lần/ngày**
        - **Phân lỏng, nước**
        - **Có thể ói**
        - **Sốt nhẹ**
        - **Mệt mỏi**
    """)
    
    with st.expander("💊 Xử trí tại nhà"):
        st.markdown("""
        ### ✅ Bù nước bằng Oresol:
        
        **Cách pha Oresol:**
        - 1 gói Oresol + 200ml nước
        - Khuấy đều
        - Cho uống từng chút một
        
        **Cách cho uống:**
        - Mỗi lần đi ngoài: Uống 100-200ml
        - Uống từng chút, không ép
        - Nếu ói: Đợi 10 phút, uống lại chậm hơn
        
        **Lưu ý:**
        - Không pha quá đặc hoặc quá loãng
        - Không pha với sữa, nước trái cây
        - Pha xong dùng trong 24h
        
        ### 🍎 Ăn uống:
        - **Tiếp tục cho bú sữa** (nếu <6 tháng)
        - **Ăn cháo, cơm** (nếu lớn hơn)
        - **Tránh:** Sữa bò, nước ngọt
    """)
    
    with st.expander("🚨 Khi nào đưa đi bệnh viện"):
        st.markdown("""
        ### 🔴 Đưa đi NGAY nếu:
        - **Đi ngoài >10 lần/ngày**
        - **Không đi tiểu >6 giờ** → Mất nước nặng
        - **Miệng khô, mắt trũng**
        - **Không có nước mắt khi khóc**
        - **Lừ đừ, khó đánh thức**
        - **Có máu trong phân**
        - **Ói liên tục, không uống được**
        - **Trẻ <6 tháng**
    """)
    
    # FAQ
    st.markdown("---")
    st.subheader("❓ Câu hỏi thường gặp")
    
    with st.expander("🤔 Làm sao biết trẻ bị mất nước?"):
        st.markdown("""
        **Dấu hiệu mất nước:**
        1. **Không đi tiểu >6 giờ**
        2. **Miệng khô** → Không có nước bọt
        3. **Mắt trũng** → Trũng vào trong
        4. **Không có nước mắt** → Khóc không ra nước mắt
        5. **Da khô, nhăn nheo**
        6. **Lừ đừ** → Không chịu chơi
        
        **→ Cần truyền dịch ngay!**
        """)
    
    st.markdown("""
    ---
    <div class="warning-box">
        <b>⚠️ QUAN TRỌNG:</b><br>
        • Tiêu chảy nguy hiểm nhất: MẤT NƯỚC<br>
        • Cho uống Oresol đúng cách<br>
        • Mất nước nặng → Truyền dịch ngay<br>
        • Thông tin trên chỉ mang tính chất <b>THAM KHẢO</b><br>
        • <b>KHÔNG THAY THẾ</b> tư vấn của bác sĩ
    </div>
    """, unsafe_allow_html=True)

