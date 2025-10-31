"""
Daily Health Tips
Mẹo vặt y tế hữu ích hàng ngày từ các nguồn uy tín
"""

import streamlit as st


def render_daily_health_tips():
    """Mẹo chăm sóc sức khỏe hàng ngày"""
    st.subheader("🌱 Mẹo chăm sóc sức khỏe hàng ngày")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 💧 1. Uống nước đủ lượng
        
        **💡 Tại sao quan trọng?**
        - Duy trì chức năng cơ thể
        - Thanh lọc độc tố
        - Giữ da đẹp, giảm táo bón
        
        **📊 Liều lượng:**
        - Người lớn: **2-2.5 lít/ngày** (8-10 cốc)
        - Trẻ em: **Theo cân nặng** (40-60ml/kg)
        - Người già: **1.5-2 lít/ngày** (nếu không hạn chế nước)
        
        **✅ Mẹo nhớ:**
        - Uống nước khi thức dậy (1 cốc)
        - Uống trước bữa ăn 30 phút
        - Uống nhiều khi sốt, đổ mồ hôi
        """)
        
        st.markdown("""
        ### 🏃 2. Vận động đều đặn
        
        **💡 Lợi ích:**
        - ✅ Tăng cường tim mạch
        - ✅ Giảm cân, kiểm soát đường huyết
        - ✅ Giảm căng thẳng, cải thiện tâm trạng
        - ✅ Tăng sức đề kháng
        
        **📅 Thời lượng:**
        - Người lớn: **150 phút/tuần** (≈30 phút/ngày, 5 ngày/tuần)
        - Hoặc: **75 phút vận động mạnh/tuần**
        - Trẻ em: **60 phút/ngày**
        
        **✅ Mẹo:**
        - Đi bộ nhanh 30 phút/ngày
        - Leo cầu thang thay vì thang máy
        - Đứng dậy mỗi 30-60 phút khi ngồi làm việc
        """)
        
        st.markdown("""
        ### 😴 3. Ngủ đủ giấc
        
        **💡 Tại sao quan trọng?**
        - Cơ thể phục hồi, tăng cường miễn dịch
        - Cải thiện trí nhớ, tâm trạng
        - Giảm nguy cơ bệnh tim, tiểu đường
        
        **📊 Thời lượng:**
        - Người lớn: **7-9 giờ/đêm**
        - Trẻ em: **10-14 giờ/ngày** (tùy tuổi)
        - Người già: **7-8 giờ/đêm**
        
        **✅ Mẹo ngủ ngon:**
        - Tắt điện thoại, TV 1 giờ trước khi ngủ
        - Giữ phòng tối, mát mẻ
        - Không uống cà phê sau 14h chiều
        - Ngủ đúng giờ, dậy đúng giờ
        """)
    
    with col2:
        st.markdown("""
        ### 🍎 4. Ăn uống cân đối
        
        **💡 Nguyên tắc:**
        - Ăn đủ 4 nhóm: Chất đạm, tinh bột, chất béo, rau quả
        - Hạn chế đường, muối
        - Uống đủ nước
        
        **📊 Khẩu phần:**
        - **Rau xanh:** 2-3 bát/bữa (chiếm 50% đĩa)
        - **Trái cây:** 2-3 phần/ngày (1 quả = 1 phần)
        - **Đạm:** 1 lòng bàn tay/bữa
        - **Tinh bột:** 1 bát cơm/bữa (tùy nhu cầu)
        
        **✅ Mẹo:**
        - Ăn chậm, nhai kỹ
        - Không bỏ bữa sáng
        - Ăn đa dạng, đủ màu sắc
        """)
        
        st.markdown("""
        ### 🧼 5. Vệ sinh tay đúng cách
        
        **💡 Tại sao quan trọng?**
        - Ngăn ngừa lây nhiễm vi khuẩn, virus
        - Giảm nguy cơ cảm cúm, tiêu chảy
        - Đặc biệt quan trọng trong mùa dịch
        
        **⏰ Khi nào rửa tay?**
        - Trước khi ăn, sau khi đi vệ sinh
        - Sau khi hắt hơi, ho
        - Sau khi chạm vào đồ vật công cộng
        - Sau khi tiếp xúc người bệnh
        
        **✅ Cách rửa:**
        - Rửa với xà phòng + nước 20-30 giây
        - Rửa kỹ: lòng bàn tay, mu bàn tay, kẽ ngón tay, móng tay
        - Lau khô bằng khăn sạch hoặc giấy
        """)
        
        st.markdown("""
        ### 🩺 6. Kiểm tra sức khỏe định kỳ
        
        **💡 Tại sao quan trọng?**
        - Phát hiện bệnh sớm → Điều trị dễ, hiệu quả cao
        - Ngăn ngừa biến chứng
        - Yên tâm về sức khỏe
        
        **📅 Lịch kiểm tra:**
        - **Người lớn (< 40):** 1-2 năm/lần
        - **Người lớn (≥ 40):** 6-12 tháng/lần
        - **Người có bệnh mãn tính:** Theo chỉ định bác sĩ
        
        **✅ Nên kiểm tra:**
        - Huyết áp, đường huyết, mỡ máu
        - Cân nặng, BMI
        - Xét nghiệm máu tổng quát
        - Khám mắt, răng (nếu cần)
        """)
    
    st.divider()
    
    st.markdown("""
    ### 🚫 7. Tránh thói quen có hại
    
    **❌ Hút thuốc lá:**
    - Tăng nguy cơ ung thư phổi, tim mạch
    - Ảnh hưởng người xung quanh (hút thuốc thụ động)
    - → **BỎ NGAY** nếu đang hút!
    
    **❌ Uống rượu bia quá mức:**
    - Gây hại gan, tim, não
    - Tăng nguy cơ ung thư
    - → **Hạn chế:** < 2 đơn vị/ngày (nam), < 1 đơn vị/ngày (nữ)
    
    **❌ Thức khuya thường xuyên:**
    - Giảm miễn dịch
    - Tăng nguy cơ bệnh tim mạch
    - → Ngủ đúng giờ, đủ giấc
    
    **❌ Ăn quá nhiều đường, muối:**
    - Đường: < 25-50g/ngày (6-12 thìa cà phê)
    - Muối: < 5g/ngày (1 thìa cà phê)
    - → Đọc nhãn thực phẩm, nấu ít đường/muối
    """)
    
    st.info("""
    💡 **Mẹo nhớ:**
    
    - **Rửa tay:** "Trước ăn, sau vệ sinh" → Dễ nhớ!
    - **Uống nước:** Đặt chai nước trên bàn → Nhắc nhở uống
    - **Vận động:** Đi bộ 30 phút/ngày → Không cần phòng gym
    - **Ngủ:** Tắt điện thoại 1h trước ngủ → Ngủ sâu hơn
    - **Ăn:** Màu càng đa dạng càng tốt → Đủ vitamin, khoáng chất
    """)


def render_preventive_care():
    """Mẹo phòng bệnh"""
    st.subheader("🛡️ Mẹo phòng bệnh")
    
    tab1, tab2, tab3 = st.tabs([
        "💉 Tiêm chủng",
        "🧘 Giảm căng thẳng",
        "🌿 Tăng cường miễn dịch"
    ])
    
    with tab1:
        st.markdown("""
        ### 💉 Tiêm chủng đầy đủ
        
        **💡 Tại sao quan trọng?**
        - Bảo vệ khỏi bệnh truyền nhiễm nguy hiểm
        - Giảm nguy cơ biến chứng
        - Bảo vệ cả gia đình, cộng đồng
        
        **📅 Lịch tiêm chủng (Người lớn):**
        - **Cúm:** Mỗi năm 1 lần (trước mùa cúm)
        - **Viêm gan B:** 3 mũi (nếu chưa tiêm)
        - **Uốn ván:** Nhắc lại mỗi 10 năm
        - **COVID-19:** Theo khuyến nghị y tế
        
        **✅ Mẹo:**
        - Ghi chép lịch tiêm vào sổ y tế
        - Nhắc nhở bác sĩ khi khám
        - Tiêm đúng lịch, không trễ
        """)
        
        st.warning("""
        ⚠️ **Lưu ý:**
        
        - Người dị ứng với thành phần vắc-xin → Hỏi bác sĩ
        - Đang sốt cao → Trì hoãn tiêm
        - Phụ nữ có thai → Hỏi bác sĩ về loại vắc-xin an toàn
        """)
    
    with tab2:
        st.markdown("""
        ### 🧘 Quản lý căng thẳng
        
        **💡 Tại sao quan trọng?**
        - Căng thẳng kéo dài → Tăng huyết áp, bệnh tim
        - Giảm miễn dịch, dễ ốm
        - Ảnh hưởng giấc ngủ, tâm trạng
        
        **✅ Mẹo giảm căng thẳng:**
        
        **1. Thở sâu (4-7-8):**
        - Hít vào 4 giây
        - Nín thở 7 giây
        - Thở ra 8 giây
        - Lặp lại 4-8 lần
        
        **2. Thiền 5-10 phút/ngày:**
        - Ngồi yên, nhắm mắt
        - Tập trung vào hơi thở
        - Để tâm trí thư giãn
        
        **3. Vận động nhẹ:**
        - Đi bộ, yoga, dưỡng sinh
        - 20-30 phút/ngày
        
        **4. Ngủ đủ giấc:**
        - 7-9 giờ/đêm
        - Ngủ sớm, dậy sớm
        
        **5. Trò chuyện, chia sẻ:**
        - Nói chuyện với người thân
        - Tìm sự hỗ trợ khi cần
        """)
        
        st.success("""
        💡 **Mẹo nhớ:**
        
        - **Thở sâu:** Áp dụng ngay khi cảm thấy căng thẳng
        - **Thiền:** Dùng app (Headspace, Calm) nếu mới bắt đầu
        - **Vận động:** Chỉ cần 20 phút/ngày → Giảm stress đáng kể
        """)
    
    with tab3:
        st.markdown("""
        ### 🌿 Tăng cường miễn dịch
        
        **💡 Tại sao quan trọng?**
        - Giảm nguy cơ cảm cúm, nhiễm khuẩn
        - Nhanh khỏi bệnh hơn
        - Sức khỏe tổng thể tốt hơn
        
        **✅ Mẹo tăng cường miễn dịch:**
        
        **1. Ăn đủ vitamin:**
        - **Vitamin C:** Cam, chanh, ổi, kiwi
        - **Vitamin D:** Ánh nắng sáng (15-30 phút), cá béo, lòng đỏ trứng
        - **Kẽm:** Thịt, hải sản, đậu
        
        **2. Ngủ đủ giấc:**
        - 7-9 giờ/đêm
        - Ngủ sớm (trước 23h)
        
        **3. Vận động vừa phải:**
        - 30 phút/ngày
        - Không tập quá sức (làm yếu miễn dịch)
        
        **4. Giảm căng thẳng:**
        - Thiền, yoga, thở sâu
        - Tránh lo âu, stress kéo dài
        
        **5. Vệ sinh tay:**
        - Rửa tay thường xuyên
        - Tránh chạm mặt khi chưa rửa tay
        
        **6. Tiêm chủng đầy đủ:**
        - Vắc-xin cúm hàng năm
        - Theo lịch tiêm chủng
        """)
        
        st.warning("""
        ⚠️ **Tránh:**
        
        - **Thức khuya thường xuyên** → Giảm miễn dịch
        - **Căng thẳng kéo dài** → Tăng cortisol → Ức chế miễn dịch
        - **Thiếu ngủ** → Giảm kháng thể
        - **Hút thuốc, uống rượu** → Tổn thương miễn dịch
        """)

