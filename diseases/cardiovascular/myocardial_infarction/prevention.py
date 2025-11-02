"""
Nhồi Máu Cơ Tim - Phòng ngừa
Prevention of Myocardial Infarction
"""

from typing import Dict, List

PREVENTION = {
    "primary_prevention": {
        "title": "🛡️ Phòng Ngừa Lần Đầu (Chưa từng bị nhồi máu)",
        "description": "Ngăn ngừa nhồi máu cơ tim xảy ra:",
        "methods": [
            {
                "name": "🚭 Bỏ Thuốc Lá",
                "priority": "QUAN TRỌNG NHẤT!",
                "benefit": "Giảm 50% nguy cơ nhồi máu",
                "facts": [
                    "Hút thuốc làm tổn thương mạch máu",
                    "Tăng nguy cơ cục máu đông",
                    "Bỏ thuốc 1 năm → Giảm nguy cơ 50%",
                    "Bỏ thuốc 10 năm → Nguy cơ gần như người không hút"
                ]
            },
            {
                "name": "🍽️ Ăn Uống Lành Mạnh",
                "description": "Chế độ ăn Địa Trung Hải (Mediterranean Diet)",
                "should_eat": [
                    "Nhiều rau xanh, trái cây (5 phần/ngày)",
                    "Cá (2-3 lần/tuần): Cá hồi, cá thu (omega-3)",
                    "Ngũ cốc nguyên hạt: Gạo lứt, bánh mì đen",
                    "Đậu, hạt: Đậu nành, đậu xanh, hạnh nhân",
                    "Dầu thực vật: Dầu olive, dầu đậu nành"
                ],
                "should_limit": [
                    "Thịt đỏ: <3 lần/tuần",
                    "Muối: <5g/ngày (<1 thìa cà phê)",
                    "Đường: <25g/ngày (<6 thìa)",
                    "Mỡ động vật, đồ chiên rán"
                ],
                "should_avoid": [
                    "Thực phẩm chế biến sẵn (xúc xích, thịt nguội)",
                    "Đồ ngọt, nước ngọt",
                    "Rượu bia (hoặc chỉ uống ít, vừa phải)"
                ]
            },
            {
                "name": "🏃 Tập Thể Dục Đều Đặn",
                "recommendation": "150 phút/tuần (30 phút × 5 ngày)",
                "activities": [
                    "Đi bộ nhanh",
                    "Đạp xe",
                    "Bơi lội",
                    "Khiêu vũ"
                ],
                "benefit": [
                    "Giảm huyết áp",
                    "Giảm cholesterol xấu (LDL)",
                    "Tăng cholesterol tốt (HDL)",
                    "Giảm cân, giảm đường huyết"
                ]
            },
            {
                "name": "⚖️ Kiểm Soát Cân Nặng",
                "target": "BMI 18.5-24.9 (không thừa cân, béo phì)",
                "benefit": "Giảm nguy cơ nhồi máu 30-40%",
                "how": [
                    "Ăn uống cân bằng",
                    "Tập thể dục đều đặn",
                    "Ngủ đủ giấc (7-8 giờ/đêm)"
                ]
            },
            {
                "name": "📊 Kiểm Soát Huyết Áp",
                "target": "<140/90 mmHg (tốt nhất <130/80)",
                "how": [
                    "Uống thuốc đều đặn (nếu bác sĩ kê)",
                    "Ăn ít muối",
                    "Tập thể dục",
                    "Giảm căng thẳng"
                ]
            },
            {
                "name": "🩸 Kiểm Soát Đường Huyết",
                "target": "HbA1c <7% (nếu tiểu đường)",
                "why": "Tiểu đường → Tăng nguy cơ nhồi máu 2-4 lần",
                "how": [
                    "Uống thuốc đều đặn",
                    "Ăn uống hợp lý",
                    "Tập thể dục",
                    "Theo dõi đường huyết"
                ]
            },
            {
                "name": "🧈 Kiểm Soát Mỡ Máu",
                "target": "LDL <100 mg/dL (nếu có nguy cơ cao)",
                "how": [
                    "Uống thuốc statin (nếu bác sĩ kê)",
                    "Ăn ít mỡ động vật",
                    "Tập thể dục"
                ]
            },
            {
                "name": "💊 Aspirin Phòng Ngừa",
                "description": "Aspirin 75-100mg/ngày (theo chỉ định bác sĩ)",
                "who": [
                    "Người có nguy cơ cao (>10% trong 10 năm)",
                    "Đã từng nhồi máu, đột quỵ",
                    "Đặt stent, bắc cầu mạch vành"
                ],
                "warning": "⚠️ CHỈ uống khi bác sĩ kê - Có nguy cơ chảy máu dạ dày!"
            },
            {
                "name": "😴 Ngủ Đủ, Giảm Căng Thẳng",
                "sleep": "7-8 giờ/ngày",
                "stress": [
                    "Thiền, yoga",
                    "Thở sâu",
                    "Nghe nhạc",
                    "Trò chuyện với người thân"
                ],
                "benefit": "Giảm huyết áp, giảm nguy cơ tim mạch"
            }
        ]
    },
    
    "secondary_prevention": {
        "title": "🛡️ Phòng Ngừa Lần Hai (Đã từng bị nhồi máu)",
        "description": "Ngăn ngừa nhồi máu lại:",
        "critical": [
            {
                "name": "💊 Uống Thuốc Đều Đặn",
                "priority": "QUAN TRỌNG NHẤT!",
                "medications": [
                    "Aspirin 100mg/ngày - SUỐT ĐỜI",
                    "Clopidogrel 75mg/ngày - Ít nhất 1 năm (nếu đặt stent)",
                    "Statin - SUỐT ĐỜI",
                    "Beta-blocker - SUỐT ĐỜI",
                    "ACE-I hoặc ARB - SUỐT ĐỜI"
                ],
                "warning": "⚠️ KHÔNG được tự ngừng thuốc! Ngừng → Nguy cơ nhồi máu lại tăng 30-50%!"
            },
            {
                "name": "🚭 BỎ THUỐC LÁ",
                "priority": "BẮT BUỘC!",
                "why": "Tiếp tục hút → Nguy cơ nhồi máu lại tăng 3-5 lần!"
            },
            {
                "name": "🏥 Tái Khám Định Kỳ",
                "schedule": [
                    "1 tuần sau ra viện",
                    "1 tháng",
                    "3 tháng",
                    "6 tháng",
                    "Sau đó mỗi 6 tháng"
                ],
                "why": "Theo dõi chức năng tim, điều chỉnh thuốc"
            },
            {
                "name": "📊 Theo Dõi Tại Nhà",
                "daily": [
                    "Đo huyết áp, nhịp tim",
                    "Cân nặng (tăng cân = dấu hiệu phù tim)",
                    "Triệu chứng: Đau ngực, khó thở"
                ]
            },
            {
                "name": "🚨 Biết Khi Nào Gọi 115",
                "triggers": [
                    "Đau ngực lại (dù nhẹ)",
                    "Khó thở tăng",
                    "Tim đập nhanh, không đều",
                    "Choáng, ngất"
                ],
                "warning": "⚠️ Đừng chủ quan - Nhồi máu lại nguy hiểm hơn lần đầu!"
            }
        ]
    },
    
    "risk_factors": {
        "title": "⚠️ Yếu Tố Nguy Cơ",
        "description": "Những người có nguy cơ cao:",
        "factors": [
            {
                "name": "Tuổi",
                "description": "Nam >45 tuổi, Nữ >55 tuổi",
                "cannot_change": True
            },
            {
                "name": "Giới tính",
                "description": "Nam có nguy cơ cao hơn nữ (trước 65 tuổi)",
                "cannot_change": True
            },
            {
                "name": "Tiền sử gia đình",
                "description": "Bố/mẹ/anh/chị bị nhồi máu <55 tuổi",
                "cannot_change": True
            },
            {
                "name": "Hút thuốc lá",
                "description": "Tăng nguy cơ 2-4 lần",
                "can_change": True,
                "action": "BỎ THUỐC LÁ!"
            },
            {
                "name": "Tăng huyết áp",
                "description": "Tăng nguy cơ 2-3 lần",
                "can_change": True,
                "action": "Uống thuốc đều, ăn ít muối"
            },
            {
                "name": "Tiểu đường",
                "description": "Tăng nguy cơ 2-4 lần",
                "can_change": True,
                "action": "Kiểm soát đường huyết tốt"
            },
            {
                "name": "Mỡ máu cao",
                "description": "Tăng nguy cơ 1.5-2 lần",
                "can_change": True,
                "action": "Uống statin, ăn ít mỡ"
            },
            {
                "name": "Béo phì",
                "description": "Tăng nguy cơ 1.5-2 lần",
                "can_change": True,
                "action": "Giảm cân, tập thể dục"
            },
            {
                "name": "Ít vận động",
                "description": "Tăng nguy cơ 1.5-2 lần",
                "can_change": True,
                "action": "Tập thể dục 30 phút/ngày"
            },
            {
                "name": "Căng thẳng",
                "description": "Tăng nguy cơ 1.5 lần",
                "can_change": True,
                "action": "Thiền, yoga, nghỉ ngơi"
            }
        ]
    }
}

