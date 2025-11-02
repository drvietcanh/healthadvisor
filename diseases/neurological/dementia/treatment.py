"""
Sa Sút Trí Tuệ - Điều trị
Treatment of Dementia
"""

from typing import Dict, List

TREATMENT = {
    "medications": {
        "title": "💊 Thuốc Điều Trị",
        "description": "Thuốc KHÔNG chữa khỏi, nhưng LÀM CHẬM tiến triển:",
        "drugs": [
            {
                "name": "Donepezil (Aricept)",
                "dosage": "5-10mg/ngày (uống buổi tối)",
                "how_it_works": "Tăng chất dẫn truyền thần kinh trong não",
                "benefit": [
                    "Làm chậm mất trí nhớ 6-12 tháng",
                    "Cải thiện chức năng nhận thức",
                    "Có thể giúp duy trì hoạt động hàng ngày lâu hơn"
                ],
                "side_effects": [
                    "Buồn nôn, nôn (thường trong tuần đầu)",
                    "Tiêu chảy",
                    "Mất ngủ",
                    "Chán ăn"
                ],
                "note": "⚠️ KHÔNG chữa khỏi, chỉ làm chậm. Cần uống đều đặn."
            },
            {
                "name": "Memantine (Namenda)",
                "dosage": "5-20mg/ngày",
                "how_it_works": "Bảo vệ tế bào não khỏi tổn thương",
                "benefit": [
                    "Làm chậm tiến triển (đặc biệt giai đoạn trung bình-nặng)",
                    "Giảm các triệu chứng hành vi (giận dữ, lo âu)"
                ],
                "side_effects": [
                    "Chóng mặt",
                    "Đau đầu",
                    "Táo bón"
                ],
                "when_used": "Thường dùng khi Donepezil không còn hiệu quả"
            },
            {
                "name": "Rivastigmine (Exelon)",
                "dosage": "Dạng uống hoặc dán da",
                "how_it_works": "Tương tự Donepezil",
                "benefit": "Hiệu quả tương đương Donepezil",
                "advantage": "Dán da → Ít tác dụng phụ tiêu hóa hơn"
            }
        ],
        "warning": "⚠️ Thuốc chỉ LÀM CHẬM, không chữa khỏi. Quan trọng nhất là CHĂM SÓC TỐT!"
    },
    
    "behavioral_symptoms": {
        "title": "😟 Điều Trị Triệu Chứng Hành Vi",
        "description": "Người sa sút trí tuệ thường có hành vi khó chịu:",
        "symptoms": [
            {
                "name": "Giận dữ, hung hăng",
                "treatment": [
                    "Giữ bình tĩnh, không tranh cãi",
                    "Chuyển hướng sự chú ý",
                    "Thuốc an thần nhẹ (theo chỉ định bác sĩ)"
                ]
            },
            {
                "name": "Nghi ngờ, hoang tưởng",
                "treatment": [
                    "Đừng cố giải thích (họ không hiểu)",
                    "Đồng tình, trấn an",
                    "Tránh tranh cãi về thực tế"
                ],
                "example": "Nếu họ nói 'Ai lấy đồ của tôi' → Đừng nói 'Không có ai', mà nói 'Để con tìm giúp'"
            },
            {
                "name": "Đi lang thang",
                "treatment": [
                    "Đảm bảo an toàn (khóa cửa, có người trông)",
                    "Đeo vòng tay có thông tin liên hệ",
                    "Thiết bị GPS (nếu có điều kiện)",
                    "Để họ đi trong phạm vi an toàn"
                ],
                "warning": "⚠️ Nguy cơ đi lạc, ngã → Rất nguy hiểm!"
            },
            {
                "name": "Ảo giác (nhìn thấy người không có)",
                "treatment": [
                    "Đừng nói 'Không có ai' (họ sẽ giận)",
                    "Nói 'Con không thấy, nhưng con ở đây với mẹ'",
                    "Thuốc chống loạn thần (theo chỉ định bác sĩ)",
                    "Kiểm tra mắt (có thể do mắt kém)"
                ]
            },
            {
                "name": "Mất ngủ, đi lại ban đêm",
                "treatment": [
                    "Tạo thói quen đi ngủ đều giờ",
                    "Tránh ngủ trưa quá dài",
                    "Tập thể dục ban ngày",
                    "Tránh cà phê, rượu buổi tối"
                ]
            }
        ]
    },
    
    "when_to_see_doctor": {
        "title": "👨‍⚕️ Khi Nào Cần Đi Khám?",
        "description": "Đi khám BÁC SĨ THẦN KINH nếu có:",
        "signs": [
            {
                "name": "Dấu hiệu sớm",
                "items": [
                    "Quên thường xuyên, ảnh hưởng cuộc sống",
                    "Khó làm việc quen thuộc",
                    "Thay đổi tính cách",
                    "Lú lẫn về thời gian, địa điểm"
                ],
                "when": "Đi khám NGAY khi phát hiện → Điều trị sớm = Hiệu quả tốt hơn"
            },
            {
                "name": "Triệu chứng nặng",
                "items": [
                    "Đi lạc, không tìm được về nhà",
                    "Không nhận ra người thân",
                    "Mất hoàn toàn khả năng tự chăm sóc",
                    "Hành vi nguy hiểm (đốt lửa, mở gas...)"
                ],
                "when": "Đi khám NGAY → Cần chăm sóc chuyên nghiệp"
            }
        ],
        "tests": [
            "Khám lâm sàng thần kinh",
            "Test trí nhớ (MMSE, MoCA)",
            "CT/MRI não (tìm tổn thương)",
            "Xét nghiệm máu (loại trừ nguyên nhân khác)"
        ]
    }
}

