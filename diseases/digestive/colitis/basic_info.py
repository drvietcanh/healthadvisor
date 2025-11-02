"""
Viêm Đại Tràng (Colitis) - Thông tin cơ bản
"""

COLITIS_INFO = {
    "name": "Viêm Đại Tràng",
    "name_en": "Colitis",
    
    "simple_explanation": """
💡 Viêm đại tràng là gì? (Giải thích đơn giản)

Đại tràng (ruột già) là nơi hấp thu nước từ thức ăn, tạo phân:
- BÌNH THƯỜNG: Đại tràng khỏe, hấp thu nước tốt
- VIÊM: Đại tràng bị viêm → Sưng, đau, tiết nhiều dịch → Tiêu chảy, đau bụng

🫀 Chuyện gì xảy ra:
1. Đại tràng bị viêm (do nhiễm trùng, tự miễn, rối loạn)
2. Niêm mạc đại tràng sưng, đỏ → Đau bụng (thường bên trái)
3. Đại tràng không hấp thu nước tốt → Phân lỏng, đi nhiều lần
4. Có thể có máu trong phân (viêm nặng)

⚠️ ĐẶC ĐIỂM:
- Có thể cấp tính (nhiễm trùng) hoặc mạn tính (rối loạn)
- Đau bụng đặc trưng: Đau quặn, đi ngoài xong đỡ đau
- Cần điều trị kéo dài (mạn tính)
    """,
    
    "types": {
        "infectious": {
            "name": "Viêm đại tràng nhiễm trùng",
            "cause": "Vi khuẩn (E. coli, Salmonella, C. difficile)",
            "duration": "Cấp tính, kéo dài vài ngày đến vài tuần",
            "severity": "Thường tự khỏi hoặc khỏi sau điều trị"
        },
        "ibd": {
            "name": "Viêm đại tràng tự miễn (IBD)",
            "cause": "Rối loạn hệ miễn dịch tấn công đại tràng",
            "duration": "Mạn tính, tái phát",
            "types": [
                "Viêm đại tràng loét (Ulcerative Colitis)",
                "Bệnh Crohn"
            ],
            "severity": "Cần điều trị lâu dài, theo dõi định kỳ"
        },
        "ischemic": {
            "name": "Viêm đại tràng thiếu máu",
            "cause": "Mạch máu nuôi đại tràng bị tắc (người già)",
            "severity": "Nguy hiểm, cần điều trị ngay"
        }
    },
    
    "prevalence": {
        "statistics": "Phổ biến ở người già, người có bệnh nền",
        "note": "Cần phân biệt với hội chứng ruột kích thích (IBS - không viêm thật)"
    }
}

