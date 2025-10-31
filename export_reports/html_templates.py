"""
HTML Templates - Mẫu HTML cho báo cáo PDF
"""

HTML_STYLES = """
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
"""

HTML_HEAD = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    {styles}
</head>
<body>
"""

HTML_FOOTER = """
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

