"""
Daily Health Tips - Preventive Care
Mẹo phòng bệnh
"""

import streamlit as st


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
        - **Sởi - Quai bị - Rubella:** Nhắc lại nếu cần (theo chỉ định)
        
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

