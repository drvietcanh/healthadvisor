"""
Viêm Tai Giữa (Otitis Media)
=============================
Bao gồm: Viêm tai giữa cấp, Viêm tai giữa mạn
"""

OTITIS_MEDIA_INFO = {
    "name_vn": "Viêm Tai Giữa",
    "name_en": "Otitis Media",
    
    "simple_explanation": """
💡 **Viêm tai giữa là gì?**

Giống như nước đọng trong tai:
- **Tai giữa bị viêm**, có dịch/mủ
- **Đau tai** dữ dội (đặc biệt ở trẻ em)
- **Có thể chảy mủ** ra ngoài (màng nhĩ thủng)

→ Giống như nước mưa đọng, cần tháo nước để khô ráo!
    """,
    
    "what_happens": """
Chuyện gì xảy ra:

1. **Tai giữa bị viêm:**
   - Tai có 3 phần: Tai ngoài → Tai giữa → Tai trong
   - Tai giữa có màng nhĩ (ngăn với tai ngoài)
   - Tai giữa thông với mũi qua ống Eustachian

2. **Viêm cấp tính:**
   - Ống Eustachian bị tắc (do cảm, viêm mũi)
   - Vi khuẩn vào tai giữa → Viêm, tạo mủ
   - Mủ đẩy màng nhĩ → Đau dữ dội
   - Màng nhĩ có thể thủng → Chảy mủ ra ngoài

3. **Viêm mạn tính:**
   - Màng nhĩ thủng lâu ngày, không lành
   - Tai giữa ẩm ướt → Dễ viêm tái phát
   - Nghe kém (do màng nhĩ thủng)
    """,
    
    "symptoms": {
        "acute": [
            "Đau tai dữ dội (đặc biệt ở trẻ em)",
            "Sốt (38-39°C)",
            "Quấy khóc, không ngủ được (ở trẻ nhỏ)",
            "Nghe kém (như bị bịt tai)",
            "Chảy mủ tai (nếu màng nhĩ thủng) - Đau giảm sau khi chảy mủ",
            "Ù tai, chóng mặt (ít gặp)"
        ],
        "chronic": [
            "Chảy mủ tai kéo dài (>3 tháng)",
            "Nghe kém (do màng nhĩ thủng)",
            "Không đau (hoặc đau nhẹ)",
            "Có mùi hôi (do nhiễm trùng mạn)"
        ],
        "in_children": [
            "👶 Trẻ em:",
            "   - Quấy khóc, không ngủ",
            "   - Sốt, bỏ ăn",
            "   - Kéo/gãi tai",
            "   - Không nghe được (gọi không quay lại)"
        ]
    },
    
    "causes": {
        "main": [
            "🦠 **Nhiễm vi khuẩn:**",
            "   - Streptococcus pneumoniae (phổ biến nhất)",
            "   - Haemophilus influenzae",
            "   - Vi khuẩn từ mũi → Vào tai giữa qua ống Eustachian",
            "",
            "🌬️ **Viêm mũi xoang:**",
            "   - Cảm cúm, viêm mũi → Ống Eustachian bị tắc",
            "   - Dịch mũi vào tai giữa → Viêm",
            "",
            "👶 **Ở trẻ em:**",
            "   - Ống Eustachian ngắn, nằm ngang → Dễ tắc",
            "   - Sức đề kháng yếu → Dễ nhiễm trùng",
            "",
            "🚭 **Yếu tố nguy cơ:**",
            "   - Hút thuốc thụ động (trẻ em)",
            "   - Đi nhà trẻ (tiếp xúc với vi khuẩn)",
            "   - Bú bình nằm (sữa vào tai giữa)",
            "   - Dị ứng, hen suyễn"
        ],
        "chronic": [
            "Viêm cấp không điều trị đúng → Chuyển mạn",
            "Màng nhĩ thủng không lành",
            "Tai giữa ẩm ướt → Dễ viêm tái phát",
            "Có thể có polyp trong tai giữa"
        ]
    },
    
    "treatment": {
        "acute": {
            "title": "🚨 Điều trị viêm tai giữa cấp:",
            "medications": [
                "**Kháng sinh:**",
                "   - Amoxicillin (liều cao) - 7-10 ngày",
                "   - Hoặc Amoxicillin-Clavulanate (nếu kháng thuốc)",
                "   - ⚠️ Phải uống đủ liều, không bỏ giữa chừng",
                "",
                "**Giảm đau, hạ sốt:**",
                "   - Paracetamol (10-15mg/kg) - Mỗi 4-6 giờ",
                "   - Ibuprofen (nếu >6 tháng tuổi) - Giảm đau tốt hơn",
                "",
                "**Nhỏ tai (nếu màng nhĩ chưa thủng):**",
                "   - Ofloxacin ear drops",
                "   - Giúp giảm đau, chống viêm"
            ],
            "when_to_see_doctor": [
                "✅ Đau tai dữ dội",
                "✅ Sốt > 38.5°C",
                "✅ Chảy mủ tai",
                "✅ Nghe kém",
                "✅ Trẻ em quấy khóc, bỏ ăn"
            ]
        },
        "chronic": {
            "title": "🏥 Điều trị viêm tai giữa mạn:",
            "treatment": [
                "**Vệ sinh tai:**",
                "   - Rửa tai tại phòng khám (hút mủ)",
                "   - Nhỏ tai: Ciprofloxacin ear drops",
                "   - Làm khô tai giữa",
                "",
                "**Phẫu thuật (nếu cần):**",
                "   - Đặt ống thông khí (Ventilation tube):",
                "   - Tạo lỗ nhỏ trên màng nhĩ",
                "   - Đặt ống nhỏ để thông khí",
                "   - Giúp tai giữa khô ráo, không viêm",
                "",
                "   - Phẫu thuật vá màng nhĩ:",
                "   - Nếu màng nhĩ thủng lớn",
                "   - Lấy mô tự thân để vá",
                "   - Cải thiện thính lực"
            ]
        },
        "complications": {
            "title": "⚠️ Biến chứng (nếu không điều trị):",
            "list": [
                "**Viêm xương chũm (Mastoiditis):**",
                "   - Xương sau tai bị viêm",
                "   - Sưng đỏ sau tai, đau",
                "   - Cần phẫu thuật",
                "",
                "**Viêm màng não:**",
                "   - Vi khuẩn vào não",
                "   - Nguy hiểm tính mạng",
                "",
                "**Điếc vĩnh viễn:**",
                "   - Màng nhĩ thủng không lành",
                "   - Tổn thương xương tai giữa",
                "",
                "**Liệt mặt:**",
                "   - Dây thần kinh mặt bị ảnh hưởng",
                "   - Hiếm nhưng nguy hiểm"
            ]
        }
    },
    
    "prevention": {
        "title": "🛡️ Cách phòng ngừa viêm tai giữa:",
        "tips": [
            "✅ **Tiêm phòng:**",
            "   - Vắc-xin phế cầu (Pneumococcal vaccine)",
            "   - Vắc-xin cúm",
            "   - Giảm nguy cơ viêm tai giữa",
            "",
            "✅ **Điều trị viêm mũi xoang:**",
            "   - Cảm cúm, viêm mũi → Điều trị sớm",
            "   - Xịt mũi nước muối",
            "   - Xì mũi đúng cách (bịt một bên)",
            "",
            "✅ **Tránh bú bình nằm:**",
            "   - Cho trẻ bú ngồi/đứng",
            "   - Tránh sữa vào tai giữa",
            "",
            "✅ **Tránh hút thuốc thụ động:**",
            "   - Không hút thuốc gần trẻ em",
            "   - Khói thuốc → Dễ viêm tai",
            "",
            "✅ **Vệ sinh tai đúng cách:**",
            "   - Không đưa tăm bông sâu vào tai",
            "   - Chỉ lau vành tai",
            "   - Nếu ráy tai nhiều → Đến bác sĩ rửa",
            "",
            "✅ **Điều trị đúng và đủ liều:**",
            "   - Uống kháng sinh đủ 7-10 ngày",
            "   - Không bỏ giữa chừng → Tránh chuyển mạn"
        ]
    },
    
    "note": """
⚠️ **LƯU Ý QUAN TRỌNG:**

**VIÊM TAI GIỮA CẤP:",
- Cần điều trị sớm với kháng sinh",
- ⚠️ Phải uống đủ liều (7-10 ngày) - Không bỏ giữa chừng!",
- Nếu không điều trị → Chuyển mạn, biến chứng",

**Ở TRẺ EM:",
- Đau tai dữ dội, sốt → Đi khám ngay",
- Không tự ý nhỏ thuốc vào tai (nếu không biết màng nhĩ thủng chưa)",
- Nếu chảy mủ tai → Đau giảm nhưng vẫn cần điều trị",

**VIÊM TAI GIỮA MẠN:",
- Màng nhĩ thủng không lành → Cần phẫu thuật",
- Vệ sinh tai thường xuyên tại phòng khám",
- Tránh nước vào tai (khi tắm, bơi)"
    """
}

