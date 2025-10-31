"""
Tab 2: Hướng Dẫn Sơ Cứu
Hiển thị hướng dẫn sơ cứu theo từng tình huống
"""

import streamlit as st
from emergency_contacts import FIRST_AID_GUIDES

def render_first_aid_tab():
    """Render tab Hướng dẫn Sơ cứu"""
    st.header("🏥 Hướng dẫn Sơ cứu Nhanh")
    
    st.info("""
    💡 **Lưu ý:** Đây chỉ là hướng dẫn sơ cứu cơ bản. 
    **LUÔN GỌI 115** trong trường hợp nghiêm trọng!
    """)
    
    # Chọn tình huống
    situations = {
        "heart_attack": "❤️ Đau tim cấp",
        "stroke": "🧠 Đột quỵ (F.A.S.T)",
        "choking_child": "👶 Trẻ em hóc dị vật",
        "burns": "🔥 Bỏng nhiệt/Nước sôi",
        "hypoglycemia": "🍬 Hạ đường huyết",
        "poisoning": "☠️ Ngộ độc",
        "bleeding": "🩸 Chảy máu",
        "drowning": "🌊 Đuối nước",
        "electric_shock": "⚡ Điện giật",
        "spinal_injury": "🦴 Chấn thương cột sống cổ",
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
        
        if 'risk_situations' in guide:
            st.warning(f"### {guide['risk_situations']['title']}")
            for item in guide['risk_situations']['items']:
                st.markdown(f"- {item}")
        
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

