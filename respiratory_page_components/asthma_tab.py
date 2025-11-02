"""
Asthma Tab Component
Hiển thị thông tin về bệnh Hen Suyễn

REFACTORED: Tách thành helper functions
"""

import streamlit as st
from .asthma_tab_helpers import render_asthma_info_and_symptoms, render_asthma_triggers_and_severity
from .asthma_tab_treatment import render_asthma_treatment, render_asthma_management


def render_asthma_tab():
    """Render tab Asthma với đầy đủ thông tin"""
    st.header("🌬️ Hen Suyễn (Asthma)")
    
    render_asthma_info_and_symptoms()
    render_asthma_triggers_and_severity()
    render_asthma_treatment()
    render_asthma_management()
