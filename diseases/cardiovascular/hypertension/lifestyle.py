"""
Hypertension Lifestyle Management
DASH diet, exercise plan, lifestyle modifications, and monitoring
"""

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

