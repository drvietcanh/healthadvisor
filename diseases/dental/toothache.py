"""
Đau Răng Cấp (Toothache)
==========================
"""

TOOTHACHE_INFO = {
    "name_vn": "Đau Răng Cấp",
    "name_en": "Acute Toothache",
    
    "simple_explanation": """
💡 **Đau răng cấp là gì?**

Đau răng đột ngột, dữ dội:
- Đau nhói, giật như điện
- Đau liên tục hoặc từng cơn
- Đau lan lên đầu, tai, mặt

→ Thường do sâu răng nặng, viêm tủy răng!
    """,
    
    "common_causes": {
        "title": "💡 Nguyên nhân đau răng:",
        "causes": [
            {
                "name": "Sâu răng nặng (phổ biến nhất):",
                "description": "Sâu vào tủy răng (thần kinh) → Đau dữ dội"
            },
            {
                "name": "Viêm tủy răng:",
                "description": "Tủy răng (thần kinh) bị viêm → Đau nhói, nhạy cảm nóng/lạnh"
            },
            {
                "name": "Áp xe răng (nhiễm trùng):",
                "description": "Mủ tích tụ ở chân răng → Đau, sưng nướu, có thể sốt"
            },
            {
                "name": "Mọc răng khôn:",
                "description": "Răng khôn mọc lệch → Đau, sưng nướu sau cùng"
            },
            {
                "name": "Nứt răng:",
                "description": "Răng bị nứt → Đau khi cắn, nhai"
            },
            {
                "name": "Viêm nướu nặng:",
                "description": "Nướu sưng đỏ, đau"
            }
        ]
    },
    
    "symptoms": {
        "pain": {
            "title": "🔍 Các kiểu đau:",
            "types": [
                "**Đau nhói, giật:** Sâu răng, viêm tủy",
                "**Đau liên tục:** Áp xe răng",
                "**Đau khi cắn/nhai:** Nứt răng, áp xe",
                "**Đau với nóng/lạnh:** Viêm tủy, sâu răng",
                "**Đau lan:** Lên đầu, tai, mặt, cổ"
            ]
        },
        "other": [
            "Sưng nướu quanh răng",
            "Sưng mặt, má",
            "Sốt (nếu có nhiễm trùng)",
            "Hôi miệng",
            "Răng lung lay (nếu nặng)",
            "Khó mở miệng (nếu sưng nhiều)"
        ]
    },
    
    "immediate_relief": {
        "title": "⚡ Giảm đau tạm thời (tại nhà):",
        "steps": [
            "1. **Uống thuốc giảm đau:**",
            "   - Paracetamol 500mg (1-2 viên, cách 6-8 giờ)",
            "   - Ibuprofen 400mg (nếu không có bệnh dạ dày)",
            "",
            "2. **Chườm lạnh:**",
            "   - Túi đá bọc khăn, chườm bên ngoài má",
            "   - Giúp giảm sưng, đau",
            "",
            "3. **Súc miệng nước muối:**",
            "   - 1 thìa muối + 1 cốc nước ấm",
            "   - Súc 2-3 lần/ngày",
            "   - Giúp sát khuẩn, giảm đau",
            "",
            "4. **Tránh:**",
            "   - Thức ăn nóng, lạnh, ngọt (kích thích đau)",
            "   - Nhai bên răng đau",
            "   - Không chườm nóng (làm sưng thêm)"
        ],
        "warning": "⚠️ **CHỈ LÀ GIẢM ĐAU TẠM THỜI** - Phải đi nha sĩ để chữa nguyên nhân!"
    },
    
    "treatment": {
        "title": "💊 Điều trị tại nha sĩ:",
        "steps": [
            "1. **Chẩn đoán:**",
            "   - Khám răng, chụp X-quang",
            "   - Xác định nguyên nhân",
            "",
            "2. **Điều trị theo nguyên nhân:**",
            "   - **Sâu răng:** Trám răng hoặc chữa tủy",
            "   - **Viêm tủy:** Chữa tủy răng (lấy tủy, trám)",
            "   - **Áp xe:** Chích mủ, chữa tủy hoặc nhổ răng",
            "   - **Mọc răng khôn:** Nhổ răng khôn",
            "",
            "3. **Kháng sinh (nếu nhiễm trùng):**",
            "   - Amoxicillin, Clindamycin",
            "",
            "4. **Giảm đau:**",
            "   - Thuốc giảm đau sau điều trị"
        ]
    },
    
    "when_see_dentist_urgent": {
        "title": "🚨 ĐI NHA SĨ NGAY (CẤP CỨU):",
        "items": [
            "⛔ Đau răng dữ dội, không chịu được",
            "⛔ Đau kèm sốt cao >38.5°C",
            "⛔ Sưng mặt, sưng nướu nhiều",
            "⛔ Khó mở miệng, khó nuốt",
            "⛔ Có mủ chảy ra từ nướu",
            "⛔ Đau lan lên tai, cổ (nghi ngờ nhiễm trùng lan)"
        ]
    },
    
    "when_see_dentist_soon": {
        "title": "🦷 Đi nha sĩ sớm (trong 1-2 ngày):",
        "items": [
            "⛔ Đau răng vừa, nhưng không tự hết",
            "⛔ Đau khi nhai, cắn",
            "⛔ Nhạy cảm với nóng/lạnh",
            "⛔ Răng có lỗ sâu, đổi màu"
        ]
    },
    
    "prevention": {
        "title": "💡 Phòng ngừa đau răng:",
        "items": [
            "✅ Đánh răng đúng cách, 2 lần/ngày",
            "✅ Dùng chỉ nha khoa",
            "✅ Khám nha sĩ định kỳ (6 tháng/lần)",
            "✅ Trám răng sâu sớm (trước khi đau)",
            "✅ Ăn ít đường, đồ ngọt",
            "✅ Không hút thuốc lá"
        ]
    },
    
    "note": "⚠️ **QUAN TRỌNG:** Đau răng KHÔNG TỰ KHỎI! Phải đi nha sĩ để chữa nguyên nhân. Đừng để đau quá lâu → Nhiễm trùng lan, nguy hiểm!"
}

