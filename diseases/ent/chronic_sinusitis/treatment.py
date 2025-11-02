"""
Chronic Sinusitis - Điều trị
"""

TREATMENT = {
    "medications": {
        "title": "💊 Thuốc điều trị:",
        "nasal_spray": {
            "title": "Xịt mũi Corticosteroid (QUAN TRỌNG NHẤT):",
            "how_it_works": "Giảm viêm, sưng niêm mạc xoang",
            "examples": [
                "Fluticasone (Flonase)",
                "Mometasone (Nasonex)",
                "Budesonide (Rhinocort)"
            ],
            "how_to_use": [
                "Xịt mỗi bên mũi 1-2 lần/ngày",
                "Dùng ĐỀU ĐẶN, lâu dài (4-12 tuần)",
                "Xịt đúng cách: Đầu hơi cúi, xịt vào mũi, không hít mạnh",
                "⚠️ Không tự ý ngừng dù đã đỡ (dễ tái phát)"
            ],
            "note": "⚠️ Cần thời gian (2-4 tuần) mới thấy rõ tác dụng!"
        },
        "nasal_rinse": {
            "title": "Rửa mũi bằng nước muối (QUAN TRỌNG):",
            "how_it_works": "Rửa sạch dịch, bụi bẩn trong xoang",
            "how_to_do": [
                "Dùng nước muối sinh lý hoặc nước muối tự pha",
                "Dùng bình rửa mũi (Neti pot) hoặc bình xịt",
                "Rửa 1-2 lần/ngày",
                "Rửa trước khi xịt thuốc → Thuốc thấm tốt hơn"
            ],
            "benefits": [
                "✅ Giảm nghẹt mũi ngay lập tức",
                "✅ Rửa sạch dịch, vi khuẩn",
                "✅ Làm ẩm niêm mạc",
                "✅ Giảm nhu cầu dùng thuốc"
            ]
        },
        "antibiotics": {
            "title": "Kháng sinh (Khi có nhiễm trùng):",
            "when": "Dịch mũi vàng/xanh đặc, sốt, đau mặt",
            "examples": [
                "Amoxicillin/Clavulanate (Augmentin)",
                "Levofloxacin",
                "Dùng 10-14 ngày (theo chỉ định bác sĩ)"
            ],
            "note": "⚠️ Hầu hết viêm xoang mạn KHÔNG cần kháng sinh trừ khi có nhiễm trùng rõ!"
        },
        "antihistamines": {
            "title": "Thuốc kháng histamine (Nếu do dị ứng):",
            "examples": [
                "Loratadine (Claritin)",
                "Cetirizine (Zyrtec)",
                "Fexofenadine (Allegra)"
            ],
            "use": "Giảm nghẹt mũi, hắt hơi do dị ứng"
        },
        "decongestants": {
            "title": "Thuốc thông mũi (Dùng ngắn hạn):",
            "examples": [
                "Pseudoephedrine (Sudafed)",
                "Xylometazoline xịt mũi (không dùng >7 ngày)"
            ],
            "warning": "⚠️ Chỉ dùng ngắn hạn (3-7 ngày). Dùng lâu → Phụ thuộc, nghẹt mũi nặng hơn!"
        }
    },
    
    "lifestyle": {
        "title": "💧 Thay đổi lối sống:",
        "tips": [
            "✅ Rửa mũi bằng nước muối hàng ngày",
            "✅ TRÁNH: Khói thuốc, bụi, hóa chất (làm nặng viêm)",
            "✅ Giữ ẩm không khí - Dùng máy tạo ẩm",
            "✅ Uống đủ nước (2-3 lít/ngày) - Làm loãng dịch",
            "✅ TRÁNH: Thay đổi nhiệt độ đột ngột",
            "✅ Xông hơi - Xông mặt với nước nóng (giảm nghẹt)",
            "✅ Tránh dị nguyên (nếu do dị ứng) - Bụi, phấn hoa, lông thú"
        ]
    },
    
    "surgery": {
        "title": "🔬 Phẫu thuật (Khi thuốc không hiệu quả):",
        "when": [
            "Điều trị thuốc 3-6 tháng không hiệu quả",
            "Có polyp mũi (khối u lành tính trong mũi)",
            "Cấu trúc mũi bất thường (vẹo vách ngăn)",
            "Triệu chứng nặng, ảnh hưởng nhiều"
        ],
        "method": "Nội soi mũi xoang (FESS) - Mở thông xoang, lấy polyp",
        "benefits": "Giảm triệu chứng rõ rệt, lâu dài",
        "recovery": "Hồi phục 1-2 tuần, cần rửa mũi sau mổ"
    },
    
    "when_to_see_doctor": {
        "title": "🏥 Khi nào cần khám bác sĩ:",
        "regular": "Khám định kỳ khi đang điều trị",
        "urgent": [
            "🚨 Sốt cao, đau mặt dữ dội",
            "🚨 Sưng đỏ quanh mắt",
            "🚨 Nhìn đôi, nhìn mờ",
            "🚨 Cứng cổ, nhức đầu dữ dội"
        ]
    }
}

