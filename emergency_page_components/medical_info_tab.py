"""
Tab 4: Thông Tin Y Tế Khẩn Cấp
Form nhập và hiển thị thông tin y tế (thuốc, dị ứng, bệnh nền...)
"""

import streamlit as st
from emergency_contacts import save_medical_info, get_medical_info

def render_medical_info_tab():
    """Render tab Thông tin Y tế"""
    st.header("📋 Thông tin Y tế Khẩn cấp")
    
    st.warning("""
    ⚠️ **Quan trọng:** Thông tin này dùng để cung cấp cho bác sĩ/nhân viên y tế khi cấp cứu.
    
    💡 **Mẹo:** In ra giấy và mang theo khi đi khám hoặc ra ngoài!
    """)
    
    # Load thông tin hiện tại
    med_info = get_medical_info()
    
    # Form nhập thông tin
    with st.form("medical_info_form"):
        st.subheader("Điền thông tin của bạn:")
        
        medications = st.text_area(
            "💊 Thuốc đang uống *",
            value=med_info.get('medications', ''),
            placeholder="VD:\n- Metformin 500mg (2 viên/ngày)\n- Amlodipine 5mg (1 viên/ngày)",
            help="Liệt kê tất cả thuốc đang dùng, cả thuốc kê đơn và không kê đơn",
            height=150
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            allergies = st.text_area(
                "🚫 Dị ứng (thuốc/thực phẩm)",
                value=med_info.get('allergies', ''),
                placeholder="VD:\n- Dị ứng Penicillin\n- Dị ứng tôm cua",
                height=100
            )
            
            blood_types = ["Chưa biết", "O", "A", "B", "AB", "O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
            current_blood_type = med_info.get('blood_type', 'Chưa biết')
            
            # Tìm index an toàn
            try:
                blood_type_index = blood_types.index(current_blood_type)
            except ValueError:
                blood_type_index = 0  # Mặc định "Chưa biết" nếu không tìm thấy
            
            blood_type = st.selectbox(
                "🩸 Nhóm máu",
                blood_types,
                index=blood_type_index
            )
        
        with col2:
            conditions = st.text_area(
                "🏥 Bệnh nền",
                value=med_info.get('conditions', ''),
                placeholder="VD:\n- Tiểu đường type 2\n- Huyết áp cao\n- Suy tim",
                height=100
            )
            
            notes = st.text_area(
                "📝 Ghi chú khác",
                value=med_info.get('notes', ''),
                placeholder="VD: Phẫu thuật tim 2020, cần theo dõi đường huyết thường xuyên",
                height=100
            )
        
        submitted = st.form_submit_button("💾 Lưu thông tin", use_container_width=True)
        
        if submitted:
            if save_medical_info(medications, allergies, conditions, blood_type, notes):
                st.success("✅ Đã lưu thông tin y tế!")
                st.balloons()
    
    st.divider()
    
    # Hiển thị thông tin để in
    if med_info.get('medications') or med_info.get('conditions'):
        st.subheader("📄 Thông tin của bạn (In ra để mang theo)")
        
        st.markdown(f"""
        ### 👤 Thông tin Y tế Khẩn cấp
        
        **📅 Cập nhật:** {med_info.get('updated_at', 'Chưa có')[:10] if med_info.get('updated_at') else 'Chưa có'}
        
        ---
        
        **💊 THUỐC ĐANG UỐNG:**
        ```
        {med_info.get('medications', 'Chưa nhập')}
        ```
        
        **🚫 DỊ ỨNG:**
        ```
        {med_info.get('allergies', 'Không có')}
        ```
        
        **🏥 BỆNH NỀN:**
        ```
        {med_info.get('conditions', 'Không có')}
        ```
        
        **🩸 NHÓM MÁU:** {med_info.get('blood_type', 'Chưa biết')}
        
        **📝 GHI CHÚ:**
        ```
        {med_info.get('notes', 'Không có')}
        ```
        
        ---
        
        **🚨 SỐ CẤP CỨU: 115**
        
        """)
        
        st.info("💡 **Cách in:** Nhấn Ctrl+P (hoặc Cmd+P trên Mac) để in trang này")

