"""
Favorites Manager - Quản lý trang yêu thích
Lưu danh sách trang người dùng đánh dấu
"""

import streamlit as st


def init_favorites():
    """Khởi tạo danh sách favorites trong session state"""
    if 'favorites' not in st.session_state:
        st.session_state.favorites = []


def add_to_favorites(page_name, page_label):
    """Thêm trang vào favorites"""
    init_favorites()
    
    favorite_item = {
        "page": page_name,
        "label": page_label
    }
    
    # Kiểm tra xem đã có chưa
    if not any(fav['page'] == page_name for fav in st.session_state.favorites):
        st.session_state.favorites.append(favorite_item)
        # Giới hạn tối đa 10 mục
        if len(st.session_state.favorites) > 10:
            st.session_state.favorites.pop(0)
        return True
    return False


def remove_from_favorites(page_name):
    """Xóa trang khỏi favorites"""
    init_favorites()
    
    st.session_state.favorites = [
        fav for fav in st.session_state.favorites 
        if fav['page'] != page_name
    ]


def is_favorite(page_name):
    """Kiểm tra xem trang có trong favorites không"""
    init_favorites()
    return any(fav['page'] == page_name for fav in st.session_state.favorites)


def get_favorites():
    """Lấy danh sách favorites"""
    init_favorites()
    return st.session_state.favorites


def render_favorite_button(page_name, page_label):
    """
    Render nút đánh dấu yêu thích
    Trả về True nếu đã thêm, False nếu đã xóa
    """
    init_favorites()
    
    is_fav = is_favorite(page_name)
    
    if is_fav:
        if st.button("⭐ Bỏ yêu thích", key=f"unfav_{page_name}"):
            remove_from_favorites(page_name)
            st.rerun()
            return False
    else:
        if st.button("⭐ Thêm vào Yêu thích", key=f"fav_{page_name}"):
            add_to_favorites(page_name, page_label)
            st.success(f"Đã thêm {page_label} vào yêu thích!")
            st.rerun()
            return True
    
    return is_fav


def render_favorites_sidebar():
    """Hiển thị favorites trong sidebar"""
    init_favorites()
    
    favorites = get_favorites()
    
    if favorites:
        st.markdown("### ⭐ Yêu thích của tôi")
        
        # Hiển thị tối đa 10 mục
        for fav in reversed(favorites[-10:]):
            page_path = f"pages/{fav['page']}.py"
            st.page_link(page_path, label=fav['label'], icon=None)
        
        if len(favorites) > 10:
            st.caption(f"... và {len(favorites) - 10} mục khác")


def render_favorites_home():
    """Hiển thị favorites ở trang chủ"""
    init_favorites()
    
    favorites = get_favorites()
    
    if favorites:
        st.markdown("### ⭐ Trang của tôi")
        
        cols = st.columns(min(len(favorites), 4))
        for idx, fav in enumerate(favorites[-8:]):  # Hiển thị tối đa 8 mục
            with cols[idx % 4]:
                if st.button(fav['label'], key=f"home_fav_{idx}", use_container_width=True):
                    page_path = f"pages/{fav['page']}.py"
                    st.switch_page(page_path)

