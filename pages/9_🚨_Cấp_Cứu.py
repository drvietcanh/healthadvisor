"""
Trang Cấp Cứu - Số điện thoại khẩn cấp và Hướng dẫn sơ cứu
Thiết kế đặc biệt cho người già: Font to, nút lớn, màu rõ ràng
"""
import streamlit as st
import sys
import os

# Thêm thư mục gốc vào path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from emergency_contacts import (
    VIETNAM_EMERGENCY_NUMBERS,
    FIRST_AID_GUIDES,
    add_personal_contact,
    delete_personal_contact,
    get_all_personal_contacts,
    save_medical_info,
    get_medical_info
)
from core.ui_config import get_custom_css

st.set_page_config(
    page_title="Số Cấp Cứu",
    page_icon="🚨",
    layout="wide"
)

# Áp dụng Dark Mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)

# Custom CSS cho trang này - NÚT LỚN HƠN, FONT LỚN HƠN
st.markdown("""
<style>
    /* Nút cấp cứu - TO VÀ RÕ */
    .emergency-button {
        padding: 30px !important;
        font-size: 32px !important;
        font-weight: bold !important;
        border-radius: 15px !important;
        margin: 10px 0 !important;
        text-align: center !important;
        cursor: pointer !important;
        border: 3px solid !important;
    }
    
    .btn-critical {
        background: linear-gradient(135deg, #ff0000 0%, #cc0000 100%) !important;
        color: white !important;
        border-color: #990000 !important;
        box-shadow: 0 8px 20px rgba(255,0,0,0.4) !important;
    }
    
    .btn-important {
        background: linear-gradient(135deg, #ff6b00 0%, #cc5500 100%) !important;
        color: white !important;
        border-color: #994400 !important;
    }
    
    .btn-info {
        background: linear-gradient(135deg, #0066ff 0%, #0052cc 100%) !important;
        color: white !important;
        border-color: #003d99 !important;
    }
    
    /* Font lớn cho người già */
    .big-text {
        font-size: 24px !important;
        line-height: 1.6 !important;
    }
    
    .huge-text {
        font-size: 36px !important;
        font-weight: bold !important;
    }
    
    /* Highlight quan trọng */
    .warning-box {
        background: #fff3cd;
        border-left: 5px solid #ff0000;
        padding: 20px;
        margin: 15px 0;
        border-radius: 5px;
        font-size: 20px !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🚨 SỐ ĐIỆN THOẠI CẤP CỨU")

st.markdown("""
<div style='background: linear-gradient(135deg, #ff4444 0%, #cc0000 100%); 
            padding: 25px; border-radius: 15px; color: white; margin-bottom: 25px;
            box-shadow: 0 8px 20px rgba(255,0,0,0.3);'>
    <h2 style='margin:0; color: white; font-size: 32px;'>⚡ KHẨN CẤP - GỌI NGAY!</h2>
    <p style='margin: 15px 0 0 0; font-size: 22px; opacity: 0.95;'>
        Mỗi giây đều quan trọng. Đừng ngần ngại gọi cấp cứu khi cần!
    </p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📞 SỐ CẤP CỨU",
    "🏥 SƠ CỨU",
    "👥 DANH BẠ",
    "📋 THÔNG TIN Y TẾ"
])

# =============== TAB 1: SỐ CẤP CỨU ===============
with tab1:
    st.header("📞 Số điện thoại cấp cứu Việt Nam")
    
    # Số 115 - Ưu tiên cao nhất
    emergency_115 = VIETNAM_EMERGENCY_NUMBERS["115"]
    st.markdown(f"""
    <a href="tel:115" style="text-decoration: none;">
        <div class='emergency-button btn-critical'>
            {emergency_115['icon']} <span style='font-size:48px;'>115</span><br>
            {emergency_115['name']}<br>
            <span style='font-size:20px;'>{emergency_115['description']}</span><br>
            <span style='font-size:18px; opacity:0.9;'>👆 BẤM ĐỂ GỌI NGAY</span>
        </div>
    </a>
    """, unsafe_allow_html=True)
    
    with st.expander("📋 Khi nào gọi 115?", expanded=False):
        st.markdown("### ⚡ GỌI 115 KHI:")
        for item in emergency_115['when_to_call']:
            st.markdown(f"- **{item}**")
        st.error("💡 **GỌI NGAY - Đừng chờ!** Tốt hơn gọi nhầm còn hơn không gọi!")
    
    st.divider()
    
    # Các số khác
    st.subheader("📱 Số điện thoại khẩn cấp khác")
    
    cols = st.columns(2)
    
    other_numbers = ["113", "114-chay", "114", "1900-54-54-58"]
    
    for idx, number in enumerate(other_numbers):
        info = VIETNAM_EMERGENCY_NUMBERS[number]
        
        with cols[idx % 2]:
            color_class = "btn-important" if info['priority'] == 2 else "btn-info"
            
            # Format số điện thoại cho tel: link (bỏ dấu -)
            tel_number = number.replace('-chay', '').replace('-', '')
            display_number = number.replace('-chay', ' Chữa cháy')
            
            st.markdown(f"""
            <a href="tel:{tel_number}" style="text-decoration: none;">
                <div class='emergency-button {color_class}'>
                    {info['icon']} {display_number}<br>
                    <span style='font-size:18px;'>{info['name']}</span><br>
                    <span style='font-size:14px; opacity:0.8;'>👆 Bấm để gọi</span>
                </div>
            </a>
            """, unsafe_allow_html=True)
            
            with st.expander(f"Chi tiết {info['name']}", expanded=False):
                st.markdown(f"**📋 Mô tả:** {info['description']}")
                st.markdown("**📞 Khi nào gọi:**")
                for item in info['when_to_call']:
                    st.markdown(f"- {item}")

# =============== TAB 2: HƯỚNG DẪN SƠ CỨU ===============
with tab2:
    st.header("🏥 Hướng dẫn Sơ cứu Nhanh")
    
    st.info("""
    💡 **Lưu ý:** Đây chỉ là hướng dẫn sơ cứu cơ bản. 
    **LUÔN GỌI 115** trong trường hợp nghiêm trọng!
    """)
    
    # Chọn tình huống
    situations = {
        "heart_attack": "❤️ Đau tim cấp",
        "stroke": "🧠 Đột quỵ (F.A.S.T)",
        "hypoglycemia": "🍬 Hạ đường huyết",
        "fall": "🤕 Ngã",
        "chest_pain": "💔 Đau ngực"
    }
    
    selected = st.selectbox(
        "Chọn tình huống:",
        list(situations.keys()),
        format_func=lambda x: situations[x],
        key="first_aid_selector"
    )
    
    if selected:
        guide = FIRST_AID_GUIDES[selected]
        
        st.markdown(f"## {guide['icon']} {guide['name']}")
        
        # Dấu hiệu
        if 'signs' in guide:
            st.markdown(f"### {guide['signs']['title']}")
            for sign in guide['signs']['items']:
                st.markdown(f"- {sign}")
        
        if 'other_signs' in guide:
            st.markdown("### Các dấu hiệu khác:")
            for sign in guide['other_signs']:
                st.markdown(f"- {sign}")
        
        st.divider()
        
        # Xử lý
        if 'actions' in guide:
            st.error(f"### {guide['actions']['title']}")
            for step in guide['actions']['steps']:
                st.markdown(f"{step}")
        
        # Trường hợp nghiêm trọng
        if 'severe' in guide:
            st.markdown(f"### {guide['severe']['title']}")
            for step in guide['severe']['steps']:
                st.markdown(f"{step}")
        
        # Khi nào gọi 115
        if 'call_115' in guide:
            st.error(f"### {guide['call_115']['title']}")
            for item in guide['call_115']['items']:
                st.markdown(f"{item}")
        
        # Không được làm
        if 'dont' in guide:
            st.warning(f"### {guide['dont']['title']}")
            for item in guide['dont']['items']:
                st.markdown(f"{item}")
        
        # Phòng ngừa
        if 'prevention' in guide:
            st.success(f"### {guide['prevention']['title']}")
            for item in guide['prevention']['items']:
                st.markdown(f"{item}")
        
        # Ghi chú
        if 'note' in guide:
            st.markdown(f"""
            <div class='warning-box'>
                {guide['note']}
            </div>
            """, unsafe_allow_html=True)

# =============== TAB 3: DANH BẠ CÁ NHÂN ===============
with tab3:
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

# =============== TAB 4: THÔNG TIN Y TẾ ===============
with tab4:
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
            
            blood_type = st.selectbox(
                "🩸 Nhóm máu",
                ["Chưa biết", "O", "A", "B", "AB", "O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"],
                index=["Chưa biết", "O", "A", "B", "AB", "O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"].index(
                    med_info.get('blood_type', 'Chưa biết')
                )
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

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; padding: 20px; background: #fff3cd; border-radius: 10px; margin-top: 20px;'>
    <h3 style='color: #cc0000; margin: 0;'>⚠️ LƯU Ý QUAN TRỌNG</h3>
    <p style='font-size: 20px; margin: 10px 0; color: #333;'>
        <b>KHI NGHI NGỜ - HÃY GỌI 115!</b><br>
        Tốt hơn gọi nhầm còn hơn không gọi.<br>
        Mỗi giây đều có giá trị trong cấp cứu!
    </p>
</div>
""", unsafe_allow_html=True)

if st.button("⬅️ Quay lại trang chính", use_container_width=True):
    st.switch_page("app.py")

