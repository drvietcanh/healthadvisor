"""
Giun Đũa (Ascariasis) Tab
"""
import streamlit as st

def render_ascarid_tab():
    """Render tab Giun Đũa"""
    st.header("🐛 Giun Đũa - Bệnh giun phổ biến nhất Việt Nam")
    
    st.markdown("""
    <div class="info-box">
        <b>💡 Hiểu đơn giản:</b><br>
        Giun đũa là loài ký sinh trùng sống trong ruột người, lây qua đường ăn uống.
        Ở Việt Nam, >40% trẻ em bị nhiễm giun đũa do điều kiện vệ sinh kém.
    </div>
    """, unsafe_allow_html=True)
    
    # Nguyên nhân và con đường lây
    with st.expander("🔍 Nguyên nhân & Con đường lây bệnh", expanded=True):
        st.markdown("""
        ### 🦠 Nguyên nhân:
        - **Giun đũa (Ascaris lumbricoides):** Loài ký sinh trùng dài 15-35cm, màu hồng trắng
        - Sống trong ruột non người, đẻ trứng theo phân ra ngoài
        - Trứng tồn tại lâu trong đất (2-3 tuần), chịu được nắng mưa
        
        ### 🗺️ Con đường lây bệnh:
        1. **Ăn phải trứng giun:** 
           - Rau sống không rửa sạch
           - Tay bẩn cầm thức ăn
           - Trẻ em chơi đất, đưa tay vào miệng
           
        2. **Ở nông thôn VN:**
           - Phân bón rau không ủ kỹ
           - Nguồn nước ô nhiễm phân người
           - Tắm ao, hồ có nước dơ
    """)
    
    # Triệu chứng
    with st.expander("⚕️ Triệu chứng nhận biết"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🟢 Triệu chứng nhẹ:
            - **Không có triệu chứng** (70% trường hợp)
            - Khó tiêu nhẹ
            - Đầy bụng sau ăn
            """)
        
        with col2:
            st.markdown("""
            ### 🔴 Triệu chứng nặng:
            - **Đau bụng quặn:** Đau quanh rốn
            - **Buồn nôn, nôn:** Có thể nôn ra giun
            - **Tiêu chảy:** Phân lỏng, có thể có giun
            - **Gầy yếu, suy dinh dưỡng:** Giun ăn thức ăn
            - **Ho, khó thở:** Giun di chuyển lên phổi
            """)
    
    # Biến chứng nguy hiểm
    with st.expander("⚠️ Biến chứng nguy hiểm - CẦN CẤP CỨU!"):
        st.markdown("""
        ### 🚨 Tắc ruột do giun:
        - **Dấu hiệu:** Đau bụng dữ dội, nôn nhiều, bụng chướng
        - **Nguyên nhân:** Quá nhiều giun quấn nhau thành búi
        - **Xử trí:** GỌI 115 NGAY! Phải mổ gấp
        
        ### 🚨 Giun chui lên phổi:
        - **Dấu hiệu:** Ho dữ dội, khó thở, sốt
        - **Nguyên nhân:** Giun non di chuyển lên phổi
        - **Xử trí:** Khám bác sĩ ngay
    """)
    
    # Điều trị
    with st.expander("💊 Thuốc tẩy giun (theo chỉ định bác sĩ)"):
        st.markdown("""
        ### ✅ Thuốc an toàn & hiệu quả:
        
        **1. Mebendazole (Vermox):**
        - Liều: 1 viên 100mg x 2 lần/ngày x 3 ngày
        - Cho: Người lớn và trẻ >2 tuổi
        - Giá: ~20.000 VNĐ/hộp
        
        **2. Albendazole (Zentel):**
        - Liều: 1 viên 400mg duy nhất (1 ngày)
        - Cho: Người lớn và trẻ >2 tuổi  
        - Giá: ~25.000 VNĐ/viên
        
        **3. Pyran tel (Combantrin):**
        - Liều: 10mg/kg cân nặng duy nhất
        - Cho: Trẻ em và người lớn
        - Giá: ~30.000 VNĐ
        
        ### ⚠️ Lưu ý khi uống thuốc:
        1. **Uống theo chỉ định bác sĩ** - Không tự ý tăng liều
        2. **Nhịn ăn trước khi uống 2 giờ** - Thuốc hấp thu tốt hơn
        3. **Tẩy cả nhà cùng lúc** - Tránh lây chéo
        4. **Tẩy lại sau 2 tuần** - Tiêu diệt giun non
    """)
    
    # Phòng ngừa
    with st.expander("🛡️ Phòng ngừa quan trọng"):
        st.markdown("""
        ### ✅ Quy tắc 5 ĐÚNG:
        
        **1. 🧼 Rửa tay đúng cách:**
        - Rửa với xà phòng trước ăn, sau đi vệ sinh
        - Không dùng chung khăn lau tay
        
        **2. 🥬 Rửa rau sạch sẽ:**
        - Ngâm muối loãng 15 phút
        - Rửa dưới vòi nước chảy 3-4 lần
        - Nấu chín khi có thể
        
        **3. 💧 Uống nước sạch:**
        - Đun sôi để nguội
        - Không uống nước ao, hồ
        - Rửa sạch bình nước
        
        **4. 🚽 Vệ sinh nhà cửa:**
        - Đi vệ sinh đúng nơi, đúng cách
        - Không thả rông trẻ em
        - Phân bón phải ủ hoai ít nhất 3 tháng
        
        **5. 🔁 Tẩy giun định kỳ:**
        - Trẻ 2-12 tuổi: **6 tháng 1 lần**
        - Người lớn: **12 tháng 1 lần**
        - Cả nhà cùng uống để hiệu quả
    """)
    
    # Mẹo dân gian
    with st.expander("🌿 Mẹo dân gian (bổ sung, không thay thế thuốc)"):
        st.markdown("""
        ### 💡 Mẹo hỗ trợ:
        
        **1. Ăn đu đủ xanh:**
        - Ăn 1 bát đu đủ xanh với mật ong lúc sáng sớm
        - Enzyme papain giúp làm tê liệt giun
        - **Chỉ hỗ trợ, không diệt giun triệt để!**
        
        **2. Uống nước sả tươi:**
        - Ép 1-2 củ sả lấy nước
        - Uống trước khi ăn sáng
        - Hỗ trợ tống giun ra ngoài
        
        **3. Ăn tỏi sống:**
        - Ăn 2-3 tép tỏi sống/ngày
        - Hoặc ép lấy nước uống
        - All trong tỏi có tác dụng kháng ký sinh
        
        ⚠️ **Quan trọng:** Mẹo dân gian không thay thế thuốc tẩy giun!
    """)
    
    # FAQ
    st.markdown("---")
    st.subheader("❓ Câu hỏi thường gặp")
    
    with st.expander("🤔 Con tôi có giun, có nguy hiểm không?"):
        st.markdown("""
        **Thông thường KHÔNG nguy hiểm**, nhưng cần điều trị:
        - Giun ăn thức ăn → Con gầy yếu, suy dinh dưỡng
        - Giun tiết độc tố → Dễ bệnh, miễn dịch kém
        - Nhiều giun quá → Tắc ruột (hiếm nhưng nguy hiểm)
        
        **Giải pháp:** Tẩy giun ngay theo chỉ định bác sĩ!
        """)
    
    with st.expander("🤔 Bao lâu tẩy giun 1 lần?"):
        st.markdown("""
        **Theo WHO khuyến cáo:**
        - Trẻ em (2-12 tuổi): **6 tháng 1 lần**
        - Người lớn: **12 tháng 1 lần**
        - Người ở vùng nhiễm cao: **3 tháng 1 lần**
        
        **VN hiện nay:** Khuyến cáo tẩy 6 tháng/lần cho tất cả trẻ em!
        """)
    
    with st.expander("🤔 Tôi đã tẩy giun rồi sao vẫn bị?"):
        st.markdown("""
        **Có 3 nguyên nhân chính:**
        1. **Tẩy không đúng cách:** Không tẩy lại sau 2 tuần
        2. **Vệ sinh kém:** Vẫn ăn phải trứng giun từ môi trường
        3. **Cả nhà chưa tẩy:** Lây chéo từ người thân
        
        **Giải pháp:** 
        - Tẩy lại đúng quy trình (1 liều, sau 2 tuần 1 liều nữa)
        - Cả nhà cùng tẩy
        - Cải thiện vệ sinh cá nhân, ăn chín uống sôi
        """)
    
    # Cảnh báo cuối
    st.markdown("""
    ---
    <div class="warning-box">
        <b>⚠️ QUAN TRỌNG:</b><br>
        • Thông tin trên chỉ mang tính chất <b>THAM KHẢO</b><br>
        • <b>KHÔNG THAY THẾ</b> tư vấn của bác sĩ<br>
        • Với triệu chứng nặng: <b>KHÁM BÁC SĨ NGAY</b><br>
        • Thuốc tẩy giun cần có <b>chỉ định BÁC SĨ</b>
    </div>
    """, unsafe_allow_html=True)

