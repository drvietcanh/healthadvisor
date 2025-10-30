"""
Emergency Contacts - Quản lý số điện thoại cấp cứu
"""

from .contact_manager import (
    add_personal_contact,
    delete_personal_contact,
    get_all_personal_contacts,
    save_medical_info,
    get_medical_info
)

from .emergency_numbers import (
    VIETNAM_EMERGENCY_NUMBERS,
    get_emergency_number_by_type
)

from .first_aid import (
    FIRST_AID_GUIDES,
    get_first_aid_guide
)

__all__ = [
    'add_personal_contact',
    'delete_personal_contact',
    'get_all_personal_contacts',
    'save_medical_info',
    'get_medical_info',
    'VIETNAM_EMERGENCY_NUMBERS',
    'get_emergency_number_by_type',
    'FIRST_AID_GUIDES',
    'get_first_aid_guide',
]

