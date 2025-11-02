"""
Sa Sút Trí Tuệ - Chăm Sóc
Care for People with Dementia
"""

from typing import Dict, List

CARE = {
    "communication": {
        "title": "💬 Cách Giao Tiếp Với Người Sa Sút Trí Tuệ",
        "description": "Giao tiếp đúng cách → Giảm căng thẳng, cải thiện chất lượng sống:",
        "principles": [
            {
                "name": "Nói đơn giản, rõ ràng",
                "how": [
                    "Nói từng câu ngắn, một ý",
                    "Nói chậm, rõ ràng",
                    "Nhìn vào mắt khi nói",
                    "Dùng tên riêng thay vì 'ông/bà'"
                ],
                "avoid": [
                    "Nói quá nhanh",
                    "Nói nhiều ý trong 1 câu",
                    "Dùng từ phức tạp",
                    "Hỏi câu hỏi khó ('Mẹ có nhớ...?')"
                ]
            },
            {
                "name": "Đừng tranh cãi về thực tế",
                "how": [
                    "Đừng nói 'Không phải', 'Sai rồi'",
                    "Đồng tình với cảm xúc (không phải sự kiện)",
                    "Chuyển hướng chủ đề",
                    "Trấn an thay vì giải thích"
                ],
                "example": [
                    "❌ SAI: 'Không có ai lấy đồ của mẹ!'",
                    "✅ ĐÚNG: 'Con hiểu mẹ lo lắng. Để con tìm giúp mẹ nhé.'"
                ]
            },
            {
                "name": "Lắng nghe, kiên nhẫn",
                "how": [
                    "Cho họ thời gian nói (không cắt ngang)",
                    "Lắng nghe cảm xúc (sợ hãi, lo âu)",
                    "Kiên nhẫn khi họ lặp lại",
                    "Tỏ ra quan tâm, không bực bội"
                ]
            },
            {
                "name": "Dùng cử chỉ, hình ảnh",
                "how": [
                    "Chỉ vào đồ vật khi nói",
                    "Làm mẫu (ví dụ: cách mặc áo)",
                    "Dùng ảnh, vật dụng quen thuộc",
                    "Hát, chơi nhạc (kích thích trí nhớ)"
                ]
            }
        ]
    },
    
    "daily_care": {
        "title": "🏠 Chăm Sóc Hàng Ngày",
        "description": "Giúp người sa sút trí tuệ sống an toàn, thoải mái:",
        "areas": [
            {
                "name": "An toàn trong nhà",
                "critical": [
                    "Khóa bếp ga, tắt bếp khi không dùng",
                    "Cất dao, kéo, vật sắc nhọn",
                    "Cất thuốc, hóa chất",
                    "Đảm bảo sàn nhà không trơn trượt",
                    "Gắn tay vịn ở nhà tắm, cầu thang",
                    "Để ánh sáng đủ (tránh vấp ngã ban đêm)"
                ],
                "warning": "⚠️ Người sa sút trí tuệ dễ quên tắt bếp, mở gas → Nguy hiểm cháy nổ!"
            },
            {
                "name": "Phòng ngừa đi lạc",
                "methods": [
                    "Đeo vòng tay có tên, số điện thoại",
                    "Dán thông tin liên hệ trong ví, túi",
                    "Chụp ảnh gần đây (để tìm nếu đi lạc)",
                    "Thông báo hàng xóm, bảo vệ",
                    "Thiết bị GPS (nếu có điều kiện)",
                    "Khóa cửa (nhưng có người trông)"
                ],
                "warning": "⚠️ Đi lạc → Nguy cơ ngã, tai nạn, mất tích!"
            },
            {
                "name": "Chăm sóc vệ sinh",
                "tips": [
                    "Nhắc nhở từng bước (từng bước một)",
                    "Làm mẫu (làm cùng họ)",
                    "Giữ thói quen (giờ tắm, giờ ăn đều)",
                    "Kiên nhẫn, không giục",
                    "Praise (khen ngợi) khi họ làm được"
                ],
                "if_resistant": [
                    "Đừng ép buộc (sẽ giận dữ)",
                    "Đợi lúc họ thoải mái hơn",
                    "Nhờ người họ tin tưởng nhắc"
                ]
            },
            {
                "name": "Ăn uống",
                "tips": [
                    "Ăn cùng bàn (không để ăn một mình)",
                    "Nhắc từng miếng (nếu quên cách dùng đũa)",
                    "Đút ăn nếu cần (giai đoạn nặng)",
                    "Thức ăn mềm, dễ nuốt (tránh nghẹn)",
                    "Uống đủ nước (nhắc nhở thường xuyên)"
                ],
                "warning": "⚠️ Quên ăn, quên uống → Suy dinh dưỡng, mất nước!"
            },
            {
                "name": "Hoạt động hàng ngày",
                "activities": [
                    "Đi bộ nhẹ (có người đi cùng)",
                    "Nghe nhạc (nhạc quen thuộc)",
                    "Xem ảnh cũ (kích thích trí nhớ)",
                    "Làm việc nhà đơn giản (lau bàn, gấp quần áo)",
                    "Vẽ, tô màu (nếu còn khả năng)"
                ],
                "benefit": "Giúp duy trì chức năng, giảm lo âu, cải thiện tâm trạng"
            }
        ]
    },
    
    "caregiver_support": {
        "title": "💪 Hỗ Trợ Người Chăm Sóc",
        "description": "Chăm sóc người sa sút trí tuệ RẤT VẤT VẢ - Cần được hỗ trợ:",
        "challenges": [
            "Chăm sóc 24/24 → Mệt mỏi, kiệt sức",
            "Căng thẳng cao → Trầm cảm, lo âu",
            "Mất thời gian → Không còn thời gian cho bản thân",
            "Chi phí cao → Thuốc, chăm sóc",
            "Xung đột gia đình → Ai chăm, ai trả tiền..."
        ],
        "self_care": {
            "title": "🧘 Chăm Sóc Bản Thân",
            "description": "QUAN TRỌNG: Chăm sóc chính mình trước, mới chăm được người khác!",
            "tips": [
                "Nghỉ ngơi đều đặn (nhờ người khác thay)",
                "Tập thể dục (giảm căng thẳng)",
                "Trò chuyện với bạn bè, gia đình",
                "Tham gia nhóm hỗ trợ người chăm sóc",
                "Đi khám bác sĩ khi cần (đừng bỏ bê sức khỏe)",
                "Nhận hỗ trợ từ xã hội (nếu có điều kiện)"
            ]
        },
        "help_resources": {
            "title": "📞 Nguồn Hỗ Trợ",
            "resources": [
                "Nhóm hỗ trợ người chăm sóc (tại bệnh viện, cộng đồng)",
                "Dịch vụ chăm sóc tại nhà (nếu có điều kiện)",
                "Tư vấn tâm lý (nếu trầm cảm, lo âu)",
                "Chia sẻ với gia đình, bạn bè (đừng cô lập)"
            ]
        }
    },
    
    "end_of_life": {
        "title": "🕊️ Giai Đoạn Cuối",
        "description": "Khi người bệnh không còn khả năng tự chăm sóc:",
        "considerations": [
            {
                "name": "Chăm sóc tại nhà vs Trung tâm",
                "options": [
                    "Chăm sóc tại nhà: Cần người chăm sóc 24/24, vất vả",
                    "Trung tâm chăm sóc: Chuyên nghiệp hơn, nhưng chi phí cao",
                    "Quyết định tùy điều kiện gia đình"
                ]
            },
            {
                "name": "Chăm sóc giảm nhẹ",
                "description": "Tập trung vào chất lượng sống, giảm đau đớn",
                "focus": [
                    "An toàn, thoải mái",
                    "Giảm đau (nếu có)",
                    "Tình cảm, yêu thương",
                    "Không can thiệp quá mức"
                ]
            }
        ]
    }
}

