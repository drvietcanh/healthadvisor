"""
Trang Chatbot AI - Trò chuyện tư vấn y tế
"""
import streamlit as st
import sys
sys.path.append('..')

from core.chatbot_enhanced import MedicalChatbot
import os

st.set_page_config(page_title="AI Bác Sĩ", page_icon="🤖", layout="wide")

st.title("🤖 AI Bác Sĩ - Trợ lý sức khỏe thông minh")

# Khởi tạo session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chatbot" not in st.session_state:
    st.session_state.chatbot = MedicalChatbot()
if "current_context" not in st.session_state:
    st.session_state.current_context = "general"
if "show_welcome" not in st.session_state:
    st.session_state.show_welcome = True

# Sidebar - Cài đặt AI
with st.sidebar:
    st.header("⚙️ Cài đặt AI")
    
    # Chọn AI Provider
    st.subheader("1️⃣ Chọn AI Provider")
    provider = st.radio(
        "Chọn nhà cung cấp AI:",
        ["gemini", "openai"],
        format_func=lambda x: {
            "gemini": "🌟 Gemini (Google) - MIỄN PHÍ!",
            "openai": "🤖 OpenAI (ChatGPT) - Trả phí"
        }[x],
        key="ai_provider"
    )
    
    # Nhập API Key
    st.subheader("2️⃣ Nhập API Key")
    
    if provider == "gemini":
        st.info("💡 **Lấy Gemini API miễn phí:**\n\n1. Vào https://aistudio.google.com/app/apikey\n2. Đăng nhập Gmail\n3. Click 'Create API key'\n4. Copy và dán vào đây")
        
        # Kiểm tra API key từ secrets hoặc env
        gemini_key_from_secrets = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY", ""))
        
        if gemini_key_from_secrets:
            st.success("✅ Đã có API key từ Secrets")
            api_key = gemini_key_from_secrets
            use_ai = True
        else:
            api_key = st.text_input(
                "Gemini API Key:",
                type="password",
                placeholder="AIzaSy...",
                help="Dán API key vừa lấy từ Google AI Studio"
            )
            
            if api_key:
                st.success("✅ API key đã nhập!")
                use_ai = True
            else:
                st.warning("⚠️ Chưa có API key - Chỉ dùng câu trả lời mẫu")
                use_ai = False
                
    else:  # OpenAI
        st.info("💰 **Lấy OpenAI API key (trả phí):**\n\n1. Vào https://platform.openai.com/api-keys\n2. Đăng nhập\n3. Click 'Create new secret key'\n4. Copy và dán vào đây")
        
        # Kiểm tra API key từ secrets hoặc env
        openai_key_from_secrets = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY", ""))
        
        if openai_key_from_secrets:
            st.success("✅ Đã có API key từ Secrets")
            api_key = openai_key_from_secrets
            use_ai = True
        else:
            api_key = st.text_input(
                "OpenAI API Key:",
                type="password",
                placeholder="sk-...",
                help="Dán API key từ OpenAI Platform"
            )
            
            if api_key:
                st.success("✅ API key đã nhập!")
                use_ai = True
            else:
                st.warning("⚠️ Chưa có API key - Chỉ dùng câu trả lời mẫu")
                use_ai = False
    
    st.divider()
    
    # Chọn chuyên khoa
    st.subheader("3️⃣ Chọn chuyên khoa")
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
    
    # Nút reset
    if st.button("🔄 Bắt đầu cuộc trò chuyện mới", use_container_width=True):
        st.session_state.messages = []
        st.session_state.chatbot = MedicalChatbot()
        st.session_state.current_context = "general"
        st.session_state.show_welcome = True
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
# Hiển thị welcome message lần đầu
if st.session_state.show_welcome and len(st.session_state.messages) == 0:
    welcome_msg = st.session_state.chatbot.get_welcome_message()
    st.markdown(welcome_msg)
    st.session_state.show_welcome = False
    
    # Hiển thị câu hỏi gợi ý đầu tiên
    st.markdown("### 💬 Câu hỏi phổ biến:")
    suggestions = st.session_state.chatbot.get_suggested_questions("general")
    
    cols = st.columns(2)
    for idx, suggestion in enumerate(suggestions[:4]):  # Hiển thị 4 câu đầu
        col_idx = idx % 2
        with cols[col_idx]:
            if st.button(f"❓ {suggestion}", key=f"quick_{idx}", use_container_width=True):
                # Tự động gửi câu hỏi này
                st.session_state.messages.append({"role": "user", "content": suggestion})
                response, context, new_suggestions = st.session_state.chatbot.generate_response(
                    suggestion, 
                    use_ai=use_ai,
                    provider=provider,
                    api_key=api_key if use_ai else None
                )
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.session_state.current_context = context
                st.rerun()

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
    # Hiển thị tin nhắn người dùng
    with st.chat_message("user", avatar="👤"):
        st.markdown(user_input)
    
    # Thêm vào lịch sử
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Lấy phản hồi từ chatbot
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Đang suy nghĩ..."):
            response, context, suggestions = st.session_state.chatbot.generate_response(
                user_input, 
                use_ai=use_ai,
                provider=provider,
                api_key=api_key if use_ai else None
            )
            st.markdown(response)
            
            # Hiển thị câu hỏi gợi ý tiếp theo
            if suggestions:
                st.markdown("---")
                st.markdown("**💡 Câu hỏi tiếp theo:**")
                cols = st.columns(2)
                for idx, suggestion in enumerate(suggestions[:4]):
                    col_idx = idx % 2
                    with cols[col_idx]:
                        st.button(
                            f"❓ {suggestion}", 
                            key=f"suggest_{len(st.session_state.messages)}_{idx}",
                            on_click=lambda s=suggestion: st.session_state.messages.append({"role": "temp", "content": s})
                        )
    
    # Thêm phản hồi vào lịch sử
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.session_state.current_context = context

# Hiển thị gợi ý dựa trên context hiện tại
if len(st.session_state.messages) > 0:
    # Lấy câu hỏi gợi ý theo context
    current_suggestions = st.session_state.chatbot.get_suggested_questions(
        st.session_state.current_context
    )
    
    if current_suggestions:
        st.markdown("---")
        st.markdown("### 💡 Câu hỏi liên quan:")
        
        cols = st.columns(2)
        for idx, suggestion in enumerate(current_suggestions[:4]):
            col_idx = idx % 2
            with cols[col_idx]:
                if st.button(
                    f"❓ {suggestion}", 
                    key=f"bottom_suggest_{idx}",
                    use_container_width=True
                ):
                    # Tự động điền vào input
                    st.session_state.temp_question = suggestion
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

