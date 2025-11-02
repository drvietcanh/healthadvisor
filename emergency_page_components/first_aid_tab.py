"""
Tab 2: Hướng Dẫn Sơ Cứu
Hiển thị hướng dẫn sơ cứu theo từng tình huống
"""

import streamlit as st
from emergency_contacts import FIRST_AID_GUIDES

def render_first_aid_tab():
    """Render tab Hướng dẫn Sơ cứu"""
    st.header("🏥 Hướng dẫn Sơ cứu Nhanh")
    
    st.info("""
    💡 **Lưu ý:** Đây chỉ là hướng dẫn sơ cứu cơ bản. 
    **LUÔN GỌI 115** trong trường hợp nghiêm trọng!
    """)
    
    # Chọn tình huống
    situations = {
        "heart_attack": "❤️ Đau tim cấp",
        "stroke": "🧠 Đột quỵ (F.A.S.T)",
        "choking_child": "👶 Trẻ em hóc dị vật",
        "choking_adult": "😰 Người lớn hóc dị vật",
        "burns": "🔥 Bỏng nhiệt/Nước sôi",
        "hypoglycemia": "🍬 Hạ đường huyết",
        "poisoning": "☠️ Ngộ độc",
        "bleeding": "🩸 Chảy máu",
        "drowning": "🌊 Đuối nước",
        "electric_shock": "⚡ Điện giật",
        "spinal_injury": "🦴 Chấn thương cột sống cổ",
        "fall": "🤕 Ngã",
        "chest_pain": "💔 Đau ngực",
        "anaphylaxis": "⚡ Sốc phản vệ",
        "seizure": "⚡ Co giật (Động kinh)",
        "unconscious": "😴 Hôn mê/Bất tỉnh",
        "alcohol_poisoning": "🍺 Ngộ độc rượu",
        "fracture": "🦴 Gãy xương",
        "cardiac_arrest": "💔 Ngừng tim - CPR",
        "heat_stroke": "☀️ Sốc nhiệt/Cảm nắng",
        "nosebleed": "🩸 Chảy máu cam nặng",
        "acute_abdominal_pain": "😣 Đau bụng cấp",
        "head_injury": "🤕 Chấn thương đầu",
        "snake_bite": "🐍 Rắn cắn",
        "food_poisoning": "🍽️ Ngộ độc thực phẩm"
    }
    
    selected = st.selectbox(
        "Chọn tình huống:",
        list(situations.keys()),
        format_func=lambda x: situations[x],
        key="first_aid_selector"
    )
    
    if selected:
        guide = FIRST_AID_GUIDES[selected]
        
        st.markdown(f"## {guide['icon']} {guide['name']}")
        
        # Dấu hiệu
        if 'signs' in guide:
            st.markdown(f"### {guide['signs']['title']}")
            for sign in guide['signs']['items']:
                st.markdown(f"{sign}")
            if 'note' in guide['signs']:
                st.info(guide['signs']['note'])
        
        # Phân loại (cho bỏng)
        if 'classification' in guide:
            st.markdown(f"### {guide['classification']['title']}")
            st.caption(guide['classification'].get('rule', ''))
            if 'examples' in guide['classification']:
                for ex in guide['classification']['examples']:
                    st.markdown(f"- {ex}")
            if 'severe_if' in guide['classification']:
                st.warning("**Bỏng nặng nếu:**")
                for item in guide['classification']['severe_if']:
                    st.markdown(f"- {item}")
        
        if 'other_signs' in guide:
            st.markdown("### Các dấu hiệu khác:")
            for sign in guide['other_signs']:
                st.markdown(f"- {sign}")
        
        if 'risk_situations' in guide:
            st.warning(f"### {guide['risk_situations']['title']}")
            for item in guide['risk_situations']['items']:
                st.markdown(f"- {item}")
        
        st.divider()
        
        # Xử lý
        if 'actions' in guide:
            st.error(f"### {guide['actions']['title']}")
            for step in guide['actions']['steps']:
                st.markdown(f"{step}")
        
        # Trường hợp nghiêm trọng
        if 'severe' in guide:
            st.markdown(f"### {guide['severe']['title']}")
            for step in guide['severe']['steps']:
                st.markdown(f"{step}")
        
        # Tự xử lý (self_help)
        if 'self_help' in guide:
            st.markdown(f"### {guide['self_help']['title']}")
            for step in guide['self_help']['steps']:
                st.markdown(f"{step}")
        
        # Phân biệt (vs_heat_exhaustion)
        if 'vs_heat_exhaustion' in guide:
            vs = guide['vs_heat_exhaustion']
            st.markdown(f"### {vs.get('title', '')}")
            col1, col2 = st.columns(2)
            with col1:
                if 'heat_exhaustion' in vs:
                    he = vs['heat_exhaustion']
                    st.success(f"**{he.get('name', '')}**")
                    for symptom in he.get('symptoms', []):
                        st.markdown(f"- {symptom}")
                    if he.get('action'):
                        st.info(he['action'])
            with col2:
                if 'heat_stroke' in vs:
                    hs = vs['heat_stroke']
                    st.error(f"**{hs.get('name', '')}**")
                    for symptom in hs.get('symptoms', []):
                        st.markdown(f"- {symptom}")
                    if hs.get('action'):
                        st.error(hs['action'])
        
        # Ép ngực đơn giản (compression_only)
        if 'compression_only' in guide:
            comp = guide['compression_only']
            st.markdown(f"### {comp.get('title', '')}")
            st.caption(comp.get('description', ''))
            for step in comp.get('steps', []):
                st.markdown(f"- {step}")
            if comp.get('note'):
                st.info(comp['note'])
        
        # Nguyên nhân nguy hiểm (dangerous_causes)
        if 'dangerous_causes' in guide:
            dc = guide['dangerous_causes']
            st.warning(f"### {dc.get('title', '')}")
            for cause in dc.get('causes', []):
                st.markdown(f"- {cause}")
        
        # Theo dõi (observations)
        if 'observations' in guide:
            obs = guide['observations']
            st.info(f"### {obs.get('title', '')}")
            for item in obs.get('items', []):
                st.markdown(f"- {item}")
        
        # Bệnh viện (hospitals)
        if 'hospitals' in guide:
            hosp = guide['hospitals']
            st.markdown(f"### {hosp.get('title', '')}")
            for hospital in hosp.get('vietnam', []):
                st.markdown(f"- {hospital}")
        
        # Khi nào gọi 115
        if 'call_115' in guide:
            st.error(f"### {guide['call_115']['title']}")
            for item in guide['call_115']['items']:
                st.markdown(f"{item}")
        
        # Khi nào gọi 115 (when_call_115 - cho bỏng)
        if 'when_call_115' in guide:
            st.error(f"### {guide['when_call_115']['title']}")
            for item in guide['when_call_115']['items']:
                st.markdown(f"- {item}")
        
        # Chăm sóc tại nhà (cho bỏng)
        if 'home_care' in guide:
            st.info(f"### {guide['home_care']['title']}")
            for step in guide['home_care']['steps']:
                st.markdown(f"{step}")
        
        # Biến chứng (cho bỏng)
        if 'complications' in guide:
            st.warning(f"### {guide['complications']['title']}")
            for item in guide['complications']['items']:
                st.markdown(f"- {item}")
        
        # Không được làm
        if 'dont' in guide:
            st.warning(f"### {guide['dont']['title']}")
            for item in guide['dont']['items']:
                st.markdown(f"{item}")
        
        # Phòng ngừa
        if 'prevention' in guide:
            st.success(f"### {guide['prevention']['title']}")
            for item in guide['prevention']['items']:
                st.markdown(f"{item}")
        
        # Ghi chú
        if 'note' in guide:
            st.markdown(f"""
            <div class='warning-box'>
                {guide['note']}
            </div>
            """, unsafe_allow_html=True)

