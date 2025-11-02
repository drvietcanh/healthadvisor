"""
Nhồi Máu Cơ Tim - Triệu chứng
Symptoms of Myocardial Infarction
"""

from typing import Dict, List

SYMPTOMS = {
    "classic_symptoms": {
        "title": "🔍 Triệu Chứng Điển Hình",
        "description": "Đây là các triệu chứng PHỔ BIẾN NHẤT khi bị nhồi máu cơ tim:",
        "symptoms": [
            {
                "name": "Đau ngực",
                "icon": "💔",
                "description": "Đau NHỨC, ÉP, như có vật nặng đè lên ngực",
                "details": [
                    "Vị trí: Sau xương ức (giữa ngực), có thể lan ra cánh tay trái, cổ, hàm",
                    "Tính chất: Đau NHỨC, ÉP, KHÓ THỞ (không phải đau nhói như dao đâm)",
                    "Thời gian: >20 phút, không giảm khi nghỉ ngơi",
                    "⚠️ Đau NGỰC + Khó thở + Vã mồ hôi = NGHI NGỜ NHỒI MÁU!"
                ],
                "warning": "⚠️ KHÔNG phải ai cũng đau ngực! Người già, tiểu đường có thể KHÔNG đau ngực!"
            },
            {
                "name": "Khó thở",
                "icon": "😮‍💨",
                "description": "Thở gấp, hụt hơi, như leo cầu thang dài",
                "details": [
                    "Khó thở ngay cả khi nghỉ ngơi",
                    "Thở nhanh >20 lần/phút",
                    "Cảm giác thiếu không khí",
                    "Có thể kèm ho, khạc đờm hồng (phù phổi)"
                ]
            },
            {
                "name": "Vã mồ hôi lạnh",
                "icon": "😓",
                "description": "Mồ hôi đổ như tắm, da lạnh, ẩm ướt",
                "details": [
                    "Mồ hôi nhiều, không do nóng",
                    "Da lạnh, ẩm ướt (không khô)",
                    "Cảm giác lạnh run",
                    "Đây là dấu hiệu SỐC - Rất nguy hiểm!"
                ]
            },
            {
                "name": "Buồn nôn, nôn",
                "icon": "🤢",
                "description": "Buồn nôn, có thể nôn (đặc biệt ở phụ nữ)",
                "details": [
                    "Phụ nữ thường có triệu chứng này nhiều hơn",
                    "Dễ nhầm với rối loạn tiêu hóa",
                    "Nếu kèm đau ngực → NGHI NGỜ NHỒI MÁU!"
                ]
            },
            {
                "name": "Chóng mặt, choáng váng",
                "icon": "😵",
                "description": "Cảm giác quay cuồng, muốn ngất",
                "details": [
                    "Do huyết áp tụt (tim không bơm máu được)",
                    "Có thể ngất xỉu",
                    "Nguy hiểm nếu ngã → Chấn thương thêm"
                ]
            },
            {
                "name": "Mệt mỏi cực độ",
                "icon": "😴",
                "description": "Mệt đến mức không thể làm gì",
                "details": [
                    "Cảm giác yếu sức đột ngột",
                    "Như kiệt sức hoàn toàn",
                    "Không thể đứng dậy, nói chuyện"
                ]
            }
        ]
    },
    
    "atypical_symptoms": {
        "title": "🔍 Triệu Chứng Không Điển Hình (Người Già, Tiểu Đường)",
        "warning": "⚠️ QUAN TRỌNG: Người >70 tuổi, tiểu đường, phụ nữ có thể KHÔNG có đau ngực!",
        "common": [
            {
                "name": "Chỉ mệt mỏi, yếu sức",
                "description": "Không đau ngực, chỉ cảm thấy mệt, yếu đột ngột",
                "risk": "Dễ bỏ qua → Chậm phát hiện → Tử vong cao"
            },
            {
                "name": "Khó thở khi nằm",
                "description": "Khó thở khi nằm xuống, phải ngồi dậy",
                "note": "Dấu hiệu phù phổi do suy tim cấp"
            },
            {
                "name": "Đau lưng, đau hàm",
                "description": "Đau ở lưng, hàm, cánh tay PHẢI (không phải trái)",
                "note": "Đau lan từ tim, dễ nhầm với đau răng, đau xương"
            },
            {
                "name": "Lơ mơ, lú lẫn",
                "description": "Người già có thể chỉ lơ mơ, không tỉnh táo",
                "risk": "Dễ nhầm với đột quỵ hoặc bệnh thần kinh"
            },
            {
                "name": "Tăng đường huyết đột ngột",
                "description": "Ở bệnh nhân tiểu đường, có thể chỉ thấy đường huyết tăng cao",
                "note": "Do stress làm tăng đường huyết"
            }
        ],
        "note": "⚠️ Nếu người già, tiểu đường có BẤT KỲ triệu chứng lạ nào → Nghĩ đến nhồi máu!"
    },
    
    "silent_mi": {
        "title": "🔇 Nhồi Máy Cơ Tim Thầm Lặng (Silent MI)",
        "description": "Một số người bị nhồi máu nhưng KHÔNG CÓ TRIỆU CHỨNG!",
        "risk_groups": [
            "Người tiểu đường (mất cảm giác đau)",
            "Người già >80 tuổi",
            "Người có bệnh thần kinh"
        ],
        "discovery": [
            "Phát hiện tình cờ khi đo điện tim (ECG)",
            "Hoặc khi đã suy tim, bác sĩ hỏi tiền sử"
        ],
        "warning": "⚠️ Nguy hiểm vì không được điều trị → Tổn thương tim nặng!"
    },
    
    "women_symptoms": {
        "title": "👩 Triệu Chứng Ở Phụ Nữ",
        "description": "Phụ nữ thường có triệu chứng KHÁC với nam giới:",
        "common": [
            "Ít đau ngực hơn nam giới",
            "Buồn nôn, nôn nhiều hơn",
            "Đau lưng, đau cổ nhiều hơn",
            "Mệt mỏi cực độ",
            "Khó thở không rõ nguyên nhân",
            "Đau vùng bụng trên (dễ nhầm với đau dạ dày)"
        ],
        "warning": "⚠️ Phụ nữ dễ bị BỎ QUA → Tử vong cao hơn nam giới!"
    },
    
    "red_flags": {
        "title": "🚨 DẤU HIỆU ĐỎ - GỌI 115 NGAY!",
        "description": "BẤT KỲ triệu chứng nào sau đây → GỌI 115 NGAY, KHÔNG ĐỢI!",
        "symptoms": [
            {
                "name": "Đau ngực dữ dội",
                "description": "Đau ép, nhức, kéo dài >15 phút, không giảm khi nghỉ"
            },
            {
                "name": "Đau ngực + Khó thở + Vã mồ hôi",
                "description": "Bộ 3 triệu chứng này = NGHI NGỜ NHỒI MÁU rất cao!"
            },
            {
                "name": "Ngất xỉu, bất tỉnh",
                "description": "Tim không bơm máu lên não → Ngất"
            },
            {
                "name": "Nhịp tim bất thường",
                "description": "Tim đập rất nhanh (>120/phút) hoặc rất chậm (<50/phút)"
            },
            {
                "name": "Choáng, huyết áp tụt",
                "description": "Da xanh, lạnh, vã mồ hôi → Sốc tim"
            },
            {
                "name": "Người già/tểu đường có triệu chứng lạ",
                "description": "Dù không đau ngực, nhưng mệt đột ngột, khó thở → Nghĩ đến nhồi máu"
            }
        ],
        "action": "🚨 GỌI 115 NGAY - ĐỪNG TỰ LÁI XE ĐẾN BỆNH VIỆN!"
    }
}

