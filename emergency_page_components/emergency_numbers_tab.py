"""
Tab 1: Số Điện Thoại Cấp Cứu
Hiển thị số 115 và các số khẩn cấp khác của Việt Nam
"""

import streamlit as st
from emergency_contacts import VIETNAM_EMERGENCY_NUMBERS

def render_emergency_numbers_tab():
    """Render tab Số Cấp Cứu"""
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
    
    other_numbers = ["113", "114-chay", "114"]
    
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

