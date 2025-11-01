"""
Trang tư vấn về bệnh Thần Kinh (Đột quỵ, Động kinh...)
"""
import streamlit as st
import sys
sys.path.append('..')

from core.ui_config import get_custom_css
from core.sidebar_menu import render_sidebar_menu, hide_default_nav
# from core import rules  # Tạm comment vì chưa cần

st.set_page_config(page_title="Thần Kinh", page_icon="🧠", layout="wide")

# Ẩn menu mặc định của Streamlit - PHẢI GỌI TRƯỚC
hide_default_nav()

# Render menu sidebar tùy chỉnh
# TẠM ẨN - Sẽ phát triển thêm chức năng sau
# render_sidebar_menu()

# Áp dụng Dark Mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)

st.title("🧠 Tư vấn Thần Kinh")

# Tabs
tab1, tab2, tab3 = st.tabs(["🚨 Đột Quỵ", "⚡ Động Kinh", "📊 Kiểm Tra BE-FAST"])

# ============= TAB ĐỘT QUỴ =============
with tab1:
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

# ============= TAB ĐỘNG KINH =============
with tab2:
    st.header("Động Kinh (Epilepsy)")
    
    with st.expander("📖 Động kinh là gì?"):
        st.markdown("""
### ⚡ ĐỘNG KINH LÀ GÌ?

Động kinh là bệnh não gây ra các cơn co giật do não phóng điện bất thường.

**Không phải ai co giật cũng là động kinh:**
- Sốt cao ở trẻ em có thể co giật
- Hạ đường huyết, hạ canxi có thể co giật
- Động kinh = Co giật tái đi tái lại không rõ nguyên nhân

**Phổ biến:** Khoảng 1% dân số (50-100 triệu người trên thế giới)
""")
    
    with st.expander("🔍 Triệu chứng"):
        st.markdown("""
### Cơn động kinh có thể có nhiều dạng:

**Cơn co giật toàn thể (Grand mal):**
- Co cứng toàn thân
- Giật cục bộ hoặc toàn thân
- Cắn lưỡi, tiểu không tự chủ
- Bất tỉnh 2-5 phút
- Sau đó lơ mơ, buồn ngủ

**Cơn vắng ý thức (Absence):**
- Chỉ "đơ" vài giây
- Mắt trợn, không đáp ứng
- Sau đó tỉnh, không nhớ gì

**Cơn động kinh khu trú:**
- Giật một phần cơ thể (tay, mặt...)
- Cảm giác lạ, ngửi mùi lạ
- Có thể vẫn tỉnh
""")
    
    with st.expander("🚑 Xử trí khi thấy người co giật"):
        st.error("### KHÔNG hoảng loạn - Làm theo 5 bước:")
        
        st.markdown("""
**1. BẢO VỆ AN TOÀN:**
- Đặt người nằm nghiêng (tránh sặc)
- Kê gối/vật mềm dưới đầu
- Di chuyển đồ vật nguy hiểm ra xa

**2. KHÔNG CHE MỒM:** 
- ❌ Không nhét thìa, gậy vào miệng (gãy răng, tổn thương!)
- ❌ Không giữ người bệnh (có thể gây gãy xương)
- ❌ Không cho uống thuốc khi đang giật

**3. TÍNH THỜI GIAN:**
- Dùng đồng hồ đếm xem co giật bao lâu

**4. GỌI 115 NẾU:**
- Co giật > 5 phút
- Co giật liên tiếp nhiều lần
- Lần đầu tiên co giật
- Bị thương khi co giật
- Mang thai

**5. SAU CƠN GIẬT:**
- Để người nằm nghiêng
- Theo dõi, an ủi
- Không cho ăn uống ngay (chờ tỉnh hẳn)
""")

# ============= TAB KIỂM TRA BE-FAST =============
with tab3:
    st.header("📊 Kiểm tra triệu chứng đột quỵ")
    
    st.warning("⚠️ Công cụ này chỉ để tham khảo. Nếu nghi ngờ đột quỵ → GỌI 115 NGAY!")
    
    st.markdown("### Kiểm tra các dấu hiệu BE-FAST:")
    
    # Form kiểm tra
    with st.form("befast_check"):
        balance = st.checkbox("**B - Mất thăng bằng, chóng mặt đột ngột**")
        eyes = st.checkbox("**E - Nhìn mờ, nhìn đôi đột ngột**")
        face = st.checkbox("**F - Xệ mặt, méo miệng**")
        arm = st.checkbox("**A - Yếu tay hoặc chân (một bên)**")
        speech = st.checkbox("**S - Nói khó, nói lắp**")
        
        st.divider()
        onset_time = st.number_input(
            "Triệu chứng xuất hiện bao lâu rồi? (giờ)",
            min_value=0.0,
            max_value=72.0,
            value=2.0,
            step=0.5
        )
        
        submitted = st.form_submit_button("Đánh giá", type="primary")
    
    if submitted:
        has_symptoms = any([balance, eyes, face, arm, speech])
        
        if has_symptoms:
            st.error("### 🚨 NGHI NGỜ ĐỘT QUỴ - HÀNH ĐỘNG NGAY!")
            st.error("### 👉 GỌI CẤP CỨU 115 NGAY!")
            
            positive_signs = []
            if balance: positive_signs.append("Mất thăng bằng")
            if eyes: positive_signs.append("Rối loạn nhìn")
            if face: positive_signs.append("Xệ mặt")
            if arm: positive_signs.append("Yếu tay chân")
            if speech: positive_signs.append("Nói khó")
            
            st.markdown(f"**Dấu hiệu phát hiện:** {', '.join(positive_signs)}")
            st.markdown(f"**Thời gian:** {onset_time} giờ trước")
            
            # Kiểm tra khung giờ điều trị
            if onset_time <= 4.5:
                st.success("✅ VẪN TRONG KHUNG GIỜ VÀNG tiêm thuốc tiêu sợi huyết!")
                st.success(f"Còn khoảng {4.5 - onset_time:.1f} giờ - NHANH LÊN!")
            elif onset_time <= 24:
                st.warning(f"⚠️ Vẫn trong khung giờ lấy huyết khối (24h)")
                st.warning("Vẫn CÓ THỂ điều trị - ĐỪNG BỎ LỠ!")
            else:
                st.error("Đã quá 24 giờ - Nhưng vẫn CẦN khám ngay để đánh giá và phòng ngừa")
            
            st.divider()
            st.markdown("""
#### ⏰ TRƯỚC KHI ĐẾN BỆNH VIỆN:
- ✅ GHI NHỚ thời điểm bình thường cuối cùng
- ✅ KHÔNG tự lái xe - Chờ xe cấp cứu
- ✅ KHÔNG cho ăn uống (nguy cơ sặc)
- ✅ Mang theo danh sách thuốc đang dùng
- ✅ Nằm đầu cao (kê 2-3 cái gối)
""")
        else:
            st.success("### ✅ Không có dấu hiệu đột quỵ rõ ràng")
            st.info("Tuy nhiên, nếu có bất kỳ triệu chứng bất thường nào, hãy gặp bác sĩ để kiểm tra.")

# Nút quay lại
st.divider()
if st.button("⬅️ Quay lại trang chính"):
    st.switch_page("app.py")

