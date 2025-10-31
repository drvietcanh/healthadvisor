"""
Tab 3: Rối Loạn Lipid Máu
Hiển thị thông tin về rối loạn lipid máu (cholesterol & triglyceride)
"""

import streamlit as st
from diseases.metabolic import dyslipidemia

def render_dyslipidemia_tab():
    """Render tab Rối Loạn Lipid Máu"""
    st.header("🧈 Rối Loạn Lipid Máu (Cholesterol & Triglyceride)")
    
    # Giới thiệu
    with st.expander("📖 Rối loạn lipid máu là gì?", expanded=True):
        st.markdown(dyslipidemia.DYSLIPIDEMIA_INFO["what_is_it"])
        st.warning(dyslipidemia.DYSLIPIDEMIA_INFO["why_dangerous"])
        
        st.subheader("🔬 Các chỉ số Lipid:")
        for lipid_key, lipid_info in dyslipidemia.DYSLIPIDEMIA_INFO["lipid_types"].items():
            with st.container():
                st.markdown(f"**{lipid_info['name']}** ({lipid_info['abbreviation']})")
                st.caption(lipid_info["simple_explanation"])
                st.divider()
    
    # Phân loại thực phẩm Traffic Light
    with st.expander("🚦 PHÂN LOẠI THỰC PHẨM - Dễ Hiểu, Dễ Nhớ", expanded=True):
        st.markdown("### Hệ thống màu sắc giúp bạn biết ngay thực phẩm nào an toàn!")
        
        # Đỏ - Nguy hiểm
        st.error("### 🔴 ĐỎ - NGUY HIỂM: TRÁNH HOÀN TOÀN")
        st.markdown(dyslipidemia.FOOD_SAFETY_CLASSIFICATION["red_danger"]["rule"])
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**Trans Fat:**")
            for food in dyslipidemia.FOOD_SAFETY_CLASSIFICATION["red_danger"]["foods"]["trans_fat_foods"][:3]:
                st.markdown(food)
        with col2:
            st.markdown("**Cholesterol Cực Cao:**")
            for food in dyslipidemia.FOOD_SAFETY_CLASSIFICATION["red_danger"]["foods"]["very_high_cholesterol"][:3]:
                st.markdown(food)
        with col3:
            st.markdown("**Mỡ Bão Hòa Cao:**")
            for food in dyslipidemia.FOOD_SAFETY_CLASSIFICATION["red_danger"]["foods"]["very_high_saturated_fat"][:3]:
                st.markdown(food)
        
        # Cam - Hạn chế
        st.warning("### 🟠 CAM - HẠN CHẾ: Ăn ít, < 2-3 lần/tuần")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Thịt Nhiều Mỡ:**")
            for food in dyslipidemia.FOOD_SAFETY_CLASSIFICATION["orange_limit"]["foods"]["fatty_meat"][:4]:
                st.markdown(food)
        with col2:
            st.markdown("**Thịt Chế Biến:**")
            for food in dyslipidemia.FOOD_SAFETY_CLASSIFICATION["orange_limit"]["foods"]["processed_meat"][:4]:
                st.markdown(food)
        
        # Xanh - An toàn
        st.success("### 🟢 XANH LÁ - AN TOÀN: Ăn tự do")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**Rau:**")
            for food in dyslipidemia.FOOD_SAFETY_CLASSIFICATION["green_safe"]["foods"]["vegetables"][:4]:
                st.markdown(food)
        with col2:
            st.markdown("**Trái Cây:**")
            for food in dyslipidemia.FOOD_SAFETY_CLASSIFICATION["green_safe"]["foods"]["fruits"][:4]:
                st.markdown(food)
        with col3:
            st.markdown("**Ngũ Cốc:**")
            for food in dyslipidemia.FOOD_SAFETY_CLASSIFICATION["green_safe"]["foods"]["whole_grains"][:4]:
                st.markdown(food)
        
        # Xanh đậm - Rất tốt
        st.success("### 🟩 XANH ĐẬM - RẤT TỐT: Nên ăn nhiều!")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Cá Giàu Omega-3:**")
            for food in dyslipidemia.FOOD_SAFETY_CLASSIFICATION["dark_green_excellent"]["foods"]["omega3_fish"]:
                st.markdown(food)
        with col2:
            st.markdown("**Hạt:**")
            for food in dyslipidemia.FOOD_SAFETY_CLASSIFICATION["dark_green_excellent"]["foods"]["nuts_seeds"]:
                st.markdown(food)
        
        st.info("💡 **Mẹo:** Càng XANH càng TỐT - càng ĐỎ càng NGUY HIỂM!")
    
    # Bảng tra cứu nhanh
    with st.expander("📊 BẢNG TRA CỨU NHANH - Món Phổ Biến VN"):
        category = st.selectbox(
            "Chọn loại món:",
            ["Món Sáng", "Bữa Chính", "Đồ Ăn Vặt", "Protein", "Dầu Nấu Ăn", "Đồ Uống"]
        )
        
        if category == "Món Sáng":
            data = dyslipidemia.QUICK_REFERENCE_TABLE["breakfast_foods"]
        elif category == "Bữa Chính":
            data = dyslipidemia.QUICK_REFERENCE_TABLE["lunch_dinner"]
        elif category == "Đồ Ăn Vặt":
            data = dyslipidemia.QUICK_REFERENCE_TABLE["snacks"]
        elif category == "Protein":
            data = dyslipidemia.QUICK_REFERENCE_TABLE["proteins"]
        elif category == "Dầu Nấu Ăn":
            data = dyslipidemia.QUICK_REFERENCE_TABLE["cooking_oils"]
        else:  # Đồ Uống
            data = dyslipidemia.QUICK_REFERENCE_TABLE["beverages"]
        
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.error("**🔴 ĐỎ**")
            for item in data["red"]:
                st.markdown(f"- {item}")
        with col2:
            st.warning("**🟠 CAM**")
            for item in data["orange"]:
                st.markdown(f"- {item}")
        with col3:
            st.info("**🟡 VÀNG**")
            for item in data["yellow"]:
                st.markdown(f"- {item}")
        with col4:
            st.success("**🟢 XANH**")
            for item in data["green"]:
                st.markdown(f"- {item}")
        with col5:
            st.success("**🟩 XANH ĐẬM**")
            for item in data["dark_green"]:
                st.markdown(f"- {item}")
    
    # Giải thích về các loại mỡ
    with st.expander("🧈 Các Loại Chất Béo - Tốt và Xấu"):
        st.subheader("☠️ Trans Fat - MỠ CHUYỂN HÓA (XẤU NHẤT!)")
        st.markdown(dyslipidemia.FAT_TYPES_EXPLANATION["trans_fat"]["simple"])
        st.error("**Tại sao nguy hiểm:**")
        for reason in dyslipidemia.FAT_TYPES_EXPLANATION["trans_fat"]["why_dangerous"][:3]:
            st.markdown(f"- {reason}")
        st.markdown("**Có trong:** " + ", ".join(dyslipidemia.FAT_TYPES_EXPLANATION["trans_fat"]["sources"][:5]))
        
        st.divider()
        
        st.subheader("🥩 Mỡ Bão Hòa (XẤU)")
        st.markdown(dyslipidemia.FAT_TYPES_EXPLANATION["saturated_fat"]["simple"])
        st.markdown("**Có trong:** " + ", ".join(dyslipidemia.FAT_TYPES_EXPLANATION["saturated_fat"]["sources"][:5]))
        st.warning(dyslipidemia.FAT_TYPES_EXPLANATION["saturated_fat"]["recommendation"])
        
        st.divider()
        
        st.subheader("🫒 Mỡ Không Bão Hòa Đơn (TỐT)")
        st.markdown(dyslipidemia.FAT_TYPES_EXPLANATION["monounsaturated_fat"]["simple"])
        st.success("**Lợi ích:** " + ", ".join(dyslipidemia.FAT_TYPES_EXPLANATION["monounsaturated_fat"]["why_good"][:2]))
        st.markdown("**Có trong:** " + ", ".join(dyslipidemia.FAT_TYPES_EXPLANATION["monounsaturated_fat"]["sources"]))
        
        st.divider()
        
        st.subheader("🐟 Omega-3 (RẤT TỐT!)")
        st.markdown(dyslipidemia.FAT_TYPES_EXPLANATION["polyunsaturated_fat"]["types"]["omega3"]["name"])
        st.success("**Lợi ích:** " + ", ".join(dyslipidemia.FAT_TYPES_EXPLANATION["polyunsaturated_fat"]["types"]["omega3"]["benefits"][:2]))
        st.markdown("**Có trong:** " + ", ".join(dyslipidemia.FAT_TYPES_EXPLANATION["polyunsaturated_fat"]["types"]["omega3"]["sources"]))
        st.info(dyslipidemia.FAT_TYPES_EXPLANATION["polyunsaturated_fat"]["types"]["omega3"]["recommendation"])
    
    # Thuốc điều trị
    with st.expander("💊 Thuốc Điều Trị"):
        st.subheader("💊 STATINS - Thuốc Hạ Cholesterol (Nhóm Chính)")
        st.markdown(dyslipidemia.STATINS["description"])
        st.info("**Cơ chế:** " + dyslipidemia.STATINS["how_it_works"]["simple"])
        
        st.markdown("**Hiệu quả:**")
        for effect in dyslipidemia.STATINS["how_it_works"]["effects"]:
            st.markdown(f"- {effect}")
        
        st.markdown("### Các loại Statin phổ biến tại VN:")
        for statin in dyslipidemia.STATINS["common_statins"][:3]:
            with st.container():
                st.markdown(f"**{statin['name']}**")
                st.caption(f"Nhãn VN: {', '.join(statin['vietnamese_brands'])}")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Liều", statin["dosage"])
                with col2:
                    st.metric("Hiệu quả", statin["ldl_reduction"])
                with col3:
                    st.metric("Giá", statin["cost"])
                st.caption(f"💡 {statin['note']}")
                st.divider()
        
        st.warning("**Tác dụng phụ thường gặp:**")
        for se in dyslipidemia.STATINS["side_effects"]["common"]:
            st.markdown(f"- {se}")
        
        st.success(dyslipidemia.STATINS["side_effects"]["myth_busting"])
        
        st.divider()
        
        st.subheader("💊 FIBRATES - Hạ Triglyceride")
        st.markdown(dyslipidemia.FIBRATES["description"])
        st.markdown("**Hiệu quả:**")
        for effect in dyslipidemia.FIBRATES["how_it_works"]["effects"]:
            st.markdown(f"- {effect}")
    
    # Công cụ phân loại lipid
    with st.expander("🧪 Công Cụ Phân Loại Chỉ Số Lipid"):
        st.markdown("Nhập kết quả xét nghiệm của bạn:")
        
        col1, col2 = st.columns(2)
        with col1:
            total_chol = st.number_input(
                "Cholesterol toàn phần (mmol/L)",
                min_value=2.0,
                max_value=15.0,
                value=5.0,
                step=0.1,
                help="Bình thường: < 5.2 mmol/L"
            )
            ldl = st.number_input(
                "LDL - Mỡ xấu (mmol/L)",
                min_value=1.0,
                max_value=10.0,
                value=3.0,
                step=0.1,
                help="Mục tiêu: < 2.6 mmol/L"
            )
        
        with col2:
            hdl = st.number_input(
                "HDL - Mỡ tốt (mmol/L)",
                min_value=0.5,
                max_value=3.0,
                value=1.3,
                step=0.1,
                help="Nam: > 1.0, Nữ: > 1.3 mmol/L"
            )
            tg = st.number_input(
                "Triglyceride (mmol/L)",
                min_value=0.5,
                max_value=20.0,
                value=1.5,
                step=0.1,
                help="Bình thường: < 1.7 mmol/L"
            )
        
        if st.button("Phân loại & Tư vấn", type="primary"):
            classification = dyslipidemia.classify_lipid_levels(total_chol, ldl, hdl, tg)
            
            st.subheader("📊 Kết quả phân loại:")
            
            # Total Cholesterol
            if "cholesterol" in classification:
                chol_info = classification["cholesterol"]
                label = chol_info.get("label", "")
                if "Tối ưu" in label or "Bình thường" in label:
                    st.success(f"**Cholesterol toàn phần:** {total_chol} mmol/L - {label} {chol_info.get('icon', '')}")
                elif "Cao" in label or "Rất cao" in label or "Nguy hiểm" in label:
                    st.error(f"**Cholesterol toàn phần:** {total_chol} mmol/L - {label} {chol_info.get('icon', '')}")
                else:
                    st.warning(f"**Cholesterol toàn phần:** {total_chol} mmol/L - {label} {chol_info.get('icon', '')}")
            
            # LDL
            if "ldl" in classification:
                ldl_info = classification["ldl"]
                label = ldl_info.get("label", "")
                if "Tối ưu" in label or "Bình thường" in label:
                    st.success(f"**LDL (mỡ xấu):** {ldl} mmol/L - {label} {ldl_info.get('icon', '')}")
                elif "Cao" in label or "Rất cao" in label or "Nguy hiểm" in label:
                    st.error(f"**LDL (mỡ xấu):** {ldl} mmol/L - {label} {ldl_info.get('icon', '')}")
                else:
                    st.warning(f"**LDL (mỡ xấu):** {ldl} mmol/L - {label} {ldl_info.get('icon', '')}")
            
            # HDL
            if "hdl" in classification:
                hdl_info = classification["hdl"]
                label = hdl_info.get("label", "")
                if "Cao" in label or "Tốt" in label:
                    st.success(f"**HDL (mỡ tốt):** {hdl} mmol/L - {label} {hdl_info.get('icon', '')}")
                else:
                    st.warning(f"**HDL (mỡ tốt):** {hdl} mmol/L - {label} {hdl_info.get('icon', '')}")
            
            # Triglyceride
            if "triglyceride" in classification:
                tg_info = classification["triglyceride"]
                label = tg_info.get("label", "")
                if "Bình thường" in label or "Tốt" in label:
                    st.success(f"**Triglyceride:** {tg} mmol/L - {label} {tg_info.get('icon', '')}")
                elif "Cao" in label or "Rất cao" in label or "Nguy hiểm" in label:
                    st.error(f"**Triglyceride:** {tg} mmol/L - {label} {tg_info.get('icon', '')}")
                else:
                    st.warning(f"**Triglyceride:** {tg} mmol/L - {label} {tg_info.get('icon', '')}")

