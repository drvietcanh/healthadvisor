"""
Hypertension Medications
Complete guide to blood pressure medications and combination therapy
"""

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
            "street_name": "Thuốc tăng tiểu",
            "examples_vn": ["Hydrochlorothiazide (HCTZ)", "Indapamide", "Furosemide", "Spironolactone"],
            "vietnam_brands": "🇻🇳 Tại VN: Natrilix SR (Indapamide 1.5mg), Fludex (Indapamide 2.5mg), Lasix (Furosemide 40mg), Aldactone (Spironolactone 25/100mg), Co-Diovan (Valsartan + HCTZ), Exforge HCT (Amlodipine + Valsartan + HCTZ)",
            "mechanism_vn": "Thải natri và nước qua thận, giảm thể tích tuần hoàn → Giảm huyết áp",
            "benefits_vn": [
                "✓ Giảm huyết áp hiệu quả",
                "✓ Rẻ tiền (đặc biệt HCTZ)",
                "✓ Tốt khi phối hợp với thuốc khác",
                "✓ Giảm phù (nếu có)",
                "✓ Indapamide: Ít tác dụng phụ hơn HCTZ"
            ],
            "side_effects_vn": [
                "Tiểu nhiều (đặc biệt ban đầu)",
                "Giảm kali máu (quan trọng! Cần theo dõi)",
                "Tăng đường huyết nhẹ",
                "Tăng acid uric (gút)",
                "Khô miệng, khát nước"
            ],
            "note_vn": "Thường dùng PHỐI HỢP với ACE-I/ARB hoặc chẹn canxi. Hiệu quả tốt nhất khi dùng liều thấp kết hợp.",
            "tips_vn": [
                "💡 Uống vào buổi sáng (tránh tiểu đêm)",
                "💡 Ăn nhiều chuối, cam (bổ sung kali)",
                "💡 Theo dõi kali máu định kỳ",
                "⚠️ Tránh nếu có gút hoặc đang dùng thuốc chống gút"
            ]
        },
        "beta_blockers": {
            "name_vn": "Thuốc chẹn beta",
            "street_name": "Nhóm '-olol'",
            "examples_vn": ["Bisoprolol", "Metoprolol", "Carvedilol", "Atenolol", "Nebivolol"],
            "vietnam_brands": "🇻🇳 Tại VN: Concor (Bisoprolol 2.5/5/10mg), Betaloc ZOK (Metoprolol 50/100mg), Dilatrend (Carvedilol 6.25/12.5/25mg), Tenormin (Atenolol 50/100mg), Nebilet (Nebivolol 5mg)",
            "mechanism_vn": "Giảm nhịp tim, giảm co bóp tim, giảm gánh nặng tim",
            "benefits_vn": [
                "✓ Giảm huyết áp",
                "✓ Bảo vệ tim (sau nhồi máu cơ tim)",
                "✓ Kiểm soát nhịp tim (loạn nhịp)",
                "✓ Giảm tử vong ở bệnh suy tim",
                "✓ Giảm lo âu (tác dụng phụ tốt!)"
            ],
            "side_effects_vn": [
                "Mệt mỏi (hay gặp)",
                "Chậm nhịp tim (< 60 lần/phút)",
                "Giảm ham muốn tình dục",
                "Tay chân lạnh",
                "Khó thở (nếu có hen suyễn)"
            ],
            "contraindications_vn": [
                "⚠️ Hen suyễn, COPD nặng",
                "⚠️ Nhịp tim < 50 lần/phút",
                "⚠️ Suy tim cấp chưa kiểm soát"
            ],
            "note_vn": "KHÔNG phải thuốc hàng đầu cho tăng huyết áp đơn thuần. Dùng khi có: tim đập nhanh, sau nhồi máu, suy tim, loạn nhịp.",
            "tips_vn": [
                "💡 KHÔNG TỰ Ý NGỪNG ĐỘT NGỘT! (nguy hiểm)",
                "💡 Phải giảm liều từ từ khi ngừng",
                "💡 Đo mạch thường xuyên",
                "⚠️ Tránh nếu có hen suyễn"
            ]
        }
    },
    "combination_therapy_vn": [
        "ACE-I/ARB + Lợi tiểu",
        "ACE-I/ARB + Chẹn canxi",
        "Chẹn canxi + Lợi tiểu",
        "Ba thuốc: ACE-I/ARB + Chẹn canxi + Lợi tiểu"
    ],
    
    "combination_drugs_vietnam": {
        "why_vn": """
💊 TẠI SAO DÙNG THUỐC PHỐI HỢP?

✅ Tiện lợi: Uống 1 viên thay vì 2-3 viên
✅ Dễ tuân thủ: Ít viên → ít quên
✅ Hiệu quả tốt hơn: 2 thuốc phối hợp > 1 thuốc liều cao
✅ Ít tác dụng phụ: Dùng liều thấp mỗi thuốc
""",
        "common_combinations": [
            {
                "name": "Co-Diovan (Valsartan + HCTZ)",
                "formula": "ARB + Lợi tiểu",
                "strengths": "80/12.5mg, 160/12.5mg, 160/25mg",
                "price": "Đắt",
                "verdict": "✅ Phổ biến, hiệu quả tốt"
            },
            {
                "name": "Exforge (Amlodipine + Valsartan)",
                "formula": "Chẹn canxi + ARB",
                "strengths": "5/80mg, 5/160mg, 10/160mg",
                "price": "Đắt",
                "verdict": "✅ Rất hiệu quả, giảm phù chân (so với Amlodipine đơn)"
            },
            {
                "name": "Exforge HCT (Amlodipine + Valsartan + HCTZ)",
                "formula": "Chẹn canxi + ARB + Lợi tiểu (3 thuốc!)",
                "strengths": "5/160/12.5mg, 10/160/12.5mg, 10/160/25mg",
                "price": "Rất đắt",
                "verdict": "✅ Cho huyết áp rất cao, cần 3 thuốc"
            },
            {
                "name": "Norvasc Combi (Amlodipine + Atorvastatin)",
                "formula": "Chẹn canxi + Statin (hạ mỡ máu)",
                "strengths": "5/10mg, 5/20mg, 10/10mg, 10/20mg",
                "price": "Đắt",
                "verdict": "✅ Tốt nếu có cả huyết áp cao + mỡ máu cao"
            },
            {
                "name": "Triplixam (Perindopril + Indapamide + Amlodipine)",
                "formula": "ACE-I + Lợi tiểu + Chẹn canxi (3 thuốc!)",
                "strengths": "5/1.25/5mg, 5/1.25/10mg, 10/2.5/5mg, 10/2.5/10mg",
                "price": "Rất đắt",
                "verdict": "✅ Rất mạnh, cho huyết áp khó kiểm soát"
            },
            {
                "name": "Coveram (Perindopril + Amlodipine)",
                "formula": "ACE-I + Chẹn canxi",
                "strengths": "5/5mg, 5/10mg, 10/5mg, 10/10mg",
                "price": "Đắt",
                "verdict": "✅ Phổ biến, hiệu quả, ít ho hơn Coversyl đơn"
            },
            {
                "name": "Bi-Preterax N (Perindopril + Indapamide)",
                "formula": "ACE-I + Lợi tiểu",
                "strengths": "5/1.25mg, 10/2.5mg",
                "price": "Trung bình",
                "verdict": "✅ Phổ biến nhất tại VN, giá tốt hơn các thuốc phối hợp khác"
            },
            {
                "name": "Amlosafe-AT (Amlodipine + Atenolol)",
                "formula": "Chẹn canxi + Beta-blocker",
                "strengths": "5/50mg",
                "price": "Rẻ",
                "verdict": "⚠️ Tốt nếu tim đập nhanh, nhưng cẩn thận beta-blocker"
            }
        ],
        "tips_vn": """
💡 LỰA CHỌN THUỐC PHỐI HỢP:

1️⃣ NẾU NGÂN SÁCH HẠN CHẾ:
   → Bi-Preterax N (Perindopril + Indapamide)
   → Hoặc mua Amlodipine generic + Enalapril riêng (rẻ nhất!)

2️⃣ NẾU CÓ TIỂU ĐƯỜNG:
   → Exforge (Amlodipine + Valsartan)
   → Coveram (Perindopril + Amlodipine)

3️⃣ NẾU CÓ PHÙ CHÂN khi dùng Amlodipine:
   → Chuyển sang Exforge (thêm ARB giảm phù)
   → Hoặc Bi-Preterax N (không có Amlodipine)

4️⃣ NẾU HUYẾT ÁP RẤT CAO (≥ 160/100):
   → Triplixam hoặc Exforge HCT (3 thuốc)

5️⃣ NẾU CÓ MỠ MÁU CAO:
   → Norvasc Combi (Amlodipine + Statin)

⚠️ LƯU Ý: Thuốc phối hợp ĐẮT HƠN nhưng TIỆN HƠN!
"""
    },
    "when_to_start_vn": """
- Huyết áp ≥140/90: Cân nhắc dùng thuốc
- Huyết áp ≥160/100: Dùng thuốc ngay + thay đổi lối sống
- Huyết áp ≥180/120: Cấp cứu, dùng thuốc ngay
- Có bệnh lý kèm (tiểu đường, bệnh thận, đột quỵ cũ): Dùng thuốc sớm hơn
"""
}

