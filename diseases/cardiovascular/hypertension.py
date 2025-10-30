"""
Module tư vấn chi tiết về Tăng Huyết Áp (Hypertension)
Bao gồm: Chẩn đoán, Thuốc, Dinh dưỡng, Luyện tập
"""

# ============= THÔNG TIN BỆNH =============

DISEASE_INFO = {
    "name_vn": "Tăng Huyết Áp",
    "name_en": "Hypertension",
    "description_vn": """
Tăng huyết áp là tình trạng huyết áp trong động mạch cao hơn bình thường (≥140/90 mmHg).
Đây là yếu tố nguy cơ chính gây đột quỵ, nhồi máu cơ tim, suy tim và bệnh thận.
""",
    "description_en": """
Hypertension is a condition where blood pressure in arteries is higher than normal (≥140/90 mmHg).
It's a major risk factor for stroke, heart attack, heart failure, and kidney disease.
""",
    "prevalence_vn": "~25% dân số Việt Nam (khoảng 25 triệu người)",
    "risk_factors_vn": [
        "Tuổi cao (>50 tuổi)",
        "Tiền sử gia đình",
        "Béo phì (BMI ≥25)",
        "Ăn mặn (>5g muối/ngày)",
        "Ít vận động",
        "Căng thẳng, stress",
        "Hút thuốc, uống rượu",
        "Ngủ không đủ giấc"
    ]
}

# ============= PHÂN LOẠI HUYẾT ÁP =============

BP_CLASSIFICATION = {
    "normal": {
        "range": "< 120/80 mmHg",
        "name_vn": "Bình thường",
        "advice_vn": "Duy trì lối sống lành mạnh. Kiểm tra huyết áp mỗi năm."
    },
    "elevated": {
        "range": "120-129/<80 mmHg",
        "name_vn": "Huyết áp cao bình thường",
        "advice_vn": "Thay đổi lối sống ngay. Giảm muối, tăng vận động. Kiểm tra sau 3-6 tháng."
    },
    "stage1": {
        "range": "130-139/80-89 mmHg",
        "name_vn": "Tăng huyết áp giai đoạn 1",
        "advice_vn": "Thay đổi lối sống + có thể cần thuốc. Tái khám sau 1 tháng."
    },
    "stage2": {
        "range": "≥140/90 mmHg",
        "name_vn": "Tăng huyết áp giai đoạn 2",
        "advice_vn": "Cần dùng thuốc + thay đổi lối sống. Khám bác sĩ trong 1 tuần."
    },
    "crisis": {
        "range": ">180/120 mmHg",
        "name_vn": "CƠN TÁN HUYẾT ÁP - CẤP CỨU",
        "advice_vn": "🚨 GỌI 115 NGAY! Nguy cơ đột quỵ, nhồi máu tim cao!"
    }
}

# ============= TRIỆU CHỨNG =============

SYMPTOMS = {
    "common_vn": [
        "Hầu hết KHÔNG có triệu chứng (bệnh thầm lặng)",
        "Đau đầu (đặc biệt vùng gáy)",
        "Chóng mặt, hoa mắt",
        "Mệt mỏi",
        "Khó thở khi gắng sức",
        "Chảy máu cam",
        "Nhìn mờ"
    ],
    "emergency_vn": [
        "🚨 Đau đầu dữ dội đột ngột",
        "🚨 Đau ngực",
        "🚨 Khó thở nghiêm trọng",
        "🚨 Yếu liệt nửa người",
        "🚨 Nói khó, méo miệng",
        "🚨 Co giật"
    ]
}

# ============= CHẨN ĐOÁN =============

DIAGNOSTIC_STEPS = {
    "screening_vn": [
        "Đo huyết áp tại nhà (sáng và tối, 7 ngày liên tiếp)",
        "Đo huyết áp tại phòng khám (ít nhất 2 lần, cách nhau 1-2 tuần)",
        "Đo huyết áp 24 giờ (nếu cần)"
    ],
    "tests_vn": [
        "Điện tâm đồ (ECG)",
        "Xét nghiệm máu: Glucose, Creatinine, Lipid, Kali",
        "Xét nghiệm nước tiểu",
        "Siêu âm tim (nếu nghi ngờ tổn thương cơ tim)",
        "Siêu âm động mạch cảnh (nếu nghi ngờ xơ vữa)"
    ]
}

# ============= THUỐC ĐIỀU TRỊ =============

MEDICATIONS = {
    "overview_vn": """
⚠️ QUAN TRỌNG: Chỉ dùng thuốc theo chỉ định của bác sĩ!
Không tự ý ngưng thuốc khi huyết áp đã ổn định.
""",
    "drug_classes": {
        "ace_inhibitors": {
            "name_vn": "Thuốc ức chế men chuyển (ACE-I)",
            "street_name": "Nhóm '-pril'",
            "examples_vn": ["Enalapril", "Lisinopril", "Ramipril", "Perindopril"],
            "vietnam_brands": "🇻🇳 Tại VN: Coversyl (Perindopril 2/4/8mg), Tritace (Ramipril 2.5/5/10mg), Enalapril 5/10mg (generic), Lisinopril 10/20mg",
            "mechanism_vn": "Giãn mạch máu, giảm gánh nặng tim",
            "benefits_vn": [
                "✓ Giảm huyết áp hiệu quả",
                "✓ Bảo vệ tim, thận (đặc biệt tốt cho tiểu đường)",
                "✓ Giảm nguy cơ đột quỵ, nhồi máu",
                "✓ Rẻ tiền (trừ Coversyl)"
            ],
            "side_effects_vn": ["Ho khan (10-15%) - Phổ biến nhất", "Chóng mặt", "Tăng kali máu"],
            "contraindications_vn": ["Thai kỳ", "Hẹp động mạch thận 2 bên"],
            "note_vn": "Thuốc lựa chọn hàng đầu cho tăng huyết áp + tiểu đường"
        },
        "arbs": {
            "name_vn": "Thuốc chẹn thụ thể Angiotensin II (ARBs)",
            "street_name": "Nhóm '-sartan'",
            "examples_vn": ["Losartan", "Valsartan", "Telmisartan", "Irbesartan", "Olmesartan"],
            "vietnam_brands": "🇻🇳 Tại VN: Cozaar (Losartan 50/100mg), Diovan (Valsartan 80/160mg), Aprovel (Irbesartan 150/300mg), Micardis (Telmisartan 40/80mg), Olmetec (Olmesartan 20/40mg)",
            "mechanism_vn": "Giãn mạch máu, bảo vệ thận và tim",
            "benefits_vn": [
                "✓ Giảm huyết áp hiệu quả",
                "✓ KHÔNG gây ho khan (ưu điểm lớn so với ACE-I)",
                "✓ Bảo vệ tim, thận tốt",
                "✓ Ít tác dụng phụ"
            ],
            "side_effects_vn": ["Chóng mặt", "Tăng kali máu", "Ít tác dụng phụ hơn ACE-I"],
            "contraindications_vn": ["Thai kỳ"],
            "note_vn": "Thay thế ACE-I khi bị ho khan. Đắt hơn ACE-I nhưng dễ dung nạp hơn."
        },
        "calcium_blockers": {
            "name_vn": "Thuốc chẹn kênh canxi",
            "street_name": "Nhóm '-dipine' (và Diltiazem, Verapamil)",
            "examples_vn": ["Amlodipine", "Nifedipine", "Diltiazem", "Verapamil", "Lercanidipine"],
            "vietnam_brands": "🇻🇳 Tại VN: Norvasc (Amlodipine 5/10mg), Amlodipine 5/10mg (generic RẺ), Adalat (Nifedipine 30/60mg), Herbesser (Diltiazem 60/90mg), Isoptin (Verapamil 80/120mg), Zanidip (Lercanidipine 10/20mg)",
            "mechanism_vn": "Giãn mạch máu, giảm co thắt",
            "benefits_vn": [
                "✓ Giảm huyết áp mạnh",
                "✓ Phù hợp người cao tuổi, người da đen",
                "✓ Không ảnh hưởng đường huyết (tốt cho tiểu đường)",
                "✓ Amlodipine: RẺ NHẤT trong các thuốc huyết áp hiện đại"
            ],
            "side_effects_vn": ["Phù mắt cá chân (hay gặp)", "Đỏ mặt, nóng mặt", "Táo bón (Verapamil)", "Chóng mặt"],
            "note_vn": "Amlodipine là thuốc huyết áp phổ biến NHẤT tại VN do rẻ và hiệu quả. Phù mắt cá có thể giảm khi phối hợp ACE-I/ARB."
        },
        "diuretics": {
            "name_vn": "Thuốc lợi tiểu",
            "examples_vn": ["Hydrochlorothiazide", "Indapamide", "Furosemide", "Spironolactone"],
            "mechanism_vn": "Thải natri và nước, giảm thể tích tuần hoàn",
            "side_effects_vn": ["Tiểu nhiều", "Giảm kali (cần bổ sung)", "Tăng đường huyết nhẹ"],
            "note_vn": "Thường dùng phối hợp với thuốc khác"
        },
        "beta_blockers": {
            "name_vn": "Thuốc chẹn beta",
            "examples_vn": ["Bisoprolol", "Metoprolol", "Carvedilol", "Atenolol"],
            "mechanism_vn": "Giảm nhịp tim, giảm co bóp tim",
            "side_effects_vn": ["Mệt mỏi", "Chậm nhịp tim", "Giảm ham muốn tình dục"],
            "note_vn": "Phù hợp khi có bệnh tim kèm theo (nhồi máu, suy tim, loạn nhịp)"
        }
    },
    "combination_therapy_vn": [
        "ACE-I/ARB + Lợi tiểu",
        "ACE-I/ARB + Chẹn canxi",
        "Chẹn canxi + Lợi tiểu",
        "Ba thuốc: ACE-I/ARB + Chẹn canxi + Lợi tiểu"
    ],
    "when_to_start_vn": """
- Huyết áp ≥140/90: Cân nhắc dùng thuốc
- Huyết áp ≥160/100: Dùng thuốc ngay + thay đổi lối sống
- Huyết áp ≥180/120: Cấp cứu, dùng thuốc ngay
- Có bệnh lý kèm (tiểu đường, bệnh thận, đột quỵ cũ): Dùng thuốc sớm hơn
"""
}

# ============= CHẾ ĐỘ ĂN UỐNG (DASH DIET) =============

NUTRITION_PLAN = {
    "overview_vn": """
Chế độ ăn DASH (Dietary Approaches to Stop Hypertension) 
được chứng minh giảm huyết áp 8-14 mmHg trong 2-4 tuần.
""",
    "recommended_foods": {
        "grains_vn": [
            "Gạo lứt, gạo nâu (6-8 lượng/ngày)",
            "Yến mạch",
            "Bánh mì nguyên cám",
            "Bột mì nguyên cám"
        ],
        "vegetables_vn": [
            "Rau xanh lá (rau ngót, rau dền, cải bó xôi) - 4-5 lượng/ngày",
            "Bí đao, bí đỏ",
            "Cà chua",
            "Ớt chuông",
            "Cà rót (giảm huyết áp tốt)"
        ],
        "fruits_vn": [
            "Chuối (giàu kali) - 4-5 lượng/ngày",
            "Cam, quýt",
            "Dưa hấu",
            "Táo",
            "Nho"
        ],
        "protein_vn": [
            "Cá (cá hồi, cá thu, cá ngừ) - 2-3 lần/tuần",
            "Gà, ức gà không da",
            "Đậu hũ, đậu phụ",
            "Các loại đậu (đậu đen, đậu đỏ, đậu xanh)",
            "Hạt hướng dương, hạt bí không muối"
        ],
        "dairy_vn": [
            "Sữa ít béo hoặc không béo - 2-3 ly/ngày",
            "Sữa chua không đường",
            "Phô mai ít muối"
        ],
        "healthy_fats_vn": [
            "Dầu ô liu",
            "Bơ (1/4 quả/ngày)",
            "Các loại hạt (óc chó, hạnh nhân, điều) - 1 nắm tay/ngày"
        ]
    },
    "foods_to_avoid": {
        "high_sodium_vn": [
            "🚫 Muối, nước mắm, tương ớt, mì chính",
            "🚫 Đồ ăn nhanh, đồ đóng hộp",
            "🚫 Thịt xông khói, xúc xích, chả lụa",
            "🚫 Dưa chua, muối chua",
            "🚫 Mì gói, snack mặn"
        ],
        "unhealthy_fats_vn": [
            "🚫 Mỡ động vật, da gà, mỡ lợn",
            "🚫 Thực phẩm chiên rán",
            "🚫 Bơ thực vật có hóa cứng",
            "🚫 Bánh ngọt có kem bơ"
        ],
        "sugar_vn": [
            "🚫 Nước ngọt có ga",
            "🚫 Đồ uống có đường",
            "🚫 Bánh kẹo ngọt",
            "🚫 Trà sữa, cà phê đá"
        ],
        "alcohol_vn": [
            "🚫 Bia, rượu (nếu dùng: Nam ≤2 ly/ngày, Nữ ≤1 ly/ngày)"
        ]
    },
    "sodium_limit_vn": """
📊 MỤC TIÊU MUỐI:
- Bình thường: < 5g muối/ngày (< 2000mg natri)
- Tăng huyết áp: < 3g muối/ngày (< 1500mg natri)
- Giai đoạn nặng: < 2g muối/ngày (< 1000mg natri)

💡 Mẹo giảm muối:
✓ Dùng chanh, gừng, tỏi, rau thơm thay muối
✓ Ăn thực phẩm tươi thay đồ đóng hộp
✓ Đọc nhãn thực phẩm (chọn sản phẩm < 120mg natri/100g)
✓ Nấu tại nhà thay ăn ngoài
✓ Rửa đồ hộp dưới nước trước khi ăn
""",
    "meal_examples_vn": {
        "breakfast": [
            "Cháo yến mạch + chuối + sữa tươi ít béo",
            "Bánh mì nguyên cám + trứng luộc + cà chua",
            "Phở gà (ít muối) + rau sống + quýt"
        ],
        "lunch": [
            "Cơm gạo lứt + cá hấp gừng + rau luộc + canh rau",
            "Bún gà + rau thập cẩm + đậu hũ",
            "Cơm + đậu hũ sốt cà chua + rau xào + táo"
        ],
        "dinner": [
            "Cơm + cá kho (ít muối) + rau luộc",
            "Miến gà + rau sống",
            "Cơm + đậu que xào + trứng luộc + dưa hấu"
        ],
        "snacks": [
            "1 nắm hạt không muối",
            "1 quả chuối hoặc táo",
            "Sữa chua không đường + trái cây"
        ]
    }
}

# ============= CHẾ ĐỘ LUYỆN TẬP =============

EXERCISE_PLAN = {
    "overview_vn": """
Vận động đều đặn giảm huyết áp 5-8 mmHg.
Mục tiêu: 150 phút vận động vừa phải/tuần (30 phút x 5 ngày).
""",
    "recommended_exercises": {
        "aerobic_vn": {
            "name": "Vận động nhịp điệu (Aerobic)",
            "examples": [
                "Đi bộ nhanh (5-6 km/h)",
                "Chạy bộ nhẹ",
                "Bơi lội",
                "Đạp xe",
                "Khiêu vũ",
                "Thể dục nhịp điệu"
            ],
            "frequency": "5-7 ngày/tuần",
            "duration": "30-60 phút/lần",
            "intensity_vn": "Vừa phải (có thể nói chuyện nhưng không hát được)",
            "benefit_vn": "Giảm huyết áp, tăng sức bền, giảm cân"
        },
        "resistance_vn": {
            "name": "Tập kháng lực (Resistance)",
            "examples": [
                "Tập tạ nhẹ",
                "Squat (ngồi xổm đứng lên)",
                "Chống đẩy",
                "Plank",
                "Dây kháng lực"
            ],
            "frequency": "2-3 ngày/tuần",
            "duration": "20-30 phút/lần",
            "sets": "2-3 hiệp x 10-15 lần",
            "benefit_vn": "Tăng cơ, giảm mỡ, cải thiện chuyển hóa"
        },
        "flexibility_vn": {
            "name": "Vận động mềm dẻo & Thư giãn",
            "examples": [
                "Yoga",
                "Tai chi",
                "Khí công",
                "Giãn cơ (stretching)"
            ],
            "frequency": "Hàng ngày",
            "duration": "10-15 phút",
            "benefit_vn": "Giảm stress, cải thiện tuần hoàn, giảm huyết áp"
        }
    },
    "safety_guidelines_vn": [
        "✅ Khởi động 5-10 phút trước tập",
        "✅ Hạ nhiệt 5-10 phút sau tập",
        "✅ Uống nước đủ trước, trong và sau tập",
        "✅ Tránh tập khi huyết áp >180/110",
        "✅ Ngừng ngay nếu có đau ngực, chóng mặt, khó thở",
        "⚠️ Hỏi bác sĩ trước khi bắt đầu nếu huyết áp ≥160/100",
        "⚠️ Tránh nín thở khi tập tạ (gây tăng huyết áp đột ngột)",
        "⚠️ Tránh tập quá sức (mục tiêu là vừa sức)"
    ],
    "target_heart_rate_vn": """
📊 NHỊP TIM MỤC TIÊU KHI TẬP:
- Nhịp tim tối đa = 220 - tuổi
- Vùng an toàn: 50-70% nhịp tim tối đa

Ví dụ: Người 50 tuổi
- Nhịp tim tối đa = 220 - 50 = 170
- Vùng an toàn = 85 - 119 nhịp/phút

💡 Cách kiểm tra: Đếm mạch 15 giây x 4
"""
}

# ============= LỐI SỐNG & QUẢN LÝ STRESS =============

LIFESTYLE_MODIFICATIONS = {
    "weight_management_vn": """
📊 QUẢN LÝ CÂN NẶNG:
- Giảm 5-10 kg có thể giảm huyết áp 5-20 mmHg
- BMI mục tiêu: 18.5 - 22.9 (người châu Á)
- Vòng eo: Nam < 90cm, Nữ < 80cm

Cách tính BMI = Cân nặng (kg) / [Chiều cao (m)]²
""",
    "stress_management_vn": [
        "Thiền định 10-20 phút/ngày",
        "Hít thở sâu (4-7-8: Hít 4s, Giữ 7s, Thở ra 8s)",
        "Ngủ đủ 7-8 giờ/đêm",
        "Dành thời gian cho sở thích",
        "Kết nối với gia đình, bạn bè",
        "Tránh làm việc quá sức",
        "Cân nhắc tham gia nhóm hỗ trợ"
    ],
    "quit_smoking_vn": """
🚭 CÁI NGHIỆN THUỐC LÁ:
- Hút thuốc làm tăng nguy cơ đột quỵ, nhồi máu tim gấp 2-4 lần
- Bỏ thuốc giảm huyết áp 5-10 mmHg trong vài tuần
- Nhờ hỗ trợ: Tư vấn + Thuốc cai nghiện (nếu cần)
- Đường dây hỗ trợ: 1800 6652 (miễn phí)
""",
    "limit_alcohol_vn": """
🍺 GIỚI HẠN RƯỢU BIA:
- Nam: ≤ 2 ly tiêu chuẩn/ngày (≤ 2 lon bia/ngày)
- Nữ: ≤ 1 ly tiêu chuẩn/ngày (≤ 1 lon bia/ngày)
- Tốt nhất: KHÔNG uống

Uống nhiều làm tăng huyết áp và giảm hiệu quả thuốc.
""",
    "monitoring_vn": """
📱 THEO DÕI TẠI NHÀ:
- Đo huyết áp 2 lần/ngày (sáng và tối)
- Ghi chép vào sổ hoặc app
- Đo đúng cách:
  ✓ Ngồi nghỉ 5 phút trước khi đo
  ✓ Không uống cà phê/thuốc lá 30 phút trước
  ✓ Không nói chuyện khi đo
  ✓ Đo cùng thời điểm mỗi ngày
  ✓ Đo 2-3 lần, lấy trung bình

- Mang sổ ghi khi khám bác sĩ
"""
}

# ============= KHI NÀO CẦN GẶP BÁC SĨ =============

WHEN_TO_SEE_DOCTOR = {
    "emergency_vn": [
        "🚨 Huyết áp > 180/120 mmHg",
        "🚨 Đau ngực",
        "🚨 Khó thở nghiêm trọng",
        "🚨 Đau đầu dữ dội",
        "🚨 Yếu liệt, tê bì nửa người",
        "🚨 Nói khó, méo miệng",
        "🚨 Nhìn mờ đột ngột",
        "🚨 Co giật"
    ],
    "urgent_vn": [
        "⚠️ Huyết áp liên tục > 160/100 mmHg",
        "⚠️ Tác dụng phụ thuốc nghiêm trọng",
        "⚠️ Huyết áp không giảm sau 3 tháng điều trị"
    ],
    "routine_vn": [
        "✓ Tái khám định kỳ 1-3 tháng/lần (theo chỉ định)",
        "✓ Xét nghiệm máu mỗi năm",
        "✓ Thay đổi thuốc hoặc liều (chỉ theo bác sĩ)"
    ]
}

# ============= CHATBOT CONVERSATION FLOW =============

CONVERSATION_STEPS = [
    {
        "step": 1,
        "question_vn": "Xin chào! Tôi là trợ lý sức khỏe về Tăng Huyết Áp. Bạn đã đo huyết áp gần đây chưa? Nếu có, chỉ số là bao nhiêu?",
        "question_en": "Hello! I'm a hypertension health assistant. Have you measured your blood pressure recently? If yes, what was the reading?",
        "follow_up_vn": ["Đo tại nhà", "Đo tại phòng khám", "Chưa đo"]
    },
    {
        "step": 2,
        "question_vn": "Bạn có triệu chứng nào sau đây không?\n- Đau đầu thường xuyên\n- Chóng mặt\n- Mệt mỏi\n- Chảy máu cam\n- Khó thở khi gắng sức",
        "question_en": "Do you have any of these symptoms?\n- Frequent headache\n- Dizziness\n- Fatigue\n- Nosebleeds\n- Shortness of breath with exertion"
    },
    {
        "step": 3,
        "question_vn": "Bạn có yếu tố nguy cơ nào?\n- Tiền sử gia đình có THA\n- Béo phì\n- Ăn mặn\n- Ít vận động\n- Hút thuốc, uống rượu",
        "question_en": "Do you have any risk factors?\n- Family history of hypertension\n- Obesity\n- High salt diet\n- Sedentary lifestyle\n- Smoking, alcohol use"
    },
    {
        "step": 4,
        "question_vn": "Bạn đang dùng thuốc gì cho huyết áp không? (nếu có, cho tôi biết tên thuốc)",
        "question_en": "Are you currently taking any blood pressure medications? (If yes, please tell me the names)"
    },
    {
        "step": 5,
        "question_vn": "Bạn muốn tư vấn về:\n1️⃣ Chế độ ăn uống\n2️⃣ Chế độ luyện tập\n3️⃣ Thuốc điều trị\n4️⃣ Cách theo dõi tại nhà\n5️⃣ Khi nào cần gặp bác sĩ",
        "question_en": "What would you like to know about:\n1️⃣ Diet\n2️⃣ Exercise\n3️⃣ Medications\n4️⃣ Home monitoring\n5️⃣ When to see a doctor"
    }
]

