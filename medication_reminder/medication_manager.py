"""
Medication Manager - Quản lý danh sách thuốc
"""
import streamlit as st
import pandas as pd
from datetime import datetime
import json
import os

# File lưu trữ dữ liệu
DATA_FILE = "data/medications.json"

@st.cache_data(ttl=60, show_spinner=False)  # Cache 1 phút
def load_medications():
    """Đọc danh sách thuốc từ file"""
    if not os.path.exists(DATA_FILE):
        os.makedirs("data", exist_ok=True)
        return []
    
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def save_medications(medications):
    """Lưu danh sách thuốc vào file"""
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(medications, f, ensure_ascii=False, indent=2)
    
    # Xóa cache để reload dữ liệu mới
    load_medications.clear()

def add_medication(name, dosage, frequency, times, notes="", start_date=None):
    """
    Thêm thuốc mới
    
    Args:
        name: Tên thuốc
        dosage: Liều lượng (VD: "500mg", "1 viên")
        frequency: Tần suất (VD: "Mỗi ngày", "2 ngày/lần")
        times: Danh sách giờ uống (VD: ["08:00", "20:00"])
        notes: Ghi chú
        start_date: Ngày bắt đầu uống
    """
    medications = load_medications()
    
    new_med = {
        "id": str(datetime.now().timestamp()),
        "name": name,
        "dosage": dosage,
        "frequency": frequency,
        "times": times,
        "notes": notes,
        "start_date": start_date or datetime.now().strftime("%Y-%m-%d"),
        "active": True,
        "created_at": datetime.now().isoformat()
    }
    
    medications.append(new_med)
    save_medications(medications)
    return True

def edit_medication(med_id, **kwargs):
    """Sửa thông tin thuốc"""
    medications = load_medications()
    
    for med in medications:
        if med['id'] == med_id:
            med.update(kwargs)
            med['updated_at'] = datetime.now().isoformat()
            break
    
    save_medications(medications)
    return True

def delete_medication(med_id):
    """Xóa thuốc (chuyển sang inactive)"""
    medications = load_medications()
    
    for med in medications:
        if med['id'] == med_id:
            med['active'] = False
            med['deleted_at'] = datetime.now().isoformat()
            break
    
    save_medications(medications)
    return True

def get_all_medications(active_only=True):
    """Lấy danh sách tất cả thuốc"""
    medications = load_medications()
    
    if active_only:
        return [m for m in medications if m.get('active', True)]
    
    return medications

def render_medication_form():
    """Hiển thị form thêm/sửa thuốc"""
    st.subheader("➕ Thêm thuốc mới")
    
    with st.form("add_medication_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input(
                "🏷️ Tên thuốc *",
                placeholder="VD: Metformin, Amlodipine...",
                help="Tên thương mại hoặc tên hoạt chất"
            )
            
            dosage = st.text_input(
                "💊 Liều lượng *",
                placeholder="VD: 500mg, 1 viên, 5ml...",
                help="Liều lượng mỗi lần uống"
            )
        
        with col2:
            frequency = st.selectbox(
                "📅 Tần suất *",
                [
                    "Mỗi ngày",
                    "2 ngày/lần",
                    "3 ngày/lần",
                    "1 tuần/lần",
                    "Khi cần thiết"
                ]
            )
            
            start_date = st.date_input(
                "📆 Ngày bắt đầu",
                value=datetime.now()
            )
        
        st.markdown("### ⏰ Giờ uống thuốc")
        st.info("💡 **Mẹo:** Chọn giờ cố định mỗi ngày để dễ nhớ. VD: 8h sáng, 8h tối")
        
        # Cho phép thêm nhiều giờ uống
        num_times = st.number_input("Số lần uống mỗi ngày", min_value=1, max_value=6, value=1)
        
        times = []
        cols = st.columns(min(num_times, 3))  # Tối đa 3 cột
        
        for i in range(num_times):
            with cols[i % 3]:
                time = st.time_input(
                    f"Lần {i+1}",
                    value=datetime.strptime(f"{8+i*4}:00", "%H:%M").time(),
                    key=f"time_{i}"
                )
                times.append(time.strftime("%H:%M"))
        
        notes = st.text_area(
            "📝 Ghi chú",
            placeholder="VD: Uống sau ăn, không uống cùng sữa...",
            help="Ghi chú về cách dùng, tác dụng phụ cần lưu ý..."
        )
        
        submitted = st.form_submit_button("✅ Thêm thuốc", use_container_width=True)
        
        if submitted:
            if not name or not dosage:
                st.error("⚠️ Vui lòng nhập đầy đủ tên thuốc và liều lượng!")
                return False
            
            success = add_medication(
                name=name,
                dosage=dosage,
                frequency=frequency,
                times=times,
                notes=notes,
                start_date=start_date.strftime("%Y-%m-%d")
            )
            
            if success:
                st.success(f"✅ Đã thêm thuốc **{name}** vào danh sách!")
                st.balloons()
                return True
            else:
                st.error("❌ Có lỗi xảy ra. Vui lòng thử lại!")
                return False
    
    return None

def render_medication_list():
    """Hiển thị danh sách thuốc"""
    medications = get_all_medications()
    
    if not medications:
        st.info("📝 Chưa có thuốc nào. Hãy thêm thuốc đầu tiên!")
        return
    
    st.subheader(f"📋 Danh sách thuốc ({len(medications)} thuốc)")
    
    for med in medications:
        with st.expander(f"💊 {med['name']} - {med['dosage']}", expanded=False):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"**📅 Tần suất:** {med['frequency']}")
                st.markdown(f"**⏰ Giờ uống:** {', '.join(med['times'])}")
                
                if med.get('notes'):
                    st.markdown(f"**📝 Ghi chú:** {med['notes']}")
                
                st.caption(f"Bắt đầu từ: {med['start_date']}")
            
            with col2:
                if st.button("🗑️ Xóa", key=f"del_{med['id']}"):
                    if delete_medication(med['id']):
                        st.success("Đã xóa!")
                        st.rerun()

