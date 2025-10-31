"""
Exercise Guide - Hướng dẫn bài tập thể thao cho các bệnh
Bổ sung vào trang Mẹo Vặt
"""

import streamlit as st


def render_general_exercise_tips():
    """Bài tập thể thao chung cho mọi người"""
    st.subheader("🏃 Bài Tập Thể Thao Chung")
    
    st.markdown("""
    ### 📋 Nguyên Tắc Chung:
    
    **✅ Áp dụng cho MỌI NGƯỜI:**
    - Vận động ít tốt hơn KHÔNG vận động
    - Bắt đầu NHẸ, tăng dần
    - Tập ĐỀU ĐẶN quan trọng hơn tập mạnh
    - Nghỉ khi đau, mệt
    """)
    
    tab1, tab2, tab3 = st.tabs([
        "💪 Bài tập cơ bản",
        "🫀 Bài tập tim mạch",
        "🧘 Thư giãn & Dẻo dai"
    ])
    
    with tab1:
        st.markdown("""
        ### 💪 Tăng Cường Cơ Bắp:
        
        **Tại sao quan trọng?**
        - Cơ mạnh → Bảo vệ khớp, xương
        - Giảm đau lưng, đau khớp
        - Tăng chuyển hóa, giảm cân
        - Giảm nguy cơ té ngã (người già)
        
        **Bài tập cơ bản:**
        - **Tập tại nhà:** Gập bụng, plank, squat nhẹ
        - **Tần suất:** 2-3 lần/tuần, mỗi lần 20-30 phút
        - **Bắt đầu:** 10-15 phút, tăng dần
        """)
        
        st.info("""
        💡 **Mẹo:**
        - Không cần phòng gym, chỉ cần thảm tập
        - Tập cùng nhạc → Vui hơn, dễ duy trì
        - Tập buổi sáng → Tăng năng lượng cả ngày
        """)
    
    with tab2:
        st.markdown("""
        ### 🫀 Bài Tập Tim Mạch:
        
        **Lợi ích:**
        - Tăng sức khỏe tim, phổi
        - Giảm huyết áp, đường huyết
        - Giảm cân
        - Cải thiện tâm trạng
        
        **Loại bài tập:**
        - **Đi bộ:** Dễ nhất, an toàn
        - **Bơi lội:** Tốt cho khớp (không tải trọng)
        - **Đạp xe:** Vận động nhẹ nhàng
        - **Khiêu vũ:** Vui, dễ duy trì
        
        **Thời lượng:**
        - Người lớn: 150 phút/tuần (≈30 phút/ngày, 5 ngày)
        - Hoặc: 75 phút vận động mạnh/tuần
        """)
        
        st.success("""
        ✅ **Bắt đầu từ đâu?**
        
        1. Tuần 1-2: Đi bộ 10-15 phút/ngày
        2. Tuần 3-4: Tăng lên 20-25 phút
        3. Tuần 5+: Đạt 30 phút/ngày
        
        ⚠️ **Dừng ngay nếu:** Đau ngực, khó thở nhiều, chóng mặt
        """)
    
    with tab3:
        st.markdown("""
        ### 🧘 Thư Giãn & Dẻo Dai:
        
        **Lợi ích:**
        - Giảm căng thẳng
        - Tăng độ linh hoạt
        - Giảm đau cứng
        - Cải thiện tư thế
        
        **Loại bài tập:**
        - **Yoga:** Kéo giãn + thở + thư giãn
        - **Thái cực quyền:** Vận động chậm, nhẹ nhàng
        - **Pilates:** Tăng cơ + dẻo dai
        - **Kéo giãn đơn giản:** Làm tại nhà 10-15 phút/ngày
        
        **Tần suất:**
        - Hàng ngày (khi thức dậy hoặc trước khi ngủ)
        - 10-20 phút
        """)
        
        st.info("""
        💡 **Mẹo:**
        - Kéo giãn BUỔI SÁNG → Giảm cứng cơ
        - Kéo giãn SAU TẬP → Giảm đau cơ
        - Thở sâu khi kéo giãn → Thư giãn hơn
        """)


def render_disease_specific_exercises():
    """Bài tập riêng cho từng bệnh"""
    st.subheader("🏥 Bài Tập Cho Từng Bệnh Cụ Thể")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "❤️ Tim mạch",
        "🩸 Tiểu đường",
        "🦴 Khớp & Cột sống",
        "🫁 Hô hấp",
        "⚖️ Giảm cân"
    ])
    
    with tab1:
        st.markdown("""
        ### ❤️ Bài Tập Cho Người Bệnh Tim Mạch:
        
        **⚠️ QUAN TRỌNG:** Hỏi bác sĩ trước khi tập!
        
        **Bài tập phù hợp:**
        - ✅ **Đi bộ:** 20-30 phút/ngày, chậm → tăng dần
        - ✅ **Bơi lội:** Tốt, không gây áp lực tim
        - ✅ **Đạp xe:** Nhẹ nhàng, trên mặt phẳng
        - ✅ **Yoga nhẹ:** Tốt cho tim mạch
        
        **TRÁNH:**
        - ❌ Tập quá sức đột ngột
        - ❌ Nâng tạ nặng
        - ❌ Chạy nhanh
        - ❌ Tập khi mệt, đau ngực
        
        **Dấu hiệu DỪNG NGAY:**
        - Đau ngực
        - Khó thở nhiều
        - Chóng mặt, choáng
        - Tim đập loạn nhịp
        """)
    
    with tab2:
        st.markdown("""
        ### 🩸 Bài Tập Cho Người Tiểu Đường:
        
        **Lợi ích:**
        - Giảm đường huyết (hiệu quả như thuốc!)
        - Tăng độ nhạy insulin
        - Giảm cân
        - Giảm nguy cơ biến chứng
        
        **Bài tập phù hợp:**
        - ✅ **Đi bộ:** 30 phút/ngày, sau bữa ăn 30-60 phút
        - ✅ **Tập kháng lực:** Tăng cơ → Giảm đường huyết
        - ✅ **Yoga, thái cực quyền:** Giảm stress
        - ✅ **Bơi lội:** Toàn thân, không gây chấn thương chân
        
        **⚠️ Lưu ý:**
        - Kiểm tra đường huyết trước và sau tập
        - Mang kẹo ngọt (phòng hạ đường huyết)
        - Không tập khi đường huyết >250 mg/dL hoặc <100 mg/dL
        - Bảo vệ chân (giày tốt, kiểm tra chân sau tập)
        """)
    
    with tab3:
        st.markdown("""
        ### 🦴 Bài Tập Cho Đau Khớp & Cột Sống:
        
        **Nguyên tắc:** Vận động NHẸ, đều đặn
        
        **Cho khớp gối:**
        - Nâng chân thẳng (nằm)
        - Đạp xe tại chỗ
        - Đi bộ nhẹ
        - Bơi lội
        
        **Cho đau lưng:**
        - Nằm co gối (kéo giãn)
        - Gập bụng nhẹ
        - Plank (tăng cơ bụng, lưng)
        - Đi bộ
        
        **Cho cứng khớp:**
        - Chườm nóng trước
        - Kéo giãn nhẹ nhàng
        - Vận động từ từ
        
        **TRÁNH:**
        - Chạy bộ (đau gối)
        - Gập lưng quá mức
        - Tập khi đang đau nhiều
        """)
        
        st.info("""
        💡 **Mẹo:**
        - Tập trong nước → Giảm áp lực lên khớp
        - Bắt đầu 5-10 phút, tăng dần
        - Nghỉ khi đau TĂNG
        """)
    
    with tab4:
        st.markdown("""
        ### 🫁 Bài Tập Cho COPD & Hen Suyễn:
        
        **Mục tiêu:** Tăng sức bền, giảm khó thở
        
        **Bài tập phù hợp:**
        - ✅ **Đi bộ:** Từ 5-10 phút → tăng dần
        - ✅ **Đạp xe tại chỗ:** Không cần đi xa
        - ✅ **Bài tập thở:** Thở môi mím, thở bụng
        - ✅ **Tập tay nhẹ:** Tăng cơ, giảm khó thở
        
        **Kỹ thuật thở:**
        - **Thở môi mím:** Hít vào mũi, thở ra bằng miệng (mím môi)
        - **Thở bụng:** Thở sâu, bụng phình ra
        - **Thở nhịp:** Hít 2 nhịp, thở 4 nhịp
        
        **⚠️ Lưu ý:**
        - Tập CHẬM, nghỉ nhiều
        - Xịt thuốc trước khi tập (nếu cần)
        - Dừng khi khó thở nhiều
        - Tập buổi sáng (không khí tốt hơn)
        """)
    
    with tab5:
        st.markdown("""
        ### ⚖️ Bài Tập Giảm Cân:
        
        **Kết hợp 2 loại:**
        1. **Tim mạch:** Đốt calories
        2. **Kháng lực:** Tăng cơ → Tăng chuyển hóa
        
        **Chương trình mẫu:**
        - **Ngày 1,3,5:** Đi bộ 30 phút + Tập kháng lực 15 phút
        - **Ngày 2,4,6:** Bơi hoặc đạp xe 30 phút
        - **Ngày 7:** Nghỉ hoặc yoga nhẹ
        
        **Lưu ý:**
        - Tập đều đặn quan trọng hơn tập mạnh
        - Kết hợp ăn kiêng (tập không giảm cân nếu ăn nhiều!)
        - Uống đủ nước
        - Nghỉ đủ để cơ phục hồi
        """)
        
        st.warning("""
        ⚠️ **Tránh:**
        - Tập quá sức đột ngột → Chấn thương
        - Chỉ tập tim mạch → Mất cơ
        - Bỏ tập nhiều ngày → Mất động lực
        """)
    
    st.markdown("""
    ---
    
    ### 💡 Nguyên Tắc Chung:
    
    1. **Bắt đầu NHẸ:** 10-15 phút/ngày
    2. **Tăng DẦN:** Thêm 5 phút mỗi tuần
    3. **Duy trì:** Tập đều đặn quan trọng hơn tập mạnh
    4. **Nghỉ khi cần:** Đau, mệt → Dừng ngay
    5. **Hỏi bác sĩ:** Nếu có bệnh mãn tính
    
    ### ⚠️ Dừng tập ngay nếu:
    - Đau ngực
    - Khó thở nhiều
    - Chóng mặt, choáng
    - Đau khớp tăng
    - Cảm thấy không ổn
    """)

