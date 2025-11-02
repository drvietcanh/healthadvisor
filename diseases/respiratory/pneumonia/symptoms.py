"""
Viêm phổi - Triệu chứng
Symptoms of Pneumonia
"""

from typing import Dict, List

SYMPTOMS = {
    "main_symptoms": {
        "title": "🔍 Triệu Chứng Chính",
        "symptoms": [
            {
                "name": "Ho",
                "icon": "🤧",
                "description": "Ho khan hoặc ho có đờm (vàng, xanh, đôi khi lẫn máu)",
                "details": [
                    "Ho khan (thường do virus, Mycoplasma)",
                    "Ho có đờm vàng/xanh (thường do vi khuẩn)",
                    "Ho ra máu (viêm phổi nặng, lao phổi)",
                    "Ho dai dẳng 1-2 tuần sau khi khỏi"
                ]
            },
            {
                "name": "Sốt",
                "icon": "🌡️",
                "description": "Sốt cao 38.5-40°C (vi khuẩn) hoặc sốt nhẹ (virus)",
                "details": [
                    "Vi khuẩn: Sốt cao, rét run, vã mồ hôi",
                    "Virus: Sốt nhẹ hoặc không sốt",
                    "Người già: Có thể KHÔNG sốt (chỉ mệt, lơ mơ)",
                    "⚠️ Sốt + ho + khó thở = Viêm phổi (cần đi khám ngay!)"
                ]
            },
            {
                "name": "Khó thở",
                "icon": "😮‍💨",
                "description": "Thở nhanh, hụt hơi, đau ngực khi thở",
                "details": [
                    "Thở nhanh >20 lần/phút (người lớn), >40 lần/phút (trẻ em)",
                    "Hụt hơi khi vận động nhẹ, thậm chí nghỉ",
                    "Đau ngực bên bị viêm (đau nhói khi ho, hít sâu)",
                    "Trẻ em: Cánh mũi phập phồng, co kéo cơ liên sườn"
                ]
            },
            {
                "name": "Đau ngực",
                "icon": "💔",
                "description": "Đau nhói một bên ngực, tăng khi ho hoặc hít sâu",
                "details": [
                    "Đau bên phổi bị viêm",
                    "Đau tăng khi ho, hít sâu",
                    "Đôi khi đau lan ra lưng"
                ]
            },
            {
                "name": "Mệt mỏi, yếu sức",
                "icon": "😴",
                "description": "Mệt nhiều, không muốn ăn, đau đầu",
                "details": [
                    "Mệt mỏi nặng, không muốn làm gì",
                    "Chán ăn, buồn nôn",
                    "Đau đầu, đau cơ khớp (giống cúm)",
                    "Người già: Lơ mơ, lú lẫn (triệu chứng duy nhất!)"
                ]
            }
        ]
    },
    
    "severe_symptoms": {
        "title": "🚨 Triệu Chứng Nặng - Cần Cấp Cứu Ngay!",
        "warning": "Nếu có các triệu chứng sau, GỌI 115 NGAY:",
        "symptoms": [
            {
                "name": "Khó thở nặng",
                "signs": [
                    "Thở gấp >30 lần/phút",
                    "Môi, đầu ngón tay tím tái",
                    "Không nói được câu dài",
                    "Trẻ em: Rút lõm lồng ngực, cánh mũi phập phồng"
                ]
            },
            {
                "name": "Sốc nhiễm khuẩn",
                "signs": [
                    "Huyết áp tụt <90/60 mmHg",
                    "Mạch nhanh >120/phút",
                    "Da lạnh, ẩm, tím tái",
                    "Lơ mơ, không tỉnh táo",
                    "Tiểu ít hoặc không tiểu"
                ]
            },
            {
                "name": "Mất nước nặng",
                "signs": [
                    "Miệng khô, khát nước dữ dội",
                    "Mắt trũng, da khô, nhăn nheo",
                    "Trẻ em: Khóc không có nước mắt",
                    "Tiểu ít, nước tiểu vàng đậm"
                ]
            },
            {
                "name": "Lơ mơ, co giật",
                "signs": [
                    "Người già: Lơ mơ, không tỉnh táo (thường KHÔNG sốt!)",
                    "Trẻ em: Co giật, li bì",
                    "Đây là DẤU HIỆU NẶNG ở người già!"
                ]
            }
        ]
    },
    
    "atypical_pneumonia": {
        "title": "🔍 Viêm Phổi Không Điển Hình (Mycoplasma)",
        "description": "Triệu chứng nhẹ hơn, dễ nhầm với cảm cúm:",
        "symptoms": [
            "Ho khan, dai dẳng 2-3 tuần",
            "Sốt nhẹ hoặc không sốt",
            "Đau họng, khàn tiếng",
            "Đau đầu, đau cơ",
            "Mệt mỏi nhẹ",
            "⚠️ Dễ bỏ qua → Chuyển nặng nếu không điều trị"
        ]
    },
    
    "elderly_symptoms": {
        "title": "👴 Triệu Chứng Ở Người Già (Thường Mơ Hồ!)",
        "warning": "⚠️ Người già thường KHÔNG sốt, KHÔNG ho nhiều → Dễ bỏ qua!",
        "common": [
            "Chỉ MỆT, YẾU SỨC (triệu chứng duy nhất!)",
            "Lơ mơ, lú lẫn (tưởng bệnh thần kinh)",
            "Không muốn ăn, ăn không ngon",
            "Thở nhanh nhẹ (nhưng không rõ ràng)",
            "Đôi khi chỉ TĂNG ĐƯỜNG HUYẾT ở bệnh nhân tiểu đường"
        ],
        "note": "→ Người già viêm phổi thường NẶNG hơn, TỬ VONG cao hơn!"
    },
    
    "children_symptoms": {
        "title": "👶 Triệu Chứng Ở Trẻ Em",
        "warning": "Trẻ <5 tuổi: Dấu hiệu khó thở quan trọng hơn sốt!",
        "common": [
            {
                "name": "Dấu hiệu khó thở",
                "signs": [
                    "Thở nhanh: >40 lần/phút (<1 tuổi), >30 lần/phút (1-5 tuổi)",
                    "Rút lõm lồng ngực (xương sườn lõm vào khi hít)",
                    "Cánh mũi phập phồng",
                    "Co kéo cơ liên sườn",
                    "⚠️ Đây là DẤU HIỆU NẶNG - Cần cấp cứu ngay!"
                ]
            },
            {
                "name": "Triệu chứng khác",
                "signs": [
                    "Ho (khan hoặc có đờm)",
                    "Sốt cao (có thể co giật)",
                    "Bỏ bú, không chịu ăn",
                    "Quấy khóc, không chịu chơi",
                    "Nôn, tiêu chảy (do nhiễm trùng toàn thân)"
                ]
            }
        ]
    }
}

