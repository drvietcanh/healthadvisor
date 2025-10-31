"""
Tips Tab - Tab Mẹo & Thủ thuật
"""
import streamlit as st


def render_tips_tab():
    """Render tab Mẹo & Thủ thuật"""
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

