"""
Học Dễ Page - Comparisons Tab
Tab So sánh
"""

import streamlit as st
from core.simple_explanations import COMPARISONS


def render_comparisons_tab():
    """Render tab So sánh"""
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

