"""
UI Configuration và Dark Mode cho HealthAdvisor
"""

def get_custom_css(dark_mode=False):
    """
    Trả về CSS tùy chỉnh cho app
    
    Args:
        dark_mode: True nếu bật dark mode
    """
    
    if dark_mode:
        # Dark Mode CSS
        return """
        <style>
            /* Dark Mode Colors */
            :root {
                --bg-color: #0e1117;
                --secondary-bg: #262730;
                --text-color: #fafafa;
                --border-color: #464646;
                --accent-color: #4da6ff;
            }
            
            /* Main Container */
            .main {
                background-color: var(--bg-color);
                color: var(--text-color);
            }
            
            /* Headers */
            h1, h2, h3, h4, h5, h6 {
                color: var(--text-color) !important;
                font-weight: 600 !important;
            }
            
            h1 { font-size: 2.5rem !important; }
            h2 { font-size: 2rem !important; }
            h3 { font-size: 1.75rem !important; }
            
            /* Text */
            p, li, span, div {
                font-size: 1.1rem !important;
                line-height: 1.8 !important;
                color: var(--text-color);
            }
            
            /* Cards */
            .disease-card {
                background-color: var(--secondary-bg);
                border: 2px solid var(--border-color);
                border-radius: 12px;
                padding: 1.5rem;
                margin: 1rem 0;
                transition: all 0.3s ease;
            }
            
            .disease-card:hover {
                border-color: var(--accent-color);
                box-shadow: 0 4px 12px rgba(77, 166, 255, 0.3);
                transform: translateY(-2px);
            }
            
            /* Buttons */
            .stButton button {
                font-size: 1.1rem !important;
                padding: 0.75rem 1.5rem !important;
                border-radius: 8px !important;
                font-weight: 500 !important;
                transition: all 0.3s ease !important;
            }
            
            .stButton button:hover {
                transform: scale(1.02);
                box-shadow: 0 4px 8px rgba(77, 166, 255, 0.4);
            }
            
            /* Inputs */
            input, textarea, select {
                font-size: 1.1rem !important;
                padding: 0.75rem !important;
                border-radius: 8px !important;
                background-color: var(--secondary-bg) !important;
                color: var(--text-color) !important;
                border: 1px solid var(--border-color) !important;
            }
            
            /* Expanders */
            .streamlit-expanderHeader {
                font-size: 1.2rem !important;
                font-weight: 600 !important;
                background-color: var(--secondary-bg) !important;
                border-radius: 8px !important;
                color: var(--text-color) !important;
            }
            
            /* Tabs */
            .stTabs [data-baseweb="tab-list"] {
                gap: 1rem;
            }
            
            .stTabs [data-baseweb="tab"] {
                font-size: 1.1rem !important;
                padding: 0.75rem 1.5rem !important;
                border-radius: 8px 8px 0 0 !important;
                font-weight: 500 !important;
                color: var(--text-color) !important;
            }
            
            .stTabs [data-baseweb="tab"][aria-selected="true"] {
                color: var(--accent-color) !important;
                background-color: rgba(77, 166, 255, 0.1) !important;
            }
            
            /* Selectbox & Dropdown */
            [data-baseweb="select"] {
                background-color: var(--secondary-bg) !important;
            }
            
            [data-baseweb="select"] * {
                color: var(--text-color) !important;
            }
            
            /* Dropdown menu */
            [role="listbox"] {
                background-color: var(--secondary-bg) !important;
                border: 1px solid var(--border-color) !important;
            }
            
            [role="option"] {
                color: var(--text-color) !important;
                background-color: var(--secondary-bg) !important;
            }
            
            [role="option"]:hover {
                background-color: rgba(77, 166, 255, 0.2) !important;
            }
            
            /* Radio & Checkbox labels */
            [data-baseweb="radio"] label,
            [data-baseweb="checkbox"] label {
                color: var(--text-color) !important;
            }
            
            /* All form labels */
            label {
                color: var(--text-color) !important;
            }
            
            /* Info boxes */
            .stAlert {
                border-radius: 8px !important;
                padding: 1rem 1.5rem !important;
                font-size: 1.05rem !important;
            }
            
            .stAlert * {
                color: var(--text-color) !important;
            }
            
            /* Sidebar - IMPROVED */
            [data-testid="stSidebar"] {
                background-color: var(--secondary-bg) !important;
            }
            
            /* Sidebar - ALL text elements */
            [data-testid="stSidebar"] * {
                color: var(--text-color) !important;
            }
            
            /* Sidebar navigation links */
            [data-testid="stSidebar"] a {
                color: var(--text-color) !important;
                text-decoration: none !important;
            }
            
            [data-testid="stSidebar"] a:hover {
                color: var(--accent-color) !important;
                background-color: rgba(77, 166, 255, 0.1) !important;
            }
            
            /* Sidebar page links */
            [data-testid="stSidebarNav"] li {
                color: var(--text-color) !important;
            }
            
            [data-testid="stSidebarNav"] a {
                color: var(--text-color) !important;
                font-size: 1.1rem !important;
                padding: 0.75rem 1rem !important;
                border-radius: 8px !important;
            }
            
            [data-testid="stSidebarNav"] a:hover {
                background-color: rgba(77, 166, 255, 0.15) !important;
                color: #ffffff !important;
            }
            
            /* Active page */
            [data-testid="stSidebarNav"] a[aria-current="page"] {
                background-color: var(--accent-color) !important;
                color: #ffffff !important;
                font-weight: 600 !important;
            }
            
            /* Sidebar markdown text */
            [data-testid="stSidebar"] [data-testid="stMarkdown"] {
                color: var(--text-color) !important;
            }
            
            [data-testid="stSidebar"] [data-testid="stMarkdown"] p,
            [data-testid="stSidebar"] [data-testid="stMarkdown"] span,
            [data-testid="stSidebar"] [data-testid="stMarkdown"] div {
                color: var(--text-color) !important;
            }
            
            /* Sidebar widgets */
            [data-testid="stSidebar"] label {
                color: var(--text-color) !important;
                font-weight: 600 !important;
            }
            
            /* Sidebar buttons */
            [data-testid="stSidebar"] button {
                color: var(--text-color) !important;
            }
            
            /* Radio buttons in sidebar */
            [data-testid="stSidebar"] [data-baseweb="radio"] label {
                color: var(--text-color) !important;
            }
            
            /* Warning boxes */
            .warning-box {
                background-color: #3d3000;
                border-left: 5px solid #ffc107;
                padding: 1rem 1.5rem;
                margin: 1rem 0;
                border-radius: 4px;
            }
            
            /* Success boxes */
            .success-box {
                background-color: #0d3d1f;
                border-left: 5px solid #28a745;
                padding: 1rem 1.5rem;
                margin: 1rem 0;
                border-radius: 4px;
            }
            
            /* Scrollbar */
            ::-webkit-scrollbar {
                width: 10px;
                height: 10px;
            }
            
            ::-webkit-scrollbar-track {
                background: var(--bg-color);
            }
            
            ::-webkit-scrollbar-thumb {
                background: var(--border-color);
                border-radius: 5px;
            }
            
            ::-webkit-scrollbar-thumb:hover {
                background: var(--accent-color);
            }
            
            /* MOBILE RESPONSIVE - DARK MODE */
            @media only screen and (max-width: 768px) {
                /* Giảm padding cho mobile */
                .main {
                    padding: 0.5rem !important;
                }
                
                /* Headers nhỏ hơn trên mobile */
                h1 { font-size: 2rem !important; }
                h2 { font-size: 1.75rem !important; }
                h3 { font-size: 1.5rem !important; }
                
                /* Text vẫn đủ lớn để đọc */
                p, li, span, div {
                    font-size: 1rem !important;
                }
                
                /* Buttons full width và dễ bấm */
                .stButton button {
                    width: 100% !important;
                    font-size: 1.2rem !important;
                    padding: 1rem !important;
                    min-height: 56px !important;
                }
                
                /* Inputs full width */
                input, textarea, select {
                    width: 100% !important;
                    font-size: 1.1rem !important;
                    min-height: 52px !important;
                }
                
                /* Columns stack trên mobile */
                [data-testid="column"] {
                    width: 100% !important;
                    margin-bottom: 1rem !important;
                }
                
                /* Cards padding nhỏ hơn */
                .disease-card {
                    padding: 1rem !important;
                    margin: 0.75rem 0 !important;
                }
                
                /* Tabs dễ bấm hơn */
                .stTabs [data-baseweb="tab"] {
                    font-size: 1rem !important;
                    padding: 0.75rem 1rem !important;
                    min-height: 48px !important;
                }
                
                /* Sidebar full width khi mở */
                [data-testid="stSidebar"] {
                    width: 100% !important;
                }
                
                /* Metrics lớn hơn */
                [data-testid="stMetricValue"] {
                    font-size: 1.75rem !important;
                }
            }
            
            /* TABLET */
            @media only screen and (min-width: 769px) and (max-width: 1024px) {
                h1 { font-size: 2.25rem !important; }
                h2 { font-size: 1.875rem !important; }
                
                .stButton button {
                    min-height: 52px !important;
                }
            }
        </style>
        """
    else:
        # Light Mode CSS (improved)
        return """
        <style>
            /* Light Mode Colors */
            :root {
                --bg-color: #ffffff;
                --secondary-bg: #f8f9fa;
                --text-color: #262730;
                --border-color: #e0e0e0;
                --accent-color: #1f77b4;
            }
            
            /* Main Container */
            .main {
                background-color: var(--bg-color);
                padding: 1rem 2rem;
            }
            
            /* Headers - Larger for readability */
            h1, h2, h3, h4, h5, h6 {
                color: var(--text-color) !important;
                font-weight: 600 !important;
                margin-top: 1.5rem !important;
                margin-bottom: 1rem !important;
            }
            
            h1 { font-size: 2.5rem !important; }
            h2 { font-size: 2rem !important; }
            h3 { font-size: 1.75rem !important; }
            h4 { font-size: 1.5rem !important; }
            
            /* Text - Larger font for elderly users */
            p, li, span, div {
                font-size: 1.1rem !important;
                line-height: 1.8 !important;
                color: var(--text-color);
            }
            
            /* Stronger emphasis */
            strong, b {
                font-weight: 700 !important;
                color: #000;
            }
            
            /* Cards */
            .disease-card {
                background-color: var(--secondary-bg);
                border: 2px solid var(--border-color);
                border-radius: 12px;
                padding: 1.5rem;
                margin: 1rem 0;
                transition: all 0.3s ease;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            }
            
            .disease-card:hover {
                border-color: var(--accent-color);
                box-shadow: 0 4px 12px rgba(31, 119, 180, 0.15);
                transform: translateY(-2px);
            }
            
            /* Buttons - Larger and more visible */
            .stButton button {
                font-size: 1.1rem !important;
                padding: 0.75rem 1.5rem !important;
                border-radius: 8px !important;
                font-weight: 500 !important;
                transition: all 0.3s ease !important;
                min-height: 48px !important;
            }
            
            .stButton button:hover {
                transform: scale(1.02);
                box-shadow: 0 4px 8px rgba(31, 119, 180, 0.3);
            }
            
            /* Inputs - Larger for easy tapping */
            input, textarea, select {
                font-size: 1.1rem !important;
                padding: 0.75rem !important;
                border-radius: 8px !important;
                border: 2px solid var(--border-color) !important;
                min-height: 48px !important;
            }
            
            input:focus, textarea:focus, select:focus {
                border-color: var(--accent-color) !important;
                box-shadow: 0 0 0 3px rgba(31, 119, 180, 0.1) !important;
            }
            
            /* Expanders */
            .streamlit-expanderHeader {
                font-size: 1.2rem !important;
                font-weight: 600 !important;
                background-color: var(--secondary-bg) !important;
                border-radius: 8px !important;
                padding: 1rem !important;
            }
            
            .streamlit-expanderHeader:hover {
                background-color: #e8f4f8 !important;
            }
            
            /* Tabs */
            .stTabs [data-baseweb="tab-list"] {
                gap: 1rem;
            }
            
            .stTabs [data-baseweb="tab"] {
                font-size: 1.1rem !important;
                padding: 0.75rem 1.5rem !important;
                border-radius: 8px 8px 0 0 !important;
                font-weight: 500 !important;
            }
            
            /* Info boxes - Better contrast */
            .stAlert {
                border-radius: 8px !important;
                padding: 1rem 1.5rem !important;
                font-size: 1.05rem !important;
                border-left: 5px solid !important;
            }
            
            /* Warning box */
            .warning-box {
                background-color: #fff3cd;
                border-left: 5px solid #ffc107;
                padding: 1rem 1.5rem;
                margin: 1rem 0;
                border-radius: 4px;
            }
            
            /* Success box */
            .success-box {
                background-color: #d4edda;
                border-left: 5px solid #28a745;
                padding: 1rem 1.5rem;
                margin: 1rem 0;
                border-radius: 4px;
            }
            
            /* Sidebar */
            [data-testid="stSidebar"] {
                background-color: var(--secondary-bg) !important;
                padding: 2rem 1rem !important;
            }
            
            /* Dividers */
            hr {
                margin: 2rem 0 !important;
                border-top: 2px solid var(--border-color) !important;
            }
            
            /* Links */
            a {
                color: var(--accent-color) !important;
                text-decoration: none !important;
                font-weight: 500 !important;
            }
            
            a:hover {
                text-decoration: underline !important;
            }
            
            /* Captions */
            .caption, [data-testid="stCaptionContainer"] {
                font-size: 1rem !important;
                color: #6c757d !important;
            }
            
            /* Loading spinner */
            .stSpinner > div {
                border-top-color: var(--accent-color) !important;
            }
            
            /* Tooltips */
            [data-baseweb="tooltip"] {
                font-size: 1rem !important;
            }
            
            /* MOBILE RESPONSIVE - LIGHT MODE */
            @media only screen and (max-width: 768px) {
                /* Giảm padding cho mobile */
                .main {
                    padding: 0.5rem !important;
                }
                
                /* Headers nhỏ hơn trên mobile */
                h1 { font-size: 2rem !important; }
                h2 { font-size: 1.75rem !important; }
                h3 { font-size: 1.5rem !important; }
                h4 { font-size: 1.25rem !important; }
                
                /* Text vẫn đủ lớn để đọc */
                p, li, span, div {
                    font-size: 1rem !important;
                    line-height: 1.6 !important;
                }
                
                /* Buttons full width và dễ bấm */
                .stButton button {
                    width: 100% !important;
                    font-size: 1.2rem !important;
                    padding: 1rem !important;
                    min-height: 56px !important;
                    margin: 0.5rem 0 !important;
                }
                
                /* Inputs full width và lớn */
                input, textarea, select {
                    width: 100% !important;
                    font-size: 1.1rem !important;
                    padding: 0.875rem !important;
                    min-height: 52px !important;
                }
                
                /* Columns stack trên mobile */
                [data-testid="column"] {
                    width: 100% !important;
                    margin-bottom: 1rem !important;
                }
                
                /* Cards padding nhỏ hơn */
                .disease-card {
                    padding: 1rem !important;
                    margin: 0.75rem 0 !important;
                }
                
                /* Tabs dễ bấm */
                .stTabs [data-baseweb="tab"] {
                    font-size: 1rem !important;
                    padding: 0.75rem 1rem !important;
                    min-height: 48px !important;
                    flex: 1 1 auto !important;
                }
                
                .stTabs [data-baseweb="tab-list"] {
                    flex-wrap: wrap !important;
                    gap: 0.5rem !important;
                }
                
                /* Expanders */
                .streamlit-expanderHeader {
                    font-size: 1.1rem !important;
                    padding: 0.875rem !important;
                }
                
                /* Info boxes */
                .stAlert {
                    font-size: 1rem !important;
                    padding: 0.875rem 1rem !important;
                }
                
                /* Sidebar */
                [data-testid="stSidebar"] {
                    width: 100% !important;
                    padding: 1rem !important;
                }
                
                /* Metrics lớn và rõ */
                [data-testid="stMetricValue"] {
                    font-size: 1.75rem !important;
                }
                
                [data-testid="stMetricLabel"] {
                    font-size: 1rem !important;
                }
                
                /* Form labels */
                label {
                    font-size: 1.1rem !important;
                    font-weight: 600 !important;
                }
                
                /* Number inputs */
                [data-baseweb="input"] input {
                    font-size: 1.2rem !important;
                }
                
                /* Selectbox */
                [data-baseweb="select"] {
                    min-height: 52px !important;
                }
                
                /* Radio buttons */
                [data-baseweb="radio"] label {
                    font-size: 1.1rem !important;
                    padding: 0.75rem !important;
                }
                
                /* Checkboxes */
                [data-baseweb="checkbox"] label {
                    font-size: 1.1rem !important;
                }
                
                /* Tables responsive */
                table {
                    font-size: 0.95rem !important;
                    display: block !important;
                    overflow-x: auto !important;
                }
                
                /* Download buttons */
                [data-testid="stDownloadButton"] button {
                    width: 100% !important;
                    min-height: 56px !important;
                }
            }
            
            /* TABLET */
            @media only screen and (min-width: 769px) and (max-width: 1024px) {
                h1 { font-size: 2.25rem !important; }
                h2 { font-size: 1.875rem !important; }
                h3 { font-size: 1.625rem !important; }
                
                .stButton button {
                    min-height: 52px !important;
                }
                
                input, textarea, select {
                    min-height: 50px !important;
                }
            }
            
            /* SMALL PHONES */
            @media only screen and (max-width: 480px) {
                /* Font nhỏ hơn cho màn hình rất nhỏ */
                h1 { font-size: 1.75rem !important; }
                h2 { font-size: 1.5rem !important; }
                h3 { font-size: 1.25rem !important; }
                
                p, li, span, div {
                    font-size: 0.95rem !important;
                }
                
                /* Tabs stack vertical */
                .stTabs [data-baseweb="tab"] {
                    width: 100% !important;
                    text-align: center !important;
                }
            }
        </style>
        """


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

