"""
Peptic Ulcer - Điều trị
"""

TREATMENT = {
    "medications": {
        "title": "💊 Thuốc điều trị:",
        "ppi": {
            "title": "Thuốc ức chế bơm proton (PPI) - BẮT BUỘC:",
            "examples": [
                "Omeprazole (Losec) - 20-40mg x 2 lần/ngày",
                "Esomeprazole (Nexium) - 40mg x 1 lần/ngày",
                "Lansoprazole - 30mg x 1-2 lần/ngày",
                "Tác dụng: Giảm tiết axit → Vết loét lành",
                "Thời gian: 6-8 tuần (loét tá tràng) hoặc 8-12 tuần (loét dạ dày)",
                "⚠️ Uống TRƯỚC ăn 30 phút để hiệu quả tốt nhất!"
            ]
        },
        "h_pylori": {
            "title": "Diệt H. pylori (Nếu có):",
            "protocol": "3 thuốc (Triple therapy):",
            "examples": [
                "PPI (Omeprazole) + Amoxicillin + Clarithromycin - 10-14 ngày",
                "PPI + Metronidazole + Tetracycline - 10-14 ngày",
                "PPI + Amoxicillin + Metronidazole - 10-14 ngày"
            ],
            "note": "⚠️ Phải uống ĐỦ LIỀU, ĐỦ NGÀY! Nếu không → Vi khuẩn kháng thuốc, khó chữa hơn!",
            "after": "Sau khi hết H. pylori: Tiếp tục uống PPI 4-6 tuần để vết loét lành hoàn toàn"
        },
        "protection": {
            "title": "Thuốc bảo vệ niêm mạc:",
            "examples": [
                "Sucralfate - Bọc vết loét, bảo vệ khỏi axit",
                "Misoprostol - Bảo vệ niêm mạc (nếu dùng NSAIDs)"
            ]
        },
        "stop_nsaids": {
            "title": "QUAN TRỌNG:",
            "warning": "🚫 TUYỆT ĐỐI ngừng thuốc giảm đau (Aspirin, Ibuprofen) khi đang bị loét!",
            "alternative": "→ Dùng Paracetamol (Panadol) thay thế (an toàn hơn)"
        }
    },
    
    "lifestyle": {
        "title": "💧 Thay đổi lối sống:",
        "diet": {
            "title": "Chế độ ăn (Giống viêm dạ dày):",
            "tips": [
                "✅ Ăn nhiều bữa nhỏ (5-6 bữa/ngày)",
                "✅ Thức ăn mềm, dễ tiêu",
                "✅ Tránh: Rượu bia, đồ cay, cà phê, thuốc lá"
            ]
        },
        "habits": {
            "title": "Thói quen:",
            "tips": [
                "✅ Bỏ thuốc lá",
                "✅ Giảm stress",
                "✅ Nghỉ ngơi đầy đủ",
                "✅ Không nằm ngay sau khi ăn"
            ]
        }
    },
    
    "monitoring": {
        "title": "📊 Theo dõi:",
        "endoscopy": "Nội soi dạ dày sau 6-8 tuần điều trị (kiểm tra vết loét đã lành chưa)",
        "h_pylori_test": "Xét nghiệm H. pylori sau 4 tuần ngừng kháng sinh (xem đã diệt hết chưa)"
    },
    
    "when_to_see_doctor": {
        "title": "🏥 Khi nào cần khám bác sĩ:",
        "urgent": [
            "🚨 Nôn ra máu hoặc phân đen",
            "🚨 Đau bụng dữ dội đột ngột",
            "🚨 Bụng cứng như gỗ",
            "🚨 Chóng mặt, ngất"
        ],
        "soon": [
            "Đau không đỡ sau 2 tuần điều trị",
            "Đau tái phát sau khi đã lành",
            "Sụt cân nhiều",
            "Trên 50 tuổi, lần đầu tiên bị"
        ]
    }
}

