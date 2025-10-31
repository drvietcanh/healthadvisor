"""
Joint Exercises Tab Component
Hiển thị bài tập cho các khớp
"""

import streamlit as st
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

try:
    from diseases.bone_joint.joint_exercises import (
        KNEE_EXERCISES,
        HIP_EXERCISES,
        HAND_EXERCISES,
        SHOULDER_EXERCISES,
        SPINE_EXERCISES,
        EXERCISE_PRINCIPLES
    )
except ImportError:
    st.error("Không thể tải module bài tập. Vui lòng kiểm tra lại.")
    st.stop()


def render_joint_exercises_tab():
    """Tab Bài tập cho khớp"""
    st.header("🏃 Bài Tập Cho Khớp & Cột Sống")
    
    # Nguyên tắc chung
    with st.expander("📋 Nguyên tắc chung", expanded=True):
        if EXERCISE_PRINCIPLES:
            principles = EXERCISE_PRINCIPLES
            
            if "general" in principles:
                st.markdown("### Nguyên tắc:")
                for principle in principles["general"]:
                    st.markdown(f"- {principle}")
            
            if "when_to_stop" in principles:
                st.error("**⚠️ Dừng tập ngay nếu:**")
                for warning in principles["when_to_stop"]:
                    st.markdown(f"- {warning}")
            
            if "frequency" in principles:
                freq = principles["frequency"]
                st.markdown("### Tần suất:")
                for key, value in freq.items():
                    st.markdown(f"- **{key}:** {value}")
    
    # Chọn khớp
    joint_option = st.radio(
        "Chọn khớp cần tập:",
        ["Gối", "Háng", "Cổ tay & Ngón tay", "Vai", "Cột sống"],
        horizontal=True
    )
    
    st.divider()
    
    # Bài tập cho Gối
    if joint_option == "Gối":
        if KNEE_EXERCISES:
            exercises = KNEE_EXERCISES
            
            col1, col2 = st.columns(2)
            
            with col1:
                if "stretching" in exercises:
                    st.markdown("### Kéo giãn:")
                    stretch = exercises["stretching"]
                    if "exercises" in stretch:
                        for ex in stretch["exercises"]:
                            if isinstance(ex, dict):
                                st.markdown(f"**{ex.get('name', '')}**")
                                st.caption(f"Tư thế: {ex.get('position', '')}")
                                st.markdown(f"Cách làm: {ex.get('movement', '')}")
                                st.markdown(f"Số lần: {ex.get('reps', '')}")
                                st.divider()
                
                if "strengthening" in exercises:
                    st.markdown("### Tăng cường cơ:")
                    strength = exercises["strengthening"]
                    if "exercises" in strength:
                        for ex in strength["exercises"]:
                            if isinstance(ex, dict):
                                st.markdown(f"**{ex.get('name', '')}**")
                                st.caption(f"Tư thế: {ex.get('position', '')}")
                                st.markdown(f"Cách làm: {ex.get('movement', '')}")
                                st.markdown(f"Số lần: {ex.get('reps', '')}")
                                st.info(f"💡 {ex.get('benefit', '')}")
                                st.divider()
            
            with col2:
                if "low_impact_cardio" in exercises:
                    st.markdown("### Vận động tim mạch:")
                    cardio = exercises["low_impact_cardio"]
                    if "exercises" in cardio:
                        for ex in cardio["exercises"]:
                            if isinstance(ex, dict):
                                st.markdown(f"**{ex.get('name', '')}**")
                                st.markdown(f"Cách tập: {ex.get('how', '')}")
                                st.markdown(f"Thời gian: {ex.get('duration', '')}")
                                if ex.get('benefit'):
                                    st.success(f"✅ {ex['benefit']}")
                                st.divider()
                
                if "avoid" in exercises:
                    st.error("**❌ TRÁNH:**")
                    for item in exercises["avoid"]:
                        st.markdown(f"- {item}")
    
    # Bài tập cho Háng
    elif joint_option == "Háng":
        if HIP_EXERCISES:
            exercises = HIP_EXERCISES
            
            col1, col2 = st.columns(2)
            
            with col1:
                if "stretching" in exercises:
                    st.markdown("### Kéo giãn:")
                    for ex in exercises["stretching"]:
                        if isinstance(ex, dict):
                            st.markdown(f"**{ex.get('name', '')}**")
                            st.caption(f"Tư thế: {ex.get('position', '')}")
                            st.markdown(f"Cách làm: {ex.get('movement', '')}")
                            st.markdown(f"Số lần: {ex.get('reps', '')}")
                            st.divider()
            
            with col2:
                if "strengthening" in exercises:
                    st.markdown("### Tăng cường cơ:")
                    for ex in exercises["strengthening"]:
                        if isinstance(ex, dict):
                            st.markdown(f"**{ex.get('name', '')}**")
                            st.caption(f"Tư thế: {ex.get('position', '')}")
                            st.markdown(f"Cách làm: {ex.get('movement', '')}")
                            st.markdown(f"Số lần: {ex.get('reps', '')}")
                            if ex.get('benefit'):
                                st.info(f"💡 {ex['benefit']}")
                            st.divider()
    
    # Bài tập cho Cổ tay & Ngón tay
    elif joint_option == "Cổ tay & Ngón tay":
        if HAND_EXERCISES:
            exercises = HAND_EXERCISES
            if "exercises" in exercises:
                for ex in exercises["exercises"]:
                    if isinstance(ex, dict):
                        st.markdown(f"**{ex.get('name', '')}**")
                        st.markdown(f"Cách làm: {ex.get('movement', '')}")
                        if ex.get('equipment'):
                            st.caption(f"Dụng cụ: {ex['equipment']}")
                        st.markdown(f"Số lần: {ex.get('reps', '')}")
                        if ex.get('duration'):
                            st.markdown(f"Thời gian: {ex['duration']}")
                        if ex.get('benefit'):
                            st.info(f"💡 {ex['benefit']}")
                        st.divider()
    
    # Bài tập cho Vai
    elif joint_option == "Vai":
        if SHOULDER_EXERCISES:
            exercises = SHOULDER_EXERCISES
            if "exercises" in exercises:
                for ex in exercises["exercises"]:
                    if isinstance(ex, dict):
                        st.markdown(f"**{ex.get('name', '')}**")
                        if ex.get('position'):
                            st.caption(f"Tư thế: {ex['position']}")
                        st.markdown(f"Cách làm: {ex.get('movement', '')}")
                        st.markdown(f"Số lần: {ex.get('reps', '')}")
                        st.divider()
    
    # Bài tập cho Cột sống
    elif joint_option == "Cột sống":
        if SPINE_EXERCISES:
            exercises = SPINE_EXERCISES
            
            if "low_back" in exercises:
                st.markdown("### Đau thắt lưng:")
                low_back = exercises["low_back"]
                if "exercises" in low_back:
                    col1, col2 = st.columns(2)
                    for i, ex in enumerate(low_back["exercises"]):
                        col = col1 if i % 2 == 0 else col2
                        with col:
                            if isinstance(ex, dict):
                                st.markdown(f"**{ex.get('name', '')}**")
                                st.caption(f"Tư thế: {ex.get('position', '')}")
                                st.markdown(f"Cách làm: {ex.get('movement', '')}")
                                st.markdown(f"Số lần: {ex.get('reps', '')}")
                                st.info(f"💡 {ex.get('benefit', '')}")
                                st.divider()
            
            if "posture" in exercises:
                posture = exercises["posture"]
                st.markdown("### Giữ tư thế đúng:")
                if "tips" in posture:
                    for tip in posture["tips"]:
                        st.markdown(f"- {tip}")
            
            if "core_strengthening" in exercises:
                st.markdown("### Tăng cường cơ bụng, lưng:")
                core = exercises["core_strengthening"]
                if "exercises" in core:
                    for ex in core["exercises"]:
                        if isinstance(ex, dict):
                            st.markdown(f"**{ex.get('name', '')}**")
                            st.caption(f"Tư thế: {ex.get('position', '')}")
                            st.markdown(f"Cách làm: {ex.get('movement', '')}")
                            st.markdown(f"Số lần: {ex.get('reps', '')}")
                            st.info(f"💡 {ex.get('benefit', '')}")
                            st.markdown(f"Tần suất: {core.get('frequency', '')}")
                            st.divider()

