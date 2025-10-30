"""
Trang Chatbot AI - Trò chuyện tư vấn y tế
"""
import streamlit as st
import sys
sys.path.append('..')

from core.chatbot import HealthChatbot
import os

st.set_page_config(page_title="AI Bác Sĩ", page_icon="🤖", layout="wide")

st.title("🤖 AI Bác Sĩ - Trợ lý sức khỏe thông minh")

# Khởi tạo session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chatbot" not in st.session_state:
    st.session_state.chatbot = None
if "disease_selected" not in st.session_state:
    st.session_state.disease_selected = False

# Sidebar - Chọn chuyên khoa
with st.sidebar:
    st.header("⚙️ Cài đặt")
    
    # Chọn chuyên khoa
    disease_type = st.selectbox(
        "Chọn chuyên khoa:",
        ["general", "cardiovascular", "diabetes", "neurological"],
        format_func=lambda x: {
            "general": "🏥 Tổng quát",
            "cardiovascular": "❤️ Tim mạch",
            "diabetes": "🩸 Tiểu đường",
            "neurological": "🧠 Thần kinh"
        }[x],
        key="disease_selector"
    )
    
    # Kiểm tra API key
    has_api_key = bool(os.getenv("OPENAI_API_KEY"))
    
    if has_api_key:
        st.success("✅ AI đã sẵn sàng")
        use_ai = st.checkbox("Sử dụng AI", value=True, help="Bật/tắt AI (cần API key)")
    else:
        st.warning("⚠️ Chưa có API key OpenAI")
        st.info("Để dùng AI, thêm OPENAI_API_KEY vào file `.streamlit/secrets.toml`")
        use_ai = False
    
    # Nút reset
    if st.button("🔄 Bắt đầu cuộc trò chuyện mới", use_container_width=True):
        st.session_state.messages = []
        st.session_state.chatbot = None
        st.session_state.disease_selected = False
        st.rerun()
    
    st.divider()
    
    # Hướng dẫn
    with st.expander("📖 Hướng dẫn sử dụng"):
        st.markdown("""
**AI Bác sĩ có thể:**
- Trả lời câu hỏi về bệnh
- Tư vấn chế độ ăn, vận động
- Giải thích thuốc điều trị
- Hướng dẫn theo dõi tại nhà

**Lưu ý:**
- Chỉ tham khảo, không thay thế bác sĩ
- Không tự ý chẩn đoán/dùng thuốc
- Triệu chứng cấp cứu → GỌI 115
""")
    
    # Ví dụ câu hỏi
    with st.expander("💡 Gợi ý câu hỏi"):
        st.markdown("""
**Tim mạch:**
- Huyết áp bao nhiêu là bình thường?
- Ăn gì để giảm huyết áp?
- Thuốc huyết áp có tác dụng phụ gì?

**Tiểu đường:**
- Đường huyết 8 mmol/L có cao không?
- Cách tính carb trong bữa ăn?
- Hạ đường huyết xử trí thế nào?

**Thần kinh:**
- Làm sao nhận biết đột quỵ?
- Phòng ngừa đột quỵ như thế nào?
""")

# Main content
st.markdown("""
<div style="background-color: #f0f8ff; padding: 1rem; border-radius: 10px; border-left: 5px solid #1f77b4;">
    <b>👋 Chào bạn!</b> Tôi là AI Bác sĩ, trợ lý sức khỏe của bạn.<br>
    Hãy hỏi tôi bất kỳ điều gì về sức khỏe nhé! 😊
</div>
""", unsafe_allow_html=True)

st.divider()

# Hiển thị lịch sử trò chuyện
for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    
    if role == "user":
        with st.chat_message("user", avatar="👤"):
            st.markdown(content)
    else:
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(content)

# Input từ người dùng
user_input = st.chat_input("Hỏi gì đó... (ví dụ: Huyết áp bao nhiêu là bình thường?)")

if user_input:
    # Khởi tạo chatbot nếu chưa có
    if st.session_state.chatbot is None:
        st.session_state.chatbot = HealthChatbot(disease_type=disease_type)
    
    # Hiển thị tin nhắn người dùng
    with st.chat_message("user", avatar="👤"):
        st.markdown(user_input)
    
    # Thêm vào lịch sử
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Lấy phản hồi từ chatbot
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Đang suy nghĩ..."):
            response = st.session_state.chatbot.get_response(user_input, use_ai=use_ai)
            st.markdown(response)
    
    # Thêm phản hồi vào lịch sử
    st.session_state.messages.append({"role": "assistant", "content": response})

# Nếu chưa có tin nhắn, hiển thị gợi ý
if len(st.session_state.messages) == 0:
    st.markdown("### 💬 Bắt đầu trò chuyện bằng cách nhập câu hỏi bên dưới!")
    
    # Quick buttons
    st.markdown("**Hoặc chọn chủ đề:**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("❤️ Huyết áp cao", use_container_width=True):
            user_input = "Tôi muốn biết về tăng huyết áp"
            st.rerun()
    
    with col2:
        if st.button("🩸 Tiểu đường", use_container_width=True):
            user_input = "Tôi muốn biết về bệnh tiểu đường"
            st.rerun()
    
    with col3:
        if st.button("🧠 Đột quỵ", use_container_width=True):
            user_input = "Làm sao nhận biết đột quỵ?"
            st.rerun()

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #888;">
    <small>
    ⚠️ <b>Lưu ý:</b> AI Bác sĩ chỉ cung cấp thông tin tham khảo, không thay thế bác sĩ thật.<br>
    Với triệu chứng nghiêm trọng, vui lòng <b>GỌI 115</b> hoặc đến bệnh viện ngay.
    </small>
</div>
""", unsafe_allow_html=True)

# Nút quay lại
if st.button("⬅️ Quay lại trang chính"):
    st.switch_page("app.py")

