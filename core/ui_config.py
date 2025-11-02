"""
UI Configuration và Dark Mode cho HealthAdvisor
REFACTORED: Tách CSS ra 2 files riêng để dễ quản lý
"""

try:
    from .dark_mode_css import DARK_MODE_CSS
except ImportError:
    DARK_MODE_CSS = ""

try:
    from .light_mode_css import LIGHT_MODE_CSS
except ImportError:
    LIGHT_MODE_CSS = ""


def get_custom_css(dark_mode=False, extra_large_font=False):
    """
    Trả về CSS tùy chỉnh cho app (bao gồm viewport meta tag cho mobile)
    
    Args:
        dark_mode: True nếu bật dark mode
        extra_large_font: True nếu bật font siêu lớn (22-24px)
    
    Returns:
        str: CSS string cho dark mode hoặc light mode + viewport meta tag + extra large font (nếu cần)
    """
    # Đảm bảo có CSS mặc định nếu import lỗi
    css = DARK_MODE_CSS if dark_mode else LIGHT_MODE_CSS
    if not css or css is None:
        css = ""  # Fallback về string rỗng
    
    # Thêm CSS cho font siêu lớn nếu bật
    if extra_large_font:
        extra_font_css = """
    <style>
        /* Extra Large Font Mode - Font siêu lớn cho người mắt kém */
        p, li, span, div {
            font-size: 24px !important; /* Tăng từ 20px lên 24px */
            line-height: 2.0 !important;
        }
        
        h1 { font-size: 3.5rem !important; /* Tăng từ 2.75rem */ }
        h2 { font-size: 3rem !important; /* Tăng từ 2.25rem */ }
        h3 { font-size: 2.5rem !important; /* Tăng từ 2rem */ }
        h4 { font-size: 2rem !important; /* Tăng từ 1.5rem */ }
        
        /* Buttons lớn hơn */
        .stButton button {
            font-size: 1.5rem !important;
            min-height: 64px !important;
            padding: 1.5rem !important;
        }
        
        /* Inputs lớn hơn */
        input, textarea, select {
            font-size: 1.4rem !important;
            min-height: 64px !important;
            padding: 1rem !important;
        }
        
        /* Tabs lớn hơn */
        .stTabs [data-baseweb="tab"] {
            font-size: 1.4rem !important;
            min-height: 60px !important;
            padding: 1.25rem !important;
        }
        
        /* Expanders lớn hơn */
        .streamlit-expanderHeader {
            font-size: 1.4rem !important;
            padding: 1.25rem !important;
            min-height: 60px !important;
        }
        
        /* Caption lớn hơn */
        .stCaption {
            font-size: 1.2rem !important;
        }
        
        /* Sidebar lớn hơn */
        .css-1d391kg {
            font-size: 1.3rem !important;
        }
        
        /* Mobile responsive cho font siêu lớn */
        @media only screen and (max-width: 480px) {
            p, li, span, div {
                font-size: 22px !important; /* Hơi nhỏ hơn trên mobile */
            }
            
            h1 { font-size: 2.5rem !important; }
            h2 { font-size: 2rem !important; }
            h3 { font-size: 1.75rem !important; }
        }
    </style>
        """
        css = css + extra_font_css
    
    # Viewport meta tag đã được thêm vào cuối CSS string
    # Streamlit sẽ inject vào <head> tự động
    # Đảm bảo luôn trả về string hợp lệ
    return css if css else ""


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
