"""
Viêm Họng Mạn Tính (Chronic Pharyngitis)
=========================================
Bao gồm: Viêm họng hạt, viêm họng do trào ngược
"""

CHRONIC_PHARYNGITIS_INFO = {
    "name_vn": "Viêm Họng Mạn Tính",
    "name_en": "Chronic Pharyngitis",
    
    "simple_explanation": """
💡 **Viêm họng mạn tính là gì?**

Giống như cổ họng bị \"xước\" mãi không lành:
- **Cổ họng đau rát** kéo dài (>3 tuần)
- **Có cảm giác vướng** như có vật gì trong họng
- **Ho khan**, khó nuốt

→ Khác với viêm họng cấp (đau vài ngày rồi khỏi)
    """,
    
    "what_happens": """
Chuyện gì xảy ra:

1. **Niêm mạc họng bị viêm kéo dài:**
   - Bình thường: Niêm mạc mềm mại, hồng
   - Viêm mạn: Niêm mạc đỏ, sưng, có thể có \"hạt\" (lymphoid follicles)

2. **Viêm họng hạt:**
   - Các hạch bạch huyết ở thành sau họng sưng to
   - Nhìn như có nhiều \"hạt\" nhỏ màu đỏ
   - Cảm giác vướng, khó chịu

3. **Có thể do nhiều nguyên nhân:**
   - Trào ngược dạ dày → Axit làm tổn thương họng
   - Hút thuốc lá, uống rượu
   - Môi trường khô, bụi
    """,
    
    "symptoms": {
        "common": [
            "Đau rát họng kéo dài (>3 tuần)",
            "Cảm giác vướng trong họng (như có vật gì)",
            "Ho khan, nhất là buổi sáng",
            "Khạc đờm nhầy trong suốt",
            "Nuốt khó, cảm giác nghẹn",
            "Khàn tiếng nhẹ (nếu viêm lan đến thanh quản)",
            "Hôi miệng (do viêm kéo dài)"
        ],
        "appearance": [
            "🔴 Thành sau họng đỏ, có thể sưng",
            "⚪ Có thể thấy \"hạt\" nhỏ (viêm họng hạt)",
            "⚪ Niêm mạc họng khô, mất độ ẩm",
            "⚪ Có thể có mảng trắng (nếu nhiễm nấm)"
        ]
    },
    
    "causes": {
        "main": [
            "🚬 **Hút thuốc lá:**",
            "   - Khói thuốc kích thích họng",
            "   - Làm khô niêm mạc",
            "   - Phổ biến nhất ở người hút thuốc",
            "",
            "🍷 **Uống rượu bia:**",
            "   - Rượu làm khô niêm mạc họng",
            "   - Kích thích viêm",
            "",
            "💨 **Trào ngược dạ dày (GERD):**",
            "   - Axit dạ dày trào lên → Đốt họng",
            "   - Đặc biệt khi nằm ngủ",
            "   - Triệu chứng: Ợ chua, đau họng buổi sáng",
            "",
            "🌬️ **Môi trường khô, bụi:**",
            "   - Điều hòa, máy sưởi → Không khí khô",
            "   - Bụi, khói công nghiệp",
            "   - Làm khô niêm mạc họng",
            "",
            "🦠 **Viêm mũi xoang mạn:**",
            "   - Dịch mũi chảy xuống họng → Kích thích",
            "   - Dịch có thể có vi khuẩn",
            "",
            "🍽️ **Thức ăn cay, nóng:**",
            "   - Kích thích niêm mạc họng",
            "   - Ăn nhiều → Viêm mạn"
        ],
        "other": [
            "Thở bằng miệng (ngạt mũi)",
            "Nói nhiều, nói to (giáo viên, ca sĩ)",
            "Dị ứng (phấn hoa, bụi nhà)",
            "Nhiễm trùng răng miệng"
        ]
    },
    
    "treatment": {
        "lifestyle": {
            "title": "🏠 Điều trị tại nhà (Quan trọng nhất):",
            "stop_smoking": [
                "🚭 **Bỏ thuốc lá:**",
                "   - Quan trọng nhất!",
                "   - Nếu không bỏ → Viêm họng không bao giờ khỏi",
                "   - Có thể dùng miếng dán nicotine, thuốc hỗ trợ"
            ],
            "reduce_alcohol": [
                "🍷 **Giảm rượu bia:**",
                "   - Tối đa 1-2 ly/ngày",
                "   - Uống nhiều nước sau khi uống rượu"
            ],
            "manage_reflux": [
                "💊 **Nếu do trào ngược dạ dày:**",
                "   - Uống thuốc giảm axit (Omeprazole, Esomeprazole)",
                "   - Ăn ít, chia nhiều bữa",
                "   - Không nằm ngay sau ăn (chờ 2-3 giờ)",
                "   - Kê gối cao khi ngủ"
            ],
            "humidify": [
                "💨 **Tăng độ ẩm không khí:**",
                "   - Máy tạo ẩm trong phòng ngủ",
                "   - Tránh điều hòa quá lạnh",
                "   - Uống nhiều nước (2-3 lít/ngày)"
            ],
            "gargle": [
                "🌊 **Súc họng:**",
                "   - Nước muối ấm (1/2 thìa muối + 1 cốc nước)",
                "   - 2-3 lần/ngày, sau ăn",
                "   - Giúp làm sạch, giảm viêm"
            ]
        },
        "medications": {
            "title": "💊 Thuốc (nếu cần):",
            "anti_inflammatory": [
                "**Chống viêm tại chỗ:**",
                "   - Xịt họng: Hexaspray, Locabiotal",
                "   - Ngậm viên: Strepsils, Lysopaine",
                "   - Giảm đau, chống viêm nhẹ"
            ],
            "antibiotics": [
                "**Kháng sinh:**",
                "   - Chỉ dùng nếu có nhiễm trùng",
                "   - Theo chỉ định bác sĩ",
                "   - ⚠️ Viêm họng mạn thường KHÔNG cần kháng sinh"
            ],
            "when_to_see_doctor": [
                "✅ Đau họng > 3 tuần",
                "✅ Đã thử điều trị tại nhà mà không đỡ",
                "✅ Có sốt, sưng hạch cổ",
                "✅ Nuốt khó, khó thở",
                "✅ Có tiền sử hút thuốc lá, uống rượu"
            ]
        },
        "doctor_treatment": {
            "title": "🏥 Bác sĩ sẽ làm gì:",
            "examination": [
                "🔍 Soi họng (xem thành sau họng)",
                "🔍 Soi mũi xoang (nếu nghi viêm xoang)",
                "🔍 Đánh giá trào ngược dạ dày"
            ],
            "procedures": [
                "**Đốt họng hạt (nếu có):**",
                "   - Dùng laser hoặc đốt điện",
                "   - Loại bỏ các \"hạt\" gây vướng",
                "   - Làm tại phòng khám, không đau"
            ],
            "referral": [
                "**Chuyển chuyên khoa nếu cần:**",
                "   - Tai Mũi Họng: Soi chi tiết",
                "   - Tiêu hóa: Nếu nghi trào ngược",
                "   - Nội tiết: Nếu nghi bệnh tuyến giáp"
            ]
        }
    },
    
    "prevention": {
        "title": "🛡️ Cách phòng ngừa viêm họng mạn:",
        "tips": [
            "✅ **Bỏ thuốc lá:**",
            "   - Quan trọng nhất!",
            "   - Nếu không bỏ → Viêm họng không bao giờ khỏi",
            "",
            "✅ **Giảm rượu bia:**",
            "   - Tối đa 1-2 ly/ngày",
            "   - Uống nhiều nước",
            "",
            "✅ **Tránh thức ăn cay, nóng:**",
            "   - Ăn vừa phải, không quá cay",
            "",
            "✅ **Tăng độ ẩm không khí:**",
            "   - Máy tạo ẩm",
            "   - Uống nhiều nước",
            "",
            "✅ **Điều trị trào ngược dạ dày:**",
            "   - Nếu có triệu chứng (ợ chua, đau họng buổi sáng)",
            "",
            "✅ **Vệ sinh răng miệng tốt:**",
            "   - Đánh răng 2 lần/ngày",
            "   - Súc miệng sau ăn",
            "",
            "✅ **Súc họng nước muối:**",
            "   - 1-2 lần/ngày",
            "   - Làm sạch, giảm viêm"
        ]
    },
    
    "note": """
⚠️ **LƯU Ý QUAN TRỌNG:**

**VIÊM HỌNG MẠN:**
- Cần điều trị lâu dài (1-3 tháng)",
- Quan trọng nhất: Thay đổi lối sống (bỏ thuốc, giảm rượu)",
- Không có thuốc \"chữa khỏi\" nếu vẫn tiếp tục hút thuốc",

**BỎ THUỐC LÁ:",
- ⚠️ Nếu vẫn hút thuốc → Viêm họng không bao giờ khỏi",
- Đây là yếu tố quan trọng nhất!",

**TRÀO NGƯỢC DẠ DÀY:",
- Nhiều người không biết mình bị",
- Triệu chứng: Ợ chua, đau họng buổi sáng, ho về đêm",
- Điều trị trào ngược → Viêm họng sẽ đỡ"
    """
}

