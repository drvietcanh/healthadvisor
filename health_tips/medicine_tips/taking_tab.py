"""
Taking Tab - Cách uống thuốc
"""

import streamlit as st


def render_taking_tab():
    """Tab Cách uống thuốc"""
    st.markdown("""
    ### 💧 Cách uống thuốc đúng:
    
    **⏰ Uống đúng giờ:**
    - "Trước ăn 30 phút" → Uống lúc đói
    - "Sau ăn" → Uống sau khi ăn no
    - "Trong bữa ăn" → Uống giữa bữa
    - "Cách nhau 4-6 giờ" → Không uống liền nhau
    
    **💊 Cách nuốt viên:**
    - Uống với nước lọc (1 cốc to)
    - Không bẻ viên (trừ khi bác sĩ cho phép)
    - Không nhai viên bao phim (sẽ mất tác dụng)
    
    **🚫 Không uống với:**
    - ⛔ Rượu, bia (gây tương tác nguy hiểm)
    - ⛔ Nước chè, cà phê (một số thuốc)
    - ⛔ Nước nóng (phá hủy thuốc)
    - ⛔ Sữa (một số thuốc như kháng sinh)
    
    **✅ Nên uống với:**
    - Nước lọc (tốt nhất)
    - Nước ấm (một số thuốc Đông y)
    """)
    
    st.success("""
    💡 **Mẹo cho trẻ em:**
    - Viên nhỏ → Nghiền nhỏ, pha với chút nước đường
    - Siro → Dùng ống tiêm, bơm vào má (trẻ dễ nuốt)
    - Không ép trẻ → Dễ nôn, mất thuốc
    """)

