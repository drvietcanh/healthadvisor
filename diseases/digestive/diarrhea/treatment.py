"""
Diarrhea - Điều trị
"""

TREATMENT = {
    "hydration": {
        "title": "💧 BÙ NƯỚC (QUAN TRỌNG NHẤT!):",
        "amount": "Uống 2-3 lít/ngày (nhiều hơn bình thường)",
        "what_to_drink": {
            "recommended": [
                "✅ **Oresol** - Tốt nhất! Bù nước + điện giải",
                "✅ **Nước lọc** + chút muối đường",
                "✅ **Nước dừa tươi** - Nhiều kali",
                "✅ **Nước cháo muối** - Dễ tiêu, bù nước",
                "✅ **Trà gừng** - Giảm buồn nôn"
            ],
            "avoid": [
                "❌ Nước ngọt có ga (làm tiêu chảy nặng hơn)",
                "❌ Rượu bia, cà phê",
                "❌ Nước ép trái cây quá ngọt"
            ]
        },
        "how_to_make_oresol": {
            "title": "Cách pha Oresol:",
            "step1": "1 gói Oresol (hoặc 1 thìa muối + 8 thìa đường)",
            "step2": "Pha với 1 lít nước đun sôi để nguội",
            "step3": "Uống từng ngụm nhỏ, thường xuyên",
            "amount": "Uống 100-200ml sau mỗi lần đi ngoài"
        },
        "warning": "⚠️ Nếu không uống được (nôn nhiều) → Phải truyền dịch ở bệnh viện!"
    },
    
    "diet": {
        "title": "🍽️ Chế độ ăn:",
        "when_acute": {
            "title": "Khi đang tiêu chảy nặng:",
            "foods": [
                "Cháo loãng, súp (dễ tiêu)",
                "Bánh mì, bánh quy",
                "Chuối (nhiều kali)",
                "Khoai tây luộc",
                "Ăn ít, chia nhiều bữa"
            ],
            "avoid": [
                "❌ Đồ chiên rán, nhiều dầu mỡ",
                "❌ Đồ cay, nóng",
                "❌ Rau sống, trái cây chưa rửa kỹ",
                "❌ Sữa (nhiều người không dung nạp lactose khi tiêu chảy)",
                "❌ Đồ ngọt, bánh kẹo"
            ]
        },
        "when_better": {
            "title": "Khi đỡ hơn (2-3 ngày sau):",
            "tips": [
                "Ăn bình thường dần",
                "Thêm sữa chua (probiotic tốt cho ruột)",
                "Ăn nhiều chất xơ nhẹ (chuối, táo)"
            ]
        }
    },
    
    "medications": {
        "title": "💊 Thuốc:",
        "note": "⚠️ KHÔNG tự ý dùng thuốc cầm tiêu chảy (Loperamide) khi có sốt hoặc phân máu!",
        "when_ok": {
            "title": "Chỉ dùng khi:",
            "conditions": [
                "Tiêu chảy nhẹ, không sốt",
                "Không có máu trong phân",
                "Cần đi công tác, không đi vệ sinh được"
            ],
            "medication": "Loperamide (Imodium) - Theo chỉ định"
        },
        "probiotics": {
            "title": "Probiotic (Tốt cho ruột):",
            "examples": [
                "Men vi sinh (Lactobacillus, Bifidobacterium)",
                "Sữa chua có men sống",
                "Giúp phục hồi vi khuẩn tốt trong ruột"
            ]
        },
        "antibiotics": {
            "title": "Kháng sinh (CHỈ dùng khi có chỉ định bác sĩ):",
            "note": "⚠️ Hầu hết tiêu chảy do virus → Không cần kháng sinh!",
            "when_needed": [
                "Nhiễm trùng nặng (Shigella, E. coli độc lực cao)",
                "Phân có máu",
                "Sốt cao kéo dài",
                "Người già, có bệnh nền"
            ]
        }
    },
    
    "prevention": {
        "title": "✅ Phòng ngừa:",
        "hygiene": {
            "title": "Vệ sinh:",
            "tips": [
                "Rửa tay thường xuyên (trước ăn, sau đi vệ sinh)",
                "Rửa tay bằng xà phòng, ít nhất 20 giây",
                "Vệ sinh nhà bếp, dụng cụ nấu ăn"
            ]
        },
        "food_safety": {
            "title": "An toàn thực phẩm:",
            "tips": [
                "Ăn chín, uống sôi",
                "Rửa rau, trái cây kỹ trước khi ăn",
                "Không ăn thịt sống, trứng sống",
                "Bảo quản thức ăn trong tủ lạnh",
                "Không ăn thức ăn để quá 2 giờ ở nhiệt độ phòng",
                "Uống nước sạch, đun sôi"
            ]
        }
    },
    
    "when_to_see_doctor": {
        "title": "🏥 Khi nào cần khám bác sĩ:",
        "urgent": [
            "🚨 Tiêu chảy > 10 lần/ngày",
            "🚨 Phân có máu",
            "🚨 Sốt cao (>39°C)",
            "🚨 Dấu hiệu mất nước nặng",
            "🚨 Đau bụng dữ dội",
            "🚨 Nôn liên tục, không uống được"
        ],
        "soon": [
            "Tiêu chảy > 3 ngày không đỡ",
            "Trẻ em < 2 tuổi",
            "Người già > 70 tuổi",
            "Có bệnh tiểu đường, suy thận",
            "Đang dùng thuốc ức chế miễn dịch"
        ]
    }
}

