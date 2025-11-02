"""
Storage Tab - Bảo quản thuốc
"""

import streamlit as st


def render_storage_tab():
    """Tab Bảo quản thuốc"""
    st.markdown("""
    ### 🏠 Bảo quản thuốc đúng cách:
    
    **✅ Nơi khô ráo, thoáng mát:**
    - Tránh phòng tắm (ẩm ướt)
    - Tránh bếp (nóng)
    - Tránh ánh nắng trực tiếp
    
    **❄️ Thuốc cần bảo quản lạnh:**
    - Insulin → Tủ lạnh (2-8°C), không đông
    - Một số kháng sinh → Kiểm tra nhãn
    - Vắc-xin → Tủ lạnh bảo quản
    
    **📦 Giữ nguyên bao bì:**
    - Giữ hộp, tờ hướng dẫn
    - Không bỏ thuốc ra túi nilon
    - Ghi rõ ngày mở nếu dùng lâu
    
    **⏰ Kiểm tra hạn sử dụng:**
    - Thuốc hết hạn → Vứt đi
    - Thuốc bị đổi màu, mốc → Không dùng
    - Thuốc quá 6 tháng mở → Hỏi bác sĩ
    """)
    
    st.info("""
    💡 **Mẹo nhớ:**
    - Thuốc đắt tiền (Insulin, thuốc tim mạch) → Cất cẩn thận, tránh ánh sáng
    - Siro trẻ em → Sau khi mở, dùng trong 1-3 tháng (xem nhãn)
    - Thuốc nhỏ mắt → Sau mở dùng trong 1 tháng
    """)

