"""
BPH - Triệu chứng
"""

SYMPTOMS = {
    "obstructive": {
        "title": "🔍 Triệu chứng do tắc nghẽn (Ứ lại nước tiểu):",
        "symptoms": [
            "**Tiểu khó** - Phải rặn mới tiểu được, dòng nước tiểu yếu, nhỏ",
            "**Tiểu rắt** - Tiểu nhiều lần, mỗi lần ít",
            "**Tiểu không hết** - Tiểu xong vẫn cảm giác còn nước tiểu",
            "**Tiểu ngắt quãng** - Dòng nước tiểu bị ngắt, phải đợi lại",
            "**Tiểu lâu** - Mất nhiều thời gian để tiểu xong",
            "**Dòng tiểu yếu** - Không mạnh như trước"
        ]
    },
    
    "irritative": {
        "title": "🔍 Triệu chứng do kích thích (Bàng quang hoạt động quá mức):",
        "symptoms": [
            "**Tiểu gấp** - Muốn đi tiểu ngay, không nhịn được",
            "**Tiểu đêm** - Thức dậy nhiều lần để đi tiểu (2-5+ lần/đêm)",
            "**Tiểu nhiều lần** - Tiểu 10-15+ lần/ngày",
            "**Tiểu buốt** - Cảm giác nóng rát khi tiểu (nếu có viêm)"
        ]
    },
    
    "severe": {
        "title": "⚠️ Triệu chứng nặng (Cần cấp cứu!):",
        "symptoms": [
            "🚨 **Bí tiểu hoàn toàn** - Muốn tiểu nhưng không tiểu được",
            "🚨 **Tiểu máu** - Nước tiểu có màu đỏ/hồng",
            "🚨 **Đau vùng bụng dưới** - Do bàng quang căng",
            "🚨 **Sốt, ớn lạnh** - Nhiễm trùng đường tiểu",
            "🚨 **Nôn, không tiểu được** - Cấp cứu!"
        ],
        "warning": "⚠️ BÍ TIỂU → CẤP CỨU NGAY! Phải đặt ống thông tiểu!"
    },
    
    "when_to_see_doctor": {
        "title": "🏥 Khi nào cần khám bác sĩ:",
        "soon": [
            "Có bất kỳ triệu chứng tiểu khó, tiểu rắt",
            "Tiểu đêm ≥2 lần/đêm",
            "Ảnh hưởng sinh hoạt, giấc ngủ",
            "Nam giới >50 tuổi"
        ],
        "urgent": [
            "🚨 Bí tiểu hoàn toàn",
            "🚨 Tiểu máu",
            "🚨 Sốt, đau bụng dưới"
        ]
    }
}

