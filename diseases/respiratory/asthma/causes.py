"""
Asthma Causes - Nguyên nhân gây hen suyễn
==========================================

Các yếu tố di truyền, dị ứng, môi trường
"""

CAUSES = {
    "genetic": {
        "name": "🧬 Di Truyền",
        "explanation": "Bố mẹ hen → Con dễ hen (40-60%)",
        "reality": "Nếu CẢ BỐ LẪN MẸ hen → Con hen 60-70%",
        "note": "Di truyền KHUYNH HƯỚNG, không phải chắc chắn 100%"
    },
    
    "allergies": {
        "name": "🤧 Dị Ứng - Nguyên Nhân #1",
        "common_allergens": [
            {
                "type": "Bụi nhà",
                "detail": "Bọ ve bụi (nhỏ li ti, sống trong ga gối, nệm)",
                "note": "PHẢI THƯỜNG XUYÊN!"
            },
            {
                "type": "Phấn hoa",
                "detail": "Mùa xuân, gần cây cỏ",
                "season": "Tháng 2-4"
            },
            {
                "type": "Lông thú",
                "detail": "Chó, mèo, chim",
                "note": "Lông VÀ nước bọt, nước tiểu"
            },
            {
                "type": "Nấm mốc",
                "detail": "Tường ẩm, nhà tắm, tủ quần áo",
                "note": "Nhà ẩm ướt rất dễ"
            },
            {
                "type": "Gián, chuột",
                "detail": "Phân, xác, lông",
                "note": "Thường thấy ở nhà cũ"
            }
        ]
    },
    
    "environmental": {
        "name": "🏭 Môi Trường",
        "factors": [
            "Khói thuốc lá (chủ động + thụ động)",
            "Ô nhiễm không khí (khói xe, nhà máy)",
            "Khói bếp (than, củi, dầu)",
            "Hóa chất (sơn, nước rửa chén, nước hoa)",
            "Khói hương, nhang (nhiều người không nghĩ tới!)"
        ],
        "vietnam_note": "Hà Nội, TP.HCM ô nhiễm cao → Hen tăng"
    }
}

