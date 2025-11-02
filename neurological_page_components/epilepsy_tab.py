"""
Neurological Page Components - Epilepsy Tab
Tab Động Kinh
"""

import streamlit as st


def render_epilepsy_tab():
    """Render tab Động Kinh"""
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

