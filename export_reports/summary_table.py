"""
Summary Table - Tạo bảng tổng hợp dữ liệu
"""

import pandas as pd


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

