"""
Parkinson - Điều trị
"""

TREATMENT = {
    "medications": {
        "title": "💊 Thuốc điều trị (QUAN TRỌNG - Phải uống đều đặn):",
        "levodopa": {
            "title": "Levodopa (L-DOPA) - Thuốc chính:",
            "how_it_works": "Chuyển thành dopamine trong não → Bù đắp dopamine thiếu",
            "examples": [
                "Levodopa/Carbidopa (Sinemet, Madopar)",
                "Levodopa/Benserazide (Madopar)"
            ],
            "dosing": "Bắt đầu: 100mg x 2-3 lần/ngày, tăng dần theo chỉ định",
            "important": "⚠️ QUAN TRỌNG: Uống TRƯỚC ăn 30-60 phút (thức ăn làm giảm hấp thu)",
            "side_effects": "Có thể gây: Buồn nôn, tụt huyết áp, rối loạn vận động (giai đoạn muộn)"
        },
        "dopamine_agonists": {
            "title": "Thuốc kích thích dopamine (Dopamine agonists):",
            "examples": [
                "Pramipexole (Mirapex)",
                "Ropinirole (Requip)",
                "Rotigotine (Neupro - miếng dán)"
            ],
            "use": "Dùng đơn độc (giai đoạn sớm) hoặc kết hợp với Levodopa",
            "side_effects": "Có thể gây: Buồn ngủ, ảo giác, rối loạn hành vi"
        },
        "mao_b_inhibitors": {
            "title": "Ức chế MAO-B (Giữ dopamine lâu hơn):",
            "examples": [
                "Selegiline (Eldepryl)",
                "Rasagiline (Azilect)"
            ],
            "use": "Kết hợp với Levodopa hoặc dùng đơn độc giai đoạn sớm"
        },
        "comt_inhibitors": {
            "title": "Ức chế COMT (Tăng thời gian tác dụng của Levodopa):",
            "examples": [
                "Entacapone (Comtan)",
                "Tolcapone (Tasmar)"
            ],
            "use": "Dùng KẾT HỢP với Levodopa để kéo dài tác dụng"
        },
        "anticholinergics": {
            "title": "Thuốc kháng cholinergic (Giảm run):",
            "examples": [
                "Trihexyphenidyl (Artane)",
                "Benztropine (Cogentin)"
            ],
            "use": "Chủ yếu giảm run, ít dùng ở người già (gây lú lẫn)",
            "warning": "⚠️ Người già >70 tuổi: Tránh dùng (gây lú lẫn, táo bón)"
        },
        "important_notes": {
            "title": "⚠️ QUAN TRỌNG về thuốc:",
            "rules": [
                "✅ Uống thuốc ĐÚNG GIỜ, ĐỦ LIỀU - Không tự ý ngừng!",
                "✅ Levodopa: Uống TRƯỚC ăn 30-60 phút",
                "✅ Không tự ý thay đổi liều - Phải hỏi bác sĩ",
                "✅ Theo dõi tác dụng phụ và báo bác sĩ",
                "❌ Không ăn nhiều đạm cùng lúc với Levodopa (làm giảm tác dụng)",
                "❌ Không tự ý ngừng thuốc đột ngột (gây triệu chứng nặng)"
            ]
        }
    },
    
    "lifestyle": {
        "title": "💧 Thay đổi lối sống (QUAN TRỌNG):",
        "exercise": {
            "title": "Tập thể dục:",
            "benefits": [
                "✅ Giữ cơ khỏe mạnh, linh hoạt",
                "✅ Cải thiện dáng đi, thăng bằng",
                "✅ Giảm cứng cơ",
                "✅ Giữ tinh thần tích cực"
            ],
            "recommended": [
                "Đi bộ 30 phút/ngày (khi còn đi được)",
                "Tập dưỡng sinh, thái cực quyền",
                "Tập kéo giãn cơ (giảm cứng)",
                "Tập vật lý trị liệu (theo chỉ định)"
            ]
        },
        "diet": {
            "title": "Chế độ ăn:",
            "tips": [
                "✅ Ăn nhiều chất xơ (tránh táo bón) - Rau, trái cây",
                "✅ Uống đủ nước (2-3 lít/ngày)",
                "✅ Ăn protein cách xa thời gian uống Levodopa",
                "❌ Tránh rượu bia (làm nặng triệu chứng)",
                "❌ Tránh cà phê quá nhiều (ảnh hưởng giấc ngủ)"
            ]
        },
        "safety": {
            "title": "An toàn:",
            "tips": [
                "✅ Loại bỏ đồ vật gây vấp ngã trong nhà (thảm, dây điện)",
                "✅ Lắp tay vịn ở cầu thang, nhà tắm",
                "✅ Mang giày chống trơn",
                "✅ Không lái xe khi đang run, cứng cơ",
                "✅ Dùng gậy nếu cần (không xấu hổ!)"
            ]
        }
    },
    
    "advanced": {
        "title": "🔬 Điều trị nâng cao (Giai đoạn nặng):",
        "deep_brain_stimulation": {
            "title": "Kích thích não sâu (DBS - Deep Brain Stimulation):",
            "description": "Đặt điện cực vào não → Kích thích điện → Giảm triệu chứng",
            "when": "Khi thuốc không còn hiệu quả, có biến chứng",
            "benefits": "Giảm run, cứng cơ, giảm liều thuốc",
            "note": "Cần phẫu thuật, chi phí cao, chỉ một số trường hợp phù hợp"
        },
        "pump_therapy": {
            "title": "Bơm thuốc liên tục:",
            "description": "Bơm Levodopa trực tiếp vào ruột non qua ống",
            "when": "Khi uống thuốc không ổn định (on-off phenomenon)"
        }
    },
    
    "when_to_see_doctor": {
        "title": "🏥 Khi nào cần khám lại:",
        "regular": "Khám định kỳ mỗi 3-6 tháng với bác sĩ thần kinh",
        "urgent": [
            "🚨 Triệu chứng nặng hơn dù đã uống thuốc",
            "🚨 Thuốc không còn tác dụng (on-off)",
            "🚨 Có tác dụng phụ nghiêm trọng",
            "🚨 Ngã nhiều lần",
            "🚨 Lú lẫn, ảo giác"
        ]
    }
}

