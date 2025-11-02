"""
General Health Tips - Fever
Mẹo xử trí sốt
"""

import streamlit as st
import pandas as pd


def render_fever_tips():
    """Hiển thị mẹo xử trí sốt"""
    st.subheader("🌡️ Xử trí sốt đúng cách")
    
    st.markdown("""
    ### 📌 Khi nào cần hạ sốt?
    
    **Sốt nhẹ (37.5-38°C):**
    - 👕 Mặc quần áo thoáng, uống nhiều nước
    - ❄️ Chườm khăn ấm (KHÔNG chườm lạnh!)
    - 💊 Chưa cần uống thuốc
    
    **Sốt cao (>38.5°C):**
    - 💊 Uống paracetamol (tính liều theo cân nặng)
    - 💧 Uống nhiều nước (nước lọc, nước hoa quả)
    - 🧽 Lau người bằng khăn ấm (nước ấm, không lạnh!)
    - 👕 Mặc quần áo mỏng, thoáng
    
    ### ⚠️ Khi nào cần đi bệnh viện?
    
    **Gọi 115 hoặc đi viện NGAY nếu:**
    - 🔥 Sốt > 40°C
    - 😰 Sốt kèm co giật
    - 😴 Li bì, khó đánh thức
    - 🤮 Nôn nhiều, không uống được nước
    - 💨 Khó thở, thở nhanh
    - 🩸 Có ban đỏ trên da
    
    **Trẻ em sốt cần đi khám nếu:**
    - < 3 tháng tuổi: Sốt > 38°C → Khám ngay
    - 3-6 tháng: Sốt > 38.5°C → Khám trong 24h
    - > 6 tháng: Sốt > 3 ngày không hạ → Khám bác sĩ
    """)
    
    # Bảng nhiệt độ
    st.markdown("### 📊 Nhiệt độ cơ thể bình thường:")
    
    temp_data = {
        "Vị trí đo": ["Nách", "Miệng", "Hậu môn", "Tai"],
        "Nhiệt độ bình thường": ["36.5-37°C", "37-37.5°C", "37.5-38°C", "36.5-37.5°C"],
        "Lưu ý": [
            "Phổ biến nhất, cộng thêm 0.5°C so với nhiệt độ thực",
            "Cộng thêm 0.3°C",
            "Chính xác nhất (trẻ nhỏ)",
            "Nhanh, tiện (trẻ lớn)"
        ]
    }
    
    df = pd.DataFrame(temp_data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.info("""
    💡 **Mẹo đo nhiệt độ:**
    - Đo ở nách: Giữ nhiệt kế 5-10 phút
    - Nếu đo nách được 37.5°C → Nhiệt độ thực ≈ 38°C (đã cộng thêm)
    - Trẻ nhỏ: Nên đo ở hậu môn (chính xác nhất)
    - Nhiệt kế điện tử: Đọc kỹ hướng dẫn, đặt đúng vị trí
    """)

