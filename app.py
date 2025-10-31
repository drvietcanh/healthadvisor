"""
HealthAdvisor - Ứng dụng tư vấn sức khỏe đa bệnh
Trang chính
"""
import streamlit as st
from core.utils import get_greeting
from core.ui_config import get_custom_css


# Cấu hình trang
st.set_page_config(
    page_title="HealthAdvisor - Tư vấn Sức khỏe",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dark Mode Toggle trong Sidebar
with st.sidebar:
    st.markdown("### ⚙️ Cài đặt Giao diện")
    
    # Initialize dark mode state
    if 'dark_mode' not in st.session_state:
        st.session_state.dark_mode = False
    
    # Toggle
    dark_mode = st.toggle(
        "🌙 Chế độ Tối (Dark Mode)",
        value=st.session_state.dark_mode,
        help="Bật/tắt chế độ tối - dễ nhìn hơn ban đêm và tiết kiệm pin"
    )
    
    st.session_state.dark_mode = dark_mode
    
    if dark_mode:
        st.caption("✅ Đang dùng chế độ tối")
    else:
        st.caption("☀️ Đang dùng chế độ sáng")
    
    st.divider()

# Áp dụng CSS tùy chỉnh
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)

# Ẩn các trang phụ trợ khỏi sidebar menu bằng CSS + JavaScript (giữ lại SOS)
hide_sidebar_pages_css = """
<style>
    /* Ẩn các trang phụ trợ trong sidebar - Cách 1: theo href (KHÔNG ẩn SOS) */
    nav[data-testid="stSidebarNav"] a[href*="_7_"],
    nav[data-testid="stSidebarNav"] a[href*="_8_"],
    nav[data-testid="stSidebarNav"] a[href*="_9_"],
    nav[data-testid="stSidebarNav"] a[href*="_10_"],
    nav[data-testid="stSidebarNav"] a[href*="AI_Bác_Sĩ"],
    nav[data-testid="stSidebarNav"] a[href*="Nhật_Ký"],
    nav[data-testid="stSidebarNav"] a[href*="Nhắc_Thuốc"],
    nav[data-testid="stSidebarNav"] a[href*="Xu_Hướng"] {
        display: none !important;
    }
    
    /* Ẩn parent li element (KHÔNG ẩn SOS) */
    nav[data-testid="stSidebarNav"] li:has(a[href*="_7_"]),
    nav[data-testid="stSidebarNav"] li:has(a[href*="_8_"]),
    nav[data-testid="stSidebarNav"] li:has(a[href*="_9_"]),
    nav[data-testid="stSidebarNav"] li:has(a[href*="_10_"]),
    nav[data-testid="stSidebarNav"] li:has(a[href*="AI_Bác_Sĩ"]),
    nav[data-testid="stSidebarNav"] li:has(a[href*="Nhật_Ký"]),
    nav[data-testid="stSidebarNav"] li:has(a[href*="Nhắc_Thuốc"]),
    nav[data-testid="stSidebarNav"] li:has(a[href*="Xu_Hướng"]) {
        display: none !important;
    }
</style>

<script>
    // JavaScript để ẩn các trang phụ trợ - chạy sau khi DOM load (GIỮ LẠI SOS)
    function hideSidebarPages() {
        const nav = document.querySelector('[data-testid="stSidebarNav"]');
        if (!nav) return;
        
        // Danh sách các pattern cần ẩn (KHÔNG bao gồm SOS)
        const patternsToHide = [
            '_7_', '_8_', '_9_', '_10_',
            'AI_Bác_Sĩ', 'Nhật_Ký', 'Nhắc_Thuốc', 'Xu_Hướng'
        ];
        
        // Tìm tất cả links trong sidebar
        const links = nav.querySelectorAll('a');
        links.forEach(link => {
            const href = link.getAttribute('href') || '';
            const text = link.textContent || '';
            
            // Bỏ qua nếu là trang SOS
            if (href.includes('_12_') || href.includes('SOS')) {
                return; // Giữ lại trang SOS
            }
            
            // Kiểm tra nếu href chứa pattern cần ẩn
            if (patternsToHide.some(pattern => href.includes(pattern))) {
                // Ẩn link và parent li
                link.style.display = 'none';
                const parentLi = link.closest('li');
                if (parentLi) {
                    parentLi.style.display = 'none';
                }
            }
            
            // Kiểm tra theo text content (fallback) - KHÔNG ẩn Cấp Cứu
            if (text.includes('5 AI Bác Sĩ') || 
                text.includes('7 Nhật Ký') || 
                text.includes('8 Nhắc Thuốc') || 
                text.includes('9 Xu Hướng')) {
                link.style.display = 'none';
                const parentLi = link.closest('li');
                if (parentLi) {
                    parentLi.style.display = 'none';
                }
            }
        });
    }
    
    // Chạy ngay khi DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', hideSidebarPages);
    } else {
        hideSidebarPages();
    }
    
    // Chạy lại sau khi Streamlit render xong (MutationObserver)
    const observer = new MutationObserver(hideSidebarPages);
    observer.observe(document.body, { childList: true, subtree: true });
    
    // Chạy lại định kỳ (fallback)
    setInterval(hideSidebarPages, 1000);
</script>
"""
st.markdown(hide_sidebar_pages_css, unsafe_allow_html=True)

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
        st.switch_page("pages/3_🩸_Tiểu_Đường.py")
    st.caption("Chuyển đổi mmol/L ↔ mg/dL")

with col3:
    if st.button("🤖 Hỏi AI Bác Sĩ", use_container_width=True, type="primary"):
        st.switch_page("pages/_🤖_AI_Bác_Sĩ.py")
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

col1, col2, col3, col4 = st.columns(4)

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
        <h3>🫁 Hô Hấp</h3>
        <p>COPD, Hen suyễn</p>
        <ul style="text-align: left;">
            <li>Triệu chứng COPD</li>
            <li>Điều trị hen suyễn</li>
            <li>Kỹ thuật thở</li>
            <li>Phòng ngừa</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    if st.button("➡️ Vào trang Hô Hấp", key="respiratory", use_container_width=True):
        st.switch_page("pages/2_🫁_Hô_Hấp.py")

with col3:
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
        st.switch_page("pages/3_🩸_Tiểu_Đường.py")

with col4:
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
        st.switch_page("pages/4_🧠_Thần_Kinh.py")

# Thêm hàng mới cho Khớp - Cột sống
st.markdown("---")
st.markdown("## 🏥 Chuyên khoa khác:")

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.markdown("""
    <div class="disease-card">
        <h3>🦴 Khớp - Cột Sống</h3>
        <p>Thoái hóa khớp, viêm khớp, đau lưng, gút</p>
        <ul style="text-align: left;">
            <li>Thoái hóa khớp gối, háng</li>
            <li>Viêm khớp dạng thấp</li>
            <li>Đau thắt lưng, thoát vị đĩa đệm</li>
            <li>Bệnh Gút</li>
            <li>Bài tập cho khớp</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    if st.button("➡️ Vào trang Khớp - Cột sống", key="joint", use_container_width=True):
        st.switch_page("pages/6_🦴_Khớp_Cột_Sống.py")

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
        st.switch_page("pages/7_🎓_Học_Dễ.py")

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
        st.switch_page("pages/_🤖_AI_Bác_Sĩ.py")

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

