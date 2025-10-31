"""
Detailed Guide Tab - Tab Hướng dẫn chi tiết
"""
import streamlit as st


def render_detailed_guide_tab():
    """Render tab Hướng dẫn chi tiết"""
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

