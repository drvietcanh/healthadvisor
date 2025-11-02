"""
Contact Manager - Quản lý danh bạ cá nhân và thông tin y tế
"""
import json
import os
from datetime import datetime
import streamlit as st

CONTACTS_FILE = "data/emergency_contacts.json"
MEDICAL_INFO_FILE = "data/medical_info.json"

@st.cache_data(ttl=60, show_spinner=False)  # Cache 1 phút
def load_contacts():
    """Đọc danh sách contacts"""
    if not os.path.exists(CONTACTS_FILE):
        return []
    
    try:
        with open(CONTACTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def save_contacts(contacts):
    """Lưu danh sách contacts"""
    os.makedirs("data", exist_ok=True)
    with open(CONTACTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)
    
    # Xóa cache để reload dữ liệu mới
    load_contacts.clear()

def add_personal_contact(name, phone, relationship, notes=""):
    """
    Thêm contact cá nhân
    
    Args:
        name: Tên người liên hệ
        phone: Số điện thoại
        relationship: Mối quan hệ (Con, Cháu, Bác sĩ...)
        notes: Ghi chú
    """
    contacts = load_contacts()
    
    new_contact = {
        "id": str(datetime.now().timestamp()),
        "name": name,
        "phone": phone,
        "relationship": relationship,
        "notes": notes,
        "created_at": datetime.now().isoformat()
    }
    
    contacts.append(new_contact)
    save_contacts(contacts)
    return True

def delete_personal_contact(contact_id):
    """Xóa contact"""
    contacts = load_contacts()
    contacts = [c for c in contacts if c['id'] != contact_id]
    save_contacts(contacts)
    return True

def get_all_personal_contacts():
    """Lấy tất cả contacts"""
    return load_contacts()

# ============= THÔNG TIN Y TẾ =============

@st.cache_data(ttl=60, show_spinner=False)  # Cache 1 phút
def load_medical_info():
    """Đọc thông tin y tế"""
    if not os.path.exists(MEDICAL_INFO_FILE):
        return {
            "medications": "",
            "allergies": "",
            "conditions": "",
            "blood_type": "",
            "notes": ""
        }
    
    try:
        with open(MEDICAL_INFO_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {
            "medications": "",
            "allergies": "",
            "conditions": "",
            "blood_type": "",
            "notes": ""
        }

def save_medical_info(medications="", allergies="", conditions="", blood_type="", notes=""):
    """
    Lưu thông tin y tế khẩn cấp
    
    Args:
        medications: Thuốc đang uống
        allergies: Dị ứng thuốc/thực phẩm
        conditions: Bệnh nền
        blood_type: Nhóm máu
        notes: Ghi chú khác
    """
    os.makedirs("data", exist_ok=True)
    
    info = {
        "medications": medications,
        "allergies": allergies,
        "conditions": conditions,
        "blood_type": blood_type,
        "notes": notes,
        "updated_at": datetime.now().isoformat()
    }
    
    with open(MEDICAL_INFO_FILE, 'w', encoding='utf-8') as f:
        json.dump(info, f, ensure_ascii=False, indent=2)
    
    # Xóa cache để reload dữ liệu mới
    load_medical_info.clear()
    
    return True

def get_medical_info():
    """Lấy thông tin y tế"""
    return load_medical_info()

