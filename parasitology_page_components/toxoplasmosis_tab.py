"""
Nhiễm Toxoplasma (Toxoplasmosis) Tab
"""
import streamlit as st

def render_toxoplasmosis_tab():
    """Render tab Toxoplasma"""
    st.header("🐱 Toxoplasma - Bệnh từ thịt sống & phân mèo")
    
    st.markdown("""
    <div class="info-box">
        <b>💡 Hiểu đơn giản:</b><br>
        Toxoplasma là ký sinh đơn bào, lây từ mèo sang người. 
        Đa số không triệu chứng, nhưng NGUY HIỂM cho bà bầu và người suy giảm miễn dịch.
    </div>
    """, unsafe_allow_html=True)
    
    # Nguyên nhân và con đường lây
    with st.expander("🔍 Nguyên nhân & Con đường lây bệnh", expanded=True):
        st.markdown("""
        ### 🦠 Nguyên nhân:
        - **Toxoplasma gondii:** Ký sinh đơn bào
        - Vật chủ chính: Mèo (chỉ mèo mới đẻ ra trứng)
        - Phổ biến toàn cầu: 30-50% người từng nhiễm
        
        ### 🗺️ Con đường lây bệnh:
        1. **Qua thịt sống (phổ biến nhất - 50%):**
           - Ăn thịt lợn/bò/dê sống/ít chín
           - Nem chua, giò sống, thịt tái
           - Ấu trùng trong thịt → Ruột người → Toàn thân
           
        2. **Qua phân mèo (30%):**
           - Phân mèo có trứng
           - Dùng tay dọn phân → Đưa tay vào miệng
           - Ăn rau sống nhiễm trứng từ đất
        
        3. **Qua rau củ (15%):**
           - Rau sống nhiễm trứng từ đất
           - Không rửa sạch
           - Nuốt trứng vào người
        
        4. **Từ mẹ sang con (hiếm nhưng nguy hiểm):**
           - Mẹ nhiễm lần đầu khi mang thai
           - Lây cho thai nhi → Dị tật, chết
           - CHÍNH LÀ LÝ DO CẦN PHÒNG NGỪA!
    """)
    
    # Triệu chứng
    with st.expander("⚕️ Triệu chứng nhận biết"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🟢 Người khỏe mạnh (90% người):
            - **Không triệu chứng**
            - Hoặc triệu chứng nhẹ như cảm cúm:
              - Sốt nhẹ 37-38°C
              - Mệt mỏi, đau cơ
              - Nổi hạch cổ
              - Tự khỏi sau 1-2 tuần
            
            ### 🟡 Triệu chứng lần đầu nhiễm:
            - **Sốt:** 38-39°C
            - **Đau đầu:** Nhẹ đến vừa
            - **Nổi hạch:** Ở cổ, nách
            - **Mệt mỏi:** Không có sức
            """)
        
        with col2:
            st.markdown("""
            ### 🔴 Người suy giảm miễn dịch (nguy hiểm!):
            - **Viêm não:** Đau đầu dữ dội, co giật
            - **Viêm phổi:** Khó thở, sốt cao
            - **Nhiễm toàn thân:** Có thể tử vong
            - **Viêm màng não:** Nhìn mờ, lú lẫn
            
            ### 🚨 Bà bầu nhiễm lần đầu (RẤT NGUY HIỂM!):
            - **Mẹ:** Triệu chứng nhẹ (như cảm cúm)
            - **THAI NHI:** Dị tật nặng!
              - Tổn thương não, mắt
              - Chậm phát triển
              - Có thể chết trong bụng
              - Sẩy thai
    """)
    
    # Nguy hiểm cho bà bầu
    with st.expander("⚠️ NGUY HIỂM CHO BÀ BẦU - Đọc kỹ!"):
        st.markdown("""
        ### 🚨 Rủi ro cho thai nhi:
        
        **Nhiễm lần đầu khi mang thai:**
        - Tuần 1-12: 10-15% lây sang con, TỔN THƯƠNG NẶNG
        - Tuần 13-24: 30-40% lây, tổn thương trung bình
        - Tuần 25-40: 60-80% lây, tổn thương nhẹ
        
        **Dị tật thai nhi:**
        - **Não:** Não nước, đầu nhỏ, chậm phát triển
        - **Mắt:** Mù, lé, tổn thương võng mạc
        - **Tai:** Điếc
        - **Gan, lách:** To, suy chức năng
        - **Tim:** Bệnh tim bẩm sinh
        
        **Có thể:**
        - Sẩy thai
        - Thai chết lưu
        - Chết sau sinh
        - Tàn tật suốt đời
        
        ### 💊 Điều trị cho bà bầu:
        **Phát hiện sớm → Điều trị ngay:**
        - Spiramycin: Phòng lây sang con
        - Pyrimethamine + Sulfadiazine: Điều trị tổn thương
        - Giảm thiểu rủi ro 50-70%
        
        **→ BÀ BẦU CẦN PHÒNG NGỪA RẤT KỸ!**
    """)
    
    # Điều trị
    with st.expander("💊 Thuốc điều trị (theo chỉ định bác sĩ)"):
        st.markdown("""
        ### ✅ Người khỏe mạnh nhiễm lần đầu:
        
        **Không cần điều trị:**
        - Tự khỏi sau 1-2 tuần
        - Cơ thể tự sản xuất kháng thể
        - Chỉ theo dõi triệu chứng
        
        **Nếu triệu chứng nặng:**
        - Pyrimethamine 25-50mg/ngày x 3-4 tuần
        - Kèm Sulfadiazine 2-4g/ngày
        - Kèm acid folic để tránh giảm bạch cầu
        
        ### 🚨 Bà bầu nhiễm lần đầu:
        
        **Tuần 1-16:**
        - Spiramycin 3g/ngày x đến khi sinh
        - Giảm 50-70% nguy cơ lây sang con
        - Theo dõi siêu âm định kỳ
        
        **Tuần 17+ hoặc đã lây sang con:**
        - Pyrimethamine + Sulfadiazine + acid folic
        - Uống 6 tuần, nghỉ 2 tuần, lặp lại
        - Giảm tổn thương cho thai nhi
        
        ### 🚨 Người suy giảm miễn dịch:
        
        **Điều trị:**
        - Pyrimethamine 100-200mg/ngày x 6 tuần
        - Kèm Sulfadiazine 4-6g/ngày
        - Tiếp tục dùng thuốc phòng lâu dài
        - Điều trị theo bác sĩ chuyên khoa
    """)
    
    # Phòng ngừa
    with st.expander("🛡️ Phòng ngừa - RẤT QUAN TRỌNG!"):
        st.markdown("""
        ### ✅ Quy tắc VÀNG:
        
        **1. 🥩 Nấu chín thịt:**
        - Thịt lợn/bò/dê: ≥70°C (bên trong không còn hồng)
        - Ướp lạnh <-20°C x 2 ngày cũng diệt được
        - **TRÁNH:** Nem chua, giò sống, thịt tái
        - **BÀ BẦU:** Không ăn thịt sống dù ít!
        
        **2. 🐱 Vệ sinh phân mèo:**
        - Dùng găng tay khi dọn phân
        - Rửa tay với xà phòng ngay sau
        - Dọn phân mèo hàng ngày (trứng phải 1-5 ngày mới nguy hiểm)
        - **BÀ BẦU:** KHÔNG dọn phân mèo!
        
        **3. 🥬 Rửa rau kỹ:**
        - Ngâm nước muối 15 phút
        - Rửa dưới vòi nước chảy
        - Gọt vỏ khi có thể
        
        **4. 🧼 Vệ sinh tay:**
        - Rửa với xà phòng 20 giây
        - Trước ăn, sau làm vườn
        - Sau chơi với mèo
        
        **5. 🏡 Nuôi mèo an toàn:**
        - Nuôi mèo trong nhà
        - Cho mèo ăn thịt nấu chín
        - Không cho mèo đi lang thang
        - **BÀ BẦU:** Giao mèo cho người khác chăm
    
    ### 🚨 ĐẶC BIỆT CHO BÀ BẦU:
        - KHÔNG ăn thịt sống/tái/nem chua
        - KHÔNG dọn phân mèo
        - KHÔNG làm vườn (tránh tiếp xúc đất)
        - KHÔNG uống sữa chưa tiệt trùng
        - Xét nghiệm Toxoplasma trước/sau khi mang thai
    """)
    
    # Xét nghiệm
    with st.expander("🔬 Xét nghiệm Toxoplasma"):
        st.markdown("""
        ### ✅ Khi nào cần xét nghiệm:
        
        **1. Trước khi mang thai:**
        - Xét nghiệm kháng thể IgM, IgG
        - Nếu đã có kháng thể → An toàn (đã từng nhiễm)
        - Nếu chưa có kháng thể → Phải phòng ngừa kỹ
        
        **2. Khi đang mang thai:**
        - Nghi ngờ nhiễm → Xét nghiệm ngay
        - Phát hiện sớm → Điều trị sớm → Giảm rủi ro
        
        **3. Người suy giảm miễn dịch:**
        - Xét nghiệm định kỳ
        - Phát hiện sớm nhiễm → Điều trị ngay
        
        ### 📊 Giải thích kết quả:
        
        **IgM âm tính, IgG âm tính:**
        - Chưa từng nhiễm → Phải phòng ngừa kỹ
        - Bà bầu: NGUY CƠ CAO nếu nhiễm
        - Theo dõi chặt
        
        **IgM âm tính, IgG dương tính:**
        - Đã từng nhiễm trước đó → An toàn
        - Có miễn dịch tự nhiên
        - Không lo lây sang con
        
        **IgM dương tính, IgG âm tính:**
        - Nhiễm GẦN ĐÂY (1-3 tháng)
        - Bà bầu: NGUY HIỂM! Cần điều trị ngay
        
        **IgM dương tính, IgG dương tính:**
        - Nhiễm trong 6-12 tháng qua
        - Cần theo dõi, đánh giá nguy cơ
    """)
    
    # FAQ
    st.markdown("---")
    st.subheader("❓ Câu hỏi thường gặp")
    
    with st.expander("🤔 Nuôi mèo có nguy hiểm không?"):
        st.markdown("""
        **KHÔNG nguy hiểm nếu:**
        - Mèo nuôi trong nhà
        - Cho mèo ăn thịt nấu chín
        - Dọn phân mèo hàng ngày
        - Rửa tay sau khi chơi với mèo
        
        **NGUY HIỂM khi:**
        - Mèo ăn thịt sống (bắt chuột, chim)
        - Phân mèo để lâu >1 ngày
        - Dùng tay trần dọn phân
        
        **BÀ BẦU:**
        - An toàn nhất: Giao mèo cho người khác
        - Hoặc: KHÔNG dọn phân, luôn đeo găng tay
        """)
    
    with st.expander("🤔 Bà bầu ăn nem chua có nguy hiểm không?"):
        st.markdown("""
        **CÓ NGUY CƠ RẤT CAO!**
        
        **Nem chua/Giò sống:**
        - Có thể chứa Toxoplasma
        - Nhiệt độ làm nem <70°C → Không diệt được
        - Mẹ nhiễm → Lây sang con → Dị tật nặng
        
        **Tỷ lệ:**
        - Mẹ nhiễm ở tuần 1-12: 10-15% lây, tổn thương NẶNG
        - Nguy cơ não nước, mù, chậm phát triển
        
        **KHUYẾN CÁO:**
        - Bà bầu: TRÁNH ĂN nem chua, thịt sống/tái
        - Chỉ ăn thịt nấu chín hoàn toàn
        - Ưu tiên sức khỏe con hơn sở thích ăn uống!
        """)
    
    with st.expander("🤔 Làm sao biết mình đã từng nhiễm Toxoplasma?"):
        st.markdown("""
        **Xét nghiệm máu:**
        1. IgG âm tính → Chưa từng nhiễm
           - Phải phòng ngừa kỹ
           - Bà bầu: Nguy cơ cao nếu nhiễm lần đầu
           
        2. IgG dương tính → Đã từng nhiễm
           - Có miễn dịch tự nhiên
           - Không lo nhiễm lại
           - Bà bầu: Không lo lây sang con
        
        **Lợi ích:**
        - Biết trước khi mang thai
        - Phòng ngừa phù hợp
        - An tâm hơn
        """)
    
    # Cảnh báo cuối
    st.markdown("""
    ---
    <div class="warning-box">
        <b>⚠️ QUAN TRỌNG:</b><br>
        • Toxoplasma NGUY HIỂM cho bà bầu - Gây dị tật thai nhi!<br>
        • TRÁNH ăn thịt sống/nem chua, dọn phân mèo<br>
        • Xét nghiệm trước khi mang thai<br>
        • Thông tin trên chỉ mang tính chất <b>THAM KHẢO</b><br>
        • <b>KHÔNG THAY THẾ</b> tư vấn của bác sĩ<br>
        • Bà bầu nghi nhiễm: <b>KHÁM BÁC SĨ NGAY</b>
    </div>
    """, unsafe_allow_html=True)

