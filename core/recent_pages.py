"""
Recent Pages Manager - Theo dõi các trang đã xem gần đây
"""

import streamlit as st


def init_recent():
    """Khởi tạo danh sách recent pages"""
    if 'recent_pages' not in st.session_state:
        st.session_state.recent_pages = []


def add_to_recent(page_name, page_label):
    """Thêm trang vào recent (không trùng lặp, giới hạn 10 mục)"""
    init_recent()
    
    # Xóa nếu đã có (để đưa lên đầu)
    st.session_state.recent_pages = [
        rp for rp in st.session_state.recent_pages 
        if rp['page'] != page_name
    ]
    
    # Thêm vào đầu
    recent_item = {
        "page": page_name,
        "label": page_label
    }
    st.session_state.recent_pages.insert(0, recent_item)
    
    # Giới hạn 10 mục
    if len(st.session_state.recent_pages) > 10:
        st.session_state.recent_pages.pop()


def get_recent_pages():
    """Lấy danh sách recent pages"""
    init_recent()
    return st.session_state.recent_pages


def render_recent_sidebar():
    """Hiển thị recent pages trong sidebar"""
    init_recent()
    
    recent = get_recent_pages()
    
    if recent:
        st.markdown("### 🕒 Đã xem gần đây")
        
        # Hiển thị tối đa 5 mục gần nhất
        for rp in recent[:5]:
            page_path = f"pages/{rp['page']}.py"
            st.page_link(page_path, label=rp['label'], icon=None)


def render_recent_home():
    """Hiển thị recent pages ở trang chủ"""
    init_recent()
    
    recent = get_recent_pages()
    
    if recent:
        st.markdown("### 🕒 Đã xem gần đây")
        
        cols = st.columns(min(len(recent), 4))
        for idx, rp in enumerate(recent[:8]):  # Hiển thị tối đa 8 mục
            with cols[idx % 4]:
                if st.button(rp['label'], key=f"home_recent_{idx}", use_container_width=True):
                    page_path = f"pages/{rp['page']}.py"
                    st.switch_page(page_path)

