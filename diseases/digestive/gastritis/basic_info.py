"""
Viêm Dạ Dày (Gastritis) - Thông tin cơ bản
"""

GASTRITIS_INFO = {
    "name": "Viêm Dạ Dày",
    "name_en": "Gastritis",
    
    "simple_explanation": """
💡 Viêm dạ dày là gì? (Giải thích đơn giản)

Tưởng tượng dạ dày như một cái túi có lớp bảo vệ:
- BÌNH THƯỜNG: Lớp niêm mạc bảo vệ, axit không làm tổn thương
- VIÊM: Lớp niêm mạc bị tổn thương → Axit tấn công → Đau, viêm

🫀 Chuyện gì xảy ra:
1. Niêm mạc dạ dày bị tổn thương (do thuốc, rượu, vi khuẩn)
2. Axit dạ dày tấn công niêm mạc → Gây viêm, đau
3. Dạ dày sưng, đỏ → Đau vùng thượng vị (trên rốn)
4. Nếu không chữa → Có thể loét dạ dày

⚠️ ĐẶC ĐIỂM:
- Cấp tính: Đau đột ngột, nặng (do rượu, thuốc)
- Mạn tính: Đau âm ỉ, kéo dài (do H. pylori)
- Chữa sớm → Khỏi nhanh (giảm axit + tránh nguyên nhân)
    """,
    
    "types": {
        "acute": {
            "name": "Viêm dạ dày cấp",
            "duration": "Đau đột ngột, kéo dài vài ngày",
            "causes": ["Rượu bia", "Thuốc giảm đau (Aspirin, Ibuprofen)", "Stress nặng"],
            "severity": "Đau nhiều nhưng dễ chữa"
        },
        "chronic": {
            "name": "Viêm dạ dày mạn",
            "duration": "Đau âm ỉ, kéo dài nhiều tháng",
            "causes": ["Vi khuẩn H. pylori", "Thuốc giảm đau lâu ngày", "Rượu bia lâu ngày"],
            "severity": "Cần điều trị lâu, có thể tiến triển thành loét"
        }
    },
    
    "statistics": {
        "prevalence": "Rất phổ biến, đặc biệt ở người già",
        "h_pylori": "50-70% người Việt nhiễm H. pylori (vi khuẩn gây viêm/loét dạ dày)"
    }
}

