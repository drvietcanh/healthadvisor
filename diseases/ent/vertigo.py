"""
Chóng Mặt/Vertigo
=================
Bao gồm: Chóng mặt tư thế (BPPV), Viêm tiền đình
"""

VERTIGO_INFO = {
    "name_vn": "Chóng Mặt/Vertigo",
    "name_en": "Dizziness/Vertigo",
    
    "simple_explanation": """
💡 **Chóng mặt là gì?**

Giống như quay vòng vòng rồi dừng lại:
- **Cảm giác quay cuồng**, mọi thứ xung quanh quay
- **Mất thăng bằng**, không đứng vững
- **Buồn nôn**, có thể nôn

→ Khác với choáng váng (cảm giác sắp ngất)
    """,
    
    "what_happens": """
Chuyện gì xảy ra:

1. **Hệ thống giữ thăng bằng bị rối loạn:**
   - **Tai trong** có ống bán khuyên (giúp giữ thăng bằng)
   - **Não** nhận tín hiệu từ tai, mắt, cơ khớp
   - Nếu bất kỳ phần nào hỏng → Mất thăng bằng

2. **Chóng mặt vs Choáng váng:**
   - **Chóng mặt (Vertigo):** Cảm giác quay cuồng (mọi thứ quay)
   - **Choáng váng (Dizziness):** Cảm giác sắp ngất, mờ mắt

3. **Các loại chóng mặt:**
   - **BPPV:** Chóng mặt khi xoay đầu (sỏi nhỏ rơi vào ống bán khuyên)
   - **Viêm tiền đình:** Chóng mặt sau nhiễm virus (cảm cúm)
    """,
    
    "symptoms": {
        "vertigo": [
            "Cảm giác quay cuồng (mọi thứ xung quanh quay)",
            "Mất thăng bằng, không đứng vững",
            "Buồn nôn, có thể nôn",
            "Ra mồ hôi lạnh",
            "Chóng mặt khi xoay đầu, cúi xuống, ngửa lên",
            "Chóng mặt khi nằm xuống hoặc ngồi dậy"
        ],
        "dizziness": [
            "Choáng váng (cảm giác sắp ngất)",
            "Mờ mắt, tối sầm",
            "Đứng không vững",
            "Yếu chân tay"
        ],
        "when_occurs": [
            "Khi xoay đầu sang một bên",
            "Khi cúi xuống nhặt đồ",
            "Khi ngửa đầu lên",
            "Khi nằm xuống hoặc ngồi dậy",
            "Khi quay người trong giường"
        ]
    },
    
    "causes": {
        "bppv": {
            "title": "🎯 Chóng mặt tư thế lành tính (BPPV - Phổ biến nhất):",
            "description": "Sỏi nhỏ trong tai trong rơi vào ống bán khuyên",
            "why": [
                "Trong tai trong có \"sỏi\" nhỏ (otoconia)",
                "Sỏi rơi vào ống bán khuyên → Kích thích thần kinh",
                "Gây chóng mặt khi xoay đầu",
                "Thường một bên tai",
                "Không nguy hiểm, có thể chữa khỏi"
            ]
        },
        "vestibular_neuronitis": {
            "title": "🦠 Viêm tiền đình (Vestibular Neuronitis):",
            "description": "Nhiễm virus làm viêm dây thần kinh tiền đình",
            "why": [
                "Sau cảm cúm, nhiễm virus",
                "Dây thần kinh tiền đình bị viêm",
                "Chóng mặt dữ dội, kéo dài vài ngày",
                "Không có điếc, không có ù tai",
                "Tự khỏi sau 1-2 tuần"
            ]
        },
        "meniere": {
            "title": "🌀 Bệnh Meniere:",
            "description": "Chóng mặt + Điếc + ù tai",
            "why": [
                "Áp lực trong tai trong tăng cao",
                "Cơn chóng mặt dữ dội (vài giờ)",
                "Kèm điếc, ù tai",
                "Có thể buồn nôn, nôn",
                "Tái phát nhiều lần"
            ]
        },
        "other": [
            "Đột quỵ (hiếm, nhưng nguy hiểm)",
            "U thần kinh thính giác",
            "Chấn thương đầu",
            "Thuốc độc với tai (Gentamicin)",
            "Thiếu máu não",
            "Huyết áp thấp khi đứng dậy"
        ]
    },
    
    "treatment": {
        "bppv": {
            "title": "🎯 Điều trị BPPV (Chóng mặt tư thế):",
            "maneuver": [
                "**Nghiệm pháp tái định vị (Epley maneuver):**",
                "   - Bác sĩ xoay đầu theo tư thế đặc biệt",
                "   - Đưa \"sỏi\" về đúng vị trí",
                "   - Làm 1-2 lần → Chóng mặt khỏi ngay",
                "   - Có thể tự làm ở nhà (theo hướng dẫn)",
                "",
                "**Tự làm ở nhà:**",
                "   - Ngồi trên giường, đầu xoay 45° về bên chóng mặt",
                "   - Nằm xuống, đầu vẫn xoay 45°",
                "   - Giữ 30 giây",
                "   - Xoay đầu 90° sang bên kia",
                "   - Giữ 30 giây",
                "   - Xoay người về bên đó, đầu cúi xuống",
                "   - Giữ 30 giây",
                "   - Ngồi dậy từ từ",
                "   - Làm 3 lần/ngày, đến khi hết chóng mặt"
            ],
            "medications": [
                "**Thuốc hỗ trợ:**",
                "   - Betahistine (Vestibularin) - Giảm chóng mặt",
                "   - Dimenhydrinate (Nauser) - Chống nôn",
                "   - Chỉ dùng khi chóng mặt dữ dội"
            ]
        },
        "vestibular_neuronitis": {
            "title": "🦠 Điều trị viêm tiền đình:",
            "treatment": [
                "**Nghỉ ngơi:**",
                "   - Nằm nghỉ khi chóng mặt dữ dội",
                "   - Tránh xoay đầu đột ngột",
                "",
                "**Thuốc:**",
                "   - Betahistine (Vestibularin)",
                "   - Dimenhydrinate (Nauser) - Chống nôn",
                "   - Tự khỏi sau 1-2 tuần",
                "",
                "**Tập phục hồi chức năng:**",
                "   - Tập thăng bằng (sau khi hết chóng mặt cấp)",
                "   - Tập nhìn, xoay đầu từ từ"
            ]
        },
        "meniere": {
            "title": "🌀 Điều trị bệnh Meniere:",
            "treatment": [
                "**Chế độ ăn:**",
                "   - Giảm muối (<2g/ngày)",
                "   - Tránh caffeine, rượu",
                "",
                "**Thuốc:**",
                "   - Betahistine (Vestibularin)",
                "   - Lợi tiểu (nếu cần)",
                "",
                "**Phẫu thuật:**",
                "   - Nếu điều trị thuốc không đỡ",
                "   - Cắt dây thần kinh tiền đình (hiếm)"
            ]
        },
        "when_to_see_doctor": {
            "urgent": [
                "🚨 Chóng mặt + Đau đầu dữ dội → Có thể đột quỵ",
                "🚨 Chóng mặt + Yếu tay chân một bên → Có thể đột quỵ",
                "🚨 Chóng mặt + Khó nói, méo miệng → Có thể đột quỵ",
                "🚨 Chóng mặt + Sốt cao, cứng cổ → Có thể viêm màng não"
            ],
            "soon": [
                "Chóng mặt kéo dài > 1 tuần",
                "Chóng mặt tái phát nhiều lần",
                "Chóng mặt kèm điếc, ù tai",
                "Chóng mặt ảnh hưởng sinh hoạt"
            ]
        }
    },
    
    "prevention": {
        "title": "🛡️ Cách phòng ngừa chóng mặt:",
        "tips": [
            "✅ **Xoay đầu từ từ:**",
            "   - Không xoay đầu đột ngột",
            "   - Khi nằm xuống, ngồi dậy → Từ từ",
            "",
            "✅ **Tránh nằm nghiêng một bên quá lâu:**",
            "   - Thay đổi tư thế khi ngủ",
            "",
            "✅ **Tập thăng bằng:**",
            "   - Đi bộ đều đặn",
            "   - Tập yoga, thái cực quyền",
            "",
            "✅ **Điều trị nguyên nhân:**",
            "   - Nếu do huyết áp thấp → Uống nhiều nước",
            "   - Nếu do thiếu máu → Bổ sung sắt",
            "",
            "✅ **Tránh rượu, thuốc lá:**",
            "   - Làm tăng chóng mặt"
        ]
    },
    
    "note": """
⚠️ **LƯU Ý QUAN TRỌNG:**

**CHÓNG MẶT TƯ THẾ (BPPV):",
- Phổ biến nhất, không nguy hiểm",
- Có thể chữa khỏi bằng nghiệm pháp Epley",
- Tránh xoay đầu đột ngột sau khi điều trị",

**CHÓNG MẶT + ĐỘT QUỴ:",
- ⚠️ Nếu chóng mặt kèm yếu tay chân, khó nói → GỌI 115 NGAY",
- Đây là dấu hiệu đột quỵ, cần cấp cứu ngay!",

**VIÊM TIỀN ĐÌNH:",
- Tự khỏi sau 1-2 tuần",
- Nghỉ ngơi, dùng thuốc hỗ trợ",
- Tập phục hồi chức năng sau khi hết chóng mặt cấp"
    """
}

