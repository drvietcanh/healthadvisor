"""
Nhiễm Trùng Tiết Niệu (UTI) - Thông tin cơ bản
"""

UTI_INFO = {
    "name": "Nhiễm Trùng Tiết Niệu",
    "name_en": "Urinary Tract Infection (UTI)",
    
    "simple_explanation": """
💡 Nhiễm trùng tiết niệu là gì? (Giải thích đơn giản)

Tưởng tượng đường tiểu như ống nước:
- BÌNH THƯỜNG: Nước sạch chảy qua, không có vi khuẩn
- NHIỄM TRÙNG: Vi khuẩn vào ống nước → Gây viêm, đau, nóng rát

🦠 Chuyện gì xảy ra:
1. Vi khuẩn xâm nhập vào đường tiểu (qua niệu đạo)
2. Vi khuẩn nhân lên → Gây viêm, sưng
3. Bàng quang viêm → Đau, buốt khi tiểu
4. Nếu không chữa → Vi khuẩn lên thận → Nguy hiểm!

⚠️ ĐẶC ĐIỂM:
- Phụ nữ dễ bị hơn nam giới (ống tiểu ngắn hơn)
- Người già, người tiểu đường dễ bị hơn
- Uống nhiều nước, vệ sinh sạch → Phòng ngừa tốt
- Chữa sớm → Khỏi nhanh (3-7 ngày dùng kháng sinh)
    """,
    
    "definition": """
Nhiễm trùng tiết niệu là tình trạng vi khuẩn xâm nhập vào đường tiểu
(niệu đạo, bàng quang, hoặc thận) gây viêm và các triệu chứng đau đớn.
    """,
    
    "types": {
        "lower_uti": {
            "name": "Nhiễm trùng đường tiểu dưới",
            "locations": ["Niệu đạo", "Bàng quang"],
            "common_name": "Viêm bàng quang",
            "severity": "Nhẹ hơn, dễ chữa"
        },
        "upper_uti": {
            "name": "Nhiễm trùng đường tiểu trên",
            "locations": ["Thận", "Niệu quản"],
            "common_name": "Viêm thận",
            "severity": "Nặng hơn, nguy hiểm, cần điều trị ngay"
        }
    },
    
    "prevalence": {
        "women": "50-60% phụ nữ bị ít nhất 1 lần trong đời",
        "men": "Ít hơn, nhưng nặng hơn nếu bị",
        "elderly": "Người già dễ bị và dễ tái phát",
        "diabetes": "Người tiểu đường dễ bị hơn"
    }
}

