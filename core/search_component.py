"""
Search Component - Tìm kiếm thông minh
Hỗ trợ tìm kiếm bệnh, triệu chứng, mẹo vặt, cấp cứu
"""

import streamlit as st
from difflib import get_close_matches

# Dictionary tra cứu - Tất cả các từ khóa có thể tìm kiếm
SEARCH_INDEX = {
    # Chuyên khoa Tim Mạch
    "tăng huyết áp": {"page": "1_❤️_Tim_Mạch", "label": "❤️ Tim Mạch", "section": "🩺 Tăng Huyết Áp"},
    "huyết áp cao": {"page": "1_❤️_Tim_Mạch", "label": "❤️ Tim Mạch", "section": "🩺 Tăng Huyết Áp"},
    "suy tim": {"page": "1_❤️_Tim_Mạch", "label": "❤️ Tim Mạch", "section": "💔 Suy Tim"},
    "nhồi máu cơ tim": {"page": "1_❤️_Tim_Mạch", "label": "❤️ Tim Mạch", "section": "💔 Nhồi Máu Cơ Tim"},
    "rối loạn nhịp tim": {"page": "1_❤️_Tim_Mạch", "label": "❤️ Tim Mạch", "section": "❤️‍🩹 Rối Loạn Nhịp Tim"},
    "xơ vữa động mạch": {"page": "1_❤️_Tim_Mạch", "label": "❤️ Tim Mạch", "section": "🫀 Xơ Vữa Động Mạch"},
    "rối loạn lipid": {"page": "1_❤️_Tim_Mạch", "label": "❤️ Tim Mạch", "section": "🧈 Rối Loạn Lipid Máu"},
    
    # Chuyên khoa Hô Hấp
    "copd": {"page": "2_🫁_Hô_Hấp", "label": "🫁 Hô Hấp", "section": "🫁 COPD"},
    "hen suyễn": {"page": "2_🫁_Hô_Hấp", "label": "🫁 Hô Hấp", "section": "🌬️ Hen Suyễn"},
    "viêm phổi": {"page": "2_🫁_Hô_Hấp", "label": "🫁 Hô Hấp", "section": "🫁 Viêm phổi"},
    "ho mãn tính": {"page": "2_🫁_Hô_Hấp", "label": "🫁 Hô Hấp", "section": "🤧 Ho Mãn Tính"},
    
    # Tiểu Đường
    "tiểu đường": {"page": "3_🩸_Tiểu_Đường", "label": "🩸 Tiểu Đường", "section": "Tất cả"},
    "đái tháo đường": {"page": "3_🩸_Tiểu_Đường", "label": "🩸 Tiểu Đường", "section": "Tất cả"},
    "đường huyết": {"page": "3_🩸_Tiểu_Đường", "label": "🩸 Tiểu Đường", "section": "Tất cả"},
    
    # Thần Kinh
    "đột quỵ": {"page": "4_🧠_Thần_Kinh", "label": "🧠 Thần Kinh", "section": "🚨 Đột Quỵ"},
    "tai biến": {"page": "4_🧠_Thần_Kinh", "label": "🧠 Thần Kinh", "section": "🚨 Đột Quỵ"},
    "động kinh": {"page": "4_🧠_Thần_Kinh", "label": "🧠 Thần Kinh", "section": "⚡ Động Kinh"},
    "đau đầu": {"page": "4_🧠_Thần_Kinh", "label": "🧠 Thần Kinh", "section": "💆 Đau Đầu"},
    "migraine": {"page": "4_🧠_Thần_Kinh", "label": "🧠 Thần Kinh", "section": "💆 Đau Đầu"},
    "sa sút trí tuệ": {"page": "4_🧠_Thần_Kinh", "label": "🧠 Thần Kinh", "section": "🧠 Sa Sút Trí Tuệ"},
    "mất ngủ": {"page": "4_🧠_Thần_Kinh", "label": "🧠 Thần Kinh", "section": "😴 Mất Ngủ"},
    
    # Khớp-Cột Sống
    "thoái hóa khớp": {"page": "6_🦴_Khớp_Cột_Sống", "label": "🦴 Khớp-Cột Sống", "section": "🦴 Thoái hóa khớp"},
    "viêm khớp": {"page": "6_🦴_Khớp_Cột_Sống", "label": "🦴 Khớp-Cột Sống", "section": "🔴 Viêm khớp dạng thấp"},
    "đau lưng": {"page": "6_🦴_Khớp_Cột_Sống", "label": "🦴 Khớp-Cột Sống", "section": "🫁 Đau thắt lưng"},
    "thoát vị đĩa đệm": {"page": "6_🦴_Khớp_Cột_Sống", "label": "🦴 Khớp-Cột Sống", "section": "💔 Thoát vị đĩa đệm"},
    "đau cổ vai gáy": {"page": "6_🦴_Khớp_Cột_Sống", "label": "🦴 Khớp-Cột Sống", "section": "💆 Đau Cổ Vai Gáy"},
    "gút": {"page": "6_🦴_Khớp_Cột_Sống", "label": "🦴 Khớp-Cột Sống", "section": "🦶 Bệnh Gút"},
    "loãng xương": {"page": "6_🦴_Khớp_Cột_Sống", "label": "🦴 Khớp-Cột Sống", "section": "🦴 Loãng Xương"},
    
    # Thận-Tiết Niệu
    "suy thận": {"page": "9_🧪_Thận_Tiết_Niệu", "label": "🧪 Thận-Tiết Niệu", "section": "🫘 Suy Thận Mạn"},
    "sỏi thận": {"page": "9_🧪_Thận_Tiết_Niệu", "label": "🧪 Thận-Tiết Niệu", "section": "🪨 Sỏi Thận"},
    
    # Mắt
    "đục thủy tinh thể": {"page": "10_👁️_Mắt", "label": "👁️ Mắt", "section": "👁️ Đục Thủy Tinh Thể"},
    "tăng nhãn áp": {"page": "10_👁️_Mắt", "label": "👁️ Mắt", "section": "👁️ Tăng Nhãn Áp"},
    "glaucoma": {"page": "10_👁️_Mắt", "label": "👁️ Mắt", "section": "👁️ Tăng Nhãn Áp"},
    "thoái hóa hoàng điểm": {"page": "10_👁️_Mắt", "label": "👁️ Mắt", "section": "👁️ Thoái Hóa Hoàng Điểm"},
    "khô mắt": {"page": "10_👁️_Mắt", "label": "👁️ Mắt", "section": "👁️ Khô Mắt"},
    
    # Tiêu Hóa
    "trào ngược dạ dày": {"page": "11_🌡️_Tiêu_Hóa", "label": "🌡️ Tiêu Hóa", "section": "🌡️ Trào Ngược Dạ Dày"},
    "gerd": {"page": "11_🌡️_Tiêu_Hóa", "label": "🌡️ Tiêu Hóa", "section": "🌡️ Trào Ngược Dạ Dày"},
    "táo bón": {"page": "11_🌡️_Tiêu_Hóa", "label": "🌡️ Tiêu Hóa", "section": "🚽 Táo Bón"},
    
    # Cấp cứu SOS
    "đau tim": {"page": "12_🆘_SOS", "label": "🆘 SOS", "section": "❤️ Đau tim cấp"},
    "đột quỵ": {"page": "12_🆘_SOS", "label": "🆘 SOS", "section": "🧠 Đột quỵ (BE-FAST)"},
    "hóc dị vật": {"page": "12_🆘_SOS", "label": "🆘 SOS", "section": "😰 Người lớn hóc dị vật"},
    "bỏng": {"page": "12_🆘_SOS", "label": "🆘 SOS", "section": "🔥 Bỏng nhiệt/Nước sôi"},
    "chảy máu": {"page": "12_🆘_SOS", "label": "🆘 SOS", "section": "🩸 Chảy máu"},
    "ngộ độc": {"page": "12_🆘_SOS", "label": "🆘 SOS", "section": "☠️ Ngộ độc"},
    "cpr": {"page": "12_🆘_SOS", "label": "🆘 SOS", "section": "💔 Ngừng tim - CPR"},
    "sốc nhiệt": {"page": "12_🆘_SOS", "label": "🆘 SOS", "section": "☀️ Sốc nhiệt/Cảm nắng"},
    
    # Mẹo vặt
    "paracetamol": {"page": "8_💡_Mẹo_Vặt", "label": "💡 Mẹo Vặt", "section": "Paracetamol"},
    "sốt": {"page": "8_💡_Mẹo_Vặt", "label": "💡 Mẹo Vặt", "section": "Sốt"},
    "nhiệt độ": {"page": "8_💡_Mẹo_Vặt", "label": "💡 Mẹo Vặt", "section": "Nhiệt độ"},
}

# Danh sách trang đơn giản (chỉ cần link đến trang)
PAGE_LINKS = {
    "hướng dẫn": "0_📖_Hướng_Dẫn",
    "học dễ": "7_🎓_Học_Dễ",
    "mẹo vặt": "8_💡_Mẹo_Vặt",
    "ai bác sĩ": "_🤖_AI_Bác_Sĩ",
    "nhắc thuốc": "_💊_Nhắc_Thuốc",
    "nhật ký": "_📊_Nhật_Ký",
    "xu hướng": "_📈_Xu_Hướng",
    "sos": "12_🆘_SOS",
}


def search_items(query):
    """
    Tìm kiếm items dựa trên query
    Trả về danh sách kết quả phù hợp
    """
    query_lower = query.lower().strip()
    results = []
    
    if not query_lower:
        return results
    
    # Tìm exact match
    if query_lower in SEARCH_INDEX:
        results.append({
            "type": "exact",
            "keyword": query_lower,
            **SEARCH_INDEX[query_lower]
        })
    
    # Tìm fuzzy match (gần đúng)
    all_keys = list(SEARCH_INDEX.keys())
    matches = get_close_matches(query_lower, all_keys, n=5, cutoff=0.6)
    
    for match in matches:
        if match not in [r["keyword"] for r in results]:  # Tránh trùng
            results.append({
                "type": "fuzzy",
                "keyword": match,
                **SEARCH_INDEX[match]
            })
    
    # Tìm từ khóa chứa query
    for key, value in SEARCH_INDEX.items():
        if query_lower in key and key not in [r["keyword"] for r in results]:
            results.append({
                "type": "contains",
                "keyword": key,
                **value
            })
    
    # Tìm trong PAGE_LINKS
    for key, page in PAGE_LINKS.items():
        if query_lower in key or key in query_lower:
            results.append({
                "type": "page",
                "keyword": key,
                "page": page,
                "label": key.title(),
                "section": "Trang chính"
            })
    
    # Giới hạn 10 kết quả
    return results[:10]


def render_search_bar():
    """
    Render search bar trong sidebar
    """
    st.markdown("### 🔍 Tìm kiếm")
    
    # Lưu lịch sử tìm kiếm
    if 'search_history' not in st.session_state:
        st.session_state.search_history = []
    
    # Search input
    search_query = st.text_input(
        "Nhập từ khóa tìm kiếm",
        key="search_input",
        placeholder="Ví dụ: đau tim, tăng huyết áp, bỏng...",
        help="Tìm kiếm bệnh, triệu chứng, mẹo vặt, cấp cứu"
    )
    
    # Lịch sử tìm kiếm
    if st.session_state.search_history:
        st.caption("📋 Tìm kiếm gần đây:")
        for i, history_item in enumerate(reversed(st.session_state.search_history[-5:])):
            if st.button(f"🔍 {history_item}", key=f"history_{i}", use_container_width=True):
                st.session_state.search_input = history_item
                st.rerun()
    
    # Nếu có query, chuyển đến trang tìm kiếm
    if search_query:
        st.session_state.search_query = search_query
        
        # Thêm vào lịch sử (nếu chưa có)
        if search_query not in st.session_state.search_history:
            st.session_state.search_history.append(search_query)
            # Giữ tối đa 10 mục
            if len(st.session_state.search_history) > 10:
                st.session_state.search_history.pop(0)
        
        # Chuyển đến trang tìm kiếm
        st.switch_page("pages/_🔍_Tìm_Kiếm.py")


def render_search_results(query):
    """
    Render kết quả tìm kiếm
    Trả về danh sách kết quả để hiển thị
    """
    results = search_items(query)
    return results

