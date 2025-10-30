"""
Module tư vấn về Bệnh Tiểu Đường - Ngôn ngữ dễ hiểu
"""

# ============= TIỂU ĐƯỜNG LÀ GÌ? =============

DISEASE_INFO = {
    "name_vn": "Bệnh Tiểu Đường",
    "name_en": "Diabetes Mellitus",
    "simple_explanation_vn": """
🍬 TIỂU ĐƯỜNG LÀ GÌ?

Tiểu đường là bệnh đường huyết (đường trong máu) cao hơn bình thường.

Tưởng tượng đơn giản:
- Bạn ăn cơm, bánh → thành đường trong máu
- Đường cần vào tế bào để làm năng lượng
- Insulin (do tụy tiết ra) giống như "chìa khóa" mở cửa cho đường vào tế bào
- Tiểu đường = Không đủ chìa khóa HOẶC chìa khóa không vặn được
→ Đường tích trong máu, không vào tế bào được
""",
    "types_simple_vn": {
        "type1": {
            "name": "Típ 1 (Type 1)",
            "explanation": "Tụy không sản xuất được insulin (không có chìa khóa)",
            "who": "Thường gặp ở trẻ em, thanh thiếu niên",
            "treatment": "Phải tiêm insulin suốt đời"
        },
        "type2": {
            "name": "Típ 2 (Type 2)",
            "explanation": "Tụy vẫn tiết insulin nhưng cơ thể kháng insulin (chìa khóa không vặn)",
            "who": "Thường gặp ở người trên 40 tuổi, béo phì",
            "treatment": "Thay đổi lối sống + thuốc uống (có thể cần insulin sau này)"
        },
        "gestational": {
            "name": "Tiểu đường thai kỳ",
            "explanation": "Đường huyết cao trong khi mang thai",
            "who": "Phụ nữ mang thai",
            "treatment": "Thường khỏi sau sinh, nhưng tăng nguy cơ típ 2 sau này"
        }
    }
}

# ============= CHỈ SỐ ĐƯỜNG HUYẾT =============

BLOOD_SUGAR_LEVELS = {
    "units_note_vn": """
📊 ĐƠN VỊ ĐO ĐƯỜNG HUYẾT:

Có 2 đơn vị phổ biến:
- mmol/L (millimol/lít) - Việt Nam, Châu Âu dùng
- mg/dL (milligram/decilít) - Mỹ dùng

🔄 QUY ĐỔI:
- mmol/L x 18 = mg/dL
- mg/dL ÷ 18 = mmol/L

Ví dụ: 
- 5.6 mmol/L = 100 mg/dL
- 180 mg/dL = 10 mmol/L
""",
    
    "normal_ranges": {
        "fasting": {
            "name_vn": "Đường huyết LÚC ĐÓI (không ăn 8 tiếng)",
            "normal": {
                "mmol": "< 5.6 mmol/L",
                "mg": "< 100 mg/dL",
                "status": "✅ BÌNH THƯỜNG"
            },
            "prediabetes": {
                "mmol": "5.6 - 6.9 mmol/L",
                "mg": "100 - 125 mg/dL",
                "status": "⚠️ TIỀN TIỂU ĐƯỜNG (nguy cơ cao)"
            },
            "diabetes": {
                "mmol": "≥ 7.0 mmol/L",
                "mg": "≥ 126 mg/dL",
                "status": "🔴 TIỂU ĐƯỜNG (nếu đo 2 lần)"
            }
        },
        "random": {
            "name_vn": "Đường huyết BẤT KỲ (không cần đói)",
            "normal": {
                "mmol": "< 7.8 mmol/L",
                "mg": "< 140 mg/dL",
                "status": "✅ BÌNH THƯỜNG"
            },
            "diabetes": {
                "mmol": "≥ 11.1 mmol/L",
                "mg": "≥ 200 mg/dL",
                "status": "🔴 TIỂU ĐƯỜNG (nếu có triệu chứng)"
            }
        },
        "after_meal": {
            "name_vn": "Đường huyết SAU ĂN 2 GIỜ",
            "normal": {
                "mmol": "< 7.8 mmol/L",
                "mg": "< 140 mg/dL",
                "status": "✅ BÌNH THƯỜNG"
            },
            "prediabetes": {
                "mmol": "7.8 - 11.0 mmol/L",
                "mg": "140 - 199 mg/dL",
                "status": "⚠️ TIỀN TIỂU ĐƯỜNG"
            },
            "diabetes": {
                "mmol": "≥ 11.1 mmol/L",
                "mg": "≥ 200 mg/dL",
                "status": "🔴 TIỂU ĐƯỜNG"
            }
        },
        "hba1c": {
            "name_vn": "HbA1c (đường huyết trung bình 3 tháng)",
            "note": "Không có đơn vị, tính theo %",
            "normal": {
                "value": "< 5.7%",
                "status": "✅ BÌNH THƯỜNG"
            },
            "prediabetes": {
                "value": "5.7 - 6.4%",
                "status": "⚠️ TIỀN TIỂU ĐƯỜNG"
            },
            "diabetes": {
                "value": "≥ 6.5%",
                "status": "🔴 TIỂU ĐƯỜNG"
            },
            "target_for_diabetics": {
                "value": "< 7%",
                "status": "🎯 MỤC TIÊU ĐIỀU TRỊ (cho người đã có tiểu đường)"
            }
        }
    },
    
    "target_for_diabetics_vn": """
🎯 MỤC TIÊU ĐƯỜNG HUYẾT CHO NGƯỜI TIỂU ĐƯỜNG:

📊 Đường huyết hàng ngày:
- Lúc đói (trước ăn):
  ✓ 4.4 - 7.2 mmol/L (80 - 130 mg/dL)
  
- Sau ăn 2 giờ:
  ✓ < 10.0 mmol/L (< 180 mg/dL)

📊 HbA1c (3 tháng):
  ✓ < 7% (mục tiêu chung)
  ✓ < 6.5% (người trẻ, khỏe)
  ✓ < 8% (người già, nhiều bệnh)

⚠️ LƯU Ý:
- Mục tiêu có thể khác nhau tùy từng người
- Hỏi bác sĩ mục tiêu cụ thể của BẠN
"""
}

# ============= DẤU HIỆU NHẬN BIẾT =============

SYMPTOMS_SIMPLE = {
    "classic_3P_vn": {
        "title": "🔺 3 DẤU HIỆU KINH ĐIỂN - Nhớ 3 chữ 'NHIỀU':",
        "symptoms": [
            {
                "name": "1️⃣ TIỂU NHIỀU (Polyuria)",
                "description": "Đi tiểu rất nhiều, cả ngày lẫn đêm",
                "details": [
                    "- Đi tiểu 10-20 lần/ngày",
                    "- Thức dậy đi tiểu 3-4 lần/đêm",
                    "- Tiểu ra nhiều nước",
                    "Tại sao? Thận thải đường ra nước tiểu → kéo nước theo"
                ]
            },
            {
                "name": "2️⃣ KHÁT NƯỚC NHIỀU (Polydipsia)",
                "description": "Khát nước liên tục, uống hoài không đủ",
                "details": [
                    "- Uống 3-5 lít nước/ngày vẫn khát",
                    "- Miệng khô liên tục",
                    "- Luôn muốn uống nước",
                    "Tại sao? Mất nước nhiều do tiểu nhiều"
                ]
            },
            {
                "name": "3️⃣ ĂN NHIỀU (Polyphagia)",
                "description": "Ăn nhiều nhưng vẫn đói, vẫn gầy",
                "details": [
                    "- Ăn nhiều hơn bình thường",
                    "- Vừa ăn xong đã đói",
                    "- Ăn nhiều nhưng gầy đi",
                    "Tại sao? Tế bào không có đường để làm năng lượng"
                ]
            }
        ]
    },
    
    "other_symptoms_vn": [
        "😴 Mệt mỏi, uể oải (cơ thể thiếu năng lượng)",
        "👁️ Nhìn mờ (đường cao làm mắt phù)",
        "🩹 Vết thương lâu lành (2-3 tuần vẫn không khỏi)",
        "🦠 Nhiễm trùng tái đi tái lại (da, nướu, tiết niệu)",
        "🦶 Tê bì chân tay (đặc biệt bàn chân)",
        "🔴 Da ngứa, khô",
        "⚫ Vùng da thâm đen (cổ, nách - dấu hiệu kháng insulin)",
        "📉 Giảm cân không rõ lý do (típ 1)"
    ],
    
    "emergency_vn": {
        "title": "🚨 CẤP CỨU - GỌI 115 NGAY:",
        "signs": [
            "⛔ Đường huyết RẤT CAO (> 22 mmol/L / > 400 mg/dL)",
            "⛔ Hơi thở có mùi trái cây lạ (dấu hiệu nhiễm toan)",
            "⛔ Thở nhanh, thở gấp",
            "⛔ Buồn nôn, nôn nhiều",
            "⛔ Đau bụng",
            "⛔ Lơ mơ, ngất",
            "",
            "⛔ Đường huyết RẤT THẤP (< 3.3 mmol/L / < 60 mg/dL):",
            "   - Vã mồ hôi lạnh",
            "   - Run rẩy",
            "   - Chóng mặt, lảo đảo",
            "   - Lú lẫn",
            "   - Co giật"
        ]
    }
}

# ============= THUỐC ĐIỀU TRỊ =============

MEDICATIONS_SIMPLE = {
    "overview_vn": """
💊 ĐIỀU TRỊ TIỂU ĐƯỜNG:

Típ 1: PHẢI TIÊM INSULIN
Típ 2: Thay đổi lối sống → Thuốc uống → Insulin (nếu cần)
""",
    
    "oral_medications": [
        {
            "class": "Metformin",
            "street_name": "Thuốc 'Met' - Thường là viên đầu tiên",
            "brand_names": "Glucophage, Diabetmin, Glucomin",
            "what_it_does": "Giảm đường gan sản xuất, giúp cơ thể dùng đường tốt hơn",
            "benefits_vn": [
                "✓ Giảm đường huyết hiệu quả",
                "✓ Giúp giảm cân nhẹ",
                "✓ Không gây hạ đường huyết",
                "✓ Rẻ tiền",
                "✓ An toàn lâu dài"
            ],
            "how_to_take": [
                "💊 Uống 1-2 lần/ngày",
                "🍽️ Uống CÙNG hoặc SAU BỮA ĂN (quan trọng!)",
                "⏰ Bắt đầu liều thấp, tăng dần"
            ],
            "side_effects": [
                "Đau bụng, chạy bụng (rất hay gặp)",
                "Buồn nôn (thường giảm sau 1-2 tuần)",
                "Đầy hơi, chướng bụng"
            ],
            "tips_vn": [
                "💡 Uống SAU ĂN để giảm tác dụng phụ",
                "💡 Bắt đầu liều thấp, tăng từ từ",
                "💡 Dùng thuốc nhả chậm (XR) nếu không chịu được thuốc thường",
                "⚠️ Không uống nếu suy thận nặng"
            ]
        },
        {
            "class": "Sulfonylureas",
            "street_name": "Nhóm kích thích tụy tiết insulin",
            "brand_names": "Glimepiride (Amaryl), Gliclazide (Diamicron)",
            "what_it_does": "Kích thích tụy tiết thêm insulin",
            "benefits_vn": [
                "✓ Giảm đường nhanh",
                "✓ Giá rẻ",
                "✓ Uống 1-2 lần/ngày"
            ],
            "how_to_take": [
                "💊 Uống TRƯỚC BỮA ĂN 15-30 phút",
                "⏰ Thường uống buổi sáng hoặc sáng + tối"
            ],
            "side_effects": [
                "⚠️ Hạ đường huyết (nguy hiểm!)",
                "Tăng cân (2-3kg)"
            ],
            "warning_vn": """
🚨 NGUY CƠ HẠ ĐƯỜNG HUYẾT:
- Nếu uống thuốc nhưng KHÔNG ĂN → nguy hiểm!
- Luôn mang kẹo trong túi
- Dấu hiệu hạ đường: Đói, run, vã mồ hôi, chóng mặt
"""
        },
        {
            "class": "DPP-4 inhibitors",
            "street_name": "Nhóm '-gliptin'",
            "brand_names": "Sitagliptin (Januvia), Vildagliptin (Galvus)",
            "what_it_does": "Tăng insulin khi ăn, giảm đường gan sản xuất",
            "benefits_vn": [
                "✓ Ít hạ đường huyết",
                "✓ Không tăng cân",
                "✓ Uống 1-2 lần/ngày",
                "✓ Ít tác dụng phụ"
            ],
            "how_to_take": [
                "💊 Uống bất kỳ lúc nào trong ngày",
                "🍽️ Có thể uống đói hoặc no"
            ],
            "side_effects": [
                "Ít tác dụng phụ",
                "Viêm họng, sổ mũi (nhẹ)"
            ],
            "note_vn": "Đắt hơn Metformin, thường dùng phối hợp"
        },
        {
            "class": "SGLT-2 inhibitors",
            "street_name": "Nhóm '-gliflozin'",
            "brand_names": "Dapagliflozin (Forxiga), Empagliflozin (Jardiance)",
            "what_it_does": "Thải đường qua nước tiểu",
            "benefits_vn": [
                "✓ Giảm đường huyết",
                "✓ Giảm cân (2-3kg)",
                "✓ Giảm huyết áp nhẹ",
                "✓ Bảo vệ tim, thận (rất tốt!)",
                "✓ Ít hạ đường huyết"
            ],
            "how_to_take": [
                "💊 Uống 1 lần/ngày vào buổi sáng"
            ],
            "side_effects": [
                "Nhiễm nấm vùng kín (phụ nữ hay gặp)",
                "Tiểu nhiều hơn",
                "Khát nước"
            ],
            "tips_vn": [
                "💡 Vệ sinh vùng kín sạch sẽ",
                "💡 Uống đủ nước",
                "⚠️ Đắt tiền nhất trong các thuốc tiểu đường"
            ]
        }
    ],
    
    "insulin_simple": {
        "when_vn": """
💉 KHI NÀO CẦN TIÊM INSULIN?

Típ 1: Luôn luôn cần insulin
Típ 2: Cần insulin khi:
- Thuốc uống không đủ kiểm soát
- HbA1c vẫn cao (> 9%)
- Đường huyết cao dai dẳng
- Mang thai
- Bệnh nặng, phẫu thuật
""",
        "types_simple": [
            {
                "type": "Insulin tác dụng nhanh",
                "examples": "Novorapid, Humalog, Apidra",
                "when": "Tiêm TRƯỚC BỮA ĂN 5-15 phút",
                "duration": "Tác dụng 3-5 giờ",
                "icon": "⚡"
            },
            {
                "type": "Insulin tác dụng ngắn",
                "examples": "Actrapid, Humulin R",
                "when": "Tiêm TRƯỚC BỮA ĂN 30 phút",
                "duration": "Tác dụng 6-8 giờ",
                "icon": "🔸"
            },
            {
                "type": "Insulin nền (NPH)",
                "examples": "Insulatard, Humulin N",
                "when": "Tiêm sáng và/hoặc tối",
                "duration": "Tác dụng 12-16 giờ",
                "icon": "⬜"
            },
            {
                "type": "Insulin nền dài",
                "examples": "Lantus, Levemir, Tresiba",
                "when": "Tiêm 1 lần/ngày, cùng giờ",
                "duration": "Tác dụng 24 giờ",
                "icon": "⬛"
            }
        ],
        "how_to_inject_vn": """
💉 CÁCH TIÊM INSULIN:

📍 Vị trí tiêm:
- Bụng (hấp thu nhanh nhất) ✓ Tốt nhất
- Đùi
- Cánh tay
- Mông

⚠️ LUÂN CHUYỂN vị trí (không tiêm một chỗ)

🔧 Kỹ thuật:
1. Rửa tay
2. Lau vùng tiêm bằng cồn (nếu có)
3. Véo nhẹ da
4. Đâm kim vuông góc 90 độ
5. Tiêm chậm rãi
6. Đợi 5-10 giây trước khi rút kim
7. Bỏ kim vào hộp đựng kim an toàn

💾 BẢO QUẢN:
- Lọ chưa mở: Tủ lạnh (2-8°C)
- Lọ đang dùng: Nhiệt độ phòng (< 30°C), dùng trong 28 ngày
- KHÔNG để đông cứng
- KHÔNG để nắng
""",
        "hypoglycemia_vn": """
⚠️ HẠ ĐƯỜNG HUYẾT - NGUY HIỂM NHẤT KHI TIÊM INSULIN

🚨 Dấu hiệu (đường < 3.9 mmol/L / < 70 mg/dL):
- Đói bỗng dưng
- Run tay, run người
- Vã mồ hôi lạnh
- Tim đập nhanh
- Chóng mặt
- Lo lắng
- Nếu nặng: Lú lẫn, co giật, ngất

✅ XỬ TRÍ NGAY:
Quy tắc 15-15:
1. Ăn/uống 15g đường:
   - 3 viên đường
   - 1/2 lon nước ngọt
   - 1 thìa mật ong
   - 3-4 viên kẹo
2. Chờ 15 phút
3. Đo lại đường huyết
4. Nếu vẫn < 3.9: Lặp lại

⛔ Nếu bất tỉnh: GỌI 115, KHÔNG cho ăn uống (sặc)

💡 PHÒNG TRÁNH:
- Luôn mang kẹo/nước ngọt
- Ăn đúng giờ sau tiêm insulin
- Đo đường trước khi lái xe
- Mang thẻ "Tôi bị tiểu đường"
"""
    }
}

# ============= CHẾ ĐỘ ĂN =============

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

# ============= VẬN ĐỘNG =============

EXERCISE_SIMPLE = {
    "why_vn": """
🏃 TẠI SAO PHẢI VẬN ĐỘNG?

Vận động giúp:
✓ Giảm đường huyết (tế bào dùng đường mà không cần nhiều insulin)
✓ Giảm cân
✓ Tăng độ nhạy insulin
✓ Giảm nguy cơ tim mạch
✓ Tâm trạng tốt hơn
✓ Ngủ ngon hơn

Vận động đều đặn = THUỐC KHÔNG TỐN TIỀN!
""",
    
    "how_much_vn": """
🎯 MỤC TIÊU:

150 phút/tuần vận động VỪA PHẢI
= 30 phút x 5 ngày

Hoặc: 75 phút/tuần vận động MẠNH

Thêm: Tập kháng lực 2-3 lần/tuần
""",
    
    "types_vn": [
        {
            "name": "🚶 VẬN ĐỘNG NHỊP ĐIỆU (Aerobic)",
            "examples": "Đi bộ nhanh, chạy bộ, bơi, đạp xe, khiêu vũ",
            "benefit": "Giảm đường huyết, tốt cho tim",
            "how_long": "30-60 phút/lần, 5-7 ngày/tuần"
        },
        {
            "name": "🏋️ TẬP KHÁNG LỰC (Tạ)",
            "examples": "Tập tạ nhẹ, dây kháng lực, squat, chống đẩy",
            "benefit": "Tăng cơ, giảm mỡ, tăng độ nhạy insulin",
            "how_long": "20-30 phút, 2-3 lần/tuần"
        },
        {
            "name": "🧘 GIÃN CƠ, YOGA",
            "examples": "Yoga, tai chi, giãn cơ",
            "benefit": "Giảm stress, mềm dẻo, thư giãn",
            "how_long": "10-15 phút mỗi ngày"
        }
    ],
    
    "safety_tips_vn": """
⚠️ AN TOÀN KHI TẬP:

TRƯỚC KHI TẬP:
✅ Đo đường huyết
   - < 5.6 mmol/L (< 100 mg/dL): Ăn bữa phụ trước
   - 5.6 - 13.9 mmol/L (100 - 250 mg/dL): An toàn, tập được
   - > 13.9 mmol/L (> 250 mg/dL): Đợi đường xuống, không tập

✅ Mang theo:
   - Kẹo, nước ngọt (phòng hạ đường)
   - Nước uống
   - Máy đo đường huyết

TRONG KHI TẬP:
✅ Mang giày tất phù hợp (bảo vệ chân)
✅ Uống nước thường xuyên
✅ Bắt đầu nhẹ, tăng dần

SAU KHI TẬP:
✅ Đo đường lại (có thể giảm đường đến 12-24 giờ sau)
✅ Theo dõi dấu hiệu hạ đường

🛑 NGỪNG NGAY NẾU:
- Run, vã mồ hôi, chóng mặt (dấu hiệu hạ đường)
- Đau ngực
- Khó thở quá
- Tê bì, đau chân
"""
}

# ============= THEO DÕI TẠI NHÀ =============

MONITORING_SIMPLE = {
    "when_to_check_vn": """
🩸 KHI NÀO ĐO ĐƯỜNG HUYẾT?

🎯 NẾU CHỈ UỐNG THUỐC:
- Đo 1-2 lần/ngày là đủ
- Xoay vòng: Sáng đói, trước ăn, sau ăn 2h, trước ngủ

🎯 NẾU TIÊM INSULIN:
- Đo ít nhất 4 lần/ngày:
  ✓ Sáng đói
  ✓ Trước bữa chính
  ✓ Sau ăn 2h (đôi khi)
  ✓ Trước ngủ
  ✓ Nếu có triệu chứng bất thường

🎯 TÌNH HUỐNG ĐẶC BIỆT:
- Khi bị ốm
- Trước và sau vận động
- Khi có triệu chứng hạ đường
- Trước khi lái xe đường dài
- Giữa đêm (nếu nghi ngờ hạ đường ban đêm)
""",
    
    "how_to_check_vn": """
💉 CÁCH ĐO ĐƯỜNG HUYẾT:

1. Rửa tay (KHÔNG dùng cồn - làm sai kết quả)
2. Lau khô
3. Gắn kim vào bút châm
4. Lấy que thử, gắn vào máy
5. Châm vào MÉP NGÓN TAY (ít đau hơn)
6. Vắt nhẹ, giọt máu to bằng hạt đậu
7. Đưa que thử vào giọt máu
8. Đợi kết quả (5 giây)
9. Ghi số vào sổ

💡 MẸO:
- Luân chuyển ngón tay (đừng châm 1 ngón)
- Châm ở mép ngón, không giữa đầu ngón
- Rửa tay nước ấm trước châm (máu lên dễ hơn)
- Vắt nhẹ từ gốc ngón lên (đừng chặt đầu ngón)
""",
    
    "target_ranges_vn": """
🎯 CHỈ SỐ MỤC TIÊU:

🩸 Đường huyết:
Lúc đói: 4.4 - 7.2 mmol/L (80 - 130 mg/dL)
Sau ăn 2h: < 10.0 mmol/L (< 180 mg/dL)

📊 HbA1c: < 7% (đo 3 tháng/lần)

📏 Huyết áp: < 140/90 mmHg

💉 Cholesterol:
LDL: < 2.6 mmol/L (< 100 mg/dL)
HDL: > 1.0 mmol/L nam, > 1.3 mmol/L nữ
Triglyceride: < 1.7 mmol/L (< 150 mg/dL)

⚖️ Cân nặng:
BMI: 18.5 - 22.9 (người châu Á)
Vòng eo: Nam < 90cm, Nữ < 80cm
""",
    
    "record_keeping_vn": """
📝 GHI CHÉP:

Ghi vào sổ hoặc app mỗi lần đo:
- Ngày giờ
- Đường huyết
- Bữa ăn (ăn gì, bao nhiêu)
- Thuốc (đã uống/tiêm chưa)
- Vận động (làm gì, bao lâu)
- Triệu chứng đặc biệt

→ Mang sổ ghi khi khám bác sĩ
"""
}

# ============= BIẾN CHỨNG =============

COMPLICATIONS_SIMPLE = {
    "why_control_vn": """
⚠️ TẠI SAO PHẢI KIỂM SOÁT ĐƯỜNG HUYẾT?

Đường huyết cao lâu ngày làm hỏng:
❤️ TIM MẠCH: Nhồi máu, đột quỵ (x2-4 lần)
👁️ MẮT: Mù lòa
🦶 THẬN: Suy thận, lọc máu
🦶 DÂY THẦN KINH: Tê chân, yếu liệt
🦶 BÀN CHÂN: Loét, hoại tử, cắt cụt

Tin tốt: Kiểm soát tốt → GIẢM 40-60% biến chứng!
""",
    
    "foot_care_vn": """
🦶 CHĂM SÓC CHÂN (Rất quan trọng!)

MỖI NGÀY:
✅ Kiểm tra chân (dùng gương nếu không nhìn được):
   - Vết thương, phồng rộp
   - Đỏ, sưng
   - Móng mọc lệch
   
✅ Rửa chân bằng nước ấm, xà phòng nhẹ
✅ Lau khô kỹ (đặc biệt kẽ ngón)
✅ Bôi kem dưỡng (trừ kẽ ngón)

CẮT MÓNG:
✅ Cắt thẳng ngang, không cắt quá sâu vào kẽ

GIÀY DÉP:
✅ Đi giày vừa vặn, êm chân
✅ Đi tất mềm, không chun chặt
✅ Kiểm tra trong giày trước khi đi (có sạn sỏi không)
✅ KHÔNG đi chân đất

🚨 GỌI BÁC SĨ NGAY NẾU:
- Vết thương không lành sau 2-3 ngày
- Đỏ, sưng, nóng, mủ
- Đau chân tăng
- Móng thay đổi màu
- Tê, mất cảm giác

💡 Khám chân ở bác sĩ ít nhất 1 lần/năm
""",
    
    "eye_care_vn": """
👁️ CHĂM SÓC MẮT:

✅ Khám mắt (đáy mắt) MỖI NĂM, ngay cả khi nhìn rõ
✅ Kiểm soát đường huyết, huyết áp tốt
✅ Bỏ thuốc lá

🚨 ĐẾN NGAY NẾU:
- Nhìn mờ đột ngột
- Thấy đốm, ruồi bay
- Mất thị trường (một phần không nhìn thấy)
- Đau mắt
"""
}

# ============= CHATBOT FLOW =============

CHATBOT_QUESTIONS = [
    {
        "step": 1,
        "question_vn": "Xin chào! Tôi là trợ lý tư vấn về bệnh tiểu đường 😊\n\n🤔 Bạn đã được chẩn đoán tiểu đường chưa?",
        "options": ["Rồi (típ 1)", "Rồi (típ 2)", "Chưa, tôi nghi ngờ", "Tiền tiểu đường"]
    },
    {
        "step": 2,
        "question_vn": "Bạn có triệu chứng nào không?\n\n- Tiểu nhiều (cả đêm)\n- Khát nước liên tục\n- Ăn nhiều nhưng gầy\n- Mệt mỏi\n- Nhìn mờ\n- Vết thương lâu lành",
        "purpose": "Đánh giá triệu chứng"
    },
    {
        "step": 3,
        "question_vn": "Đường huyết gần đây của bạn là bao nhiêu? (nếu có đo)\n\nVí dụ: 8.5 mmol/L hoặc 150 mg/dL"
    },
    {
        "step": 4,
        "question_vn": "Bạn đang điều trị thế nào?\n\n1️⃣ Chưa điều trị\n2️⃣ Chỉ thay đổi lối sống\n3️⃣ Uống thuốc\n4️⃣ Tiêm insulin\n5️⃣ Cả thuốc và insulin"
    },
    {
        "step": 5,
        "question_vn": "Tôi có thể tư vấn gì cho bạn?\n\n1️⃣ Giải thích về bệnh tiểu đường\n2️⃣ Ăn uống như thế nào?\n3️⃣ Thuốc điều trị\n4️⃣ Đo đường huyết tại nhà\n5️⃣ Vận động an toàn\n6️⃣ Phòng ngừa biến chứng"
    }
]

