"""
Trang Tìm Kiếm - Hiển thị kết quả tìm kiếm
"""

import streamlit as st
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.search_component import render_search_results, SEARCH_INDEX, PAGE_LINKS
from core.ui_config import get_custom_css
from core.sidebar_menu import render_sidebar_menu, hide_default_nav

st.set_page_config(page_title="Tìm Kiếm", page_icon="🔍", layout="wide")

# Ẩn menu mặc định
hide_default_nav()

# Render menu sidebar
render_sidebar_menu()

# Áp dụng CSS
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
extra_large_font = st.session_state.get('extra_large_font', False)
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode, extra_large_font=extra_large_font), unsafe_allow_html=True)

st.title("🔍 Tìm Kiếm")

# Lấy query từ session state hoặc từ input
if 'search_query' in st.session_state:
    query = st.session_state.search_query
else:
    query = ""

# Search box
search_input = st.text_input(
    "Nhập từ khóa tìm kiếm",
    value=query,
    placeholder="Ví dụ: đau tim, tăng huyết áp, bỏng, sốt...",
    key="search_input_main"
)

# Nếu có query, tìm kiếm
if search_input:
    st.session_state.search_query = search_input
    results = render_search_results(search_input)
    
    if results:
        st.success(f"Tìm thấy {len(results)} kết quả cho: **{search_input}**")
        st.divider()
        
        # Hiển thị kết quả theo loại
        st.markdown("### 📋 Kết quả tìm kiếm:")
        
        for i, result in enumerate(results):
            with st.expander(f"{result.get('label', '')} - {result.get('section', '')}", expanded=(i == 0)):
                st.markdown(f"**Từ khóa:** {result['keyword']}")
                st.markdown(f"**Trang:** {result.get('label', '')}")
                if result.get('section'):
                    st.markdown(f"**Phần:** {result['section']}")
                
                if st.button(f"👉 Vào trang {result.get('label', '')}", key=f"goto_{i}"):
                    page_path = f"pages/{result['page']}.py"
                    st.switch_page(page_path)
    else:
        st.warning(f"Không tìm thấy kết quả cho: **{search_input}**")
        st.info("💡 **Gợi ý:**")
        st.markdown("""
        - Kiểm tra lại chính tả
        - Thử từ khóa khác (ví dụ: "đau tim" thay vì "đau tim cấp")
        - Tìm kiếm theo tên bệnh hoặc triệu chứng
        """)
        
        # Gợi ý từ khóa phổ biến
        st.markdown("### 🔤 Từ khóa phổ biến:")
        popular_keywords = [
            "đau tim", "đột quỵ", "tăng huyết áp", "tiểu đường", 
            "bỏng", "hóc dị vật", "sốt", "đau đầu"
        ]
        cols = st.columns(4)
        for idx, keyword in enumerate(popular_keywords):
            with cols[idx % 4]:
                if st.button(f"🔍 {keyword}", key=f"popular_{idx}"):
                    st.session_state.search_query = keyword
                    st.rerun()
else:
    st.info("👆 Nhập từ khóa vào ô tìm kiếm phía trên để bắt đầu")
    
    # Hiển thị số lượng từ khóa có sẵn
    st.markdown(f"""
    **💡 Mẹo tìm kiếm:**
    - Tìm theo **tên bệnh**: đau tim, tiểu đường, đột quỵ...
    - Tìm theo **triệu chứng**: sốt, đau đầu, chảy máu...
    - Tìm theo **tình huống cấp cứu**: bỏng, hóc dị vật, ngộ độc...
    - Tìm theo **chuyên khoa**: tim mạch, hô hấp, thần kinh...
    
    **📊 Hiện có:** {len(SEARCH_INDEX)} từ khóa về bệnh và {len(PAGE_LINKS)} trang có thể tìm kiếm
    """)

# Nút quay lại
st.divider()
if st.button("⬅️ Quay lại trang chính"):
    st.switch_page("app.py")

