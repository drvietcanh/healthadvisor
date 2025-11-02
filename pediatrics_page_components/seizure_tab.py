"""
Động Kinh ở Trẻ Em (Seizures in Children) Tab
"""
import streamlit as st

def render_seizure_tab():
    """Render tab Động Kinh ở Trẻ Em"""
    st.header("⚡ Động Kinh ở Trẻ Em - Xử trí cơn co giật")
    
    st.markdown("""
    <div class="info-box">
        <b>💡 Hiểu đơn giản:</b><br>
        Động kinh = Co giật do não phóng điện bất thường. 
        Quan trọng: Xử trí đúng khi trẻ co giật để tránh nguy hiểm.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("🔍 Nguyên nhân & Triệu chứng", expanded=True):
        st.markdown("""
        ### 🧠 Nguyên nhân:
        **1. Sốt cao (phổ biến nhất):**
        - Sốt >39°C gây co giật
        - Thường không nguy hiểm
        
        **2. Động kinh thực sự:**
        - Não phóng điện bất thường
        - Tái phát nhiều lần
        
        **3. Nguyên nhân khác:**
        - Chấn thương đầu
        - Nhiễm trùng não
        - Rối loạn chuyển hóa
        
        ### ⚕️ Triệu chứng:
        - **Co giật toàn thân**
        - **Mắt trợn ngược**
        - **Không tỉnh**
        - **Nghiến răng**
        - **Có thể són tiểu**
    """)
    
    with st.expander("⚠️ Xử trí khi trẻ co giật"):
        st.markdown("""
        ### ✅ XỬ TRÍ NGAY:
        
        **1. Đặt trẻ nằm nghiêng:**
        - Tránh nuốt lưỡi
        - Tránh sặc
        - Nằm nơi an toàn, không có đồ vật sắc nhọn
        
        **2. KHÔNG cho gì vào miệng:**
        - KHÔNG đưa khăn, muỗng
        - KHÔNG ép hàm mở
        - Dễ gây gãy răng, tắc đường thở
        
        **3. Dùng thuốc đạn hậu môn:**
        - Nếu sốt: Paracetamol 15mg/kg
        - Nếu động kinh: Diazepam 0.5mg/kg
        - Đợi cơn ngưng
        
        **4. Đưa đi bệnh viện:**
        - Sau cơn co giật
        - Nếu cơn kéo dài >5 phút → Gọi 115
        
        ### ❌ KHÔNG LÀM:
        - Ép giữ chặt trẻ
        - Cho nước hay thuốc khi đang co giật
        - Đưa vào miệng
    """)
    
    with st.expander("💊 Điều trị"):
        st.markdown("""
        ### ✅ Thuốc chống động kinh:
        
        **1. Phenobarbital:**
        - Uống hàng ngày
        - Ngăn ngừa cơn co giật
        
        **2. Valproate:**
        - Uống 2-3 lần/ngày
        
        **3. Carbamazepine:**
        - Cho trẻ lớn
        
        **⚠️ Lưu ý:**
        - Uống theo chỉ định bác sĩ
        - KHÔNG tự ý bỏ thuốc
        - Uống đúng giờ
        - Theo dõi tác dụng phụ
    """)
    
    # FAQ
    st.markdown("---")
    st.subheader("❓ Câu hỏi thường gặp")
    
    with st.expander("🤔 Co giật do sốt có nguy hiểm không?"):
        st.markdown("""
        **Thường KHÔNG nguy hiểm:**
        - Xảy ra khi sốt >39°C
        - Không ảnh hưởng lâu dài
        - Không gây tổn thương não
        
        **Cần làm:**
        - Hạ sốt sớm
        - Theo dõi khi sốt
        - Uống thuốc hạ sốt đúng liều
        
        **Nguy hiểm nếu:**
        - Cơn kéo dài >15 phút
        - Tái phát nhiều lần trong ngày
        - Có tổn thương não
        """)
    
    st.markdown("""
    ---
    <div class="warning-box">
        <b>⚠️ QUAN TRỌNG:</b><br>
        • Co giật: Đặt nằm nghiêng, KHÔNG đưa gì vào miệng<br>
        • Cơn >5 phút: Gọi 115 NGAY<br>
        • Uống thuốc theo chỉ định, đúng giờ<br>
        • Thông tin trên chỉ mang tính chất <b>THAM KHẢO</b><br>
        • <b>KHÔNG THAY THẾ</b> tư vấn của bác sĩ
    </div>
    """, unsafe_allow_html=True)

