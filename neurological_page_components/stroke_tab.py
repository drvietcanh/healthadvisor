"""
Neurological Page Components - Stroke Tab
Tab Đột Quỵ
"""

import streamlit as st


def render_stroke_tab():
    """Render tab Đột Quỵ"""
    st.header("Đột Quỵ (Tai biến mạch máu não)")
    
    with st.expander("📖 Đột quỵ là gì?", expanded=True):
        st.markdown("""
### 🧠 ĐỘT QUỴ LÀ GÌ?

Đột quỵ xảy ra khi não bị thiếu máu đột ngột:
- **Đột quỵ thiếu máu** (80%): Mạch máu não bị tắc
- **Đột quỵ chảy máu** (20%): Mạch máu não vỡ, chảy máu

Giống như cơn "đau tim" của não - RẤT NGUY HIỂM!

⏰ **THỜI GIAN LÀ VÀNG:**
- Trong 4.5 giờ đầu: Có thể tiêm thuốc tiêu sợi huyết
- Trong 24 giờ đầu: Có thể lấy huyết khối
- Càng sớm điều trị = càng ít tổn thương não
""")
    
    with st.expander("🚨 BE-FAST - Dấu hiệu cảnh báo"):
        st.error("### BẤT KỲ DẤU HIỆU NÀO → GỌI 115 NGAY!")
        
        st.markdown("""
#### Nhớ 6 chữ BE-FAST:

**B - Balance (Mất thăng bằng)**
- Chóng mặt đột ngột
- Loạng choạng, khó đứng vững
- Đi không thẳng

**E - Eyes (Rối loạn thị giác)**
- Nhìn mờ, nhìn đôi
- Mất một phần thị trường
- Nhắm mắt không được

**F - Face (Xệ mặt)**
- Một bên mặt xệ, méo miệng
- Nụ cười lệch
- Không nhướng mày được

**A - Arm (Yếu tay chân)**
- Yếu, tê một bên tay/chân
- Giơ hai tay lên, một tay sa xuống
- Không cầm nắm được

**S - Speech (Nói khó)**
- Nói lắp, nói không rõ
- Nói không ra lời
- Không hiểu người khác nói gì

**T - Time (Thời gian - GỌI 115!)**
- GHI NHỚ thời điểm bình thường cuối cùng
- GỌI 115 NGAY - Mỗi phút trì hoãn = 2 triệu tế bào não chết!
""")
    
    with st.expander("💊 Phòng ngừa đột quỵ"):
        st.markdown("""
### Kiểm soát các yếu tố nguy cơ:

**1. Huyết áp** (quan trọng nhất!)
- Mục tiêu: < 140/90 mmHg
- Uống thuốc đều đặn
- Ăn ít muối

**2. Tiểu đường**
- Kiểm soát đường huyết tốt
- HbA1c < 7%

**3. Cholesterol**
- Ăn ít mỡ động vật
- Có thể cần thuốc statin

**4. Rung nhĩ** (loạn nhịp tim)
- Nguy cơ đột quỵ tăng 5 lần
- Cần thuốc chống đông

**5. Lối sống:**
- ✅ Bỏ thuốc lá (giảm 50% nguy cơ)
- ✅ Vận động 30 phút/ngày
- ✅ Ăn nhiều rau, ít mỡ
- ✅ Giảm cân nếu thừa cân
- ❌ Hạn chế rượu bia
""")

