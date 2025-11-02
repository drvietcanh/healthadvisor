"""
Đau đầu (Headache) - Thông tin cơ bản
Basic information about Headache
"""

from typing import Dict

HEADACHE_INFO = {
    "name": "Đau đầu",
    "name_en": "Headache",
    
    "simple_explanation": """
💡 Đau đầu là gì? (Giải thích đơn giản)

Tưởng tượng đầu như một chiếc bóng bay:
- BÌNH THƯỜNG: Bóng mềm, không căng
- ĐAU ĐẦU: Bóng BỊ ÉP, CĂNG, ĐAU NHỨC

🫁 Chuyện gì xảy ra:
1. Mạch máu não GIÃN RA hoặc CO THẮT → Kích thích dây thần kinh
2. Cơ cổ/gáy CO THẮT → Đau lan lên đầu
3. Dây thần kinh BỊ KÍCH THÍCH → Cảm giác đau

⚠️ ĐẶC ĐIỂM:
- Đa số ĐAU ĐẦU là LÀNH TÍNH (đau căng thẳng, đau nửa đầu)
- Một số ĐAU ĐẦU là NGUY HIỂM (u não, viêm màng não, xuất huyết não)
- Cần PHÂN BIỆT để biết khi nào cần cấp cứu!
    """,
    
    "definition": """
Đau đầu là cảm giác đau, nhức ở vùng đầu, có thể từ nhẹ đến rất nặng,
do nhiều nguyên nhân: Mạch máu, cơ, dây thần kinh, hoặc các bệnh nghiêm trọng.
    """,
    
    "statistics_vietnam": {
        "prevalence": "90% người từng đau đầu ít nhất 1 lần",
        "migraine": "8-12% dân số (nữ > nam 3 lần)",
        "tension": "Phổ biến nhất (70-80% đau đầu)",
        "chronic": "1-3% dân số đau đầu mạn tính",
        "severity": "Đau đầu là nguyên nhân phổ biến thứ 3 gây mất năng suất lao động"
    },
    
    "why_important": """
⚠️ TẠI SAO CẦN QUAN TÂM ĐAU ĐẦU?

1. **Ảnh hưởng cuộc sống:**
   - Đau đầu → Không làm việc được
   - Đau nửa đầu → Nôn, sợ ánh sáng, phải nằm phòng tối
   - → Mất năng suất, chất lượng cuộc sống

2. **Có thể là dấu hiệu nguy hiểm:**
   - Đau đầu ĐỘT NGỘT, DỮ DỘI → Xuất huyết não (TỬ VONG!)
   - Đau đầu + Sốt + Cứng gáy → Viêm màng não (NGUY HIỂM!)
   - Đau đầu tăng dần + Yếu tay chân → U não

3. **Cần điều trị đúng:**
   - Uống thuốc SAI → Không khỏi, tổn thương gan/thận
   - Đau nửa đầu cần thuốc ĐẶC HIỆU (không phải Paracetamol)
    """,
    
    "types": {
        "primary": {
            "name": "Đau đầu nguyên phát (Lành tính)",
            "description": "Đau đầu là bệnh chính, không do bệnh khác",
            "examples": [
                "Đau đầu căng thẳng (Tension headache) - Phổ biến nhất",
                "Đau nửa đầu (Migraine) - Nặng, có thể nôn",
                "Đau đầu từng chuỗi (Cluster headache) - Hiếm, rất đau"
            ]
        },
        "secondary": {
            "name": "Đau đầu thứ phát (Có thể nguy hiểm!)",
            "description": "Đau đầu do bệnh khác gây ra",
            "examples": [
                "Xuất huyết não, u não",
                "Viêm màng não, viêm xoang",
                "Tăng huyết áp, ngộ độc",
                "Chấn thương đầu"
            ],
            "warning": "⚠️ Cần tìm nguyên nhân và điều trị gốc!"
        }
    }
}

