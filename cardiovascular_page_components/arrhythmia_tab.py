"""
Tab: Rối Loạn Nhịp Tim (Arrhythmia)
Hiển thị thông tin về các loại rối loạn nhịp tim phổ biến
"""

import streamlit as st


# ============= DATA DICTIONARIES =============

DISEASE_INFO = {
    "description_vn": """
    **Rối loạn nhịp tim** là tình trạng tim đập **quá nhanh, quá chậm, hoặc không đều**.
    
    🫀 **Tim bình thường:** Đập 60-100 nhịp/phút, đều đặn như đồng hồ  
    ⚠️ **Rối loạn nhịp:** Tim đập bất thường → ảnh hưởng tuần hoàn máu
    
    💡 **Hiểu đơn giản:** Tim như máy bơm nước, nếu bơm nhanh/chậm bất thường → nước không lưu thông tốt
    """,
    
    "prevalence_vn": "Rất phổ biến, đặc biệt ở người già, người có bệnh tim sẵn có"
}

SYMPTOMS = {
    "common_vn": [
        "**Hồi hộp, đánh trống ngực** - Cảm giác tim đập mạnh trong ngực",
        "**Tim đập nhanh** - Cảm thấy tim đập nhanh > 100 nhịp/phút",
        "**Tim đập chậm** - Cảm thấy tim đập chậm < 60 nhịp/phút",
        "**Tim bỏ sót nhịp** - Cảm giác tim ngừng vài giây rồi lại đập mạnh",
        "**Khó thở** - Thở gấp, hụt hơi",
        "**Mệt mỏi** - Người yếu, không muốn làm gì",
        "**Chóng mặt, choáng váng** - Đầu quay quay, muốn ngất"
    ],
    
    "serious_vn": [
        "🚨 **Ngất xỉu** - Mất ý thức ngã xuống",
        "🚨 **Đau ngực** - Đau như bị đè ép",
        "🚨 **Khó thở nặng** - Không thở được",
        "🚨 **Mạch rất nhanh** - >150 nhịp/phút",
        "🚨 **Mạch rất chậm** - <40 nhịp/phút với triệu chứng"
    ]
}

TYPES = {
    "tachycardia": {
        "name": "❤️‍🩹 Tim Đập Nhanh (Tachycardia)",
        "description": "Tim đập **> 100 nhịp/phút** khi nghỉ",
        "examples": [
            "**Sinus tachycardia:** Tim nhanh bình thường (do căng thẳng, uống cà phê)",
            "**Atrial fibrillation:** Tim rung nhĩ, đập không đều (nguy hiểm!)",
            "**Supraventricular:** Tim đập nhanh đột ngột ở người trẻ"
        ],
        "treatment": "Tùy loại: Thở sâu → Thuốc → Sốc điện → Đốt điện",
        "when_worry": "Tim > 150 nhịp/phút kèm khó thở/đau ngực → Gọi 115"
    },
    
    "bradycardia": {
        "name": "❤️‍🩹 Tim Đập Chậm (Bradycardia)",
        "description": "Tim đập **< 60 nhịp/phút**",
        "examples": [
            "**Người khỏe mạnh:** Vận động viên tim đập 40-50 nhịp/phút (bình thường)",
            "**Sick sinus:** Mạch chậm do bệnh tim sẵn có",
            "**Heart block:** Tim bỏ sót nhịp do dẫn truyền bị tắc"
        ],
        "treatment": "Không triệu chứng: Theo dõi. Có triệu chứng: Máy tạo nhịp",
        "when_worry": "Tim < 40 nhịp/phút kèm chóng mặt/ngất → Gọi 115"
    },
    
    "premature": {
        "name": "❤️‍🩹 Tim Bỏ Sót Nhịp (Premature Beat)",
        "description": "Tim đập thêm 1 nhịp sớm, sau đó nghỉ dài rồi đập mạnh",
        "examples": [
            "**PAC:** Nhịp sớm ở tâm nhĩ (ít nguy hiểm)",
            "**PVC:** Nhịp sớm ở tâm thất (cần khám nếu thường xuyên)"
        ],
        "treatment": "Ít: Không cần điều trị. Nhiều: Thuốc, loại bỏ nguyên nhân",
        "when_worry": "Bỏ sót > 5 lần/phút kèm khó thở → Khám bác sĩ"
    }
}

COMMON_CAUSES = {
    "reversible": [
        "**Căng thẳng (Stress)** - Lo lắng, sợ hãi",
        "**Cà phê, trà đậm** - Quá nhiều caffeine",
        "**Rượu, bia** - Sau khi uống",
        "**Thiếu ngủ** - Mệt mỏi kéo dài",
        "**Thuốc** - Thuốc cảm, hen suyễn",
        "**Thiếu nước** - Mất nước"
    ],
    
    "heart_disease": [
        "**Bệnh tim sẵn có** - Bệnh mạch vành, suy tim",
        "**Sau nhồi máu cơ tim** - Tim bị tổn thương",
        "**Bệnh van tim** - Van tim hư hỏng",
        "**Bẩm sinh** - Tim bất thường từ nhỏ"
    ],
    
    "other": [
        "**Tăng huyết áp** - Huyết áp cao lâu ngày",
        "**Rối loạn tuyến giáp** - Cường giáp (tim nhanh)",
        "**Rối loạn điện giải** - Thiếu kali, magie",
        "**Tuổi già** - Tổn thương tim do tuổi tác"
    ]
}

ACTIONS = {
    "immediate": [
        "1️⃣ **Thở sâu, chậm:** Hít vào 4 giây, thở ra 4 giây (làm 5-10 lần)",
        "2️⃣ **Nằm nghỉ:** Nằm xuống, thả lỏng cơ thể",
        "3️⃣ **Uống nước:** Nếu khát hoặc mất nước",
        "4️⃣ **Loại bỏ nguyên nhân:** Nghỉ cà phê, rượu, thuốc cảm",
        "5️⃣ **Theo dõi mạch:** Đếm mạch trong 1 phút",
        "",
        "⏱️ **Nếu không đỡ sau 10 phút** hoặc triệu chứng nặng → Khám bác sĩ ngay"
    ],
    
    "prevention": [
        "✅ **Giảm stress:** Tập thiền, yoga, thư giãn",
        "✅ **Hạn chế cà phê:** Không quá 1-2 ly/ngày",
        "✅ **Ngủ đủ:** 7-9 giờ/đêm",
        "✅ **Tập thể dục vừa phải:** Đi bộ 30 phút/ngày",
        "✅ **Không hút thuốc:** Thuốc lá hại tim",
        "✅ **Kiểm soát huyết áp:** Uống thuốc đều đặn",
        "✅ **Giữ cân nặng hợp lý:** Tránh béo phì"
    ]
}

WHEN_TO_SEE_DOCTOR = {
    "urgent": [
        "🚨 **GỌI 115 NGAY NẾU:**",
        "",
        "- **Ngất xỉu** (mất ý thức)",
        "- **Đau ngực dữ dội** (đau như bị đè ép)",
        "- **Tim đập > 150 nhịp/phút** kèm khó thở",
        "- **Tim < 40 nhịp/phút** kèm chóng mặt",
        "- **Không thở được**",
        "- **Đang có bệnh tim** + triệu chứng mới"
    ],
    
    "soon": [
        "📋 **KHÁM BÁC SĨ TRONG TUẦN NẾU:**",
        "",
        "- Tim bỏ sót nhịp **thường xuyên** (> 5 lần/phút)",
        "- Hồi hộp **kéo dài > 30 phút** không đỡ",
        "- **Mệt mỏi, khó thở** kéo dài",
        "- **Lần đầu tiên** bị rối loạn nhịp tim",
        "- Đang dùng thuốc tim mạch + triệu chứng mới"
    ]
}

MEDICATIONS = {
    "antiarrhythmic": {
        "name": "💊 Thuốc Chống Loạn Nhịp",
        "examples": [
            "**Metoprolol (Betabloc)** - Giảm tim nhanh, hạ huyết áp",
            "**Digoxin** - Tăng sức co bóp tim, chậm nhịp",
            "**Amiodarone** - Chống nhiều loại loạn nhịp (mạnh)",
            "**Verapamil** - Giảm tim nhanh"
        ],
        "note": "⚠️ Uống đúng giờ, đúng liều. KHÔNG tự ý ngưng thuốc!"
    },
    
    "anticoagulation": {
        "name": "💊 Thuốc Chống Đông (Với Rung Nhĩ)",
        "examples": [
            "**Warfarin** - Thuốc cũ, phải xét nghiệm máu",
            "**Apixaban, Dabigatran** - Thuốc mới, không cần xét nghiệm"
        ],
        "note": "🩸 Phòng ngừa đột quỵ do cục máu đông. Dễ chảy máu → Tránh va đập!"
    },
    
    "pacemaker": {
        "name": "🔋 Máy Tạo Nhịp Tim (Pacemaker)",
        "description": "Khi tim đập quá chậm → Gắn máy tạo nhịp",
        "types": [
            "**Tạm thời:** Qua tĩnh mạch, dùng vài ngày",
            "**Vĩnh viễn:** Phẫu thuật gắn máy dưới da"
        ],
        "after_surgery": [
            "✅ Nghỉ ngơi 1 tuần sau phẫu thuật",
            "✅ Tránh động tác tay mạnh 1 tháng",
            "✅ Không đến gần máy quét an ninh",
            "✅ Theo dõi định kỳ mỗi 6 tháng"
        ]
    }
}


# ============= RENDER FUNCTIONS =============

def render_arrhythmia_tab():
    """Render tab Rối Loạn Nhịp Tim"""
    
    st.header("❤️‍🩹 Rối Loạn Nhịp Tim")
    
    # Cảnh báo quan trọng
    st.error("""
    **⚠️ QUAN TRỌNG:** Rối loạn nhịp tim có thể nguy hiểm!
    - Nếu có triệu chứng **NGẶT XỈU**, **ĐAU NGỰC**, **KHÓ THỞ NẶNG** → **GỌI 115 NGAY!**
    """)
    
    # Giới thiệu
    with st.expander("📖 Rối loạn nhịp tim là gì?", expanded=True):
        st.markdown(DISEASE_INFO["description_vn"])
        st.info(f"**Phổ biến:** {DISEASE_INFO['prevalence_vn']}")
    
    # Triệu chứng
    with st.expander("🔍 Dấu hiệu nhận biết"):
        st.subheader("Triệu chứng thường gặp:")
        for symptom in SYMPTOMS["common_vn"]:
            st.markdown(f"- {symptom}")
        
        st.divider()
        st.error("**⚠️ TRIỆU CHỨNG NGUY HIỂM - GỌI 115:**")
        for symptom in SYMPTOMS["serious_vn"]:
            st.markdown(f"**{symptom}**")
    
    # Các loại rối loạn nhịp tim
    with st.expander("📋 Các loại rối loạn nhịp tim phổ biến"):
        for type_key, type_info in TYPES.items():
            st.subheader(type_info["name"])
            st.markdown(f"**Mô tả:** {type_info['description']}")
            
            st.markdown("**Ví dụ:**")
            for example in type_info["examples"]:
                st.markdown(f"- {example}")
            
            st.markdown(f"**💡 {type_info['treatment']}**")
            st.warning(f"⚠️ **Khi nào lo:** {type_info['when_worry']}")
            st.divider()
    
    # Nguyên nhân
    with st.expander("🤔 Nguyên nhân thường gặp"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("**✅ Nguyên nhân có thể khắc phục:**")
            for cause in COMMON_CAUSES["reversible"]:
                st.markdown(f"- {cause}")
        
        with col2:
            st.warning("**⚠️ Nguyên nhân do bệnh tim:**")
            for cause in COMMON_CAUSES["heart_disease"]:
                st.markdown(f"- {cause}")
        
        st.divider()
        st.info("**💡 Nguyên nhân khác:** " + ", ".join(COMMON_CAUSES["other"]))
    
    # Xử trí
    with st.expander("⚡ Xử trí tại nhà"):
        st.markdown("**KHI TIM ĐẬP BẤT THƯỜNG:**")
        for action in ACTIONS["immediate"]:
            if action == "":
                st.divider()
            else:
                st.markdown(action)
        
        st.divider()
        
        st.markdown("**PHÒNG NGỪA:**")
        for prevention in ACTIONS["prevention"]:
            st.markdown(f"- {prevention}")
    
    # Khi nào khám bác sĩ
    with st.expander("🏥 Khi nào cần khám bác sĩ"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.error("\n".join(WHEN_TO_SEE_DOCTOR["urgent"]))
        
        with col2:
            st.warning("\n".join(WHEN_TO_SEE_DOCTOR["soon"]))
    
    # Thuốc điều trị
    with st.expander("💊 Thuốc & Điều trị"):
        st.subheader("📋 Thuốc chống loạn nhịp")
        for med_info in [MEDICATIONS["antiarrhythmic"], MEDICATIONS["anticoagulation"]]:
            st.markdown(f"**{med_info['name']}**")
            for example in med_info["examples"]:
                st.markdown(f"- {example}")
            st.markdown(f"💡 {med_info['note']}")
            st.divider()
        
        st.subheader("🔋 Máy tạo nhịp tim")
        st.markdown(f"**{MEDICATIONS['pacemaker']['description']}**")
        st.markdown("**Các loại:**")
        for ptype in MEDICATIONS["pacemaker"]["types"]:
            st.markdown(f"- {ptype}")
        
        st.markdown("**💡 Sau phẫu thuật:**")
        for after in MEDICATIONS["pacemaker"]["after_surgery"]:
            st.markdown(f"- {after}")
    
    # Lưu ý
    st.info("""
    💡 **LƯU Ý:** 
    - Rối loạn nhịp tim cần **điện tâm đồ (ECG)** để chẩn đoán chính xác
    - Nhiều trường hợp **không cần điều trị**, chỉ theo dõi
    - **Quan trọng nhất:** Phát hiện sớm và xử trí kịp thời khi nguy hiểm
    """)

