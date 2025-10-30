"""
Dark Mode CSS cho HealthAdvisor
================================

CSS tối ưu cho người cao tuổi ở chế độ tối
"""

DARK_MODE_CSS = """
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

