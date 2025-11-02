"""
Suy Thận Mạn - Chế độ ăn
Diet for Chronic Kidney Disease
"""

from typing import Dict, List

DIET = {
    "general_principles": {
        "title": "🍽️ Nguyên Tắc Chung",
        "description": "Chế độ ăn thay đổi theo giai đoạn suy thận:",
        "stages": [
            {
                "stage": "Giai đoạn 1-2 (Nhẹ)",
                "diet": "Gần như bình thường, chỉ cần:",
                "restrictions": [
                    "Ăn ít muối (<5g/ngày)",
                    "Uống đủ nước (1.5-2L/ngày)",
                    "Kiểm soát tiểu đường, huyết áp"
                ]
            },
            {
                "stage": "Giai đoạn 3 (Trung bình)",
                "diet": "Bắt đầu hạn chế:",
                "restrictions": [
                    "Ăn ít muối (<3g/ngày)",
                    "Hạn chế đạm (0.8g/kg cân nặng)",
                    "Hạn chế kali (nếu kali máu cao)",
                    "Uống nước vừa phải"
                ]
            },
            {
                "stage": "Giai đoạn 4-5 (Nặng)",
                "diet": "Hạn chế chặt chẽ:",
                "restrictions": [
                    "Ăn ít muối (<2g/ngày)",
                    "Hạn chế đạm (0.6g/kg)",
                    "Hạn chế kali chặt chẽ",
                    "Hạn chế phốt pho",
                    "Hạn chế nước (nếu phù)"
                ]
            }
        ]
    },
    
    "salt_restriction": {
        "title": "🧂 Hạn Chế Muối",
        "description": "Quan trọng nhất - Giảm phù, huyết áp:",
        "target": {
            "stage_1_2": "<5g/ngày (<1 thìa cà phê)",
            "stage_3": "<3g/ngày",
            "stage_4_5": "<2g/ngày"
        },
        "avoid": [
            "Muối ăn, nước mắm, nước tương (nhiều muối)",
            "Đồ muối chua (dưa, cà)",
            "Thực phẩm chế biến sẵn (xúc xích, thịt nguội, đồ hộp)",
            "Snack mặn (bim bim, lạc rang muối)",
            "Nước chấm, gia vị"
        ],
        "tips": [
            "Dùng gia vị khác: Chanh, tỏi, ớt, hành",
            "Nấu tại nhà (kiểm soát được muối)",
            "Đọc nhãn thực phẩm (chọn loại ít muối)",
            "Nếm trước khi cho muối"
        ]
    },
    
    "protein_restriction": {
        "title": "🥩 Hạn Chế Đạm (Giai đoạn 3-5)",
        "description": "Giảm gánh nặng cho thận:",
        "target": {
            "stage_3": "0.8g/kg cân nặng",
            "stage_4_5": "0.6g/kg cân nặng",
            "example": "Người 60kg: 36-48g đạm/ngày"
        },
        "high_protein": [
            "Thịt (100g = 20g đạm)",
            "Cá (100g = 18g đạm)",
            "Trứng (1 quả = 6g đạm)",
            "Đậu (100g = 20g đạm)"
        ],
        "low_protein": [
            "Rau xanh (ít đạm)",
            "Trái cây (ít đạm)",
            "Tinh bột (gạo, mì, bánh mì - ít đạm)"
        ],
        "tips": [
            "Ưu tiên đạm chất lượng cao (thịt, cá, trứng) - Ít nhưng đủ",
            "Giảm đạm từ thực vật (đậu)",
            "Có thể cần tư vấn dinh dưỡng để đảm bảo đủ dinh dưỡng"
        ],
        "warning": "⚠️ Đừng giảm đạm quá mức → Suy dinh dưỡng! Phải có tư vấn dinh dưỡng!"
    },
    
    "potassium_restriction": {
        "title": "🍌 Hạn Chế Kali (Nếu Kali Máu Cao)",
        "description": "Kali cao → Loạn nhịp tim nguy hiểm:",
        "when": "Khi kali máu >5.0 mEq/L (giai đoạn 3-5)",
        "target": "<2-3g kali/ngày",
        "high_potassium": [
            "Chuối (1 quả = 400mg)",
            "Cam, quýt",
            "Rau lá xanh (rau cải, bông cải)",
            "Khoai tây",
            "Cà chua",
            "Đậu",
            "Nước dừa",
            "Chocolate"
        ],
        "low_potassium": [
            "Táo, lê",
            "Dưa hấu",
            "Rau cải trắng",
            "Dưa chuột",
            "Cà rốt"
        ],
        "tips": [
            "Ngâm rau củ trong nước 2 giờ → Giảm kali một phần",
            "Luộc rau, bỏ nước → Giảm kali",
            "Ăn trái cây ít kali",
            "Tránh nước ép (nhiều kali)"
        ],
        "warning": "⚠️ Kali máu >5.5 mEq/L → Nguy hiểm! Phải hạn chế chặt chẽ!"
    },
    
    "phosphorus_restriction": {
        "title": "🥛 Hạn Chế Phốt Pho (Giai đoạn 3-5)",
        "description": "Phốt pho cao → Ngứa da, loãng xương:",
        "target": "<800-1000mg/ngày",
        "high_phosphorus": [
            "Sữa, phô mai",
            "Cá, hải sản",
            "Đậu, hạt",
            "Thịt nội tạng",
            "Thực phẩm chế biến sẵn (có chất phụ gia phốt pho)"
        ],
        "tips": [
            "Hạn chế sữa (chọn loại ít phốt pho)",
            "Dùng thuốc gắn phốt pho trong bữa ăn",
            "Đọc nhãn thực phẩm (tránh chất phụ gia phốt pho)"
        ]
    },
    
    "fluid_restriction": {
        "title": "💧 Hạn Chế Nước (Nếu Phù, Giai Đoạn 4-5)",
        "description": "Phù do nước dư thừa:",
        "when": "Khi phù, hoặc gần chạy thận",
        "amount": "Lượng nước = Lượng nước tiểu + 500mL",
        "example": "Nếu tiểu 500mL/ngày → Uống 1000mL/ngày",
        "includes": [
            "Nước uống",
            "Canh, súp",
            "Trái cây nhiều nước (dưa hấu)",
            "Nước trong thức ăn"
        ],
        "tips": [
            "Uống từng ngụm nhỏ",
            "Súc miệng khi khát (không nuốt)",
            "Ăn đá viên (tính vào lượng nước)",
            "Theo dõi cân nặng (tăng cân = tích nước)"
        ],
        "warning": "⚠️ Không hạn chế nước quá mức → Mất nước! Phải theo chỉ định bác sĩ!"
    },
    
    "sample_meal": {
        "title": "🍽️ Mẫu Bữa Ăn (Giai Đoạn 3)",
        "breakfast": [
            "1 bát phở (ít nước mắm)",
            "1 quả táo",
            "Không uống sữa"
        ],
        "lunch": [
            "Cơm 1 bát",
            "Thịt gà luộc 50g",
            "Rau cải trắng luộc (ít)",
            "Canh không muối"
        ],
        "dinner": [
            "Cơm 1 bát",
            "Cá kho (ít nước mắm)",
            "Rau luộc",
            "Trái cây: Dưa hấu 1 miếng nhỏ"
        ],
        "note": "💡 Mỗi người khác nhau - Cần tư vấn dinh dưỡng cá nhân hóa!"
    }
}

