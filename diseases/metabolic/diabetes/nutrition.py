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

