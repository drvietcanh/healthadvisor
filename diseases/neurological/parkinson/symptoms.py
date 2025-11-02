"""
Parkinson - Triệu chứng
"""

SYMPTOMS = {
    "early": {
        "title": "🔍 Triệu chứng sớm (Giai đoạn đầu):",
        "symptoms": [
            "**Run nhẹ** - Thường bắt đầu ở một tay khi nghỉ (run khi để yên)",
            "**Chữ viết nhỏ dần** - Viết chữ ngày càng nhỏ (micrographia)",
            "**Khứu giác kém** - Không ngửi thấy mùi như trước",
            "**Giấc ngủ rối loạn** - Vung tay chân khi ngủ, la hét trong mơ",
            "**Táo bón** - Không rõ nguyên nhân",
            "**Mệt mỏi** - Cảm thấy yếu sức, không muốn làm gì",
            "**Đau vai, cổ** - Cứng cơ vùng vai cổ",
            "**Thay đổi giọng nói** - Nói nhỏ hơn, đơn điệu hơn"
        ],
        "note": "💡 Quan trọng: Phát hiện SỚM → Điều trị SỚM → Kết quả tốt hơn nhiều!"
    },
    
    "classic": {
        "title": "🎯 4 Triệu chứng ĐIỂN HÌNH (Tremor, Rigidity, Bradykinesia, Postural instability):",
        "tremor": {
            "name": "1. Run (Tremor)",
            "characteristics": [
                "Run khi NGHỈ (không làm gì) - Đặc trưng của Parkinson",
                "Run ở tay trước (thường một bên trước)",
                "Run như 'vê thuốc' - Ngón cái và ngón trỏ chà xát nhau",
                "Giảm run khi làm việc hoặc ngủ",
                "Khác run do tuổi già: Run khi NGHỈ (Parkinson) vs Run khi LÀM (run lành tính)"
            ]
        },
        "rigidity": {
            "name": "2. Cứng cơ (Rigidity)",
            "characteristics": [
                "Cơ cứng như gỗ - Gấp/duỗi khó khăn",
                "Đau cơ - Đặc biệt vai, cổ, lưng",
                "Di chuyển như robot - Không mượt mà",
                "Dáng đi cứng nhắc - Tay không vung tự nhiên"
            ]
        },
        "bradykinesia": {
            "name": "3. Chậm vận động (Bradykinesia)",
            "characteristics": [
                "Cử động CHẬM - Đứng lên, đi lại, quay người đều chậm",
                "Khó bắt đầu vận động - Như bị 'dính' xuống ghế",
                "Nét mặt ít biểu cảm - Mặt như đeo mặt nạ",
                "Nói chậm, giọng đơn điệu - Không có ngữ điệu",
                "Chữ viết nhỏ dần - Mỗi chữ càng viết càng nhỏ"
            ]
        },
        "postural": {
            "name": "4. Mất thăng bằng (Postural Instability)",
            "characteristics": [
                "Dáng đứng gù - Đầu và vai cúi về phía trước",
                "Dễ ngã - Đặc biệt khi quay người, đứng lên",
                "Bước đi ngắn, chân kéo lê",
                "Đứng không vững - Dễ đẩy ngã khi bị tác động nhẹ"
            ],
            "note": "⚠️ Triệu chứng này xuất hiện MUỘN (giai đoạn nặng)"
        }
    },
    
    "other": {
        "title": "📋 Triệu chứng khác:",
        "non_motor": [
            "**Mất khứu giác** - Không ngửi thấy mùi (thường xuất hiện SỚM)",
            "**Táo bón** - Do nhu động ruột chậm",
            "**Rối loạn giấc ngủ** - Khó ngủ, la hét khi ngủ (do mơ)",
            "**Trầm cảm** - Buồn bã, chán nản",
            "**Suy giảm nhận thức** - Lú lẫn, mất trí nhớ (giai đoạn muộn)",
            "**Mệt mỏi** - Yếu sức, không có năng lượng"
        ]
    },
    
    "when_to_see_doctor": {
        "title": "🏥 Khi nào cần khám bác sĩ:",
        "urgent": [
            "🚨 Có bất kỳ triệu chứng run, cứng cơ, chậm vận động",
            "🚨 Chữ viết thay đổi (nhỏ dần)",
            "🚨 Mất khứu giác đột ngột",
            "🚨 Dáng đi thay đổi (kéo lê chân, không vung tay)",
            "🚨 Thường xuyên ngã không rõ nguyên nhân"
        ],
        "note": "💡 Quan trọng: Parkinson phát hiện SỚM → Điều trị SỚM → Chất lượng sống tốt hơn nhiều! Đừng nghĩ 'đó chỉ là tuổi già'!"
    }
}

