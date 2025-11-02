"""
IBS - Điều trị
"""

TREATMENT = {
    "diet": {
        "title": "🍽️ Chế độ ăn (QUAN TRỌNG NHẤT):",
        "fodmap": {
            "title": "Chế độ ăn FODMAP thấp:",
            "description": "Tránh thức ăn lên men trong ruột → Giảm đầy hơi, đau",
            "avoid": [
                "❌ **Fructose** - Táo, lê, mật ong, siro ngô",
                "❌ **Lactose** - Sữa, sữa chua, phô mai (nếu không dung nạp)",
                "❌ **Fructans** - Lúa mì, hành, tỏi",
                "❌ **Galactans** - Đậu, đậu lăng",
                "❌ **Polyols** - Sorbitol (kẹo không đường), đào, mận"
            ],
            "can_eat": [
                "✅ Thịt, cá, trứng",
                "✅ Gạo, yến mạch",
                "✅ Chuối, việt quất, dâu tây",
                "✅ Rau xanh, cà rốt",
                "✅ Sữa không lactose"
            ],
            "note": "⚠️ Thử loại bỏ từng nhóm một, xem nhóm nào gây triệu chứng. Không cần tránh tất cả!"
        },
        "general": {
            "title": "Nguyên tắc chung:",
            "tips": [
                "✅ Ăn nhiều bữa nhỏ (5-6 bữa/ngày) thay vì 3 bữa lớn",
                "✅ Ăn chậm, nhai kỹ",
                "✅ Uống đủ nước (2-3 lít/ngày)",
                "✅ Ghi nhật ký ăn uống - Xem thức ăn nào gây triệu chứng",
                "❌ TRÁNH: Đồ cay, nóng, nhiều dầu mỡ",
                "❌ TRÁNH: Rượu bia, cà phê (kích thích ruột)",
                "❌ TRÁNH: Đồ ngọt nhân tạo (sorbitol, mannitol)",
                "❌ TRÁNH: Ăn quá no, quá nhanh"
            ]
        },
        "fiber": {
            "title": "Chất xơ:",
            "soluble": {
                "title": "Chất xơ hòa tan (Tốt cho IBS):",
                "sources": [
                    "Yến mạch",
                    "Hạt lanh",
                    "Psyllium (Metamucil)",
                    "Chuối",
                    "Đu đủ"
                ],
                "benefit": "Giảm tiêu chảy (IBS-D), giảm táo bón (IBS-C)"
            },
            "insoluble": {
                "title": "Chất xơ không hòa tan (Cẩn thận):",
                "sources": [
                    "Cám lúa mì",
                    "Ngũ cốc nguyên hạt",
                    "Rau sống"
                ],
                "warning": "⚠️ Có thể làm nặng triệu chứng ở một số người"
            }
        }
    },
    
    "medications": {
        "title": "💊 Thuốc điều trị:",
        "antispasmodics": {
            "title": "Thuốc giảm co thắt (Giảm đau bụng):",
            "examples": [
                "Hyoscine (Buscopan)",
                "Mebeverine (Colofac)",
                "Dicyclomine (Bentyl)"
            ],
            "use": "Uống khi đau, hoặc trước khi ăn (nếu ăn thường gây đau)"
        },
        "antidiarrheal": {
            "title": "Thuốc cầm tiêu chảy (IBS-D):",
            "examples": [
                "Loperamide (Imodium) - Khi có tiêu chảy",
                "Không dùng thường xuyên, chỉ khi cần"
            ]
        },
        "laxatives": {
            "title": "Thuốc nhuận tràng (IBS-C):",
            "examples": [
                "Polyethylene glycol (Miralax)",
                "Psyllium (Metamucil)",
                "Dùng đều đặn để giữ phân mềm"
            ]
        },
        "probiotics": {
            "title": "Probiotic (Men vi sinh):",
            "description": "Cân bằng vi khuẩn ruột → Có thể cải thiện triệu chứng",
            "examples": [
                "Sữa chua có men sống",
                "Men vi sinh dạng viên (Lactobacillus, Bifidobacterium)",
                "Cần dùng đều đặn ít nhất 4 tuần"
            ],
            "note": "⚠️ Hiệu quả không chắc chắn, nhưng an toàn, đáng thử"
        },
        "antidepressants": {
            "title": "Thuốc chống trầm cảm liều thấp:",
            "description": "Giảm đau, giảm nhạy cảm ruột (không phải để chữa trầm cảm)",
            "examples": [
                "Amitriptyline - Liều thấp (10-25mg)",
                "Chỉ dùng khi triệu chứng nặng, ảnh hưởng nhiều"
            ],
            "note": "⚠️ Cần bác sĩ kê đơn!"
        }
    },
    
    "stress_management": {
        "title": "🧘 Quản lý stress (QUAN TRỌNG):",
        "why": "Stress, lo âu làm nặng triệu chứng IBS rất nhiều!",
        "methods": [
            "✅ Tập thể dục đều đặn - Đi bộ, yoga, thái cực quyền",
            "✅ Thiền, hít thở sâu - Giảm căng thẳng",
            "✅ Ngủ đủ giấc - 7-8 giờ/đêm",
            "✅ Tránh stress quá mức",
            "✅ Tâm lý trị liệu (nếu cần) - CBT (Cognitive Behavioral Therapy)"
        ]
    },
    
    "when_to_see_doctor": {
        "title": "🏥 Khi nào cần khám bác sĩ:",
        "soon": [
            "Có triệu chứng IBS (đau bụng + thay đổi thói quen đi tiêu)",
            "Triệu chứng kéo dài >3 tháng",
            "Ảnh hưởng sinh hoạt, công việc",
            "Không đáp ứng với thay đổi chế độ ăn"
        ],
        "urgent": [
            "🚨 Có máu trong phân",
            "🚨 Sụt cân không rõ nguyên nhân",
            "🚨 Sốt",
            "🚨 Triệu chứng xuất hiện sau 50 tuổi",
            "🚨 Có người thân bị ung thư đại tràng"
        ],
        "note": "💡 Quan trọng: Khám để loại trừ bệnh nguy hiểm trước! IBS chỉ chẩn đoán sau khi loại trừ các bệnh khác."
    }
}

