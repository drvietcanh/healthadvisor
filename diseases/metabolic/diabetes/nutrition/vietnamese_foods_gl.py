"""
Vietnamese Foods Glycemic Load - Bảng GL thực phẩm Việt Nam
Danh sách 45+ thực phẩm phổ biến với GI, carb, GL và khuyến nghị
"""

# Danh sách thực phẩm Việt Nam với GL chi tiết
VIETNAMESE_FOODS_GL = [
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
]

