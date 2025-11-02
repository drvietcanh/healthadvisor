"""
Lỵ Amip (Amoebic Dysentery) Tab
"""
import streamlit as st

def render_amoebic_dysentery_tab():
    """Render tab Lỵ Amip"""
    st.header("🦠 Lỵ Amip - Tiêu chảy ra máu kèm mủ")
    
    st.markdown("""
    <div class="info-box">
        <b>💡 Hiểu đơn giản:</b><br>
        Lỵ amip là bệnh nhiễm ký sinh đơn bào, gây tiêu chảy ra máu kèm mủ nhầy.
        Lây qua nước uống, thức ăn nhiễm bẩn. Phổ biến ở vùng nhiệt đới.
    </div>
    """, unsafe_allow_html=True)
    
    # Nguyên nhân và con đường lây
    with st.expander("🔍 Nguyên nhân & Con đường lây bệnh", expanded=True):
        st.markdown("""
        ### 🦠 Nguyên nhân:
        - **Entamoeba histolytica:** Đơn bào ký sinh trong đại tràng
        - Ăn vào trứng kén → Nở trong ruột → Đi vào thành ruột gây viêm
        - Phổ biến: VN, Ấn Độ, Châu Phi, Trung Mỹ
        
        ### 🗺️ Con đường lây bệnh:
        1. **Qua nước uống:**
           - Uống nước ao, hồ không sạch
           - Nước giếng không đun sôi
           - Nước đá không rõ nguồn gốc
           
        2. **Qua thức ăn:**
           - Rau sống không rửa sạch
           - Thức ăn để lâu, không che đậy
           - Ruồi/bọ làm nhiễm thức ăn
        
        3. **Qua phân:**
           - Phân người bệnh không xử lý
           - Dùng phân bón rau không ủ
           - Vệ sinh kém
        
        4. **Vùng nguy cơ:**
           - Nông thôn, miền núi
           - Nguồn nước không sạch
           - Vệ sinh kém
    """)
    
    # Triệu chứng
    with st.expander("⚕️ Triệu chứng nhận biết"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🟢 Lỵ nhẹ (90% người):
            - **Tiêu chảy nhẹ:** 5-10 lần/ngày
            - **Phân nhầy:** Có chút máu
            - **Đau bụng:** Quặn từng cơn
            - Tự khỏi sau vài ngày
            
            ### 🟡 Lỵ cấp (10% người):
            - **Tiêu chảy dữ dội:** 20-30 lần/ngày
            - **Phân:** Máu + mủ nhầy
            - **Đau bụng:** Quặn dữ dội
            - **Sốt nhẹ:** 38-39°C
            """)
        
        with col2:
            st.markdown("""
            ### 🔴 Lỵ nặng:
            - **Mất nước:** Da khô, mắt trũng
            - **Sốt cao:** 39-40°C
            - **Đau bụng:** Dữ dội, không chịu được
            - **Toàn thân:** Mệt mỏi, gầy sút
            
            ### 🚨 Biến chứng:
            - **Viêm gan amip:** Đau bụng phải, sốt
            - **Áp xe gan:** Nang to trong gan
            - **Thủng đại tràng:** Nguy hiểm!
            - **Lây lan:** Amip vào máu → Toàn thân
    """)
    
    # Biến chứng nguy hiểm
    with st.expander("⚠️ Biến chứng nguy hiểm"):
        st.markdown("""
        ### 🚨 Áp xe gan amip:
        - Amip chui qua thành ruột → Gan
        - Tạo "nang mủ" trong gan
        - **Dấu hiệu:**
          - Sốt cao 39-40°C
          - Đau bụng phải (dưới sườn)
          - Gan to, ấn đau
        - **Xử trí:** Kháng sinh đặc biệt + Dẫn lưu
        
        ### 🚨 Thủng đại tràng:
        - Amip ăn lỗ trong đại tràng
        - Phân rò ra ổ bụng → Nhiễm trùng
        - **Nguy hiểm:** Viêm phúc mạc, sốc nhiễm trùng
        - **Xử trí:** Mổ gấp!
        
        ### 🚨 Amip vào máu:
        - Lây lan khắp cơ thể
        - Vào não → Áp xe não
        - Vào phổi → Áp xe phổi
        - **Tỷ lệ tử vong:** 50-90%
        
        **→ Cần điều trị sớm!**
    """)
    
    # Điều trị
    with st.expander("💊 Thuốc điều trị (theo chỉ định bác sĩ)"):
        st.markdown("""
        ### ✅ Thuốc điều trị lỵ trong ruột:
        
        **1. Metronidazole (Flagyl) - TỐT NHẤT:**
        - Liều: 750mg x 3 lần/ngày x 5-10 ngày
        - Diệt amip: Hiệu quả 95%
        - Cho: Người lớn
        - Giá: ~30.000 VNĐ/viên
        - **Lưu ý:** Không uống rượu bia!
        
        **2. Tinidazole (Fasigyn):**
        - Liều: 2g/ngày x 3 ngày
        - Hiệu quả: 95%
        - Ít tác dụng phụ hơn Flagyl
        - Giá: ~100.000 VNĐ/viên
        
        **3. Paromomycin (Humatin):**
        - Liều: 25-30mg/kg/ngày x 7-10 ngày
        - Cho: Trẻ em, bà bầu
        - Hiệu quả: 85-90%
        - Giá: ~80.000 VNĐ
        
        ### 🔄 Điều trị áp xe gan:
        - **Metronidazole:** 750mg x 3 lần/ngày x 10 ngày
        - **Dẫn lưu:** Nếu nang to >5cm
        - **Phẫu thuật:** Nếu nang vỡ
        - **Theo dõi:** Siêu âm sau 1-2 tuần
        
        ### ⚠️ Lưu ý khi điều trị:
        1. **Uống đủ liều:** Không bỏ giữa chừng
        2. **Bù nước:** Uống nhiều Oresol
        3. **Tránh rượu bia:** Khi uống Metronidazole
        4. **Tái khám:** Sau 1-2 tuần
    """)
    
    # Phòng ngừa
    with st.expander("🛡️ Phòng ngừa - RẤT QUAN TRỌNG!"):
        st.markdown("""
        ### ✅ Quy tắc VÀNG:
        
        **1. 💧 Uống nước sạch:**
        - Đun sôi 100°C để nguội
        - Không uống nước ao, hồ
        - Nước đá phải rõ nguồn gốc
        - Lọc nước qua hệ thống
        
        **2. 🥬 Rửa rau kỹ:**
        - Ngâm nước muối 15 phút
        - Rửa dưới vòi nước chảy 3-4 lần
        - Nấu chín rau (nếu có thể)
        
        **3. 🍽️ Vệ sinh thức ăn:**
        - Che đậy thức ăn
        - Không để lâu, không để ruồi bọ
        - Rửa tay trước ăn, sau đi vệ sinh
        
        **4. 🚽 Vệ sinh phân:**
        - Xử lý phân đúng cách
        - Không dùng phân tươi bón rau
        - Phân phải ủ hoai 3-6 tháng
        
        **5. 🧼 Vệ sinh tay:**
        - Rửa với xà phòng 20 giây
        - Trước ăn, sau đi vệ sinh
        - Cắt móng tay ngắn
    """)
    
    # Phân biệt lỵ amip và lỵ trực khuẩn
    with st.expander("🤔 Lỵ Amip khác Lỵ Trực Khuẩn thế nào?"):
        st.markdown("""
        | Đặc điểm | Lỵ AMIP | Lỵ TRỰC KHUẨN |
        |----------|---------|---------------|
        | **Nguyên nhân** | Đơn bào | Vi khuẩn |
        | **Khởi phát** | Chậm (1-2 tuần) | Nhanh (1-3 ngày) |
        | **Số lần đi ngoài** | 10-30 lần/ngày | 20-40 lần/ngày |
        | **Phân** | Máu + mủ | Máu ít, nước nhiều |
        | **Sốt** | Nhẹ (<38°C) | Cao (38-40°C) |
        | **Đau bụng** | Quặn dữ dội | Quặn nhẹ |
        | **Biến chứng** | Áp xe gan | Ít biến chứng |
        
        💡 **Điều trị khác nhau:** Cần phân biệt để dùng đúng thuốc!
    """)
    
    # FAQ
    st.markdown("---")
    st.subheader("❓ Câu hỏi thường gặp")
    
    with st.expander("🤔 Tôi tiêu chảy ra máu, có phải lỵ amip không?"):
        st.markdown("""
        **CÓ THỂ, nhưng cần xét nghiệm:**
        
        **Dấu hiệu lỵ amip:**
        - Tiêu chảy nhiều lần
        - Phân: Máu + mủ nhầy (giống dưa chuột cắt ngang)
        - Đau bụng quặn dữ dội
        - Sốt nhẹ hoặc không sốt
        
        **Làm gì:**
        1. Khám bác sĩ → Xét nghiệm phân
        2. Soi phân tìm amip
        3. Nếu có: Uống Metronidazole
        4. Bù nước bằng Oresol
        """)
    
    with st.expander("🤔 Bị lỵ amip có nguy hiểm không?"):
        st.markdown("""
        **CÓ THỂ RẤT NGUY HIỂM nếu không điều trị:**
        
        **Biến chứng nặng:**
        - Áp xe gan: Nang mủ trong gan
        - Thủng đại tràng: Mổ gấp!
        - Amip vào máu: Tỷ lệ tử vong 50-90%
        
        **Triệu chứng nguy hiểm:**
        - Sốt cao + Đau bụng phải → Áp xe gan
        - Đau bụng dữ dội + Sốt → Thủng ruột
        - Sốt cao + Hôn mê → Nhiễm trùng nặng
        
        **→ ĐIỀU TRỊ NGAY khi có triệu chứng!**
        """)
    
    with st.expander("🤔 Tại sao phải uống Metronidazole 5-10 ngày?"):
        st.markdown("""
        **Vì amip có 2 dạng:**
        1. **Dạng hoạt động:** Gây lỵ, dễ diệt
        2. **Dạng kén:** Nằm im trong ruột, khó diệt
        
        **Metronidazole:**
        - Diệt dạng hoạt động: 3-5 ngày
        - Diệt dạng kén: 7-10 ngày
        - Uống ít ngày → Dạng kén còn → Bị lại
        
        **→ Uống đủ liều để diệt hết!**
        """)
    
    # Cảnh báo cuối
    st.markdown("""
    ---
    <div class="warning-box">
        <b>⚠️ QUAN TRỌNG:</b><br>
        • Lỵ amip có thể gây ÁP XE GAN, thủng ruột nếu không điều trị!<br>
        • Bù nước bằng Oresol khi tiêu chảy<br>
        • Uống nước sạch, rửa tay thường xuyên<br>
        • Thông tin trên chỉ mang tính chất <b>THAM KHẢO</b><br>
        • <b>KHÔNG THAY THẾ</b> tư vấn của bác sĩ<br>
        • Sốt cao + Đau bụng: <b>KHÁM BÁC SĨ NGAY</b>
    </div>
    """, unsafe_allow_html=True)

