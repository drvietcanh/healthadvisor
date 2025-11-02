"""
Colitis - Điều trị
"""

TREATMENT = {
    "infectious_colitis": {
        "title": "💊 Điều trị viêm đại tràng nhiễm trùng:",
        "medications": [
            "Kháng sinh (nếu do vi khuẩn): Metronidazole, Ciprofloxacin",
            "Bù nước: Oresol, nước lọc",
            "Thuốc giảm đau: Paracetamol"
        ],
        "diet": [
            "Cháo loãng, súp (khi đang tiêu chảy)",
            "Tránh: Rau sống, đồ cay, sữa (nếu không dung nạp)",
            "Khi đỡ: Ăn bình thường, thêm sữa chua"
        ],
        "duration": "Vài ngày đến vài tuần"
    },
    
    "ibd_colitis": {
        "title": "💊 Điều trị viêm đại tràng mạn (IBD):",
        "medications": {
            "mild": {
                "title": "Viêm nhẹ:",
                "meds": [
                    "Mesalamine (5-ASA) - 2-4g/ngày",
                    "Sulfasalazine - Thuốc cũ, rẻ hơn",
                    "Dùng đường uống hoặc đặt hậu môn"
                ]
            },
            "moderate": {
                "title": "Viêm vừa:",
                "meds": [
                    "Corticosteroid (Prednisone) - Uống hoặc đặt hậu môn",
                    "Thuốc ức chế miễn dịch (Azathioprine)"
                ]
            },
            "severe": {
                "title": "Viêm nặng:",
                "meds": [
                    "Thuốc sinh học (Infliximab, Adalimumab) - Hiện đại, đắt",
                    "Corticosteroid liều cao",
                    "Có thể cần phẫu thuật (cắt đại tràng)"
                ]
            }
        },
        "duration": "Điều trị lâu dài, theo dõi định kỳ",
        "monitoring": "Nội soi đại tràng mỗi 1-2 năm để theo dõi"
    },
    
    "diet": {
        "title": "🍽️ Chế độ ăn:",
        "during_flare": {
            "title": "Khi đang viêm (flare):",
            "foods": [
                "✅ Cháo loãng, súp",
                "✅ Cơm mềm, bánh mì",
                "✅ Thịt nạc luộc/hấp",
                "✅ Trứng",
                "❌ Tránh: Rau sống, trái cây chưa rửa, đồ cay"
            ]
        },
        "when_stable": {
            "title": "Khi ổn định:",
            "tips": [
                "Ăn bình thường, đầy đủ dinh dưỡng",
                "Thêm sữa chua (probiotic)",
                "Uống đủ nước",
                "Tránh đồ cay, rượu bia"
            ]
        }
    },
    
    "lifestyle": {
        "title": "💧 Lối sống:",
        "tips": [
            "Giảm stress (stress làm nặng thêm)",
            "Ngủ đủ, nghỉ ngơi",
            "Tập thể dục nhẹ (đi bộ)",
            "Không hút thuốc"
        ]
    },
    
    "when_to_see_doctor": {
        "title": "🏥 Khi nào cần khám bác sĩ:",
        "urgent": [
            "🚨 Tiêu chảy máu nhiều",
            "🚨 Sốt cao, đau bụng dữ dội",
            "🚨 Dấu hiệu tắc ruột (bụng chướng, không đi ngoài được)",
            "🚨 Mất nước nặng"
        ],
        "soon": [
            "Tiêu chảy kéo dài > 1 tuần",
            "Phân có máu (dù ít)",
            "Đau bụng thường xuyên",
            "Sụt cân không rõ nguyên nhân",
            "Người già, có bệnh nền"
        ]
    }
}

