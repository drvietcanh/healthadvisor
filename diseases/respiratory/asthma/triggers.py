"""
Asthma Triggers - Các yếu tố kích phát hen suyễn
===================================================

Hướng dẫn cách tránh các yếu tố kích phát
"""

TRIGGERS = {
    "title": "🔥 Các Yếu Tố KÍCH PHÁT Hen",
    "description": "Biết TRÁNH = Giảm cơn hen 50-70%!",
    
    "allergens": {
        "name": "🤧 Dị Nguyên (Allergens)",
        "items": [
            {
                "trigger": "Bụi nhà (Bọ ve bụi)",
                "where": "Ga gối, nệm, thảm, rèm",
                "how_to_avoid": [
                    "Giặt ga gối 1 tuần/lần (nước nóng >60°C)",
                    "Phơi nệm nắng thường xuyên",
                    "Dùng vỏ gối chống ve bụi",
                    "BỎ thảm, rèm dày (nếu được)",
                    "Lau nhà ẩm (không quét khô → bụi bay)"
                ]
            },
            {
                "trigger": "Lông chó, mèo",
                "reality": "Lông, nước bọt, nước tiểu",
                "how_to_avoid": [
                    "TỐT NHẤT: Không nuôi",
                    "Nếu nuôi: Không cho vào phòng ngủ",
                    "Tắm thú cưng 1 tuần/lần",
                    "Rửa tay sau khi sờ"
                ]
            },
            {
                "trigger": "Gián, chuột",
                "where": "Nhà cũ, bếp",
                "how_to_avoid": [
                    "Dọn dẹp sạch sẽ",
                    "Không để thức ăn thừa",
                    "Bít kín khe hở"
                ]
            },
            {
                "trigger": "Nấm mốc",
                "where": "Tường ẩm, nhà tắm, tủ quần áo",
                "how_to_avoid": [
                    "Giảm độ ẩm (<50%)",
                    "Thông gió tốt",
                    "Lau sạch nấm mốc (dùng nước tẩy pha loãng)"
                ]
            }
        ]
    },
    
    "irritants": {
        "name": "💨 Chất Kích Thích",
        "items": [
            {
                "trigger": "Khói thuốc lá",
                "danger": "CỰC KỲ NGUY HIỂM!",
                "effects": [
                    "Làm hen NẶNG hơn",
                    "Thuốc KÉMHIỆU QUẢ hơn",
                    "Trẻ hít khói thuốc → Dễ hen gấp 2-3 lần"
                ],
                "action": "🚫 BỎ THUỐC + TRÁNH khói thuốc thụ động!"
            },
            {
                "trigger": "Ô nhiễm không khí",
                "sources": "Khói xe, bụi, khói nhà máy",
                "how_to_avoid": [
                    "Đeo khẩu trang N95 khi ra đường",
                    "Hạn chế ra ngoài khi AQI >150",
                    "Đóng cửa sổ khi ô nhiễm cao"
                ]
            },
            {
                "trigger": "Mùi nồng",
                "examples": "Nước hoa, xịt phòng, sơn, nước rửa chén",
                "tip": "Chọn sản phẩm KHÔNG MÙI"
            },
            {
                "trigger": "Khói nhang, hương",
                "reality": "Nhiều người KHÔNG biết đây là yếu tố kích hen!",
                "tip": "Thắp ít, thông gió tốt"
            }
        ]
    },
    
    "weather": {
        "name": "🌦️ Thời Tiết",
        "triggers": [
            {
                "condition": "Không khí LẠNH",
                "when": "Mùa đông, sáng sớm, phòng máy lạnh",
                "how_to_avoid": [
                    "Đeo khẩu trang khi ra ngoài trời lạnh",
                    "Hít thở qua mũi (KHÔNG qua miệng)",
                    "Quấn khăn che mũi, miệng"
                ]
            },
            {
                "condition": "Độ ẩm CAO",
                "when": "Mùa mưa, gần biển",
                "problem": "Nấm mốc, ve bụi sinh sôi"
            },
            {
                "condition": "Thay đổi ĐỘT NGỘT",
                "when": "Giao mùa, vào phòng lạnh từ ngoài nóng",
                "tip": "Thích nghi từ từ"
            }
        ]
    },
    
    "infections": {
        "name": "🦠 Nhiễm Trùng",
        "main": "Cảm lạnh, cúm, viêm phế quản",
        "reality": "70-80% cơn hen nặng do NHIỄM TRÙNG đường hô hấp",
        "prevention": [
            "Tiêm vắc-xin cúm HÀNG NĂM",
            "Rửa tay thường xuyên",
            "Tránh người ốm",
            "Tăng cường miễn dịch"
        ]
    },
    
    "emotions": {
        "name": "😭 Cảm Xúc",
        "triggers": "Cười to, khóc, giận dữ, stress",
        "why": "Thở nhanh, mất kiểm soát nhịp thở → Kích hen",
        "tip": "Học THỞ chậm, kiểm soát cảm xúc"
    },
    
    "foods_drugs": {
        "name": "💊 Thức Ăn & Thuốc",
        "foods": [
            "Đồ uống lạnh đá (shock nhiệt độ)",
            "Thực phẩm dị ứng (tôm, cua, trứng, sữa...)",
            "Chất bảo quản (sulfite trong rượu vang, mứt)"
        ],
        "drugs": [
            "Aspirin (10% người hen dị ứng Aspirin!)",
            "Thuốc chống viêm NSAID (Ibuprofen...)",
            "Thuốc hạ áp (Beta-blocker)"
        ],
        "action": "⚠️ BÁO với bác sĩ NẾU bị hen sau uống thuốc!"
    }
}

