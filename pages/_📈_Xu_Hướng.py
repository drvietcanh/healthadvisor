"""
Trang Phân tích Xu hướng Sức khỏe
Phân tích dữ liệu từ Nhật ký, đưa ra cảnh báo và gợi ý
"""
import streamlit as st
import sys
import os
from datetime import datetime, timedelta

# Thêm thư mục gốc vào path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from health_trends import (
    analyze_blood_pressure_trend,
    analyze_blood_sugar_trend,
    analyze_weight_trend,
    get_overall_health_score,
    check_bp_alerts,
    check_bs_alerts,
    check_weight_alerts,
    generate_recommendations,
)
from diary_components.data_manager import load_csv_data
from core.ui_config import get_custom_css
from health_trends_page_components import (
    render_overview_tab,
    render_blood_pressure_tab,
    render_blood_sugar_tab,
    render_weight_tab,
    render_correlation_tab,
    render_recommendations_section
)

st.set_page_config(
    page_title="Xu Hướng Sức Khỏe",
    page_icon="📈",
    layout="wide"
)

# Áp dụng Dark Mode
try:
    if 'dark_mode' not in st.session_state:
        st.session_state.dark_mode = False
    if 'extra_large_font' not in st.session_state:
        st.session_state.extra_large_font = False
    css_content = get_custom_css(dark_mode=st.session_state.dark_mode, extra_large_font=st.session_state.extra_large_font)
    if css_content:
        st.markdown(css_content, unsafe_allow_html=True)
except Exception:
    # Nếu có lỗi, bỏ qua CSS - app vẫn chạy được
    pass

# Header
st.title("📈 Phân tích Xu hướng Sức khỏe")

st.markdown("""
<div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            padding: 25px; border-radius: 15px; color: white; margin-bottom: 25px;'>
    <h3 style='margin:0; color: white;'>💡 Phân tích Thông minh</h3>
    <p style='margin: 10px 0 0 0; font-size: 18px;'>
        Dựa trên dữ liệu từ Nhật ký của bạn, chúng tôi phân tích xu hướng, 
        phát hiện vấn đề sớm và đưa ra gợi ý cải thiện.
    </p>
</div>
""", unsafe_allow_html=True)

# Đọc dữ liệu từ Nhật ký
df = load_csv_data()

if df is None or len(df) == 0:
    st.warning("""
    ### 📝 Chưa có dữ liệu để phân tích
    
    Bạn cần nhập dữ liệu ở trang **📊 Nhật Ký** trước.
    
    **Cần ít nhất:**
    - 7 ngày dữ liệu để phân tích xu hướng ngắn hạn
    - 30 ngày dữ liệu để phân tích chi tiết
    
    💡 Càng nhiều dữ liệu, phân tích càng chính xác!
    """)
    
    if st.button("➡️ Đi đến Nhật Ký", use_container_width=True):
        st.switch_page("pages/_📊_Nhật_Ký.py")
    
    st.stop()

# Kiểm tra số lượng dữ liệu
data_count = len(df)
st.info(f"📊 Đang phân tích **{data_count} bản ghi** từ Nhật ký của bạn")

# Chọn khoảng thời gian phân tích
col_period1, col_period2 = st.columns([3, 1])

with col_period1:
    analysis_days = st.select_slider(
        "Phân tích",
        options=[7, 14, 30, 60, 90],
        value=30,
        format_func=lambda x: f"{x} ngày gần nhất"
    )

with col_period2:
    if st.button("🔄 Làm mới phân tích"):
        st.rerun()

st.divider()

# Phân tích dữ liệu
with st.spinner("🔍 Đang phân tích dữ liệu..."):
    bp_analysis = analyze_blood_pressure_trend(df, days=analysis_days)
    bs_analysis = analyze_blood_sugar_trend(df, days=analysis_days)
    weight_analysis = analyze_weight_trend(df, days=analysis_days)
    
    # Điểm sức khỏe tổng thể
    overall = get_overall_health_score(bp_analysis, bs_analysis, weight_analysis)
    
    # Cảnh báo
    bp_alerts = check_bp_alerts(bp_analysis)
    bs_alerts = check_bs_alerts(bs_analysis)
    weight_alerts = check_weight_alerts(weight_analysis)
    all_alerts = bp_alerts + bs_alerts + weight_alerts
    
    # Gợi ý
    recommendations = generate_recommendations(bp_analysis, bs_analysis, weight_analysis, overall)

# Overview Tab
render_overview_tab(bp_analysis, bs_analysis, weight_analysis, overall, all_alerts)

# =============== XU HƯỚNG CHI TIẾT ===============
st.header("📊 Xu hướng Chi tiết")

tab1, tab2, tab3, tab4 = st.tabs([
    "❤️ Huyết áp",
    "🩸 Đường huyết",
    "⚖️ Cân nặng",
    "🔗 Mối liên hệ"
])

# TAB 1: HUYẾT ÁP
with tab1:
    render_blood_pressure_tab(bp_analysis, df, analysis_days)

# TAB 2: ĐƯỜNG HUYẾT
with tab2:
    render_blood_sugar_tab(bs_analysis, df, analysis_days)

# TAB 3: CÂN NẶNG
with tab3:
    render_weight_tab(weight_analysis, df, analysis_days)

# TAB 4: MỐI LIÊN HỆ
with tab4:
    render_correlation_tab(df)

st.divider()

# Gợi ý
render_recommendations_section(recommendations)

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p><b>💡 Lưu ý:</b> Phân tích này chỉ mang tính tham khảo. 
    Vui lòng tham khảo ý kiến bác sĩ cho chẩn đoán và điều trị chính xác.</p>
</div>
""", unsafe_allow_html=True)

if st.button("⬅️ Quay lại trang chính", use_container_width=True):
    st.switch_page("app.py")
