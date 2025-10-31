"""
Other Medications - Các thuốc điều trị mỡ máu khác
"""

OTHER_MEDICATIONS = {
    "ezetimibe": {
        "name": "Ezetimibe (Ezetrol, Zetia)",
        "vietnamese_brands": ["Ezetrol", "Ezetimibe"],
        "type": "Ức chế hấp thu cholesterol",
        "how_it_works": "Ngăn ruột hấp thu cholesterol từ thức ăn",
        "dosage": "10 mg/ngày",
        "effects": [
            "↓ LDL thêm 15-20% (khi kết hợp Statin)",
            "↓ LDL 18% (đơn độc)"
        ],
        "cost": "150,000-300,000đ/tháng",
        "when_to_use": [
            "LDL vẫn cao dù đã dùng Statin liều cao",
            "Kết hợp Statin để tăng hiệu quả",
            "Không dung nạp Statin liều cao"
        ],
        "side_effects": "Ít tác dụng phụ, an toàn",
        "note": "Thường KẾT HỢP Statin, ít khi dùng đơn độc"
    },
    
    "omega3": {
        "name": "Omega-3 (EPA/DHA)",
        "vietnamese_brands": ["Dầu cá Omega-3", "EPA-E"],
        "type": "Bổ sung dầu cá",
        "dosage": "2-4 gram EPA+DHA/ngày",
        "effects": [
            "↓ Triglyceride: 20-30% (liều cao)",
            "↑ HDL nhẹ",
            "Chống viêm, chống huyết khối"
        ],
        "cost": "100,000-400,000đ/tháng",
        "when_to_use": [
            "Triglyceride cao (>200 mg/dL hay 2.3 mmol/L)",
            "Bổ sung cho Statin/Fibrate"
        ],
        "note": "ĂN CÁ BÉO (cá thu, hồi) TỰ NHIÊN TỐT HƠN! Viên uống chỉ là bổ sung."
    },
    
    "pcsk9_inhibitors": {
        "name": "PCSK9 Inhibitors (Evolocumab, Alirocumab)",
        "type": "Thuốc tiêm sinh học (rất đắt)",
        "vietnamese_brands": ["Repatha (Evolocumab)", "Praluent (Alirocumab)"],
        "effects": [
            "↓ LDL: 50-60% (MẠNH!)",
            "Giảm nguy cơ nhồi máu tim, đột quỵ 15-20%"
        ],
        "dosage": "Tiêm dưới da 1-2 lần/tháng",
        "cost": "20-50 TRIỆU đồng/tháng (CỰC ĐẮT!)",
        "when_to_use": [
            "LDL CỰC CAO (gia đình tăng cholesterol di truyền)",
            "Đã nhồi máu tim + LDL vẫn cao dù dùng Statin liều cao + Ezetimibe",
            "Không dung nạp Statin"
        ],
        "availability": "Rất ít tại VN, chỉ bệnh viện lớn (BV Chợ Rẫy, Bạch Mai)",
        "note": "CHỈ cho trường hợp đặc biệt, rất nặng. Cần chỉ định bác sĩ chuyên khoa"
    },
    
    "inclisiran": {
        "name": "Inclisiran (Leqvio) - THUỐC MỚI 2020-2022",
        "type": "Thuốc tiêm siRNA (ức chế PCSK9)",
        "vietnamese_brands": ["Leqvio", "Inclisiran"],
        "how_it_works": "Ức chế tạo PCSK9 ở gan bằng công nghệ siRNA → Giảm LDL lâu dài",
        "effects": [
            "↓ LDL: 50% (tương đương PCSK9 inhibitors)",
            "Tác dụng kéo dài (tiêm 2 lần/năm!)"
        ],
        "dosage": "Tiêm dưới da 2 lần/năm (6 tháng/lần) - TIỆN LỢI NHẤT!",
        "cost": "15-40 TRIỆU đồng/năm (đắt nhưng tiện)",
        "when_to_use": [
            "LDL vẫn cao dù dùng Statin + Ezetimibe",
            "Không dung nạp Statin",
            "Cần giảm LDL mạnh nhưng muốn tiêm ít lần"
        ],
        "side_effects": "Ít tác dụng phụ, an toàn hơn PCSK9 mAbs",
        "availability": "Mới có tại VN (2023-2024), rất ít nơi có",
        "note": "🌟 THUỐC MỚI NHẤT - Chỉ tiêm 2 lần/năm, rất tiện! Chưa phổ biến tại VN"
    },
    
    "bempedoic_acid": {
        "name": "Bempedoic Acid (Nexletol) - THUỐC MỚI 2020",
        "type": "Thuốc uống giảm cholesterol (không phải Statin)",
        "vietnamese_brands": ["Nexletol", "Bempedoic acid"],
        "how_it_works": "Ức chế enzyme ở gan (giống Statin nhưng cơ chế khác)",
        "effects": [
            "↓ LDL: 15-25% (đơn độc)",
            "↓ LDL: 35-40% (kết hợp Ezetimibe)",
            "KHÔNG gây đau cơ (ưu điểm lớn so với Statin)"
        ],
        "dosage": "180mg/ngày, uống với thức ăn",
        "cost": "Chưa có tại VN (mới FDA 2020)",
        "when_to_use": [
            "Không dung nạp Statin (đau cơ nhiều)",
            "Cần thuốc uống giảm LDL (không muốn tiêm)",
            "Kết hợp với Ezetimibe để tăng hiệu quả"
        ],
        "side_effects": [
            "Tăng acid uric (gút) - 2-3%",
            "Tăng nguy cơ viêm gân",
            "Ít tác dụng phụ khác"
        ],
        "availability": "Chưa có tại VN",
        "note": "🌟 LỰA CHỌN MỚI cho người không dung nạp Statin. Chưa có tại VN"
    },
    
    "bempedoic_ezetimibe": {
        "name": "Bempedoic Acid + Ezetimibe (Nexlizet) - THUỐC PHỐI HỢP MỚI",
        "type": "Thuốc phối hợp uống",
        "effects": [
            "↓ LDL: 35-40%",
            "Tiện lợi: 1 viên thay vì 2 viên"
        ],
        "dosage": "1 viên/ngày, với thức ăn",
        "cost": "Chưa có tại VN",
        "when_to_use": [
            "Không dung nạp Statin",
            "Cần giảm LDL vừa phải, không muốn tiêm"
        ],
        "availability": "Chưa có tại VN",
        "note": "🌟 Kết hợp 2 thuốc uống trong 1 viên - tiện lợi"
    },
    
    "icosapent_ethyl": {
        "name": "Icosapent Ethyl (Vascepa) - Omega-3 tinh khiết",
        "type": "Omega-3 tinh khiết (EPA)",
        "vietnamese_brands": ["Vascepa", "Icosapent ethyl"],
        "how_it_works": "EPA tinh khiết liều cao - khác với dầu cá thông thường",
        "effects": [
            "↓ Triglyceride: 20-30%",
            "Giảm nguy cơ biến cố tim mạch 25% (quan trọng!)",
            "Đặc biệt tốt cho người đã có bệnh tim + TG cao"
        ],
        "dosage": "2g x 2 lần/ngày (4g/ngày) với bữa ăn",
        "cost": "1-2 triệu đồng/tháng",
        "when_to_use": [
            "Đã nhồi máu tim/đột quỵ + Triglyceride 1.5-5.6 mmol/L",
            "Đang dùng Statin nhưng TG vẫn cao",
            "Muốn giảm thêm nguy cơ tim mạch"
        ],
        "side_effects": "Ít, an toàn",
        "availability": "Có tại VN nhưng ít",
        "note": "🌟 ĐẶC BIỆT: Giảm nguy cơ tim mạch, không chỉ giảm TG. Dùng cho người đã có bệnh tim"
    }
}

