"""
Medication Report - Tạo báo cáo thuốc đang uống HTML
"""

from datetime import datetime
from .html_templates import HTML_STYLES, HTML_HEAD


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
    
    # Styles riêng cho medication report
    med_styles = """
        <style>
            @media print {
                body { margin: 0; }
                .no-print { display: none; }
                @page { margin: 2cm; }
            }
            
            body {
                font-family: 'Segoe UI', Arial, sans-serif;
                max-width: 21cm;
                margin: 0 auto;
                padding: 20px;
            }
            
            .header {
                text-align: center;
                padding: 30px 0;
                border-bottom: 3px solid #FF9800;
                margin-bottom: 30px;
            }
            
            .header h1 {
                margin: 0;
                color: #FF9800;
            }
        </style>
    """
    
    html = HTML_HEAD.format(
        title="Báo cáo Thuốc",
        styles=med_styles
    )
    
    html += f"""
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

