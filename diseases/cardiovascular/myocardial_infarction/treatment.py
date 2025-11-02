"""
Nhồi Máu Cơ Tim - Điều trị
Treatment of Myocardial Infarction
"""

from typing import Dict, List

TREATMENT = {
    "acute_treatment": {
        "title": "⚡ Điều Trị Cấp Cứu (Trong Bệnh Viện)",
        "description": "Điều trị ngay khi đến bệnh viện:",
        "methods": [
            {
                "name": "Can Thiệp Mạch Vành (PCI - Đặt Stent)",
                "description": "Phương pháp TỐT NHẤT - Mở mạch máu bằng ống thông",
                "how": [
                    "Luồn ống thông từ động mạch tay/chân lên tim",
                    "Bơm bóng mở rộng chỗ tắc",
                    "Đặt stent (lưới kim loại) để giữ mạch máu mở"
                ],
                "benefit": [
                    "Mở mạch máu NGAY → Cứu cơ tim tối đa",
                    "Tỷ lệ thành công 95%",
                    "Thời gian: 30-90 phút",
                    "Cứu được 90% cơ tim nếu làm trong 2 giờ đầu"
                ],
                "availability": "Chỉ có ở bệnh viện lớn (tỉnh, trung ương)",
                "cost": "Chi phí cao (15-30 triệu đồng)"
            },
            {
                "name": "Tiêu Sợi Huyết (Thrombolysis)",
                "description": "Tiêm thuốc phá vỡ cục máu đông",
                "how": [
                    "Tiêm thuốc vào tĩnh mạch",
                    "Thuốc theo máu đến tim → Phá cục máu đông",
                    "Mạch máu được mở lại"
                ],
                "benefit": [
                    "Có thể làm ở bệnh viện huyện (không cần phòng can thiệp)",
                    "Chi phí thấp hơn (2-5 triệu đồng)",
                    "Hiệu quả tốt nếu làm trong 3 giờ đầu"
                ],
                "limitations": [
                    "Chỉ hiệu quả trong 6 giờ đầu",
                    "Có nguy cơ chảy máu (1-2%)",
                    "Không dùng được nếu có chảy máu dạ dày, đột quỵ gần đây"
                ],
                "when_used": "Khi không có phòng can thiệp mạch vành"
            },
            {
                "name": "Điều Trị Nội Khoa (Thuốc)",
                "description": "Dùng thuốc để bảo vệ tim, ngăn tổn thương thêm",
                "medications": [
                    {
                        "name": "Aspirin",
                        "dosage": "300mg (nhai) ngay, sau đó 100mg/ngày",
                        "why": "Làm loãng máu, ngăn cục máu đông mới"
                    },
                    {
                        "name": "Clopidogrel (Plavix)",
                        "dosage": "300-600mg ngay, sau đó 75mg/ngày",
                        "why": "Làm loãng máu, thường dùng cùng aspirin"
                    },
                    {
                        "name": "Atorvastatin (Lipitor)",
                        "dosage": "80mg/ngày",
                        "why": "Giảm cholesterol, ổn định mảng xơ vữa"
                    },
                    {
                        "name": "Beta-blocker (Metoprolol)",
                        "dosage": "Theo chỉ định bác sĩ",
                        "why": "Giảm nhịp tim, giảm nhu cầu oxy của tim"
                    },
                    {
                        "name": "ACE-I (Captopril, Enalapril)",
                        "dosage": "Theo chỉ định bác sĩ",
                        "why": "Bảo vệ tim, giảm suy tim sau nhồi máu"
                    }
                ],
                "when_used": "Khi quá muộn (>12 giờ) hoặc không thể can thiệp/tiêu sợi huyết"
            }
        ]
    },
    
    "post_mi_care": {
        "title": "🏥 Chăm Sóc Sau Nhồi Máu",
        "description": "Điều trị sau khi ổn định:",
        "medications": {
            "title": "💊 Thuốc Phải Uống Suốt Đời (Không được ngừng!):",
            "must_take": [
                {
                    "name": "Aspirin 100mg",
                    "frequency": "Mỗi ngày",
                    "why": "Ngăn nhồi máu lại",
                    "warning": "⚠️ KHÔNG được ngừng trừ khi bác sĩ bảo!"
                },
                {
                    "name": "Clopidogrel 75mg",
                    "frequency": "Mỗi ngày, ít nhất 1 năm (nếu đặt stent)",
                    "why": "Ngăn stent bị tắc",
                    "warning": "⚠️ Ngừng sớm → Stent tắc → Nhồi máu lại!"
                },
                {
                    "name": "Statin (Atorvastatin, Rosuvastatin)",
                    "frequency": "Mỗi ngày",
                    "why": "Giảm cholesterol, ổn định mảng xơ vữa"
                },
                {
                    "name": "Beta-blocker",
                    "frequency": "Mỗi ngày",
                    "why": "Giảm nhịp tim, bảo vệ tim"
                },
                {
                    "name": "ACE-I hoặc ARB",
                    "frequency": "Mỗi ngày",
                    "why": "Bảo vệ tim, giảm suy tim"
                }
            ]
        },
        "monitoring": {
            "title": "📊 Theo Dõi",
            "items": [
                "Đo huyết áp, nhịp tim hàng ngày",
                "Tái khám sau 1 tuần, 1 tháng, 3 tháng, 6 tháng",
                "Xét nghiệm máu: Cholesterol, đường huyết",
                "Điện tim (ECG) định kỳ",
                "Siêu âm tim: Đánh giá chức năng tim"
            ]
        },
        "lifestyle": {
            "title": "🏃 Thay Đổi Lối Sống",
            "critical": [
                "🚭 BỎ THUỐC LÁ (quan trọng nhất!)",
                "🍽️ Ăn ít muối, ít mỡ, nhiều rau",
                "🏃 Tập thể dục đều đặn (theo hướng dẫn bác sĩ)",
                "😴 Ngủ đủ giấc, giảm căng thẳng",
                "⚖️ Kiểm soát cân nặng, huyết áp, đường huyết"
            ]
        }
    },
    
    "rehabilitation": {
        "title": "🏥 Phục Hồi Chức Năng Tim (Cardiac Rehabilitation)",
        "description": "Chương trình tập luyện có hướng dẫn sau nhồi máu",
        "benefits": [
            "Tăng sức khỏe tim mạch",
            "Giảm nguy cơ nhồi máu lại 25-30%",
            "Cải thiện chất lượng sống",
            "Giảm lo âu, trầm cảm"
        ],
        "phases": [
            {
                "phase": "Giai đoạn 1 (Trong viện, 3-7 ngày)",
                "activities": [
                    "Tập thở sâu",
                    "Đi lại nhẹ trong phòng",
                    "Giáo dục về bệnh"
                ]
            },
            {
                "phase": "Giai đoạn 2 (Sau ra viện, 3-6 tháng)",
                "activities": [
                    "Tập thể dục có hướng dẫn (đi bộ, đạp xe)",
                    "Theo dõi nhịp tim, huyết áp khi tập",
                    "Tăng dần cường độ"
                ]
            },
            {
                "phase": "Giai đoạn 3 (Dài hạn)",
                "activities": [
                    "Tập thể dục tại nhà",
                    "Duy trì lối sống lành mạnh"
                ]
            }
        ]
    }
}

