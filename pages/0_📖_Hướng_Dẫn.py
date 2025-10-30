"""
Trang Hướng dẫn sử dụng HealthAdvisor
"""
import streamlit as st
import sys
sys.path.append('..')

from core.ui_config import get_custom_css

st.set_page_config(page_title="Hướng dẫn", page_icon="📖", layout="wide")

# Áp dụng Dark Mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)

st.title("📖 Hướng dẫn sử dụng HealthAdvisor")

st.success("👋 **Chào mừng bạn đến với HealthAdvisor!** Chỉ cần 3 phút để biết cách dùng app này.")

# Tab hướng dẫn
tab1, tab2, tab3, tab4 = st.tabs([
    "🚀 Bắt đầu nhanh",
    "📚 Hướng dẫn chi tiết",
    "❓ Câu hỏi thường gặp",
    "💡 Mẹo & Thủ thuật"
])

# ===== TAB 1: BẮT ĐẦU NHANH =====
with tab1:
    st.header("🚀 3 Bước Bắt Đầu")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 1️⃣ Kiểm tra Sức khỏe
        
        **Bạn muốn:**
        - Kiểm tra huyết áp?
        - Đo đường huyết?
        - Tính BMI?
        
        👉 **Vào các trang:**
        - ❤️ Tim Mạch
        - 🩸 Tiểu Đường
        - 📊 Công cụ
        
        📝 **Nhập số liệu** → Nhận **kết quả + tư vấn**
        """)
    
    with col2:
        st.markdown("""
        ### 2️⃣ Tìm hiểu Bệnh
        
        **Bạn muốn học về:**
        - Tăng huyết áp?
        - Tiểu đường?
        - Đột quỵ?
        
        👉 **Vào trang tương ứng:**
        - ❤️ Tim Mạch → Tab "Giới thiệu"
        - 🩸 Tiểu Đường → Tab "Thuốc"
        - 🧠 Thần Kinh
        
        📚 **Đọc thông tin** dễ hiểu, bằng tiếng Việt
        """)
    
    with col3:
        st.markdown("""
        ### 3️⃣ Hỏi AI Bác Sĩ
        
        **Bạn có câu hỏi?**
        - Huyết áp bao nhiêu là bình thường?
        - Ăn gì để giảm đường huyết?
        - Thuốc có tác dụng phụ gì?
        
        👉 **Vào trang:**
        - 🤖 AI Bác Sĩ
        
        💬 **Chat trực tiếp** với AI (miễn phí!)
        """)
    
    st.divider()
    
    st.info("💡 **Mẹo:** Dùng **Sidebar** (bên trái) để chuyển giữa các trang!")
    
    # Video demo (placeholder)
    st.subheader("🎥 Video Hướng dẫn (30 giây)")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ", start_time=0)  # Thay bằng video thật
    
    st.info("📺 Chưa có video? Xem hình ảnh minh họa bên dưới! ⬇️")

# ===== TAB 2: HƯỚNG DẪN CHI TIẾT =====
with tab2:
    st.header("📚 Hướng dẫn Chi tiết từng Trang")
    
    # ❤️ TIM MẠCH
    with st.expander("❤️ Trang Tim Mạch", expanded=False):
        st.markdown("""
        ### 📍 Bạn sẽ tìm thấy gì:
        
        **Tab "Giới thiệu":**
        - Tăng huyết áp là gì?
        - Phân loại huyết áp (bình thường → nguy hiểm)
        - Triệu chứng, nguyên nhân
        
        **Tab "Thuốc":**
        - 5 nhóm thuốc huyết áp phổ biến
        - Tên thuốc tại Việt Nam
        - Tác dụng phụ
        - Cách uống đúng
        
        **Tab "Dinh dưỡng":**
        - Chế độ ăn DASH
        - Thực phẩm nên ăn/tránh
        - Giảm muối thế nào
        
        **Tab "Công cụ":**
        - ⚡ **Đánh giá huyết áp** (nhập số → kết quả)
        - Tính BMI
        - Tìm hiểu thêm
        
        ---
        
        ### 🎯 Cách dùng:
        1. Click vào tab bạn quan tâm
        2. Đọc thông tin
        3. Dùng công cụ nếu cần
        4. Hỏi AI nếu còn thắc mắc
        """)
    
    # 🩸 TIỂU ĐƯỜNG
    with st.expander("🩸 Trang Tiểu Đường", expanded=False):
        st.markdown("""
        ### 📍 Bạn sẽ tìm thấy gì:
        
        **Tab "Giới thiệu":**
        - Tiểu đường là gì? (giải thích đơn giản!)
        - Típ 1 vs Típ 2
        - Chỉ số đường huyết (mmol/L và mg/dL)
        - Triệu chứng
        
        **Tab "Thuốc":**
        - Thuốc uống (Metformin, DPP-4i...)
        - **Insulin đầy đủ** (5 loại + cách tiêm)
        - Tên thuốc VN
        - Hạ đường huyết - xử trí
        
        **Tab "Ăn uống":**
        - **GI vs GL** (quan trọng!)
        - 60+ thực phẩm VN (cơm, phở, bún, trái cây...)
        - Đếm carb
        - Thực đơn mẫu
        
        **Tab "Công cụ":**
        - Chuyển đổi đường huyết (mmol/L ↔ mg/dL)
        - Tính BMI
        
        ---
        
        ### 🎯 Ví dụ:
        ❓ **"Tôi ăn xoài có sao không?"**
        → Vào Tab "Ăn uống" → Tìm "Xoài" → GL = 11 (Trung bình) → Ăn 1/2 quả OK!
        """)
    
    # 🧠 THẦN KINH
    with st.expander("🧠 Trang Thần Kinh", expanded=False):
        st.markdown("""
        ### 📍 Bạn sẽ tìm thấy gì:
        
        **Đột quỵ:**
        - Dấu hiệu **BE-FAST** (quan trọng nhất!)
        - ⚠️ **Thời gian vàng** - GỌI 115 NGAY!
        - Phòng ngừa
        
        **Động kinh (Epilepsy):**
        - Triệu chứng
        - Xử trí khi có cơn
        - Điều trị
        
        ---
        
        ### 🚨 Ghi nhớ BE-FAST:
        - **B**alance: Mất thăng bằng
        - **E**yes: Nhìn mờ
        - **F**ace: Xệ mặt
        - **A**rms: Yếu tay chân
        - **S**peech: Nói khó
        - **T**ime: GỌI 115 NGAY!!!
        """)
    
    # 🤖 AI BÁC SĨ
    with st.expander("🤖 Trang AI Bác Sĩ", expanded=False):
        st.markdown("""
        ### 📍 Tính năng:
        
        **Chat với AI:**
        - Hỏi bất kỳ câu gì về sức khỏe
        - AI trả lời bằng tiếng Việt
        - Dễ hiểu, không chuyên môn quá sâu
        
        **Cách dùng:**
        1. **Chọn AI Provider** (Gemini MIỄN PHÍ!)
        2. **Nhập API key** (lấy trong 1 phút)
        3. **Chọn chuyên khoa** (Tim mạch/Tiểu đường...)
        4. **Hỏi!**
        
        **Lấy Gemini API key:**
        1. Vào: https://aistudio.google.com/app/apikey
        2. Đăng nhập Gmail
        3. Click "Create API key"
        4. Copy & paste vào app
        
        ---
        
        ### 💬 Ví dụ câu hỏi:
        - "Huyết áp 140/90 có cao không?"
        - "Ăn gì để giảm đường huyết?"
        - "Metformin có tác dụng phụ gì?"
        - "Khi nào cần gọi cấp cứu?"
        
        ✅ AI sẽ trả lời chi tiết, dễ hiểu!
        """)
    
    # 🎓 HỌC DỄ
    with st.expander("🎓 Trang Học Dễ", expanded=False):
        st.markdown("""
        ### 📍 Tính năng:
        
        **Giải thích y khoa bằng hình ảnh & ví dụ đời thường:**
        - Huyết áp = Bơm nước 🚰
        - Tiểu đường = Chìa khóa không vặn 🔑
        - Đột quỵ = Tắc đường ống 🚧
        
        **Mẹo nhớ:**
        - Khẩu quyết dễ nhớ
        - So sánh trực quan
        
        **Trắc nghiệm:**
        - Kiểm tra kiến thức
        - Vui, không áp lực!
        
        ---
        
        ### 🎯 Phù hợp với:
        - Người mới tìm hiểu
        - Người già, ít học
        - Muốn học nhanh, nhớ lâu
        """)

# ===== TAB 3: FAQ =====
with tab3:
    st.header("❓ Câu hỏi Thường gặp")
    
    with st.expander("❓ App này miễn phí không?"):
        st.success("✅ **Hoàn toàn MIỄN PHÍ!**")
        st.markdown("""
        - Tất cả thông tin: **Miễn phí**
        - Công cụ: **Miễn phí**
        - AI Bác Sĩ: **Miễn phí** (nếu dùng Gemini)
        
        💰 Chỉ tốn tiền nếu bạn chọn OpenAI (ChatGPT) - nhưng Gemini miễn phí cũng rất tốt!
        """)
    
    with st.expander("❓ Tôi có thể tin thông tin trên app không?"):
        st.info("📚 **Thông tin từ nguồn đáng tin cậy:**")
        st.markdown("""
        - Hướng dẫn y khoa quốc tế (AHA, ADA, WHO...)
        - Bệnh viện uy tín (Mayo Clinic, Cleveland Clinic...)
        - Dược điển Việt Nam
        
        ⚠️ **LƯU Ý:**
        - App **KHÔNG thay thế** bác sĩ!
        - App chỉ **giáo dục** và **tư vấn chung**
        - **KHÔNG tự ý điều trị** dựa vào app
        - **Luôn hỏi bác sĩ** khi có bệnh!
        """)
    
    with st.expander("❓ Tôi cần API key để làm gì?"):
        st.markdown("""
        **API key dùng để:**
        - Kích hoạt tính năng **AI Bác Sĩ**
        - Chat hỏi đáp thông minh
        
        **Không có API key vẫn dùng được:**
        - ✅ Tất cả thông tin bệnh
        - ✅ Công cụ tính toán
        - ✅ Trang Học Dễ
        - ❌ Chỉ không chat được với AI
        
        **Lấy API key:**
        - **Gemini (Google):** MIỄN PHÍ, 1 phút lấy được
        - **OpenAI:** Trả phí, phức tạp hơn
        
        👉 Khuyến nghị: Dùng Gemini!
        """)
    
    with st.expander("❓ Tôi quên cách dùng, làm sao?"):
        st.success("📖 **Quay lại trang này bất kỳ lúc nào!**")
        st.markdown("""
        1. Click **Sidebar** (bên trái)
        2. Chọn **📖 Hướng Dẫn**
        3. Đọc lại!
        
        Hoặc:
        - Hỏi **🤖 AI Bác Sĩ**: "Hướng dẫn tôi cách dùng app này"
        """)
    
    with st.expander("❓ App có lưu dữ liệu của tôi không?"):
        st.warning("🔒 **Quyền riêng tư:**")
        st.markdown("""
        **Hiện tại:**
        - App **KHÔNG lưu** dữ liệu cá nhân
        - Tất cả tính toán **chỉ trên máy bạn**
        - Không gửi về server
        
        **Tương lai (nếu thêm tính năng):**
        - Sẽ có tùy chọn **lưu lịch sử** (optional)
        - Bạn **hoàn toàn kiểm soát** dữ liệu
        - Có thể **xóa bất kỳ lúc nào**
        """)

# ===== TAB 4: MẸO & THỦTHUẬT =====
with tab4:
    st.header("💡 Mẹo & Thủ thuật Dùng App Hiệu quả")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("✨ Mẹo Chung")
        st.markdown("""
        **1. Dùng Sidebar để điều hướng nhanh**
        - Click icon ☰ (góc trên bên trái)
        - Chọn trang muốn xem
        
        **2. Đánh dấu trang yêu thích**
        - Bookmark trên trình duyệt (Ctrl+D)
        - Ví dụ: Bookmark trực tiếp "🩸 Tiểu Đường"
        
        **3. Dùng tìm kiếm trình duyệt**
        - Ctrl+F để tìm từ khóa trong trang
        - Ví dụ: Tìm "Metformin" trong trang Thuốc
        
        **4. Screenshot để lưu lại**
        - Windows: Win + Shift + S
        - Mac: Cmd + Shift + 4
        - Lưu thông tin quan trọng!
        
        **5. In PDF nếu cần**
        - Ctrl+P → Save as PDF
        - Có thể đưa cho bác sĩ xem
        """)
    
    with col2:
        st.subheader("🎯 Mẹo Chuyên sâu")
        st.markdown("""
        **Cho bệnh nhân Tăng huyết áp:**
        - Vào "❤️ Tim Mạch" → Tab "Dinh dưỡng"
        - Đọc phần **"Giảm muối"**
        - Screenshot danh sách thực phẩm tránh
        - Dán lên tủ lạnh! 😊
        
        **Cho bệnh nhân Tiểu đường:**
        - Vào "🩸 Tiểu Đường" → Tab "Ăn uống"
        - Đọc **bảng GI/GL 60+ món VN**
        - Screenshot → Mang theo khi đi chợ/ăn quán!
        
        **Cho người chăm sóc:**
        - Học **BE-FAST** ở trang "🧠 Thần Kinh"
        - Screenshot → Dán lên tường
        - Biết dấu hiệu → Cứu mạng người thân!
        
        **Dùng AI Bác Sĩ hiệu quả:**
        - Hỏi cụ thể, chi tiết
        - Ví dụ: "Huyết áp 145/95, 55 tuổi, có tiểu đường, nên làm gì?"
        - Càng chi tiết → AI tư vấn càng chính xác!
        """)
    
    st.divider()
    
    st.success("🎉 **Chúc bạn sử dụng HealthAdvisor hiệu quả!**")
    st.info("💬 Có thắc mắc? Hỏi ngay **🤖 AI Bác Sĩ** bất kỳ lúc nào!")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>📧 Góp ý? Liên hệ: <a href='https://github.com/drvietcanh/healthadvisor'>GitHub</a></p>
    <p>Made with ❤️ for Vietnamese Healthcare</p>
</div>
""", unsafe_allow_html=True)

