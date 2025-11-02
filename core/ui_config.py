"""
UI Configuration và Dark Mode cho HealthAdvisor
REFACTORED: Tách CSS ra 2 files riêng để dễ quản lý
"""

from .dark_mode_css import DARK_MODE_CSS
from .light_mode_css import LIGHT_MODE_CSS


def get_custom_css(dark_mode=False):
    """
    Trả về CSS tùy chỉnh cho app (bao gồm viewport meta tag cho mobile)
    
    Args:
        dark_mode: True nếu bật dark mode
    
    Returns:
        str: CSS string cho dark mode hoặc light mode + viewport meta tag
    """
    css = DARK_MODE_CSS if dark_mode else LIGHT_MODE_CSS
    
    # Viewport meta tag đã được thêm vào cuối CSS string
    # Streamlit sẽ inject vào <head> tự động
    return css


def get_loading_spinner_css():
    """Custom loading spinner animation"""
    return """
    <style>
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        
        .loading-text {
            animation: pulse 1.5s ease-in-out infinite;
            font-size: 1.2rem;
            text-align: center;
            color: #1f77b4;
            margin: 2rem 0;
        }
    </style>
    """


def get_success_animation():
    """Success animation CSS"""
    return """
    <style>
        @keyframes slideIn {
            from {
                transform: translateY(-20px);
                opacity: 0;
            }
            to {
                transform: translateY(0);
                opacity: 1;
            }
        }
        
        .success-message {
            animation: slideIn 0.5s ease-out;
        }
    </style>
    """
