"""
Sán Lá Gan (Liver Fluke) Tab
"""
import streamlit as st

def render_liver_fluke_tab():
    """Render tab Sán Lá Gan"""
    st.header("🪲 Sán Lá Gan - Bệnh từ ăn cá sống")
    
    st.markdown("""
    <div class="info-box">
        <b>💡 Hiểu đơn giản:</b><br>
        Sán lá gan sống ký sinh trong ống mật của người, gây viêm gan, tắc mật.
        Bệnh do ăn cá sống, gỏi cá, nem cá (phổ biến ở miền Bắc, miền Trung VN).
    </div>
    """, unsafe_allow_html=True)
    
    # Nguyên nhân và con đường lây
    with st.expander("🔍 Nguyên nhân & Con đường lây bệnh", expanded=True):
        st.markdown("""
        ### 🦠 Nguyên nhân:
        - **Sán lá gan nhỏ (Opisthorchis, Clonorchis):** Dài 1-2cm, dẹt
        - **Sán lá gan lớn (Fasciola):** Dài 3-5cm
        - Sống trong ống mật, hút máu, tiết độc tố
        - Phổ biến: VN (miền Bắc, Trung), Campuchia, Lào
        
        ### 🗺️ Con đường lây bệnh:
        1. **Sán lá gan NHỎ (phổ biến ở VN):**
           - **Ăn cá sống/gỏi cá** (gỏi cá, sashimi)
           - **Nem cá:** Cá sống trộn thính
           - Ấu trùng trong cá → Vào ruột → Lên ống mật
           
        2. **Sán lá gan LỚN:**
           - **Ăn rau cải chưa nấu chín** (rau muống, cải xoong)
           - Uống nước ao có ấu trùng
           - Ấu trùng → Ruột → Xuyên qua thành ruột → Gan
        
        3. **Vùng nguy cơ cao:**
           - Miền Bắc: Ninh Bình, Nam Định, Hà Nam
           - Miền Trung: Quảng Bình, Quảng Trị
           - Dùng nước ao, ăn cá sống
    """)
    
    # Triệu chứng
    with st.expander("⚕️ Triệu chứng nhận biết"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🟢 Triệu chứng nhẹ:
            - **Không triệu chứng** (80% người bị)
            - Chỉ phát hiện khi xét nghiệm
            - Có thể sống nhiều năm không biết
            
            ### 🟡 Triệu chứng thường gặp:
            - **Mệt mỏi:** Không muốn làm gì
            - **Chán ăn:** Ăn không ngon
            - **Đau bụng nhẹ:** Bên phải, dưới sườn
            - **Bụng to:** Khó tiêu, đầy hơi
            """)
        
        with col2:
            st.markdown("""
            ### 🔴 Triệu chứng nặng:
            - **Vàng da:** Da, mắt vàng (tắc mật)
            - **Đau bụng dữ dội:** Quặn từng cơn
            - **Sốt:** Viêm ống mật cấp
            - **Gầy sút:** Sụt cân nhanh
            
            ### 🚨 Biến chứng:
            - Xơ gan (sán sống lâu năm)
            - Ung thư ống mật (rất nguy hiểm!)
            - Viêm túi mật
            - Tắc mật hoàn toàn
    """)
    
    # Biến chứng nguy hiểm
    with st.expander("⚠️ Biến chứng nguy hiểm"):
        st.markdown("""
        ### 🚨 Ung thư ống mật:
        - Sán sống trong ống mật 10-20 năm
        - Gây viêm mãn tính → Ung thư
        - **Rất khó điều trị**, tỷ lệ sống thấp
        
        ### 🚨 Xơ gan:
        - Sán gây viêm gan mãn tính
        - Gan bị tổn thương → Xơ
        - → Suy gan, cổ trướng
        
        ### 🚨 Tắc mật:
        - Sán chết → Tắc ống mật
        - Vàng da, đau bụng dữ dội
        - **Cần can thiệp gấp!**
        
        **→ Điều trị sớm để tránh biến chứng!**
    """)
    
    # Điều trị
    with st.expander("💊 Thuốc điều trị (theo chỉ định bác sĩ)"):
        st.markdown("""
        ### ✅ Thuốc điều trị:
        
        **1. Praziquantel (Biltricide) - TỐT NHẤT:**
        - Liều: 25mg/kg x 3 lần/ngày x 1 ngày
        - Diệt sán lá gan nhỏ: Hiệu quả 95%
        - Uống sau ăn no
        - Giá: ~50.000-100.000 VNĐ
        
        **2. Triclabendazole (Egaten):**
        - Liều: 10mg/kg x 2 lần/ngày x 1 ngày
        - Cho sán lá gan lớn
        - Hiệu quả: 90-95%
        - Giá: ~200.000 VNĐ
        
        **3. Albendazole (Zentel):**
        - Liều: 10mg/kg/ngày x 7 ngày
        - Cho sán lá gan lớn
        - Hiệu quả: 70-80%
        - Giá: ~25.000 VNĐ/viên
        
        ### ⚠️ Lưu ý khi điều trị:
        1. **Uống sau ăn:** Tránh kích ứng dạ dày
        2. **Điều trị cả gia đình:** Nếu cùng ăn cá sống
        3. **Tái khám:** Sau 3-6 tháng
        4. **Xét nghiệm lại:** Xem còn sán không
        
        ### 🔄 Điều trị ung thư ống mật:
        - **Nếu phát hiện sớm:** Phẫu thuật + Hóa trị
        - **Nếu muộn:** Chỉ hóa trị
        - **Tiên lượng:** Rất xấu
        - → **PHẢI phòng ngừa!**
    """)
    
    # Phòng ngừa
    with st.expander("🛡️ Phòng ngừa - RẤT QUAN TRỌNG!"):
        st.markdown("""
        ### ✅ Quy tắc VÀNG:
        
        **1. 🐟 Không ăn cá sống:**
        - TRÁNH: Gỏi cá, sashimi, nem cá
        - TRÁNH: Cá sống trộn thính
        - **Nấu chín cá ≥63°C** (cá trắng, không còn trong suốt)
        - Rán/chiên cá kỹ 5 phút
        
        **2. 🥬 Rửa rau kỹ:**
        - Ngâm nước muối 15 phút
        - Rửa dưới vòi nước chảy
        - Nấu chín rau cải (rau muống, cải xoong)
        
        **3. 💧 Uống nước sạch:**
        - Đun sôi để nguội
        - Không uống nước ao, hồ trực tiếp
        - Lọc nước qua hệ thống
        
        **4. 🚽 Vệ sinh phân:**
        - Xử lý phân cá/người đúng cách
        - Không thải vào ao, hồ
        - Người bị → Điều trị để tránh lây
        
        **5. 🔍 Tẩy sán định kỳ:**
        - Người vùng nhiễm cao: 6 tháng 1 lần
        - Người hay ăn cá sống: 12 tháng 1 lần
        - Khám bác sĩ nếu có triệu chứng
    """)
    
    # Phát hiện bệnh
    with st.expander("🔎 Cách phát hiện bệnh"):
        st.markdown("""
        ### ✅ Xét nghiệm:
        
        **1. Xét nghiệm phân:**
        - Soi tìm trứng sán trong phân
        - Làm 3 lần mới chắc
        - Hiệu quả: 70-80%
        
        **2. Xét nghiệm máu:**
        - Kháng thể kháng sán
        - Chính xác cao
        - Phát hiện nhiễm cũ hoặc mới
        
        **3. Siêu âm bụng:**
        - Thấy sán trong ống mật
        - Viêm túi mật, gan to
        - Giãn ống mật
        
        **4. Chụp ống mật:**
        - CT scan hoặc MRI
        - Phát hiện tổn thương, ung thư
        
        ### 🚨 Dấu hiệu cần khám ngay:
        - Vàng da (da, mắt vàng)
        - Đau bụng dữ dội bên phải
        - Sốt + Đau bụng
        - Ăn cá sống + Có triệu chứng
    """)
    
    # FAQ
    st.markdown("---")
    st.subheader("❓ Câu hỏi thường gặp")
    
    with st.expander("🤔 Tôi ăn gỏi cá, nem cá có bị sán lá gan không?"):
        st.markdown("""
        **CÓ NGUY CƠ RẤT CAO!**
        
        **Gỏi cá/Nem cá:**
        - Có thể chứa ấu trùng sán lá gan
        - Nhiệt độ làm gỏi <63°C → Không diệt được
        - Phải nấu chín kỹ mới an toàn
        
        **Nguy cơ lây:**
        - Cá ao, hồ không kiểm dịch → 40-60%
        - Cá biển → 5-10%
        - Cá nuôi sạch → <5%
        
        **KHUYẾN CÁO:**
        - Tránh ăn gỏi cá, nem cá ở vùng nhiễm
        - Nếu ăn: Chỉ ăn ít, cá sạch
        - Trẻ em, bà bầu: KHÔNG ăn!
        """)
    
    with st.expander("🤔 Bị sán lá gan có nguy hiểm không?"):
        st.markdown("""
        **CÓ THỂ RẤT NGUY HIỂM!**
        
        **Sán sống lâu năm:**
        - Gây viêm ống mật mãn tính
        - → Ung thư ống mật (tỷ lệ sống <20%)
        - → Xơ gan, suy gan
        
        **Triệu chứng:**
        - Vàng da, đau bụng
        - Tắc mật, viêm túi mật
        - Cần can thiệp y tế ngay
        
        **→ Cần điều trị sớm để tránh nguy hiểm!**
        """)
    
    with st.expander("🤔 Làm sao biết mình có sán lá gan?"):
        st.markdown("""
        **Kiểm tra ngay nếu:**
        1. **Đã ăn cá sống/gỏi/nem:**
           - Trong 3-12 tháng qua
           - Sống vùng nhiễm cao
        
        2. **Có triệu chứng:**
           - Mệt mỏi, chán ăn
           - Đau bụng bên phải
           - Vàng da
           - Sốt + Đau bụng
        
        **Làm gì:**
        - Khám bác sĩ → Xét nghiệm phân/máu
        - Siêu âm bụng
        - Nếu có: Điều trị ngay
        """)
    
    with st.expander("🤔 Sán lá gan nhỏ và lớn khác nhau thế nào?"):
        st.markdown("""
        **Sán lá gan NHỎ:**
        - Lây qua: Ăn cá sống/gỏi
        - Phổ biến: VN, Campuchia, Lào
        - Điều trị: Praziquantel
        - Nguy hiểm: Ung thư ống mật
        
        **Sán lá gan LỚN:**
        - Lây qua: Ăn rau cải chưa nấu
        - Phổ biến: Châu Á, Nam Mỹ
        - Điều trị: Triclabendazole
        - Nguy hiểm: Xơ gan
        
        **→ Cả hai đều cần điều trị sớm!**
        """)
    
    # Cảnh báo cuối
    st.markdown("""
    ---
    <div class="warning-box">
        <b>⚠️ QUAN TRỌNG:</b><br>
        • Sán lá gan có thể gây UNG THƯ ỐNG MẬT nếu sống lâu năm!<br>
        • TRÁNH ăn cá sống/gỏi cá, nem cá<br>
        • Nấu chín cá ≥63°C (cá trắng, không còn trong suốt)<br>
        • Thông tin trên chỉ mang tính chất <b>THAM KHẢO</b><br>
        • <b>KHÔNG THAY THẾ</b> tư vấn của bác sĩ<br>
        • Vàng da, đau bụng dữ dội: <b>KHÁM BÁC SĨ NGAY</b>
    </div>
    """, unsafe_allow_html=True)

