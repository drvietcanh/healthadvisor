"""
Drug Interactions Tab - Tương tác thuốc
"""

import streamlit as st


def render_drug_interactions_tab():
    """Tab Tương tác thuốc"""
    st.markdown("""
    ### 🔄 Tương tác thuốc nguy hiểm:
    
    **⚠️ Paracetamol + Rượu Bia:**
    - 🍺 **Rượu bia + Paracetamol = SUY GAN CẤP TÍNH, TỬ VONG!**
    - ⏰ Phải cách ít nhất **8-12 giờ** sau khi uống rượu bia
    - 🔥 Đau đầu do say rượu? → Uống nước, nghỉ ngơi, KHÔNG dùng paracetamol!
    
    **⚠️ Thuốc huyết áp + Nước bưởi:**
    - Một số thuốc huyết áp (Amlodipine, Felodipine, Nifedipine...) không uống với nước bưởi
    - → Tăng tác dụng, hạ huyết áp quá mức → Chóng mặt, ngất xỉu
    - ✅ An toàn: Losartan, Valsartan, Enalapril ít bị ảnh hưởng
    
    **⚠️ Aspirin + Thuốc chống đông:**
    - → Tăng nguy cơ chảy máu nghiêm trọng
    - Phải có chỉ định bác sĩ, theo dõi chặt chẽ
    
    **⚠️ Kháng sinh + Sữa/Canxi:**
    - Tetracycline, Ciprofloxacin không uống với sữa, canxi
    - → Tạo phức hợp không hấp thu được → Mất tác dụng
    - ✅ Cách xa bữa ăn/sữa 2 giờ
    
    **⚠️ Sắt + Trà/Cà phê:**
    - Trà, cà phê chứa tanin → Giảm hấp thu sắt
    - → Uống cách xa 1-2 giờ
    
    **✅ Nên làm:**
    - Kê khai đầy đủ thuốc đang uống với bác sĩ
    - Hỏi dược sĩ về tương tác
    - Đọc kỹ tờ hướng dẫn
    - Không tự ý kết hợp thuốc
    """)
    
    st.warning("""
    ⚠️ **Lưu ý quan trọng:**
    
    - Uống nhiều loại thuốc → Phải có bác sĩ theo dõi
    - Tự ý kết hợp thuốc → Nguy hiểm!
    - Có tác dụng phụ bất thường → Dừng thuốc, gọi bác sĩ ngay
    - Ghi nhớ: **Rượu bia + Paracetamol = TỬ VONG!**
    """)

