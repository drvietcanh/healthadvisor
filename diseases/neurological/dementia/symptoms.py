"""
Sa Sút Trí Tuệ - Triệu chứng
Symptoms of Dementia
"""

from typing import Dict, List

SYMPTOMS = {
    "early_signs": {
        "title": "🔍 Dấu Hiệu Sớm (Giai Đoạn Đầu)",
        "description": "Phát hiện SỚM → Điều trị SỚM → Làm chậm tiến triển!",
        "signs": [
            {
                "name": "Quên thường xuyên",
                "icon": "🧠",
                "description": "Quên những việc vừa xảy ra, lặp lại câu hỏi",
                "examples": [
                    "Quên đã ăn cơm chưa (hỏi lại nhiều lần)",
                    "Quên tắt bếp, đóng cửa",
                    "Quên tên người quen",
                    "Đặt đồ vật sai chỗ (chìa khóa trong tủ lạnh)"
                ],
                "vs_normal": "⚠️ Khác với quên bình thường: Quên NGAY sau khi làm, không nhớ lại được"
            },
            {
                "name": "Khó tập trung, làm việc quen thuộc",
                "icon": "🤔",
                "description": "Khó làm những việc từng làm dễ dàng",
                "examples": [
                    "Không biết nấu món quen thuộc",
                    "Không biết dùng điện thoại, TV",
                    "Không biết đường về nhà (đi lạc)",
                    "Khó quản lý tiền bạc, thanh toán hóa đơn"
                ]
            },
            {
                "name": "Lú lẫn về thời gian, địa điểm",
                "icon": "🗓️",
                "description": "Không biết hôm nay thứ mấy, đang ở đâu",
                "examples": [
                    "Tưởng đang ở quá khứ (như năm 1980)",
                    "Không biết đang ở nhà mình hay nhà ai",
                    "Đi ra ngoài và quên đường về",
                    "Tưởng đang mùa hè nhưng đang mùa đông"
                ]
            },
            {
                "name": "Thay đổi tính cách",
                "icon": "😟",
                "description": "Tính cách thay đổi, dễ giận dữ, lo âu",
                "examples": [
                    "Người từng vui vẻ → Trở nên cáu gắt",
                    "Nghi ngờ người thân (tưởng lấy đồ của mình)",
                    "Lo âu, sợ hãi không rõ nguyên nhân",
                    "Mất hứng thú với sở thích cũ"
                ]
            },
            {
                "name": "Khó tìm từ ngữ",
                "icon": "💬",
                "description": "Khó diễn đạt, dùng từ sai, nói lặp lại",
                "examples": [
                    "Quên tên đồ vật quen thuộc (gọi 'cái đó' thay vì tên)",
                    "Lặp lại câu hỏi, câu chuyện nhiều lần",
                    "Khó theo dõi cuộc trò chuyện",
                    "Nói ít hơn, im lặng nhiều hơn"
                ]
            },
            {
                "name": "Khó đưa ra quyết định",
                "icon": "🤷",
                "description": "Khó lựa chọn, đưa ra quyết định",
                "examples": [
                    "Không biết mặc gì, ăn gì",
                    "Khó xử lý tình huống mới",
                    "Dễ bị lừa, làm theo người khác dễ dàng"
                ]
            }
        ],
        "note": "⚠️ Nếu có >2 dấu hiệu trên → Nên đi khám bác sĩ thần kinh!"
    },
    
    "moderate_stage": {
        "title": "🔍 Giai Đoạn Trung Bình",
        "description": "Triệu chứng rõ ràng hơn, cần người chăm sóc:",
        "signs": [
            {
                "name": "Mất trí nhớ nặng",
                "details": [
                    "Quên tên người thân (con, cháu)",
                    "Quên đã kết hôn, có con",
                    "Tưởng người đã chết vẫn còn sống",
                    "Quên quá khứ gần hoàn toàn"
                ]
            },
            {
                "name": "Mất định hướng",
                "details": [
                    "Không biết đang ở đâu",
                    "Đi lạc, không tìm được về nhà",
                    "Không nhận ra nhà mình",
                    "Cần có người đi cùng khi ra ngoài"
                ]
            },
            {
                "name": "Mất khả năng tự chăm sóc",
                "details": [
                    "Không biết tự tắm rửa, mặc quần áo",
                    "Không biết tự ăn (quên cách dùng đũa)",
                    "Tiểu tiện, đại tiện không tự chủ",
                    "Cần người chăm sóc 24/24"
                ]
            },
            {
                "name": "Thay đổi hành vi",
                "details": [
                    "Dễ giận dữ, hung hăng",
                    "Nghi ngờ, hoang tưởng (tưởng người thân hại mình)",
                    "Ảo giác (nhìn thấy người không có)",
                    "Đi lang thang không mục đích"
                ]
            }
        ]
    },
    
    "severe_stage": {
        "title": "🔍 Giai Đoạn Nặng",
        "description": "Mất hầu hết khả năng, cần chăm sóc hoàn toàn:",
        "signs": [
            "Không nhận ra bất kỳ ai (kể cả người thân)",
            "Không nói được (hoặc nói vô nghĩa)",
            "Không đi lại được, nằm liệt giường",
            "Không tự ăn được, phải đút",
            "Mất hoàn toàn kiểm soát tiểu tiện, đại tiện",
            "Không phản ứng với môi trường xung quanh"
        ],
        "duration": "Giai đoạn này thường kéo dài 1-3 năm trước khi tử vong"
    },
    
    "vs_normal_forgetfulness": {
        "title": "🔍 Phân Biệt: Quên Bình Thường vs Sa Sút Trí Tuệ",
        "description": "QUAN TRỌNG: Không phải quên nào cũng là sa sút trí tuệ!",
        "normal": {
            "name": "Quên bình thường (do tuổi tác):",
            "examples": [
                "Quên tên người mới gặp → Sau đó nhớ lại",
                "Quên để đồ vật ở đâu → Tự tìm được sau đó",
                "Quên việc ít quan trọng → Nhớ lại khi nhắc",
                "Vẫn tự chăm sóc được, sống độc lập",
                "Nhận biết mình quên → Tự cười, tự nhắc mình"
            ]
        },
        "dementia": {
            "name": "Sa sút trí tuệ:",
            "examples": [
                "Quên việc VỪA LÀM → Không nhớ lại được",
                "Quên tên người QUEN → Không nhớ lại được",
                "Quên cách làm việc QUEN THUỘC → Không tự làm được",
                "Mất khả năng tự chăm sóc → Cần người giúp",
                "KHÔNG nhận biết mình quên → Tức giận khi người khác nhắc"
            ]
        },
        "note": "⚠️ Nếu quên ẢNH HƯỞNG cuộc sống hàng ngày → Nên đi khám!"
    }
}

