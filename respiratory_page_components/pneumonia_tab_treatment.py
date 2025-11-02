"""
Pneumonia Tab - Diagnosis, Treatment, Prevention, Complications
Chẩn đoán, điều trị, phòng ngừa, biến chứng
"""

import streamlit as st
from diseases.respiratory import pneumonia


def render_pneumonia_diagnosis():
    """Render chẩn đoán"""
    with st.expander("🔬 Chẩn đoán"):
        if hasattr(pneumonia, 'DIAGNOSIS') and pneumonia.DIAGNOSIS:
            diag = pneumonia.DIAGNOSIS
            
            # Xét nghiệm
            if "tests" in diag:
                tests = diag["tests"]
                st.markdown("### 📋 Xét nghiệm chẩn đoán")
                if "common" in tests:
                    for test in tests["common"][:3]:
                        if isinstance(test, dict):
                            st.markdown(f"**{test.get('name', '')}**")
                            st.caption(test.get('description', ''))
                            if "findings" in test:
                                for finding in test["findings"]:
                                    st.markdown(f"- {finding}")
                            if "note" in test:
                                st.warning(test["note"])
                            st.divider()
            
            # Đánh giá mức độ nặng
            if "severity_assessment" in diag:
                severity = diag["severity_assessment"]
                st.markdown("### 📊 Đánh giá mức độ nặng (CURB-65)")
                st.caption(severity.get('description', ''))
                if "scores" in severity:
                    for score_item in severity["scores"]:
                        if isinstance(score_item, dict):
                            st.markdown(f"**{score_item.get('score', '')}:** {score_item.get('severity', '')}")
                            st.caption(f"Điều trị: {score_item.get('treatment', '')}")
                            if score_item.get('mortality'):
                                st.warning(f"Tỷ lệ tử vong: {score_item['mortality']}")
                            st.divider()
                if "note" in severity:
                    st.error(severity["note"])


def render_pneumonia_treatment():
    """Render điều trị"""
    with st.expander("💊 Điều trị viêm phổi", expanded=True):
        if hasattr(pneumonia, 'TREATMENT') and pneumonia.TREATMENT:
            treatment = pneumonia.TREATMENT
            
            # Kháng sinh
            if "antibiotics" in treatment:
                abx = treatment["antibiotics"]
                st.markdown("### 🦠 Kháng sinh")
                st.caption("Chọn kháng sinh theo mức độ nặng:")
                
                # Nhẹ
                if "mild" in abx:
                    mild = abx["mild"]
                    st.markdown(f"#### {mild.get('name', 'Viêm phổi nhẹ')}")
                    if "options" in mild:
                        for opt in mild["options"][:2]:
                            st.markdown(f"**{opt.get('name', '')}**")
                            st.caption(f"Liều: {opt.get('dosage', '')}")
                            st.caption(f"Thời gian: {opt.get('duration', '')}")
                            if opt.get('note'):
                                st.info(opt['note'])
                    if "note" in mild:
                        st.warning(mild["note"])
                    st.divider()
                
                # Trung bình
                if "moderate" in abx:
                    mod = abx["moderate"]
                    st.markdown(f"#### {mod.get('name', 'Viêm phổi trung bình')}")
                    if "options" in mod:
                        for opt in mod["options"][:2]:
                            st.markdown(f"**{opt.get('name', '')}**")
                            st.caption(f"Liều: {opt.get('dosage', '')}")
                            st.caption(f"Thời gian: {opt.get('duration', '')}")
                
                # Nặng
                if "severe" in abx:
                    severe = abx["severe"]
                    st.markdown(f"#### {severe.get('name', 'Viêm phổi nặng')}")
                    st.error(severe.get('warning', ''))
                    if "options" in severe:
                        for opt in severe["options"][:2]:
                            st.markdown(f"**{opt.get('name', '')}**")
                            st.caption(f"Liều: {opt.get('dosage', '')}")
            
            # Điều trị hỗ trợ
            if "supportive" in treatment:
                supportive = treatment["supportive"]
                st.markdown("### 💉 Điều trị hỗ trợ")
                if "treatments" in supportive:
                    for tx in supportive["treatments"][:3]:
                        if isinstance(tx, dict):
                            st.markdown(f"**{tx.get('name', '')}**")
                            if tx.get('indication'):
                                st.caption(f"Khi nào: {tx['indication']}")
                            if "methods" in tx:
                                for method in tx["methods"]:
                                    st.markdown(f"- {method}")
                            if "medications" in tx:
                                for med in tx["medications"]:
                                    st.markdown(f"- {med}")
                            if tx.get('note'):
                                st.info(tx['note'])
                            st.divider()
            
            # Khi nào cần nhập viện
            if "when_to_hospitalize" in treatment:
                hosp = treatment["when_to_hospitalize"]
                st.error("### 🏥 Khi nào cần nhập viện?")
                if "criteria" in hosp:
                    for criterion in hosp["criteria"][:3]:
                        if isinstance(criterion, dict):
                            st.markdown(f"**{criterion.get('indication', '')}**")
                            if "details" in criterion:
                                for detail in criterion["details"]:
                                    st.markdown(f"- {detail}")
                if "warning" in hosp:
                    st.error(hosp["warning"])


def render_pneumonia_prevention():
    """Render phòng ngừa"""
    with st.expander("🛡️ Phòng ngừa viêm phổi"):
        if hasattr(pneumonia, 'PREVENTION') and pneumonia.PREVENTION:
            prev = pneumonia.PREVENTION
            
            # Vaccine
            if "vaccination" in prev:
                vacc = prev["vaccination"]
                st.markdown("### 💉 Tiêm vaccine (QUAN TRỌNG NHẤT!)")
                st.caption(vacc.get('description', ''))
                if "vaccines" in vacc:
                    for vax in vacc["vaccines"][:3]:
                        if isinstance(vax, dict):
                            st.markdown(f"**{vax.get('name', '')}**")
                            st.caption(f"Đối tượng: {vax.get('target', '')}")
                            if "schedule" in vax:
                                if isinstance(vax["schedule"], list):
                                    for sched in vax["schedule"][:2]:
                                        st.markdown(f"- {sched}")
                                else:
                                    st.caption(vax["schedule"])
                            if vax.get('effectiveness'):
                                st.success(f"Hiệu quả: {vax['effectiveness']}")
                            if vax.get('note'):
                                st.warning(vax['note'])
                            st.divider()
            
            # Lối sống
            if "lifestyle" in prev:
                lifestyle = prev["lifestyle"]
                st.markdown("### 🏃 Lối sống lành mạnh")
                if "recommendations" in lifestyle:
                    for rec in lifestyle["recommendations"][:5]:
                        if isinstance(rec, dict):
                            st.markdown(f"**{rec.get('name', '')}**")
                            st.caption(rec.get('description', ''))
                            if "when" in rec:
                                for when in rec["when"]:
                                    st.markdown(f"- {when}")
                            if rec.get('benefit'):
                                st.success(f"Lợi ích: {rec['benefit']}")
                            if rec.get('note'):
                                st.warning(rec['note'])
            
            # Dấu hiệu cảnh báo
            if "warning_signs" in prev:
                warnings = prev["warning_signs"]
                st.error("### ⚠️ Khi nào cần đi khám ngay?")
                if "signs" in warnings:
                    for sign_item in warnings["signs"][:2]:
                        if isinstance(sign_item, dict):
                            st.markdown(f"**{sign_item.get('name', '')}**")
                            if "details" in sign_item:
                                for detail in sign_item["details"]:
                                    st.markdown(f"- {detail}")
                if "emergency" in warnings:
                    st.error(warnings["emergency"])


def render_pneumonia_complications():
    """Render biến chứng"""
    with st.expander("⚠️ Biến chứng"):
        if hasattr(pneumonia, 'COMPLICATIONS') and pneumonia.COMPLICATIONS:
            comp = pneumonia.COMPLICATIONS
            
            if "systemic" in comp:
                systemic = comp["systemic"]
                st.error(f"### {systemic.get('name', 'Toàn thân')}")
                if "complications" in systemic:
                    for comp_item in systemic["complications"][:2]:
                        if isinstance(comp_item, dict):
                            st.markdown(f"**{comp_item.get('name', '')}**")
                            st.caption(comp_item.get('description', ''))
                            if comp_item.get('mortality'):
                                st.error(f"Tỷ lệ tử vong: {comp_item['mortality']}")
                            if comp_item.get('warning'):
                                st.error(comp_item['warning'])
                            st.divider()

