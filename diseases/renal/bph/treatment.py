"""
BPH - Điều trị
"""

TREATMENT = {
    "medications": {
        "title": "💊 Thuốc điều trị:",
        "alpha_blockers": {
            "title": "Thuốc giãn cơ (Alpha-blockers) - Giảm triệu chứng nhanh:",
            "how_it_works": "Giãn cơ tuyến tiền liệt và cổ bàng quang → Dễ tiểu hơn",
            "examples": [
                "Tamsulosin (Flomax) - 0.4mg x 1 lần/ngày",
                "Terazosin (Hytrin)",
                "Doxazosin (Cardura)"
            ],
            "benefits": [
                "✅ Giảm triệu chứng NHANH (sau vài ngày)",
                "✅ Dễ tiểu, dòng tiểu mạnh hơn",
                "✅ Giảm tiểu đêm"
            ],
            "side_effects": [
                "Tụt huyết áp khi đứng (chóng mặt)",
                "Chóng mặt, mệt mỏi",
                "Ngất (hiếm)"
            ],
            "note": "⚠️ Uống buổi tối, đứng lên từ từ sau khi uống"
        },
        "5_alpha_reductase": {
            "title": "Thuốc giảm kích thước (5-alpha reductase inhibitors):",
            "how_it_works": "Giảm kích thước tuyến tiền liệt từ từ (6-12 tháng)",
            "examples": [
                "Finasteride (Proscar) - 5mg x 1 lần/ngày",
                "Dutasteride (Avodart)"
            ],
            "benefits": [
                "✅ Giảm kích thước tuyến → Giảm tắc nghẽn",
                "✅ Giảm nguy cơ bí tiểu",
                "✅ Giảm nguy cơ phẫu thuật"
            ],
            "side_effects": [
                "Giảm ham muốn tình dục (5-10%)",
                "Rối loạn cương dương (3-5%)",
                "Tác dụng chậm (6-12 tháng mới thấy rõ)"
            ],
            "note": "⚠️ Phải uống lâu dài, không bỏ giữa chừng!"
        },
        "combination": {
            "title": "Kết hợp 2 loại thuốc:",
            "description": "Alpha-blocker + 5-alpha reductase inhibitor",
            "when": "Khi triệu chứng nặng, tuyến to",
            "benefit": "Vừa giảm triệu chứng nhanh + Giảm kích thước lâu dài"
        }
    },
    
    "lifestyle": {
        "title": "💧 Thay đổi lối sống:",
        "tips": [
            "✅ TRÁNH nhịn tiểu lâu - Đi tiểu ngay khi buồn",
            "✅ Tránh uống nhiều nước trước khi ngủ (giảm tiểu đêm)",
            "✅ TRÁNH: Cà phê, rượu bia, trà đậm (kích thích tiểu)",
            "✅ Tập Kegel (co thắt cơ sàn chậu) - Giúp kiểm soát tiểu",
            "✅ Đi tiểu đầy đủ - Đừng vội vã, ngồi tiểu cho thoải mái",
            "✅ Tránh táo bón (làm nặng triệu chứng)"
        ]
    },
    
    "surgery": {
        "title": "🔬 Phẫu thuật (Khi thuốc không hiệu quả):",
        "when": [
            "Thuốc không hiệu quả sau 3-6 tháng",
            "Bí tiểu tái phát",
            "Có biến chứng: Nhiễm trùng, sỏi bàng quang",
            "Triệu chứng nặng, ảnh hưởng nhiều"
        ],
        "methods": [
            "**TURP (Cắt tuyến qua niệu đạo)** - Phương pháp chuẩn vàng",
            "**Laser cắt tuyến** - Ít chảy máu, hồi phục nhanh",
            "**Rezūm (Hơi nước)** - Ít xâm lấn, hồi phục nhanh",
            "**UroLift** - Nâng tuyến lên, không cắt"
        ],
        "benefits": "Giảm triệu chứng rõ rệt, lâu dài",
        "risks": "Có thể gây: Rối loạn cương dương, xuất tinh ngược dòng"
    },
    
    "when_to_see_doctor": {
        "title": "🏥 Khi nào cần khám lại:",
        "regular": "Khám định kỳ mỗi 6-12 tháng khi đang điều trị",
        "urgent": [
            "🚨 Bí tiểu hoàn toàn",
            "🚨 Tiểu máu",
            "🚨 Sốt, đau bụng",
            "🚨 Thuốc không còn tác dụng"
        ]
    }
}

