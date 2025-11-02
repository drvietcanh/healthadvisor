"""
General Health Tips - Temperature Guide
Hướng dẫn đo nhiệt độ
"""

import streamlit as st


def render_temperature_guide():
    """Hướng dẫn đo nhiệt độ"""
    st.subheader("🌡️ Cách đo nhiệt độ đúng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### ✅ Cách đo ở NÁCH (phổ biến nhất):
        
        1. **Chuẩn bị:**
           - Lắc nhiệt kế thủy ngân xuống dưới 35°C
           - Lau khô nách
        
        2. **Đo:**
           - Đặt đầu nhiệt kế vào giữa nách
           - Ép cánh tay sát vào ngực
           - Giữ 5-10 phút (nhiệt kế thủy ngân) hoặc đến khi kêu "bíp" (nhiệt kế điện tử)
        
        3. **Đọc kết quả:**
           - Đọc số trên vạch đỏ
           - Nhiệt độ nách + 0.5°C = Nhiệt độ thực
           - VD: Đo nách 37.5°C → Nhiệt độ thực ≈ 38°C
        """)
    
    with col2:
        st.markdown("""
        ### ✅ Cách đo ở MIỆNG (người lớn):
        
        1. **Chuẩn bị:**
           - Không uống nước nóng/lạnh 30 phút trước
           - Đặt nhiệt kế dưới lưỡi
        
        2. **Đo:**
           - Ngậm miệng, thở bằng mũi
           - Giữ 3-5 phút
           - Nhiệt độ miệng + 0.3°C = Nhiệt độ thực
        
        ### ⚠️ Lưu ý:
        - Trẻ nhỏ không đo miệng (dễ cắn vỡ)
        - Nhiệt kế điện tử: Đọc kỹ hướng dẫn
        - Nhiệt kế hồng ngoại: Đo tai hoặc trán (nhanh nhưng kém chính xác hơn)
        """)
    
    st.warning("""
    ⚠️ **TRÁNH SAI LẦM:**
    - ❌ Đo ngay sau khi ăn/uống (sai số cao)
    - ❌ Đo khi vừa tắm/vận động (thân nhiệt chưa ổn định)
    - ❌ Dùng nhiệt kế thủy ngân với trẻ nhỏ (nguy hiểm nếu vỡ)
    - ❌ Đo không đủ thời gian (kết quả sai)
    """)

