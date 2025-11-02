"""
Scheduler - Lịch nhắc uống thuốc
"""
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import json
import os
from .medication_manager import get_all_medications

# File lưu lịch sử
HISTORY_FILE = "data/medication_history.json"

@st.cache_data(ttl=60, show_spinner=False)  # Cache 1 phút
def load_history():
    """Đọc lịch sử uống thuốc"""
    if not os.path.exists(HISTORY_FILE):
        return []
    
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def save_history(history):
    """Lưu lịch sử uống thuốc"""
    os.makedirs("data", exist_ok=True)
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
    
    # Xóa cache để reload dữ liệu mới
    load_history.clear()

def mark_as_taken(med_id, scheduled_time, actual_time=None, notes=""):
    """Đánh dấu đã uống thuốc"""
    history = load_history()
    
    record = {
        "id": str(datetime.now().timestamp()),
        "med_id": med_id,
        "scheduled_time": scheduled_time,
        "actual_time": actual_time or datetime.now().isoformat(),
        "status": "taken",
        "notes": notes
    }
    
    history.append(record)
    save_history(history)
    return True

def mark_as_skipped(med_id, scheduled_time, reason=""):
    """Đánh dấu bỏ qua (không uống)"""
    history = load_history()
    
    record = {
        "id": str(datetime.now().timestamp()),
        "med_id": med_id,
        "scheduled_time": scheduled_time,
        "actual_time": datetime.now().isoformat(),
        "status": "skipped",
        "notes": reason
    }
    
    history.append(record)
    save_history(history)
    return True

def get_today_schedule():
    """Lấy lịch uống thuốc hôm nay"""
    medications = get_all_medications()
    today = datetime.now().date()
    
    schedule = []
    
    for med in medications:
        for time_str in med['times']:
            scheduled_dt = datetime.strptime(f"{today} {time_str}", "%Y-%m-%d %H:%M")
            
            # Kiểm tra đã uống chưa
            history = load_history()
            taken = False
            
            for record in history:
                if (record['med_id'] == med['id'] and 
                    record['scheduled_time'].startswith(str(today)) and
                    time_str in record['scheduled_time'] and
                    record['status'] == 'taken'):
                    taken = True
                    break
            
            schedule.append({
                "med_id": med['id'],
                "med_name": med['name'],
                "dosage": med['dosage'],
                "time": time_str,
                "datetime": scheduled_dt,
                "taken": taken,
                "notes": med.get('notes', '')
            })
    
    # Sắp xếp theo thời gian
    schedule.sort(key=lambda x: x['datetime'])
    
    return schedule

def get_upcoming_doses(hours=24):
    """Lấy các liều thuốc sắp tới"""
    schedule = get_today_schedule()
    now = datetime.now()
    
    upcoming = [
        dose for dose in schedule
        if dose['datetime'] > now and dose['datetime'] <= now + timedelta(hours=hours)
        and not dose['taken']
    ]
    
    return upcoming

def render_schedule_view():
    """Hiển thị lịch uống thuốc hôm nay"""
    st.subheader("📅 Lịch uống thuốc hôm nay")
    
    today_str = datetime.now().strftime("%A, %d/%m/%Y")
    st.markdown(f"**{today_str}**")
    
    schedule = get_today_schedule()
    
    if not schedule:
        st.info("📝 Chưa có lịch uống thuốc nào. Hãy thêm thuốc trước!")
        return
    
    # Thống kê
    total = len(schedule)
    taken = sum(1 for s in schedule if s['taken'])
    remaining = total - taken
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📊 Tổng số liều", total)
    with col2:
        st.metric("✅ Đã uống", taken, delta=f"{taken/total*100:.0f}%" if total > 0 else "0%")
    with col3:
        st.metric("⏳ Còn lại", remaining)
    
    st.divider()
    
    # Hiển thị lịch
    now = datetime.now()
    
    for dose in schedule:
        is_past = dose['datetime'] < now
        is_near = now <= dose['datetime'] <= now + timedelta(minutes=30)
        
        # Màu sắc và icon
        if dose['taken']:
            icon = "✅"
            color = "green"
        elif is_past and not dose['taken']:
            icon = "⚠️"
            color = "red"
        elif is_near:
            icon = "🔔"
            color = "orange"
        else:
            icon = "⏰"
            color = "blue"
        
        # Hiển thị
        with st.container():
            col_time, col_med, col_action = st.columns([1, 3, 2])
            
            with col_time:
                st.markdown(f"### {icon} {dose['time']}")
                if is_past and not dose['taken']:
                    st.caption("⚠️ Trễ giờ")
                elif is_near:
                    st.caption("🔔 Sắp tới!")
            
            with col_med:
                st.markdown(f"**{dose['med_name']}**")
                st.caption(f"Liều lượng: {dose['dosage']}")
                if dose['notes']:
                    st.caption(f"💡 {dose['notes']}")
            
            with col_action:
                if not dose['taken']:
                    col_a, col_b = st.columns(2)
                    
                    with col_a:
                        if st.button("✅ Đã uống", key=f"taken_{dose['med_id']}_{dose['time']}", use_container_width=True):
                            scheduled_time = dose['datetime'].isoformat()
                            if mark_as_taken(dose['med_id'], scheduled_time):
                                st.success("✅ Đã ghi nhận!")
                                st.rerun()
                    
                    with col_b:
                        if st.button("⏭️ Bỏ qua", key=f"skip_{dose['med_id']}_{dose['time']}", use_container_width=True):
                            scheduled_time = dose['datetime'].isoformat()
                            if mark_as_skipped(dose['med_id'], scheduled_time):
                                st.info("Đã bỏ qua")
                                st.rerun()
                else:
                    st.success("✅ Đã uống")
            
            st.divider()
    
    # Nhắc nhở
    upcoming = get_upcoming_doses(hours=2)
    if upcoming:
        st.info(f"🔔 **Sắp tới:** {len(upcoming)} liều thuốc trong 2 giờ tới!")

