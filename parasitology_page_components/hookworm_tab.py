"""
Giun Móc (Hookworm) Tab
"""
import streamlit as st

def render_hookworm_tab():
    """Render tab Giun Móc"""
    st.header("🪱 Giun Móc - Bệnh gây thiếu máu trầm trọng")
    
    st.markdown("""
    <div class="info-box">
        <b>💡 Hiểu đơn giản:</b><br>
        Giun móc sống trong ruột, bám vào thành ruột và hút máu. 
        Hậu quả: Thiếu máu nặng, người xanh xao, mệt mỏi.
    </div>
    """, unsafe_allow_html=True)
    
    # Nguyên nhân và con đường lây
    with st.expander("🔍 Nguyên nhân & Con đường lây bệnh", expanded=True):
        st.markdown("""
        ### 🦠 Nguyên nhân:
        - **Giun móc (Ancylostoma, Necator):** Dài 1-1.5cm, màu đỏ hồng
        - Có "răng" hoặc "móc" bám vào ruột non, hút máu người
        - Phổ biến ở vùng nhiệt đới: VN, Lào, Campuchia
        
        ### 🗺️ Con đường lây bệnh:
        1. **Qua da (80%):**
           - Đi chân đất trên đất dơ
           - Ấu trùng giun xuyên qua da chân → vào máu
           - Trẻ em nông thôn hay bị nhất
           
        2. **Qua miệng (20%):**
           - Ăn rau sống có trứng giun
           - Uống nước ao, hồ bẩn
    """)
    
    # Triệu chứng
    with st.expander("⚕️ Triệu chứng nhận biết"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🟡 Triệu chứng ban đầu:
            - **Ngứa chân:** Da ửng đỏ, ngứa như kiến cắn
            - **Ho, khó thở:** Ấu trùng qua phổi
            - **Đau bụng nhẹ:** Khó tiêu
            
            ### 🔴 Thiếu máu (sau vài tháng):
            - **Mệt mỏi:** Người không muốn làm gì
            - **Chóng mặt:** Hoa mắt khi đứng dậy
            - **Xanh xao:** Mặt trắng bệch, thiếu máu
            - **Thở gấp:** Leo cầu thang đã mệt
            """)
        
        with col2:
            st.markdown("""
            ### 🚨 Thiếu máu nặng:
            - **Suy tim:** Tim đập nhanh, phù chân
            - **Phù:** Mi mắt sưng, chân sưng
            - **Trẻ chậm lớn:** Thấp còi, suy dinh dưỡng
            - **Thèm ăn đất:** Dấu hiệu thiếu kẽm do giun
    """)
    
    # Biến chứng nguy hiểm
    with st.expander("⚠️ Biến chứng nguy hiểm"):
        st.markdown("""
        ### 🚨 Thiếu máu nặng:
        - **Giun hút >50ml máu/ngày** = Mất máu liên tục
        - **Hậu quả:** 
          - Xanh xao, mệt mỏi suốt ngày
          - Không học được, không làm được việc
          - Trẻ chậm phát triển, nhỏ con
        - **Xử trí:** Truyền máu + Tẩy giun ngay
        
        ### 🚨 Suy tim do thiếu máu:
        - Tim phải làm việc quá sức khi thiếu máu
        - Phù chân, khó thở
        - **Xử trí:** KHÁM BÁC SĨ NGAY!
    """)
    
    # Điều trị
    with st.expander("💊 Thuốc tẩy giun (theo chỉ định bác sĩ)"):
        st.markdown("""
        ### ✅ Thuốc điều trị:
        
        **1. Albendazole (Zentel) - TỐT NHẤT:**
        - Liều: 1 viên 400mg x 2 lần/ngày x 3 ngày
        - Diệt: 95% giun móc
        - Giá: ~25.000 VNĐ/viên
        
        **2. Mebendazole (Vermox):**
        - Liều: 1 viên 100mg x 2 lần/ngày x 3 ngày
        - Diệt: 80% giun móc
        - Giá: ~20.000 VNĐ/hộp
        
        **3. Pyran tel (Combantrin):**
        - Liều: 20mg/kg cân nặng x 3 ngày
        - Cho: Trẻ em
        - Giá: ~30.000 VNĐ
        
        ### 💉 Điều trị thiếu máu:
        **1. Uống sắt:**
        - Ferrous fumarate 325mg, 1 viên/ngày
        - Uống: Trước ăn, với nước cam (dễ hấp thu)
        - Uống: 2-3 tháng để bù máu
        
        **2. Truyền máu (thiếu máu nặng):**
        - Khi Hb <7g/dL → Truyền máu
        - Sau đó mới tẩy giun
    """)
    
    # Phòng ngừa
    with st.expander("🛡️ Phòng ngừa quan trọng"):
        st.markdown("""
        ### ✅ Quy tắc VÀNG:
        
        **1. 👟 Đi giày dép:**
        - Luôn đi giày/dép khi ra ngoài
        - Đặc biệt: Vùng nông thôn, rừng núi
        - Trẻ em bắt buộc đi giày đến trường
        
        **2. 🚽 Vệ sinh sạch sẽ:**
        - Đi vệ sinh đúng nơi
        - Không thả rông trẻ em
        - Phân phải xử lý (ủ hoai 3 tháng)
        
        **3. 🥬 Ăn chín uống sôi:**
        - Rửa rau kỹ, nấu chín khi có thể
        - Không uống nước ao, hồ
        - Rửa tay trước ăn, sau đi vệ sinh
        
        **4. 🔁 Tẩy giun định kỳ:**
        - Trẻ em: 6 tháng 1 lần
        - Người lớn: 12 tháng 1 lần
        - Cả nhà cùng tẩy
    """)
    
    # Khác biệt với giun đũa
    with st.expander("🤔 Giun Móc khác Giun Đũa thế nào?"):
        st.markdown("""
        | Đặc điểm | Giun Đũa | Giun Móc |
        |----------|----------|----------|
        | **Kích thước** | 15-35cm (giun lớn) | 1-1.5cm (giun nhỏ) |
        | **Màu sắc** | Hồng trắng | Đỏ hồng |
        | **Cách gây bệnh** | Ăn thức ăn | HÚT MÁU |
        | **Triệu chứng chính** | Đau bụng | THIẾU MÁU (xanh xao) |
        | **Lây qua** | Miệng (chủ yếu) | DA + MIỆNG |
        | **Nguy hiểm** | Tắc ruột | Thiếu máu nặng |
        
        💡 **Nhớ:** Giun móc → Thiếu máu, xanh xao. Giun đũa → Đau bụng, nôn.
    """)
    
    # FAQ
    st.markdown("---")
    st.subheader("❓ Câu hỏi thường gặp")
    
    with st.expander("🤔 Tại sao giun móc lại nguy hiểm hơn giun đũa?"):
        st.markdown("""
        **Giun Móc hút máu → Thiếu máu liên tục:**
        - Mỗi giun hút 0.2-0.5ml máu/ngày
        - Người có 50 giun = Mất 10-25ml máu/ngày
        - 1 tháng = Mất 300-750ml máu (vô cùng nhiều!)
        
        **Hậu quả:** Xanh xao, mệt mỏi, trẻ chậm lớn, học kém.
        
        → Cần tẩy giun + uống sắt ngay!
        """)
    
    with st.expander("🤔 Tôi đi chân đất có bị giun móc không?"):
        st.markdown("""
        **CÓ NGUY CƠ CAO** nếu:
        - Đi trên đất dơ (có phân người/chó)
        - Vùng nông thôn, rừng núi VN
        - Không rửa chân ngay sau khi về
        
        **Giải pháp:**
        1. Luôn đi giày/dép khi ra ngoài
        2. Rửa chân sạch khi về nhà
        3. Tẩy giun định kỳ 6 tháng/lần
        """)
    
    with st.expander("🤔 Tôi xanh xao, mệt mỏi, có phải thiếu máu do giun?"):
        st.markdown("""
        **Có thể là** nếu có đủ các dấu hiệu:
        - Xanh xao mặt
        - Mệt mỏi, chóng mặt
        - Đi chân đất thường xuyên
        - Sống vùng nông thôn
        
        **Làm gì:**
        1. Khám bác sĩ → Xét nghiệm máu (Hb)
        2. Xét nghiệm phân → Tìm trứng giun
        3. Nếu có giun: Tẩy giun + Uống sắt
        4. Nếu Hb <7g/dL: Truyền máu
        """)
    
    # Cảnh báo cuối
    st.markdown("""
    ---
    <div class="warning-box">
        <b>⚠️ QUAN TRỌNG:</b><br>
        • Giun Móc gây thiếu máu NẶNG - Cần điều trị sớm!<br>
        • Thông tin trên chỉ mang tính chất <b>THAM KHẢO</b><br>
        • <b>KHÔNG THAY THẾ</b> tư vấn của bác sĩ<br>
        • Với thiếu máu nặng: <b>KHÁM BÁC SĨ NGAY</b>
    </div>
    """, unsafe_allow_html=True)

