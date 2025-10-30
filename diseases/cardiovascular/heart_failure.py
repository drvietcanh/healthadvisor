"""
Module tư vấn về Suy Tim - Ngôn ngữ dễ hiểu cho bệnh nhân
"""

# ============= SUY TIM LÀ GÌ? =============

DISEASE_INFO = {
    "name_vn": "Suy Tim",
    "name_en": "Heart Failure",
    "simple_explanation_vn": """
🫀 SUY TIM LÀ GÌ?

Suy tim có nghĩa là tim bạn không bơm máu tốt như trước. 
Không phải tim ngừng đập, mà tim yếu đi, không đủ sức đẩy máu nuôi cơ thể.

Giống như chiếc bơm nước cũ - vẫn chạy nhưng không đủ mạnh.
""",
    "causes_simple_vn": [
        "💔 Nhồi máu cơ tim (đã bị đau tim trước đây)",
        "📈 Huyết áp cao lâu năm (tim phải làm việc vất vả)",
        "🩺 Bệnh van tim (van tim hỏng, không đóng mở tốt)",
        "🫀 Bệnh cơ tim (cơ tim yếu từ nhiều nguyên nhân)",
        "💓 Rối loạn nhịp tim (tim đập không đều)"
    ]
}

# ============= DẤU HIỆU NHẬN BIẾT =============

SYMPTOMS_SIMPLE = {
    "main_signs_vn": {
        "title": "🚨 5 DẤU HIỆU CHÍNH - Ghi nhớ 5 chữ H:",
        "signs": [
            {
                "letter": "H1 - HỔN HẾN (khó thở)",
                "description": "Thở nhanh, thở gấp, đặc biệt khi:",
                "details": [
                    "- Đi bộ nhanh, leo cầu thang",
                    "- Nằm xuống (phảiê nhiều gối mới thở được)",
                    "- Ban đêm thức giấc vì khó thở",
                    "- Cảm giác như sắp ngạt"
                ]
            },
            {
                "letter": "H2 - HÚNG (phù nước)",
                "description": "Sưng phù ở:",
                "details": [
                    "- Bàn chân, cổ chân (ấn vào lõm xuống)",
                    "- Ống chân, bắp chân",
                    "- Bụng chướng (tích nước trong bụng)",
                    "- Tăng cân đột ngột (2-3kg trong vài ngày)"
                ]
            },
            {
                "letter": "H3 - HƠI (mệt mỏi, uể oải)",
                "description": "Mệt lả không rõ lý do:",
                "details": [
                    "- Làm việc nhà cũng thấy mệt",
                    "- Không muốn hoạt động",
                    "- Ngủ nhiều vẫn mệt",
                    "- Không còn sức như trước"
                ]
            },
            {
                "letter": "H4 - HO (ho dai dẳng)",
                "description": "Ho kéo dài, đặc biệt:",
                "details": [
                    "- Ho ban đêm",
                    "- Ho khi nằm",
                    "- Khạc đờm có bọt màu hồng",
                    "- Ho không khỏi dù uống thuốc ho"
                ]
            },
            {
                "letter": "H5 - HỐI (chóng mặt, choáng váng)",
                "description": "Cảm giác:",
                "details": [
                    "- Đầu quay quay, muốn té",
                    "- Đứng lên bị choáng",
                    "- Tim đập nhanh, hồi hộp",
                    "- Ngất xỉu (nghiêm trọng)"
                ]
            }
        ]
    },
    "emergency_vn": {
        "title": "🚨 KHI NÀO GỌI CẤP CỨU 115?",
        "signs": [
            "⛔ Thở rất khó, phải há hốc mồm thở",
            "⛔ Ngực đau dữ dội",
            "⛔ Tím môi, tím móng tay",
            "⛔ Khạc đờm có máu, bọt hồng",
            "⛔ Choáng váng, sắp ngất",
            "⛔ Tim đập rất nhanh hoặc rất chậm"
        ]
    }
}

# ============= THUỐC ĐIỀU TRỊ - GIẢI THÍCH ĐƠN GIẢN =============

MEDICATIONS_SIMPLE = {
    "warning_vn": """
⚠️ LƯU Ý QUAN TRỌNG:
- Chỉ uống thuốc bác sĩ kê
- KHÔNG tự ý ngưng thuốc (rất nguy hiểm!)
- Uống đúng giờ, đủ liều
- Hỏi bác sĩ nếu có tác dụng không tốt
""",
    
    "common_drugs_simple": [
        {
            "type": "Thuốc lợi tiểu (thuốc tiểu)",
            "street_name": "Thường gọi: 'Thuốc đi tiểu'",
            "examples": "Lasix, Furosemide, Aldactone",
            "what_it_does": "Giúp cơ thể đào thải nước và muối ra ngoài",
            "benefits": [
                "✓ Giảm phù nề chân, bụng",
                "✓ Giảm khó thở (vì giảm nước trong phổi)",
                "✓ Tim không phải làm việc quá sức"
            ],
            "how_to_take": [
                "🕐 Uống vào buổi sáng (tránh tiểu đêm)",
                "💧 Có thể tiểu nhiều trong 2-3 giờ đầu",
                "🚽 Chuẩn bị nhà vệ sinh gần (sẽ đi tiểu nhiều)"
            ],
            "side_effects_simple": [
                "Có thể tiểu nhiều, mất nước → uống nước đủ",
                "Có thể hết kali → ăn chuối, cam (giàu kali)",
                "Chóng mặt khi đứng lên → đứng lên từ từ"
            ],
            "when_to_call_doctor": [
                "⚠️ Tiểu quá ít hoặc quá nhiều",
                "⚠️ Mệt rã rời, yếu cơ",
                "⚠️ Tim đập loạn"
            ]
        },
        {
            "type": "Thuốc ức chế men chuyển",
            "street_name": "Thuốc tên có đuôi '-pril'",
            "examples": "Enalapril, Lisinopril, Ramipril",
            "what_it_does": "Giúp mạch máu giãn rộng, tim bơm nhẹ nhàng hơn",
            "benefits": [
                "✓ Giảm gánh nặng cho tim",
                "✓ Giảm huyết áp",
                "✓ Bảo vệ tim và thận",
                "✓ Sống lâu hơn (đã được chứng minh)"
            ],
            "how_to_take": [
                "💊 Uống 1-2 lần/ngày",
                "🍽️ Có thể uống lúc đói hoặc no",
                "📅 Uống đều đặn mỗi ngày"
            ],
            "side_effects_simple": [
                "Ho khan (khoảng 10% người bị) - nếu ho nhiều báo bác sĩ",
                "Chóng mặt nhẹ ngày đầu",
                "Mệt (sẽ quen dần)"
            ],
            "important_notes": [
                "🚫 KHÔNG uống nếu đang mang thai",
                "⚠️ Báo bác sĩ nếu ho quá nhiều (sẽ đổi sang thuốc khác)"
            ]
        },
        {
            "type": "Thuốc chẹn beta",
            "street_name": "Thuốc tên có đuôi '-lol'",
            "examples": "Bisoprolol, Metoprolol, Carvedilol",
            "what_it_does": "Làm tim đập chậm lại, nghỉ ngơi nhiều hơn",
            "benefits": [
                "✓ Tim đập chậm, ít vất vả",
                "✓ Giảm nguy cơ đau tim",
                "✓ Điều hòa nhịp tim",
                "✓ Kéo dài tuổi thọ"
            ],
            "how_to_take": [
                "💊 Uống 1-2 lần/ngày",
                "🍽️ Tốt nhất uống cùng bữa ăn",
                "⏰ Uống đúng giờ"
            ],
            "side_effects_simple": [
                "Mệt, uể oải (thường giảm sau vài tuần)",
                "Tay chân lạnh",
                "Chóng mặt nhẹ",
                "Ngủ không ngon (ít gặp)"
            ],
            "important_notes": [
                "⚠️ KHÔNG ngưng đột ngột (rất nguy hiểm!)",
                "📊 Nếu muốn ngưng, phải giảm từ từ theo bác sĩ"
            ]
        },
        {
            "type": "Digoxin (Lá ké)",
            "street_name": "Thuốc lá ké, Lanoxin",
            "examples": "Digoxin 0.25mg",
            "what_it_does": "Giúp tim co bóp mạnh hơn, đập chậm và đều hơn",
            "benefits": [
                "✓ Tim co bóp khỏe hơn",
                "✓ Điều trị rối loạn nhịp tim",
                "✓ Giảm triệu chứng suy tim"
            ],
            "how_to_take": [
                "💊 Thường uống 1 lần/ngày",
                "⏰ Uống cùng giờ mỗi ngày",
                "📏 Liều rất quan trọng - ĐÚNG LIỀU"
            ],
            "side_effects_simple": [
                "Buồn nôn, chán ăn",
                "Nhìn có vầng vàng quanh đèn (dấu hiệu nguy hiểm!)",
                "Tim đập chậm quá"
            ],
            "when_to_call_doctor": [
                "⚠️ Buồn nôn nhiều, không ăn được",
                "⚠️ Nhìn thấy màu vàng lạ",
                "⚠️ Tim đập < 50 nhịp/phút",
                "⚠️ Loạn nhịp tim"
            ]
        }
    ]
}

# ============= CHẾ ĐỘ ĂN - NGÔN NGỮ DÂN DÃ =============

NUTRITION_SIMPLE = {
    "main_rule_vn": """
🍽️ NGUYÊN TẮC ĂN UỐNG CHO NGƯỜI SUY TIM:

Nhớ 3 GIẢM, 3 TĂNG:

📉 3 GIẢM:
1. GIẢM MUỐI (quan trọng nhất!)
2. GIẢM NƯỚC (nếu bác sĩ dặn)
3. GIẢM MỠ ĐỘNG VẬT

📈 3 TĂNG:
1. TĂNG RAU CỦ
2. TĂNG ĐẠM (thịt nạc, cá, trứng)
3. TĂNG KALI (chuối, cam, khoai)
""",
    
    "salt_restriction_simple": {
        "why_vn": """
🧂 TẠI SAO PHẢI GIẢM MUỐI?

Muối giữ nước → Nước tích nhiều → Tim phải bơm nhiều hơn → Tim càng yếu

Giống như bắt người đã mệt phải kéo thêm nước nặng vậy!
""",
        "how_much_vn": """
📊 ĂN BAO NHIÊU MUỐI?

Người bình thường: 1 thìa cà phê muối/ngày
Người suy tim: ½ thìa cà phê muối/ngày (hoặc ít hơn)

💡 MẸO TÍNH NHANH:
- 1 thìa cà phê muối = 5g
- Bạn cần ăn < 2-3g muối/ngày
""",
        "hidden_salt_vn": """
🕵️ MUỐI ẨN - TRÁNH CÁC MÓN NÀY:

❌ Đồ MẶN:
- Mắm, nước mắm, tương
- Muối chua, dưa chua
- Chả, giò, thịt nguội
- Xúc xích, thịt xông khói
- Snack (khoai chiên, bánh quy mặn)

❌ Đồ HỘP/ĐÓNG GÓI:
- Mì gói (rất nhiều muối!)
- Đồ hộp (cá hộp, thịt hộp)
- Nước sốt chai (tương ớt, xì dầu)
- Bột canh, hạt nêm, mì chính

❌ ĂN NGOÀI:
- Phở (nước dùng mặn)
- Bún, miến (nước dùng)
- Cơm quán (thường nấu mặn)
- Đồ ăn nhanh
""",
        "tips_vn": """
💡 LÀM SAO ĂN NGON MÀ ÍT MUỐI?

✅ THAY MUỐI BẰNG:
- Chanh, giấm
- Gừng, tỏi, hành
- Tiêu, ớt (ít)
- Rau thơm (ngò, rau răm, húng)

✅ NẤU Ở NHÀ:
- Tự nấu, tự nêm nhạt
- Nếu ăn phở/bún: bỏ nước dùng, chỉ ăn rau + thịt

✅ ĐỌC NHÃN:
- Chọn sản phẩm ghi "ít muối" hoặc "không muối"
- Tránh sản phẩm có > 120mg natri/100g
"""
    },
    
    "fluid_restriction_simple": {
        "why_vn": """
💧 TẠI SAO PHẢI HẠN CHẾ NƯỚC?

Nếu suy tim nặng:
- Thận làm việc kém
- Nước tích lại trong cơ thể
- Phù chân, phù phổi, khó thở

Nhưng không phải ai cũng phải hạn chế!
→ Hỏi bác sĩ xem bạn có cần không.
""",
        "how_much_vn": """
📏 UỐNG BAO NHIÊU NƯỚC?

Nếu bác sĩ bảo hạn chế:
- Thường: 1 - 1.5 lít/ngày (5-7 ly)
- Suy tim nặng: 0.8 - 1 lít/ngày (4-5 ly)

💡 CÁCH TÍNH:
Tất cả chất lỏng đều tính:
- Nước lọc, trà
- Súp, cháo, canh
- Sữa, nước hoa quả
- Thạch, kem
""",
        "tips_vn": """
💡 MẸO KIỂM SOÁT NƯỚC:

✅ Dùng ly nhỏ
✅ Súc miệng khi khát (đừng nuốt)
✅ Ngậm đá lạnh
✅ Nhai kẹo cao su không đường
✅ Cân mỗi sáng - nếu tăng cân đột ngột (1-2kg) = tích nước!
"""
    },
    
    "what_to_eat_vn": {
        "breakfast_examples": [
            "🥣 Cháo thịt băm (nhạt) + trứng + rau",
            "🍞 Bánh mì + trứng luộc + cà chua",
            "🥛 Sữa tươi không đường + yến mạch + chuối"
        ],
        "lunch_examples": [
            "🍚 Cơm + cá hấp (ít muối) + rau luộc + canh rau",
            "🍚 Cơm + ức gà luộc + đậu hũ + rau xào",
            "🍚 Cơm + thịt bò xào rau củ (ít muối)"
        ],
        "dinner_examples": [
            "🍜 Miến gà (bỏ nước dùng, chỉ ăn thịt + rau)",
            "🍚 Cơm + cá kho (rất nhạt) + rau",
            "🥗 Salad gà + bánh mì nguyên cám"
        ],
        "snacks": [
            "🍌 Chuối (tốt, nhiều kali)",
            "🍊 Cam, quýt",
            "🥜 Hạt không muối (1 nắm nhỏ)",
            "🥛 Sữa chua không đường"
        ]
    },
    
    "foods_to_avoid_simple": [
        "🚫 Đồ CHIÊN RÁN (gà rán, khoai chiên...)",
        "🚫 Đồ MỠ NHIỀU (mỡ lợn, da gà, sườn...)",
        "🚫 Đồ NGỌT (bánh kem, nước ngọt...)",
        "🚫 RƯỢU, BIA (quan trọng!)",
        "🚫 CÀ PHÊ NHIỀU (> 2 ly/ngày)",
        "🚫 Đồ HỘP, ĐÓ NG GÓI"
    ]
}

# ============= VẬN ĐỘNG - HƯỚNG DẪN ĐƠN GIẢN =============

EXERCISE_SIMPLE = {
    "can_i_exercise_vn": """
❓ SUY TIM CÓ ĐƯỢC VẬN ĐỘNG KHÔNG?

✅ CÓ! Vận động vừa phải RẤT TốT:
- Giúp tim khỏe hơn
- Tăng sức bền
- Giảm mệt mỏi
- Tâm trạng tốt hơn

❌ NHƯNG:
- Phải vận động ĐÚNG CÁCH
- KHÔNG tập quá sức
- Phải hỏi bác sĩ trước
""",
    
    "safe_exercises_vn": [
        {
            "name": "🚶 ĐI BỘ",
            "description": "Tốt nhất cho người suy tim",
            "how_to": [
                "Đi bộ chậm rãi 10-30 phút/ngày",
                "Đi đều đặn, không vội",
                "Nếu mệt thì nghỉ, ngồi xuống",
                "Đi ở chỗ bằng phẳng (tránh lên dốc)"
            ],
            "target": "Mục tiêu: 30 phút/ngày, 5 ngày/tuần"
        },
        {
            "name": "🧘 TẬP GIÃ CƠ NHẸ NHÀNG",
            "description": "Giãn cơ, yoga nhẹ, tai chi",
            "how_to": [
                "Giãn cơ từng phần: cánh tay, chân, lưng",
                "Hít thở sâu khi giãn",
                "Không giãn quá căng",
                "10-15 phút mỗi ngày"
            ]
        },
        {
            "name": "🪑 TẬP NGỒI",
            "description": "Nếu quá mệt để đi bộ",
            "how_to": [
                "Ngồi trên ghế, co duỗi chân",
                "Xoay cổ tay, cổ chân",
                "Vung tay nhẹ nhàng",
                "5-10 phút, vài lần/ngày"
            ]
        }
    ],
    
    "exercise_rules_vn": """
⚠️ QUY TẮC AN TOÀN KHI TẬP:

✅ TRƯỚC KHI TẬP:
1. Hỏi bác sĩ xem được tập không
2. Chọn thời điểm mát mẻ (sáng sớm, chiều mát)
3. Mặc quần áo thoáng mát
4. Đi giày êm chân

✅ TRONG KHI TẬP:
1. Tập NHẸ NHÀNG, TỪTỪ
2. Có thể nói chuyện được = vừa sức
3. Không nín thở
4. Uống nước từng ngụm nhỏ (nếu được phép)

🛑 NGỪNG NGAY NẾU:
- Đau ngực
- Khó thở nhiều
- Chóng mặt, muốn ngất
- Mệt quá
- Tim đập loạn, rất nhanh
- Buồn nôn

→ Ngồi xuống nghỉ. Nếu không khỏi sau 5-10 phút: GỌI 115
""",
    
    "what_not_to_do_vn": [
        "❌ KHÔNG nâng vật nặng (>5kg)",
        "❌ KHÔNG đẩy, kéo đồ nặng",
        "❌ KHÔNG chạy bộ nhanh",
        "❌ KHÔNG leo dốc cao",
        "❌ KHÔNG tập khi trời nóng",
        "❌ KHÔNG tập khi đang bị cảm, sốt",
        "❌ KHÔNG tập sau ăn (đợi 1-2 giờ)"
    ]
}

# ============= THEO DÕI TẠI NHÀ =============

HOME_MONITORING_SIMPLE = {
    "daily_tasks_vn": """
📋 THEO DÕI MỖI NGÀY:

1️⃣ CÂN NẶNG (quan trọng nhất!)
   ⏰ Mỗi sáng, sau đi vệ sinh, trước ăn sáng
   📝 Ghi vào sổ
   🚨 Nếu tăng > 1kg trong 1 ngày hoặc > 2kg trong 1 tuần → GỌI BÁC SĨ
   
   Tại sao? Tăng cân nhanh = tích nước = suy tim nặng lên!

2️⃣ TRIỆU CHỨNG
   ✅ Có khó thở không?
   ✅ Chân có phù không?
   ✅ Có mệt bất thường không?
   ✅ Ho nhiều không?
   
3️⃣ UỐNG THUỐC ĐÚNG GIỜ
   ✅ Dùng hộp phân liều thuốc
   ✅ Đặt báo thức nhắc nhở
   ✅ Không quên liều nào
""",
    
    "red_flags_vn": """
🚩 DẤU HIỆU NGUY HIỂM - GỌI BÁC SĨ NGAY:

⛔ CẤP CỨU 115 NẾU:
- Thở rất khó, không nằm được
- Đau ngực
- Choáng váng, ngất
- Khạc máu

⚠️ GỌI BÁC SĨ TRONG NGÀY NẾU:
- Tăng cân > 1kg/ngày
- Phù chân tăng nhanh
- Khó thở nhiều hơn bình thường
- Mệt tăng đột ngột
- Ho tăng, ho đờm nhiều
- Tim đập rất nhanh (>100) hoặc rất chậm (<50)
- Chóng mặt nhiều lần

📞 GỌI BÁC SĨ SAU VÀI NGÀY NẾU:
- Chán ăn hoàn toàn
- Buồn nôn nhiều ngày
- Tác dụng phụ thuốc khó chịu
"""
}

# ============= LỜI KHUYÊN SỐNG CHUNG VỚI SUY TIM =============

LIVING_WITH_HF = {
    "daily_tips_vn": [
        "😴 NGỦ ĐỦ GIẤC: 7-8 giờ/đêm, đầu cao hơn chân (2-3 cái gối)",
        "🧘 GIẢM STRESS: Nghe nhạc, thiền, cầu nguyện",
        "❄️ TRÁNH NÓNG QUÁNH: Ở nơi mát, dùng quạt/máy lạnh",
        "🚫 BỎ THUỐC LÁ: Hút thuốc làm tim yếu thêm",
        "💉 TIÊM PHÒNG: Cúm, phế cầu (hỏi bác sĩ)",
        "👨‍👩‍👧 NHỜ GIA ĐÌNH: Không ngại yêu cầu giúp đỡ",
        "📱 KẾT NỐI: Tham gia nhóm bệnh nhân suy tim"
    ],
    
    "sex_and_relationship_vn": """
❤️ QUAN HỆ TÌNH DỤC:

Nhiều người suy tim vẫn có thể quan hệ bình thường.

✅ AN TOÀN NẾU:
- Bạn có thể leo 2 tầng cầu thang không khó thở
- Triệu chứng ổn định

⚠️ LƯU Ý:
- Chọn tư thế thoải mái, không vất vả
- Ngừng nếu đau ngực, khó thở
- Hỏi bác sĩ nếu lo lắng

Đừng ngại hỏi bác sĩ - họ quen với câu hỏi này!
""",
    
    "travel_tips_vn": """
✈️ ĐI DU LỊCH:

✅ ĐƯỢC đi du lịch nếu bệnh ổn định
✅ Chuẩn bị:
- Mang đủ thuốc (+ thêm 1 tuần phòng trường hợp)
- Mang danh sách thuốc, bệnh án tóm tắt
- Biết bệnh viện gần nơi đến
- Mua bảo hiểm du lịch

⚠️ TRÁNH:
- Vùng cao > 2000m (ít oxy)
- Nơi quá nóng, ẩm
- Bay dài > 4 giờ (dễ phù chân - phải đi lại thường xuyên)
"""
}

# ============= CÂU HỎI THƯỜNG GẶP =============

FAQ_SIMPLE = [
    {
        "q_vn": "Suy tim có khỏi được không?",
        "a_vn": "Suy tim là bệnh mãn tính, khó khỏi hẳn. NHƯNG bạn vẫn có thể sống tốt, lâu dài nếu:\n- Uống thuốc đúng\n- Ăn uống đúng cách\n- Vận động vừa phải\n- Theo dõi sát\n\nNhiều người sống 10-20 năm với suy tim!"
    },
    {
        "q_vn": "Tôi có thể làm việc được không?",
        "a_vn": "Tùy mức độ suy tim:\n- Nhẹ: Có thể làm việc nhẹ nhàng\n- Nặng: Nên nghỉ ngơi nhiều\n\nTránh công việc:\n- Nặng nhọc\n- Căng thẳng cao\n- Môi trường nóng"
    },
    {
        "q_vn": "Nếu quên uống thuốc thì sao?",
        "a_vn": "- Nhớ ra trong cùng ngày: Uống ngay\n- Đã gần giờ liều sau: Bỏ qua, KHÔNG uống 2 liều\n- KHÔNG tự ý tăng liều\n- Đặt báo thức để nhớ"
    },
    {
        "q_vn": "Có cần kiêng quan hệ tình dục không?",
        "a_vn": "Không nhất thiết! Nếu bệnh ổn định, bạn vẫn có thể quan hệ bình thường. Hỏi bác sĩ để yên tâm."
    }
]

# ============= CÂU HỎI CHO CHATBOT =============

CHATBOT_QUESTIONS = [
    {
        "step": 1,
        "question_vn": "Xin chào! Tôi là trợ lý tư vấn về bệnh suy tim. Để tôi hiểu tình trạng của bạn:\n\n🤔 Bạn đã được bác sĩ chẩn đoán suy tim chưa?",
        "options": ["Rồi", "Chưa, tôi chỉ nghi ngờ", "Không chắc"]
    },
    {
        "step": 2,
        "question_vn": "Bạn có triệu chứng nào sau đây không? (có thể chọn nhiều)\n\n- Khó thở (đặc biệt khi nằm xuống)\n- Phù chân\n- Mệt mỏi\n- Ho (đặc biệt ban đêm)\n- Chóng mặt",
        "purpose": "Đánh giá triệu chứng"
    },
    {
        "step": 3,
        "question_vn": "Bạn đang uống thuốc gì cho tim không? Nếu có, kể tên giúp tôi nhé.\n\n(Ví dụ: Lasix, Enalapril, Bisoprolol...)"
    },
    {
        "step": 4,
        "question_vn": "Bây giờ bạn muốn tôi tư vấn về phần nào?\n\n1️⃣ Giải thích về bệnh suy tim\n2️⃣ Ăn uống thế nào?\n3️⃣ Thuốc điều trị\n4️⃣ Có được tập thể dục không?\n5️⃣ Theo dõi tại nhà như thế nào?\n6️⃣ Khi nào cần gọi bác sĩ?"
    }
]

