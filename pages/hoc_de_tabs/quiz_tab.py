"""
Học Dễ Page - Quiz Tab
Tab Trắc nghiệm
"""

import streamlit as st


def render_quiz_tab():
    """Render tab Trắc nghiệm"""
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

