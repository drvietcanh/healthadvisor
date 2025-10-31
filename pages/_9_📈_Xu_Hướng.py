"""
Trang Phân tích Xu hướng Sức khỏe
Phân tích dữ liệu từ Nhật ký, đưa ra cảnh báo và gợi ý
"""
import streamlit as st
import pandas as pd
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
    create_trend_chart,
    create_comparison_chart,
    create_correlation_chart
)
from diary_components.data_manager import load_csv_data
from core.ui_config import get_custom_css

st.set_page_config(
    page_title="Xu Hướng Sức Khỏe",
    page_icon="📈",
    layout="wide"
)

# Áp dụng Dark Mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)

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
        st.switch_page("pages/6_📊_Nhật_Ký.py")
    
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

# =============== ĐIỂM SỨC KHỎE TỔNG THỂ ===============
st.header("🎯 Điểm Sức khỏe Tổng thể")

col_score1, col_score2, col_score3 = st.columns([2, 2, 3])

with col_score1:
    # Điểm số lớn
    st.markdown(f"""
    <div style='text-align: center; padding: 30px; 
                background: linear-gradient(135deg, #{overall['color']}44 0%, #{overall['color']}22 100%);
                border-radius: 15px; border: 3px solid {overall['color']};'>
        <h1 style='font-size: 72px; margin: 0; color: {overall['color']};'>
            {overall['score']}
        </h1>
        <p style='font-size: 24px; margin: 10px 0 0 0;'>/ 100 điểm</p>
    </div>
    """, unsafe_allow_html=True)

with col_score2:
    st.markdown(f"""
    <div style='text-align: center; padding: 30px;'>
        <p style='font-size: 64px; margin: 0;'>{overall['emoji']}</p>
        <h2 style='margin: 10px 0;'>{overall['rating']}</h2>
    </div>
    """, unsafe_allow_html=True)

with col_score3:
    st.markdown("### 📊 Phân tích:")
    if overall['positive_trends'] > 0:
        st.success(f"✅ {overall['positive_trends']} chỉ số đang cải thiện")
    if overall['negative_trends'] > 0:
        st.warning(f"⚠️ {overall['negative_trends']} chỉ số đang xấu đi")
    
    if overall['issues']:
        st.markdown("**Vấn đề cần chú ý:**")
        for issue in overall['issues'][:3]:  # Hiển thị tối đa 3
            st.markdown(f"- {issue}")

st.divider()

# =============== CẢNH BÁO ===============
if all_alerts:
    st.header("🚨 Cảnh báo")
    
    for alert in all_alerts[:5]:  # Hiển thị tối đa 5 cảnh báo
        if alert['type'] == 'danger':
            st.error(f"### {alert['title']}\n{alert['message']}")
        elif alert['type'] == 'warning':
            st.warning(f"### {alert['title']}\n{alert['message']}")
        else:
            st.info(f"### {alert['title']}\n{alert['message']}")
    
    st.divider()

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
    if bp_analysis:
        # Thông tin tổng quan
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Huyết áp trung bình",
                f"{bp_analysis['avg_systolic']}/{bp_analysis['avg_diastolic']}",
                delta=f"{bp_analysis['systolic_trend']['change_percent']}%"
            )
        
        with col2:
            st.metric(
                "Phân loại",
                bp_analysis['category']
            )
        
        with col3:
            trend_emoji = {"increasing": "📈", "decreasing": "📉", "stable": "➡️"}
            st.metric(
                "Xu hướng 7 ngày",
                trend_emoji.get(bp_analysis['systolic_trend']['trend'], "➡️") + 
                " " + bp_analysis['systolic_trend']['trend'].capitalize()
            )
        
        # Biểu đồ xu hướng huyết áp tâm thu
        df_filtered = df[df['Ngày'] >= (datetime.now() - timedelta(days=analysis_days))]
        df_filtered = df_filtered.sort_values('Ngày')
        
        if len(df_filtered) > 0:
            fig_bp = create_trend_chart(
                df_filtered[df_filtered['Huyết áp tâm thu'].notna()],
                'Huyết áp tâm thu',
                'Xu hướng Huyết áp Tâm thu',
                'mmHg',
                reference_lines={
                    'Bình thường': (120, 'normal'),
                    'Cao': (140, 'danger')
                }
            )
            st.plotly_chart(fig_bp, use_container_width=True)
            
            # Biểu đồ tâm trương
            fig_bp_dia = create_trend_chart(
                df_filtered[df_filtered['Huyết áp tâm trương'].notna()],
                'Huyết áp tâm trương',
                'Xu hướng Huyết áp Tâm trương',
                'mmHg',
                reference_lines={
                    'Bình thường': (80, 'normal'),
                    'Cao': (90, 'danger')
                }
            )
            st.plotly_chart(fig_bp_dia, use_container_width=True)
    else:
        st.info("📝 Chưa có đủ dữ liệu huyết áp để phân tích")

# TAB 2: ĐƯỜNG HUYẾT
with tab2:
    if bs_analysis:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Đường huyết TB",
                f"{bs_analysis['avg']} mmol/L",
                delta=f"{bs_analysis['trend']['change_percent']}%"
            )
        
        with col2:
            st.metric(
                "Phân loại",
                bs_analysis['category']
            )
        
        with col3:
            if bs_analysis['low_count'] > 0:
                st.metric("⚠️ Hạ đường huyết", f"{bs_analysis['low_count']} lần")
            else:
                st.metric("Cao (>7.0)", f"{bs_analysis['high_count']} lần")
        
        # Biểu đồ
        df_filtered = df[df['Ngày'] >= (datetime.now() - timedelta(days=analysis_days))]
        df_filtered = df_filtered.sort_values('Ngày')
        
        if len(df_filtered) > 0 and 'Đường huyết' in df_filtered.columns:
            fig_bs = create_trend_chart(
                df_filtered[df_filtered['Đường huyết'].notna()],
                'Đường huyết',
                'Xu hướng Đường huyết',
                'mmol/L',
                reference_lines={
                    'Bình thường': (5.6, 'normal'),
                    'Tiền ĐTĐ': (7.0, 'warning'),
                    'Hạ': (3.9, 'danger')
                }
            )
            st.plotly_chart(fig_bs, use_container_width=True)
    else:
        st.info("📝 Chưa có đủ dữ liệu đường huyết để phân tích")

# TAB 3: CÂN NẶNG
with tab3:
    if weight_analysis:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Cân nặng hiện tại",
                f"{weight_analysis['current']} kg"
            )
        
        with col2:
            st.metric(
                "Thay đổi",
                f"{weight_analysis['change']:+.1f} kg",
                delta=weight_analysis['message']
            )
        
        with col3:
            st.metric(
                "Trung bình",
                f"{weight_analysis['avg']} kg"
            )
        
        # Biểu đồ
        df_filtered = df[df['Ngày'] >= (datetime.now() - timedelta(days=analysis_days))]
        df_filtered = df_filtered.sort_values('Ngày')
        
        if len(df_filtered) > 0 and 'Cân nặng (kg)' in df_filtered.columns:
            fig_weight = create_trend_chart(
                df_filtered[df_filtered['Cân nặng (kg)'].notna()],
                'Cân nặng (kg)',
                'Xu hướng Cân nặng',
                'kg'
            )
            st.plotly_chart(fig_weight, use_container_width=True)
    else:
        st.info("📝 Chưa có đủ dữ liệu cân nặng để phân tích")

# TAB 4: MỐI LIÊN HỆ
with tab4:
    st.markdown("### 🔗 Mối liên hệ giữa các chỉ số")
    st.info("💡 Cân nặng và huyết áp thường có mối liên hệ với nhau. Giảm cân có thể giúp giảm huyết áp.")
    
    fig_corr = create_correlation_chart(df)
    
    if fig_corr:
        st.plotly_chart(fig_corr, use_container_width=True)
        
        # Giải thích
        st.markdown("""
        **Cách đọc biểu đồ:**
        - Mỗi điểm = 1 lần đo
        - Màu đỏ = Huyết áp cao
        - Màu vàng/xanh = Huyết áp tốt hơn
        - Nếu điểm tập trung theo đường chéo lên → Cân nặng tăng, huyết áp cũng tăng
        """)
    else:
        st.info("📝 Cần thêm dữ liệu để phân tích mối liên hệ")

st.divider()

# =============== GỢI Ý THÔNG MINH ===============
if recommendations:
    st.header("💡 Gợi ý Cải thiện")
    
    cols = st.columns(2)
    
    for idx, rec in enumerate(recommendations):
        with cols[idx % 2]:
            st.markdown(f"""
            <div style='padding: 20px; background: #f8f9fa; border-radius: 10px; 
                        border-left: 4px solid #4CAF50; margin-bottom: 15px;'>
                <h4 style='margin: 0 0 10px 0;'>{rec['icon']} {rec['title']}</h4>
                <p style='margin: 0;'>{rec['message']}</p>
            </div>
            """, unsafe_allow_html=True)

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

