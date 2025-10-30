"""
History - Lịch sử uống thuốc và thống kê
"""
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import os
from .scheduler import load_history
from .medication_manager import get_all_medications

def get_adherence_rate(days=7):
    """
    Tính tỷ lệ tuân thủ uống thuốc
    
    Args:
        days: Số ngày tính từ hôm nay trở về trước
    
    Returns:
        float: Tỷ lệ % (0-100)
    """
    history = load_history()
    medications = get_all_medications()
    
    if not medications:
        return 0
    
    # Tính tổng số liều dự kiến trong N ngày
    total_expected = 0
    for med in medications:
        total_expected += len(med['times']) * days
    
    # Đếm số liều đã uống
    taken_count = 0
    cutoff_date = datetime.now() - timedelta(days=days)
    
    for record in history:
        if record['status'] == 'taken':
            record_time = datetime.fromisoformat(record['actual_time'])
            if record_time >= cutoff_date:
                taken_count += 1
    
    if total_expected == 0:
        return 0
    
    return (taken_count / total_expected) * 100

def export_history_csv():
    """Xuất lịch sử ra file CSV"""
    history = load_history()
    
    if not history:
        return None
    
    # Chuyển sang DataFrame
    df = pd.DataFrame(history)
    
    # Lấy thông tin thuốc
    medications = get_all_medications(active_only=False)
    med_dict = {m['id']: m['name'] for m in medications}
    
    df['medication_name'] = df['med_id'].map(med_dict)
    
    # Format lại thời gian
    df['scheduled_time'] = pd.to_datetime(df['scheduled_time']).dt.strftime('%Y-%m-%d %H:%M')
    df['actual_time'] = pd.to_datetime(df['actual_time']).dt.strftime('%Y-%m-%d %H:%M')
    
    # Chọn và sắp xếp cột
    columns = ['scheduled_time', 'actual_time', 'medication_name', 'status', 'notes']
    df = df[columns]
    
    # Đổi tên cột sang tiếng Việt
    df.columns = ['Giờ dự kiến', 'Giờ thực tế', 'Tên thuốc', 'Trạng thái', 'Ghi chú']
    
    # Chuyển status sang tiếng Việt
    status_map = {
        'taken': 'Đã uống',
        'skipped': 'Bỏ qua',
        'missed': 'Quên uống'
    }
    df['Trạng thái'] = df['Trạng thái'].map(status_map)
    
    # Xuất CSV với UTF-8-BOM
    csv = df.to_csv(index=False, encoding='utf-8-sig')
    
    return csv

def render_history_view():
    """Hiển thị lịch sử uống thuốc"""
    st.subheader("📊 Lịch sử & Thống kê")
    
    # Tabs
    tab1, tab2 = st.tabs(["📈 Thống kê", "📜 Lịch sử"])
    
    # ===== TAB THỐNG KÊ =====
    with tab1:
        # Tỷ lệ tuân thủ
        col1, col2, col3 = st.columns(3)
        
        with col1:
            rate_7d = get_adherence_rate(days=7)
            st.metric("📊 Tuân thủ 7 ngày", f"{rate_7d:.1f}%")
            if rate_7d >= 80:
                st.success("✅ Tốt!")
            elif rate_7d >= 60:
                st.warning("⚠️ Cần cải thiện")
            else:
                st.error("❌ Kém")
        
        with col2:
            rate_30d = get_adherence_rate(days=30)
            st.metric("📊 Tuân thủ 30 ngày", f"{rate_30d:.1f}%")
        
        with col3:
            medications = get_all_medications()
            st.metric("💊 Tổng số thuốc", len(medications))
        
        st.divider()
        
        # Biểu đồ xu hướng
        st.markdown("### 📈 Xu hướng tuân thủ (7 ngày)")
        
        history = load_history()
        
        if history:
            # Tạo DataFrame
            df = pd.DataFrame(history)
            df['date'] = pd.to_datetime(df['actual_time']).dt.date
            
            # 7 ngày gần nhất
            last_7_days = [(datetime.now().date() - timedelta(days=i)) for i in range(6, -1, -1)]
            
            daily_stats = []
            for day in last_7_days:
                taken = len(df[(df['date'] == day) & (df['status'] == 'taken')])
                skipped = len(df[(df['date'] == day) & (df['status'] == 'skipped')])
                
                # Tổng số liều dự kiến trong ngày
                total = 0
                for med in medications:
                    total += len(med['times'])
                
                daily_stats.append({
                    'Ngày': day.strftime('%d/%m'),
                    'Đã uống': taken,
                    'Bỏ qua': skipped,
                    'Tỷ lệ %': (taken/total*100) if total > 0 else 0
                })
            
            chart_df = pd.DataFrame(daily_stats)
            
            # Vẽ biểu đồ
            st.bar_chart(chart_df.set_index('Ngày')['Tỷ lệ %'])
            
            # Hiển thị bảng
            st.dataframe(chart_df, use_container_width=True)
        else:
            st.info("📝 Chưa có dữ liệu lịch sử")
    
    # ===== TAB LỊCH SỬ =====
    with tab2:
        history = load_history()
        
        if not history:
            st.info("📝 Chưa có lịch sử uống thuốc")
            return
        
        # Bộ lọc
        col_filter1, col_filter2 = st.columns(2)
        
        with col_filter1:
            filter_days = st.selectbox(
                "Hiển thị",
                [7, 14, 30, 90, 365],
                format_func=lambda x: f"{x} ngày gần nhất"
            )
        
        with col_filter2:
            filter_status = st.multiselect(
                "Trạng thái",
                ["taken", "skipped", "missed"],
                default=["taken", "skipped"],
                format_func=lambda x: {"taken": "✅ Đã uống", "skipped": "⏭️ Bỏ qua", "missed": "⚠️ Quên"}[x]
            )
        
        # Lọc dữ liệu
        df = pd.DataFrame(history)
        df['date'] = pd.to_datetime(df['actual_time'])
        
        cutoff = datetime.now() - timedelta(days=filter_days)
        df = df[df['date'] >= cutoff]
        
        if filter_status:
            df = df[df['status'].isin(filter_status)]
        
        # Lấy tên thuốc
        medications = get_all_medications(active_only=False)
        med_dict = {m['id']: m['name'] for m in medications}
        df['med_name'] = df['med_id'].map(med_dict)
        
        # Hiển thị
        df_display = df[['scheduled_time', 'actual_time', 'med_name', 'status', 'notes']].copy()
        df_display['scheduled_time'] = pd.to_datetime(df_display['scheduled_time']).dt.strftime('%d/%m %H:%M')
        df_display['actual_time'] = pd.to_datetime(df_display['actual_time']).dt.strftime('%d/%m %H:%M')
        
        status_map = {
            'taken': '✅ Đã uống',
            'skipped': '⏭️ Bỏ qua',
            'missed': '⚠️ Quên'
        }
        df_display['status'] = df_display['status'].map(status_map)
        
        df_display.columns = ['Giờ dự kiến', 'Giờ thực tế', 'Thuốc', 'Trạng thái', 'Ghi chú']
        
        st.dataframe(df_display.sort_values('Giờ thực tế', ascending=False), use_container_width=True)
        
        # Nút xuất CSV
        st.divider()
        csv = export_history_csv()
        
        if csv:
            st.download_button(
                label="📥 Tải xuất file CSV",
                data=csv,
                file_name=f"lich_su_uong_thuoc_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                use_container_width=True
            )

