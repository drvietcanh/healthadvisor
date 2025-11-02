"""
IBS - Triệu chứng
"""

SYMPTOMS = {
    "common": {
        "title": "🔍 Triệu chứng thường gặp:",
        "abdominal_pain": {
            "title": "Đau bụng:",
            "characteristics": [
                "**Đau quặn bụng** - Đau từng cơn, thường ở bụng dưới",
                "**Đau giảm sau khi đi ngoài** - Đặc trưng của IBS",
                "**Đau tăng khi stress, lo lắng**",
                "**Đau tăng sau khi ăn** - Đặc biệt thức ăn cay, nhiều dầu",
                "Mức độ: Từ khó chịu đến đau vừa (hiếm khi đau dữ dội)"
            ]
        },
        "bowel_changes": {
            "title": "Thay đổi thói quen đi tiêu:",
            "types": [
                {
                    "name": "IBS-D (Tiêu chảy):",
                    "symptoms": [
                        "Tiêu chảy thường xuyên",
                        "Phân lỏng, nhiều nước",
                        "Phải đi tiêu gấp, không nhịn được",
                        "Đi nhiều lần/ngày"
                    ]
                },
                {
                    "name": "IBS-C (Táo bón):",
                    "symptoms": [
                        "Táo bón thường xuyên",
                        "Phân cứng, khó đi",
                        "Đi tiêu ít (<3 lần/tuần)",
                        "Phải rặn nhiều"
                    ]
                },
                {
                    "name": "IBS-M (Hỗn hợp):",
                    "symptoms": [
                        "Vừa tiêu chảy vừa táo bón",
                        "Thay đổi luân phiên",
                        "Khó dự đoán"
                    ]
                }
            ]
        },
        "other": {
            "title": "Triệu chứng khác:",
            "symptoms": [
                "**Đầy hơi, chướng bụng** - Bụng căng, khó chịu",
                "**Xì hơi nhiều** - Hoặc không xì được (táo bón)",
                "**Cảm giác đi tiêu không hết** - Đi xong vẫn muốn đi tiếp",
                "**Chất nhầy trong phân** - Có thể có ít nhầy (không phải máu)",
                "**Mệt mỏi** - Do stress, lo lắng về bệnh"
            ]
        }
    },
    
    "red_flags": {
        "title": "⚠️ Dấu hiệu cảnh báo (KHÔNG phải IBS - Cần khám ngay!):",
        "signs": [
            "🚨 **Có máu trong phân** - Đỏ tươi hoặc đen",
            "🚨 **Sụt cân không rõ nguyên nhân**",
            "🚨 **Sốt** - Dấu hiệu nhiễm trùng",
            "🚨 **Triệu chứng xuất hiện sau 50 tuổi** - Ít khi là IBS",
            "🚨 **Có người thân bị ung thư đại tràng**",
            "🚨 **Thiếu máu (da xanh, mệt mỏi)**",
            "🚨 **Đau bụng dữ dội, liên tục**"
        ],
        "note": "⚠️ Nếu có các dấu hiệu trên → KHÔNG phải IBS đơn giản! Cần khám bác sĩ ngay để loại trừ bệnh nguy hiểm!"
    }
}

