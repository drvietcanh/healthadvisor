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
    - Menu Điều hướng (10 trang chính)
    - Quick Actions (4 trang phụ trợ)
    """
    with st.sidebar:
        st.markdown("### ⚙️ Cài đặt Giao diện")
        
        # Initialize dark mode state
        if 'dark_mode' not in st.session_state:
            st.session_state.dark_mode = False
        
        # Toggle
        dark_mode = st.toggle(
            "🌙 Chế độ Tối (Dark Mode)",
            value=st.session_state.dark_mode,
            help="Bật/tắt chế độ tối - dễ nhìn hơn ban đêm và tiết kiệm pin"
        )
        
        st.session_state.dark_mode = dark_mode
        
        if dark_mode:
            st.caption("✅ Đang dùng chế độ tối")
        else:
            st.caption("☀️ Đang dùng chế độ sáng")
        
        st.divider()
        
        # Menu Navigation - Tùy chỉnh hoàn toàn
        # Xem MENU_STRUCTURE.md để biết chi tiết về cấu trúc menu
        st.markdown("### 📂 Điều hướng")
        
        # Danh sách menu items (10 trang hiển thị)
        menu_items = [
            ("📖 Hướng Dẫn", "pages/0_📖_Hướng_Dẫn.py"),
            ("❤️ Tim Mạch", "pages/1_❤️_Tim_Mạch.py"),
            ("🫁 Hô Hấp", "pages/2_🫁_Hô_Hấp.py"),
            ("🩸 Tiểu Đường", "pages/3_🩸_Tiểu_Đường.py"),
            ("🧠 Thần Kinh", "pages/4_🧠_Thần_Kinh.py"),
            ("⚖️ Hội Chứng Chuyển Hóa", "pages/5_⚖️_Hội_Chứng_Chuyển_Hóa.py"),
            ("🦴 Khớp - Cột Sống", "pages/6_🦴_Khớp_Cột_Sống.py"),
            ("🎓 Học Dễ", "pages/7_🎓_Học_Dễ.py"),
            ("💡 Mẹo Vặt", "pages/8_💡_Mẹo_Vặt.py"),
            ("🆘 SOS", "pages/12_🆘_SOS.py"),
        ]
        
        # Hiển thị menu items
        for label, page_path in menu_items:
            if st.button(label, key=f"menu_{page_path}", use_container_width=True):
                st.switch_page(page_path)
        
        st.divider()
        
        # Quick Actions - Các trang phụ trợ (ẩn khỏi menu chính)
        st.markdown("### 🚀 Truy cập nhanh")
        
        quick_actions = [
            ("🤖 AI Bác Sĩ", "pages/_🤖_AI_Bác_Sĩ.py"),
            ("📊 Nhật Ký", "pages/_📊_Nhật_Ký.py"),
            ("💊 Nhắc Thuốc", "pages/_💊_Nhắc_Thuốc.py"),
            ("📈 Xu Hướng", "pages/_📈_Xu_Hướng.py"),
        ]
        
        for label, page_path in quick_actions:
            if st.button(label, key=f"quick_{page_path}", use_container_width=True):
                st.switch_page(page_path)

