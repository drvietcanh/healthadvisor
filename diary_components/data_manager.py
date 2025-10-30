"""
Data Manager - Quản lý load/save CSV data
"""
import pandas as pd
import streamlit as st
from datetime import datetime


def load_csv_data(uploaded_file):
    """
    Load dữ liệu từ file CSV
    
    Args:
        uploaded_file: File upload từ st.file_uploader
        
    Returns:
        tuple: (success: bool, data: pd.DataFrame or None, message: str)
    """
    if uploaded_file is None:
        return False, None, "Chưa chọn file"
    
    try:
        # Đọc file CSV
        df = pd.read_csv(uploaded_file)
        
        # Kiểm tra format - ít nhất phải có các cột cơ bản
        required_columns = ['Ngày giờ']
        if not all(col in df.columns for col in required_columns):
            return False, None, "File không đúng định dạng! Thiếu cột 'Ngày giờ'"
        
        # Load thành công
        return True, df, f"Đã tải {len(df)} bản ghi thành công!"
        
    except pd.errors.EmptyDataError:
        return False, None, "File CSV rỗng!"
    except pd.errors.ParserError:
        return False, None, "File CSV bị lỗi định dạng!"
    except Exception as e:
        return False, None, f"Lỗi khi đọc file: {str(e)}"


def save_csv_data(health_data):
    """
    Tạo CSV data để download
    
    Args:
        health_data: pd.DataFrame chứa dữ liệu sức khỏe
        
    Returns:
        tuple: (csv_data: str, filename: str)
    """
    # Tạo CSV với encoding UTF-8-BOM để mở được bằng Excel
    csv = health_data.to_csv(index=False, encoding='utf-8-sig')
    
    # Tạo tên file với timestamp
    filename = f"nhat_ky_suc_khoe_{datetime.now().strftime('%d%m%Y_%H%M')}.csv"
    
    return csv, filename


def initialize_health_data():
    """
    Khởi tạo DataFrame rỗng với các cột cần thiết
    
    Returns:
        pd.DataFrame: DataFrame rỗng với schema đầy đủ
    """
    return pd.DataFrame(columns=[
        'Ngày giờ',
        'Thời điểm',
        'Huyết áp tâm thu',
        'Huyết áp tâm trương',
        'Mạch (nhịp/phút)',
        'Đường huyết (mmol/L)',
        'Đường huyết (mg/dL)',
        'HbA1c (%)',
        'Cholesterol toàn phần (mg/dL)',
        'LDL (mg/dL)',
        'HDL (mg/dL)',
        'Triglyceride (mg/dL)',
        'Acid Uric (mg/dL)',
        'Creatinine (mg/dL)',
        'eGFR (mL/min)',
        'Cân nặng (kg)',
        'Ghi chú'
    ])

