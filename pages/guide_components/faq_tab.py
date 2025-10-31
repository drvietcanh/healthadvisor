"""
FAQ Tab - Tab Câu hỏi thường gặp
"""
import streamlit as st


def render_faq_tab():
    """Render tab FAQ"""
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

