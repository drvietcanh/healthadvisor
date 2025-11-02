"""
Sidebar Menu Module - Menu điều hướng tùy chỉnh cho tất cả các trang
"""
import streamlit as st


def hide_default_nav():
    """
    CSS và JavaScript để ẩn HOÀN TOÀN sidebar navigation mặc định của Streamlit
    PHẢI GỌI TRƯỚC KHI RENDER NỘI DUNG KHÁC
    """
    hide_default_nav_css = """
    <style>
        /* Ẩn HOÀN TOÀN sidebar navigation mặc định của Streamlit */
        nav[data-testid="stSidebarNav"],
        nav[data-testid="stSidebarNav"] *,
        section[data-testid="stSidebarNav"],
        div[data-testid="stSidebarNav"],
        ul[data-testid="stSidebarNav"] {
            display: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
            height: 0 !important;
            width: 0 !important;
            overflow: hidden !important;
            position: absolute !important;
            left: -9999px !important;
        }
        
        /* Ẩn search bar trong sidebar nav */
        div[data-testid="stSidebarNav"] input,
        div[data-testid="stSidebarNav"] button,
        button[aria-label="View less"],
        button[aria-label="View more"] {
            display: none !important;
            visibility: hidden !important;
        }
        
        /* Đảm bảo sidebar container vẫn hiển thị */
        section[data-testid="stSidebar"],
        div[data-testid="stSidebar"] {
            display: block !important;
        }
        
        /* MOBILE: Đảm bảo sidebar có thể mở được */
        @media only screen and (max-width: 768px) {
            /* Sidebar button toggle - luôn hiển thị trên mobile */
            button[data-testid="baseButton-header"][aria-label*="sidebar"] {
                display: block !important;
                position: fixed !important;
                top: 1rem !important;
                left: 1rem !important;
                z-index: 999 !important;
                background-color: var(--accent-color) !important;
                color: white !important;
                padding: 0.75rem !important;
                border-radius: 50% !important;
                width: 56px !important;
                height: 56px !important;
                box-shadow: 0 4px 12px rgba(0,0,0,0.3) !important;
            }
            
            /* Sidebar khi mở trên mobile - full screen overlay */
            [data-testid="stSidebar"][aria-expanded="true"] {
                width: 100vw !important;
                max-width: 100vw !important;
                z-index: 999 !important;
                position: fixed !important;
                top: 0 !important;
                left: 0 !important;
                height: 100vh !important;
                overflow-y: auto !important;
            }
        }
    </style>
    
    <script>
        // JavaScript để ẩn menu mặc định - chạy ngay lập tức và liên tục
        (function() {
            function hideDefaultNav() {
                // Tìm tất cả các selector có thể chứa menu mặc định
                const selectors = [
                    'nav[data-testid="stSidebarNav"]',
                    'section[data-testid="stSidebarNav"]',
                    'div[data-testid="stSidebarNav"]',
                    'ul[data-testid="stSidebarNav"]',
                    '[class*="sidebar-nav"]',
                    '[id*="sidebar-nav"]'
                ];
                
                selectors.forEach(selector => {
                    const elements = document.querySelectorAll(selector);
                    elements.forEach(el => {
                        el.style.display = 'none';
                        el.style.visibility = 'hidden';
                        el.style.opacity = '0';
                        el.style.height = '0';
                        el.style.width = '0';
                        el.style.position = 'absolute';
                        el.style.left = '-9999px';
                    });
                });
                
                // Ẩn search bar và nút view less/more
                const searchBars = document.querySelectorAll('div[data-testid="stSidebarNav"] input, div[data-testid="stSidebarNav"] button');
                searchBars.forEach(el => {
                    el.style.display = 'none';
                    el.style.visibility = 'hidden';
                });
                
                // Ẩn tất cả nút view less/more
                const buttons = document.querySelectorAll('button[aria-label*="View"], button[aria-label*="view"]');
                buttons.forEach(btn => {
                    if (btn.textContent.includes('View') || btn.getAttribute('aria-label')?.includes('View')) {
                        btn.style.display = 'none';
                        btn.style.visibility = 'hidden';
                    }
                });
            }
            
            // Chạy ngay lập tức
            if (document.body) {
                hideDefaultNav();
            }
            
            // Chạy khi DOM ready
            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', hideDefaultNav);
            } else {
                hideDefaultNav();
            }
            
            // MutationObserver để theo dõi thay đổi DOM
            const observer = new MutationObserver(function(mutations) {
                hideDefaultNav();
            });
            
            // Bắt đầu observe
            if (document.body) {
                observer.observe(document.body, { 
                    childList: true, 
                    subtree: true,
                    attributes: true,
                    attributeFilter: ['style', 'class']
                });
            }
            
            // Fallback: chạy định kỳ
            setInterval(hideDefaultNav, 50);
            
            // Chạy sau khi Streamlit load xong
            window.addEventListener('load', hideDefaultNav);
        })();
    </script>
    """
    st.markdown(hide_default_nav_css, unsafe_allow_html=True)


def render_sidebar_menu():
    """
    Render menu sidebar tùy chỉnh cho tất cả các trang
    Bao gồm:
    - Dark Mode Toggle
    - Menu Điều hướng (13 trang chính)
    - Quick Actions (4 trang phụ trợ)
    """
    with st.sidebar:
        st.markdown("### ⚙️ Cài đặt Giao diện")
        
        # Initialize dark mode state
        if 'dark_mode' not in st.session_state:
            st.session_state.dark_mode = False
        
        # Initialize extra large font state
        if 'extra_large_font' not in st.session_state:
            st.session_state.extra_large_font = False
        
        # Toggle Dark Mode
        dark_mode = st.toggle(
            "🌙 Chế độ Tối (Dark Mode)",
            value=st.session_state.dark_mode,
            help="Bật/tắt chế độ tối - dễ nhìn hơn ban đêm và tiết kiệm pin"
        )
        
        st.session_state.dark_mode = dark_mode
        
        # Toggle Extra Large Font
        extra_large_font = st.toggle(
            "🔤 Font Siêu Lớn",
            value=st.session_state.extra_large_font,
            help="Tăng font lên 22-24px - Dễ đọc hơn cho người mắt kém"
        )
        
        st.session_state.extra_large_font = extra_large_font
        
        if dark_mode:
            st.caption("✅ Đang dùng chế độ tối")
        else:
            st.caption("☀️ Đang dùng chế độ sáng")
        
        if extra_large_font:
            st.caption("✅ Font siêu lớn đã bật")
        
        st.divider()
        
        # Search Bar
        try:
            from core.search_component import render_search_bar
            render_search_bar()
            st.divider()
        except ImportError:
            pass  # Nếu chưa có search component thì bỏ qua
        
        # Favorites
        try:
            from core.favorites_manager import render_favorites_sidebar
            render_favorites_sidebar()
            st.divider()
        except ImportError:
            pass
        
        # Recent Pages
        try:
            from core.recent_pages import render_recent_sidebar
            render_recent_sidebar()
            st.divider()
        except ImportError:
            pass
        
        # Menu Navigation - Tùy chỉnh hoàn toàn
        # Chia thành 4 nhóm theo mức độ ưu tiên
        
        # ===== NHÓM 1: MENU CHÍNH (Priority 1 - Quan trọng nhất) =====
        st.markdown("### 📂 Menu Chính")
        
        priority_1_items = [
            ("🆘 SOS", "12_🆘_SOS"),  # Đưa SOS lên đầu
            ("❤️ Tim Mạch", "1_❤️_Tim_Mạch"),
            ("🩸 Tiểu Đường", "3_🩸_Tiểu_Đường"),
            ("🧠 Thần Kinh", "4_🧠_Thần_Kinh"),
            ("🫁 Hô Hấp", "2_🫁_Hô_Hấp"),
        ]
        
        for label, page_name in priority_1_items:
            st.page_link(f"pages/{page_name}.py", label=label, icon=None)
        
        st.divider()
        
        # ===== NHÓM 2: CHUYÊN KHOA (Priority 2) =====
        st.markdown("### 🏥 Chuyên Khoa")
        
        priority_2_items = [
            ("🦴 Khớp - Cột Sống", "6_🦴_Khớp_Cột_Sống"),
            ("⚖️ Hội Chứng Chuyển Hóa", "5_⚖️_Hội_Chứng_Chuyển_Hóa"),
            ("🧪 Thận-Tiết Niệu", "9_🧪_Thận_Tiết_Niệu"),
            ("👁️ Mắt", "10_👁️_Mắt"),
            ("🌡️ Tiêu Hóa", "11_🌡️_Tiêu_Hóa"),
            ("🦷 Răng Hàm Mặt", "13_🦷_Răng_Hàm_Mặt"),
            ("🦋 Da Liễu", "14_🦋_Da_Liễu"),
            ("👂 Tai Mũi Họng", "15_👂_Tai_Mũi_Họng"),
            ("🎯 Nội Tiết", "16_🦋_Nội_Tiết"),
            ("🐛 Ký Sinh Trùng", "17_🐛_Ký_Sinh_Trùng"),
        ]
        
        for label, page_name in priority_2_items:
            st.page_link(f"pages/{page_name}.py", label=label, icon=None)
        
        st.divider()
        
        # ===== NHÓM 3: HỖ TRỢ (Priority 3) =====
        st.markdown("### 💡 Hỗ Trợ")
        
        priority_3_items = [
            ("💡 Mẹo Vặt", "8_💡_Mẹo_Vặt"),
            ("🎓 Học Dễ", "7_🎓_Học_Dễ"),
            ("📖 Hướng Dẫn", "0_📖_Hướng_Dẫn"),
            ("🤖 AI Bác Sĩ", "_🤖_AI_Bác_Sĩ"),
        ]
        
        for label, page_name in priority_3_items:
            st.page_link(f"pages/{page_name}.py", label=label, icon=None)
        
        st.divider()
        
        # Quick Actions - Các trang phụ trợ (ẩn khỏi menu chính)
        st.markdown("### 🚀 Truy cập nhanh")
        
        quick_actions = [
            ("🤖 AI Bác Sĩ", "_🤖_AI_Bác_Sĩ"),
            ("📊 Nhật Ký", "_📊_Nhật_Ký"),
            ("💊 Nhắc Thuốc", "_💊_Nhắc_Thuốc"),
            ("📈 Xu Hướng", "_📈_Xu_Hướng"),
        ]
        
        for label, page_name in quick_actions:
            st.page_link(f"pages/{page_name}.py", label=label, icon=None)

