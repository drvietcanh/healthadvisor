"""
Trang HỌC DỄ - Giải thích bằng hình ảnh, ví dụ đời thường
"""
import streamlit as st
import sys
sys.path.append('..')

from core.simple_explanations import EVERYDAY_EXAMPLES, MEMORY_TRICKS, COMPARISONS
from core.ui_config import get_custom_css
from core.sidebar_menu import render_sidebar_menu, hide_default_nav

st.set_page_config(page_title="Học Dễ", page_icon="🎓", layout="wide")

# Ẩn menu mặc định của Streamlit - PHẢI GỌI TRƯỚC
hide_default_nav()

# Render menu sidebar tùy chỉnh
render_sidebar_menu()


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

st.title("🎓 Học Y Khoa Siêu Dễ!")
st.markdown("### Giải thích bằng hình ảnh - Ai cũng hiểu! 😊")

# Tabs
tabs = st.tabs([
    "💡 Giải Thích Đơn Giản",
    "🧠 Mẹo Nhớ",
    "📏 So Sánh",
    "🎮 Trắc Nghiệm"
])

# ============= TAB 1: GIẢI THÍCH ĐƠN GIẢN =============
with tabs[0]:
    st.header("💡 Giải thích bệnh bằng ví dụ đời thường")
    
    topic = st.selectbox(
        "Chọn chủ đề muốn tìm hiểu:",
        [
            "💓 Huyết áp cao là gì?",
            "🍬 Tiểu đường là gì?",
            "💔 Suy tim là gì?",
            "🧠 Đột quỵ là gì?"
        ]
    )
    
    topic_map = {
        "💓 Huyết áp cao là gì?": "blood_pressure",
        "🍬 Tiểu đường là gì?": "diabetes",
        "💔 Suy tim là gì?": "heart_failure",
        "🧠 Đột quỵ là gì?": "stroke"
    }
    
    selected_topic = topic_map[topic]
    
    # Hiển thị giải thích
    st.markdown(EVERYDAY_EXAMPLES[selected_topic]["simple_vn"])
    
    # Hiển thị visual
    if "visual" in EVERYDAY_EXAMPLES[selected_topic]:
        st.code(EVERYDAY_EXAMPLES[selected_topic]["visual"], language="")
    
    st.divider()
    
    # Video giải thích (giả lập)
    st.info("💡 **MẸO HỌC:** Đọc lại 3 lần → Kể lại cho người thân → Nhớ lâu!")

# ============= TAB 2: MẸO NHỚ =============
with tabs[1]:
    st.header("🧠 Mẹo nhớ siêu dễ")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Nhớ BE-FAST")
        st.markdown(MEMORY_TRICKS["befast_easy"])
        
        # Test ngay
        if st.button("🎮 Test ngay!", key="test_befast"):
            st.success("""
**HÃY THỬ NGAY:**

1. **CƯỜI** → Xem gương → Lệch miệng không?
2. **GIƠ 2 TAY** → 1 tay sa xuống không?
3. **NÓI**: "Hôm nay trời đẹp" → Nói rõ không?

✅ Tất cả OK = Bình thường
❌ Có 1 dấu hiệu = GỌI 115!
""")
    
    with col2:
        st.subheader("📊 Nhớ đường huyết")
        st.markdown(MEMORY_TRICKS["blood_sugar_levels"])
        
        # Quiz
        if st.button("❓ Câu hỏi kiểm tra", key="quiz_sugar"):
            st.info("""
**Đường huyết đói 6.5 mmol/L là gì?**

A. Bình thường ✅
B. Tiền tiểu đường ⚠️
C. Tiểu đường 🔴

**Đáp án:** B - Tiền tiểu đường (6 nằm giữa 5 và 7!)
""")
    
    st.divider()
    
    st.subheader("🧂 Mẹo giảm muối")
    st.markdown(MEMORY_TRICKS["salt_reduction"])

# ============= TAB 3: SO SÁNH =============
with tabs[2]:
    st.header("📏 So sánh để dễ hiểu")
    
    # Thuốc giống như gì?
    st.subheader(COMPARISONS["medications_simple"]["title"])
    
    for med in COMPARISONS["medications_simple"]["examples"]:
        with st.expander(f"{med['emoji']} {med['drug']}", expanded=False):
            st.markdown(f"### {med['like']}")
            st.markdown(med['explain'])
            
            # Visual
            if med['drug'] == "Thuốc lợi tiểu":
                st.code("""
┌─────────────────────┐
│  TRƯỚC UỐNG THUỐC  │
│  Cơ thể: 💧💧💧💧   │
│  Áp lực: Cao ⬆️     │
└─────────────────────┘
        ↓
    Uống thuốc 💊
        ↓
┌─────────────────────┐
│   SAU UỐNG THUỐC   │
│  Đi tiểu: 🚽💦💦   │
│  Cơ thể: 💧💧      │
│  Áp lực: Giảm ⬇️    │
└─────────────────────┘
""", language="")
    
    st.divider()
    
    # Khẩu phần ăn
    st.subheader(COMPARISONS["portion_sizes"]["title"])
    
    for portion in COMPARISONS["portion_sizes"]["examples"]:
        st.markdown(f"- {portion}")
    
    # Tool so sánh
    st.divider()
    st.subheader("🎯 Công cụ so sánh")
    
    calc_type = st.radio(
        "Bạn muốn so sánh gì?",
        ["Huyết áp", "Đường huyết", "Muối trong món ăn"]
    )
    
    if calc_type == "Huyết áp":
        bp = st.slider("Huyết áp của bạn (mmHg):", 80, 200, 120)
        
        if bp < 120:
            st.success(f"**{bp} mmHg** = Như áp lực bơm tay bóng đá 🏀 - Bình thường!")
        elif bp < 140:
            st.warning(f"**{bp} mmHg** = Như áp lực bơm hơi xe đạp 🚲 - Hơi cao!")
        elif bp < 160:
            st.error(f"**{bp} mmHg** = Như áp lực bơm hơi xe máy 🏍️ - Cao!")
        else:
            st.error(f"**{bp} mmHg** = Như nồi áp suất đang sôi 🍲 - RẤT NGUY HIỂM!")
    
    elif calc_type == "Đường huyết":
        sugar = st.slider("Đường huyết (mg/dL):", 50, 400, 100)
        sugar_mmol = round(sugar / 18, 1)
        
        # So sánh với thìa đường
        spoons = round(sugar / 100, 1)
        
        st.info(f"**{sugar} mg/dL** = **{sugar_mmol} mmol/L**")
        st.info(f"Tương đương **{spoons} thìa cà phê đường** trong máu")
        
        if sugar < 100:
            st.success("✅ Bình thường!")
        elif sugar < 140:
            st.warning("⚠️ Hơi cao!")
        else:
            st.error("🔴 Cao - Cần điều trị!")
    
    else:  # Muối
        salt_source = st.selectbox(
            "Món ăn/Thực phẩm:",
            [
                "1 bát phở",
                "1 gói mì gói",
                "1 thìa nước mắm",
                "1 miếng chả lụa",
                "1 bát cơm nhà (nấu nhạt)"
            ]
        )
        
        salt_map = {
            "1 bát phở": 3.5,
            "1 gói mì gói": 4.0,
            "1 thìa nước mắm": 2.5,
            "1 miếng chả lụa": 1.5,
            "1 bát cơm nhà (nấu nhạt)": 0.5
        }
        
        salt_g = salt_map[salt_source]
        percent_of_limit = round(salt_g / 3 * 100)
        
        st.metric(
            f"Lượng muối trong {salt_source}",
            f"{salt_g}g",
            f"{percent_of_limit}% giới hạn ngày (THA)"
        )
        
        if salt_g > 3:
            st.error(f"🚫 QUÁ MẶN! Vượt giới hạn người tăng huyết áp!")
        elif salt_g > 2:
            st.warning(f"⚠️ Khá mặn! Nên giảm bớt.")
        else:
            st.success(f"✅ OK! Trong giới hạn.")

# ============= TAB 4: TRẮC NGHIỆM =============
with tabs[3]:
    st.header("🎮 Trắc nghiệm kiến thức")
    
    st.info("Kiểm tra xem bạn đã hiểu chưa! 😊")
    
    # Quiz 1
    st.subheader("Câu 1: Huyết áp là gì?")
    q1 = st.radio(
        "",
        [
            "A. Nhiệt độ của máu",
            "B. Áp lực máu trong mạch",
            "C. Tốc độ tim đập",
            "D. Lượng máu trong cơ thể"
        ],
        key="q1"
    )
    
    if st.button("Kiểm tra câu 1"):
        if "B" in q1:
            st.success("✅ ĐÚNG! Huyết áp = Áp lực máu, giống như áp lực nước trong ống!")
        else:
            st.error("❌ SAI! Huyết áp = Áp lực máu trong mạch nhé!")
    
    st.divider()
    
    # Quiz 2
    st.subheader("Câu 2: Insulin giống như gì?")
    q2 = st.radio(
        "",
        [
            "A. Chìa khóa mở cửa",
            "B. Cái bơm nước",
            "C. Cái quạt",
            "D. Cái đèn"
        ],
        key="q2"
    )
    
    if st.button("Kiểm tra câu 2"):
        if "A" in q2:
            st.success("✅ ĐÚNG! Insulin = Chìa khóa mở cửa tế bào cho đường vào!")
        else:
            st.error("❌ SAI! Insulin như chìa khóa, mở cửa tế bào!")
    
    st.divider()
    
    # Quiz 3
    st.subheader("Câu 3: Nhớ BE-FAST - S là gì?")
    q3 = st.radio(
        "",
        [
            "A. Sleeping (Ngủ)",
            "B. Speech (Nói khó)",
            "C. Strong (Khỏe)",
            "D. Sad (Buồn)"
        ],
        key="q3"
    )
    
    if st.button("Kiểm tra câu 3"):
        if "B" in q3:
            st.success("✅ ĐÚNG! S = Speech (Nói khó) - Dấu hiệu đột quỵ!")
        else:
            st.error("❌ SAI! S = Speech (Nói khó, nói lắp)")
    
    st.divider()
    
    score_section = st.container()
    with score_section:
        if st.button("📊 Xem điểm tổng", type="primary"):
            st.balloons()
            st.success("""
🎉 **CHÚC MỪNG!**

Bạn đã học xong phần cơ bản!

**GHI NHỚ:**
- Huyết áp = Áp lực máu
- Insulin = Chìa khóa
- BE-FAST = Nhận biết đột quỵ
- Số càng cao = Càng nguy hiểm

👉 Tiếp tục học thêm ở các trang khác!
""")

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; padding: 1rem;">
    💡 <b>MẸO HỌC HIỆU QUẢ:</b><br>
    1. Đọc → 2. Xem hình → 3. Kể lại → 4. Làm quiz → 5. Nhớ lâu!
</div>
""", unsafe_allow_html=True)

if st.button("⬅️ Quay lại trang chính"):
    st.switch_page("app.py")

