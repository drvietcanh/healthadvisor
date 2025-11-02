"""
Giun Kim (Pinworm/Threadworm) Tab
"""
import streamlit as st

def render_pinworm_tab():
    """Render tab Giun Kim"""
    st.header("📌 Giun Kim - Bệnh gây ngứa hậu môn")
    
    st.markdown("""
    <div class="info-box">
        <b>💡 Hiểu đơn giản:</b><br>
        Giun kim rất nhỏ, sống trong đại tràng. Ban đêm, giun chui ra hậu môn đẻ trứng → Ngứa dữ dội.
        Trẻ em hay bị nhất, lây lan rất nhanh trong gia đình.
    </div>
    """, unsafe_allow_html=True)
    
    # Nguyên nhân và con đường lây
    with st.expander("🔍 Nguyên nhân & Con đường lây bệnh", expanded=True):
        st.markdown("""
        ### 🦠 Nguyên nhân:
        - **Giun kim (Enterobius vermicularis):** Dài 0.5-1cm, trắng như sợi chỉ
        - Trẻ em bị nhiều nhất (50-80% trẻ tuổi mầm non)
        - Sống trong đại tràng, ban đêm ra ngoài hậu môn đẻ trứng
        
        ### 🗺️ Con đường lây bệnh:
        1. **Tự lây (thường gặp nhất):**
           - Gãi hậu môn → Trứng dính móng tay
           - Đưa tay vào miệng → Nuốt trứng
           - → Nhiễm đi nhiễm lại
           
        2. **Lây trong gia đình:**
           - Trứng bay lơ lửng trong không khí
           - Bám vào quần áo, chăn gối, đồ chơi
           - Cả nhà hít phải trứng
        
        3. **Trẻ mầm non:**
           - Dùng chung đồ chơi
           - Không rửa tay
           - Ngủ chung giường
    """)
    
    # Triệu chứng
    with st.expander("⚕️ Triệu chứng nhận biết"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🔴 Triệu chứng chính:
            - **Ngứa hậu môn:** Dữ dội vào ban đêm (10-11h tối)
            - **Giấc ngủ kém:** Quấy khóc, trằn trọc
            - **Ban ngày bình thường:** Không ngứa nhiều
            
            ### 🟡 Triệu chứng khác:
            - **Gầy, kém ăn:** Do ngứa, khó chịu
            - **Nghiến răng:** Khi ngủ (một số trẻ)
            - **Kích thích:** Khó chịu, dễ cáu
            """)
        
        with col2:
            st.markdown("""
            ### 👀 Dấu hiệu nhận biết:
            - **Thấy giun:** Nhỏ như sợi chỉ, trắng
            - **Vùng hậu môn ửng đỏ:** Do gãi
            - **Trẻ hay gãi đít:** Lúc tối, khi ngủ
            - **Da nhiễm trùng:** Nếu gãi quá nhiều
            
            ### 🚨 Biến chứng hiếm:
            - Viêm âm đạo (ở bé gái)
            - Viêm ruột thừa (rất hiếm)
    """)
    
    # Kiểm tra giun kim
    with st.expander("🔎 Cách kiểm tra có giun kim"):
        st.markdown("""
        ### ✅ Test đơn giản tại nhà:
        
        **1. Soi đèn (tối 10-11h):**
        - Tắt đèn, bật đèn pin
        - Nhìn vùng hậu môn bé
        - Sẽ thấy giun trắng nhỏ bò ra ngoài
        
        **2. Dùng băng keo:**
        - Dán băng keo 2 mặt vào hậu môn
        - Để 1 đêm (trước khi tắm)
        - Sáng hôm sau gỡ ra → Đem bác sĩ soi
        
        **3. Xét nghiệm phân:**
        - Thường KHÔNG phát hiện được
        - Vì giun không đẻ trứng trong phân
        - Dùng test băng keo tốt hơn
    """)
    
    # Điều trị
    with st.expander("💊 Thuốc tẩy giun (theo chỉ định bác sĩ)"):
        st.markdown("""
        ### ✅ Thuốc điều trị:
        
        **1. Mebendazole (Vermox) - TỐT NHẤT:**
        - Liều: 1 viên 100mg duy nhất
        - Người lớn & trẻ >1 tuổi: Uống lại sau 2 tuần
        - **CẢ NHÀ CÙNG UỐNG** (quan trọng!)
        - Giá: ~20.000 VNĐ
        
        **2. Albendazole (Zentel):**
        - Liều: 1 viên 400mg duy nhất
        - Uống lại sau 2 tuần
        - Giá: ~25.000 VNĐ
        
        **3. Pyran tel (Combantrin):**
        - Liều: 10mg/kg cân nặng
        - Uống lại sau 2 tuần
        - Giá: ~30.000 VNĐ
        
        ### ⚠️ Lưu ý QUAN TRỌNG:
        **Phải uống lại sau 2 tuần:**
        - Liều 1: Diệt giun trưởng thành
        - Liều 2: Diệt giun non mới nở từ trứng
        - Nếu chỉ uống 1 lần → Sẽ bị lại
        
        **CẢ NHÀ CÙNG UỐNG:**
        - Giun kim lây rất nhanh
        - Trẻ em đã bị → Cả nhà cũng có
        - Chỉ 1 người không uống → Lây lại
    """)
    
    # Phòng ngừa
    with st.expander("🛡️ Phòng ngừa - Rất quan trọng!"):
        st.markdown("""
        ### ✅ Quy tắc VÀNG:
        
        **1. 🧼 Vệ sinh tay:**
        - Rửa tay với xà phòng (20 giây)
        - Trước ăn, sau đi vệ sinh
        - Cắt móng tay ngắn (không để trứng dính)
        
        **2. 🛏️ Vệ sinh giường chiếu:**
        - Giặt chăn, gối, khăn trong nước nóng
        - Phơi nắng to (giết trứng)
        - Vệ sinh đồ chơi của trẻ
        
        **3. 🩲 Mặc quần lót chật:**
        - Ngăn trẻ gãi hậu môn
        - Thay quần lót sáng hôm sau
        - Giặt riêng với nước nóng
        
        **4. 🚿 Tắm rửa sạch:**
        - Tắm ngay khi thức dậy
        - Rửa hậu môn kỹ
        - Không tắm chung với trẻ khác (khi đang bị)
        
        **5. 🔁 Tẩy giun định kỳ:**
        - Nếu thường xuyên bị → 3 tháng 1 lần
        - Cả nhà cùng uống
    """)
    
    # Tại sao hay bị lại
    with st.expander("🤔 Tại sao giun kim hay bị lại?"):
        st.markdown("""
        ### 🔄 Chu kỳ lây:
        
        **Ban đêm (10-11h):**
        1. Giun trưởng thành chui ra hậu môn
        2. Đẻ trứng (hàng ngàn quả)
        3. Trứng dính vào da, quần áo
        4. Bé gãi → Trứng dính móng tay
        
        **Sáng hôm sau:**
        5. Đưa tay vào miệng → Nuốt trứng
        6. Trứng nở thành giun non
        7. Sau 2-6 tuần → Giun trưởng thành
        8. Lại chui ra đẻ trứng...
        
        **→ Chu kỳ lặp lại liên tục!**
        
        💡 **Vì thế:** Phải vệ sinh rất kỹ + Uống thuốc đúng 2 lần.
    """)
    
    # FAQ
    st.markdown("---")
    st.subheader("❓ Câu hỏi thường gặp")
    
    with st.expander("🤔 Con tôi gãi đít tối, có phải giun kim không?"):
        st.markdown("""
        **90% CÓ THỂ là giun kim** nếu:
        - Ngứa dữ dội vào buổi tối
        - Ngứa quanh hậu môn (không phải vùng khác)
        - Sáng lại bình thường
        
        **Làm gì:**
        1. Soi đèn pin tối 10-11h → Xem có giun không
        2. Nếu thấy: Uống thuốc tẩy giun
        3. Nếu không thấy: Thử dùng băng keo test
        """)
    
    with st.expander("🤔 Tại sao phải uống thuốc 2 lần cách 2 tuần?"):
        st.markdown("""
        **Vì chu kỳ sống của giun:**
        - Liều 1: Chỉ diệt giun đã trưởng thành
        - Sau 2 tuần: Giun non trong cơ thể mới lớn
        - Liều 2: Diệt đợt giun non này
        
        **Nếu chỉ uống 1 lần:**
        - Sau 2-3 tuần → Bị lại
        - Vì giun non vẫn còn trong cơ thể
        
        → NHẤT ĐỊNH phải uống đủ 2 liều!
        """)
    
    with st.expander("🤔 Tại sao cả nhà phải uống dù chỉ trẻ bị?"):
        st.markdown("""
        **Giun kim lây vô cùng nhanh:**
        - Trứng bay trong không khí
        - Bám vào quần áo, chăn gối
        - Ai hít phải trứng đều bị nhiễm
        
        **Thực tế:**
        - Bé nhỏ bị → Mẹ bế cũng nhiễm
        - Ngủ chung giường → Cả nhà nhiễm
        - Dùng chung khăn → Lây tiếp
        
        **Chỉ 1 người không uống:**
        - Sẽ đẻ trứng lại
        - → Cả nhà bị lây lại
        
        → **LUÔN LUÔN CẢ NHÀ CÙNG UỐNG!**
        """)
    
    # Cảnh báo cuối
    st.markdown("""
    ---
    <div class="warning-box">
        <b>⚠️ QUAN TRỌNG:</b><br>
        • Giun kim lây RẤT NHANH - Cả nhà phải điều trị!<br>
        • Uống thuốc ĐỦ 2 LIỀU cách 2 tuần<br>
        • Vệ sinh sạch sẽ: Tay, giường, quần áo<br>
        • Thông tin trên chỉ mang tính chất <b>THAM KHẢO</b><br>
        • <b>KHÔNG THAY THẾ</b> tư vấn của bác sĩ
    </div>
    """, unsafe_allow_html=True)

