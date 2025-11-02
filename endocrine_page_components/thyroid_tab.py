"""Thyroid Tab Component"""

import streamlit as st
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

from diseases.endocrine.thyroid import THYROID_INFO, HYPOTHYROIDISM, HYPERTHYROIDISM, GOITER_INFO

def render_thyroid_tab():
    """Render tab Bệnh Tuyến Giáp - Tổng quan"""
    st.header("🦋 Bệnh Tuyến Giáp (Thyroid Disease)")
    
    with st.expander("📖 Bệnh tuyến giáp là gì?", expanded=True):
        if THYROID_INFO:
            st.markdown(THYROID_INFO.get("simple_explanation", ""))
            if THYROID_INFO.get("why_important"):
                st.warning(THYROID_INFO["why_important"])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔽 Suy Giáp (Hypothyroidism)")
        st.info("Tuyến giáp tiết hormone QUÁ ÍT")
        if HYPOTHYROIDISM and "symptoms" in HYPOTHYROIDISM:
            st.markdown("**Triệu chứng:**")
            for s in HYPOTHYROIDISM["symptoms"]["common"][:5]:
                st.markdown(f"- {s}")
        if HYPOTHYROIDISM and "treatment" in HYPOTHYROIDISM:
            st.markdown("**Điều trị:**")
            st.caption("Levothyroxine (uống suốt đời)")
    
    with col2:
        st.markdown("### 🔼 Cường Giáp (Hyperthyroidism)")
        st.info("Tuyến giáp tiết hormone QUÁ NHIỀU")
        if HYPERTHYROIDISM and "symptoms" in HYPERTHYROIDISM:
            st.markdown("**Triệu chứng:**")
            for s in HYPERTHYROIDISM["symptoms"]["common"][:5]:
                st.markdown(f"- {s}")
        if HYPERTHYROIDISM and "treatment" in HYPERTHYROIDISM:
            st.markdown("**Điều trị:**")
            st.caption("Thuốc kháng giáp, Iodine phóng xạ")
    
    st.divider()
    
    with st.expander("🔍 Chi tiết Suy Giáp"):
        if HYPOTHYROIDISM:
            if "symptoms" in HYPOTHYROIDISM:
                st.markdown(f"### {HYPOTHYROIDISM['symptoms']['title']}")
                for s in HYPOTHYROIDISM["symptoms"]["common"]:
                    st.markdown(f"- {s}")
            if "treatment" in HYPOTHYROIDISM:
                st.divider()
                st.markdown(f"### {HYPOTHYROIDISM['treatment']['title']}")
                if "levothyroxine" in HYPOTHYROIDISM["treatment"]:
                    lev = HYPOTHYROIDISM["treatment"]["levothyroxine"]
                    st.markdown(f"**{lev['title']}**")
                    st.caption(lev["description"])
                    st.markdown("**Cách uống:**")
                    for tip in lev.get("how_to_take", []):
                        st.markdown(f"- {tip}")
                    if lev.get("warning"):
                        st.warning(lev["warning"])
    
    with st.expander("🔍 Chi tiết Cường Giáp"):
        if HYPERTHYROIDISM:
            if "symptoms" in HYPERTHYROIDISM:
                st.markdown(f"### {HYPERTHYROIDISM['symptoms']['title']}")
                for s in HYPERTHYROIDISM["symptoms"]["common"]:
                    st.markdown(f"- {s}")
            if "treatment" in HYPERTHYROIDISM:
                st.divider()
                st.markdown(f"### {HYPERTHYROIDISM['treatment']['title']}")
                if "antithyroid" in HYPERTHYROIDISM["treatment"]:
                    st.markdown(f"**{HYPERTHYROIDISM['treatment']['antithyroid']['title']}**")
                    for item in HYPERTHYROIDISM["treatment"]["antithyroid"].get("examples", []):
                        st.markdown(f"- {item}")
    
    with st.expander("🔍 Bướu Cổ"):
        if GOITER_INFO:
            st.markdown(f"**{GOITER_INFO['simple_explanation']}**")
            st.markdown("**Nguyên nhân:**")
            for cause in GOITER_INFO["causes"]:
                st.markdown(f"- {cause}")

