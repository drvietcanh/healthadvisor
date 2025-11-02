"""
Viêm phổi (Pneumonia) Tab Component
Hiển thị thông tin về bệnh Viêm phổi
"""

import streamlit as st
import sys
sys.path.append('..')
from diseases.respiratory import pneumonia


def render_pneumonia_tab():
    """Render tab Viêm phổi với đầy đủ thông tin"""
    st.header("🫁 Viêm phổi (Pneumonia)")
    
    # Thông tin cơ bản
    with st.expander("📖 Viêm phổi là gì?", expanded=True):
        if hasattr(pneumonia, 'PNEUMONIA_INFO') and pneumonia.PNEUMONIA_INFO:
            info_dict = pneumonia.PNEUMONIA_INFO
            if isinstance(info_dict, dict):
                st.markdown(info_dict.get("simple_explanation", ""))
                if info_dict.get("why_dangerous"):
                    st.warning(info_dict.get("why_dangerous"))
    
    # Nguyên nhân
    with st.expander("🔍 Nguyên nhân viêm phổi"):
        if hasattr(pneumonia, 'CAUSES') and pneumonia.CAUSES:
            causes = pneumonia.CAUSES
            if isinstance(causes, dict):
                # Vi khuẩn
                if "bacteria" in causes:
                    bacteria = causes["bacteria"]
                    st.markdown(f"### {bacteria.get('name', 'Vi khuẩn')}")
                    st.caption(bacteria.get('description', ''))
                    if "common" in bacteria:
                        for b in bacteria["common"][:2]:
                            st.markdown(f"**{b.get('name', '')}**")
                            st.caption(b.get('description', ''))
                            if b.get('prevention'):
                                st.success(f"💡 {b['prevention']}")
                    st.divider()
                
                # Virus
                if "viruses" in causes:
                    viruses = causes["viruses"]
                    st.markdown(f"### {viruses.get('name', 'Virus')}")
                    st.caption(viruses.get('description', ''))
                    if "common" in viruses:
                        for v in viruses["common"][:3]:
                            st.markdown(f"**{v.get('name', '')}**")
                            st.caption(v.get('description', ''))
                            if v.get('prevention'):
                                st.success(f"💡 {v['prevention']}")
                            if v.get('warning'):
                                st.warning(v['warning'])
                    st.divider()
                
                # Yếu tố nguy cơ
                if "risk_factors" in causes:
                    risks = causes["risk_factors"]
                    st.markdown(f"### {risks.get('name', 'Yếu tố nguy cơ')}")
                    st.caption(risks.get('description', ''))
                    for key in ["age", "chronic_diseases", "lifestyle"]:
                        if key in risks:
                            risk_item = risks[key]
                            st.markdown(f"**{risk_item.get('name', key)}**")
                            if "diseases" in risk_item:
                                for d in risk_item["diseases"][:3]:
                                    st.markdown(f"- {d}")
                            elif "factors" in risk_item:
                                for f in risk_item["factors"][:3]:
                                    st.markdown(f"- {f}")
                            elif "reason" in risk_item:
                                st.caption(risk_item["reason"])
    
    # Triệu chứng
    with st.expander("🩺 Triệu chứng viêm phổi", expanded=True):
        if hasattr(pneumonia, 'SYMPTOMS') and pneumonia.SYMPTOMS:
            symptoms_dict = pneumonia.SYMPTOMS
            
            # Triệu chứng chính
            if "main_symptoms" in symptoms_dict:
                main = symptoms_dict["main_symptoms"]
                st.subheader(f"{main.get('title', '🔍 Triệu Chứng Chính')}")
                if "symptoms" in main:
                    for symptom in main["symptoms"]:
                        if isinstance(symptom, dict):
                            st.markdown(f"### {symptom.get('icon', '')} {symptom.get('name', '')}")
                            st.caption(symptom.get('description', ''))
                            if "details" in symptom:
                                for detail in symptom["details"]:
                                    st.markdown(f"- {detail}")
                            st.divider()
            
            # Triệu chứng nặng
            if "severe_symptoms" in symptoms_dict:
                severe = symptoms_dict["severe_symptoms"]
                st.error(f"### {severe.get('title', '🚨 Triệu Chứng Nặng')}")
                st.warning(severe.get('warning', ''))
                if "symptoms" in severe:
                    for symptom in severe["symptoms"]:
                        if isinstance(symptom, dict):
                            st.markdown(f"**{symptom.get('name', '')}**")
                            if "signs" in symptom:
                                for sign in symptom["signs"]:
                                    st.markdown(f"- {sign}")
                            st.divider()
            
            # Triệu chứng ở người già
            if "elderly_symptoms" in symptoms_dict:
                elderly = symptoms_dict["elderly_symptoms"]
                st.warning(f"### {elderly.get('title', '👴 Triệu Chứng Ở Người Già')}")
                st.error(elderly.get('warning', ''))
                if "common" in elderly:
                    for item in elderly["common"]:
                        st.markdown(f"- {item}")
                if "note" in elderly:
                    st.error(elderly["note"])
    
    # Chẩn đoán
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
    
    # Điều trị
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
    
    # Phòng ngừa
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
    
    # Biến chứng
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

