"""
Đau đầu - Các loại đau đầu
Types of Headache
"""

from typing import Dict, List

HEADACHE_TYPES = {
    "tension": {
        "name": "Đau đầu căng thẳng (Tension Headache)",
        "description": "Phổ biến nhất (70-80% đau đầu), thường lành tính",
        "characteristics": {
            "pain": {
                "type": "Đau ép, căng như có dây buộc quanh đầu",
                "location": "Hai bên đầu, thái dương, sau gáy",
                "severity": "Nhẹ đến trung bình (4-6/10)"
            },
            "duration": "30 phút đến vài giờ, có thể vài ngày",
            "triggers": [
                "Căng thẳng, lo âu",
                "Mỏi mắt (nhìn màn hình lâu)",
                "Tư thế ngồi sai (cổ gáy căng)",
                "Thiếu ngủ, mệt mỏi",
                "Đói, uống ít nước"
            ],
            "treatment": {
                "mild": "Nghỉ ngơi, xoa bóp, Paracetamol 500mg",
                "moderate": "Paracetamol 500-1000mg × 2-3 lần/ngày, Ibuprofen 400mg",
                "prevention": "Giảm căng thẳng, ngủ đủ, tập thể dục, massage"
            }
        }
    },
    
    "migraine": {
        "name": "Đau nửa đầu (Migraine)",
        "description": "Đau đầu nặng, thường một bên, có thể nôn, sợ ánh sáng",
        "characteristics": {
            "pain": {
                "type": "Đau nhói, đập theo nhịp mạch, rất đau",
                "location": "Một bên đầu (thái dương, trán)",
                "severity": "Trung bình đến nặng (6-9/10)",
                "duration": "4-72 giờ"
            },
            "aura": {
                "description": "30% người có triệu chứng báo trước (Aura)",
                "symptoms": [
                    "Nhìn thấy ánh sáng nhấp nháy, đường zigzag (5-60 phút)",
                    "Tê một bên mặt/tay",
                    "Nói khó, yếu một bên (hiếm)"
                ],
                "warning": "⚠️ Nếu yếu tay chân kéo dài >1 giờ → Cần khám ngay (loại trừ đột quỵ!)"
            },
            "accompanying": {
                "common": [
                    "Buồn nôn, nôn (80%)",
                    "Sợ ánh sáng, tiếng động (90%)",
                    "Chóng mặt, mệt mỏi",
                    "Cần nằm phòng tối, yên tĩnh"
                ]
            },
            "triggers": [
                "Thay đổi hormone (phụ nữ trước kỳ kinh)",
                "Thức ăn: Rượu vang, phô mai, chocolate, đồ nướng",
                "Thiếu ngủ hoặc ngủ quá nhiều",
                "Căng thẳng hoặc sau khi hết căng thẳng",
                "Thời tiết thay đổi",
                "Mùi mạnh (nước hoa, khói thuốc)"
            ],
            "treatment": {
                "acute": [
                    "Paracetamol/Ibuprofen (nếu nhẹ)",
                    "Triptans: Sumatriptan, Rizatriptan (nếu nặng, theo chỉ định BS)",
                    "Ergotamine (theo chỉ định BS)"
                ],
                "prevention": [
                    "Thuốc: Propranolol, Topiramate, Amitriptyline (theo chỉ định BS)",
                    "Tránh yếu tố kích phát",
                    "Ngủ đủ, ăn đều bữa",
                    "Yoga, thiền, giảm căng thẳng"
                ],
                "warning": "⚠️ Không tự mua Triptan - Cần bác sĩ kê đơn!"
            },
            "frequency": {
                "episodic": "Dưới 15 ngày/tháng",
                "chronic": "Trên 15 ngày/tháng, kéo dài >3 tháng (Cần điều trị phòng ngừa)"
            }
        }
    },
    
    "cluster": {
        "name": "Đau đầu từng chuỗi (Cluster Headache)",
        "description": "Hiếm gặp, nhưng rất đau, tập trung thành từng đợt",
        "characteristics": {
            "pain": {
                "type": "Đau NHÓI DỮ DỘI như bị đâm, đốt",
                "location": "Một bên đầu, quanh mắt, thái dương",
                "severity": "Rất nặng (9-10/10) - Đau nhất trong các loại đau đầu!",
                "duration": "15 phút đến 3 giờ"
            },
            "accompanying": {
                "common": [
                    "Mắt đỏ, chảy nước mắt",
                    "Nghẹt mũi, chảy nước mũi một bên",
                    "Vã mồ hôi mặt",
                    "Không thể ngồi yên (phải đi lại, đập đầu vào tường)"
                ]
            },
            "pattern": {
                "episodic": "Đau mỗi ngày, vài lần/ngày, kéo dài 2-12 tuần → Hết, tái phát sau vài tháng",
                "chronic": "Đau liên tục, không có giai đoạn hết (hiếm)"
            },
            "demographics": "Nam nhiều hơn nữ (4:1), thường 20-50 tuổi",
            "treatment": {
                "acute": "Thở oxy 100% (hiệu quả nhất), Triptan tiêm, Ergotamine",
                "prevention": "Verapamil, Prednisolone (theo chỉ định BS)",
                "warning": "⚠️ Rất đau, cần điều trị chuyên khoa!"
            }
        }
    },
    
    "sinus": {
        "name": "Đau đầu do viêm xoang (Sinus Headache)",
        "description": "Đau đầu kèm viêm xoang",
        "characteristics": {
            "pain": {
                "type": "Đau nhức, căng tức",
                "location": "Trán, gò má, sau mắt, sau gáy",
                "worsens": "Cúi đầu, rặn → Đau tăng"
            },
            "accompanying": [
                "Nghẹt mũi, chảy nước mũi vàng/xanh",
                "Sốt nhẹ",
                "Đau mặt khi ấn xoang",
                "Mất khứu giác"
            ],
            "treatment": [
                "Thuốc thông mũi: Pseudoephedrine, Oxymetazoline (xịt mũi)",
                "Kháng sinh (nếu do vi khuẩn)",
                "Kháng histamine (nếu do dị ứng)",
                "Rửa mũi bằng nước muối"
            ]
        }
    },
    
    "medication_overuse": {
        "name": "Đau đầu do lạm dụng thuốc (Medication Overuse Headache)",
        "description": "Đau đầu do uống thuốc quá nhiều",
        "cause": "Uống thuốc giảm đau >10-15 ngày/tháng, kéo dài >3 tháng",
        "mechanism": "Cơ thể quen thuốc → Cần liều cao hơn → Đau đầu tái phát",
        "vicious_cycle": "Đau → Uống thuốc → Hết đau → Đau lại → Uống thuốc...",
        "treatment": {
            "stop": "NGỪNG thuốc đau đầu (dưới sự giám sát bác sĩ)",
            "alternative": "Dùng thuốc phòng ngừa thay thế",
            "duration": "2-10 tuần sau khi ngừng thuốc → Đau đầu sẽ giảm"
        },
        "warning": "⚠️ Không tự ý tăng liều thuốc giảm đau! Tối đa 2-3 lần/tuần."
    }
}

DANGEROUS_SIGNS = {
    "title": "🚨 DẤU HIỆU ĐAU ĐẦU NGUY HIỂM - CẦN CẤP CỨU NGAY!",
    "thunderclap": {
        "name": "Đau đầu sét đánh (Thunderclap Headache)",
        "description": "Đau đầu DỮ DỘI, ĐỘT NGỘT, đạt đỉnh trong vài giây",
        "causes": [
            "Xuất huyết não (Vỡ mạch máu não) - NGUY HIỂM TỬ VONG!",
            "Tách thành động mạch não",
            "Viêm màng não"
        ],
        "action": "🚨 GỌI 115 NGAY - Đừng đợi!"
    },
    "first_severe": {
        "name": "Đau đầu lần đầu tiên, rất nặng",
        "description": "Người >50 tuổi, đau đầu lần đầu, rất nặng",
        "risk": "Có thể là u não, xuất huyết não",
        "action": "Đi khám ngay, không tự uống thuốc"
    },
    "progressive": {
        "name": "Đau đầu tăng dần, ngày càng nặng",
        "description": "Đau đầu tăng dần trong vài tuần/tháng",
        "accompanying": [
            "Yếu tay chân một bên",
            "Co giật",
            "Thay đổi tính cách",
            "Nhìn mờ, nhìn đôi"
        ],
        "risk": "Có thể là u não",
        "action": "Khám chuyên khoa thần kinh ngay"
    },
    "with_fever_stiff_neck": {
        "name": "Đau đầu + Sốt + Cứng gáy",
        "description": "Không cúi đầu được, cổ cứng",
        "accompanying": [
            "Sốt cao",
            "Nhạy cảm ánh sáng",
            "Lơ mơ",
            "Nôn"
        ],
        "risk": "Viêm màng não - NGUY HIỂM TỬ VONG!",
        "action": "🚨 GỌI 115 NGAY - Viêm màng não cần điều trị kháng sinh NGAY!"
    },
    "after_head_injury": {
        "name": "Đau đầu sau chấn thương đầu",
        "description": "Sau ngã, va đập đầu",
        "accompanying": [
            "Lơ mơ, không tỉnh táo",
            "Nôn nhiều",
            "Co giật",
            "Chảy máu tai/mũi"
        ],
        "risk": "Chấn thương sọ não, xuất huyết não",
        "action": "🚨 GỌI 115 NGAY"
    },
    "with_visual_changes": {
        "name": "Đau đầu + Thay đổi thị giác + Yếu tay chân",
        "description": "Nhìn mờ, nhìn đôi + Yếu tay chân một bên",
        "risk": "Đột quỵ, u não",
        "action": "GỌI 115 NGAY - Có thể là đột quỵ!"
    }
}

