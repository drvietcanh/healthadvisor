"""
Peptic Ulcer - Triệu chứng
"""

SYMPTOMS = {
    "pain": {
        "title": "🔍 Đặc điểm đau:",
        "gastric_ulcer": {
            "title": "Loét dạ dày:",
            "characteristics": [
                "Đau vùng thượng vị (trên rốn)",
                "Đau khi ăn hoặc sau ăn (thức ăn chạm vết loét)",
                "Đau nóng rát, cồn cào",
                "Đau có thể lan ra sau lưng"
            ]
        },
        "duodenal_ulcer": {
            "title": "Loét tá tràng:",
            "characteristics": [
                "Đau vùng thượng vị (trên rốn)",
                "Đau khi đói (đặc biệt 2-3 giờ sau ăn)",
                "Đau ban đêm (1-3 giờ sáng)",
                "Ăn vào → Đau giảm ngay (thức ăn che vết loét)"
            ]
        }
    },
    
    "other": {
        "title": "Triệu chứng khác:",
        "symptoms": [
            "Ợ hơi, ợ chua",
            "Buồn nôn, nôn",
            "Đầy bụng, khó tiêu",
            "Chán ăn",
            "Sụt cân (do đau, không ăn được)"
        ]
    },
    
    "complications": {
        "title": "⚠️ Biến chứng nguy hiểm:",
        "bleeding": {
            "title": "Chảy máu dạ dày:",
            "symptoms": [
                "🚨 Nôn ra máu (máu đỏ tươi hoặc màu cà phê)",
                "🚨 Đi ngoài phân đen (như nhựa đường, mùi tanh)",
                "🚨 Chóng mặt, ngất (do mất máu)",
                "🚨 Da xanh, mệt mỏi cực độ"
            ],
            "warning": "⚠️ Chảy máu dạ dày → CẤP CỨU NGAY! Gọi 115 hoặc đi bệnh viện!"
        },
        "perforation": {
            "title": "Thủng dạ dày:",
            "symptoms": [
                "🚨 Đau bụng DỮ DỘI đột ngột (như dao đâm)",
                "🚨 Bụng cứng như gỗ",
                "🚨 Sốt, mạch nhanh",
                "🚨 Không đứng thẳng được (nằm co lại)"
            ],
            "warning": "⚠️ Thủng dạ dày → PHẪU THUẬT NGAY! CẤP CỨU!"
        }
    }
}

