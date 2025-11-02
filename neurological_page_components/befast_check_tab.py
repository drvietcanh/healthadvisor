"""
Neurological Page Components - BE-FAST Check Tab
Tab Kiểm tra BE-FAST
"""

import streamlit as st


def render_befast_check_tab():
    """Render tab Kiểm tra BE-FAST"""
    st.header("📊 Kiểm tra triệu chứng đột quỵ")
    
    st.warning("⚠️ Công cụ này chỉ để tham khảo. Nếu nghi ngờ đột quỵ → GỌI 115 NGAY!")
    
    st.markdown("### Kiểm tra các dấu hiệu BE-FAST:")
    
    # Form kiểm tra
    with st.form("befast_check"):
        balance = st.checkbox("**B - Mất thăng bằng, chóng mặt đột ngột**")
        eyes = st.checkbox("**E - Nhìn mờ, nhìn đôi đột ngột**")
        face = st.checkbox("**F - Xệ mặt, méo miệng**")
        arm = st.checkbox("**A - Yếu tay hoặc chân (một bên)**")
        speech = st.checkbox("**S - Nói khó, nói lắp**")
        
        st.divider()
        onset_time = st.number_input(
            "Triệu chứng xuất hiện bao lâu rồi? (giờ)",
            min_value=0.0,
            max_value=72.0,
            value=2.0,
            step=0.5
        )
        
        submitted = st.form_submit_button("Đánh giá", type="primary")
    
    if submitted:
        has_symptoms = any([balance, eyes, face, arm, speech])
        
        if has_symptoms:
            st.error("### 🚨 NGHI NGỜ ĐỘT QUỴ - HÀNH ĐỘNG NGAY!")
            st.error("### 👉 GỌI CẤP CỨU 115 NGAY!")
            
            positive_signs = []
            if balance: positive_signs.append("Mất thăng bằng")
            if eyes: positive_signs.append("Rối loạn nhìn")
            if face: positive_signs.append("Xệ mặt")
            if arm: positive_signs.append("Yếu tay chân")
            if speech: positive_signs.append("Nói khó")
            
            st.markdown(f"**Dấu hiệu phát hiện:** {', '.join(positive_signs)}")
            st.markdown(f"**Thời gian:** {onset_time} giờ trước")
            
            # Kiểm tra khung giờ điều trị
            if onset_time <= 4.5:
                st.success("✅ VẪN TRONG KHUNG GIỜ VÀNG tiêm thuốc tiêu sợi huyết!")
                st.success(f"Còn khoảng {4.5 - onset_time:.1f} giờ - NHANH LÊN!")
            elif onset_time <= 24:
                st.warning(f"⚠️ Vẫn trong khung giờ lấy huyết khối (24h)")
                st.warning("Vẫn CÓ THỂ điều trị - ĐỪNG BỎ LỠ!")
            else:
                st.error("Đã quá 24 giờ - Nhưng vẫn CẦN khám ngay để đánh giá và phòng ngừa")
            
            st.divider()
            st.markdown("""
#### ⏰ TRƯỚC KHI ĐẾN BỆNH VIỆN:
- ✅ GHI NHỚ thời điểm bình thường cuối cùng
- ✅ KHÔNG tự lái xe - Chờ xe cấp cứu
- ✅ KHÔNG cho ăn uống (nguy cơ sặc)
- ✅ Mang theo danh sách thuốc đang dùng
- ✅ Nằm đầu cao (kê 2-3 cái gối)
""")
        else:
            st.success("### ✅ Không có dấu hiệu đột quỵ rõ ràng")
            st.info("Tuy nhiên, nếu có bất kỳ triệu chứng bất thường nào, hãy gặp bác sĩ để kiểm tra.")

