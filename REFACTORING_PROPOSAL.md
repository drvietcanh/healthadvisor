# ĐỀ XUẤT TÁCH MODULE - CÁC FILE > 300 DÒNG

## 📊 TÓM TẮT

Tổng số file cần xem xét: **14 files**
- Files > 350 dòng: 6 files (ưu tiên cao)
- Files 300-350 dòng: 8 files (ưu tiên vừa)

---

## 🔴 ƯU TIÊN CAO (> 350 dòng)

### 1. `pages/0_📖_Hướng_Dẫn.py` (381 dòng)

**Cấu trúc hiện tại:**
- 4 tabs: Bắt đầu nhanh, Hướng dẫn chi tiết, FAQ, Mẹo & Thủ thuật
- Mỗi tab có nhiều markdown content

**Đề xuất tách:**
```
pages/
  └── guide_components/
      ├── __init__.py
      ├── quick_start_tab.py      # Tab 1: Bắt đầu nhanh (~90 dòng)
      ├── detailed_guide_tab.py   # Tab 2: Hướng dẫn chi tiết (~150 dòng)
      ├── faq_tab.py              # Tab 3: FAQ (~70 dòng)
      └── tips_tab.py             # Tab 4: Mẹo & Thủ thuật (~80 dòng)
```

**Lợi ích:**
- Mỗi tab độc lập, dễ bảo trì
- Có thể tái sử dụng components

---

### 2. `export_reports/pdf_generator.py` (373 dòng)

**Cấu trúc hiện tại:**
- 2 functions chính: `generate_health_report_html()` và `generate_medication_report_html()`
- Nhiều HTML/CSS inline

**Đề xuất tách:**
```
export_reports/
  ├── pdf_generator.py           # Main file (tổng hợp) (~30 dòng)
  ├── health_report.py           # Health report HTML (~180 dòng)
  ├── medication_report.py       # Medication report HTML (~140 dòng)
  └── html_templates.py          # HTML templates chung (~50 dòng)
```

**Lợi ích:**
- Tách logic theo chức năng
- Dễ thêm loại báo cáo mới

---

### 3. `diseases/respiratory/copd/assessment.py` (369 dòng)

**Cấu trúc hiện tại:**
- 4 dictionaries lớn: MMRC_SCALE, CAT_QUESTIONNAIRE, GOLD_CLASSIFICATION, SIX_MINUTE_WALK_TEST
- 2 functions: calculate_cat_score(), get_mmrc_grade()

**Đề xuất tách:**
```
diseases/respiratory/copd/assessment/
  ├── __init__.py                # Export all (~30 dòng)
  ├── mmrc_scale.py              # MMRC scale (~100 dòng)
  ├── cat_questionnaire.py      # CAT questionnaire (~110 dòng)
  ├── gold_classification.py     # GOLD classification (~95 dòng)
  ├── walk_test.py               # 6-minute walk test (~35 dòng)
  └── calculators.py             # calculate_cat_score, get_mmrc_grade (~30 dòng)
```

**Lợi ích:**
- Mỗi assessment tool độc lập
- Dễ test và mở rộng

---

### 4. `diseases/metabolic/dyslipidemia/medications.py` (357 dòng)

**Cấu trúc hiện tại:**
- 3 nhóm thuốc lớn: STATINS, FIBRATES, OTHER_MEDICATIONS
- TREATMENT_PROTOCOLS
- 3 functions: get_medication_info(), get_side_effects(), get_treatment_recommendation()

**Đề xuất tách:**
```
diseases/metabolic/dyslipidemia/medications/
  ├── __init__.py                # Export all (~25 dòng)
  ├── statins.py                 # STATINS (~120 dòng)
  ├── fibrates.py                # FIBRATES (~60 dòng)
  ├── other_medications.py       # OTHER_MEDICATIONS (~80 dòng)
  ├── treatment_protocols.py     # TREATMENT_PROTOCOLS (~55 dòng)
  └── medication_functions.py    # Functions (~40 dòng)
```

**Lợi ích:**
- Tách theo nhóm thuốc, dễ tìm kiếm
- Có thể thêm nhóm thuốc mới

---

### 5. `core/light_mode_css.py` (347 dòng) và `core/dark_mode_css.py` (334 dòng)

**Cấu trúc hiện tại:**
- CSS strings rất dài

**Đề xuất:**
- **GIỮ NGUYÊN** - CSS thường dài, tách ra sẽ khó đọc
- Nếu cần, có thể tách theo section:
  ```
  core/css/
    ├── __init__.py
    ├── base_styles.py      # Common styles
    ├── headers.py         # Header styles
    ├── cards.py           # Card styles
    └── light_mode_css.py  # Light mode specific
  ```
- **Khuyến nghị: GIỮ NGUYÊN** vì CSS thường dài và khó tách logic

---

### 6. `diary_components/instructions.py` (347 dòng)

**Cấu trúc hiện tại:**
- Nhiều functions render instructions khác nhau

**Đề xuất tách:**
```
diary_components/instructions/
  ├── __init__.py                # Export all (~15 dòng)
  ├── overview.py                # render_instructions() (~40 dòng)
  ├── bp_guide.py                # render_bp_guide() (~150 dòng)
  ├── bs_guide.py                # render_bs_guide() (~80 dòng)
  └── weight_guide.py            # render_weight_guide() (~70 dòng)
```

**Lợi ích:**
- Mỗi guide độc lập
- Dễ cập nhật từng phần

---

## 🟡 ƯU TIÊN VỪA (300-350 dòng)

### 7. `diseases/respiratory/copd/exercises.py` (346 dòng)

**Cấu trúc hiện tại:**
- Nhiều dictionaries: EXERCISE_BENEFITS, EXERCISE_PRINCIPLES, BREATHING_TECHNIQUES, AEROBIC_EXERCISES, STRENGTH_EXERCISES, FLEXIBILITY_EXERCISES, DAILY_ACTIVITIES, FOUR_WEEK_PROGRAM

**Đề xuất tách:**
```
diseases/respiratory/copd/exercises/
  ├── __init__.py                # Export all (~30 dòng)
  ├── benefits.py                 # EXERCISE_BENEFITS (~40 dòng)
  ├── principles.py               # EXERCISE_PRINCIPLES (~50 dòng)
  ├── breathing.py                # BREATHING_TECHNIQUES (~80 dòng)
  ├── aerobic.py                  # AEROBIC_EXERCISES (~60 dòng)
  ├── strength.py                 # STRENGTH_EXERCISES (~50 dòng)
  └── programs.py                 # Flexibility, Daily, 4-week (~60 dòng)
```

---

### 8. `health_trends/analyzer.py` (342 dòng)

**Cấu trúc hiện tại:**
- Nhiều functions phân tích: calculate_trend(), analyze_blood_pressure_trend(), analyze_blood_sugar_trend(), analyze_weight_trend(), get_overall_health_score(), check_bp_alerts(), check_bs_alerts(), check_weight_alerts(), generate_recommendations()

**Đề xuất tách:**
```
health_trends/
  ├── analyzer.py                 # Main file (tổng hợp) (~30 dòng)
  ├── trend_calculator.py         # calculate_trend() (~50 dòng)
  ├── bp_analyzer.py              # BP analysis functions (~90 dòng)
  ├── bs_analyzer.py              # BS analysis functions (~80 dòng)
  ├── weight_analyzer.py          # Weight analysis (~70 dòng)
  └── recommendations.py          # generate_recommendations() (~50 dòng)
```

---

### 9. `pages/9_📈_Xu_Hướng.py` (339 dòng)

**Cấu trúc hiện tại:**
- Page với nhiều sections, charts, alerts

**Đề xuất:**
- **GIỮ NGUYÊN** - Page files thường dài do UI
- Hoặc tách thành components:
  ```
  pages/trends_components/
    ├── overview_section.py
    ├── alerts_section.py
    ├── charts_section.py
    └── recommendations_section.py
  ```
- **Khuyến nghị: GIỮ NGUYÊN** vì page files thường dài do UI code

---

### 10. `diseases/cardiovascular/heart_failure/management.py` (336 dòng)

**Cấu trúc hiện tại:**
- NUTRITION_SIMPLE, EXERCISE_SIMPLE, HOME_MONITORING, DAILY_LIVING_TIPS

**Đề xuất tách:**
```
diseases/cardiovascular/heart_failure/management/
  ├── __init__.py                 # Export all (~20 dòng)
  ├── nutrition.py                # NUTRITION_SIMPLE (~140 dòng)
  ├── exercise.py                 # EXERCISE_SIMPLE (~80 dòng)
  ├── home_monitoring.py          # HOME_MONITORING (~60 dòng)
  └── daily_living.py             # DAILY_LIVING_TIPS (~60 dòng)
```

---

### 11. `diseases/metabolic/dyslipidemia/nutrition/vietnamese_foods.py` (334 dòng)

**Cấu trúc hiện tại:**
- GOOD_FOODS, BAD_FOODS, FOOD_TIPS

**Đề xuất tách:**
```
diseases/metabolic/dyslipidemia/nutrition/
  ├── vietnamese_foods.py         # Main (tổng hợp) (~30 dòng)
  ├── good_foods.py               # GOOD_FOODS (~150 dòng)
  ├── bad_foods.py                # BAD_FOODS (~100 dòng)
  └── food_tips.py                # FOOD_TIPS (~60 dòng)
```

---

### 12. `diseases/metabolic/diabetes/nutrition/vietnamese_foods_gl.py` (333 dòng)

**Cấu trúc hiện tại:**
- Một list lớn VIETNAMESE_FOODS_GL

**Đề xuất:**
- **GIỮ NGUYÊN** - Data file, tách ra sẽ khó quản lý
- Hoặc tách theo nhóm:
  ```
  diseases/metabolic/diabetes/nutrition/vietnamese_foods/
    ├── __init__.py
    ├── grains.py          # Cơm, phở, bún...
    ├── fruits.py          # Trái cây
    ├── vegetables.py      # Rau củ
    └── proteins.py        # Thịt, cá, trứng
  ```
- **Khuyến nghị: GIỮ NGUYÊN** nếu < 400 dòng, vì data files dễ quản lý khi gom lại

---

### 13. `pages/6_🎓_Học_Dễ.py` (300 dòng - đúng giới hạn)

**Khuyến nghị: GIỮ NGUYÊN** - Đúng 300 dòng, không cần tách

---

## 📋 KẾ HOẠCH THỰC HIỆN

### Phase 1: Ưu tiên cao (Files > 350 dòng)
1. ✅ `copd/assessment.py` - Tách thành assessment/ module
2. ✅ `dyslipidemia/medications.py` - Tách thành medications/ module
3. ✅ `diary_components/instructions.py` - Tách thành instructions/ module
4. ✅ `pages/0_📖_Hướng_Dẫn.py` - Tách thành guide_components/
5. ✅ `export_reports/pdf_generator.py` - Tách thành modules

### Phase 2: Ưu tiên vừa (300-350 dòng)
6. `copd/exercises.py` - Tách thành exercises/ module
7. `health_trends/analyzer.py` - Tách thành modules
8. `heart_failure/management.py` - Tách thành management/ module
9. `dyslipidemia/nutrition/vietnamese_foods.py` - Tách theo nhóm

### Phase 3: Giữ nguyên (CSS, Data files)
- `light_mode_css.py`, `dark_mode_css.py` - **GIỮ NGUYÊN**
- `vietnamese_foods_gl.py` - **GIỮ NGUYÊN**
- `pages/9_📈_Xu_Hướng.py` - **GIỮ NGUYÊN**
- `pages/6_🎓_Học_Dễ.py` - **GIỮ NGUYÊN**

---

## ✅ NGUYÊN TẮC TÁCH MODULE

1. **Mỗi file ≤ 300 dòng** (lý tưởng 200-250)
2. **Tách theo logic/chức năng** (KHÔNG tách theo số dòng đều nhau)
3. **Test ngay sau mỗi bước**
4. **Giữ backward compatibility** (file gốc import từ modules mới)
5. **Commit rõ ràng** sau mỗi file hoàn thành

---

## 📝 LƯU Ý

- **CSS files**: Thường dài, nên GIỮ NGUYÊN nếu < 400 dòng
- **Data files** (lists, dicts lớn): Có thể GIỮ NGUYÊN nếu < 400 dòng
- **Page files**: Thường dài do UI, nên GIỮ NGUYÊN nếu < 350 dòng
- **Logic files**: Nên TÁCH nếu > 300 dòng

