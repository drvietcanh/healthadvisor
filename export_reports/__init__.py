"""
Export Reports Module - Tạo báo cáo PDF/HTML
"""

from .health_report import generate_health_report_html
from .medication_report import generate_medication_report_html
from .summary_table import create_summary_table

__all__ = [
    'generate_health_report_html',
    'generate_medication_report_html',
    'create_summary_table'
]
