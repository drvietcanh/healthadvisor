"""
Sán Dây (Tapeworm) Tab
"""
import streamlit as st

def render_tapeworm_tab():
    """Render tab Sán Dây"""
    st.header("🥓 Sán Dây - Bệnh từ ăn thịt sống/hái sửa chưa nấu chín")
    
    st.markdown("""
    <div class="info-box">
        <b>💡 Hiểu đơn giản:</b><br>
        Sán dây dài 2-10 mét, sống trong ruột người. Có nhiều đốt, mỗi đốt đẻ trứng.
        Bệnh do ăn thịt lợn/bò sống (nguy hiểm!) hoặc ăn rau có ấu trùng.
    </div>
    """, unsafe_allow_html=True)
    
    # Nguyên nhân và con đường lây
    with st.expander("🔍 Nguyên nhân & Con đường lây bệnh", expanded=True):
        st.markdown("""
        ### 🦠 Nguyên nhân:
        - **Sán dây lợn (Taenia solium):** Dài 2-8 mét
        - **Sán dây bò (Taenia saginata):** Dài 5-10 mét
        - Có nhiều đốt, mỗi đốt đẻ trứng
        - Đốt già rụng ra, theo phân ra ngoài
        
        ### 🗺️ Con đường lây bệnh:
        1. **Sán dây BÒ (phổ biến hơn):**
           - Ăn thịt bò sống/ít chín
           - Ăn nem chua, gỏi bò
           - → Ấu trùng vào ruột, phát triển thành sán dây
           
        2. **Sán dây LỢN (nguy hiểm hơn!):**
           - Ăn thịt lợn sống
           - Ăn nem, giò sống
           - → Ấu trùng vào ruột
           - **Nguy hiểm:** Có thể chui lên não!
        
        3. **Ăn trứng từ rau:**
           - Rau sống bị nhiễm trứng
           - Không rửa sạch
           - → Nhiễm trực tiếp
    """)
    
    # Triệu chứng
    with st.expander("⚕️ Triệu chứng nhận biết"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🟢 Triệu chứng nhẹ:
            - **Không triệu chứng** (70% người bị)
            - Chỉ phát hiện khi thấy đốt sán trong phân
            - Đốt sán: Như hạt gạo, trắng, bò lổm ngổm
            
            ### 🟡 Triệu chứng thường gặp:
            - **Đau bụng nhẹ:** Khó tiêu
            - **Buồn nôn:** Đầy hơi
            - **Sụt cân:** Sán hút chất dinh dưỡng
            - **Thèm ăn lạ:** Hoặc chán ăn
            """)
        
        with col2:
            st.markdown("""
            ### 🔴 Triệu chứng sán dây LỢN (nguy hiểm!):
            - **Co giật:** Nếu ấu trùng lên não
            - **Đau đầu:** Dữ dội, tái diễn
            - **Nhìn mờ:** Áp lực trong não
            - **Liệt chân tay:** Nếu chèn ép thần kinh
            
            ### 🚨 Biến chứng:
            - Viêm não do sán
            - Tổn thương mắt (nếu vào mắt)
            - Cần phẫu thuật gấp!
    """)
    
    # Sự nguy hiểm
    with st.expander("⚠️ Tại sao sán dây lợn nguy hiểm?"):
        st.markdown("""
        ### 🚨 Sán dây LỢN khác BÒ:
        
        | Đặc điểm | Sán dây BÒ | Sán dây LỢN |
        |----------|------------|-------------|
        | **Chỉ ở ruột** | ✅ Có | ❌ KHÔNG |
        | **Chui lên não** | ❌ Không | ✅ CÓ! |
        | **Co giật** | ❌ Không | ✅ CÓ! |
        | **Điều trị** | Dễ | Khó, cần mổ |
        
        ### 💀 Ấu trùng sán lợn lên não:
        - Ấu trùng tạo "nang" trong não
        - Nang to lên → Chèn ép não
        - → Co giật, liệt, có thể chết
        
        **PHẢI KHÁM NGAY nếu:**
        - Có triệu chứng + Ăn thịt lợn sống
        - Co giật không rõ nguyên nhân
        - Đau đầu dữ dội, tái diễn
    """)
    
    # Điều trị
    with st.expander("💊 Thuốc tẩy sán (theo chỉ định bác sĩ)"):
        st.markdown("""
        ### ✅ Thuốc điều trị sán dây:
        
        **1. Praziquantel (Biltricide) - TỐT NHẤT:**
        - Liều: 10-20mg/kg cân nặng, uống duy nhất
        - Diệt sán dây bò: Hiệu quả 95%
        - Diệt sán dây lợn: Hiệu quả 85%
        - Giá: ~50.000-100.000 VNĐ
        
        **2. Niclosamide (Yomesan):**
        - Liều: 2g (4 viên), nhai vào sáng sớm
        - Uống với nước, sau 2 giờ uống thuốc nhuận tràng
        - Hiệu quả: 80-90%
        - Giá: ~80.000 VNĐ
        
        **3. Albendazole (Zentel):**
        - Liều: 400mg x 2 lần/ngày x 3 ngày
        - Cho sán dây bò
        - Giá: ~25.000 VNĐ/viên
        
        ### ⚠️ Lưu ý khi tẩy sán:
        1. **Tẩy đúng thuốc:** Sán dây lợn cần Praziquantel đặc biệt
        2. **Tẩy cùng ăn nhiều chất xơ:** Để tống sán ra dễ dàng
        3. **Kiểm tra phân:** Sau 1-2 tuần, xem còn đốt sán không
        4. **Điều trị lại:** Nếu vẫn còn đốt sán
        
        ### 🚨 Điều trị nang sán trong não:
        - **Praziquantel + Steroid:** Uống 2-3 tuần
        - Hoặc **Albendazole:** Uống 8-30 ngày
        - **Phẫu thuật:** Nếu nang to, gây nguy hiểm
        - **Theo dõi chặt:** Tái khám định kỳ
    """)
    
    # Phòng ngừa
    with st.expander("🛡️ Phòng ngừa - RẤT QUAN TRỌNG!"):
        st.markdown("""
        ### ✅ Quy tắc VÀNG:
        
        **1. 🥩 Nấu chín thịt:**
        - **Thịt bò:** ≥70°C (bên trong không còn hồng)
        - **Thịt lợn:** ≥70°C (hoàn toàn màu xám)
        - Ấu trùng chết ở nhiệt độ cao
        - **TRÁNH:** Nem chua, giò sống, thịt tái
        
        **2. 🧊 Ướp lạnh sâu:**
        - Nhiệt độ <-20°C x 7 ngày
        - Giết chết ấu trùng
        - An toàn để ăn sau khi nấu chín
        
        **3. 🥬 Rửa rau kỹ:**
        - Ngâm nước muối 15 phút
        - Rửa dưới vòi nước chảy
        - Tránh ăn rau sống ở vùng nhiễm cao
        
        **4. 🚽 Vệ sinh phân:**
        - Xử lý phân đúng cách
        - Không thải trực tiếp ra môi trường
        - Người bị → Điều trị ngay để tránh lây
        
        **5. 🔍 Kiểm tra thịt:**
        - Mua thịt rõ nguồn gốc
        - Không mua thịt lạ, không rõ xuất xứ
        - Thịt bò/lợn phải qua kiểm dịch
    """)
    
    # Phát hiện sán dây
    with st.expander("🔎 Cách phát hiện có sán dây"):
        st.markdown("""
        ### ✅ Dấu hiệu thường gặp:
        
        **1. Thấy đốt sán trong phân:**
        - Sau khi đại tiện
        - Như "hạt gạo dài", trắng
        - Có thể bò ra ngoài hậu môn
        - Thỉnh thoảng động đậy
        
        **2. Xét nghiệm phân:**
        - Soi tìm trứng sán
        - Hiệu quả 50-70% (không cao)
        - Phải soi 3 lần mới chắc
        
        **3. Xét nghiệm máu:**
        - Tìm kháng thể kháng sán
        - Chỉ dùng cho nghi ngờ cao
        
        **4. Siêu âm/CT/MRI:**
        - Nếu nghi ấu trùng lên não
        - Thấy nang sán trong não
        - Bất thường → Khám bác sĩ ngay!
    """)
    
    # FAQ
    st.markdown("---")
    st.subheader("❓ Câu hỏi thường gặp")
    
    with st.expander("🤔 Tôi ăn nem chua, gỏi bò có bị sán không?"):
        st.markdown("""
        **CÓ NGUY CƠ CAO!**
        
        **Nem chua/Giò sống/Thịt tái:**
        - Có thể chứa ấu trùng sán dây
        - Nhiệt độ làm nem <70°C → Không diệt được
        - Phải nấu chín mới an toàn
        
        **Nguy cơ lây:**
        - Thịt không rõ nguồn gốc → 40-60% nguy cơ
        - Thịt có kiểm dịch → 5-10% nguy cơ
        
        **KHUYẾN CÁO:**
        - Tránh ăn nem chua, thịt tái
        - Nếu ăn: Chỉ ăn ít, rõ nguồn gốc
        - Trẻ em, bà bầu: KHÔNG ăn!
        """)
    
    with st.expander("🤔 Sán dây lợn và bò khác nhau thế nào?"):
        st.markdown("""
        **Sán dây BÒ:** Chỉ sống trong ruột
        - Không chui ra ngoài
        - Gây đau bụng, sụt cân
        - Điều trị dễ
        - Ít nguy hiểm
        
        **Sán dây LỢN:** Có thể lên não
        - Ấu trùng tạo nang trong não
        - Co giật, liệt
        - Cần điều trị phức tạp
        - RẤT nguy hiểm!
        
        **→ Tránh ăn thịt LỢN sống/tái!**
        """)
    
    with st.expander("🤔 Làm sao biết mình có sán dây?"):
        st.markdown("""
        **Kiểm tra ngay nếu:**
        1. **Đã ăn thịt sống/tái/nem:**
           - Trong 1-3 tháng qua
           - Có kèm triệu chứng
        
        2. **Có dấu hiệu:**
           - Thấy đốt sán trong phân
           - Đau bụng khó tiêu
           - Sụt cân không rõ nguyên nhân
        
        3. **Triệu chứng nặng (sán lợn):**
           - Co giật
           - Đau đầu dữ dội
           - Nhìn mờ
        
        **Làm gì:**
        - Khám bác sĩ → Xét nghiệm phân
        - Nếu có co giật → Khám ngay, làm CT não
        """)
    
    # Cảnh báo cuối
    st.markdown("""
    ---
    <div class="warning-box">
        <b>⚠️ QUAN TRỌNG:</b><br>
        • Sán dây LỢN có thể lên não → Co giật, nguy hiểm!<br>
        • TRÁNH ăn thịt sống/nem chua, gỏi bò<br>
        • Nấu chín thịt ≥70°C (không còn hồng)<br>
        • Thông tin trên chỉ mang tính chất <b>THAM KHẢO</b><br>
        • <b>KHÔNG THAY THẾ</b> tư vấn của bác sĩ<br>
        • Với co giật, đau đầu: <b>KHÁM BÁC SĨ NGAY</b>
    </div>
    """, unsafe_allow_html=True)

