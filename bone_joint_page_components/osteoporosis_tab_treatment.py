"""
Osteoporosis Tab - Diagnosis, Treatment, Nutrition, Prevention
Chẩn đoán, điều trị, dinh dưỡng, phòng ngừa
"""

import streamlit as st
from diseases.bone_joint.osteoporosis import DIAGNOSIS, TREATMENT, NUTRITION, PREVENTION


def render_osteoporosis_diagnosis():
    """Render chẩn đoán"""
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


def render_osteoporosis_treatment():
    """Render điều trị"""
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


def render_osteoporosis_nutrition():
    """Render dinh dưỡng"""
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


def render_osteoporosis_prevention():
    """Render phòng ngừa"""
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
                    if balance.get("benefit"):
                        st.info(f"**Lợi ích:** {balance.get('benefit', '')}")
                    for ex in balance.get("exercises", []):
                        st.markdown(f"- {ex}")
            
            # Phòng ngã
            if "prevent_falls" in PREVENTION:
                falls = PREVENTION["prevent_falls"]
                st.markdown(f"### {falls.get('title', '')}")
                
                if "home_safety" in falls:
                    safety = falls["home_safety"]
                    st.markdown("#### 🏠 An toàn trong nhà:")
                    if isinstance(safety, list):
                        for tip in safety:
                            st.markdown(f"- {tip}")
                    else:
                        st.markdown(f"- {safety}")
                
                if "personal" in falls:
                    personal = falls["personal"]
                    st.markdown("#### 👤 Bản thân:")
                    if isinstance(personal, list):
                        for tip in personal:
                            st.markdown(f"- {tip}")
                    else:
                        st.markdown(f"- {personal}")

