"""
General Health Tips - Medicine
Mẹo vặt về thuốc
"""

import streamlit as st
import pandas as pd


def render_medicine_tips():
    """Mẹo vặt về thuốc"""
    st.subheader("💊 Mẹo vặt về thuốc")
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📅 Bảo quản thuốc",
        "💧 Cách uống thuốc",
        "🍽️ Thuốc & Thức ăn",
        "🔄 Tương tác thuốc",
        "⏰ Quên uống thuốc",
        "📋 Đọc nhãn thuốc"
    ])
    
    with tab1:
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
    
    with tab2:
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
    
    with tab3:
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
    
    with tab4:
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
    
    with tab5:
        st.markdown("""
        ### ⏰ Quên uống thuốc - Xử trí thế nào?
        
        **🕐 **Quên thuốc - Nhớ lại trong vòng 1-2 giờ:**
        - ✅ **Uống ngay** (nếu chưa đến lần uống tiếp theo)
        - ✅ Uống bù, sau đó uống lần tiếp theo **đúng giờ**
        - ✅ Ví dụ: Quên 8h sáng, nhớ lúc 9h → Uống ngay, 8h tối uống đúng giờ
        
        **⏰ **Quên thuốc - Gần đến lần uống tiếp (còn 2-3 giờ):**
        - ✅ **Bỏ qua lần quên**, đợi đến lần uống tiếp theo
        - ❌ **KHÔNG uống gấp đôi liều!** → Quá liều, nguy hiểm
        - ✅ Ví dụ: Quên 8h sáng, nhớ lúc 6h chiều (gần 8h tối) → Bỏ qua, uống 8h tối bình thường
        
        **💊 **Thuốc uống 1 lần/ngày:**
        - Quên → Uống ngay khi nhớ ra
        - Nếu gần đến lần uống hôm sau → Bỏ qua, đợi lần sau
        - **KHÔNG uống 2 viên cùng lúc!**
        
        **💊 **Thuốc uống nhiều lần/ngày (2-3 lần):**
        - Quên lần 1 → Uống ngay nếu còn cách lần 2 > 2 giờ
        - Gần đến lần 2 → Bỏ qua lần 1, uống đúng giờ lần 2
        
        **📊 **Bảng xử trí quên thuốc theo loại:**
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
    
    with tab6:
        st.markdown("""
        ### 📋 Đọc nhãn thuốc đúng cách:
        
        **🏷️ **Thông tin quan trọng trên nhãn thuốc:**
        
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
        
        **⚠️ **Cảnh báo trên nhãn:**
        - "Không dùng quá 3-5 ngày" → Dùng đúng thời gian
        - "Có thể gây buồn ngủ" → Không lái xe sau khi uống
        - "Không dùng với rượu bia" → TUYỆT ĐỐI tuân thủ
        - "Không dùng khi mang thai" → Hỏi bác sĩ
        
        **✅ **Kiểm tra trước khi uống:**
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

