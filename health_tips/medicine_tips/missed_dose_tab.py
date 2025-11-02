"""
Missed Dose Tab - Quên uống thuốc
"""

import streamlit as st
import pandas as pd


def render_missed_dose_tab():
    """Tab Quên uống thuốc"""
    st.markdown("""
    ### ⏰ Quên uống thuốc - Xử trí thế nào?
    
    **🕐 Quên thuốc - Nhớ lại trong vòng 1-2 giờ:**
    - ✅ **Uống ngay** (nếu chưa đến lần uống tiếp theo)
    - ✅ Uống bù, sau đó uống lần tiếp theo **đúng giờ**
    - ✅ Ví dụ: Quên 8h sáng, nhớ lúc 9h → Uống ngay, 8h tối uống đúng giờ
    
    **⏰ Quên thuốc - Gần đến lần uống tiếp (còn 2-3 giờ):**
    - ✅ **Bỏ qua lần quên**, đợi đến lần uống tiếp theo
    - ❌ **KHÔNG uống gấp đôi liều!** → Quá liều, nguy hiểm
    - ✅ Ví dụ: Quên 8h sáng, nhớ lúc 6h chiều (gần 8h tối) → Bỏ qua, uống 8h tối bình thường
    
    **💊 Thuốc uống 1 lần/ngày:**
    - Quên → Uống ngay khi nhớ ra
    - Nếu gần đến lần uống hôm sau → Bỏ qua, đợi lần sau
    - **KHÔNG uống 2 viên cùng lúc!**
    
    **💊 Thuốc uống nhiều lần/ngày (2-3 lần):**
    - Quên lần 1 → Uống ngay nếu còn cách lần 2 > 2 giờ
    - Gần đến lần 2 → Bỏ qua lần 1, uống đúng giờ lần 2
    
    **📊 Bảng xử trí quên thuốc theo loại:**
    """)
    
    forgot_med_data = {
        "Loại thuốc": [
            "Thuốc huyết áp (1 lần/ngày)",
            "Thuốc tiểu đường (Metformin)",
            "Kháng sinh (2-3 lần/ngày)",
            "Thuốc tim mạch (Aspirin)",
            "Thuốc kháng đông"
        ],
        "Quên < 2 giờ": [
            "Uống ngay",
            "Uống ngay (trước bữa ăn)",
            "Uống ngay, tiếp tục đúng giờ",
            "Uống ngay",
            "Uống ngay, hỏi bác sĩ"
        ],
        "Quên > 2 giờ": [
            "Bỏ qua, uống lần sau đúng giờ",
            "Bỏ qua, uống trước bữa ăn tiếp",
            "Bỏ qua, uống lần tiếp đúng giờ",
            "Uống ngay nếu còn xa lần sau",
            "Bỏ qua, hỏi bác sĩ"
        ],
        "Không được": [
            "Uống gấp đôi liều",
            "Uống gấp đôi (tụt đường huyết)",
            "Uống gấp đôi",
            "Uống gấp đôi",
            "Tự ý bù liều"
        ]
    }
    
    df_forgot = pd.DataFrame(forgot_med_data)
    st.dataframe(df_forgot, use_container_width=True, hide_index=True)
    
    st.success("""
    💡 **Mẹo nhớ:**
    
    - **Quên < 2 giờ:** Uống ngay → Bình thường
    - **Quên > 2 giờ:** Bỏ qua → Uống lần sau đúng giờ
    - **Gần lần uống tiếp:** Bỏ qua → Đợi lần sau
    - **TUYỆT ĐỐI:** Không uống gấp đôi liều!
    - **Ghi chép:** Ghi vào sổ hoặc dùng app nhắc thuốc
    """)

