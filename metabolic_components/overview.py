"""
Tab Tổng Quan - Hội Chứng Chuyển Hóa
"""
import streamlit as st


def render_overview_tab():
    """Render tab tổng quan về Hội chứng Chuyển hóa"""
    
    st.header("📊 Hội Chứng Chuyển Hóa (Metabolic Syndrome)")
    
    # Giới thiệu
    st.info("""
    **Hội chứng Chuyển hóa** là cụm 5 bệnh lý liên quan chặt chẽ, có chung gốc rễ là **BÉO PHÌ**.
    
    Nếu có ≥3 trong 5 yếu tố sau, bạn có Hội chứng Chuyển hóa:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🎯 5 Thành Phần Chính:
        
        1. **⚖️ Béo bụng (Béo phì trung tâm)**
           - Nam: Vòng eo ≥ 90 cm
           - Nữ: Vòng eo ≥ 80 cm
        
        2. **🩸 Đường huyết cao**
           - Đói ≥ 5.6 mmol/L (100 mg/dL)
           - Hoặc đang điều trị tiểu đường
        
        3. **💉 Huyết áp cao**
           - ≥ 130/85 mmHg
           - Hoặc đang điều trị huyết áp
        
        4. **🧪 Triglyceride cao**
           - ≥ 1.7 mmol/L (150 mg/dL)
        
        5. **💙 HDL-C thấp (cholesterol tốt)**
           - Nam: < 1.0 mmol/L (40 mg/dL)
           - Nữ: < 1.3 mmol/L (50 mg/dL)
        """)
    
    with col2:
        st.markdown("""
        ### ⚠️ Tại Sao Nguy Hiểm?
        
        **Tăng nguy cơ:**
        - 🫀 Bệnh tim mạch: **3 lần**
        - 💔 Đột quỵ: **2-3 lần**
        - 🩸 Tiểu đường type 2: **5 lần**
        - 🫘 Bệnh thận mãn: **2 lần**
        - 🎗️ Một số loại ung thư
        
        ### ✅ Tin Tốt: CÓ THỂ ĐẢO NGƯỢC!
        
        - Giảm 5-10% cân nặng
        - Ăn uống lành mạnh
        - Vận động 150 phút/tuần
        - Kiểm soát stress
        - Ngủ đủ giấc
        
        → **Có thể đảo ngược hoàn toàn!**
        """)
    
    # Sơ đồ mối liên hệ
    st.markdown("---")
    st.subheader("🔗 Mối Liên Hệ Giữa Các Bệnh")
    
    st.markdown("""
    ```
    ┌─────────────────────────────────┐
    │     ⚖️ BÉO PHÌ (Gốc rễ)         │
    └────────────┬────────────────────┘
                 │
         ┌───────┼───────┐
         ▼       ▼       ▼
    ┌─────┐ ┌─────┐ ┌─────┐
    │🩸ĐTĐ│ │💉HA │ │🧪Lipid│
    └──┬──┘ └──┬──┘ └──┬──┘
       └───────┼───────┘
               ▼
         ┌─────────┐
         │ ❤️ Tim   │
         │  Mạch   │
         └─────────┘
               │
         ┌─────┼─────┐
         ▼     ▼     ▼
     Nhồi máu Đột quỵ Suy tim
    ```
    
    **Vòng luẩn quẩn:**
    - Béo phì → Kháng insulin → Tiểu đường
    - Béo phì → Tăng huyết áp → Tim mạch
    - Tiểu đường + Cao HA → Đột quỵ, Suy thận
    
    **PHÁ VỠ VÒNG LẶP:** Giảm cân là chìa khóa! ✨
    """)
    
    # Statistics VN
    st.markdown("---")
    st.subheader("📈 Thống Kê Việt Nam")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Béo phì", "25%", "↑38%/năm", help="Tốc độ tăng nhanh nhất ĐNA")
    with col2:
        st.metric("Tiểu đường", "6.5%", "↑2x trong 10 năm")
    with col3:
        st.metric("Cao huyết áp", "25-30%", "↑ theo tuổi")
    with col4:
        st.metric("Lipid máu cao", "~30%", "Đo ở người >40 tuổi")

