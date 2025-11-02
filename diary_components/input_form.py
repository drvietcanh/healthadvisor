"""
Input Form - Form nhập dữ liệu sức khỏe
"""
import streamlit as st
from datetime import datetime
import pandas as pd
from core.utils import classify_blood_pressure


def render_input_form():
    """Hiển thị form nhập liệu đầy đủ và xử lý submit"""
    
    st.subheader("➕ Bước 2: Thêm dữ liệu mới")
    
    with st.form("add_health_data", clear_on_submit=True):
        # Thời gian
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 📅 Thời gian")
            measurement_date = st.date_input("Ngày đo", value=datetime.now())
            measurement_time = st.time_input("Giờ đo", value=datetime.now().time())
        with col2:
            st.markdown("#### ⏰ Thời điểm")
            time_of_day = st.radio("Đo vào lúc:", 
                ["🌅 Sáng (đói)", "🌞 Trưa (sau ăn 2h)", "🌙 Tối (trước ngủ)", "🍽️ Sau ăn"])
        
        st.divider()
        
        # Huyết áp & Mạch
        st.markdown("#### ❤️ Huyết áp")
        col1, col2, col3 = st.columns(3)
        with col1:
            systolic = st.number_input("Tâm thu (mmHg)", 70, 250, 120, 1, help="Số lớn (trên)")
        with col2:
            diastolic = st.number_input("Tâm trương (mmHg)", 40, 150, 80, 1, help="Số nhỏ (dưới)")
        with col3:
            pulse = st.number_input("Mạch (nhịp/phút)", 40, 200, 75, 1)
        
        # Đánh giá huyết áp
        if systolic and diastolic:
            bp_category = classify_blood_pressure(systolic, diastolic)
            if "Bình thường" in bp_category:
                st.success(f"✅ {bp_category}")
            elif "Cao" in bp_category or "Nguy hiểm" in bp_category:
                st.error(f"⚠️ {bp_category}")
            else:
                st.warning(f"⚠️ {bp_category}")
        
        if pulse:
            if pulse < 60:
                st.warning(f"⚠️ Mạch chậm ({pulse} < 60)")
            elif pulse > 100:
                st.warning(f"⚠️ Mạch nhanh ({pulse} > 100)")
            else:
                st.success(f"✅ Mạch bình thường (60-100)")
        
        st.divider()
        
        # Đường huyết
        st.markdown("#### 🩸 Đường huyết")
        col1, col2, col3 = st.columns(3)
        with col1:
            glucose_unit = st.radio("Đơn vị:", ["mmol/L", "mg/dL"], horizontal=True)
        with col2:
            if glucose_unit == "mmol/L":
                glucose_mmol = st.number_input("Đường huyết (mmol/L)", 2.0, 30.0, 5.5, 0.1)
                glucose_mgdl = round(glucose_mmol * 18)
            else:
                glucose_mgdl = st.number_input("Đường huyết (mg/dL)", 36, 540, 100, 1)
                glucose_mmol = round(glucose_mgdl / 18, 1)
        with col3:
            st.info(f"📊 **Quy đổi:**\n\n{glucose_mmol} mmol/L\n\n= {glucose_mgdl} mg/dL")
        
        st.divider()
        
        # Cân nặng & Vòng eo
        st.markdown("#### ⚖️ Cân nặng & Đo lường cơ thể (tùy chọn)")
        col1, col2, col3 = st.columns(3)
        with col1:
            weight = st.number_input("Cân nặng (kg)", 30.0, 200.0, value=None, step=0.1)
        with col2:
            waist = st.number_input("Vòng eo (cm)", 50.0, 200.0, value=None, step=0.1, help="Đo ngang rốn")
        with col3:
            if weight and waist:
                st.caption("💡 Giúp theo dõi giảm cân & béo phì")
            else:
                st.caption("")
        
        st.divider()
        
        # Calories (cho quản lý cân nặng)
        st.markdown("#### 🍽️ Calories (tùy chọn - để quản lý cân nặng)")
        col1, col2, col3 = st.columns(3)
        with col1:
            calories_in = st.number_input("Calories ăn vào", 0, 5000, value=None, step=50, help="Tổng calories ăn trong ngày")
        with col2:
            calories_out = st.number_input("Calories đốt cháy", 0, 3000, value=None, step=50, help="Từ vận động, tập luyện")
        with col3:
            if calories_in and calories_out:
                balance = calories_in - calories_out
                if balance > 0:
                    st.warning(f"⚠️ Thừa: +{balance} cal")
                elif balance < 0:
                    st.success(f"✅ Thiếu hụt: {balance} cal\n\n(Giảm cân)")
                else:
                    st.info(f"⚖️ Cân bằng: 0 cal")
        
        st.divider()
        
        # Xét nghiệm
        st.markdown("#### 🧪 Xét nghiệm (Tùy chọn)")
        st.info("💡 Chỉ nhập khi có kết quả xét nghiệm. Để trống nếu không có!")
        
        # HbA1c
        with st.expander("🩸 HbA1c (Đường huyết trung bình 3 tháng)"):
            col1, col2 = st.columns(2)
            with col1:
                hba1c = st.number_input("HbA1c (%)", 4.0, 15.0, value=None, step=0.1)
            with col2:
                if hba1c:
                    if hba1c < 5.7:
                        st.success("✅ Bình thường (< 5.7%)")
                    elif hba1c < 6.5:
                        st.warning("⚠️ Tiền tiểu đường")
                    else:
                        st.error("❌ Tiểu đường (≥ 6.5%)")
                else:
                    st.caption("📊 BT: <5.7% | Tiền TĐ: 5.7-6.4% | TĐ: ≥6.5%")
        
        # Mỡ máu
        with st.expander("💊 Mỡ máu (Lipid panel)"):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 400, value=None, step=1)
            with col2:
                ldl = st.number_input("LDL - Xấu (mg/dL)", 50, 300, value=None, step=1)
            with col3:
                hdl = st.number_input("HDL - Tốt (mg/dL)", 20, 100, value=None, step=1)
            with col4:
                triglyceride = st.number_input("Triglyceride (mg/dL)", 50, 500, value=None, step=1)
            
            # Đánh giá
            if cholesterol or ldl or hdl or triglyceride:
                st.markdown("**📊 Đánh giá:**")
                c1, c2, c3, c4 = st.columns(4)
                with c1:
                    if cholesterol:
                        st.success("✅ TC: Tốt") if cholesterol < 200 else st.warning("⚠️ TC: Cao")
                with c2:
                    if ldl:
                        st.success("✅ LDL: Tốt") if ldl < 100 else st.warning("⚠️ LDL: Cao")
                with c3:
                    if hdl:
                        st.success("✅ HDL: Tốt") if hdl >= 60 else st.info("ℹ️ HDL: TB")
                with c4:
                    if triglyceride:
                        st.success("✅ TG: BT") if triglyceride < 150 else st.warning("⚠️ TG: Cao")
        
        # Acid Uric & Thận
        with st.expander("🔬 Acid Uric & Chức năng thận"):
            col1, col2, col3 = st.columns(3)
            with col1:
                uric_acid = st.number_input("Acid Uric (mg/dL)", 2.0, 15.0, value=None, step=0.1)
                if uric_acid:
                    st.success("✅ BT (≤7.0)") if uric_acid <= 7.0 else st.error("❌ Cao - Nguy cơ gút!")
            with col2:
                creatinine = st.number_input("Creatinine (mg/dL)", 0.5, 10.0, value=None, step=0.1)
                if creatinine:
                    st.success("✅ BT") if creatinine <= 1.2 else st.warning("⚠️ Cao - Kiểm tra thận!")
            with col3:
                egfr = st.number_input("eGFR (mL/min)", 5, 150, value=None, step=1)
                if egfr:
                    if egfr >= 90:
                        st.success("✅ BT (≥90)")
                    elif egfr >= 60:
                        st.info("ℹ️ Giảm nhẹ")
                    else:
                        st.warning("⚠️ Giảm")
        
        st.divider()
        
        # Ghi chú
        st.markdown("#### 📝 Ghi chú (tùy chọn)")
        notes = st.text_area("Ghi chú", 
            placeholder="Ví dụ: Đau đầu nhẹ, uống thuốc lúc 7h sáng...",
            label_visibility="collapsed")
        
        # Nút submit
        submitted = st.form_submit_button("💾 LƯU VÀO NHẬT KÝ", use_container_width=True, type="primary")
        
        if submitted:
            timestamp = datetime.combine(measurement_date, measurement_time)
            new_row = {
                'Ngày giờ': timestamp.strftime("%d/%m/%Y %H:%M"),
                'Thời điểm': time_of_day,
                'Huyết áp tâm thu': systolic,
                'Huyết áp tâm trương': diastolic,
                'Mạch (nhịp/phút)': pulse,
                'Đường huyết (mmol/L)': glucose_mmol,
                'Đường huyết (mg/dL)': glucose_mgdl,
                'HbA1c (%)': hba1c,
                'Cholesterol toàn phần (mg/dL)': cholesterol,
                'LDL (mg/dL)': ldl,
                'HDL (mg/dL)': hdl,
                'Triglyceride (mg/dL)': triglyceride,
                'Acid Uric (mg/dL)': uric_acid,
                'Creatinine (mg/dL)': creatinine,
                'eGFR (mL/min)': egfr,
                'Cân nặng (kg)': weight,
                'Vòng eo (cm)': waist,
                'Calories ăn vào': calories_in,
                'Calories đốt cháy': calories_out,
                'Ghi chú': notes
            }
            
            st.session_state.health_data = pd.concat([
                st.session_state.health_data,
                pd.DataFrame([new_row])
            ], ignore_index=True)
            
            st.session_state.health_data = st.session_state.health_data.sort_values(
                'Ngày giờ', ascending=False
            ).reset_index(drop=True)
            
            st.success("✅ **Đã lưu thành công!** Kéo xuống xem dữ liệu và biểu đồ bên dưới.")
            st.balloons()
            
            return True
    
    return False

