"""
Viêm phổi (Pneumonia) Tab Component
Hiển thị thông tin về bệnh Viêm phổi

REFACTORED: Tách thành helper functions
"""

import streamlit as st
from .pneumonia_tab_info import render_pneumonia_info, render_pneumonia_causes, render_pneumonia_symptoms
from .pneumonia_tab_treatment import render_pneumonia_diagnosis, render_pneumonia_treatment, render_pneumonia_prevention, render_pneumonia_complications


def render_pneumonia_tab():
    """Render tab Viêm phổi với đầy đủ thông tin"""
    st.header("🫁 Viêm phổi (Pneumonia)")
    
    render_pneumonia_info()
    render_pneumonia_causes()
    render_pneumonia_symptoms()
    render_pneumonia_diagnosis()
    render_pneumonia_treatment()
    render_pneumonia_prevention()
    render_pneumonia_complications()
