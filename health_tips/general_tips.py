"""
General Health Tips
Các mẹo vặt y tế hữu ích cho người dân
"""

import streamlit as st


def render_fever_tips():
    """Hiển thị mẹo xử trí sốt"""
    st.subheader("🌡️ Xử trí sốt đúng cách")
    
    st.markdown("""
    ### 📌 Khi nào cần hạ sốt?
    
    **Sốt nhẹ (37.5-38°C):**
    - 👕 Mặc quần áo thoáng, uống nhiều nước
    - ❄️ Chườm khăn ấm (KHÔNG chườm lạnh!)
    - 💊 Chưa cần uống thuốc
    
    **Sốt cao (>38.5°C):**
    - 💊 Uống paracetamol (tính liều theo cân nặng)
    - 💧 Uống nhiều nước (nước lọc, nước hoa quả)
    - 🧽 Lau người bằng khăn ấm (nước ấm, không lạnh!)
    - 👕 Mặc quần áo mỏng, thoáng
    
    ### ⚠️ Khi nào cần đi bệnh viện?
    
    **Gọi 115 hoặc đi viện NGAY nếu:**
    - 🔥 Sốt > 40°C
    - 😰 Sốt kèm co giật
    - 😴 Li bì, khó đánh thức
    - 🤮 Nôn nhiều, không uống được nước
    - 💨 Khó thở, thở nhanh
    - 🩸 Có ban đỏ trên da
    
    **Trẻ em sốt cần đi khám nếu:**
    - < 3 tháng tuổi: Sốt > 38°C → Khám ngay
    - 3-6 tháng: Sốt > 38.5°C → Khám trong 24h
    - > 6 tháng: Sốt > 3 ngày không hạ → Khám bác sĩ
    """)
    
    # Bảng nhiệt độ
    st.markdown("### 📊 Nhiệt độ cơ thể bình thường:")
    
    temp_data = {
        "Vị trí đo": ["Nách", "Miệng", "Hậu môn", "Tai"],
        "Nhiệt độ bình thường": ["36.5-37°C", "37-37.5°C", "37.5-38°C", "36.5-37.5°C"],
        "Lưu ý": [
            "Phổ biến nhất, cộng thêm 0.5°C so với nhiệt độ thực",
            "Cộng thêm 0.3°C",
            "Chính xác nhất (trẻ nhỏ)",
            "Nhanh, tiện (trẻ lớn)"
        ]
    }
    
    import pandas as pd
    df = pd.DataFrame(temp_data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.info("""
    💡 **Mẹo đo nhiệt độ:**
    - Đo ở nách: Giữ nhiệt kế 5-10 phút
    - Nếu đo nách được 37.5°C → Nhiệt độ thực ≈ 38°C (đã cộng thêm)
    - Trẻ nhỏ: Nên đo ở hậu môn (chính xác nhất)
    - Nhiệt kế điện tử: Đọc kỹ hướng dẫn, đặt đúng vị trí
    """)


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


def render_medicine_tips():
    """Mẹo vặt về thuốc"""
    st.subheader("💊 Mẹo vặt về thuốc")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📅 Bảo quản thuốc",
        "💧 Cách uống thuốc",
        "🍽️ Thuốc & Thức ăn",
        "🔄 Tương tác thuốc"
    ])
    
    with tab1:
        st.markdown("""
        ### 🏠 Bảo quản thuốc đúng cách:
        
        **✅ Nơi khô ráo, thoáng mát:**
        - Tránh phòng tắm (ẩm ướt)
        - Tránh bếp (nóng)
        - Tránh ánh nắng trực tiếp
        
        **❄️ Thuốc cần bảo quản lạnh:**
        - Insulin → Tủ lạnh (2-8°C), không đông
        - Một số kháng sinh → Kiểm tra nhãn
        - Vắc-xin → Tủ lạnh bảo quản
        
        **📦 Giữ nguyên bao bì:**
        - Giữ hộp, tờ hướng dẫn
        - Không bỏ thuốc ra túi nilon
        - Ghi rõ ngày mở nếu dùng lâu
        
        **⏰ Kiểm tra hạn sử dụng:**
        - Thuốc hết hạn → Vứt đi
        - Thuốc bị đổi màu, mốc → Không dùng
        - Thuốc quá 6 tháng mở → Hỏi bác sĩ
        """)
        
        st.info("""
        💡 **Mẹo nhớ:**
        - Thuốc đắt tiền (Insulin, thuốc tim mạch) → Cất cẩn thận, tránh ánh sáng
        - Siro trẻ em → Sau khi mở, dùng trong 1-3 tháng (xem nhãn)
        - Thuốc nhỏ mắt → Sau mở dùng trong 1 tháng
        """)
    
    with tab2:
        st.markdown("""
        ### 💧 Cách uống thuốc đúng:
        
        **⏰ Uống đúng giờ:**
        - "Trước ăn 30 phút" → Uống lúc đói
        - "Sau ăn" → Uống sau khi ăn no
        - "Trong bữa ăn" → Uống giữa bữa
        - "Cách nhau 4-6 giờ" → Không uống liền nhau
        
        **💊 Cách nuốt viên:**
        - Uống với nước lọc (1 cốc to)
        - Không bẻ viên (trừ khi bác sĩ cho phép)
        - Không nhai viên bao phim (sẽ mất tác dụng)
        
        **🚫 Không uống với:**
        - ⛔ Rượu, bia (gây tương tác nguy hiểm)
        - ⛔ Nước chè, cà phê (một số thuốc)
        - ⛔ Nước nóng (phá hủy thuốc)
        - ⛔ Sữa (một số thuốc như kháng sinh)
        
        **✅ Nên uống với:**
        - Nước lọc (tốt nhất)
        - Nước ấm (một số thuốc Đông y)
        """)
        
        st.success("""
        💡 **Mẹo cho trẻ em:**
        - Viên nhỏ → Nghiền nhỏ, pha với chút nước đường
        - Siro → Dùng ống tiêm, bơm vào má (trẻ dễ nuốt)
        - Không ép trẻ → Dễ nôn, mất thuốc
        """)
    
    with tab3:
        st.markdown("""
        ### 🍽️ Thuốc & Thức ăn - Khi nào hợp lý?
        
        **📋 Bảng hướng dẫn uống thuốc thông dụng:**
        """)
        
        import pandas as pd
        
        med_food_data = {
            "Loại thuốc": [
                "Paracetamol (Panadol, Efferalgan)",
                "Ibuprofen (Brufen, Nurofen)",
                "Aspirin",
                "Thuốc kháng sinh (Amoxicillin, Ciprofloxacin...)",
                "Thuốc bổ sắt",
                "Canxi",
                "Vitamin D",
                "Thuốc huyết áp (Amlodipine, Enalapril...)",
                "Thuốc tiểu đường (Metformin)",
                "Omeprazole (giảm đau dạ dày)",
                "Thyroxine (hormone tuyến giáp)",
                "Kháng sinh Tetracycline"
            ],
            "Nên uống": [
                "Khi nào cũng được, với hoặc không với thức ăn",
                "Sau khi ăn no (tránh đau dạ dày)",
                "Sau khi ăn (tránh viêm dạ dày)",
                "Xem nhãn - thường sau ăn hoặc cách 2h với sữa",
                "Khi đói (hấp thu tốt hơn)",
                "Sau khi ăn (hấp thu tốt hơn)",
                "Sau khi ăn (cần chất béo để hấp thu)",
                "Theo chỉ định, thường sau ăn",
                "Sau khi ăn (giảm tác dụng phụ)",
                "Trước ăn 30 phút (tác dụng tốt nhất)",
                "Khi đói, trước ăn 30-60 phút",
                "Cách xa bữa ăn 2 giờ (trước hoặc sau)"
            ],
            "Tránh uống với": [
                "Rượu bia (SUY GAN!)",
                "Rượu bia, thức ăn cay",
                "Rượu bia, thức ăn cay",
                "Sữa, sữa chua (một số loại)",
                "Trà, cà phê, sữa (giảm hấp thu)",
                "Trà, cà phê (giảm hấp thu)",
                "Không có",
                "Nước bưởi (một số loại)",
                "Rượu bia",
                "Không có",
                "Sữa, canxi, sắt (cách xa 2-4 giờ)",
                "Sữa, canxi, sắt, thuốc kháng acid"
            ]
        }
        
        df = pd.DataFrame(med_food_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        st.warning("""
        ⚠️ **LƯU Ý QUAN TRỌNG:**
        
        - **Paracetamol + Rượu bia:** 🚫 TUYỆT ĐỐI TRÁNH! → Suy gan cấp tính, tử vong
        - **Thuốc huyết áp + Nước bưởi:** ⚠️ Một số loại tương tác → Hạ huyết áp quá mức
        - **Kháng sinh + Sữa:** ⚠️ Một số giảm hấp thu → Uống cách xa 2 giờ
        - **Aspirin/Ibuprofen:** ⚠️ Uống sau ăn để tránh viêm loét dạ dày
        """)
        
        st.info("""
        💡 **Mẹo nhớ:**
        
        - **Thuốc đau dạ dày (Omeprazole):** Uống TRƯỚC ăn 30 phút → Tác dụng tốt nhất
        - **Thuốc sắt:** Uống khi đói + uống nước cam (vitamin C giúp hấp thu)
        - **Canxi:** Uống sau ăn + không uống cùng sắt (cách xa 2 giờ)
        - **Kháng sinh:** Đọc kỹ nhãn, nhiều loại không uống với sữa
        """)
    
    with tab4:
        st.markdown("""
        ### 🔄 Tương tác thuốc nguy hiểm:
        
        **⚠️ Paracetamol + Rượu Bia:**
        - 🍺 **Rượu bia + Paracetamol = SUY GAN CẤP TÍNH, TỬ VONG!**
        - ⏰ Phải cách ít nhất **8-12 giờ** sau khi uống rượu bia
        - 🔥 Đau đầu do say rượu? → Uống nước, nghỉ ngơi, KHÔNG dùng paracetamol!
        
        **⚠️ Thuốc huyết áp + Nước bưởi:**
        - Một số thuốc huyết áp (Amlodipine, Felodipine, Nifedipine...) không uống với nước bưởi
        - → Tăng tác dụng, hạ huyết áp quá mức → Chóng mặt, ngất xỉu
        - ✅ An toàn: Losartan, Valsartan, Enalapril ít bị ảnh hưởng
        
        **⚠️ Aspirin + Thuốc chống đông:**
        - → Tăng nguy cơ chảy máu nghiêm trọng
        - Phải có chỉ định bác sĩ, theo dõi chặt chẽ
        
        **⚠️ Kháng sinh + Sữa/Canxi:**
        - Tetracycline, Ciprofloxacin không uống với sữa, canxi
        - → Tạo phức hợp không hấp thu được → Mất tác dụng
        - ✅ Cách xa bữa ăn/sữa 2 giờ
        
        **⚠️ Sắt + Trà/Cà phê:**
        - Trà, cà phê chứa tanin → Giảm hấp thu sắt
        - → Uống cách xa 1-2 giờ
        
        **✅ Nên làm:**
        - Kê khai đầy đủ thuốc đang uống với bác sĩ
        - Hỏi dược sĩ về tương tác
        - Đọc kỹ tờ hướng dẫn
        - Không tự ý kết hợp thuốc
        """)
        
        st.warning("""
        ⚠️ **Lưu ý quan trọng:**
        
        - Uống nhiều loại thuốc → Phải có bác sĩ theo dõi
        - Tự ý kết hợp thuốc → Nguy hiểm!
        - Có tác dụng phụ bất thường → Dừng thuốc, gọi bác sĩ ngay
        - Ghi nhớ: **Rượu bia + Paracetamol = TỬ VONG!**
        """)

