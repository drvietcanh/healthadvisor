"""
Paracetamol Render Display
Hiển thị máy tính paracetamol với UI
"""

import streamlit as st


def render_paracetamol_calculator():
    """Hiển thị máy tính paracetamol"""
    from .calculator_logic import calculate_paracetamol_dose
    
    st.subheader("💊 Máy tính liều Paracetamol")
    
    st.info("""
    **📌 Paracetamol là gì?**
    
    Paracetamol (còn gọi là Acetaminophen) là thuốc hạ sốt, giảm đau an toàn nhất.
    - ✅ Dùng được cho trẻ em, phụ nữ có thai
    - ✅ Không gây viêm dạ dày (khác với Aspirin, Ibuprofen)
    - ⚠️ Nhưng QUÁ LIỀU sẽ GÂY ĐỘC GAN - rất nguy hiểm!
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        weight_kg = st.number_input(
            "⚖️ Cân nặng (kg)",
            min_value=5.0,
            max_value=150.0,
            value=50.0,
            step=0.5,
            help="Nhập cân nặng chính xác"
        )
    
    with col2:
        age_years = st.number_input(
            "🎂 Tuổi (năm) - tùy chọn",
            min_value=0,
            max_value=120,
            value=None,
            step=1,
            help="Nhập tuổi để tính chính xác hơn (tùy chọn)"
        )
    
    # Tính toán
    if st.button("🧮 Tính liều", type="primary", use_container_width=True):
        if weight_kg <= 0:
            st.error("⚠️ Vui lòng nhập cân nặng hợp lệ!")
            return
        
        result = calculate_paracetamol_dose(weight_kg, age_years)
        
        if not result:
            st.error("❌ Không thể tính toán. Vui lòng kiểm tra lại!")
            return
        
        # Hiển thị kết quả
        st.success("✅ **Kết quả tính toán:**")
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.metric("💊 Liều mỗi lần", f"{result['dose_mg']} mg")
            st.metric("⏰ Cách nhau", f"{result['frequency_hours']} giờ")
        
        with col_b:
            st.metric("📊 Tối đa/ngày", f"{result['max_daily_mg']} mg")
            st.metric("🔄 Số lần/ngày", f"Tối đa {result['max_daily_mg'] // result['dose_mg']} lần")
        
        st.divider()
        
        # Cách dùng cụ thể
        st.markdown("### 📋 Cách dùng cụ thể theo từng loại:")
        
        # Siro cho trẻ em
        if result['is_child'] and result['syrup_ml']:
            st.markdown(f"""
            **🍼 Siro Paracetamol (160mg/5ml) - Dành cho trẻ nhỏ:**
            - Mỗi lần: **{result['syrup_ml']} ml** (≈ {result['dose_mg']}mg)
            - Cách {result['frequency_hours']}-6 giờ/lần
            - 💡 Dùng ống tiêm định lượng (có sẵn trong hộp) hoặc thìa đo đúng ml
            - ⚠️ Không dùng thìa ăn cơm (sai liều!)
            """)
        
        # Hiển thị các loại viên
        st.markdown("**💊 Viên Paracetamol (người lớn & trẻ lớn):**")
        
        formulations = result['tablet_formulations']
        
        # Viên 250mg
        if "250mg" in formulations:
            count = formulations["250mg"]
            if isinstance(count, int):
                st.markdown(f"""
                - **Viên 250mg:** {count} viên = {count * 250}mg
                  - VD: Panadol 250mg, Paracetamol 250mg (generic)
                """)
            else:
                st.markdown(f"""
                - **Viên 250mg:** {count}
                """)
        
        # Viên 500mg (phổ biến nhất)
        if "500mg" in formulations:
            count = formulations["500mg"]
            if isinstance(count, int):
                st.markdown(f"""
                - **Viên 500mg:** ✅ {count} viên = {count * 500}mg (KHUYẾN NGHỊ)
                  - VD: Panadol 500mg, Paracetamol 500mg (generic), Hapacol 500mg
                """)
            else:
                st.markdown(f"""
                - **Viên 500mg:** {count}
                """)
        
        # Viên 650mg
        if "650mg" in formulations:
            count = formulations["650mg"]
            if isinstance(count, int):
                total_mg = count * 650
                st.markdown(f"""
                - **Viên 650mg (Efferalgan):** {count} viên = {total_mg}mg
                  - 💡 Efferalgan tan trong miệng, dễ uống
                """)
            else:
                st.markdown(f"""
                - **Viên 650mg:** {count}
                """)
        
        # Viên 1000mg
        if "1000mg" in formulations:
            count = formulations["1000mg"]
            if isinstance(count, int):
                st.markdown(f"""
                - **Viên 1000mg:** {count} viên = {count * 1000}mg
                  - VD: Panadol Extra, Paracetamol 1000mg (người lớn nặng cân)
                """)
        
        st.divider()
        
        # Tóm tắt
        st.markdown("### 📊 Tóm tắt:")
        st.markdown(f"""
        ⏰ **Cách nhau:** {result['frequency_hours']}-8 giờ/lần
        📅 **Tối đa:** {result['max_daily_mg']}mg trong 24 giờ
        """)
        
        # Cảnh báo an toàn
        st.error(f"""
        ⚠️ **CẢNH BÁO ĐỎ - TỐI QUAN TRỌNG:**
        
        **🚫 TUYỆT ĐỐI KHÔNG uống Paracetamol sau khi uống rượu bia!**
        
        - 🍺 **Rượu bia + Paracetamol = SUY GAN CẤP TÍNH, CÓ THỂ TỬ VONG!**
        - ⏰ Cách ít nhất **8-12 giờ** sau khi uống rượu bia mới được dùng paracetamol
        - 🔥 Đau đầu do say rượu? → Uống nhiều nước, nghỉ ngơi, KHÔNG uống paracetamol!
        - 💀 **Đây là nguyên nhân hàng đầu gây suy gan do thuốc tại VN!**
        
        **📋 Các lưu ý khác:**
        1. **{result['safety_note']}**
        2. **Không quá {result['max_daily_mg']} mg trong 24 giờ**
        3. **Không tự ý tăng liều** - Quá liều gây suy gan!
        4. Nếu sốt không giảm sau 2-3 ngày → **Đi khám bác sĩ**
        5. Trẻ em < 3 tháng tuổi → **Hỏi bác sĩ trước khi dùng**
        6. **Đã uống rượu?** → Đợi ít nhất 8-12 giờ, uống nhiều nước, nghỉ ngơi
        """)
        
        # Bảng tóm tắt
        st.markdown("### 📊 Tóm tắt liều dùng:")
        
        if result['is_child']:
            tips = [
                f"🎯 **Liều mỗi lần:** {result['dose_mg']}mg ({result['syrup_ml']}ml siro nếu dùng)",
                f"⏰ **Cách nhau:** {result['frequency_hours']}-6 giờ",
                f"📅 **Tối đa/ngày:** {result['max_daily_mg']}mg (≈ {result['max_daily_mg'] // result['dose_mg']} lần)",
                "✅ **An toàn:** Không uống quá 4 lần/ngày",
                "⚠️ **Tránh:** Không dùng cùng lúc với thuốc khác có paracetamol"
            ]
        else:
            tips = [
                f"🎯 **Liều mỗi lần:** {result['dose_mg']}mg",
                f"⏰ **Cách nhau:** {result['frequency_hours']}-8 giờ",
                f"📅 **Tối đa/ngày:** {result['max_daily_mg']}mg (4 lần × 1000mg)",
                "✅ **An toàn:** Cách 6-8 giờ/lần, không quá 4 lần/ngày",
                "⚠️ **Tránh:** Không dùng quá 4000mg/ngày, không uống rượu khi dùng"
            ]
        
        for tip in tips:
            st.markdown(f"- {tip}")

