"""
PDF Generator - Tạo báo cáo HTML đẹp (có thể in ra PDF)
"""
import pandas as pd
from datetime import datetime
import base64
import io

def create_summary_table(df):
    """Tạo bảng tổng hợp dữ liệu"""
    if df is None or len(df) == 0:
        return "<p>Không có dữ liệu</p>"
    
    # Lấy 30 ngày gần nhất
    df_recent = df.tail(30).copy()
    
    # Tạo HTML table
    table_html = """
    <table style='width: 100%; border-collapse: collapse; margin: 20px 0;'>
        <thead>
            <tr style='background: #4CAF50; color: white;'>
                <th style='padding: 12px; border: 1px solid #ddd;'>Ngày</th>
                <th style='padding: 12px; border: 1px solid #ddd;'>Huyết áp</th>
                <th style='padding: 12px; border: 1px solid #ddd;'>Đường huyết</th>
                <th style='padding: 12px; border: 1px solid #ddd;'>Cân nặng</th>
            </tr>
        </thead>
        <tbody>
    """
    
    for _, row in df_recent.iterrows():
        date_str = pd.to_datetime(row['Ngày']).strftime('%d/%m/%Y')
        bp = f"{row.get('Huyết áp tâm thu', '-')}/{row.get('Huyết áp tâm trương', '-')}" if pd.notna(row.get('Huyết áp tâm thu')) else '-'
        bs = f"{row.get('Đường huyết', '-')}" if pd.notna(row.get('Đường huyết')) else '-'
        weight = f"{row.get('Cân nặng (kg)', '-')}" if pd.notna(row.get('Cân nặng (kg)')) else '-'
        
        table_html += f"""
            <tr>
                <td style='padding: 10px; border: 1px solid #ddd;'>{date_str}</td>
                <td style='padding: 10px; border: 1px solid #ddd; text-align: center;'>{bp}</td>
                <td style='padding: 10px; border: 1px solid #ddd; text-align: center;'>{bs}</td>
                <td style='padding: 10px; border: 1px solid #ddd; text-align: center;'>{weight}</td>
            </tr>
        """
    
    table_html += """
        </tbody>
    </table>
    """
    
    return table_html

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
    
    html = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Báo cáo Sức khỏe - {patient_info.get('name', 'Bệnh nhân')}</title>
        <style>
            @media print {{
                body {{ margin: 0; }}
                .no-print {{ display: none; }}
                @page {{ margin: 2cm; }}
            }}
            
            body {{
                font-family: 'Segoe UI', Arial, sans-serif;
                max-width: 21cm;
                margin: 0 auto;
                padding: 20px;
                background: white;
                color: #333;
            }}
            
            .header {{
                text-align: center;
                padding: 30px 0;
                border-bottom: 3px solid #4CAF50;
                margin-bottom: 30px;
            }}
            
            .header h1 {{
                margin: 0;
                color: #4CAF50;
                font-size: 32px;
            }}
            
            .header p {{
                margin: 10px 0 0 0;
                color: #666;
                font-size: 16px;
            }}
            
            .patient-info {{
                background: #e8f5e9;
                padding: 20px;
                border-radius: 8px;
                margin: 20px 0;
            }}
            
            .patient-info h2 {{
                margin: 0 0 15px 0;
                color: #2e7d32;
            }}
            
            .info-row {{
                display: flex;
                margin: 10px 0;
            }}
            
            .info-label {{
                font-weight: bold;
                width: 150px;
            }}
            
            .section {{
                margin: 30px 0;
                page-break-inside: avoid;
            }}
            
            .section h2 {{
                color: #4CAF50;
                border-bottom: 2px solid #4CAF50;
                padding-bottom: 10px;
                margin: 20px 0 15px 0;
            }}
            
            .footer {{
                margin-top: 50px;
                padding-top: 20px;
                border-top: 1px solid #ddd;
                text-align: center;
                color: #666;
                font-size: 14px;
            }}
            
            .warning {{
                background: #fff3cd;
                border-left: 4px solid #ffc107;
                padding: 15px;
                margin: 20px 0;
            }}
        </style>
    </head>
    <body>
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
        
        <div class="footer">
            <p><b>Health Advisor</b> - Ứng dụng Quản lý Sức khỏe cho Người Việt</p>
            <p>Tạo bởi: Health Advisor Team | Email: support@healthadvisor.vn</p>
        </div>
        
        <div class="no-print" style='margin-top: 30px; text-align: center; padding: 20px; background: #f0f0f0; border-radius: 8px;'>
            <p style='margin: 0; font-size: 18px;'><b>💡 Cách lưu thành PDF:</b></p>
            <p style='margin: 10px 0 0 0;'>Nhấn <b>Ctrl+P</b> (hoặc Cmd+P trên Mac) → Chọn "Save as PDF" → Lưu file</p>
        </div>
    </body>
    </html>
    """
    
    return html

def generate_medication_report_html(medications, medical_info):
    """
    Tạo báo cáo thuốc đang uống HTML
    
    Args:
        medications: List danh sách thuốc
        medical_info: Dict thông tin y tế
    
    Returns:
        HTML string
    """
    current_date = datetime.now().strftime('%d/%m/%Y')
    
    # Danh sách thuốc
    meds_html = ""
    if medications and len(medications) > 0:
        meds_html = "<table style='width: 100%; border-collapse: collapse; margin: 20px 0;'>"
        meds_html += """
        <thead>
            <tr style='background: #4CAF50; color: white;'>
                <th style='padding: 12px; border: 1px solid #ddd;'>Tên thuốc</th>
                <th style='padding: 12px; border: 1px solid #ddd;'>Liều lượng</th>
                <th style='padding: 12px; border: 1px solid #ddd;'>Giờ uống</th>
                <th style='padding: 12px; border: 1px solid #ddd;'>Ghi chú</th>
            </tr>
        </thead>
        <tbody>
        """
        
        for med in medications:
            times_str = ', '.join(med.get('times', []))
            meds_html += f"""
            <tr>
                <td style='padding: 10px; border: 1px solid #ddd;'><b>{med['name']}</b></td>
                <td style='padding: 10px; border: 1px solid #ddd; text-align: center;'>{med['dosage']}</td>
                <td style='padding: 10px; border: 1px solid #ddd; text-align: center;'>{times_str}</td>
                <td style='padding: 10px; border: 1px solid #ddd;'>{med.get('notes', '-')}</td>
            </tr>
            """
        
        meds_html += "</tbody></table>"
    else:
        meds_html = "<p>Không có thuốc nào đang uống.</p>"
    
    # Thông tin y tế
    medical_html = f"""
    <div style='background: #fff3e0; padding: 20px; border-radius: 8px; margin: 20px 0;'>
        <h3 style='margin: 0 0 15px 0; color: #e65100;'>🏥 Thông tin Y tế Khẩn cấp</h3>
        
        <div style='margin: 10px 0;'>
            <b>🩸 Nhóm máu:</b> {medical_info.get('blood_type', 'Chưa biết')}
        </div>
        
        <div style='margin: 15px 0;'>
            <b>🚫 Dị ứng:</b><br>
            <pre style='background: white; padding: 10px; border-radius: 5px; margin: 5px 0;'>{medical_info.get('allergies', 'Không có') if medical_info.get('allergies') else 'Không có'}</pre>
        </div>
        
        <div style='margin: 15px 0;'>
            <b>🏥 Bệnh nền:</b><br>
            <pre style='background: white; padding: 10px; border-radius: 5px; margin: 5px 0;'>{medical_info.get('conditions', 'Không có') if medical_info.get('conditions') else 'Không có'}</pre>
        </div>
    </div>
    """
    
    html = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <title>Báo cáo Thuốc</title>
        <style>
            @media print {{
                body {{ margin: 0; }}
                .no-print {{ display: none; }}
                @page {{ margin: 2cm; }}
            }}
            
            body {{
                font-family: 'Segoe UI', Arial, sans-serif;
                max-width: 21cm;
                margin: 0 auto;
                padding: 20px;
            }}
            
            .header {{
                text-align: center;
                padding: 30px 0;
                border-bottom: 3px solid #FF9800;
                margin-bottom: 30px;
            }}
            
            .header h1 {{
                margin: 0;
                color: #FF9800;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>💊 BÁO CÁO THUỐC ĐANG UỐNG</h1>
            <p>Ngày: {current_date}</p>
        </div>
        
        <div class="section">
            <h2 style='color: #FF9800;'>📋 Danh sách Thuốc</h2>
            {meds_html}
        </div>
        
        {medical_html}
        
        <div style='margin-top: 30px; padding: 15px; background: #ffebee; border-radius: 8px;'>
            <p style='margin: 0;'><b>🚨 SỐ CẤP CỨU: 115</b></p>
            <p style='margin: 10px 0 0 0;'>Mang theo báo cáo này khi đi khám để bác sĩ biết thuốc bạn đang dùng.</p>
        </div>
        
        <div class="no-print" style='margin-top: 30px; text-align: center; padding: 20px; background: #f0f0f0; border-radius: 8px;'>
            <p><b>💡 Nhấn Ctrl+P để lưu thành PDF</b></p>
        </div>
    </body>
    </html>
    """
    
    return html

