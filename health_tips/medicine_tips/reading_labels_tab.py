"""
Reading Labels Tab - Đọc nhãn thuốc
"""

import streamlit as st


def render_reading_labels_tab():
    """Tab Đọc nhãn thuốc"""
    st.markdown("""
    ### 📋 Đọc nhãn thuốc đúng cách:
    
    **🏷️ Thông tin quan trọng trên nhãn thuốc:**
    
    **1. Tên thuốc:**
    - Tên thương mại (ví dụ: Panadol) + Tên hoạt chất (Paracetamol)
    - Kiểm tra xem có đúng thuốc cần mua không
    
    **2. Liều lượng:**
    - Ví dụ: "500mg" → Số mg trong 1 viên
    - "10ml" → Số ml trong 1 lần uống
    - Đọc kỹ để không nhầm lẫn
    
    **3. Cách dùng:**
    - "Ngày 2 lần, mỗi lần 1 viên" → 2 lần/ngày
    - "Uống sau ăn" → Sau khi ăn no
    - "Uống trước ăn 30 phút" → Lúc đói
    - "Uống với nhiều nước" → 1 cốc nước to
    
    **4. Hạn sử dụng:**
    - "HSD: 31/12/2025" → Hết hạn ngày 31/12/2025
    - Sau ngày này → KHÔNG dùng nữa!
    
    **5. Bảo quản:**
    - "Bảo quản ở nhiệt độ phòng" → Không cần tủ lạnh
    - "Bảo quản ở 2-8°C" → Tủ lạnh (không đông)
    - "Tránh ánh sáng" → Để trong hộp, không để ngoài
    
    **⚠️ Cảnh báo trên nhãn:**
    - "Không dùng quá 3-5 ngày" → Dùng đúng thời gian
    - "Có thể gây buồn ngủ" → Không lái xe sau khi uống
    - "Không dùng với rượu bia" → TUYỆT ĐỐI tuân thủ
    - "Không dùng khi mang thai" → Hỏi bác sĩ
    
    **✅ Kiểm tra trước khi uống:**
    - ✅ Thuốc còn hạn không?
    - ✅ Thuốc đúng tên, đúng liều không?
    - ✅ Đã đọc hướng dẫn chưa?
    - ✅ Có tác dụng phụ gì không?
    """)
    
    st.info("""
    💡 **Mẹo nhớ:**
    
    - **Không hiểu** → Hỏi dược sĩ hoặc bác sĩ
    - **Thuốc cũ** → Kiểm tra hạn sử dụng
    - **Đổi nhãn** → Kiểm tra tên hoạt chất (có thể cùng thuốc, khác thương hiệu)
    - **Thuốc của người khác** → KHÔNG dùng! Mỗi người có liều khác nhau
    """)

