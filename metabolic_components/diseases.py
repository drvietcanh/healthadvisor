"""
Tab Bệnh Liên Quan - Các bệnh do béo phì gây ra
"""
import streamlit as st
from diseases.metabolic import obesity


def render_diseases_tab():
    """Render tab các bệnh liên quan béo phì"""
    
    st.header("🔗 Các Bệnh Liên Quan Béo Phì")
    
    st.info("""
    Béo phì là **gốc rễ** của nhiều bệnh mãn tính. Dưới đây là các bệnh có trong app 
    mà bạn có thể tìm hiểu thêm.
    """)
    
    # Direct consequences
    st.subheader("⚡ Hậu Quả Trực Tiếp (Nguy cơ rất cao)")
    
    for disease_id, disease_data in obesity.RELATED_DISEASES["direct_consequences"].items():
        with st.expander(f"{disease_data['name']} - Nguy cơ: {disease_data['risk']}"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"""
                **Cơ chế:**
                
                {disease_data.get('mechanism', 'Chưa có thông tin')}
                """)
                
                if 'symptoms' in disease_data:
                    st.markdown("**Triệu chứng:**")
                    symptoms = disease_data['symptoms']
                    if isinstance(symptoms, list):
                        for symptom in symptoms:
                            st.markdown(f"• {symptom}")
                    elif isinstance(symptoms, str):
                        st.markdown(f"• {symptoms}")
            
            with col2:
                if disease_data.get('page'):
                    st.info(f"📖 Xem thêm tại trang:\n**{disease_data['page']}**")
                
                if 'prevention' in disease_data:
                    st.success(f"""
                    **Phòng ngừa:**
                    
                    {disease_data['prevention']}
                    """)
    
    # Indirect consequences
    st.markdown("---")
    st.subheader("🔄 Hậu Quả Gián Tiếp (Qua các bệnh khác)")
    
    for disease_id, disease_data in obesity.RELATED_DISEASES["indirect_consequences"].items():
        with st.expander(f"{disease_data['name']} - Nguy cơ: {disease_data['risk']}"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"""
                **Cơ chế:**
                
                {disease_data.get('mechanism', 'Chưa có thông tin')}
                """)
                
                if 'symptoms' in disease_data:
                    st.markdown("**Triệu chứng:**")
                    symptoms = disease_data['symptoms']
                    if isinstance(symptoms, list):
                        for symptom in symptoms:
                            st.markdown(f"• {symptom}")
                    elif isinstance(symptoms, str):
                        st.markdown(f"• {symptoms}")
            
            with col2:
                if disease_data.get('page'):
                    st.info(f"📖 Xem thêm tại trang:\n**{disease_data['page']}**")
                
                if 'prevention' in disease_data:
                    st.success(f"""
                    **Phòng ngừa:**
                    
                    {disease_data['prevention']}
                    """)
    
    # Other complications
    st.markdown("---")
    st.subheader("🩺 Biến Chứng Khác")
    
    for disease_id, disease_data in obesity.RELATED_DISEASES["other_complications"].items():
        with st.expander(f"{disease_data['name']} - Nguy cơ: {disease_data['risk']}"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"""
                **Cơ chế:**
                
                {disease_data.get('mechanism', 'Chưa có thông tin')}
                """)
                
                if 'symptoms' in disease_data:
                    st.markdown("**Triệu chứng:**")
                    symptoms = disease_data['symptoms']
                    if isinstance(symptoms, list):
                        for symptom in symptoms:
                            st.markdown(f"• {symptom}")
                    elif isinstance(symptoms, str):
                        st.markdown(f"• {symptoms}")
            
            with col2:
                if disease_data.get('page'):
                    st.info(f"📖 Xem thêm tại trang:\n**{disease_data['page']}**")
                
                if 'prevention' in disease_data:
                    st.success(f"""
                    **Phòng ngừa:**
                    
                    {disease_data['prevention']}
                    """)
    
    # Prevention summary
    st.markdown("---")
    st.success("""
    ### ✅ Phòng Ngừa Tất Cả Các Bệnh Trên:
    
    **1️⃣ Giảm cân:** Chỉ cần giảm 5-10% cân nặng đã giảm nguy cơ đáng kể!
    
    **2️⃣ Ăn uống:**
    - Giảm cơm, tăng rau
    - Tránh đồ chiên rán, ngọt
    - Ăn đủ protein
    
    **3️⃣ Vận động:**
    - 150 phút/tuần (30 phút x 5 ngày)
    - Đi bộ, tập nhẹ
    
    **4️⃣ Khám định kỳ:**
    - 6 tháng/lần
    - Xét nghiệm: Đường máu, lipid máu, huyết áp
    """)

