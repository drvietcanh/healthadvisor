"""
Trang Nhắc Uống Thuốc - Medication Reminder
Giúp người dùng (đặc biệt người già) nhớ uống thuốc đúng giờ
"""
import streamlit as st

st.set_page_config(
    page_title="Nhắc Uống Thuốc",
    page_icon="💊",
    layout="wide"
)

import sys
import os

# Thêm thư mục gốc vào path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from medication_reminder import (
    render_medication_form,
    render_schedule_view,
    render_history_view
)
from medication_reminder.medication_manager import render_medication_list
from core.ui_config import get_custom_css

try:
    # Kiểm tra session_state có tồn tại và là dict
    if hasattr(st, 'session_state') and st.session_state is not None:
        if 'dark_mode' not in st.session_state:
            st.session_state.dark_mode = False
        if 'extra_large_font' not in st.session_state:
            st.session_state.extra_large_font = False
        css_content = get_custom_css(
            dark_mode=st.session_state.dark_mode, 
            extra_large_font=st.session_state.extra_large_font
        )
        if css_content:
            st.markdown(css_content, unsafe_allow_html=True)
except Exception:
    # Nếu có lỗi, bỏ qua CSS - app vẫn chạy được
    pass

# Header
st.title("💊 Nhắc Uống Thuốc")
st.markdown("""
<div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            padding: 20px; border-radius: 10px; color: white; margin-bottom: 20px;'>
    <h3 style='margin:0; color: white;'>🔔 Đừng quên uống thuốc đúng giờ!</h3>
    <p style='margin: 10px 0 0 0; opacity: 0.9;'>
        Quản lý lịch uống thuốc, nhận nhắc nhở, và theo dõi tiến độ điều trị của bạn.
    </p>
</div>
""", unsafe_allow_html=True)

# Hướng dẫn nhanh
with st.expander("📖 Hướng dẫn sử dụng", expanded=False):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### ✨ Tính năng
        - ✅ **Thêm thuốc:** Quản lý danh sách thuốc cần uống
        - ⏰ **Đặt lịch nhắc:** Đặt giờ uống cho từng thuốc
        - 📅 **Lịch hôm nay:** Xem lịch uống thuốc trong ngày
        - ✅ **Đánh dấu đã uống:** Ghi nhận khi đã uống thuốc
        - 📊 **Thống kê:** Theo dõi tỷ lệ tuân thủ điều trị
        """)
    
    with col2:
        st.markdown("""
        ### 💡 Mẹo sử dụng
        1. **Chọn giờ cố định** mỗi ngày (VD: 8h sáng, 8h tối)
        2. **Bật thông báo** trên điện thoại để nhận nhắc
        3. **Ghi chú** cách dùng (trước/sau ăn, không uống cùng sữa...)
        4. **Kiểm tra mỗi ngày** để đảm bảo không bỏ sót
        5. **Xuất CSV** để mang đi khám bệnh
        """)

st.divider()

# Tabs chính
tab1, tab2, tab3, tab4 = st.tabs([
    "📅 Lịch hôm nay",
    "➕ Quản lý thuốc",
    "📊 Thống kê",
    "❓ Câu hỏi thường gặp"
])

# =============== TAB 1: LỊCH HÔM NAY ===============
with tab1:
    render_schedule_view()

# =============== TAB 2: QUẢN LÝ THUỐC ===============
with tab2:
    # Form thêm thuốc
    render_medication_form()
    
    st.divider()
    
    # Danh sách thuốc
    render_medication_list()

# =============== TAB 3: THỐNG KÊ ===============
with tab3:
    render_history_view()

# =============== TAB 4: FAQ ===============
with tab4:
    st.subheader("❓ Câu hỏi thường gặp")
    
    with st.expander("🔔 Làm sao để nhận thông báo nhắc uống thuốc?"):
        st.markdown("""
        Hiện tại, tính năng thông báo tự động chưa được tích hợp trực tiếp.
        
        **Giải pháp:**
        1. **Trên điện thoại:** Đặt báo thức/alarm cho mỗi giờ uống thuốc
        2. **Trên máy tính:** Dùng Calendar (Google Calendar, Outlook) đặt lịch lặp lại
        3. **Kiểm tra app mỗi ngày:** Vào tab "Lịch hôm nay" để xem lịch
        
        💡 **Mẹo:** Screenshot lịch hôm nay và đặt làm hình nền điện thoại!
        """)
    
    with st.expander("❌ Nếu quên uống thuốc thì phải làm sao?"):
        st.markdown("""
        ### Nguyên tắc chung:
        
        ✅ **Nếu nhớ trong vòng vài giờ:**
        - Uống ngay khi nhớ ra
        - Đánh dấu trong app với ghi chú "Uống trễ X giờ"
        
        ⚠️ **Nếu gần giờ uống lần tiếp theo:**
        - **KHÔNG uống 2 liều cùng lúc**
        - Bỏ qua liều đã quên
        - Uống liều tiếp theo đúng giờ
        
        🚨 **Lưu ý quan trọng:**
        - Mỗi loại thuốc có quy định riêng
        - Hỏi bác sĩ/dược sĩ về cách xử lý khi quên uống
        - Một số thuốc (tim mạch, tiểu đường) cần đặc biệt cẩn thận
        
        📞 **Khi nghi ngờ:** Gọi cho dược sĩ/bác sĩ để được tư vấn
        """)
    
    with st.expander("📊 Tỷ lệ tuân thủ là gì? Bao nhiêu % là tốt?"):
        st.markdown("""
        ### Tỷ lệ tuân thủ (Adherence Rate)
        
        **Định nghĩa:** Tỷ lệ % số liều thuốc đã uống / tổng số liều dự kiến
        
        **Phân loại:**
        - ✅ **≥ 80%:** Tốt - Điều trị hiệu quả
        - ⚠️ **60-79%:** Trung bình - Cần cải thiện
        - ❌ **< 60%:** Kém - Nguy cơ điều trị không hiệu quả
        
        **Tại sao quan trọng?**
        - Uống thuốc không đều → thuốc không phát huy tác dụng
        - Đặc biệt quan trọng với thuốc huyết áp, tiểu đường, tim mạch
        - Có thể gây kháng thuốc (VD: kháng sinh)
        
        💡 **Mục tiêu:** Duy trì tỷ lệ tuân thủ ≥ 80%
        """)
    
    with st.expander("💊 Tôi uống nhiều loại thuốc, có cách nào dễ nhớ không?"):
        st.markdown("""
        ### Mẹo nhớ uống thuốc cho người uống nhiều loại:
        
        1️⃣ **Hộp thuốc 7 ngày**
        - Mua hộp chia ngăn theo ngày trong tuần
        - Chuẩn bị thuốc 1 tuần vào tối Chủ Nhật
        - Mỗi sáng chỉ cần lấy ngăn của ngày hôm đó
        
        2️⃣ **Gắn với thói quen hàng ngày**
        - Để thuốc cạnh bàn ăn (uống sau bữa ăn)
        - Để cạnh bàn chải đánh răng (uống sáng/tối)
        - Để cạnh tivi (uống khi xem tin tức)
        
        3️⃣ **Báo thức điện thoại**
        - Đặt nhiều báo thức với tên thuốc
        - VD: "8:00 - Uống Metformin 500mg"
        
        4️⃣ **Nhờ người thân nhắc nhở**
        - Con cháu giúp nhắc và kiểm tra
        
        5️⃣ **Dùng app này mỗi ngày**
        - Kiểm tra tab "Lịch hôm nay" mỗi sáng
        - Đánh dấu tick khi đã uống
        """)
    
    with st.expander("📱 Tôi có thể dùng trên điện thoại không?"):
        st.markdown("""
        ### Sử dụng trên điện thoại/máy tính bảng
        
        ✅ **Có thể dùng!** App này chạy trên trình duyệt web
        
        **Cách dùng:**
        1. Mở trình duyệt (Chrome, Safari, Edge...)
        2. Vào link của app
        3. Có thể thêm vào màn hình chính (Add to Home Screen)
        
        **Lưu ý:**
        - Cần kết nối internet
        - Dữ liệu lưu trên máy của bạn
        - Nên dùng cùng 1 thiết bị để dữ liệu đồng bộ
        
        💡 **Tip:** Bookmark (đánh dấu trang) để dễ truy cập
        """)
    
    with st.expander("🗑️ Làm sao để xóa thuốc không uống nữa?"):
        st.markdown("""
        ### Cách xóa thuốc
        
        1. Vào tab **"Quản lý thuốc"**
        2. Tìm thuốc cần xóa trong danh sách
        3. Nhấn nút **"🗑️ Xóa"** bên phải
        4. Thuốc sẽ được đánh dấu không còn dùng
        
        ⚠️ **Lưu ý:**
        - Lịch sử uống thuốc vẫn được giữ lại
        - Không ảnh hưởng đến các thuốc khác
        - Có thể thêm lại nếu bắt đầu uống lại
        
        🚨 **Quan trọng:**
        - **KHÔNG tự ý ngừng thuốc** mà không hỏi bác sĩ
        - Đặc biệt thuốc huyết áp, tim mạch, tiểu đường
        - Ngừng đột ngột có thể nguy hiểm!
        """)
    
    with st.expander("📥 Làm sao để xuất dữ liệu mang đi khám bác sĩ?"):
        st.markdown("""
        ### Xuất dữ liệu
        
        **Cách 1: Xuất file CSV**
        1. Vào tab **"Thống kê"**
        2. Chọn tab **"Lịch sử"**
        3. Nhấn **"📥 Tải xuất file CSV"**
        4. Mở bằng Excel hoặc Google Sheets
        
        **Cách 2: Screenshot (chụp màn hình)**
        1. Vào tab "Lịch hôm nay" hoặc "Thống kê"
        2. Chụp màn hình
        3. Mang file ảnh đi khám
        
        **Cách 3: In ra giấy**
        1. Mở tab cần in
        2. Nhấn Ctrl+P (hoặc Cmd+P trên Mac)
        3. Chọn máy in hoặc "Save as PDF"
        
        💡 **Khi đi khám, bác sĩ cần biết:**
        - Danh sách thuốc đang uống
        - Liều lượng và giờ uống
        - Tỷ lệ tuân thủ (% uống đúng)
        - Có tác dụng phụ gì không
        """)

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>💊 <b>Lưu ý quan trọng:</b> App này chỉ hỗ trợ nhắc nhở uống thuốc, 
    KHÔNG thay thế lời khuyên y tế từ bác sĩ/dược sĩ.</p>
    <p>🚨 Nếu có bất kỳ thắc mắc nào về thuốc, hãy hỏi bác sĩ hoặc dược sĩ!</p>
</div>
""", unsafe_allow_html=True)

if st.button("⬅️ Quay lại trang chính", use_container_width=True):
    st.switch_page("app.py")

