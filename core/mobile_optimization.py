"""
Mobile Optimization - Tối ưu trải nghiệm mobile
Bao gồm: Tab navigation dưới cùng, cải thiện sidebar, touch gestures
"""

MOBILE_OPTIMIZATION_CSS = """
<style>
    /* ========== TAB NAVIGATION DƯỚI CÙNG MÀN HÌNH ========== */
    
    @media only screen and (max-width: 768px) {
        /* Container tabs - Fixed bottom trên mobile */
        .stTabs [data-baseweb="tab-list"] {
            position: fixed !important;
            bottom: 0 !important;
            left: 0 !important;
            right: 0 !important;
            background-color: var(--bg-color, #ffffff) !important;
            border-top: 2px solid var(--border-color, #e0e0e0) !important;
            padding: 0.5rem !important;
            z-index: 998 !important;
            display: flex !important;
            overflow-x: auto !important;
            -webkit-overflow-scrolling: touch !important;
            scrollbar-width: none !important; /* Firefox */
            -ms-overflow-style: none !important; /* IE/Edge */
            box-shadow: 0 -2px 8px rgba(0,0,0,0.1) !important;
        }
        
        /* Ẩn scrollbar cho tabs container */
        .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar {
            display: none !important;
        }
        
        /* Tabs - Horizontal scroll, dễ bấm */
        .stTabs [data-baseweb="tab"] {
            min-width: 120px !important;
            max-width: 180px !important;
            flex-shrink: 0 !important;
            font-size: 1rem !important;
            padding: 0.75rem 1rem !important;
            min-height: 52px !important;
            white-space: nowrap !important;
            text-align: center !important;
        }
        
        /* Padding bottom cho main content để tránh bị che bởi tabs */
        .main .block-container {
            padding-bottom: 80px !important;
        }
        
        /* Tab content - Thêm padding top để không bị che */
        .stTabs [data-baseweb="tab-panel"] {
            padding-top: 1rem !important;
            min-height: calc(100vh - 150px) !important;
        }
    }
    
    /* ========== CẢI THIỆN SIDEBAR TRÊN MOBILE ========== */
    
    @media only screen and (max-width: 768px) {
        /* Sidebar button - To hơn, dễ bấm */
        button[data-testid="baseButton-header"][aria-label*="sidebar"],
        button[data-testid="baseButton-header"][aria-label*="Sidebar"] {
            position: fixed !important;
            top: 1rem !important;
            left: 1rem !important;
            z-index: 999 !important;
            width: 56px !important;
            height: 56px !important;
            border-radius: 50% !important;
            background-color: var(--accent-color, #4da6ff) !important;
            color: white !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3) !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            font-size: 1.5rem !important;
        }
        
        /* Sidebar khi mở - Full screen overlay */
        [data-testid="stSidebar"][aria-expanded="true"] {
            width: 100vw !important;
            max-width: 100vw !important;
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            height: 100vh !important;
            z-index: 998 !important;
            overflow-y: auto !important;
            -webkit-overflow-scrolling: touch !important;
            background-color: var(--secondary-bg, #f8f9fa) !important;
            box-shadow: 2px 0 8px rgba(0,0,0,0.2) !important;
        }
        
        /* Nút đóng sidebar - To, dễ bấm */
        [data-testid="stSidebar"][aria-expanded="true"] button[aria-label*="Close"],
        [data-testid="stSidebar"][aria-expanded="true"] button[aria-label*="close"] {
            position: fixed !important;
            top: 1rem !important;
            right: 1rem !important;
            width: 48px !important;
            height: 48px !important;
            border-radius: 50% !important;
            background-color: rgba(255,255,255,0.9) !important;
            color: var(--text-color, #262730) !important;
            font-size: 1.5rem !important;
            z-index: 999 !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.2) !important;
        }
        
        /* Sidebar content - Font lớn, spacing tốt */
        [data-testid="stSidebar"] {
            padding: 2rem 1rem !important;
        }
        
        [data-testid="stSidebar"] * {
            font-size: 1.2rem !important;
            line-height: 1.8 !important;
        }
        
        /* Sidebar buttons - Full width, lớn */
        [data-testid="stSidebar"] .stButton button {
            width: 100% !important;
            min-height: 56px !important;
            font-size: 1.3rem !important;
            padding: 1rem !important;
            margin: 0.5rem 0 !important;
        }
        
        /* Sidebar toggles - Lớn hơn */
        [data-testid="stSidebar"] [data-baseweb="toggle"] {
            min-height: 52px !important;
            font-size: 1.2rem !important;
        }
        
        /* Sidebar text - Dễ đọc */
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] h4 {
            font-size: 1.5rem !important;
            margin: 1rem 0 !important;
        }
        
        /* Sidebar dividers - Spacing tốt */
        [data-testid="stSidebar"] hr {
            margin: 1.5rem 0 !important;
            border-top: 2px solid var(--border-color, #e0e0e0) !important;
        }
    }
    
    /* ========== TOUCH GESTURES SUPPORT ========== */
    
    @media only screen and (max-width: 768px) {
        /* Tăng touch target size - Dễ bấm hơn */
        button, a, input, select, textarea,
        [data-baseweb="tab"],
        [data-baseweb="radio"] label,
        [data-baseweb="checkbox"] label {
            min-height: 44px !important; /* Apple HIG recommendation */
            min-width: 44px !important;
            -webkit-tap-highlight-color: rgba(77, 166, 255, 0.3) !important;
        }
        
        /* Disable text selection khi swipe (tránh select nhầm) */
        .stTabs [data-baseweb="tab-list"],
        .stTabs [data-baseweb="tab"] {
            -webkit-user-select: none !important;
            user-select: none !important;
            -webkit-touch-callout: none !important;
        }
        
        /* Smooth scrolling */
        * {
            -webkit-overflow-scrolling: touch !important;
            scroll-behavior: smooth !important;
        }
        
        /* Remove 300ms tap delay trên mobile */
        button, a, [data-baseweb="tab"] {
            touch-action: manipulation !important;
        }
    }
    
    /* ========== OFFLINE MODE INDICATOR ========== */
    
    /* Network status indicator */
    .network-status {
        position: fixed !important;
        top: 1rem !important;
        right: 1rem !important;
        z-index: 997 !important;
        padding: 0.5rem 1rem !important;
        border-radius: 20px !important;
        font-size: 0.875rem !important;
        font-weight: 600 !important;
        display: none !important;
    }
    
    .network-status.offline {
        background-color: #dc3545 !important;
        color: white !important;
        display: block !important;
    }
    
    .network-status.online {
        background-color: #28a745 !important;
        color: white !important;
        display: block !important;
    }
    
    @media only screen and (max-width: 768px) {
        .network-status {
            font-size: 1rem !important;
            padding: 0.75rem 1.25rem !important;
            top: 80px !important; /* Tránh che sidebar button */
        }
    }
    
    /* ========== IMPROVED MOBILE EXPERIENCE ========== */
    
    @media only screen and (max-width: 768px) {
        /* Prevent zoom on input focus (iOS) */
        input, select, textarea {
            font-size: 16px !important; /* Prevent zoom on iOS */
        }
        
        /* Better scroll experience */
        body {
            -webkit-overflow-scrolling: touch !important;
            overflow-x: hidden !important;
        }
        
        /* Main container - No horizontal scroll */
        .main {
            overflow-x: hidden !important;
            max-width: 100vw !important;
        }
        
        /* Cards - Better spacing */
        .disease-card,
        [data-testid="stExpander"] {
            margin: 0.75rem 0 !important;
        }
        
        /* Alerts - Full width, better spacing */
        .stAlert {
            margin: 1rem 0 !important;
            padding: 1rem !important;
        }
        
        /* Tables - Horizontal scroll */
        table {
            display: block !important;
            overflow-x: auto !important;
            -webkit-overflow-scrolling: touch !important;
        }
    }
</style>
"""

MOBILE_OPTIMIZATION_JS = """
<script>
    // ========== NETWORK STATUS DETECTION ==========
    
    // Network status indicator
    function updateNetworkStatus() {
        const status = navigator.onLine ? 'online' : 'offline';
        const statusElement = document.getElementById('network-status');
        
        if (!statusElement) {
            // Create status element if not exists
            const div = document.createElement('div');
            div.id = 'network-status';
            div.className = 'network-status ' + status;
            div.textContent = status === 'online' ? '✓ Trực tuyến' : '⚠️ Offline';
            document.body.appendChild(div);
        } else {
            statusElement.className = 'network-status ' + status;
            statusElement.textContent = status === 'online' ? '✓ Trực tuyến' : '⚠️ Offline';
        }
        
        // Hide online status after 3 seconds
        if (status === 'online') {
            setTimeout(() => {
                const el = document.getElementById('network-status');
                if (el) el.style.display = 'none';
            }, 3000);
        }
    }
    
    // Listen to online/offline events
    window.addEventListener('online', updateNetworkStatus);
    window.addEventListener('offline', updateNetworkStatus);
    
    // Initial check
    updateNetworkStatus();
    
    // ========== TOUCH GESTURES FOR TABS ==========
    
    // Swipe left/right to change tabs (trên mobile)
    if (window.innerWidth <= 768) {
        let touchStartX = 0;
        let touchEndX = 0;
        
        document.addEventListener('touchstart', function(e) {
            touchStartX = e.changedTouches[0].screenX;
        }, { passive: true });
        
        document.addEventListener('touchend', function(e) {
            touchEndX = e.changedTouches[0].screenX;
            handleSwipe();
        }, { passive: true });
        
        function handleSwipe() {
            const swipeThreshold = 50; // Minimum swipe distance
            const swipeDistance = touchEndX - touchStartX;
            
            // Only swipe on tab content area
            const tabPanel = document.querySelector('[data-baseweb="tab-panel"]');
            if (!tabPanel) return;
            
            if (Math.abs(swipeDistance) > swipeThreshold) {
                const tabs = document.querySelectorAll('[data-baseweb="tab"]');
                const activeTabIndex = Array.from(tabs).findIndex(tab => 
                    tab.getAttribute('aria-selected') === 'true'
                );
                
                if (swipeDistance > 0 && activeTabIndex > 0) {
                    // Swipe right - previous tab
                    tabs[activeTabIndex - 1].click();
                } else if (swipeDistance < 0 && activeTabIndex < tabs.length - 1) {
                    // Swipe left - next tab
                    tabs[activeTabIndex + 1].click();
                }
            }
        }
    }
    
    // ========== IMPROVED SIDEBAR ON MOBILE ==========
    
    // Close sidebar khi click bên ngoài (mobile only)
    if (window.innerWidth <= 768) {
        document.addEventListener('click', function(e) {
            const sidebar = document.querySelector('[data-testid="stSidebar"][aria-expanded="true"]');
            const sidebarButton = document.querySelector('button[data-testid="baseButton-header"][aria-label*="sidebar"]');
            const isClickInsideSidebar = sidebar && sidebar.contains(e.target);
            const isClickOnButton = sidebarButton && (sidebarButton === e.target || sidebarButton.contains(e.target));
            
            if (sidebar && !isClickInsideSidebar && !isClickOnButton && !e.target.closest('[data-testid="stSidebar"]')) {
                sidebarButton.click(); // Close sidebar
            }
        });
    }
    
    // ========== SMOOTH SCROLL TO TOP ==========
    
    // Add scroll to top button (mobile)
    if (window.innerWidth <= 768) {
        function createScrollToTopButton() {
            const btn = document.createElement('button');
            btn.innerHTML = '↑';
            btn.className = 'scroll-to-top-btn';
            btn.style.cssText = `
                position: fixed;
                bottom: 80px;
                right: 1rem;
                width: 48px;
                height: 48px;
                border-radius: 50%;
                background-color: var(--accent-color, #4da6ff);
                color: white;
                border: none;
                font-size: 1.5rem;
                z-index: 997;
                box-shadow: 0 4px 12px rgba(0,0,0,0.3);
                display: none;
                cursor: pointer;
            `;
            
            btn.onclick = () => window.scrollTo({ top: 0, behavior: 'smooth' });
            
            window.addEventListener('scroll', () => {
                btn.style.display = window.scrollY > 300 ? 'block' : 'none';
            });
            
            document.body.appendChild(btn);
        }
        
        if (document.body) {
            createScrollToTopButton();
        } else {
            document.addEventListener('DOMContentLoaded', createScrollToTopButton);
        }
    }
    
    // ========== PREFER-REDUCE-MOTION SUPPORT ==========
    
    // Respect user's motion preferences
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReducedMotion) {
        const style = document.createElement('style');
        style.textContent = `
            *, *::before, *::after {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }
        `;
        document.head.appendChild(style);
    }
</script>
"""


def get_mobile_optimization():
    """
    Trả về CSS và JS cho tối ưu mobile
    
    Returns:
        str: CSS + JS string để inject vào trang
    """
    return MOBILE_OPTIMIZATION_CSS + MOBILE_OPTIMIZATION_JS

