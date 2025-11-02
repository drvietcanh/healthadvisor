"""
Osteoporosis Tab Component
Hiển thị thông tin về Loãng Xương

REFACTORED: Tách thành helper functions
"""

import streamlit as st
from .osteoporosis_tab_info import render_osteoporosis_info, render_osteoporosis_causes, render_osteoporosis_symptoms
from .osteoporosis_tab_treatment import render_osteoporosis_diagnosis, render_osteoporosis_treatment, render_osteoporosis_nutrition, render_osteoporosis_prevention


def render_osteoporosis_tab():
    """Tab Loãng Xương"""
    st.header("🦴 Loãng Xương (Osteoporosis)")
    
    render_osteoporosis_info()
    render_osteoporosis_causes()
    render_osteoporosis_symptoms()
    render_osteoporosis_diagnosis()
    render_osteoporosis_treatment()
    render_osteoporosis_nutrition()
    render_osteoporosis_prevention()
