"""
Food Interactions Tab - Thuốc & Thức ăn
"""

import streamlit as st
import pandas as pd


def render_food_interactions_tab():
    """Tab Thuốc & Thức ăn"""
    st.markdown("""
    ### 🍽️ Thuốc & Thức ăn - Khi nào hợp lý?
    
    **📋 Bảng hướng dẫn uống thuốc thông dụng:**
    """)
    
    med_food_data = {
        "Loại thuốc": [
            "Paracetamol (Panadol, Efferalgan)",
            "Ibuprofen (Brufen, Nurofen)",
            "Aspirin",
            "Thuốc kháng sinh (Amoxicillin, Ciprofloxacin...)",
            "Thuốc bổ sắt",
            "Canxi",
            "Vitamin D",
            "Thuốc huyết áp (Amlodipine, Enalapril...)",
            "Thuốc tiểu đường (Metformin)",
            "Omeprazole (giảm đau dạ dày)",
            "Thyroxine (hormone tuyến giáp)",
            "Kháng sinh Tetracycline"
        ],
        "Nên uống": [
            "Khi nào cũng được, với hoặc không với thức ăn",
            "Sau khi ăn no (tránh đau dạ dày)",
            "Sau khi ăn (tránh viêm dạ dày)",
            "Xem nhãn - thường sau ăn hoặc cách 2h với sữa",
            "Khi đói (hấp thu tốt hơn)",
            "Sau khi ăn (hấp thu tốt hơn)",
            "Sau khi ăn (cần chất béo để hấp thu)",
            "Theo chỉ định, thường sau ăn",
            "Sau khi ăn (giảm tác dụng phụ)",
            "Trước ăn 30 phút (tác dụng tốt nhất)",
            "Khi đói, trước ăn 30-60 phút",
            "Cách xa bữa ăn 2 giờ (trước hoặc sau)"
        ],
        "Tránh uống với": [
            "Rượu bia (SUY GAN!)",
            "Rượu bia, thức ăn cay",
            "Rượu bia, thức ăn cay",
            "Sữa, sữa chua (một số loại)",
            "Trà, cà phê, sữa (giảm hấp thu)",
            "Trà, cà phê (giảm hấp thu)",
            "Không có",
            "Nước bưởi (một số loại)",
            "Rượu bia",
            "Không có",
            "Sữa, canxi, sắt (cách xa 2-4 giờ)",
            "Sữa, canxi, sắt, thuốc kháng acid"
        ]
    }
    
    df = pd.DataFrame(med_food_data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.warning("""
    ⚠️ **LƯU Ý QUAN TRỌNG:**
    
    - **Paracetamol + Rượu bia:** 🚫 TUYỆT ĐỐI TRÁNH! → Suy gan cấp tính, tử vong
    - **Thuốc huyết áp + Nước bưởi:** ⚠️ Một số loại tương tác → Hạ huyết áp quá mức
    - **Kháng sinh + Sữa:** ⚠️ Một số giảm hấp thu → Uống cách xa 2 giờ
    - **Aspirin/Ibuprofen:** ⚠️ Uống sau ăn để tránh viêm loét dạ dày
    """)
    
    st.info("""
    💡 **Mẹo nhớ:**
    
    - **Thuốc đau dạ dày (Omeprazole):** Uống TRƯỚC ăn 30 phút → Tác dụng tốt nhất
    - **Thuốc sắt:** Uống khi đói + uống nước cam (vitamin C giúp hấp thu)
    - **Canxi:** Uống sau ăn + không uống cùng sắt (cách xa 2 giờ)
    - **Kháng sinh:** Đọc kỹ nhãn, nhiều loại không uống với sữa
    """)

