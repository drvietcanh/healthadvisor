"""
Thuốc điều trị Tiểu Đường - Thuốc uống & GLP-1
Bao gồm: Metformin, Sulfonylureas, DPP-4i, SGLT-2i, GLP-1, Acarbose, Thiazolidinediones
"""

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
            "brand_names": "Glucophage (Pháp) 🇫🇷, Merckformin (Đức) 🇩🇪, Diabetmin, Gluformin, Metforal",
            "vietnam_brands": "🇻🇳 Tại VN: Glucophage 500/850/1000mg, Merckformin 500/850mg, Gluformin 500mg, Diabetmin 500mg, Metforal 500/850mg",
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
            "brand_names": "Glimepiride (Amaryl), Gliclazide (Diamicron MR), Glipizide",
            "vietnam_brands": "🇻🇳 Tại VN: Amaryl 1/2/3/4mg, Glimestad 2/4mg, Diamicron MR 30/60mg, Glicab MR 30mg, Glipizide 5mg",
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
            "brand_names": "Sitagliptin (Januvia), Vildagliptin (Galvus), Saxagliptin (Onglyza), Linagliptin (Trajenta)",
            "vietnam_brands": "🇻🇳 Tại VN: Januvia 50/100mg, Galvus 50mg, Onglyza 5mg, Trajenta 5mg, Kombiglyze (phối hợp)",
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
            "brand_names": "Dapagliflozin (Forxiga), Empagliflozin (Jardiance), Canagliflozin (Invokana)",
            "vietnam_brands": "🇻🇳 Tại VN: Forxiga 5/10mg, Jardiance 10/25mg, Invokana 100/300mg, Qtern (phối hợp)",
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
        },
        {
            "class": "GLP-1 agonists",
            "street_name": "Thuốc tiêm giảm cân",
            "brand_names": "Liraglutide (Victoza, Saxenda), Semaglutide (Ozempic, Wegovy), Dulaglutide (Trulicity)",
            "vietnam_brands": "🇻🇳 Tại VN: Victoza 6mg/ml bút tiêm, Ozempic 0.25/0.5/1mg bút tiêm, Trulicity 0.75/1.5mg bút tiêm, Saxenda (giảm cân)",
            "what_it_does": "Kích thích tiết insulin, làm chậm tiêu hóa, giảm thèm ăn",
            "benefits_vn": [
                "✓ Giảm đường huyết mạnh",
                "✓ GIẢM CÂN nhiều (5-10kg) 🌟",
                "✓ Bảo vệ tim mạch",
                "✓ Giảm nguy cơ đột quỵ, nhồi máu",
                "✓ Không gây hạ đường huyết"
            ],
            "how_to_take": [
                "💉 Tiêm dưới da 1 lần/tuần (Ozempic, Trulicity)",
                "💉 Hoặc 1 lần/ngày (Victoza)",
                "📍 Tiêm vào bụng, đùi hoặc cánh tay"
            ],
            "side_effects": [
                "Buồn nôn, nôn (thường giảm sau 2-4 tuần)",
                "Chán ăn (tốt cho giảm cân!)",
                "Tiêu chảy hoặc táo bón",
                "Đầy hơi"
            ],
            "tips_vn": [
                "💡 Bắt đầu liều thấp, tăng dần",
                "💡 Ăn bữa nhỏ, nhiều lần",
                "💡 Tránh thức ăn nhiều dầu mỡ",
                "⚠️ Rất đắt (2-5 triệu/tháng)",
                "🌟 Ozempic/Wegovy nổi tiếng giảm cân"
            ]
        },
        {
            "class": "Alpha-glucosidase inhibitors",
            "street_name": "Thuốc chặn hấp thu đường",
            "brand_names": "Acarbose (Glucobay), Miglitol, Voglibose",
            "vietnam_brands": "🇻🇳 Tại VN: Glucobay 50/100mg, Acarbose 50/100mg (generic), Voglibose 0.2/0.3mg",
            "what_it_does": "Làm chậm hấp thu carb từ ruột → Đường không tăng vọt sau ăn",
            "benefits_vn": [
                "✓ Giảm đường sau ăn",
                "✓ Không gây hạ đường huyết",
                "✓ Không tăng cân",
                "✓ Rẻ tiền"
            ],
            "how_to_take": [
                "💊 Uống CÙNG MIẾNG ĂN ĐẦU TIÊN (quan trọng!)",
                "⏰ Uống trước bữa ăn 1-2 phút",
                "📅 Thường 3 lần/ngày (3 bữa chính)"
            ],
            "side_effects": [
                "Đầy hơi, chướng bụng (rất hay gặp)",
                "Tiêu chảy",
                "Đau bụng"
            ],
            "tips_vn": [
                "💡 Bắt đầu liều thấp để giảm đầy hơi",
                "💡 Ăn ít carb → Ít tác dụng phụ",
                "⚠️ Không dùng nếu có bệnh ruột"
            ]
        },
        {
            "class": "Thiazolidinediones",
            "street_name": "Nhóm '-glitazone'",
            "brand_names": "Pioglitazone (Actos, Glustin)",
            "vietnam_brands": "🇻🇳 Tại VN: Actos 15/30mg, Pioglitazone 15/30mg (generic), Competact (phối hợp metformin)",
            "what_it_does": "Tăng độ nhạy insulin ở cơ, mỡ",
            "benefits_vn": [
                "✓ Giảm kháng insulin",
                "✓ Bảo vệ tế bào beta tụy",
                "✓ Cải thiện mỡ máu (HDL tăng)"
            ],
            "how_to_take": [
                "💊 Uống 1 lần/ngày",
                "🍽️ Có thể uống đói hoặc no"
            ],
            "side_effects": [
                "Tăng cân (2-4kg) - do giữ nước",
                "Phù chân",
                "Tăng nguy cơ gãy xương (phụ nữ)",
                "Suy tim (nếu có bệnh tim sẵn)"
            ],
            "tips_vn": [
                "⚠️ KHÔNG dùng nếu có suy tim",
                "⚠️ Hiện ít dùng (có thuốc tốt hơn)",
                "💡 Cân nặng + theo dõi phù"
            ]
        }
    ]
}

