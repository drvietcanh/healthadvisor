"""
Dinh dưỡng cho người Tiểu Đường
Bao gồm: Nguyên tắc ăn, Đếm carb, Chỉ số GI, Thực đơn mẫu
"""

NUTRITION_SIMPLE = {
    "basic_principles_vn": """
🍽️ NGUYÊN TẮC ĂN UỐNG CHO NGƯỜI TIỂU ĐƯỜNG:

Không phải "kiêng khem tuyệt đối" mà là "ăn THÔNG MINH":

✅ 5 NGUYÊN TẮC VÀNG:

1️⃣ ĂN ĐÚNG GIỜ, ĐỀU ĐẶN
   - 3 bữa chính + 2-3 bữa phụ
   - Không bỏ bữa
   - Khoảng cách 3-4 giờ

2️⃣ KIỂM SOÁT LƯỢNG (không ăn quá nhiều)
   - Dùng đĩa nhỏ
   - Nửa đĩa rau, 1/4 cơm, 1/4 thịt/cá

3️⃣ CHỌN CARB TỐT (tinh bột phức hợp)
   - Gạo lứt > gạo trắng
   - Bánh mì nguyên cám > bánh mì trắng
   - Khoai lang > khoai tây chiên

4️⃣ NHIỀU RAU, VỪA PHẢI TRÁI CÂY
   - Rau: Ăn thoải mái
   - Trái cây: 2-3 lần/ngày, mỗi lần 1 quả nhỏ

5️⃣ TRÁNH ĐƯỜNG, ĐỒ NGỌT
   - Không nước ngọt, trà sữa
   - Hạn chế bánh kẹo, kem
""",
    
    "carb_counting_simple": {
        "what_vn": """
🔢 ĐẾM CARB (Tinh bột) LÀ GÌ?

Carb (tinh bột, đường) làm tăng đường huyết nhất.
Biết đếm carb giúp kiểm soát đường huyết tốt hơn.

1 phần carb = 15g carb = tăng đường ~3 mmol/L
""",
        "examples_15g_carb": [
            "🍚 1/3 chén cơm (~50g cơm chín)",
            "🍞 1 lát bánh mì",
            "🍝 1/3 chén mì/phở/bún",
            "🥔 1/2 củ khoai nhỏ",
            "🍌 1/2 quả chuối",
            "🍎 1 quả táo nhỏ",
            "🥛 1 ly sữa (200ml)",
            "🍪 2 chiếc bánh quy nhỏ"
        ],
        "daily_target_vn": """
📊 MỤC TIÊU CARB MỖI NGÀY:

Phụ nữ: 9-13 phần (135-195g carb)
Nam giới: 11-15 phần (165-225g carb)

Phân bổ:
- Bữa chính: 3-5 phần
- Bữa phụ: 1-2 phần

Ví dụ bữa ăn 4 phần carb:
- 2/3 chén cơm + 1/2 quả táo + 1/2 chén rau củ
"""
    },
    
    "glycemic_index_simple": {
        "what_vn": """
📈 CHỈ SỐ ĐƯỜNG HUYẾT (GI - Glycemic Index)

GI cho biết thực phẩm làm tăng đường nhanh hay chậm:
- GI thấp (< 55): Tốt ✓ (tăng đường chậm)
- GI trung bình (56-69): Ăn vừa phải
- GI cao (≥ 70): Hạn chế ✗ (tăng đường nhanh)
""",
        "low_gi_foods": [
            "✅ GẠO LỨT, gạo nâu (GI ~50)",
            "✅ Yến mạch (GI ~55)",
            "✅ Đậu các loại (GI ~30-40)",
            "✅ Hầu hết rau (GI ~15-30)",
            "✅ Táo, lê, cam (GI ~40-50)",
            "✅ Sữa (GI ~30-40)"
        ],
        "high_gi_foods": [
            "❌ GẠO TRẮNG (GI ~73)",
            "❌ Bánh mì trắng (GI ~75)",
            "❌ Khoai tây chiên (GI ~85)",
            "❌ Ngũ cốc ngọt (GI ~80)",
            "❌ Dưa hấu (GI ~72)",
            "❌ Đường, mật (GI ~100)"
        ]
    },
    
    "glycemic_load_advanced": {
        "what_vn": """
📊 TẢI LƯỢNG ĐƯỜNG HUYẾT (GL - Glycemic Load)

🔬 KHOA HỌC DỄ HIỂU:

GL = (GI × lượng carb trong khẩu phần ăn) ÷ 100

**TẠI SAO GL QUAN TRỌNG HƠN GI?**

GI chỉ cho biết CHẤT LƯỢNG carb (tăng đường nhanh hay chậm)
GL cho biết CHẤT LƯỢNG + SỐ LƯỢNG = Ảnh hưởng THỰC TẾ lên đường huyết!

📏 PHÂN LOẠI GL:
- GL thấp (< 10): Tốt ✓
- GL trung bình (11-19): Vừa phải
- GL cao (≥ 20): Hạn chế ✗
""",
        "comparison_gi_vs_gl": """
🔍 SO SÁNH GI vs GL - VÍ DỤ THỰC TẾ:

┌─────────────────────────────────────────────────────────────┐
│ Ví dụ 1: DƯA HẤU (Bất ngờ!)                                │
├─────────────────────────────────────────────────────────────┤
│ GI:  72 (CAO ❌)  → Nghe có vẻ nguy hiểm?                  │
│ Carb: 6g/100g     → Nhưng ít carb!                          │
│ GL:  4 (THẤP ✅)  → Thực tế AN TOÀN nếu ăn vừa phải!        │
│                                                              │
│ 💡 KẾT LUẬN: Ăn 1-2 lát dưa hấu OK!                        │
│    (Vì lượng carb thực tế ít)                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Ví dụ 2: KHOAI LANG vs KHOAI TÂY                           │
├─────────────────────────────────────────────────────────────┤
│ KHOAI LANG (150g):                                          │
│  GI:  54 (Thấp ✅)                                          │
│  Carb: 27g                                                   │
│  GL:  15 (Trung bình)  → Ăn được!                          │
│                                                              │
│ KHOAI TÂY CHIÊN (150g):                                    │
│  GI:  85 (Rất cao ❌)                                       │
│  Carb: 40g                                                   │
│  GL:  34 (RẤT CAO ❌❌)  → TRÁNH!                          │
│                                                              │
│ 💡 KẾT LUẬN: Khoai lang TỐT HƠN gấp nhiều lần!            │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Ví dụ 3: GẠO TRẮNG vs GẠO LỨT (Cùng 150g cơm chín)        │
├─────────────────────────────────────────────────────────────┤
│ GẠO TRẮNG:                                                  │
│  GI:  73 (Cao ❌)                                           │
│  Carb: 45g                                                   │
│  GL:  33 (RẤT CAO ❌)  → Tăng đường NHANH & MẠNH!         │
│                                                              │
│ GẠO LỨT:                                                    │
│  GI:  50 (Thấp ✅)                                          │
│  Carb: 43g                                                   │
│  GL:  22 (Cao nhưng chấp nhận được)                        │
│       → Tăng đường CHẬM hơn, ỔN ĐỊNH hơn                   │
│                                                              │
│ 💡 KẾT LUẬN: Gạo lứt giảm GL 33%, đường ổn định hơn!      │
└─────────────────────────────────────────────────────────────┘
""",
        "real_world_examples": [
            # ========== THỰC PHẨM TINH BỘT VIỆT NAM ==========
            {
                "food": "🍚 CƠM TRẮNG GẠO TẺ (150g = 1 chén)",
                "gi": 73,
                "carb_per_serving": "45g",
                "gl": 33,
                "verdict": "❌ GL RẤT CAO - Giảm xuống 2/3 chén (GL = 22) hoặc chuyển sang gạo lứt"
            },
            {
                "food": "🍚 CƠM LỨT (150g = 1 chén)",
                "gi": 50,
                "carb_per_serving": "43g",
                "gl": 22,
                "verdict": "⚠️ GL CAO - Chấp nhận được, tốt hơn gạo trắng 33%"
            },
            {
                "food": "🍚 CƠM TẤM (150g = 1 chén)",
                "gi": 70,
                "carb_per_serving": "44g",
                "gl": 31,
                "verdict": "❌ GL RẤT CAO - Giống cơm trắng, hạn chế"
            },
            {
                "food": "🍜 PHỞ (1 tô, 200g bánh phở)",
                "gi": 70,
                "carb_per_serving": "50g",
                "gl": 35,
                "verdict": "❌ GL RẤT CAO - Giảm bánh phở 1/2, thêm nhiều rau, thịt"
            },
            {
                "food": "🍜 BÚN (1 tô, 200g)",
                "gi": 65,
                "carb_per_serving": "48g",
                "gl": 31,
                "verdict": "❌ GL RẤT CAO - Ăn ít bún, nhiều rau"
            },
            {
                "food": "🍜 MIẾN (100g khô = ~300g chín)",
                "gi": 52,
                "carb_per_serving": "45g",
                "gl": 23,
                "verdict": "⚠️ GL CAO - Tốt hơn bún/phở một chút"
            },
            {
                "food": "🍚 XÔI (150g)",
                "gi": 88,
                "carb_per_serving": "50g",
                "gl": 44,
                "verdict": "❌❌ GL CỰC CAO - TRÁNH! Tăng đường rất nhanh"
            },
            {
                "food": "🥖 BÁNH MÌ VIỆT NAM (1 ổ, ~80g)",
                "gi": 75,
                "carb_per_serving": "40g",
                "gl": 30,
                "verdict": "❌ GL RẤT CAO - Ăn 1/2 ổ, kẹp nhiều rau, trứng, thịt"
            },
            {
                "food": "🥟 BÁNH BAO (1 cái lớn)",
                "gi": 68,
                "carb_per_serving": "35g",
                "gl": 24,
                "verdict": "❌ GL CAO - Ăn 1 cái nhỏ, kết hợp rau"
            },
            
            # ========== CỦ, KHOAI VIỆT NAM ==========
            {
                "food": "🍠 KHOAI LANG LUỘC (150g)",
                "gi": 54,
                "carb_per_serving": "27g",
                "gl": 15,
                "verdict": "✅ GL TRUNG BÌNH - TỐT! Thay thế cơm tốt"
            },
            {
                "food": "🥔 KHOAI TÂY LUỘC (150g)",
                "gi": 78,
                "carb_per_serving": "27g",
                "gl": 21,
                "verdict": "⚠️ GL CAO - Kém hơn khoai lang, ăn ít"
            },
            {
                "food": "🥔 KHOAI TÂY CHIÊN (150g)",
                "gi": 85,
                "carb_per_serving": "40g",
                "gl": 34,
                "verdict": "❌❌ GL CỰC CAO - TRÁNH HOÀN TOÀN!"
            },
            {
                "food": "🥔 KHOAI MÔN LUỘC (150g)",
                "gi": 53,
                "carb_per_serving": "32g",
                "gl": 17,
                "verdict": "✅ GL TRUNG BÌNH - Tốt! Giống khoai lang"
            },
            {
                "food": "🥔 KHOAI SỌ LUỘC (150g)",
                "gi": 50,
                "carb_per_serving": "30g",
                "gl": 15,
                "verdict": "✅ GL TRUNG BÌNH - Tốt! An toàn"
            },
            
            # ========== TRÁI CÂY VIỆT NAM ==========
            {
                "food": "🍌 CHUỐI TIÊU (1 quả vừa, 120g)",
                "gi": 51,
                "carb_per_serving": "27g",
                "gl": 14,
                "verdict": "✅ GL TRUNG BÌNH - Ăn 1/2 quả tốt hơn (GL = 7)"
            },
            {
                "food": "🍌 CHUỐI XANH (1 quả, 120g)",
                "gi": 42,
                "carb_per_serving": "24g",
                "gl": 10,
                "verdict": "✅ GL THẤP - TỐT HƠN chuối chín!"
            },
            {
                "food": "🥭 XOÀI (1 quả nhỏ, 150g)",
                "gi": 51,
                "carb_per_serving": "22g",
                "gl": 11,
                "verdict": "✅ GL TRUNG BÌNH - Ăn vừa phải, 1/2 quả/lần"
            },
            {
                "food": "🍊 CAM (1 quả vừa, 150g)",
                "gi": 43,
                "carb_per_serving": "15g",
                "gl": 6,
                "verdict": "✅ GL THẤP - Tuyệt vời! Ăn 1-2 quả/ngày OK"
            },
            {
                "food": "🍊 QUÝT (1 quả vừa, 100g)",
                "gi": 47,
                "carb_per_serving": "13g",
                "gl": 6,
                "verdict": "✅ GL THẤP - Tốt! Ăn thoải mái"
            },
            {
                "food": "🍈 BƯỞI (3-4 múi, 150g)",
                "gi": 25,
                "carb_per_serving": "11g",
                "gl": 3,
                "verdict": "✅✅ GL RẤT THẤP - TUYỆT VỜI! Trái cây tốt nhất cho tiểu đường"
            },
            {
                "food": "🥭 ỔI (1/2 quả, 100g)",
                "gi": 33,
                "carb_per_serving": "9g",
                "gl": 3,
                "verdict": "✅✅ GL RẤT THẤP - Rất tốt! Giàu chất xơ"
            },
            {
                "food": "🍉 DƯA HẤU (120g = 1 lát vừa)",
                "gi": 72,
                "carb_per_serving": "7g",
                "gl": 5,
                "verdict": "✅ GL THẤP - Ăn được 1-2 lát! GI cao nhưng ít carb"
            },
            {
                "food": "🥭 DƯA GẤN/DƯA LƯỚI (150g)",
                "gi": 65,
                "carb_per_serving": "13g",
                "gl": 8,
                "verdict": "✅ GL THẤP - Ăn vừa phải OK"
            },
            {
                "food": "🍍 THƠM/DỨA (100g)",
                "gi": 66,
                "carb_per_serving": "13g",
                "gl": 9,
                "verdict": "✅ GL THẤP - Ăn ít, khoảng 2-3 lát"
            },
            {
                "food": "🍇 NHÃN (10 quả, ~100g)",
                "gi": 60,
                "carb_per_serving": "17g",
                "gl": 10,
                "verdict": "✅ GL THẤP - Ăn vừa phải, 7-10 quả"
            },
            {
                "food": "🍇 VẢI (10 quả, ~100g)",
                "gi": 57,
                "carb_per_serving": "17g",
                "gl": 10,
                "verdict": "✅ GL THẤP - Ăn vừa phải, 7-10 quả"
            },
            {
                "food": "🥭 MÍT (150g)",
                "gi": 75,
                "carb_per_serving": "38g",
                "gl": 29,
                "verdict": "❌ GL CAO - Ăn ít, 2-3 múi thôi, rất ngọt!"
            },
            {
                "food": "🥭 CHÔM CHÔM (10 quả, ~100g)",
                "gi": 59,
                "carb_per_serving": "16g",
                "gl": 9,
                "verdict": "✅ GL THẤP - Ăn vừa phải OK"
            },
            {
                "food": "🥭 MĂNG CỤT (5 quả, ~100g)",
                "gi": 62,
                "carb_per_serving": "18g",
                "gl": 11,
                "verdict": "✅ GL TRUNG BÌNH - Ăn ít, 4-5 quả"
            },
            {
                "food": "🍈 ĐU ĐỦ CHÍN (150g)",
                "gi": 60,
                "carb_per_serving": "15g",
                "gl": 9,
                "verdict": "✅ GL THẤP - Tốt! Ăn vừa phải"
            },
            {
                "food": "🍎 TÁO TÂY (1 quả vừa, 150g)",
                "gi": 36,
                "carb_per_serving": "19g",
                "gl": 7,
                "verdict": "✅ GL THẤP - Tuyệt vời! Ăn 1-2 quả/ngày"
            },
            
            # ========== ĐỒ UỐNG VIỆT NAM ==========
            {
                "food": "🥛 SỮA ĐẬU NÀNH KHÔNG ĐƯỜNG (250ml)",
                "gi": 34,
                "carb_per_serving": "6g",
                "gl": 2,
                "verdict": "✅✅ GL RẤT THẤP - Rất tốt! Uống thoải mái"
            },
            {
                "food": "🥛 SỮA ĐẬU NÀNH CÓ ĐƯỜNG (250ml)",
                "gi": 44,
                "carb_per_serving": "18g",
                "gl": 8,
                "verdict": "⚠️ GL THẤP - Tốt hơn không đường nhưng chấp nhận được"
            },
            {
                "food": "☕ CÀ PHÊ SỮA ĐÁ (1 ly)",
                "gi": 60,
                "carb_per_serving": "25g",
                "gl": 15,
                "verdict": "⚠️ GL TRUNG BÌNH - Giảm đường, dùng sữa tươi không đường"
            },
            {
                "food": "🧋 TRÀ SỮA TRÂN CHÂU (1 ly lớn)",
                "gi": 70,
                "carb_per_serving": "60g",
                "gl": 42,
                "verdict": "❌❌ GL CỰC CAO - TRÁNH! Đường + trân châu rất cao"
            },
            {
                "food": "🥤 NƯỚC MÍA (250ml)",
                "gi": 65,
                "carb_per_serving": "28g",
                "gl": 18,
                "verdict": "⚠️ GL CAO - Hạn chế, uống ít"
            },
            {
                "food": "🥤 NƯỚC DỪA TƯƠI (250ml)",
                "gi": 54,
                "carb_per_serving": "9g",
                "gl": 5,
                "verdict": "✅ GL THẤP - Tốt! Không đường tốt hơn"
            },
            
            # ========== ĐỒ ĂN VẶT VIỆT NAM ==========
            {
                "food": "🍡 CHÈ (1 chén có đường)",
                "gi": 75,
                "carb_per_serving": "45g",
                "gl": 34,
                "verdict": "❌ GL RẤT CAO - TRÁNH! Nhiều đường + tinh bột"
            },
            {
                "food": "🥜 ĐẬU PHỘNG RANG (30g = 1 nắm)",
                "gi": 14,
                "carb_per_serving": "5g",
                "gl": 1,
                "verdict": "✅✅ GL RẤT THẤP - Tuyệt vời! Ăn vặt tốt"
            },
            {
                "food": "🌰 HẠNH NHÂN (30g = 1 nắm)",
                "gi": 0,
                "carb_per_serving": "3g",
                "gl": 0,
                "verdict": "✅✅ GL RẤT THẤP - Hoàn hảo! Ăn vặt tốt nhất"
            },
            {
                "food": "🌰 ĐIỀU (30g = 1 nắm)",
                "gi": 25,
                "carb_per_serving": "9g",
                "gl": 2,
                "verdict": "✅✅ GL RẤT THẤP - Rất tốt! Nhưng đừng ăn quá nhiều (nhiều calo)"
            },
            
            # ========== RAU CỦ VIỆT NAM ==========
            {
                "food": "🥬 RAU MUỐNG, CẢI, RAU NGÓT (100g)",
                "gi": 15,
                "carb_per_serving": "2g",
                "gl": 0,
                "verdict": "✅✅ GL = 0 - ĂN TỰ DO! Càng nhiều càng tốt"
            },
            {
                "food": "🥕 CÀ RỐT (100g)",
                "gi": 39,
                "carb_per_serving": "10g",
                "gl": 4,
                "verdict": "✅ GL RẤT THẤP - Ăn thoải mái"
            },
            {
                "food": "🍅 CÀ CHUA (150g = 1 quả lớn)",
                "gi": 38,
                "carb_per_serving": "6g",
                "gl": 2,
                "verdict": "✅✅ GL RẤT THẤP - Ăn tự do"
            },
            {
                "food": "🥒 DƯA LEO (100g)",
                "gi": 15,
                "carb_per_serving": "3g",
                "gl": 0,
                "verdict": "✅✅ GL = 0 - Ăn thoải mái"
            }
        ],
        "practical_tips_vn": """
💡 MẸO ÁP DỤNG GL THỰC TẾ:

1️⃣ GIẢM KHẨU PHẦN ĂN:
   ❌ 1 chén cơm trắng (GL = 33)
   ✅ 2/3 chén cơm trắng (GL = 22)
   ✅✅ 2/3 chén cơm lứt (GL = 15) ← TỐT NHẤT!

2️⃣ KẾT HỢP THÔNG MINH:
   Thêm rau, protein, mỡ tốt → Làm CHẬM hấp thu đường!
   
   Ví dụ: Cơm + rau + cá = GL thấp hơn chỉ ăn cơm!

3️⃣ CHỌN THỰC PHẨM GL THẤP:
   - Đậu các loại (GL 3-7) ✅
   - Rau xanh (GL 0-3) ✅
   - Táo, lê, cam (GL 5-7) ✅
   - Yến mạch (GL 9) ✅
   - Gạo lứt (GL 22 cho 1 chén) ⚠️

4️⃣ TRÁNH GL CAO:
   - Gạo trắng (GL 33) ❌
   - Khoai tây chiên (GL 34) ❌
   - Bánh ngọt, bánh mì trắng (GL 20-30) ❌
   - Nước ngọt (GL 20-25) ❌

5️⃣ QUY TẮC VÀNG:
   📊 Tổng GL mỗi bữa < 40
   📊 Tổng GL mỗi ngày < 100 (lý tưởng: 60-80)
""",
        "science_explanation_vn": """
🔬 GIẢI THÍCH KHOA HỌC (Dễ hiểu):

**GI (Glycemic Index - Chỉ số Đường huyết):**
- Đo TOC ĐỘ đường huyết tăng
- Test: Ăn 50g carb từ thực phẩm
- So sánh với 50g glucose (= 100)
- ⚠️ HẠN CHẾ: Không tính số lượng thực tế ăn!

**GL (Glycemic Load - Tải lượng Đường huyết):**
- Đo TÁC ĐỘNG THỰC TẾ lên đường huyết
- Tính cả CHẤT LƯỢNG (GI) và SỐ LƯỢNG (carb)
- ✅ ƯU ĐIỂM: Phản ánh chính xác khẩu phần ăn thực tế!

**Công thức:**
GL = (GI × g carb trong khẩu phần) ÷ 100

**Ví dụ minh họa:**
Dưa hấu 120g có:
- GI = 72 (cao!)
- Carb = 7g (ít!)
- GL = (72 × 7) ÷ 100 = 5 (thấp → OK!)

**Tại sao GL quan trọng với bệnh tiểu đường?**

1. Dự đoán chính xác đường huyết sau ăn
2. Giúp tính liều insulin chính xác hơn
3. Kiểm soát đường tốt hơn (HbA1c thấp hơn)
4. Giảm biến chứng tim mạch
5. Thực tế, áp dụng dễ hơn GI!
"""
    },
    
    "meal_plate_method_vn": """
🍽️ PHƯƠNG PHÁP ĐĨA ĂN (Đơn giản nhất!):

Chia đĩa thành 4 phần:

🥗 1/2 ĐĨA = RAU (không tinh bột)
   Rau xanh, cà chua, dưa chuột, bông cải, đậu que...
   
🍚 1/4 ĐĨA = TINH BỘT
   Cơm (nâu/lứt), bánh mì nguyên cám, khoai lang...
   
🍗 1/4 ĐĨA = PROTEIN
   Thịt nạc, cá, gà (không da), trứng, đậu hủ...

➕ Thêm:
🥛 1 ly sữa không đường/ít béo
🍎 1 quả trái cây nhỏ
""",
    
    "foods_to_eat_vn": {
        "carbs_good": {
            "title": "🍚 TINH BỘT TỐT:",
            "foods": [
                "Gạo lứt, gạo nâu, gạo mầm",
                "Yến mạch",
                "Bánh mì nguyên cám",
                "Khoai lang (luộc, hấp)",
                "Bột mì nguyên cám",
                "Đậu các loại (đậu đen, đậu đỏ, đậu xanh)"
            ]
        },
        "protein": {
            "title": "🍗 ĐẠM:",
            "foods": [
                "Cá (cá hồi, cá thu, cá ngừ) - TỐT NHẤT",
                "Ức gà, ức vịt (không da)",
                "Thịt nạc (bò, heo nạc)",
                "Trứng (1-2 quả/ngày)",
                "Đậu hủ, đậu phụ",
                "Sữa ít béo, sữa chua không đường",
                "Các loại hạt (hạnh nhân, óc chó, điều)"
            ]
        },
        "vegetables": {
            "title": "🥬 RAU (ĂN TỰ DO):",
            "foods": [
                "Rau xanh lá (cải, rau ngót, rau muống)",
                "Bông cải xanh, bông cải trắng",
                "Cà chua",
                "Dưa chuột",
                "Ớt chuông",
                "Đậu que, đậu cove",
                "Nấm các loại",
                "Cà rốt, củ cải"
            ]
        },
        "fruits": {
            "title": "🍎 TRÁI CÂY (VỪA PHẢI):",
            "foods": [
                "Táo, lê (1 quả/lần)",
                "Cam, quýt (1 quả/lần)",
                "Dâu tây (1 chén)",
                "Ổi (1/2 quả)",
                "Chuối xanh (1/2 quả)",
                "Bưởi (2-3 múi)"
            ],
            "note": "Ăn trái cây NGUYÊN QUẢ, không ép nước (mất chất xơ)"
        },
        "fats": {
            "title": "🥑 MỠ TỐT:",
            "foods": [
                "Dầu ô liu",
                "Dầu hạt lanh",
                "Bơ (1/4 quả)",
                "Hạt óc chó, hạnh nhân, điều (1 nắm)",
                "Cá béo (omega-3)"
            ]
        }
    },
    
    "foods_to_avoid_vn": [
        "🚫 ĐƯỜNG, KẸO, CHOCOLATE",
        "🚫 NƯỚC NGỌT có ga, nước trái cây đóng chai",
        "🚫 TRÀ SỮA, cà phê đường",
        "🚫 BÁNH NGỌT, bánh kem, bánh quy ngọt",
        "🚫 KEM ốc quế",
        "🚫 MẬT ONG, xi-rô (dù tự nhiên vẫn là đường!)",
        "🚫 MỨT, JAM",
        "🚫 ĐỒ CHIÊN RÁN (gà rán, khoai chiên, nem rán...)",
        "🚫 ĐỒ ĐÓNG HỘP, đồ ăn nhanh",
        "🚫 THỊT GÀ RÁN, thịt chế biến sẵn",
        "🚫 RƯỢU, BIA (nếu uống: rất ít, cùng bữa ăn)"
    ],
    
    "meal_examples_vn": {
        "breakfast": [
            "🥣 Cháo yến mạch + 1/2 chuối + sữa tươi không đường + 1 nắm hạt",
            "🍳 Bánh mì nguyên cám + trứng luộc + cà chua + bơ",
            "🥛 Sữa chua không đường + yến mạch + trái cây + hạt chia"
        ],
        "lunch": [
            "🍚 Cơm gạo lứt (2/3 chén) + cá hấp + rau luộc + canh rau",
            "🍚 Cơm nâu + ức gà nướng + đậu hũ + rau xào + cam",
            "🥗 Salad gà + bánh mì nguyên cám + sữa"
        ],
        "dinner": [
            "🍚 Cơm lứt (1/2 chén) + cá kho + rau luộc + canh",
            "🍜 Phở gà (ít bún) + nhiều rau + thịt gà + táo",
            "🥗 Salad + thịt bò xào + khoai lang luộc"
        ],
        "snacks": [
            "🍎 1 quả táo + 10 hạt hạnh nhân",
            "🥛 1 ly sữa không đường",
            "🥕 Rau củ sống + sốt sữa chua",
            "🥚 1 quả trứng luộc"
        ]
    }
}

