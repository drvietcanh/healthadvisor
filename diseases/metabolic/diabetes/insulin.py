"""
Insulin - Các loại, Cách dùng, Bảo quản
Bao gồm: Insulin nhanh, ngắn, trung bình, dài, hỗn hợp
"""

INSULIN_INFO = {
    "when_vn": """
💉 KHI NÀO CẦN TIÊM INSULIN?

Típ 1: Luôn luôn cần insulin
Típ 2: Cần insulin khi:
- Thuốc uống không đủ kiểm soát
- HbA1c vẫn cao (> 9%)
- Đường huyết cao dai dẳng
- Mang thai
- Bệnh nặng, phẫu thuật
""",
    "types_simple": [
        {
            "type": "⚡ Insulin tác dụng CỰC NHANH (Ultra-fast)",
            "examples": "Novorapid (Aspart), Humalog (Lispro), Apidra (Glulisine), Fiasp",
            "vietnam_brands": "🇻🇳 Tại VN: NovoRapid FlexPen/Penfill 100IU/ml, Humalog KwikPen 100IU/ml, Apidra SoloStar",
            "when": "Tiêm TRƯỚC BỮA ĂN 0-15 phút (hoặc ngay sau ăn)",
            "duration": "⏱️ Bắt đầu: 10-20 phút | Đỉnh: 1-3 giờ | Kéo dài: 3-5 giờ",
            "use_case": "Dùng cho bữa ăn, điều chỉnh đường cao đột ngột",
            "icon": "⚡",
            "color": "Trong suốt"
        },
        {
            "type": "🔸 Insulin tác dụng NGẮN (Regular/Short-acting)",
            "examples": "Actrapid (Novo Nordisk), Humulin R (Eli Lilly), Insuman Rapid",
            "vietnam_brands": "🇻🇳 Tại VN: Actrapid HM Penfill 100IU/ml, Humulin R 100IU/ml lọ 10ml, Actrapid vial",
            "when": "Tiêm TRƯỚC BỮA ĂN 30 phút",
            "duration": "⏱️ Bắt đầu: 30 phút | Đỉnh: 2-4 giờ | Kéo dài: 6-8 giờ",
            "use_case": "Dùng cho bữa ăn (cần tính toán thời gian hơn insulin nhanh)",
            "icon": "🔸",
            "color": "Trong suốt"
        },
        {
            "type": "⬜ Insulin nền TRUNG BÌNH (NPH - Intermediate)",
            "examples": "Insulatard (Novo Nordisk), Humulin N (Eli Lilly), Insuman Basal",
            "vietnam_brands": "🇻🇳 Tại VN: Insulatard HM Penfill 100IU/ml, Humulin N vial 10ml, Insulatard FlexPen",
            "when": "Tiêm 1-2 lần/ngày (sáng và/hoặc tối trước ngủ)",
            "duration": "⏱️ Bắt đầu: 1-2 giờ | Đỉnh: 4-8 giờ | Kéo dài: 12-18 giờ",
            "use_case": "Duy trì đường huyết nền cả ngày",
            "icon": "⬜",
            "color": "Đục, màu sữa (PHẢI LẮC ĐỀU trước tiêm!)"
        },
        {
            "type": "⬛ Insulin nền DÀI (Long-acting)",
            "examples": "Lantus/Toujeo (Glargine), Levemir (Detemir), Tresiba (Degludec), Abasaglar",
            "vietnam_brands": "🇻🇳 Tại VN: Lantus SoloStar 100IU/ml, Toujeo SoloStar 300IU/ml, Levemir FlexPen, Tresiba FlexTouch, Abasaglar KwikPen",
            "when": "Tiêm 1 lần/ngày, CÙNG GIỜ mỗi ngày",
            "duration": "⏱️ Bắt đầu: 1-2 giờ | Không đỉnh rõ | Kéo dài: 20-24 giờ (Tresiba: 42 giờ)",
            "use_case": "Insulin nền tốt nhất, ít hạ đường, tiêm ít lần",
            "icon": "⬛",
            "color": "Trong suốt"
        },
        {
            "type": "🔀 Insulin HỖN HỢP (Premixed)",
            "examples": "NovoMix 30/50/70, Humalog Mix 25/50, Mixtard 30/40/50, Ryzodeg 70/30",
            "vietnam_brands": "🇻🇳 Tại VN: NovoMix 30 FlexPen (30% nhanh + 70% NPH), Humalog Mix 25 KwikPen, Mixtard 30 HM Penfill, Ryzodeg FlexTouch",
            "when": "Tiêm 2 lần/ngày (trước bữa sáng + bữa tối 15 phút)",
            "duration": "⏱️ Phối hợp insulin nhanh + chậm",
            "use_case": "Tiện lợi, không cần tiêm 2 loại riêng, phù hợp người già",
            "icon": "🔀",
            "color": "Đục (PHẢI LẮC 20 LẦN trước tiêm!)",
            "note": "Số 30/50/70 = % insulin tác dụng nhanh"
        }
    ],
    "how_to_inject_vn": """
💉 CÁCH TIÊM INSULIN:

📍 Vị trí tiêm:
- Bụng (hấp thu nhanh nhất) ✓ Tốt nhất
- Đùi
- Cánh tay
- Mông

⚠️ LUÂN CHUYỂN vị trí (không tiêm một chỗ)

🔧 Kỹ thuật:
1. Rửa tay
2. Lau vùng tiêm bằng cồn (nếu có)
3. Véo nhẹ da
4. Đâm kim vuông góc 90 độ
5. Tiêm chậm rãi
6. Đợi 5-10 giây trước khi rút kim
7. Bỏ kim vào hộp đựng kim an toàn

💾 BẢO QUẢN:
- Lọ chưa mở: Tủ lạnh (2-8°C)
- Lọ đang dùng: Nhiệt độ phòng (< 30°C), dùng trong 28 ngày
- KHÔNG để đông cứng
- KHÔNG để nắng
""",
    "hypoglycemia_vn": """
⚠️ HẠ ĐƯỜNG HUYẾT - NGUY HIỂM NHẤT KHI TIÊM INSULIN

🚨 Dấu hiệu (đường < 3.9 mmol/L / < 70 mg/dL):
- Đói bỗng dưng
- Run tay, run người
- Vã mồ hôi lạnh
- Tim đập nhanh
- Chóng mặt
- Lo lắng
- Nếu nặng: Lú lẫn, co giật, ngất

✅ XỬ TRÍ NGAY:
Quy tắc 15-15:
1. Ăn/uống 15g đường:
   - 3 viên đường
   - 1/2 lon nước ngọt
   - 1 thìa mật ong
   - 3-4 viên kẹo
2. Chờ 15 phút
3. Đo lại đường huyết
4. Nếu vẫn < 3.9: Lặp lại

⛔ Nếu bất tỉnh: GỌI 115, KHÔNG cho ăn uống (sặc)

💡 PHÒNG TRÁNH:
- Luôn mang kẹo/nước ngọt
- Ăn đúng giờ sau tiêm insulin
- Đo đường trước khi lái xe
- Mang thẻ "Tôi bị tiểu đường"
"""
}

# Insulin regimens (chế độ tiêm insulin)
INSULIN_REGIMENS = {
    "basal_bolus": {
        "name_vn": "Chế độ Nền + Bữa ăn (Basal-Bolus)",
        "description": "Insulin nền dài (1 lần/ngày) + Insulin nhanh (trước mỗi bữa ăn)",
        "example": "Lantus (tối) + Novorapid (sáng/trưa/tối trước ăn)",
        "pros": "Linh hoạt nhất, kiểm soát tốt nhất",
        "cons": "Tiêm nhiều lần (4 lần/ngày)",
        "suitable_for": "Típ 1, Típ 2 cần kiểm soát chặt"
    },
    "premixed": {
        "name_vn": "Chế độ Insulin hỗn hợp",
        "description": "Insulin hỗn hợp 2 lần/ngày (sáng + tối)",
        "example": "NovoMix 30 (trước bữa sáng + bữa tối)",
        "pros": "Đơn giản, ít lần tiêm",
        "cons": "Kém linh hoạt, phải ăn đúng giờ",
        "suitable_for": "Típ 2, người già"
    },
    "basal_only": {
        "name_vn": "Chỉ Insulin nền",
        "description": "Insulin nền dài 1 lần/ngày + Thuốc uống",
        "example": "Lantus (tối) + Metformin (sáng/tối)",
        "pros": "Đơn giản, chỉ tiêm 1 lần",
        "cons": "Không kiểm soát đường sau ăn",
        "suitable_for": "Típ 2 mới bắt đầu insulin"
    }
}

