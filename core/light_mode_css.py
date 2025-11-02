"""
Light Mode CSS cho HealthAdvisor
=================================

CSS tối ưu cho người cao tuổi ở chế độ sáng
"""

LIGHT_MODE_CSS = """
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
    
    h1 { font-size: 2.75rem !important; }
    h2 { font-size: 2.25rem !important; }
    h3 { font-size: 2rem !important; }
    h4 { font-size: 1.5rem !important; }
    
    /* Text - Larger font for elderly users */
    p, li, span, div {
        font-size: 1.2rem !important;
        line-height: 1.9 !important;
        color: var(--text-color);
        margin-bottom: 0.75rem !important;
    }
    
    /* Stronger emphasis */
    strong, b {
        font-weight: 700 !important;
        color: #000;
    }
    
    /* Cards - Better spacing */
    .disease-card {
        background-color: var(--secondary-bg);
        border: 2px solid var(--border-color);
        border-radius: 15px;
        padding: 1.75rem;
        margin: 1.25rem 0;
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
        font-size: 1.2rem !important;
        padding: 0.875rem 1.75rem !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        min-height: 56px !important;
    }
    
    .stButton button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 8px rgba(31, 119, 180, 0.3);
    }
    
    /* Inputs - Larger for easy tapping */
    input, textarea, select {
        font-size: 1.2rem !important;
        padding: 0.875rem !important;
        border-radius: 10px !important;
        border: 2px solid var(--border-color) !important;
        min-height: 52px !important;
    }
    
    input:focus, textarea:focus, select:focus {
        border-color: var(--accent-color) !important;
        box-shadow: 0 0 0 3px rgba(31, 119, 180, 0.1) !important;
    }
    
    /* Expanders - Larger and more visible */
    .streamlit-expanderHeader {
        font-size: 1.3rem !important;
        font-weight: 600 !important;
        background-color: var(--secondary-bg) !important;
        border-radius: 10px !important;
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
        font-size: 1.2rem !important;
        padding: 0.875rem 1.75rem !important;
        border-radius: 10px 10px 0 0 !important;
        font-weight: 600 !important;
        min-height: 52px !important;
    }
    
    /* Info boxes - Better contrast */
    .stAlert {
        border-radius: 10px !important;
        padding: 1.25rem 1.75rem !important;
        font-size: 1.15rem !important;
        border-left: 5px solid !important;
        margin-bottom: 1.5rem !important;
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
    
    /* Dividers - More spacing */
    hr {
        margin: 2.5rem 0 !important;
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
        /* Font nhỏ hơn cho màn hình rất nhỏ nhưng vẫn đủ đọc */
        h1 { font-size: 1.75rem !important; }
        h2 { font-size: 1.5rem !important; }
        h3 { font-size: 1.25rem !important; }
        
        p, li, span, div {
            font-size: 1rem !important; /* Tăng từ 0.95rem để dễ đọc hơn */
            line-height: 1.7 !important;
        }
        
        /* Tabs stack vertical và dễ bấm */
        .stTabs [data-baseweb="tab"] {
            width: 100% !important;
            text-align: center !important;
            min-height: 52px !important; /* Tăng từ 48px */
            font-size: 1.1rem !important; /* Tăng font */
            padding: 1rem !important;
        }
        
        /* Buttons lớn hơn trên màn hình nhỏ */
        .stButton button {
            min-height: 60px !important; /* Tăng từ 56px */
            font-size: 1.3rem !important;
            padding: 1.25rem !important;
        }
        
        /* Inputs lớn hơn */
        input, textarea, select {
            min-height: 56px !important;
            font-size: 1.2rem !important;
        }
        
        /* Expanders dễ bấm */
        .streamlit-expanderHeader {
            font-size: 1.2rem !important;
            padding: 1rem !important;
            min-height: 52px !important;
        }
    }
    
    /* Viewport meta tag injection via CSS - Thêm vào head */
    @supports (-webkit-appearance: none) {
        html {
            -webkit-text-size-adjust: 100%;
        }
    }
</style>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
"""

