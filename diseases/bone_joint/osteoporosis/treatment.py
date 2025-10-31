"""
Osteoporosis Treatment - Điều Trị Loãng Xương
"""

TREATMENT = {
    "title": "💊 Điều Trị Loãng Xương",
    
    "principles": {
        "title": "Nguyên Tắc:",
        "items": [
            "Bổ sung Canxi + Vitamin D (nền tảng)",
            "Thuốc tăng mật độ xương (nếu cần)",
            "Vận động hợp lý",
            "Phòng ngừa ngã"
        ]
    },
    
    "calcium_vitamin_d": {
        "title": "1. Canxi + Vitamin D (BẮT BUỘC):",
        "calcium": {
            "daily_dose": "1,000-1,200mg/ngày",
            "with_meal": "Nên uống sau ăn (dễ hấp thu)",
            "split_dose": "Chia 2 lần (500-600mg/lần)",
            "forms": [
                "Calcium Carbonate (rẻ, nhiều canxi)",
                "Calcium Citrate (dễ hấp thu, ít tác dụng phụ)"
            ],
            "brands_vn": [
                "Calcium Corbiere",
                "Calcium Sandoz",
                "Calci-D"
            ],
            "price": "100,000-200,000đ/tháng",
            "side_effects": [
                "Táo bón (uống nhiều nước, ăn nhiều chất xơ)",
                "Đầy bụng (chia nhỏ liều)"
            ]
        },
        "vitamin_d": {
            "daily_dose": "800-1,000 IU/ngày",
            "forms": [
                "Viên nén",
                "Nước uống"
            ],
            "brands_vn": [
                "Aquadetrim",
                "Vitamin D3",
                "Colecalciferol"
            ],
            "price": "50,000-100,000đ/tháng",
            "note": "Có thể kết hợp Canxi + Vitamin D trong 1 viên"
        }
    },
    
    "medications": {
        "title": "2. Thuốc Tăng Mật Độ Xương:",
        "description": "Dùng khi T-score < -2.5 hoặc đã gãy xương",
        "drugs": [
            {
                "name": "Bisphosphonates",
                "examples": ["Alendronate (Fosamax)", "Risedronate (Actonel)", "Zoledronic acid"],
                "how_it_works": "Làm chậm quá trình mất xương",
                "form": "Uống hoặc tiêm",
                "frequency": "Hàng tuần hoặc hàng năm (tiêm)",
                "price": "500,000-2,000,000đ/tháng",
                "side_effects": [
                    "Đau dạ dày (uống với nhiều nước, không nằm sau 30 phút)",
                    "Đau cơ, xương (tạm thời)",
                    "Viêm thực quản (hiếm)"
                ],
                "contraindication": "Suy thận nặng, phụ nữ có thai"
            },
            {
                "name": "Denosumab (Prolia)",
                "how_it_works": "Ức chế tế bào phá xương",
                "form": "Tiêm dưới da",
                "frequency": "6 tháng/lần",
                "price": "5,000,000-7,000,000đ/mũi",
                "note": "Đắt nhưng hiệu quả, tiện lợi"
            },
            {
                "name": "Teriparatide (Forteo)",
                "how_it_works": "Kích thích tạo xương mới",
                "form": "Tiêm dưới da hàng ngày",
                "duration": "Tối đa 2 năm",
                "price": "Rất đắt, chỉ dùng khi nặng",
                "indication": "Loãng xương nặng, đã gãy nhiều xương"
            }
        ]
    },
    
    "hormone_therapy": {
        "title": "3. Liệu Pháp Hormone (Phụ Nữ Mãn Kinh):",
        "description": "Bổ sung Estrogen (HRT) - chỉ khi cần và bác sĩ chỉ định",
        "note": "⚠️ Có nguy cơ ung thư, tim mạch - cân nhắc kỹ!"
    },
    
    "monitoring": {
        "title": "Theo Dõi Điều Trị:",
        "methods": [
            "Đo mật độ xương 1-2 năm/lần",
            "Xét nghiệm máu (canxi, vitamin D)",
            "Theo dõi tác dụng phụ",
            "Đánh giá nguy cơ gãy xương"
        ]
    }
}

