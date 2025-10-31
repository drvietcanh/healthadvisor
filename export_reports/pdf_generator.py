"""
PDF Generator - Tạo báo cáo HTML đẹp (có thể in ra PDF)
Backward compatible - Import từ submodule
"""

from .health_report import generate_health_report_html
from .medication_report import generate_medication_report_html
from .summary_table import create_summary_table

# Export để backward compatible
__all__ = [
    'generate_health_report_html',
    'generate_medication_report_html',
    'create_summary_table'
]
