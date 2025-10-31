"""
Osteoporosis Tab Component
Hiển thị thông tin về Loãng Xương
"""

import streamlit as st
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

try:
    from diseases.bone_joint.osteoporosis import (
        OSTEOPOROSIS_INFO,
        CAUSES,
        SYMPTOMS,
        DIAGNOSIS,
        TREATMENT,
        NUTRITION,
        PREVENTION
    )
except ImportError:
    st.error("Không thể tải module loãng xương. Vui lòng kiểm tra lại.")
    st.stop()


def render_osteoporosis_tab():
    """Tab Loãng Xương"""
    st.header("🦴 Loãng Xương (Osteoporosis)")
    
    # Thông tin cơ bản
    with st.expander("📖 Loãng xương là gì?", expanded=True):
        if OSTEOPOROSIS_INFO:
            st.markdown(OSTEOPOROSIS_INFO.get("simple_explanation", ""))
            
            # Chuyện gì xảy ra
            if "what_happens" in OSTEOPOROSIS_INFO:
                what_happens = OSTEOPOROSIS_INFO["what_happens"]
                st.markdown(f"### {what_happens.get('title', '')}")
                st.markdown(what_happens.get("explanation", ""))
            
            st.divider()
            
            # Phổ biến
            if "prevalence" in OSTEOPOROSIS_INFO:
                st.markdown("### 📊 Phổ biến ở Việt Nam:")
                prevalence = OSTEOPOROSIS_INFO["prevalence"]
                st.markdown(f"- **Tổng dân số:** {prevalence.get('vietnam', '')}")
                st.markdown(f"- **Phụ nữ sau 50 tuổi:** {prevalence.get('women_50', '')}")
                st.markdown(f"- **Nam giới sau 60 tuổi:** {prevalence.get('men_50', '')}")
            
            # Vị trí thường gãy
            if "common_sites" in OSTEOPOROSIS_INFO:
                st.markdown("### 🔍 Vị trí thường gãy:")
                for site in OSTEOPOROSIS_INFO["common_sites"]:
                    st.markdown(f"- {site}")
            
            # Hậu quả
            if "impact" in OSTEOPOROSIS_INFO:
                impact = OSTEOPOROSIS_INFO["impact"]
                st.markdown(f"### {impact.get('title', '')}")
                for item in impact.get("items", []):
                    st.markdown(f"- {item}")
    
    # Nguyên nhân
    with st.expander("🔍 Nguyên nhân", expanded=False):
        if CAUSES:
            # Không tránh được
            if "unavoidable" in CAUSES:
                unavoidable = CAUSES["unavoidable"]
                st.markdown(f"### {unavoidable.get('title', '')}")
                for factor in unavoidable.get("factors", []):
                    if isinstance(factor, dict):
                        st.markdown(f"**{factor.get('name', '')}:** {factor.get('description', '')}")
                    else:
                        st.markdown(f"- {factor}")
            
            st.divider()
            
            # Có thể thay đổi
            if "modifiable" in CAUSES:
                modifiable = CAUSES["modifiable"]
                st.markdown(f"### {modifiable.get('title', '')}")
                for factor in modifiable.get("factors", []):
                    if isinstance(factor, dict):
                        st.markdown(f"**{factor.get('name', '')}:** {factor.get('description', '')}")
                    else:
                        st.markdown(f"- {factor}")
    
    # Triệu chứng
    with st.expander("⚠️ Triệu chứng", expanded=False):
        if SYMPTOMS:
            # Giai đoạn sớm
            if "early_stage" in SYMPTOMS:
                early = SYMPTOMS["early_stage"]
                st.markdown(f"### {early.get('title', '')}")
                st.markdown(f"**{early.get('description', '')}**")
                if early.get("note"):
                    st.info(early["note"])
            
            st.divider()
            
            # Giai đoạn muộn
            if "advanced_stage" in SYMPTOMS:
                advanced = SYMPTOMS["advanced_stage"]
                st.markdown(f"### {advanced.get('title', '')}")
                for symptom in advanced.get("symptoms", []):
                    if isinstance(symptom, dict):
                        st.markdown(f"**{symptom.get('name', '')}:**")
                        st.markdown(f"  {symptom.get('description', '')}")
                        if symptom.get("location"):
                            st.caption(f"📍 {symptom['location']}")
                        if symptom.get("example"):
                            st.caption(f"💡 {symptom['example']}")
                        if symptom.get("common_sites"):
                            st.markdown("Vị trí thường gãy:")
                            for site in symptom["common_sites"]:
                                st.markdown(f"  - {site}")
            
            # Cảnh báo gãy xương
            if "fracture_warning" in SYMPTOMS:
                warning = SYMPTOMS["fracture_warning"]
                st.warning(f"### {warning.get('title', '')}")
                for sign in warning.get("signs", []):
                    st.markdown(f"- {sign}")
                if warning.get("action"):
                    st.error(f"**{warning['action']}**")
            
            # Khi nào nên đi khám
            if "when_to_see_doctor" in SYMPTOMS:
                when_to_see = SYMPTOMS["when_to_see_doctor"]
                st.markdown(f"### {when_to_see.get('title', '')}")
                for indicator in when_to_see.get("indicators", []):
                    st.markdown(f"- {indicator}")
    
    # Chẩn đoán
    with st.expander("📊 Chẩn đoán", expanded=False):
        if DIAGNOSIS:
            # Phương pháp
            if "method" in DIAGNOSIS:
                method = DIAGNOSIS["method"]
                st.markdown(f"### {method.get('title', '')}")
                if "dxa_scan" in method:
                    dxa = method["dxa_scan"]
                    st.markdown(f"#### {dxa.get('name', '')}")
                    st.markdown(f"**{dxa.get('description', '')}**")
                    st.markdown(f"**Là gì:** {dxa.get('what_is_it', '')}")
                    st.markdown(f"**Đo ở:** {dxa.get('where', '')}")
                    st.markdown(f"**Thời gian:** {dxa.get('duration', '')}")
                    st.markdown(f"**Giá:** {dxa.get('price', '')}")
                    st.markdown(f"**Tần suất:** {dxa.get('frequency', '')}")
            
            st.divider()
            
            # T-Score
            if "t_score" in DIAGNOSIS:
                t_score = DIAGNOSIS["t_score"]
                st.markdown(f"### {t_score.get('title', '')}")
                st.caption(t_score.get("explanation", ""))
                for level in t_score.get("levels", []):
                    st.markdown(f"#### {level.get('range', '')}")
                    st.markdown(f"**{level.get('interpretation', '')}**")
                    st.markdown(level.get("description", ""))
                    if level.get("action"):
                        st.info(f"💡 {level['action']}")
                    st.divider()
            
            # Xét nghiệm khác
            if "other_tests" in DIAGNOSIS:
                other = DIAGNOSIS["other_tests"]
                st.markdown(f"### {other.get('title', '')}")
                if other.get("blood_tests"):
                    for test in other["blood_tests"]:
                        st.markdown(f"- {test}")
                if other.get("purpose"):
                    st.caption(f"**Mục đích:** {other['purpose']}")
            
            # Ai nên đo
            if "who_should_test" in DIAGNOSIS:
                who = DIAGNOSIS["who_should_test"]
                st.markdown(f"### {who.get('title', '')}")
                for criterion in who.get("criteria", []):
                    st.markdown(f"- {criterion}")
    
    # Điều trị
    with st.expander("💊 Điều trị", expanded=False):
        if TREATMENT:
            # Nguyên tắc
            if "principles" in TREATMENT:
                principles = TREATMENT["principles"]
                st.markdown(f"### {principles.get('title', '')}")
                for item in principles.get("items", []):
                    st.markdown(f"- {item}")
            
            st.divider()
            
            # Canxi + Vitamin D
            if "calcium_vitamin_d" in TREATMENT:
                cal_vitd = TREATMENT["calcium_vitamin_d"]
                st.markdown(f"### {cal_vitd.get('title', '')}")
                
                if "calcium" in cal_vitd:
                    calcium = cal_vitd["calcium"]
                    st.markdown("#### Canxi:")
                    st.markdown(f"**Liều hàng ngày:** {calcium.get('daily_dose', '')}")
                    st.markdown(f"**Cách uống:** {calcium.get('with_meal', '')}")
                    st.markdown(f"**Chia liều:** {calcium.get('split_dose', '')}")
                    if calcium.get("forms"):
                        st.markdown("**Dạng thuốc:**")
                        for form in calcium["forms"]:
                            st.markdown(f"  - {form}")
                    if calcium.get("brands_vn"):
                        st.markdown("**Thuốc tại VN:**")
                        for brand in calcium["brands_vn"]:
                            st.markdown(f"  - {brand}")
                    st.markdown(f"**Giá:** {calcium.get('price', '')}")
                    if calcium.get("side_effects"):
                        st.markdown("**Tác dụng phụ:**")
                        for side_effect in calcium["side_effects"]:
                            st.markdown(f"  - {side_effect}")
                
                st.divider()
                
                if "vitamin_d" in cal_vitd:
                    vitd = cal_vitd["vitamin_d"]
                    st.markdown("#### Vitamin D:")
                    st.markdown(f"**Liều hàng ngày:** {vitd.get('daily_dose', '')}")
                    if vitd.get("forms"):
                        st.markdown("**Dạng thuốc:**")
                        for form in vitd["forms"]:
                            st.markdown(f"  - {form}")
                    if vitd.get("brands_vn"):
                        st.markdown("**Thuốc tại VN:**")
                        for brand in vitd["brands_vn"]:
                            st.markdown(f"  - {brand}")
                    st.markdown(f"**Giá:** {vitd.get('price', '')}")
                    if vitd.get("note"):
                        st.info(vitd["note"])
            
            st.divider()
            
            # Thuốc tăng mật độ xương
            if "medications" in TREATMENT:
                meds = TREATMENT["medications"]
                st.markdown(f"### {meds.get('title', '')}")
                st.caption(meds.get("description", ""))
                
                for drug in meds.get("drugs", []):
                    st.markdown(f"#### {drug.get('name', '')}")
                    if drug.get("examples"):
                        st.markdown(f"**Ví dụ:** {', '.join(drug['examples'])}")
                    st.markdown(f"**Cách hoạt động:** {drug.get('how_it_works', '')}")
                    st.markdown(f"**Dạng:** {drug.get('form', '')}")
                    st.markdown(f"**Tần suất:** {drug.get('frequency', '')}")
                    st.markdown(f"**Giá:** {drug.get('price', '')}")
                    if drug.get("side_effects"):
                        st.markdown("**Tác dụng phụ:**")
                        for side_effect in drug["side_effects"]:
                            st.markdown(f"  - {side_effect}")
                    if drug.get("contraindication"):
                        st.warning(f"**Chống chỉ định:** {drug['contraindication']}")
                    if drug.get("note"):
                        st.info(f"💡 {drug['note']}")
                    st.divider()
            
            # Lưu ý điều trị
            if "notes" in TREATMENT:
                notes = TREATMENT["notes"]
                st.markdown("### ⚠️ Lưu ý quan trọng:")
                for note in notes:
                    if isinstance(note, dict):
                        st.markdown(f"**{note.get('title', '')}:**")
                        st.markdown(note.get("content", ""))
                    else:
                        st.markdown(f"- {note}")
    
    # Dinh dưỡng
    with st.expander("🍽️ Dinh dưỡng", expanded=False):
        if NUTRITION:
            # Thực phẩm giàu canxi
            if "calcium_rich_foods" in NUTRITION:
                calcium_foods = NUTRITION["calcium_rich_foods"]
                st.markdown(f"### {calcium_foods.get('title', '')}")
                for food in calcium_foods.get("foods", []):
                    if isinstance(food, dict):
                        st.markdown(f"#### {food.get('name', '')}")
                        if food.get("examples"):
                            st.markdown(f"**Ví dụ:** {', '.join(food['examples'])}")
                        st.markdown(f"**Canxi:** {food.get('calcium', '')}")
                        if food.get("serving"):
                            st.markdown(f"**Khẩu phần:** {food['serving']}")
                        if food.get("tip"):
                            st.caption(f"💡 {food['tip']}")
                        st.divider()
            
            # Thực phẩm giàu vitamin D
            if "vitamin_d_foods" in NUTRITION:
                vitd_foods = NUTRITION["vitamin_d_foods"]
                st.markdown(f"### {vitd_foods.get('title', '')}")
                for food in vitd_foods.get("foods", []):
                    if isinstance(food, dict):
                        st.markdown(f"#### {food.get('name', '')}")
                        if food.get("examples"):
                            st.markdown(f"**Ví dụ:** {', '.join(food['examples'])}")
                        st.markdown(f"**Vitamin D:** {food.get('vitamin_d', '')}")
                        st.divider()
            
            # Thực phẩm cần tránh
            if "foods_to_avoid" in NUTRITION:
                avoid = NUTRITION["foods_to_avoid"]
                st.markdown(f"### {avoid.get('title', '')}")
                for item in avoid.get("items", []):
                    if isinstance(item, dict):
                        st.markdown(f"**{item.get('name', '')}:** {item.get('reason', '')}")
                    else:
                        st.markdown(f"- {item}")
    
    # Phòng ngừa
    with st.expander("🛡️ Phòng ngừa", expanded=False):
        if PREVENTION:
            # Cả đời
            if "lifelong" in PREVENTION:
                lifelong = PREVENTION["lifelong"]
                st.markdown(f"### {lifelong.get('title', '')}")
                st.success(f"**{lifelong.get('key_message', '')}**")
                for stage in lifelong.get("stages", []):
                    if isinstance(stage, dict):
                        st.markdown(f"#### {stage.get('stage', '')}")
                        for action in stage.get("actions", []):
                            st.markdown(f"- {action}")
                        st.divider()
            
            # Vận động
            if "exercise" in PREVENTION:
                exercise = PREVENTION["exercise"]
                st.markdown(f"### {exercise.get('title', '')}")
                
                if "weight_bearing" in exercise:
                    weight = exercise["weight_bearing"]
                    st.markdown(f"#### {weight.get('title', '')}")
                    for ex in weight.get("exercises", []):
                        st.markdown(f"- {ex}")
                    st.info(f"**Lợi ích:** {weight.get('benefit', '')}")
                
                st.divider()
                
                if "resistance" in exercise:
                    resistance = exercise["resistance"]
                    st.markdown(f"#### {resistance.get('title', '')}")
                    for ex in resistance.get("exercises", []):
                        st.markdown(f"- {ex}")
                    if resistance.get("frequency"):
                        st.caption(f"**Tần suất:** {resistance['frequency']}")
                
                st.divider()
                
                if "balance" in exercise:
                    balance = exercise["balance"]
                    st.markdown(f"#### {balance.get('title', '')}")
                    st.markdown(balance.get("why", ""))
                    for ex in balance.get("exercises", []):
                        st.markdown(f"- {ex}")
            
            # Phòng ngã
            if "prevent_falls" in PREVENTION:
                falls = PREVENTION["prevent_falls"]
                st.markdown(f"### {falls.get('title', '')}")
                st.markdown(falls.get("why", ""))
                
                if "home_safety" in falls:
                    safety = falls["home_safety"]
                    st.markdown(f"#### {safety.get('title', '')}")
                    for tip in safety.get("tips", []):
                        st.markdown(f"- {tip}")
                
                if "outdoor_safety" in falls:
                    outdoor = falls["outdoor_safety"]
                    st.markdown(f"#### {outdoor.get('title', '')}")
                    for tip in outdoor.get("tips", []):
                        st.markdown(f"- {tip}")

