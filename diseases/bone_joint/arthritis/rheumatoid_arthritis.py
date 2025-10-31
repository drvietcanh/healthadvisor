"""
Rheumatoid Arthritis - Viêm khớp dạng thấp
Bệnh tự miễn, khác với thoái hóa khớp
"""

RHEUMATOID_ARTHRITIS_INFO = {
    "title": "🔴 Viêm Khớp Dạng Thấp (Rheumatoid Arthritis)",
    "simple_explanation": """
💡 Viêm khớp dạng thấp là gì?

Khác với thoái hóa khớp (mòn tự nhiên), viêm khớp dạng thấp là bệnh TỰ MIỄN:
- Hệ miễn dịch tấn công nhầm vào khớp → Viêm, sưng, đau
- Không chỉ mòn, mà là VIÊM MẠN TÍNH
- Ảnh hưởng nhiều khớp (đối xứng 2 bên)
- Có thể ảnh hưởng tim, phổi, mắt

🕐 Ai dễ bị?
- Phụ nữ (2-3 lần nam giới)
- Tuổi 30-60
- Gia đình có người bị
- Hút thuốc lá
    """,
    
    "key_differences": {
        "osteoarthritis": "Thoái hóa: Mòn tự nhiên, đau khi vận động, 1 vài khớp",
        "rheumatoid": "Viêm dạng thấp: Tự miễn, viêm nhiều khớp, đau cả khi nghỉ"
    }
}

RHEUMATOID_ARTHRITIS_SYMPTOMS = {
    "title": "🔍 Triệu Chứng Viêm Khớp Dạng Thấp",
    
    "early_symptoms": [
        "Đau, sưng khớp (thường khớp nhỏ: ngón tay, cổ tay, bàn chân)",
        "Cứng khớp buổi sáng >30 phút (đặc trưng!)",
        "Mệt mỏi, sốt nhẹ",
        "Các khớp 2 bên đều bị (đối xứng)",
        "Đau cả khi nghỉ (khác thoái hóa)"
    ],
    
    "advanced_symptoms": [
        "Biến dạng khớp (ngón tay vẹo, cổ tay lệch)",
        "Teo cơ quanh khớp",
        "Nổi hạt dưới da (rheumatoid nodules)",
        "Viêm mạch máu",
        "Ảnh hưởng tim, phổi, mắt"
    ],
    
    "red_flags": [
        "🚨 Sưng nóng đỏ nhiều khớp cùng lúc",
        "🚨 Cứng khớp buổi sáng >1 giờ",
        "🚨 Mệt mỏi, sốt, sụt cân",
        "🚨 Các khớp nhỏ (ngón tay, cổ tay) bị trước"
    ]
}

RHEUMATOID_ARTHRITIS_TREATMENT = {
    "title": "💊 Điều Trị Viêm Khớp Dạng Thấp",
    
    "importance": """
⚠️ QUAN TRỌNG: Phải điều trị SỚM và TÍCH CỰC!
- Nếu không điều trị → Hủy khớp, tàn phế trong 2-3 năm
- Điều trị sớm → Ngăn hủy khớp, giữ chức năng
- Cần bác sĩ chuyên khoa KHỚP (Rheumatologist)
    """,
    
    "medications": {
        "dmards": {
            "title": "DMARDs - Thuốc cơ bản (Quan trọng nhất!)",
            "explanation": "Ức chế hệ miễn dịch → Giảm viêm, ngăn hủy khớp",
            "examples": [
                {
                    "drug": "Methotrexate",
                    "dose": "7.5-25mg/tuần (1 lần/tuần)",
                    "note": "Thuốc số 1, rẻ, hiệu quả. Uống với axit folic để giảm tác dụng phụ"
                },
                {
                    "drug": "Sulfasalazine",
                    "dose": "2-3g/ngày",
                    "note": "An toàn, tốt cho khớp nhỏ"
                },
                {
                    "drug": "Leflunomide",
                    "dose": "10-20mg/ngày",
                    "note": "Tác dụng tương đương Methotrexate"
                }
            ],
            "duration": "Dùng lâu dài (nhiều năm), không ngưng đột ngột"
        },
        
        "biologicals": {
            "title": "Thuốc sinh học (Cho trường hợp nặng)",
            "explanation": "Thuốc mới, đắt, hiệu quả cao",
            "examples": [
                "Adalimumab (Humira) - Tiêm dưới da",
                "Etanercept (Enbrel) - Tiêm dưới da",
                "Tocilizumab (Actemra) - Truyền tĩnh mạch"
            ],
            "cost": "5-15 triệu đồng/tháng",
            "when": "DMARDs không đáp ứng",
            "note": "Cần theo dõi chặt chẽ vì ức chế miễn dịch mạnh"
        },
        
        "symptom_relief": {
            "title": "Thuốc giảm đau tạm thời",
            "nsaids": {
                "drug": "NSAIDs (Ibuprofen, Diclofenac)",
                "purpose": "Giảm đau, viêm nhanh",
                "note": "Chỉ giảm triệu chứng, KHÔNG ngăn hủy khớp"
            },
            "steroids": {
                "drug": "Corticosteroid (Prednisone)",
                "purpose": "Giảm viêm mạnh, nhanh",
                "note": "Dùng liều thấp, ngắn ngày. Có tác dụng phụ nếu dùng lâu"
            }
        }
    },
    
    "treatment_goal": [
        "Giảm đau, viêm",
        "Ngăn hủy khớp",
        "Giữ chức năng khớp",
        "Ngăn biến chứng tim, phổi"
    ]
}

RHEUMATOID_ARTHRITIS_MEDICATIONS = {
    "dmard_regimens": {
        "first_line": {
            "drug": "Methotrexate đơn độc",
            "dose": "7.5-25mg/tuần",
            "duration": "2-3 tháng để đánh giá",
            "if_fail": "Thêm Sulfasalazine hoặc Hydroxychloroquine"
        },
        "combination": {
            "name": "Phối hợp DMARDs",
            "example": "Methotrexate + Sulfasalazine + Hydroxychloroquine",
            "when": "Đơn độc không đủ",
            "note": "Phối hợp nhiều thuốc hiệu quả hơn 1 thuốc liều cao"
        },
        "biological": {
            "when": "DMARDs không đáp ứng sau 3-6 tháng",
            "note": "Đắt, cần chỉ định bác sĩ chuyên khoa"
        }
    },
    
    "monitoring": [
        "Xét nghiệm máu mỗi 1-3 tháng (gan, thận, máu)",
        "Theo dõi triệu chứng đau, sưng",
        "Chụp X-quang khớp định kỳ (6-12 tháng)",
        "Theo dõi tác dụng phụ"
    ],
    
    "important_notes": [
        "✅ Dùng DMARDs ĐỀU ĐẶN, không bỏ quên",
        "✅ Kết hợp thuốc giảm đau khi cần",
        "✅ Tập thể dục nhẹ (không bỏ tập!)",
        "✅ Nghỉ ngơi khi viêm cấp",
        "❌ Không tự ý ngưng thuốc",
        "❌ Tránh nhiễm trùng (ức chế miễn dịch)",
        "⚠️ Phụ nữ: Tránh thai khi dùng DMARDs (gây dị tật thai)"
    ]
}

