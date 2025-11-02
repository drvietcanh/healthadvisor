"""
Practical Health Tips - Mẹo vặt thực tế nhất
Các mẹo hay gặp trong cuộc sống hàng ngày
"""

import streamlit as st


def render_common_ailments_tab():
    """Mẹo xử trí các bệnh thường gặp"""
    st.subheader("🩺 Xử trí các bệnh thường gặp tại nhà")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🤧 CẢM LẠNH (Common Cold)
        
        **Triệu chứng:**
        - Sổ mũi, nghẹt mũi
        - Hắt hơi, ho
        - Đau họng nhẹ
        
        **💊 Xử trí tại nhà:**
        1. **Nghỉ ngơi nhiều:** Ngủ đủ giấc giúp cơ thể phục hồi
        2. **Uống nhiều nước ấm:** Trà gừng, nước chanh mật ong
        3. **Rửa mũi bằng nước muối:** Xịt nước muối sinh lý 3-4 lần/ngày
        4. **Súc họng nước muối:** Pha 1 thìa muối vào 200ml nước ấm
        5. **Paracetamol nếu sốt:** 500-650mg mỗi 6-8h (người lớn)
        
        **⚠️ Khi nào gọi bác sĩ:**
        - Sốt >38.5°C kéo dài >3 ngày
        - Khó thở, đau ngực
        - Ho ra đờm vàng, xanh
        
        ---
        
        ### 🤒 SỐT (Fever)
        
        **Triệu chứng:**
        - Nhiệt độ >37.5°C
        - Ớn lạnh, đau đầu
        - Mệt mỏi
        
        **🌡️ Xử trí tại nhà:**
        1. **Uống nhiều nước:** Phòng mất nước do sốt
        2. **Chườm ấm:** Khăn ấm lau người (KHÔNG chườm lạnh!)
        3. **Nghỉ ngơi:** Nằm yên, mặc quần áo thoáng
        4. **Paracetamol:** 500-1000mg mỗi 6h nếu sốt >38°C
        5. **Theo dõi:** Đo nhiệt độ mỗi 2-4 giờ
        
        **🚨 Khi nào gọi 115:**
        - Sốt >40°C không hạ
        - Co giật (đặc biệt trẻ em)
        - Mê sảng, không tỉnh táo
        
        ---
        
        ### 🦷 ĐAU RĂNG (Toothache)
        
        **Triệu chứng:**
        - Đau nhói, nhức răng
        - Sưng nướu, má
        - Đau khi nhai
        
        **💊 Xử trí tạm thời:**
        1. **Súc miệng nước muối ấm:** 1 thìa muối + 200ml nước
        2. **Chườm lạnh bên ngoài:** Khăn lạnh chườm 15 phút
        3. **Paracetamol:** 500mg để giảm đau
        4. **Tránh:** Thức ăn nóng, lạnh, ngọt
        5. **Không tự ý:** Nhổ răng, chọc vào chỗ đau
        
        **⚠️ Cần đi nha sĩ khi:**
        - Sưng mặt, khó mở miệng
        - Sốt, mệt mỏi
        - Đau >24h không đỡ
        
        ---
        
        ### 🩹 VẾT CẮT, XƯỚC (Cuts & Scrapes)
        
        **Triệu chứng:**
        - Chảy máu
        - Đau, sưng
        - Dễ nhiễm trùng
        
        **🩹 Xử trí đúng cách:**
        1. **Rửa sạch:** Nước sạch + xà phòng nhẹ
        2. **Cầm máu:** Băng ép 10-15 phút
        3. **Bôi thuốc:** Betadine, cồn y tế
        4. **Băng vết thương:** Gạc vô trùng + băng dính
        5. **Theo dõi:** Đổi băng 1-2 lần/ngày
        
        **🚨 Khi nào gọi 115:**
        - Chảy máu ồ ạt, không cầm được
        - Vết thương sâu, nhiều máu
        - Có dị vật (thủy tinh, kim loại)
        """)
    
    with col2:
        st.markdown("""
        ### 🤢 BUỒN NÔN, NÔN (Nausea & Vomiting)
        
        **Triệu chứng:**
        - Buồn nôn, khó chịu dạ dày
        - Nôn nhiều lần
        - Mệt mỏi, khát nước
        
        **💊 Xử trí:**
        1. **Nghỉ ngơi:** Ngồi thẳng, không nằm ngay
        2. **Uống từng ngụm nhỏ:** Nước ấm, trà gừng
        3. **Tránh:** Thức ăn rắn trong 2-4 giờ đầu
        4. **Ăn nhẹ khi đỡ:** Chuối, cơm trắng, táo
        5. **Gừng:** Nhai gừng tươi hoặc trà gừng
        
        **🚨 Khi nào gọi 115:**
        - Nôn máu, nôn màu cà phê
        - Nôn liên tục >24h
        - Mất ý thức, co giật
        
        ---
        
        ### 🔥 BỎNG NHẸ (Minor Burns)
        
        **Triệu chứng:**
        - Đỏ da, đau rát
        - Phồng rộp nhẹ (độ 1, 2)
        
        **🔥 Xử trí ngay:**
        1. **Làm mát NGAY:** Cho vùng bỏng vào nước lạnh 15-20 phút
        2. **Không bôi:** Kem đánh răng, nước mắm, bia
        3. **Băng:** Gạc vô trùng, KHÔNG nặn vỡ bóng nước
        4. **Thuốc:** Thuốc mỡ bỏng có Bạc sulfadiazine
        5. **Theo dõi:** Vệ sinh hàng ngày, quan sát nhiễm trùng
        
        **🚨 GỌI 115 NGAY khi:**
        - Bỏng độ 3 (da trắng/đen, không đau)
        - Bỏng >10% diện tích cơ thể
        - Bỏng vùng mặt, bàn tay, bộ phận sinh dục
        
        ---
        
        ### 😰 CHUỘT RÚT (Muscle Cramp)
        
        **Triệu chứng:**
        - Cơ co thắt đột ngột
        - Đau dữ dội
        - Thường ở chân, bắp chân
        
        **💪 Xử trí:**
        1. **Duỗi cơ:** Kéo duỗi cơ theo chiều ngược lại
        2. **Massage:** Xoa bóp cơ bị co
        3. **Chườm nóng:** Túi nước nóng sau khi hết co
        4. **Uống nước:** Phòng mất cân bằng điện giải
        5. **Phòng ngừa:** Uống đủ nước + Kali (chuối, cam)
        
        **⚠️ Nên khám khi:**
        - Chuột rút thường xuyên
        - Chuột rút khi không vận động
        - Đau kéo dài sau chuột rút
        
        ---
        
        ### 🤦 ĐAU ĐẦU (Headache)
        
        **Triệu chứng:**
        - Đau âm ỉ hoặc đau dữ dội
        - Đau một bên hoặc cả đầu
        
        **💊 Xử trí nhẹ:**
        1. **Nghỉ ngơi:** Nằm yên, tắt đèn
        2. **Chườm lạnh/lạnh:** Khăn lạnh hoặc ấm
        3. **Massage:** Xoa thái dương, gáy
        4. **Paracetamol:** 500mg nếu đau nhiều
        5. **Uống nước:** Mất nước gây đau đầu
        
        **🚨 GỌI 115 NGAY:**
        - Đau đầu dữ dội đột ngột (sét đánh)
        - Kèm sốt cao, cứng cổ
        - Méo mặt, yếu liệt tay chân
        """)

