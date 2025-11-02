"""
Chàm Khô (Eczema/Dermatitis)
==============================
"""

ECZEMA_INFO = {
    "name_vn": "Chàm Khô",
    "name_en": "Eczema/Dermatitis",
    
    "simple_explanation": """
💡 **Chàm khô là gì?**

Giống như da bị "khô nứt" và "viêm":
- **Da khô** → Mất độ ẩm, mất lớp bảo vệ
- **Da viêm** → Đỏ, ngứa, có thể có mụn nước
- **Mãn tính** → Tái phát nhiều lần

→ Giống như đất khô cằn, cần tưới nước (dưỡng ẩm)!
    """,
    
    "what_happens": """
Chuyện gì xảy ra:

1. **Da mất độ ẩm:**
   - Lớp bảo vệ da bị yếu
   - Da khô, nứt nẻ

2. **Chất gây dị ứng/kích ứng xâm nhập:**
   - Qua da khô → Vào sâu trong da
   - Gây viêm → Da đỏ, ngứa

3. **Vòng lặp:**
   - Ngứa → Gãi → Da tổn thương → Ngứa hơn
   - Khó thoát khỏi nếu không điều trị đúng
    """,
    
    "types": {
        "atopic_dermatitis": {
            "name": "Chàm thể tạng (Atopic Dermatitis)",
            "description": "Bệnh mãn tính, thường ở trẻ em, có thể kéo dài đến tuổi già",
            "common_locations": ["Khuỷu tay", "Đầu gối", "Cổ", "Mặt (trẻ em)"]
        },
        "contact_dermatitis": {
            "name": "Viêm da tiếp xúc (Contact Dermatitis)",
            "description": "Dị ứng/kích ứng với chất cụ thể (kim loại, hóa chất, mỹ phẩm)",
            "common_locations": ["Tay (tiếp xúc hóa chất)", "Cổ tay (đồng hồ)", "Tai (bông tai)"]
        },
        "seborrheic_dermatitis": {
            "name": "Viêm da tiết bã (Seborrheic Dermatitis)",
            "description": "Vảy da đầu, ngực, mặt (do nấm men)",
            "common_locations": ["Da đầu (gàu)", "Lông mày", "Ngực"]
        }
    },
    
    "symptoms": {
        "common": [
            "Da khô, nứt nẻ (như đất khô)",
            "Ngứa dữ dội (đặc biệt vào ban đêm)",
            "Da đỏ, sưng (do viêm)",
            "Có thể có mụn nước nhỏ (rất ngứa)",
            "Da dày lên, có vảy (nếu bị lâu)",
            "Vết xước (do gãi)"
        ],
        "progression": [
            "🔴 **Giai đoạn cấp (Bùng phát):**",
            "   - Đỏ, ngứa dữ dội",
            "   - Có mụn nước, chảy nước",
            "",
            "🟡 **Giai đoạn bán cấp:**",
            "   - Đỏ nhẹ hơn",
            "   - Da khô, có vảy",
            "",
            "🟢 **Giai đoạn mạn (Da dày):**",
            "   - Da dày, sẫm màu",
            "   - Nứt nẻ, có thể đau"
        ]
    },
    
    "causes": {
        "main": [
            "Yếu tố di truyền (da nhạy cảm từ nhỏ)",
            "Da khô do môi trường (thời tiết lạnh, khô)",
            "Chất gây dị ứng (phấn hoa, bụi, lông động vật)",
            "Chất kích ứng (xà phòng, nước rửa chén, chất tẩy)",
            "Căng thẳng, lo lắng (làm bùng phát)",
            "Thay đổi thời tiết (nóng sang lạnh)"
        ],
        "triggers": [
            "🧴 **Hóa chất:** Xà phòng, nước rửa chén, chất tẩy",
            "🧵 **Vải:** Len, vải thô (cọ xát da)",
            "🌡️ **Thời tiết:** Lạnh, khô (mùa đông)",
            "💧 **Nước nóng:** Tắm nước nóng → Mất độ ẩm da",
            "😰 **Căng thẳng:** Stress → Bùng phát",
            "🍜 **Thức ăn:** Một số người dị ứng thức ăn (sữa, trứng, đậu nành)"
        ]
    },
    
    "treatment": {
        "home_care": {
            "title": "🏠 Xử trí tại nhà:",
            "steps": [
                "1. **Dưỡng ẩm da (QUAN TRỌNG NHẤT):**",
                "   - Bôi kem dưỡng ẩm 2-3 lần/ngày",
                "   - Ngay sau khi tắm (da còn ẩm)",
                "   - Chọn kem không mùi, không cồn",
                "   - Ví dụ: Cetaphil, Eucerin, Vaseline",
                "",
                "2. **Tránh chất kích ứng:**",
                "   - Không dùng xà phòng có mùi thơm",
                "   - Mang găng tay khi rửa chén",
                "   - Tránh vải len (mặc cotton)",
                "",
                "3. **Không gãi:**",
                "   - Gãi → Da tổn thương → Nặng hơn",
                "   - Cắt móng tay ngắn",
                "   - Đắp khăn lạnh nếu ngứa quá",
                "",
                "4. **Tắm đúng cách:**",
                "   - Nước ấm (không nóng)",
                "   - Không tắm quá 10 phút",
                "   - Dùng sữa tắm dịu nhẹ (không xà phòng)",
                "   - Bôi kem dưỡng ẩm ngay sau tắm",
                "",
                "5. **Thuốc bôi không cần kê đơn:**",
                "   - Hydrocortisone 1% (bôi 2 lần/ngày, tối đa 2 tuần)",
                "   - Calamine lotion (làm dịu ngứa)"
            ],
            "duration": "⏰ **Thời gian:** 2-4 tuần để thấy cải thiện"
        },
        "when_to_see_doctor": {
            "title": "🏥 Khi nào cần đi khám bác sĩ:",
            "reasons": [
                "❌ Ngứa quá, ảnh hưởng giấc ngủ",
                "❌ Da có mủ, sưng (nhiễm trùng)",
                "❌ Bôi thuốc 2 tuần mà không đỡ",
                "❌ Chàm lan rộng (nhiều chỗ trên người)",
                "❌ Có vết nứt sâu, chảy máu",
                "❌ Ảnh hưởng sinh hoạt hàng ngày"
            ]
        },
        "doctor_treatment": {
            "title": "💊 Bác sĩ sẽ làm gì:",
            "options": [
                "💊 **Thuốc bôi corticoid:**",
                "   - Mometasone, Clobetasol (mạnh hơn)",
                "   - Bôi 1-2 lần/ngày, tối đa 2 tuần",
                "   - ⚠️ Không bôi lâu (teo da)",
                "",
                "💊 **Thuốc kháng histamine:**",
                "   - Cetirizine, Loratadine (uống)",
                "   - Giảm ngứa, đặc biệt ban đêm",
                "",
                "💊 **Thuốc bôi ức chế miễn dịch (nếu nặng):**",
                "   - Tacrolimus, Pimecrolimus",
                "   - Không phải corticoid → An toàn hơn",
                "",
                "💊 **Thuốc uống (nếu rất nặng):**",
                "   - Prednisolone (corticoid uống) - Ngắn hạn",
                "   - Cyclosporine - Ít dùng",
                "",
                "🔬 **Xét nghiệm dị ứng (nếu cần):**",
                "   - Xác định chất gây dị ứng",
                "   - Tránh tiếp xúc"
            ]
        }
    },
    
    "prevention": {
        "title": "🛡️ Cách phòng ngừa và kiểm soát chàm:",
        "tips": [
            "✅ **Dưỡng ẩm hàng ngày:**",
            "   - Bôi kem dưỡng ẩm 2-3 lần/ngày",
            "   - Đặc biệt sau tắm, rửa tay",
            "   - Ngay cả khi da không khô (phòng ngừa)",
            "",
            "✅ **Tránh chất kích ứng:**",
            "   - Xà phòng dịu nhẹ, không mùi",
            "   - Tránh nước quá nóng",
            "   - Mang găng tay khi làm việc nhà",
            "",
            "✅ **Quần áo cotton:**",
            "   - Tránh vải len, thô (cọ xát da)",
            "   - Giặt quần áo bằng bột giặt dịu nhẹ",
            "",
            "✅ **Quản lý căng thẳng:**",
            "   - Ngủ đủ giấc",
            "   - Tập thể dục, thư giãn",
            "   - Stress → Bùng phát chàm",
            "",
            "✅ **Theo dõi thời tiết:**",
            "   - Mùa đông: Dưỡng ẩm nhiều hơn",
            "   - Mùa hè: Tránh mồ hôi (kích ứng da)",
            "",
            "✅ **Nếu đã biết chất gây dị ứng:**",
            "   - Tránh tiếp xúc hoàn toàn",
            "   - Đọc nhãn sản phẩm (kiểm tra thành phần)"
        ]
    },
    
    "note": """
⚠️ **LƯU Ý QUAN TRỌNG:**
- Chàm là bệnh mãn tính → Không thể "chữa khỏi hoàn toàn"
- Mục tiêu: Kiểm soát, giảm bùng phát
- Dưỡng ẩm là nền tảng → Phải làm hàng ngày
- Thuốc corticoid bôi chỉ dùng ngắn hạn (tối đa 2 tuần)
- Gãi → Nặng hơn → Phải cố gắng không gãi
- Nếu có mủ, sưng → Có thể nhiễm trùng → Khám bác sĩ NGAY
    """
}

