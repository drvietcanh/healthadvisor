"""
Quick Start Tab - Tab Bắt đầu nhanh
"""
import streamlit as st


def render_quick_start_tab():
    """Render tab Bắt đầu nhanh"""
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

