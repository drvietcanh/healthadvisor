"""
Health Report - Tạo báo cáo sức khỏe HTML
"""

import pandas as pd
from datetime import datetime
from .html_templates import HTML_STYLES, HTML_HEAD, HTML_FOOTER
from .summary_table import create_summary_table


def generate_health_report_html(patient_info, df, bp_analysis=None, bs_analysis=None):
    """
    Tạo báo cáo sức khỏe HTML
    
    Args:
        patient_info: Dict thông tin bệnh nhân {'name': '', 'age': '', ...}
        df: DataFrame dữ liệu từ Nhật ký
        bp_analysis: Kết quả phân tích huyết áp
        bs_analysis: Kết quả phân tích đường huyết
    
    Returns:
        HTML string
    """
    
    current_date = datetime.now().strftime('%d/%m/%Y')
    
    # Tính toán thống kê
    stats_html = ""
    
    if df is not None and len(df) > 0:
        total_records = len(df)
        date_from = pd.to_datetime(df['Ngày']).min().strftime('%d/%m/%Y')
        date_to = pd.to_datetime(df['Ngày']).max().strftime('%d/%m/%Y')
        
        stats_html = f"""
        <div style='background: #f8f9fa; padding: 15px; border-radius: 8px; margin: 20px 0;'>
            <h3 style='margin: 0 0 10px 0;'>📊 Thống kê:</h3>
            <ul style='margin: 0; padding-left: 20px;'>
                <li>Tổng số lần đo: <b>{total_records}</b></li>
                <li>Từ ngày: <b>{date_from}</b> đến <b>{date_to}</b></li>
        """
        
        if bp_analysis:
            stats_html += f"""
                <li>Huyết áp trung bình: <b>{bp_analysis['avg_systolic']}/{bp_analysis['avg_diastolic']} mmHg</b></li>
                <li>Phân loại: <b>{bp_analysis['category']}</b></li>
            """
        
        if bs_analysis:
            stats_html += f"""
                <li>Đường huyết trung bình: <b>{bs_analysis['avg']} mmol/L</b></li>
                <li>Phân loại: <b>{bs_analysis['category']}</b></li>
            """
        
        stats_html += """
            </ul>
        </div>
        """
    
    # Tạo bảng dữ liệu
    data_table = create_summary_table(df) if df is not None else "<p>Không có dữ liệu</p>"
    
    html = HTML_HEAD.format(
        title=f"Báo cáo Sức khỏe - {patient_info.get('name', 'Bệnh nhân')}",
        styles=HTML_STYLES
    )
    
    html += f"""
        <div class="header">
            <h1>📊 BÁO CÁO SỨC KHỎE</h1>
            <p>Health Advisor - Ứng dụng Quản lý Sức khỏe</p>
            <p>Ngày xuất báo cáo: {current_date}</p>
        </div>
        
        <div class="patient-info">
            <h2>👤 Thông tin Bệnh nhân</h2>
            <div class="info-row">
                <span class="info-label">Họ tên:</span>
                <span>{patient_info.get('name', 'Chưa cập nhật')}</span>
            </div>
            <div class="info-row">
                <span class="info-label">Tuổi:</span>
                <span>{patient_info.get('age', 'Chưa cập nhật')}</span>
            </div>
            <div class="info-row">
                <span class="info-label">Giới tính:</span>
                <span>{patient_info.get('gender', 'Chưa cập nhật')}</span>
            </div>
            <div class="info-row">
                <span class="info-label">Ngày tạo báo cáo:</span>
                <span>{current_date}</span>
            </div>
        </div>
        
        {stats_html}
        
        <div class="section">
            <h2>📋 Chi tiết Dữ liệu (30 ngày gần nhất)</h2>
            {data_table}
        </div>
        
        <div class="warning">
            <p style='margin: 0;'><b>⚠️ Lưu ý:</b> Báo cáo này chỉ mang tính chất tham khảo, 
            được tạo tự động từ dữ liệu bạn nhập. Vui lòng tham khảo ý kiến bác sĩ 
            để có chẩn đoán và điều trị chính xác.</p>
        </div>
    """
    
    html += HTML_FOOTER
    
    return html

