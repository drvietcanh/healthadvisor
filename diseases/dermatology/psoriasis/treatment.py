"""
Psoriasis - Điều trị
"""

TREATMENT = {
    "topical": {
        "title": "💊 Thuốc bôi (Điều trị nhẹ-trung bình):",
        "corticosteroids": {
            "title": "Thuốc corticosteroid bôi:",
            "examples": [
                "Betamethasone (Diprosone)",
                "Clobetasol (Temovate)",
                "Triamcinolone"
            ],
            "use": "Bôi 1-2 lần/ngày vào mảng vảy nến",
            "warning": "⚠️ KHÔNG dùng lâu ngày liên tục (gây teo da). Dùng theo đợt, nghỉ giữa các đợt."
        },
        "vitamin_d": {
            "title": "Thuốc Vitamin D bôi:",
            "examples": [
                "Calcipotriol (Dovonex)",
                "Calcitriol"
            ],
            "use": "Bôi 2 lần/ngày, có thể dùng lâu dài",
            "benefit": "An toàn hơn corticosteroid, ít tác dụng phụ"
        },
        "coal_tar": {
            "title": "Nhựa than (Coal tar):",
            "description": "Dầu gội, kem bôi chứa nhựa than",
            "use": "Giảm vảy, ngứa, đặc biệt da đầu",
            "smell": "Có mùi đặc trưng (không thơm)"
        },
        "salicylic_acid": {
            "title": "Acid salicylic:",
            "description": "Làm bong vảy, giúp thuốc khác thấm tốt hơn",
            "use": "Bôi trước khi bôi thuốc khác"
        }
    },
    
    "phototherapy": {
        "title": "☀️ Liệu pháp ánh sáng (Phototherapy):",
        "description": "Chiếu tia UVB vào da → Giảm viêm, giảm tạo tế bào",
        "types": [
            "UVB băng hẹp (NB-UVB) - Hiệu quả, an toàn",
            "PUVA - Uống thuốc + chiếu UVA"
        ],
        "frequency": "2-3 lần/tuần, trong 2-3 tháng",
        "benefits": "Hiệu quả tốt, ít tác dụng phụ",
        "note": "⚠️ Cần bác sĩ chỉ định, không tự ý tắm nắng!"
    },
    
    "systemic": {
        "title": "💊 Thuốc uống (Điều trị nặng):",
        "methotrexate": {
            "title": "Methotrexate:",
            "use": "Uống 1 lần/tuần",
            "benefits": "Hiệu quả tốt, rẻ",
            "side_effects": "Có thể gây: Buồn nôn, thiếu máu, tổn thương gan",
            "monitoring": "Cần xét nghiệm máu định kỳ"
        },
        "cyclosporine": {
            "title": "Cyclosporine:",
            "use": "Uống hàng ngày",
            "benefits": "Hiệu quả nhanh",
            "side_effects": "Có thể gây: Tăng huyết áp, suy thận",
            "note": "⚠️ Chỉ dùng ngắn hạn (3-6 tháng)"
        },
        "biologics": {
            "title": "Thuốc sinh học (Biologics):",
            "examples": [
                "Adalimumab (Humira)",
                "Etanercept (Enbrel)",
                "Infliximab (Remicade)"
            ],
            "use": "Tiêm dưới da hoặc truyền tĩnh mạch",
            "benefits": "Hiệu quả rất tốt, an toàn",
            "cons": "Đắt tiền, cần bảo quản lạnh"
        }
    },
    
    "lifestyle": {
        "title": "💧 Thay đổi lối sống:",
        "tips": [
            "✅ Giữ ẩm da - Bôi kem dưỡng ẩm hàng ngày",
            "✅ TRÁNH: Trầy xước, cào gãi (làm nặng vảy nến)",
            "✅ Tắm nước ấm (không nóng) - Làm mềm vảy",
            "✅ TRÁNH: Stress, lo âu (làm nặng vảy nến)",
            "✅ Uống đủ nước",
            "✅ Tập thể dục - Giảm stress",
            "✅ TRÁNH: Rượu bia, hút thuốc (làm nặng)",
            "✅ Phơi nắng nhẹ (5-10 phút) - Có thể giúp (nhưng không quá)"
        ]
    },
    
    "when_to_see_doctor": {
        "title": "🏥 Khi nào cần khám bác sĩ:",
        "soon": [
            "Có mảng da đỏ, vảy trắng",
            "Ngứa, đau ảnh hưởng sinh hoạt",
            "Vảy nến lan rộng",
            "Vảy nến da đầu, móng tay"
        ],
        "urgent": [
            "🚨 Đau khớp kèm vảy nến (viêm khớp vảy nến)",
            "🚨 Mảng da đỏ lan rộng, có mủ (vảy nến mủ - hiếm)",
            "🚨 Sốt, mệt mỏi với vảy nến lan rộng"
        ]
    }
}

