"""
Export Reports - Xuất báo cáo sức khỏe ra file
"""

from .pdf_generator import (
    generate_health_report_html,
    generate_medication_report_html,
    create_summary_table
)

__all__ = [
    'generate_health_report_html',
    'generate_medication_report_html',
    'create_summary_table',
]

