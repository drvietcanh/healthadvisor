"""
HealthAdvisor - Ứng dụng tư vấn sức khỏe đa bệnh
Trang chính
"""
import streamlit as st
from core.utils import get_greeting


# Cấu hình trang
st.set_page_config(
    page_title="HealthAdvisor - Tư vấn Sức khỏe",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS tùy chỉnh
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .disease-card {
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        margin: 1rem 0;
        transition: all 0.3s;
    }
    .disease-card:hover {
        border-color: #1f77b4;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .warning-box {
        background-color: #fff3cd;
        border-left: 5px solid #ffc107;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🏥 HealthAdvisor</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Trợ lý sức khỏe thông minh - Tư vấn y tế dễ hiểu cho mọi người</div>',
    unsafe_allow_html=True
)

# Welcome Banner - New users
if 'first_visit' not in st.session_state:
    st.session_state.first_visit = True

if st.session_state.first_visit:
    st.balloons()
    st.success("🎉 **Chào mừng bạn đến với HealthAdvisor!** Hãy bắt đầu bằng cách chọn một trong các mục dưới đây:")
    st.session_state.first_visit = False

# Quick Actions
st.markdown("### 🚀 Bạn muốn làm gì hôm nay?")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📊 Kiểm tra Huyết Áp", use_container_width=True, type="primary"):
        st.switch_page("pages/1_❤️_Tim_Mạch.py")
    st.caption("Đánh giá huyết áp & nhận tư vấn")

with col2:
    if st.button("🩸 Kiểm tra Đường Huyết", use_container_width=True, type="primary"):
        st.switch_page("pages/2_🩸_Tiểu_Đường.py")
    st.caption("Chuyển đổi mmol/L ↔ mg/dL")

with col3:
    if st.button("🤖 Hỏi AI Bác Sĩ", use_container_width=True, type="primary"):
        st.switch_page("pages/4_🤖_AI_Bác_Sĩ.py")
    st.caption("Chat với AI - Miễn phí!")

st.divider()

# Lời chào
greeting = get_greeting()
st.markdown(f"### {greeting}! 👋")

# Cảnh báo quan trọng
st.markdown("""
<div class="warning-box">
    <b>⚠️ LƯU Ý QUAN TRỌNG:</b><br>
    • Ứng dụng này chỉ cung cấp thông tin tham khảo, <b>KHÔNG THAY THẾ</b> bác sĩ<br>
    • Không tự ý chẩn đoán và điều trị<br>
    • Với triệu chứng cấp cứu: <b>GỌI 115 NGAY</b>
</div>
""", unsafe_allow_html=True)

# Giới thiệu
st.markdown("""
## 🎯 Ứng dụng giúp bạn:

✅ **Nhận biết** dấu hiệu bệnh sớm  
✅ **Hiểu rõ** về bệnh lý của mình  
✅ **Tư vấn** chế độ ăn uống, sinh hoạt phù hợp  
✅ **Hướng dẫn** cách theo dõi, quản lý bệnh tại nhà  
✅ **Trò chuyện** với AI bác sĩ để giải đáp thắc mắc  
""")

# Các chuyên khoa
st.markdown("## 🏨 Chọn chuyên khoa bạn quan tâm:")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="disease-card">
        <h3>❤️ Tim Mạch</h3>
        <p>Tăng huyết áp, suy tim, bệnh mạch vành</p>
        <ul style="text-align: left;">
            <li>Hướng dẫn đo huyết áp</li>
            <li>Chế độ ăn ít muối</li>
            <li>Thuốc tim mạch</li>
            <li>Vận động an toàn</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    if st.button("➡️ Vào trang Tim Mạch", key="cardio", use_container_width=True):
        st.switch_page("pages/1_❤️_Tim_Mạch.py")

with col2:
    st.markdown("""
    <div class="disease-card">
        <h3>🩸 Tiểu Đường</h3>
        <p>Típ 1, Típ 2, Tiền tiểu đường</p>
        <ul style="text-align: left;">
            <li>Đo đường huyết tại nhà</li>
            <li>Đếm carb, chỉ số GI</li>
            <li>Hướng dẫn tiêm insulin</li>
            <li>Phòng biến chứng</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    if st.button("➡️ Vào trang Tiểu Đường", key="diabetes", use_container_width=True):
        st.switch_page("pages/2_🩸_Tiểu_Đường.py")

with col3:
    st.markdown("""
    <div class="disease-card">
        <h3>🧠 Thần Kinh</h3>
        <p>Đột quỵ, động kinh, Parkinson</p>
        <ul style="text-align: left;">
            <li>Nhận biết BE-FAST</li>
            <li>Phòng ngừa đột quỵ</li>
            <li>Xử trí co giật</li>
            <li>Phục hồi chức năng</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    if st.button("➡️ Vào trang Thần Kinh", key="neuro", use_container_width=True):
        st.switch_page("pages/3_🧠_Thần_Kinh.py")

# Trang học dễ
st.markdown("---")
st.markdown("## 🎓 Học Y Khoa Siêu Dễ!")

col_learn1, col_learn2 = st.columns(2)
with col_learn1:
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 1rem; border-radius: 10px;">
        <h4>💡 Giải thích bằng hình ảnh</h4>
        <p>• So sánh với đời thường<br>
        • Mẹo nhớ siêu dễ<br>
        • Trắc nghiệm vui<br>
        • Công cụ so sánh trực quan</p>
    </div>
    """, unsafe_allow_html=True)
with col_learn2:
    if st.button("📚 Vào trang Học Dễ", key="learn", use_container_width=True, type="primary"):
        st.switch_page("pages/5_🎓_Học_Dễ.py")

# Chatbot AI
st.markdown("---")
st.markdown("## 🤖 Trò chuyện với AI Bác sĩ")

col_a, col_b = st.columns([2, 1])
with col_a:
    st.markdown("""
    **AI Bác sĩ** có thể:
    - Trả lời câu hỏi về bệnh của bạn
    - Tư vấn từng bước như bác sĩ thật
    - Giải thích bằng ngôn ngữ dễ hiểu
    - Hỗ trợ 24/7
    """)
with col_b:
    if st.button("💬 Bắt đầu trò chuyện", key="chatbot", use_container_width=True, type="primary"):
        st.switch_page("pages/4_🤖_AI_Bác_Sĩ.py")

# Thông tin liên hệ cấp cứu
st.markdown("---")
st.markdown("## 🚨 Số điện thoại cấp cứu")

col_x, col_y, col_z = st.columns(3)
with col_x:
    st.info("**☎️ Cấp cứu:** 115")
with col_y:
    st.info("**☎️ Tư vấn sức khỏe:** 1900 9095")
with col_z:
    st.info("**☎️ Bệnh viện:** 114")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888; padding: 1rem;">
    <small>
    HealthAdvisor v1.0 | Phát triển bởi AI<br>
    Mọi thông tin chỉ mang tính chất tham khảo<br>
    © 2025 - Với mục tiêu nâng cao sức khỏe cộng đồng
    </small>
</div>
""", unsafe_allow_html=True)

