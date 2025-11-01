"""
Gout Treatment - Điều trị bệnh Gút
"""

GOUT_TREATMENT = {
    "title": "💊 Điều Trị Bệnh Gút",
    
    "acute_attack": {
        "title": "1️⃣ Điều Trị Cơn Gút Cấp:",
        "goal": "Giảm đau, viêm NGAY LẬP TỨC",
        "medications": [
            {
                "drug": "Colchicine",
                "dose": "0.5mg, 2-3 lần/ngày (bắt đầu sớm!)",
                "when": "Dùng trong 24h đầu → Hiệu quả tốt nhất",
                "note": "Thuốc đặc hiệu cho gút, nhưng có tác dụng phụ tiêu chảy"
            },
            {
                "drug": "NSAIDs (Ibuprofen, Diclofenac, Naproxen)",
                "dose": "Liều cao, theo chỉ định",
                "when": "Dùng sớm khi đau",
                "note": "Uống sau ăn, tránh dạ dày. Không dùng nếu suy thận"
            },
            {
                "drug": "Corticosteroid (Prednisone)",
                "dose": "20-40mg/ngày, giảm dần",
                "when": "Không dung nạp Colchicine/NSAIDs",
                "note": "Hiệu quả nhanh, nhưng có tác dụng phụ"
            }
        ],
        "other_measures": [
            "Nghỉ ngơi, nâng cao khớp",
            "Chườm lạnh (không chườm nóng!)",
            "Uống nhiều nước (3-4 lít/ngày)",
            "TRÁNH rượu bia, thức ăn nhiều purine"
        ]
    },
    
    "long_term": {
        "title": "2️⃣ Điều Trị Lâu Dài (Ngăn tái phát):",
        "goal": "Giảm acid uric máu < 6 mg/dL (≈ 0.3 mmol/L, 360 μmol/L)",
        "when_start": [
            ">2 cơn gút/năm",
            "Có hạt tophi",
            "Có sỏi thận do acid uric",
            "Acid uric > 8 mg/dL (≈ > 0.5 mmol/L) dù chưa có cơn"
        ],
        "medications": {
            "allopurinol": {
                "drug": "Allopurinol",
                "dose": "100-600mg/ngày (bắt đầu 100mg, tăng dần)",
                "mechanism": "Ngăn tạo acid uric",
                "note": "Thuốc số 1, rẻ, an toàn. Uống hàng ngày suốt đời"
            },
            "febuxostat": {
                "drug": "Febuxostat",
                "dose": "40-80mg/ngày",
                "mechanism": "Ngăn tạo acid uric",
                "note": "Đắt hơn Allopurinol, dùng khi không dung nạp Allopurinol"
            },
            "probenecid": {
                "drug": "Probenecid",
                "mechanism": "Tăng thải acid uric qua thận",
                "note": "Chỉ dùng khi thận tốt, không có sỏi thận"
            },
            "benzbromarone": {
                "drug": "Benzbromarone",
                "mechanism": "Tăng thải acid uric",
                "note": "Hiệu quả nhưng ít dùng do độc gan"
            }
        },
        "important": "⚠️ Khi bắt đầu thuốc hạ acid uric → Có thể tăng cơn gút (tinh thể tan ra). Dùng Colchicine dự phòng 3-6 tháng!"
    }
}

GOUT_MEDICATIONS = {
    "treatment_principle": """
Điều trị gút có 2 giai đoạn:
1. CẮT CƠN (Khi đang đau) → Dùng Colchicine/NSAIDs
2. DỰ PHÒNG (Ngăn tái phát) → Dùng Allopurinol/Febuxostat

⚠️ KHÔNG dùng Allopurinol khi đang có cơn đau! → Làm nặng thêm!
    """,
    
    "monitoring": [
        "Xét nghiệm acid uric máu: Mục tiêu < 6 mg/dL (≈ 0.3 mmol/L, 360 μmol/L)",
        "Xét nghiệm định kỳ: Gan, thận, máu (mỗi 3-6 tháng)",
        "Theo dõi số cơn gút (giảm dần khi điều trị đúng)",
        "Theo dõi hạt tophi (nhỏ dần, mất sau 1-2 năm)"
    ],
    
    "side_effects": {
        "colchicine": [
            "Tiêu chảy, buồn nôn (phổ biến)",
            "Giảm liều nếu tiêu chảy",
            "Không dùng nếu suy thận nặng"
        ],
        "allopurinol": [
            "Phát ban da (1-5%)",
            "Dị ứng nặng (HIẾM nhưng nguy hiểm)",
            "Tăng cơn gút khi mới bắt đầu (dùng Colchicine dự phòng)",
            "Tăng men gan nhẹ"
        ]
    }
}

GOUT_PREVENTION = {
    "title": "🛡️ Phòng Ngừa Bệnh Gút",
    
    "lifestyle": [
        "⚖️ Giảm cân (nếu thừa cân)",
        "💧 Uống nhiều nước (2-3 lít/ngày)",
        "🚫 Tránh rượu bia (đặc biệt bia!)",
        "🍎 Ăn nhiều rau, trái cây",
        "🏃 Tập thể dục đều đặn",
        "😴 Ngủ đủ giấc"
    ],
    
    "diet_tips": [
        "Giảm thịt đỏ (<150g/ngày)",
        "Tránh nội tạng, hải sản",
        "Hạn chế nước ngọt có đường",
        "Ăn sữa ít béo, anh đào",
        "Uống cà phê (nếu không có vấn đề tim mạch)"
    ],
    
    "medication_adherence": [
        "Dùng thuốc hạ acid uric ĐỀU ĐẶN, không bỏ",
        "Mục tiêu: Acid uric < 6 mg/dL (≈ 0.3 mmol/L)",
        "Theo dõi định kỳ với bác sĩ",
        "Dùng Colchicine dự phòng khi mới bắt đầu thuốc hạ acid uric"
    ],
    
    "warning": """
⚠️ Nhiều người bỏ thuốc sau khi hết đau → Sai lầm!
- Bỏ thuốc → Acid uric tăng lại → Tái phát
- Phải dùng thuốc HÀNG NGÀY, SUỐT ĐỜI (như huyết áp, tiểu đường)
    """
}

