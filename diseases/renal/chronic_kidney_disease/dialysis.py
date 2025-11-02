"""
Suy Thận Mạn - Chạy thận nhân tạo
Dialysis for End-Stage Kidney Disease
"""

from typing import Dict, List

DIALYSIS = {
    "when_needed": {
        "title": "⏰ Khi Nào Cần Chạy Thận?",
        "description": "Chạy thận khi thận không còn lọc được đủ:",
        "indicators": [
            {
                "name": "Giai đoạn 5",
                "criteria": "eGFR <15 mL/phút",
                "description": "Thận chỉ còn <15% chức năng"
            },
            {
                "name": "Triệu chứng nặng",
                "symptoms": [
                    "Mệt mỏi cực độ (không làm được gì)",
                    "Buồn nôn, nôn nhiều",
                    "Phù nặng, khó thở (phù phổi)",
                    "Lơ mơ, co giật (nhiễm độc ure)",
                    "Kali máu rất cao → Loạn nhịp tim nguy hiểm"
                ],
                "note": "Có thể cần chạy thận sớm hơn (eGFR 10-15) nếu có triệu chứng"
            },
            {
                "name": "Mất cân bằng nước, điện giải",
                "conditions": [
                    "Phù phổi (không đáp ứng thuốc lợi tiểu)",
                    "Kali máu >6.5 mEq/L (nguy hiểm tính mạng)",
                    "Toan chuyển hóa nặng"
                ]
            }
        ],
        "timing": "💡 Thường bắt đầu khi eGFR = 10-12 mL/phút"
    },
    
    "types": {
        "title": "🔬 Các Loại Chạy Thận",
        "description": "Có 2 phương pháp chính:",
        "hemodialysis": {
            "name": "Chạy Thận Nhân Tạo (Hemodialysis)",
            "description": "Lọc máu qua máy",
            "how": [
                "Rút máu từ tĩnh mạch",
                "Máu đi qua máy lọc (có màng lọc)",
                "Máy loại bỏ chất độc, nước dư",
                "Máu sạch trả lại cơ thể"
            ],
            "frequency": "3 lần/tuần, mỗi lần 4 giờ",
            "location": [
                "Trung tâm chạy thận (bệnh viện)",
                "Hoặc tại nhà (nếu có điều kiện)"
            ],
            "access": {
                "title": "Cách tiếp cận mạch máu:",
                "types": [
                    {
                        "name": "Fistula (Cầu nối động-tĩnh mạch)",
                        "description": "Nối động mạch với tĩnh mạch ở cánh tay",
                        "benefit": "Tốt nhất, ít biến chứng",
                        "timing": "Phải làm trước 3-6 tháng khi chạy thận"
                    },
                    {
                        "name": "Graft (Ghép mạch nhân tạo)",
                        "description": "Dùng ống nhân tạo nối động-tĩnh mạch",
                        "when": "Khi không làm được fistula"
                    },
                    {
                        "name": "Catheter (Ống thông tĩnh mạch)",
                        "description": "Ống thông ở cổ, ngực",
                        "when": "Tạm thời, hoặc khi không làm được fistula/graft",
                        "risk": "Nguy cơ nhiễm trùng cao"
                    }
                ]
            },
            "life_with_dialysis": {
                "title": "Cuộc sống với chạy thận:",
                "challenges": [
                    "Phải đến trung tâm 3 lần/tuần (mất 4 giờ/lần)",
                    "Chế độ ăn chặt chẽ (ít muối, ít kali, ít phốt pho)",
                    "Hạn chế nước uống (tránh phù)",
                    "Mệt mỏi sau chạy thận (1-2 giờ)",
                    "Chi phí cao (100-200 triệu/năm)"
                ],
                "benefits": [
                    "Giữ được sự sống",
                    "Giảm triệu chứng (mệt mỏi, buồn nôn)",
                    "Cải thiện chất lượng sống (so với không chạy)"
                ]
            }
        },
        "peritoneal_dialysis": {
            "name": "Lọc Màng Bụng (Peritoneal Dialysis)",
            "description": "Lọc máu qua màng bụng",
            "how": [
                "Bơm dịch lọc vào bụng qua ống thông",
                "Màng bụng lọc máu (như bộ lọc)",
                "Sau vài giờ, rút dịch ra (có chất độc)",
                "Lặp lại 4-5 lần/ngày"
            ],
            "advantage": [
                "Tự làm tại nhà",
                "Linh hoạt hơn về thời gian",
                "Ít ảnh hưởng đến cuộc sống"
            ],
            "disadvantage": [
                "Nguy cơ nhiễm trùng màng bụng",
                "Cần người nhà hỗ trợ",
                "Không phù hợp mọi người"
            ]
        }
    },
    
    "preparation": {
        "title": "🏥 Chuẩn Bị Chạy Thận",
        "description": "Chuẩn bị trước khi chạy thận:",
        "steps": [
            {
                "name": "Giáo dục bệnh nhân và gia đình",
                "topics": [
                    "Chạy thận là gì, tại sao cần",
                    "Cuộc sống với chạy thận",
                    "Chế độ ăn, nước uống",
                    "Biến chứng có thể gặp"
                ]
            },
            {
                "name": "Tạo cầu nối mạch máu (Fistula)",
                "timing": "3-6 tháng trước khi chạy thận",
                "why": "Fistula cần thời gian trưởng thành",
                "warning": "⚠️ Đừng đợi đến khi suy thận nặng mới làm!"
            },
            {
                "name": "Điều trị biến chứng",
                "items": [
                    "Thiếu máu (EPO, sắt)",
                    "Loãng xương (vitamin D)",
                    "Tăng huyết áp"
                ]
            },
            {
                "name": "Chuẩn bị tâm lý",
                "description": "Chạy thận là điều trị SUỐT ĐỜI (trừ khi ghép thận)",
                "support": [
                    "Tư vấn tâm lý",
                    "Gia đình hỗ trợ",
                    "Tham gia nhóm bệnh nhân chạy thận"
                ]
            }
        ]
    },
    
    "kidney_transplant": {
        "title": "🫘 Ghép Thận",
        "description": "Phương pháp tốt nhất cho suy thận giai đoạn cuối:",
        "benefits": [
            "Không cần chạy thận",
            "Chất lượng sống tốt hơn chạy thận",
            "Tuổi thọ cao hơn",
            "Ít biến chứng hơn"
        ],
        "sources": [
            {
                "name": "Thận người chết não (cadaveric)",
                "availability": "Rất ít, phải chờ đợi lâu",
                "waiting_time": "2-5 năm (thậm chí lâu hơn)"
            },
            {
                "name": "Thận người sống",
                "donors": "Người thân trong gia đình",
                "benefit": "Không phải chờ, thận tốt hơn",
                "requirement": "Phù hợp nhóm máu, mô"
            }
        ],
        "post_transplant": {
            "title": "Sau ghép thận:",
            "medications": [
                "Thuốc ức chế miễn dịch (suốt đời)",
                "Ngăn thận ghép bị đào thải",
                "Có nguy cơ nhiễm trùng cao"
            ],
            "monitoring": "Khám định kỳ, xét nghiệm máu thường xuyên",
            "survival": "Tỷ lệ sống 90-95% sau 5 năm (nếu tuân thủ điều trị)"
        }
    }
}

