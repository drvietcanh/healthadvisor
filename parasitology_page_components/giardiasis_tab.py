"""
Nhiễm Ký Sinh Giardia (Giardiasis) Tab
"""
import streamlit as st

def render_giardiasis_tab():
    """Render tab Nhiễm Ký Sinh Giardia"""
    st.header("💧 Nhiễm Ký Sinh Giardia - Bệnh của khách du lịch")
    
    st.markdown("""
    <div class="info-box">
        <b>💡 Hiểu đơn giản:</b><br>
        Giardia là ký sinh đơn bào sống trong ruột non, gây tiêu chảy, đầy hơi.
        Bệnh "khách du lịch" - phổ biến ở người đi du lịch nhiều nơi.
    </div>
    """, unsafe_allow_html=True)
    
    # Nguyên nhân và con đường lây
    with st.expander("🔍 Nguyên nhân & Con đường lây bệnh", expanded=True):
        st.markdown("""
        ### 🦠 Nguyên nhân:
        - **Giardia lamblia:** Đơn bào ký sinh trong ruột non
        - Có 2 dạng: Dạng hoạt động (trophozoite) và dạng kén (cyst)
        - Bám vào thành ruột → Hút chất dinh dưỡng
        - Phổ biến toàn cầu, đặc biệt vùng nhiệt đới
        
        ### 🗺️ Con đường lây bệnh:
        1. **Qua nước uống:**
           - Uống nước ao, hồ, suối
           - Nước giếng không đun sôi
           - Nước đá nhiễm bẩn
           - Bể bơi công cộng
           
        2. **Qua thức ăn:**
           - Rau sống không rửa sạch
           - Thức ăn nhiễm kén
           - Ruồi/bọ làm nhiễm thức ăn
        
        3. **Qua tiếp xúc:**
           - Tay bẩn → Miệng
           - Dùng chung đồ cá nhân
           - Trẻ em mầm non
        
        4. **Vùng nguy cơ cao:**
           - Đi du lịch nhiều nơi
           - Vùng nhiệt đới, nước kém
           - Nông thôn, miền núi
           - Chơi ở bể bơi công cộng
    """)
    
    # Triệu chứng
    with st.expander("⚕️ Triệu chứng nhận biết"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🟢 Triệu chứng nhẹ:
            - **Không triệu chứng** (70% người)
            - Chỉ phát hiện khi xét nghiệm
            - Có thể sống chung hòa bình
            
            ### 🟡 Triệu chứng thường gặp:
            - **Tiêu chảy:** Phân lỏng, nước, không máu
            - **Đầy hơi:** Bụng chướng, khó tiêu
            - **Ợ hơi:** Bụng sôi ùng ục
            - **Mệt mỏi:** Không có sức
            - **Sụt cân:** Do kém hấp thu
            """)
        
        with col2:
            st.markdown("""
            ### 🔴 Triệu chứng nặng:
            - **Tiêu chảy dữ dội:** 10-20 lần/ngày
            - **Mất nước:** Da khô, mắt trũng
            - **Phân mỡ:** Bóng, nổi trên nước
            - **Đau bụng:** Quặn, đầy hơi
            - **Buồn nôn:** Chán ăn hoàn toàn
            
            ### 🚨 Biến chứng hiếm:
            - Suy dinh dưỡng (trẻ em)
            - Kém hấp thu mãn tính
            - Viêm túi mật
            - Tổn thương ruột
    """)
    
    # Triệu chứng đặc trưng
    with st.expander("🎯 Đặc điểm riêng của nhiễm Giardia"):
        st.markdown("""
        ### 💡 Dấu hiệu điển hình:
        
        **1. Đầy hơi + Ợ hơi rất nhiều:**
        - Bụng chướng như bóng bay
        - Ợ hơi liên tục, có mùi hôi
        - Sôi bụng ùng ục
        
        **2. Phân mỡ (Steatorrhea):**
        - Phân bóng, như có mỡ
        - Nổi trên mặt nước
        - Màu vàng nhạt, dính
        - Khó cọ rửa toilet
        
        **3. Tiêu chảy không máu:**
        - Phân lỏng, nước
        - KHÔNG có máu (khác lỵ amip)
        - Mùi hôi, nổi bọt
        
        **4. Kéo dài:**
        - Tự khỏi 2-6 tuần (đôi khi)
        - Nhưng hay tái phát
        - Cần điều trị để khỏi hẳn
    """)
    
    # Điều trị
    with st.expander("💊 Thuốc điều trị (theo chỉ định bác sĩ)"):
        st.markdown("""
        ### ✅ Thuốc điều trị:
        
        **1. Metronidazole (Flagyl) - TỐT NHẤT:**
        - Liều: 250mg x 3 lần/ngày x 5-7 ngày
        - Hoặc: 2g/ngày x 3 ngày
        - Diệt giardia: Hiệu quả 90-95%
        - Giá: ~30.000 VNĐ/viên
        - **Lưu ý:** Không uống rượu bia!
        
        **2. Tinidazole (Fasigyn):**
        - Liều: 2g duy nhất (1 lần)
        - Hoặc: 500mg x 2 lần/ngày x 5 ngày
        - Hiệu quả: 95%
        - Ít tác dụng phụ hơn
        - Giá: ~100.000 VNĐ/viên
        
        **3. Nitazoxanide (Alinia):**
        - Liều: 500mg x 2 lần/ngày x 3 ngày
        - Cho: Người lớn
        - Hiệu quả: 85%
        - Giá: ~150.000 VNĐ
        
        **4. Paromomycin (Humatin):**
        - Liều: 25-30mg/kg/ngày x 5-10 ngày
        - Cho: Bà bầu (an toàn nhất)
        - Hiệu quả: 70%
        - Giá: ~80.000 VNĐ
        
        ### ⚠️ Lưu ý khi điều trị:
        1. **Uống đủ liều:** Không bỏ giữa chừng
        2. **Tránh rượu bia:** Khi uống Metronidazole
        3. **Tái khám:** Sau 1-2 tuần
        4. **Điều trị lại:** Nếu vẫn còn triệu chứng
    """)
    
    # Phòng ngừa
    with st.expander("🛡️ Phòng ngừa - RẤT QUAN TRỌNG!"):
        st.markdown("""
        ### ✅ Quy tắc VÀNG:
        
        **1. 💧 Uống nước sạch:**
        - Đun sôi 100°C để nguội
        - Không uống nước ao, hồ, suối
        - Nước đá phải rõ nguồn gốc
        - Khi du lịch: Chỉ uống nước đóng chai
        
        **2. 🥬 Rửa rau kỹ:**
        - Ngâm nước muối 15 phút
        - Rửa dưới vòi nước chảy
        - Nấu chín rau (nếu có thể)
        
        **3. 🏊 Tránh bể bơi:**
        - Không nuốt nước bể bơi
        - Tắm sạch trước khi vào
        - Trẻ em: Dạy không nuốt nước
        
        **4. 🧼 Vệ sinh tay:**
        - Rửa với xà phòng 20 giây
        - Trước ăn, sau đi vệ sinh
        - Cắt móng tay ngắn
        
        **5. 🍽️ Vệ sinh thức ăn:**
        - Che đậy thức ăn
        - Không để lâu, không để ruồi
        - Khi du lịch: Chỉ ăn thức ăn nấu chín
    """)
    
    # Tại sao gọi là "Bệnh khách du lịch"
    with st.expander("✈️ Tại sao gọi là 'Bệnh khách du lịch'?"):
        st.markdown("""
        ### 🌍 Đặc điểm:
        
        **1. Lây qua nước uống:**
        - Du lịch nhiều nơi → Uống nước lạ
        - Nước địa phương có thể nhiễm
        - Hệ thống tiêu hóa chưa quen
        
        **2. Vùng nguy cơ cao:**
        - Vùng nhiệt đới
        - Nước kém phát triển
        - Vệ sinh kém
        
        **3. Triệu chứng xuất hiện:**
        - Sau khi về nhà 1-2 tuần
        - Đầy hơi, tiêu chảy
        - Tự khỏi → Tái phát
        
        **4. Điều trị:**
        - Cần uống thuốc đủ liều
        - Tái khám để chắc chắn
        - Dạy gia đình phòng ngừa
        
        💡 **Khi du lịch:** Chỉ uống nước đóng chai!
    """)
    
    # FAQ
    st.markdown("---")
    st.subheader("❓ Câu hỏi thường gặp")
    
    with st.expander("🤔 Tôi đầy hơi, ợ hơi nhiều, có phải nhiễm Giardia?"):
        st.markdown("""
        **CÓ THỂ, nhưng cần xét nghiệm:**
        
        **Dấu hiệu nhiễm Giardia:**
        - Đầy hơi, ợ hơi liên tục
        - Tiêu chảy không máu
        - Phân mỡ (bóng, nổi)
        - Mệt mỏi, chán ăn
        - Đi du lịch hoặc uống nước ao
        
        **Làm gì:**
        1. Khám bác sĩ → Xét nghiệm phân
        2. Soi phân tìm kén giardia
        3. Nếu có: Uống Metronidazole
        4. Điều chỉnh chế độ ăn: Ít chất béo
        """)
    
    with st.expander("🤔 Bị nhiễm Giardia có nguy hiểm không?"):
        st.markdown("""
        **THƯỜNG KHÔNG nguy hiểm, nhưng:**
        
        **Triệu chứng khó chịu:**
        - Đầy hơi suốt ngày
        - Tiêu chảy kéo dài
        - Mệt mỏi, chán ăn
        - Sụt cân
        
        **Biến chứng:**
        - Suy dinh dưỡng (trẻ em)
        - Kém hấp thu mãn tính
        - Giảm chất lượng cuộc sống
        
        **→ Nên điều trị sớm để khỏi hẳn!**
        """)
    
    with st.expander("🤔 Tôi đi du lịch về bị tiêu chảy, phải làm sao?"):
        st.markdown("""
        **CÓ THỂ là nhiễm Giardia hoặc các bệnh khác:**
        
        **Làm gì:**
        1. **Bù nước:** Uống Oresol liên tục
        2. **Nghỉ ngơi:** Tránh đi xa, thức ăn lạ
        3. **Khám bác sĩ:** Sau 2-3 ngày không khỏi
        4. **Xét nghiệm:** Tìm nguyên nhân
        5. **Điều trị:** Uống thuốc đúng
        
        **Phòng ngừa lần sau:**
        - Chỉ uống nước đóng chai
        - Tránh ăn thức ăn sống
        - Rửa tay thường xuyên
        """)
    
    # Cảnh báo cuối
    st.markdown("""
    ---
    <div class="warning-box">
        <b>⚠️ QUAN TRỌNG:</b><br>
        • Nhiễm Giardia gây đầy hơi, tiêu chảy khó chịu<br>
        • Khi du lịch: Chỉ uống nước đóng chai!<br>
        • Uống thuốc đủ liều để tránh tái phát<br>
        • Thông tin trên chỉ mang tính chất <b>THAM KHẢO</b><br>
        • <b>KHÔNG THAY THẾ</b> tư vấn của bác sĩ<br>
        • Tiêu chảy kéo dài: <b>KHÁM BÁC SĨ</b>
    </div>
    """, unsafe_allow_html=True)

