"""
Sốt ở Trẻ Em (Fever in Children) Tab
"""
import streamlit as st

def render_fever_tab():
    """Render tab Sốt ở Trẻ Em"""
    st.header("🌡️ Sốt ở Trẻ Em - Cách xử trí đúng")
    
    st.markdown("""
    <div class="info-box">
        <b>💡 Hiểu đơn giản:</b><br>
        Sốt là dấu hiệu tốt! Nghĩa là cơ thể đang chống lại vi khuẩn/virus.
        Quan trọng: Biết khi nào sốt nhẹ (không lo) và khi nào NGUY HIỂM (phải đưa đi bác sĩ ngay).
    </div>
    """, unsafe_allow_html=True)
    
    # Nguyên nhân
    with st.expander("🔍 Nguyên nhân sốt ở trẻ em", expanded=True):
        st.markdown("""
        ### 🦠 Tại sao trẻ em bị sốt?
        
        **Sốt KHÔNG phải bệnh, mà là DẤU HIỆU:**
        - Cơ thể đang chống lại vi khuẩn/virus
        - Miễn dịch đang hoạt động tốt
        - Giống như "báo động" của cơ thể
        
        ### 🌡️ Nguyên nhân thường gặp:
        
        **1. Cảm cúm thông thường (80%):**
        - Virus cảm, cúm
        - Sốt 38-39°C
        - Kèm ho, sổ mũi
        - Tự khỏi sau 3-5 ngày
        
        **2. Viêm họng/họng amidan:**
        - Vi khuẩn hoặc virus
        - Sốt 38-40°C
        - Đau họng, nuốt khó
        - Trẻ quấy khóc
        
        **3. Tiêu chảy/Ói:**
        - Nhiễm trùng ruột
        - Sốt 37.5-39°C
        - Đi ngoài nhiều lần
        
        **4. Phát ban (Ban sởi, thủy đậu):**
        - Nổi ban đỏ
        - Sốt kèm theo
        
        **5. Viêm tai giữa:**
        - Nhiễm trùng tai
        - Trẻ đau tai, quấy
        
        **6. NGuy hiểm (hiếm):**
        - Viêm màng não
        - Nhiễm trùng máu
        - Sốt xuất huyết
    """)
    
    # Phân loại sốt
    with st.expander("📊 Phân loại sốt"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🟢 Sốt nhẹ (37.5-38°C):
            - **Không cần lo**
            - Cho trẻ nghỉ ngơi
            - Uống nhiều nước
            - Theo dõi thêm
            
            ### 🟡 Sốt vừa (38-39°C):
            - **Cần hạ sốt**
            - Uống thuốc paracetamol
            - Lau người bằng nước ấm
            - Theo dõi sát
            """)
        
        with col2:
            st.markdown("""
            ### 🔴 Sốt cao (39-40°C):
            - **NGUY HIỂM**
            - Hạ sốt ngay
            - Theo dõi chặt chẽ
            - Khám bác sĩ nếu không hạ
            
            ### 🚨 Sốt rất cao (>40°C):
            - **CẤP CỨU**
            - Hạ sốt ngay lập tức
            - Đưa đi bệnh viện NGAY
            - Có thể co giật!
            """)
    
    # Xử trí sốt
    with st.expander("💊 Cách hạ sốt cho trẻ"):
        st.markdown("""
        ### ✅ Thuốc hạ sốt:
        
        **1. Paracetamol (Hapacol, Efferalgan):**
        - **Liều:** 10-15mg/kg cân nặng
        - **Ví dụ:** Trẻ 10kg = 100-150mg
        - **Cách dùng:** 4-6 giờ/lần (tối đa 4 lần/ngày)
        - **Dạng:** Thuốc nước, viên, đạn hậu môn
        - **Giá:** ~30.000-50.000 VNĐ
        
        **2. Ibuprofen (Brufen, Nurofen):**
        - **Liều:** 5-10mg/kg cân nặng
        - **Cho trẻ >6 tháng**
        - **Cách dùng:** 6-8 giờ/lần
        - **Lưu ý:** Không dùng khi sốt xuất huyết
        
        ### 🧴 Cách lau người hạ sốt:
        **Chuẩn bị:**
        - Nước ấm (37-38°C), không lạnh!
        - 2-3 khăn mềm
        - Chăn mỏng
        
        **Cách làm:**
        1. Lau vùng nách, háng (5 phút)
        2. Lau toàn thân (15-20 phút)
        3. Lau đầu, cổ
        4. Mặc quần áo mỏng, thoáng
        5. Đo lại nhiệt độ sau 30 phút
        
        ⚠️ **KHÔNG:**
        - Lau bằng nước lạnh
        - Lau bằng rượu/cồn
        - Đắp chăn ủ kín
    """)
    
    # Khi nào cần khám bác sĩ
    with st.expander("🚨 Khi nào PHẢI đưa trẻ đi bác sĩ NGAY?"):
        st.markdown("""
        ### 🔴 Đưa đi NGAY nếu:
        
        **1. Trẻ <3 tháng:**
        - Sốt >38°C
        - Cần khám BẤT KỲ lúc nào
        
        **2. Trẻ 3-6 tháng:**
        - Sốt >38.5°C
        - Không hạ sau khi uống thuốc
        
        **3. Trẻ >6 tháng:**
        - Sốt >40°C
        - Sốt >3 ngày không hạ
        - Không hạ sau khi uống thuốc
        
        **4. Có triệu chứng NGUY HIỂM:**
        - **Co giật**
        - **Nôn ói liên tục**
        - **Khó thở**
        - **Phát ban đỏ**
        - **Cổ cứng**
        - **Hôn mê, khó đánh thức**
        - **Da tím tái**
        - **Bỏ bú, bỏ ăn hoàn toàn**
        - **Khóc ngất**
        
        **5. Có dấu hiệu mất nước:**
        - Không đi tiểu >6 giờ
        - Miệng khô
        - Mắt trũng
        - Không có nước mắt khi khóc
    """)
    
    # Co giật do sốt
    with st.expander("⚠️ Co giật do sốt cao"):
        st.markdown("""
        ### 🚨 Khi trẻ co giật:
        
        **Dấu hiệu:**
        - Co giật toàn thân
        - Mắt trợn ngược
        - Trẻ không tỉnh
        - Thường xảy ra khi sốt >39°C
        
        **XỬ TRÍ NGAY:**
        1. **Đặt trẻ nằm nghiêng** → Tránh nuốt lưỡi, sặc
        2. **Không cho gì vào miệng** → Dễ gây tắc đường thở
        3. **Không giữ chặt** → Làm gãy xương
        4. **Dùng thuốc đạn hậu môn** → Paracetamol hoặc Diazepam
        5. **Đưa đi bệnh viện ngay** → Sau cơn co giật
        
        **Sau cơn co giật:**
        - Trẻ sẽ ngủ
        - Vẫn cần khám bác sĩ
        - Có thể tái phát nếu sốt lại
        
        **Phòng ngừa:**
        - Uống thuốc hạ sốt sớm
        - Theo dõi thân nhiệt
        - Không để sốt >38.5°C
    """)
    
    # Chăm sóc tại nhà
    with st.expander("🏠 Chăm sóc trẻ sốt tại nhà"):
        st.markdown("""
        ### ✅ Những việc NÊN làm:
        
        **1. 💧 Cho uống nhiều nước:**
        - Nước lọc
        - Nước Oresol (khi tiêu chảy)
        - Nước trái cây pha loãng
        - Tránh nước có đường nhiều
        
        **2. 👕 Mặc quần áo thoáng:**
        - Áo mỏng, rộng
        - Không đắp chăn dày
        - Nếu lạnh: Đắp chăn mỏng
        
        **3. 🏠 Nghỉ ngơi:**
        - Không cho ra ngoài
        - Nghỉ ở nhà, tránh gió
        - Ngủ đủ giấc
        
        **4. 🌡️ Theo dõi thân nhiệt:**
        - Đo mỗi 2-4 giờ
        - Ghi nhận nhiệt độ
        - Theo dõi các triệu chứng
        
        **5. 🍎 Ăn uống nhẹ:**
        - Nếu trẻ chán ăn: Không ép
        - Uống sữa, nước
        - Ăn cháo loãng nếu muốn
        
        ### ❌ Những việc KHÔNG nên làm:
        - Đắp chăn ủ kín
        - Lau bằng nước lạnh
        - Lau bằng rượu/cồn
        - Tự ý dùng kháng sinh
        - Vượt quá liều thuốc
    """)
    
    # FAQ
    st.markdown("---")
    st.subheader("❓ Câu hỏi thường gặp")
    
    with st.expander("🤔 Sốt bao nhiêu độ là nguy hiểm?"):
        st.markdown("""
        **Tùy theo tuổi:**
        - Trẻ <3 tháng: **>38°C = Đưa đi bác sĩ**
        - Trẻ 3-6 tháng: **>38.5°C = Nên khám**
        - Trẻ >6 tháng: **>40°C = Cấp cứu**
        
        **Nhưng QUAN TRỌNG hơn nhiệt độ:**
        - **Trạng thái trẻ** (hoạt động bình thường vs nằm liệt)
        - **Có co giật không**
        - **Có khó thở không**
        - **Có nôn ói không**
        
        💡 **Nhiệt độ cao + Trẻ vẫn chơi = Ít lo hơn**  
        💡 **Nhiệt độ vừa + Trẻ nằm liệt = NGUY HIỂM!**
        """)
    
    with st.expander("🤔 Trẻ sốt bao lâu phải đưa đi bệnh viện?"):
        st.markdown("""
        **Thời gian:**
        - **<3 ngày:** Theo dõi tại nhà
        - **3-5 ngày:** Nên khám bác sĩ
        - **>5 ngày:** Phải khám
        - **Kèm triệu chứng nguy hiểm:** Đưa đi NGAY
        
        **Dấu hiệu CẦN đi:**
        - Không hạ sau khi uống thuốc
        - Sốt tăng cao dần
        - Kèm ho dữ dội
        - Tiêu chảy nhiều
        - Trẻ lừ đừ, không chịu ăn
        """)
    
    with st.expander("🤔 Tại sao không được lau bằng nước lạnh?"):
        st.markdown("""
        **Nước lạnh gây NGUY HIỂM:**
        1. Làm co mạch máu → Sốt khó hạ
        2. Rét run → Sốt tăng cao hơn
        3. Tim đập nhanh → Ảnh hưởng tim
        4. Trẻ khó chịu, hoảng sợ
        
        **Đúng:** Nước ấm 37-38°C
        - Giãn mạch máu → Dễ hạ sốt
        - Trẻ dễ chịu hơn
        - An toàn cho tim
        
        💡 **Nhớ:** Nước ấm bằng nhiệt độ nước tắm bình thường!
        """)
    
    # Cảnh báo cuối
    st.markdown("""
    ---
    <div class="warning-box">
        <b>⚠️ QUAN TRỌNG:</b><br>
        • Sốt là dấu hiệu tốt - Cơ thể đang chống bệnh<br>
        • Trẻ <3 tháng sốt >38°C: Đưa đi bác sĩ NGAY<br>
        • Co giật + Sốt cao: Xử trí đúng cách, đưa đi cấp cứu<br>
        • Thông tin trên chỉ mang tính chất <b>THAM KHẢO</b><br>
        • <b>KHÔNG THAY THẾ</b> tư vấn của bác sĩ<br>
        • Khi nghi ngờ: <b>KHÁM BÁC SĨ</b>
    </div>
    """, unsafe_allow_html=True)

