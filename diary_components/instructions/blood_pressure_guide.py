"""
Blood Pressure Guide - Hướng dẫn đo huyết áp đúng chuẩn
"""

import streamlit as st


def render_bp_guide():
    """Hiển thị hướng dẫn đo huyết áp đúng chuẩn"""
    with st.expander("🩺 Hướng dẫn ĐO HUYẾT ÁP ĐÚNG CHUẨN (WHO/AHA)", expanded=False):
        st.markdown("""
        ## 🩺 CÁCH ĐO HUYẾT ÁP CHÍNH XÁC
        
        ### 📋 CHUẨN BỊ TRƯỚC KHI ĐO (30 phút trước):
        
        ❌ **TRÁNH:**
        - Uống cà phê, trà, thuốc lá
        - Ăn no
        - Vận động mạnh
        - Căng thẳng, lo lắng
        - Nín đi tiểu (nên đi vệ sinh trước khi đo)
        
        ✅ **NÊN:**
        - Ngồi nghỉ yên 5-10 phút
        - Thư giãn, hít thở đều
        - Trong phòng ấm áp, yên tĩnh
        
        ---
        
        ### 🪑 TƯ THẾ ĐO ĐÚNG:
        
        ```
        👤 Ngồi thẳng lưng, dựa vào ghế
        💪 Cánh tay đo đặt trên bàn (ngang tim)
        🦵 Hai chân đặt phẳng sàn, không gác chân
        ✋ Lòng bàn tay ngửa lên
        🤐 Không nói chuyện khi đang đo
        ```
        
        **HÌNH ẢNH:**
        ```
             👤 Đầu thẳng
             |
        💪---+---💪  Tay trên bàn (ngang tim)
             |
            🪑 Ngồi thẳng
             |
        🦵   |   🦵  Chân phẳng sàn
        ```
        
        ---
        
        ### 📏 QUẤN BĂNG ĐO:
        
        1. **Vị trí:** Quấn quanh cánh tay trái (nếu thuận tay phải)
        2. **Độ cao:** Cách khuỷu tay 2-3 cm
        3. **Độ chặt:** Lọt 2 ngón tay vào giữa băng và da
        4. **Ống nghe:** Đặt đúng vị trí động mạch (bên trong khuỷu tay)
        
        ⚠️ **LƯU Ý:**
        - Cởi áo dài tay (không đo qua áo)
        - Không quấn quá chặt hoặc quá lỏng
        - Băng phải ngang mức tim
        
        ---
        
        ### 🔢 ĐO THẾ NÀO:
        
        **Máy điện tử (Tự động):**
        1. Bật máy
        2. Quấn băng đúng vị trí
        3. Ngồi yên, không cử động
        4. Nhấn nút Start
        5. Chờ máy đo xong (1-2 phút)
        6. Ghi lại kết quả
        
        **Máy thủy ngân (Cần người đo):**
        1. Quấn băng
        2. Bơm căng băng đến 180-200 mmHg
        3. Từ từ xả khí, nghe động mạch
        4. Tiếng đầu tiên = Tâm thu
        5. Tiếng cuối cùng = Tâm trương
        
        ---
        
        ### 🔁 ĐO BAO NHIÊU LẦN:
        
        ✅ **ĐÚNG CHUẨN:**
        - Đo **2-3 lần** (cách nhau 1-2 phút)
        - Lấy kết quả **TRUNG BÌNH** của 2-3 lần
        - Nếu chênh lệch > 10 mmHg → Đo lại
        
        ✅ **THỜI ĐIỂM ĐO:**
        - **Sáng:** Sau khi thức dậy, trước khi uống thuốc/ăn sáng
        - **Tối:** Trước khi đi ngủ
        - Đo **cùng giờ** mỗi ngày
        
        ---
        
        ### 📊 GHI CHÉP KẾT QUẢ:
        
        ✅ **Ghi rõ:**
        - Ngày giờ đo
        - Kết quả (ví dụ: 130/85)
        - Mạch (nếu máy có)
        - Thời điểm (sáng/tối, trước/sau ăn)
        - Cảm giác (đau đầu, chóng mặt...)
        
        → **Nhập vào app này để theo dõi xu hướng!**
        
        ---
        
        ### ⚠️ SAI LẦM THƯỜNG GẶP:
        
        | Sai lầm | Hậu quả | Cách khắc phục |
        |---------|---------|----------------|
        | Quấn băng qua áo | Kết quả cao hơn | Cởi áo |
        | Tay thòng xuống | Kết quả cao hơn | Đặt tay lên bàn |
        | Nói chuyện khi đo | Kết quả cao hơn | Im lặng |
        | Gác chân lên chân | Kết quả cao hơn | 2 chân phẳng sàn |
        | Đo 1 lần | Không chính xác | Đo 2-3 lần |
        | Băng quá chặt/lỏng | Sai số lớn | Lọt 2 ngón tay |
        
        ---
        
        ### 🚨 KHI NÀO CẦN GỌI BÁC SĨ:
        
        🚨 **NGAY LẬP TỨC - GỌI 115 (CẤP CỨU):**
        - Huyết áp ≥ 180/120 + đau đầu dữ dội
        - Huyết áp ≥ 180/120 + đau ngực
        - Huyết áp ≥ 180/120 + khó thở
        - Huyết áp ≥ 180/120 + mờ mắt
        - Huyết áp ≥ 180/120 + buồn nôn/nôn
        - Huyết áp ≥ 180/120 + tê tay chân
        
        📞 **HẸN GẶP BÁC SĨ (trong vài ngày):**
        - Huyết áp ≥ 140/90 liên tục 3-5 ngày
        - Dao động nhiều (100/60 → 160/100)
        - Có triệu chứng: chóng mặt, đau đầu, mệt...
        
        ---
        
        ### 📚 NGUỒN THAM KHẢO:
        - American Heart Association (AHA)
        - World Health Organization (WHO)
        - European Society of Hypertension (ESH)
        """)

