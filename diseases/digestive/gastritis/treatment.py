"""
Gastritis - Điều trị
"""

TREATMENT = {
    "medications": {
        "title": "💊 Thuốc điều trị:",
        "antacids": {
            "title": "Thuốc trung hòa axit (Giảm đau nhanh):",
            "examples": [
                "Maalox, Gaviscon - Uống sau ăn hoặc khi đau",
                "Tác dụng: Trung hòa axit ngay lập tức",
                "Lưu ý: Không dùng lâu ngày (có tác dụng phụ)"
            ]
        },
        "h2_blockers": {
            "title": "Thuốc giảm tiết axit (H2 blockers):",
            "examples": [
                "Famotidine (Pepcid) - 20mg x 2 lần/ngày",
                "Cimetidine - Theo chỉ định",
                "Tác dụng: Giảm tiết axit dạ dày",
                "Thời gian: 2-4 tuần"
            ]
        },
        "ppi": {
            "title": "Thuốc ức chế bơm proton (PPI) - Mạnh nhất:",
            "examples": [
                "Omeprazole (Losec) - 20mg x 1-2 lần/ngày",
                "Esomeprazole (Nexium)",
                "Lansoprazole",
                "Tác dụng: Giảm tiết axit mạnh, lành niêm mạc",
                "Thời gian: 4-8 tuần, uống TRƯỚC ăn 30 phút"
            ]
        },
        "antibiotics": {
            "title": "Kháng sinh (Nếu có H. pylori):",
            "protocol": "Dùng 2-3 loại kháng sinh + PPI (10-14 ngày)",
            "examples": [
                "Amoxicillin + Clarithromycin + Omeprazole",
                "Metronidazole + Tetracycline + PPI"
            ],
            "note": "Cần bác sĩ kê đơn, không tự ý dùng!"
        },
        "protection": {
            "title": "Thuốc bảo vệ niêm mạc:",
            "examples": [
                "Sucralfate - Bọc niêm mạc, bảo vệ khỏi axit",
                "Bismuth - Bảo vệ và diệt H. pylori"
            ]
        }
    },
    
    "lifestyle": {
        "title": "💧 Thay đổi lối sống (QUAN TRỌNG!):",
        "diet": {
            "title": "Chế độ ăn:",
            "avoid": [
                "❌ **Rượu bia** - Làm tổn thương niêm mạc",
                "❌ **Đồ cay, nóng** - Kích thích dạ dày",
                "❌ **Cà phê, trà đậm** - Tăng tiết axit",
                "❌ **Đồ chua** - Chanh, dấm",
                "❌ **Đồ chiên rán, nhiều dầu mỡ**",
                "❌ **Ăn no, ăn nhanh**"
            ],
            "recommend": [
                "✅ **Ăn nhiều bữa nhỏ** - 5-6 bữa/ngày, mỗi bữa ít",
                "✅ **Ăn chậm, nhai kỹ**",
                "✅ **Thức ăn mềm, dễ tiêu** - Cháo, súp, cơm mềm",
                "✅ **Sữa chua** - Probiotic tốt cho dạ dày",
                "✅ **Gừng, nghệ** - Giảm viêm (trà gừng, nghệ)"
            ]
        },
        "habits": {
            "title": "Thói quen:",
            "tips": [
                "✅ Không nằm ngay sau khi ăn (đợi 2-3 giờ)",
                "✅ Kê gối cao khi ngủ (tránh trào ngược)",
                "✅ Giảm stress, nghỉ ngơi đầy đủ",
                "✅ Bỏ thuốc lá (nếu có)",
                "✅ Tránh dùng thuốc giảm đau (Aspirin, Ibuprofen) - Dùng Paracetamol thay thế"
            ]
        }
    },
    
    "when_to_see_doctor": {
        "title": "🏥 Khi nào cần khám bác sĩ:",
        "urgent": [
            "🚨 Nôn ra máu hoặc phân đen",
            "🚨 Đau dữ dội không chịu được",
            "🚨 Chóng mặt, ngất",
            "🚨 Sốt kèm đau bụng"
        ],
        "soon": [
            "Triệu chứng không đỡ sau 1-2 tuần tự điều trị",
            "Đau kéo dài > 2 tuần",
            "Sụt cân không rõ nguyên nhân",
            "Trên 50 tuổi, lần đầu tiên bị đau dạ dày"
        ]
    }
}

