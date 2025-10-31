"""
Paracetamol Calculator
Tính liều paracetamol đúng theo cân nặng (kg)
An toàn cho trẻ em và người lớn
"""

import streamlit as st


def calculate_paracetamol_dose(weight_kg: float, age_years: int = None) -> dict:
    """
    Tính liều paracetamol theo cân nặng
    
    Args:
        weight_kg: Cân nặng (kg)
        age_years: Tuổi (năm) - optional, để kiểm tra an toàn
    
    Returns:
        dict: {
            "dose_mg": liều tính bằng mg,
            "syrup_ml": liều siro (nếu dùng siro 160mg/5ml),
            "tablet_formulations": dict với số viên theo từng hàm lượng,
            "max_daily_mg": liều tối đa trong 24h,
            "frequency": khoảng cách giữa các lần (giờ),
            "safety_note": lưu ý an toàn
        }
    """
    if weight_kg <= 0:
        return None
    
    # Liều paracetamol: 10-15mg/kg/lần cho trẻ em
    # Liều người lớn: 500-1000mg/lần (tối đa 4000mg/ngày)
    
    # Trẻ em (< 12 tuổi hoặc < 40kg)
    if age_years and age_years < 12 or weight_kg < 40:
        dose_per_kg = 15  # mg/kg - liều an toàn cho trẻ
        dose_mg = round(weight_kg * dose_per_kg)
        
        # Không quá 1000mg/lần cho trẻ
        dose_mg = min(dose_mg, 1000)
        
        # Liều tối đa ngày: 60mg/kg (không quá 4000mg)
        max_daily_mg = min(int(weight_kg * 60), 4000)
        frequency_hours = 4  # Cách 4-6 giờ
        safety_note = "Trẻ em: Cách 4-6 giờ/lần, tối đa 4 lần/ngày"
    else:
        # Người lớn (≥ 12 tuổi hoặc ≥ 40kg)
        if weight_kg < 50:
            dose_mg = 500
        elif weight_kg < 70:
            dose_mg = 650
        else:
            dose_mg = 1000
        
        max_daily_mg = 4000  # Tối đa 4000mg/ngày cho người lớn
        frequency_hours = 6  # Cách 6-8 giờ
        safety_note = "Người lớn: Cách 6-8 giờ/lần, tối đa 4 lần/ngày"
    
    # Tính siro (160mg/5ml) - thường cho trẻ em
    syrup_ml = None
    if weight_kg < 40:
        syrup_ml = round((dose_mg / 160) * 5, 1)
    
    # Tính số viên theo các hàm lượng phổ biến
    # Các hàm lượng: 250mg, 500mg, 650mg
    tablet_formulations = {}
    
    # Viên 250mg (thường cho trẻ lớn/thanh thiếu niên)
    tablets_250 = dose_mg / 250
    if tablets_250 == int(tablets_250):
        tablet_formulations["250mg"] = int(tablets_250)
    elif tablets_250 < 1:
        tablet_formulations["250mg"] = "1 viên (≈250mg, hơi thiếu)"
    else:
        tablet_formulations["250mg"] = f"{int(tablets_250)}+ viên (không khuyến nghị - dùng loại khác)"
    
    # Viên 500mg (phổ biến nhất)
    tablets_500 = dose_mg / 500
    if tablets_500 == int(tablets_500):
        tablet_formulations["500mg"] = int(tablets_500)
    elif tablets_500 < 1:
        tablet_formulations["500mg"] = "1 viên (≈500mg)"
    else:
        # Làm tròn lên/xuống gần nhất
        if tablets_500 <= 1.5:
            tablet_formulations["500mg"] = "1 viên (≈500mg, hơi thiếu)"
        else:
            tablet_formulations["500mg"] = int(round(tablets_500))
    
    # Viên 650mg (Efferalgan)
    tablets_650 = dose_mg / 650
    if tablets_650 == int(tablets_650):
        tablet_formulations["650mg"] = int(tablets_650)
    elif tablets_650 < 1:
        tablet_formulations["650mg"] = "1 viên (≈650mg, hơi dư)"
    else:
        if tablets_650 <= 1.3:
            tablet_formulations["650mg"] = "1 viên (≈650mg)"
        else:
            tablet_formulations["650mg"] = f"{int(round(tablets_650))} viên (≈{int(round(tablets_650)) * 650}mg)"
    
    # Viên 1000mg (người lớn)
    if dose_mg >= 1000:
        tablets_1000 = dose_mg / 1000
        if tablets_1000 == int(tablets_1000):
            tablet_formulations["1000mg"] = int(tablets_1000)
        else:
            tablet_formulations["1000mg"] = int(round(tablets_1000))
    
    return {
        "dose_mg": dose_mg,
        "syrup_ml": syrup_ml,
        "tablet_formulations": tablet_formulations,
        "max_daily_mg": max_daily_mg,
        "frequency_hours": frequency_hours,
        "safety_note": safety_note,
        "is_child": weight_kg < 40 or (age_years and age_years < 12)
    }


def render_paracetamol_calculator():
    """Hiển thị máy tính paracetamol"""
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


def get_paracetamol_guidelines() -> str:
    """Trả về hướng dẫn sử dụng paracetamol"""
    return """
## 📚 Hướng dẫn sử dụng Paracetamol đúng cách

### ✅ Khi nào dùng Paracetamol?

Paracetamol dùng để:
- 🔥 **Hạ sốt:** Khi nhiệt độ > 38.5°C (đo ở nách) hoặc khi sốt gây khó chịu
- 😣 **Giảm đau:** Đau đầu, đau răng, đau cơ, đau nhức sau tiêm vaccine

### ❌ Khi nào KHÔNG dùng?

- ⛔ **Suy gan, viêm gan** (tuyệt đối tránh!)
- ⛔ **Đã uống rượu bia trong 8-12 giờ** → TUYỆT ĐỐI TRÁNH!
- ⛔ Đã uống quá 4000mg trong 24h
- ⛔ Đang uống thuốc khác có chứa paracetamol (tránh quá liều)
- ⛔ Dị ứng với paracetamol

### 🚫 CẢNH BÁO ĐỎ - Paracetamol + Rượu Bia:

**NGUY HIỂM CHẾT NGƯỜI!**

- 🍺 **Rượu bia làm gan không thể chuyển hóa paracetamol an toàn**
- 💀 **→ Tích tụ độc tố → Suy gan cấp tính → Tử vong trong 48-72 giờ**
- ⏰ **Quy tắc vàng:** Sau khi uống rượu bia, đợi **ít nhất 8-12 giờ** mới dùng paracetamol
- 🔥 **Đau đầu do say rượu?** → Uống nhiều nước, nghỉ ngơi, KHÔNG dùng paracetamol!

### 💡 Mẹo an toàn:

1. **Kiểm tra thành phần:** Nhiều thuốc cảm cúm có chứa paracetamol
   - Panadol = Paracetamol
   - Efferalgan = Paracetamol 650mg
   - Tiffy, Decolgen = Có paracetamol + các chất khác
   - → Đọc kỹ nhãn, tránh uống cùng lúc!

2. **Cách đo siro cho trẻ:**
   - ✅ Dùng ống tiêm định lượng (có sẵn trong hộp)
   - ✅ Đo đúng ml, không dùng thìa ăn cơm
   - ✅ Trẻ không chịu uống? Pha loãng với chút nước

3. **Dấu hiệu quá liều (gọi 115 ngay!):**
   - Nôn mửa
   - Đau bụng vùng gan (bên phải)
   - Vàng da, vàng mắt
   - Buồn ngủ bất thường

4. **Nếu sốt không hạ sau 2-3 ngày:**
   - → Đi khám bác sĩ (có thể là viêm nhiễm cần kháng sinh)
   - → Không tự ý tăng liều paracetamol

### 📊 Liều chuẩn theo cân nặng:

- **Trẻ em:** 10-15mg/kg/lần, cách 4-6 giờ
- **Người lớn:** 500-1000mg/lần, cách 6-8 giờ
- **Tối đa:** 60mg/kg/ngày (trẻ) hoặc 4000mg/ngày (người lớn)
"""

