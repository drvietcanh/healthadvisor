"""
Basic Gout Info - Thông tin cơ bản về bệnh Gút
"""

GOUT_INFO = {
    "title": "🦶 Bệnh Gút (Gout)",
    "simple_explanation": """
💡 Bệnh Gút là gì?

Giống như đường tan trong nước, acid uric trong máu cũng vậy.
- Khi acid uric QUÁ NHIỀU → Kết tinh thành tinh thể sắc nhọn
- Tinh thể này lắng đọng ở khớp → Đâm vào mô → ĐAU DỮ DỘI như bị dao đâm!
- Thường ở: Ngón chân cái (80%), gối, cổ chân, khuỷu tay

🕐 Ai dễ bị?
- Nam giới >40 tuổi (nữ ít hơn, thường sau mãn kinh)
- Uống nhiều rượu bia
- Ăn nhiều thịt đỏ, hải sản, nội tạng
- Thừa cân, béo phì
- Gia đình có người bị
- Dùng thuốc lợi tiểu (cho huyết áp cao)
- Bệnh thận
    """,
    
    "hyperuricemia": {
        "title": "⚠️ Tăng Acid Uric Máu (Chưa Phải Gút)",
        "explanation": """
💡 Acid uric cao nhưng CHƯA CÓ CƠN ĐAU:

🔍 Phân biệt:
- **Tăng acid uric máu:** Acid uric cao nhưng chưa có triệu chứng
- **Bệnh Gút:** Acid uric cao + CÓ CƠN ĐAU KHỚP

📊 Mức acid uric:
- Bình thường: Nam < 7 mg/dL (< 420 μmol/L), Nữ < 6 mg/dL (< 360 μmol/L)
- Tăng nhẹ: 7-8 mg/dL (420-480 μmol/L, chưa cần thuốc, chỉ thay đổi lối sống)
- Tăng cao: > 8 mg/dL (> 480 μmol/L, nguy cơ gút cao)
- Rất cao: > 9-10 mg/dL (> 540-600 μmol/L, nguy cơ rất cao)

⚠️ LƯU Ý QUAN TRỌNG:
- Chỉ 10-20% người acid uric cao → BỊ GÚT
- Nhiều người acid uric cao nhưng KHÔNG BAO GIỜ bị gút!
- → Không cần uống thuốc ngay khi chỉ tăng nhẹ!
        """,
        
        "when_to_treat": {
            "no_medication": {
                "title": "KHÔNG cần thuốc (Chỉ thay đổi lối sống):",
                "conditions": [
                    "Acid uric 7-8 mg/dL (420-480 μmol/L)",
                    "Chưa có cơn gút",
                    "Không có sỏi thận",
                    "Không có bệnh tim mạch, tiểu đường"
                ],
                "actions": [
                    "Giảm cân (nếu thừa cân)",
                    "Uống nhiều nước (2-3 lít/ngày)",
                    "Hạn chế rượu bia",
                    "Giảm thịt đỏ, hải sản",
                    "Tập thể dục",
                    "Xét nghiệm lại sau 6 tháng"
                ]
            },
            
            "consider_medication": {
                "title": "Cân nhắc thuốc:",
                "conditions": [
                    "Acid uric > 8-9 mg/dL (> 480-540 μmol/L)",
                    "Đã có >1 cơn gút",
                    "Có sỏi thận do acid uric",
                    "Có bệnh tim mạch, tiểu đường + acid uric cao"
                ],
                "note": "Cần tham khảo bác sĩ, không tự ý uống thuốc"
            }
        },
        
        "monitoring": [
            "Xét nghiệm acid uric 1-2 lần/năm",
            "Theo dõi triệu chứng (có cơn đau khớp không?)",
            "Kiểm tra chức năng thận",
            "Kiểm tra huyết áp, đường huyết"
        ]
    },
    
    "stages": {
        "asymptomatic": {
            "name": "Giai đoạn im lặng",
            "description": "Acid uric cao nhưng chưa có triệu chứng",
            "duration": "Có thể nhiều năm"
        },
        "acute": {
            "name": "Gút cấp - Cơn đau dữ dội",
            "description": "Viêm khớp đau như dao đâm, sưng nóng đỏ",
            "duration": "3-10 ngày, tự khỏi nhưng dễ tái phát"
        },
        "chronic": {
            "name": "Gút mạn",
            "description": "Nhiều cơn, tinh thể lắng đọng thành hạt tophi",
            "complications": "Hủy khớp, sỏi thận"
        }
    }
}

