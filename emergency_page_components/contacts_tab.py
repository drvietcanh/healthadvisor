"""
Tab 3: Danh Bạ Cá Nhân
Quản lý danh bạ cá nhân (con cháu, bác sĩ, bệnh viện...)
"""

import streamlit as st
from emergency_contacts import (
    add_personal_contact,
    delete_personal_contact,
    get_all_personal_contacts
)

def render_contacts_tab():
    """Render tab Danh bạ Cá nhân"""
    st.header("👥 Danh bạ Cá nhân")
    
    st.info("💡 **Thêm số điện thoại của con cháu, bác sĩ riêng, bệnh viện gần nhà**")
    
    # Form thêm contact
    with st.expander("➕ Thêm số mới", expanded=False):
        with st.form("add_contact_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            
            with col1:
                name = st.text_input("👤 Tên *", placeholder="VD: Con trai Minh")
                phone = st.text_input("📱 Số điện thoại *", placeholder="VD: 0912345678")
            
            with col2:
                relationship = st.selectbox("👨‍👩‍👦 Mối quan hệ", [
                    "Con",
                    "Cháu",
                    "Vợ/Chồng",
                    "Anh/Chị/Em",
                    "Bác sĩ riêng",
                    "Bệnh viện",
                    "Hàng xóm",
                    "Bạn bè",
                    "Khác"
                ])
                notes = st.text_input("📝 Ghi chú", placeholder="VD: Gọi khi cần thiết")
            
            submitted = st.form_submit_button("✅ Thêm vào danh bạ", use_container_width=True)
            
            if submitted:
                if not name or not phone:
                    st.error("⚠️ Vui lòng nhập đầy đủ tên và số điện thoại!")
                else:
                    if add_personal_contact(name, phone, relationship, notes):
                        st.success(f"✅ Đã thêm **{name}** vào danh bạ!")
                        st.rerun()
    
    st.divider()
    
    # Hiển thị danh sách
    contacts = get_all_personal_contacts()
    
    if not contacts:
        st.info("📝 Chưa có số điện thoại nào. Hãy thêm số đầu tiên!")
    else:
        st.subheader(f"📋 Danh sách ({len(contacts)} số)")
        
        for contact in contacts:
            with st.container():
                col1, col2, col3 = st.columns([3, 2, 1])
                
                with col1:
                    st.markdown(f"### 👤 {contact['name']}")
                    # Tạo link gọi điện
                    st.markdown(f"""
                    <a href="tel:{contact['phone']}" style="text-decoration: none;">
                        <div style="background: linear-gradient(135deg, #00c853 0%, #00a043 100%); 
                                    color: white; padding: 15px; border-radius: 10px; 
                                    font-size: 24px; font-weight: bold; text-align: center;
                                    box-shadow: 0 4px 10px rgba(0,200,83,0.3);">
                            📱 {contact['phone']}<br>
                            <span style="font-size: 16px;">👆 BẤM ĐỂ GỌI</span>
                        </div>
                    </a>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f"**Quan hệ:** {contact['relationship']}")
                    if contact.get('notes'):
                        st.caption(f"💡 {contact['notes']}")
                
                with col3:
                    if st.button("🗑️ Xóa", key=f"del_{contact['id']}"):
                        if delete_personal_contact(contact['id']):
                            st.success("Đã xóa!")
                            st.rerun()
                
                st.divider()

