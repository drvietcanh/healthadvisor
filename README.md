# StrokeAdvisor — Streamlit app for early stroke risk triage & patient counseling (Vietnam-first)

> **Purpose**: Provide a patient-facing, VN-first Streamlit app that uses **rule‑based medical logic plus an LLM assistant** to help **recognize warning signs**, **triage urgency**, and **educate** on **prevention and next steps** for **common stroke phenotypes** (ischemic LVO/non‑LVO, hemorrhagic, posterior circulation, TIA), aligned to **AHA/ASA 2024–2025** and **Bộ Y tế Việt Nam 2024** guidance.  
> **Audience**: patients & caregivers (default), clinicians (optional “pro mode”).  
> **Safety**: **Not a diagnostic tool** and **not a substitute for clinical care**. When high‑risk symptoms are flagged, the app **immediately instructs to call 115/EMS** and provides **nearest stroke‑ready hospitals** (optional add‑on).

---

## 0) Quick start

```bash
# Python 3.10–3.12 recommended
pip install streamlit pydantic python-dateutil httpx tiktoken openai==1.*  # or your LLM SDK
# Optional (map/hospital lookup):
pip install pandas geopy folium

# Run
streamlit run app.py
```

Folder layout
```
strokeadvisor/
  app.py
  pages/
    1_🧭_Triage.py
    2_🧮_Risk_Calculators.py
    3_📚_Education.py
    4_🩺_Clinician_Mode.py
  core/
    rules.py
    scoring.py
    prompts.py
    models.py
    utils.py
  data/
    hospitals_vn.csv           # optional add-on: stroke-ready facilities
  README.md
```

---

## 1) Scope & design principles

- **Patient-first, Vietnamese language by default**, English toggle.
- **Deterministic first, generative second**: critical decisions (e.g., *go to ER now*) are **rules‑based**. LLM is used for **plain‑language explanations**, **education**, and **follow‑up Q&A**.
- **Explainable**: every recommendation shows **which rule/scale** fired (BE‑FAST, posterior signs, RACE, ABCD², NIHSS summary in pro mode, etc.).
- **Time‑critical**: collect **Last Known Well (LKW)** early; surface **thrombolysis/thrombectomy windows** in plain VN.
- **Privacy‑lite**: no PHI storage by default; all inputs ephemeral in session state.
- **Offline‑friendly**: core logic has **no network dependency**; LLM is optional.

---

## 2) Clinical logic included (rule‑based)

### 2.1 Community recognition / urgent triage
- **BE‑FAST** (*Balance, Eyes, Face, Arm, Speech, Time*) with posterior signs emphasis (vertigo, ataxia, diplopia, dysarthria, dysphagia).  
- **Red flags that force “Call 115”:**
  - Any positive **BE‑FAST** or **posterior red flags** with **acute onset** (minutes–hours) and **LKW ≤ 24h**.
  - **Severe headache “thunderclap”** + **nausea/vomiting** → suspect **hemorrhage**.
  - **New focal deficits** (weakness, aphasia, unilateral neglect, visual loss), especially **maximal at onset**.
  - **Anticoagulant use** or **head trauma** with neuro deficits.
  - **Decreased consciousness**.
- **Transport logic** (optional): If prehospital **LVO suspicion**, prefer **thrombectomy‑capable center** when delays reasonable.

### 2.2 Prehospital LVO suspicion (EMS/Pro mode)
- **RACE** scale (0–9) — *suspect LVO if ≥5* → prioritize EVT‑capable center; show caveats & local validation status.
- (Optional utilities) **LAMS, FAST‑ED, G‑FAST** as alternatives for comparison.

### 2.3 TIA short‑term risk
- **ABCD²** (Age, BP, Clinical features, Duration, Diabetes) → **high risk if ≥4** → urgent ED evaluation within **24h** (often same‑day).

### 2.4 Stroke severity snapshot (Clinician Mode)
- **NIHSS** checklist (education/simulation only). Display total and itemization; warn **training is required** and this is **not for certification**.

### 2.5 Prevention messaging
- **Primary prevention** (BP, lipids, DM, smoking, sleep, weight, activity, diet) with structured checklists and lifestyle goals.
- (Optional) Link to validated **risk tools** (e.g., Stroke Riskometer) for long‑term prevention education (not for acute triage).

> **Important**: All scales are **decision aids**, not definitive diagnoses. Always defer to **local protocols** and **Bộ Y tế 2024** guidance.

---

## 3) Evidence & guideline anchors (for copywriters & reviewers)

- **Bộ Y tế Việt Nam (11/2024) – Hướng dẫn chẩn đoán và điều trị đột quỵ não**: windows, NIHSS interpretation notes, pathways.  
- **AHA/ASA 2024**: primary prevention guideline; lifestyle & risk‑factor control.  
- **BE‑FAST vs FAST**: posterior circulation sensitivity considerations.  
- **RACE**: validated prehospital LVO screen; 2024–2025 studies (incl. VN population) suggest good accuracy for LVO identification; use with local protocols.  
- **ABCD² for TIA**: identifies higher early stroke risk; thresholds for urgent workup.  
- **NIHSS**: standardized severity scale; training resources.

> See “References” for links you can open in Cursor.

---

## 4) App flows & UX

### 4.1 Home (“Tư vấn nhanh”)
1. **Language** switch (VN/EN).  
2. **Two big buttons**: *Tự đánh giá nhanh* (patient) vs *Chế độ chuyên môn* (clinician).  
3. **If acute symptoms** detected → full‑width **red banner**: *Gọi 115 ngay – Nghi ngờ đột quỵ*. Show **LKW recorder** and **do‑not‑do list** (không tự lái xe, không ăn uống, mang theo danh sách thuốc…).
4. One‑click **map to nearest stroke‑ready hospital** (optional local CSV geocoded).

### 4.2 Patient path — “Tự đánh giá nhanh”
- Short wizard: **onset time**, **BE‑FAST items**, **posterior signs**, **headache profile**, **anticoagulants/trauma**, **pregnancy/puerperium**.
- Clear **triage card**:
  - **RED**: *GỌI 115 NGAY* + why (e.g., BE‑FAST Face+, LKW 2h).
  - **AMBER**: *Khám cấp cứu trong 24 giờ* (e.g., suspected TIA).
  - **GREEN**: *Không gợi ý đột quỵ cấp* → education & return precautions.  
- Each card shows **rules fired** + **what happens next** at hospital (CT/CTA, tPA/tenecteplase windows, EVT window, BP targets).

### 4.3 Risk calculators page
- **ABCD²** form with auto‑sum & interpretation → *ED within 24h if ≥4*.
- (Optional) **Primary prevention** mini‑checklist + links to longer prevention content.

### 4.4 Education page (LLM‑assisted)
- Structured articles with **“Ask AI”** box beneath each section.  
- Topics: *Dấu hiệu nhận biết*, *Vì sao phải đến viện sớm*, *Tái phát & phòng ngừa*, *Thuốc thường gặp*, *Phục hồi chức năng sớm*, *Đột quỵ và rung nhĩ*, *Đột quỵ sau sinh*…  
- Guardrails: **no medication changes**; **no dosing advice**; always include **seek‑care fallback**.

### 4.5 Clinician Mode (locked behind disclaimer)
- **RACE** calculator, **NIHSS** teaching checklist, **copy‑to‑clipboard** handover note (LKW, deficits, vitals, glucose, anticoagulants).  
- Optionally compare **RACE vs G‑FAST/LAMS**.

---

## 5) Implementation details

### 5.1 Data models (Pydantic)
```python
class AcuteInput(BaseModel):
    lkw_minutes: int | None
    befast_face: bool
    befast_arm: bool
    befast_speech: bool
    befast_balance: bool
    befast_eyes: bool
    posterior_signs: list[str]  # vertigo, ataxia, diplopia, dysphagia
    thunderclap_headache: bool
    anticoagulant_use: bool
    head_trauma: bool
    pregnant_or_postpartum: bool
```

### 5.2 Core rules (pseudo‑logic)
```python
def triage(input: AcuteInput) -> TriageResult:
    if any([input.befast_face, input.befast_arm, input.befast_speech,
            input.befast_balance, input.befast_eyes]) and (input.lkw_minutes is not None and input.lkw_minutes <= 24*60):
        return RED_115("BE‑FAST positive with recent onset")
    if input.thunderclap_headache or input.head_trauma or input.anticoagulant_use:
        return RED_115("Hemorrhage risk / head trauma / anticoagulant")
    if "TIA_like" in input.posterior_signs:  # e.g., transient neuro deficits now resolved
        # compute ABCD2 separately
        ...
    return GREEN_EDU("No acute high‑risk pattern detected; give return precautions")
```

### 5.3 Scores
- **RACE** (Clinician Mode): compute 0–9 from face/arm/leg/ gaze/aphasia/agnosia; flag **≥5** as LVO‑suspect (show limitations & local validation notes).
- **ABCD²**: auto‑sum 0–7; **≥4 high risk** → ED in ≤24h.

### 5.4 LLM prompts (safety‑first)
- **System prompt** pins: *You are a cautious medical educator; you never diagnose; you direct emergency care when rules indicate; you cite guidelines; you avoid doses.*
- **Few‑shot** examples turning rules into **plain‑VN patient advice**.
- **Tools disabled** for anything that could be misconstrued as medical orders.

### 5.5 UI tips
- Use **`st.form`** for inputs; **`st.session_state`** for persistence.
- Big **color‑coded `st.alert`** cards for triage outcomes.
- For hospitals map: `folium` + `geopy` to compute nearest facilities (optional).

### 5.6 Testing
- Unit tests for **rules** (pytest).
- Golden tests for **LLM prompts** (snapshot prompts & responses).
- Manual UAT scripts with **simulated cases** (anterior vs posterior; TIA; mimics).

---

## 6) Minimal runnable `app.py` (skeleton)

```python
import streamlit as st
from core.rules import triage
from core.scoring import abcd2_score, race_score

st.set_page_config(page_title="StrokeAdvisor", page_icon="🧠", layout="centered")

st.title("🧠 StrokeAdvisor — Tư vấn nhận biết & xử trí sớm nghi ngờ đột quỵ")
st.caption("Không thay thế bác sĩ. Nếu có dấu hiệu cấp, hãy gọi 115.")

with st.form("quick"):
    lkw_hours = st.number_input("Thời điểm bình thường cuối cùng (giờ trước)", min_value=0, max_value=72, value=2)
    be = st.checkbox("Mất thăng bằng (Balance)")
    eyes = st.checkbox("Rối loạn nhìn (Eyes)")
    face = st.checkbox("Xệ mép / méo miệng (Face)")
    arm = st.checkbox("Yếu tay/chân (Arm/Leg)")
    speech = st.checkbox("Nói khó/loạn ngôn (Speech)")
    thunder = st.checkbox("Nhức đầu dữ dội đột ngột")
    ac = st.checkbox("Đang dùng thuốc chống đông")
    trauma = st.checkbox("Vừa chấn thương đầu")
    submitted = st.form_submit_button("Đánh giá nhanh")

if submitted:
    # Call your core triage
    result = triage(...)
    st.success(result.message)  # or st.error / st.warning per outcome
```

> See `core/rules.py` for full implementation. Add `pages/` for calculators, education, and clinician mode.

---

## 7) Safety, ethics, and regulatory notes

- The app **does not** display medication **doses** or **treatment orders**.
- Always show a **prominent emergency banner** when rules indicate *RED*.
- Display **sources** and **last updated** dates; schedule **regular content reviews**.
- If adding imaging‑AI integrations (e.g., from PACS), ensure **appropriate licensing** & **regulatory clearance**; this README intentionally **avoids** imaging automation.

---

## 8) References (openable links)

- **Bộ Y tế Việt Nam (11/2024). Hướng dẫn chẩn đoán và điều trị đột quỵ não**  
  - https://thuvienphapluat.vn/van-ban/The-thao-Y-te/Quyet-dinh-3312-QD-BYT-2024-tai-lieu-chuyen-mon-Huong-dan-chan-doan-dieu-tri-dot-quy-nao-651734.aspx  
  - PDF mirror: https://trungtamthuoc.com/pdf/huong-dan-chan-doan-va-dieu-tri-dot-quy-nao-bo-y-te-05-11-2024-trungtamthuoc.pdf

- **AHA/ASA 2024. Guideline for the Primary Prevention of Stroke**  
  - https://www.ahajournals.org/doi/10.1161/STR.0000000000000475 (overview https://professional.heart.org/en/science-news/2024-guideline-for-the-primary-prevention-of-stroke)

- **BE‑FAST evidence & posterior signs**  
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC11477353/  
  - FAST vs BE‑FAST retention: https://www.ahajournals.org/doi/10.1161/JAHA.123.035696

- **RACE (prehospital LVO)**  
  - Original/overview: https://www.ahajournals.org/doi/10.1161/strokeaha.113.003071  
  - Revalidation: https://pubmed.ncbi.nlm.nih.gov/30580284/  
  - 2024–2025 data incl. Việt Nam: https://karger.com/cee/article/doi/10.1159/000543260/918582/Predictive-value-of-the-prehospital-RACE-scale-for

- **ABCD² (TIA)**  
  - https://www.mdcalc.com/calc/357/abcd2-score-tia  
  - AHA scientific statement 2023: https://www.ahajournals.org/doi/10.1161/STR.0000000000000418

- **NIHSS (education/training PDFs)**  
  - NINDS Feb 2024: https://www.ninds.nih.gov/sites/default/files/documents/NIH-Stroke-Scale_updatedFeb2024_508.pdf

- **Industry imaging AI (context, **not** embedded)**  
  - Viz.ai platform & clearances: https://www.viz.ai/news ; LVO: https://www.viz.ai/large-vessel-occlusion  
  - RapidAI overview: https://www.rapidai.com/neurovascular/ischemic-stroke ; NCBI brief: https://www.ncbi.nlm.nih.gov/books/NBK611329/

- **Stroke Riskometer (prevention education)**  
  - https://nisan.aut.ac.nz/stroke-riskometer/clinical-trials  
  - Validation background: https://pmc.ncbi.nlm.nih.gov/articles/PMC4335600/

---

## 9) Roadmap (next waves)

- **Wave 1**: core triage rules, ABCD², education library, VN/EN toggle.  
- **Wave 2**: RACE (pro mode), hospital locator, printable handover.  
- **Wave 3**: personalization (risk factors, AF screening prompts), offline bundles.  
- **Wave 4**: audit logs (anonymous), analytics, content CMS.  
- **Wave 5**: device integrations (BP cuff) & telehealth handoff (if permitted).

---

## 10) Attribution & disclaimer

This tool is for **education and early recognition** only. It **does not diagnose** or replace emergency medical care. In **any** doubt, **call 115 / go to the nearest emergency department.**

(c) 2025 StrokeAdvisor contributors. Licensed under MIT (app code) and CC BY‑NC 4.0 (text content), unless guideline excerpts impose stricter terms.
