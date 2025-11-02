"""
Viêm phổi - Nguyên nhân
Causes of Pneumonia
"""

from typing import Dict, List

CAUSES = {
    "bacteria": {
        "name": "Vi khuẩn",
        "description": "Nguyên nhân phổ biến nhất (60-70% ca)",
        "common": [
            {
                "name": "Phế cầu (Streptococcus pneumoniae)",
                "description": "Phổ biến nhất, gây viêm phổi điển hình (sốt cao, ho có đờm vàng)",
                "prevention": "Tiêm vaccine phế cầu (Pneumovax) cho người >65 tuổi, người bệnh mãn tính"
            },
            {
                "name": "Haemophilus influenzae",
                "description": "Thường gặp ở người COPD, hút thuốc",
                "risk": "Người già, suy giảm miễn dịch"
            },
            {
                "name": "Staphylococcus aureus",
                "description": "Nặng, thường sau cúm, có thể áp xe phổi",
                "risk": "Sau nhiễm virus, người bệnh viện"
            }
        ],
        "atypical": [
            {
                "name": "Mycoplasma pneumoniae",
                "description": "Viêm phổi không điển hình (ho khan, sốt nhẹ, đau họng)",
                "common": "Trẻ em, thanh niên"
            },
            {
                "name": "Chlamydia pneumoniae",
                "description": "Nhẹ, tự khỏi, ho dai dẳng",
                "treatment": "Kháng sinh nhóm Macrolide"
            }
        ]
    },
    
    "viruses": {
        "name": "Virus",
        "description": "20-30% ca, thường nhẹ hơn vi khuẩn",
        "common": [
            {
                "name": "COVID-19",
                "description": "Gây viêm phổi nặng, đặc biệt người già, bệnh nền",
                "prevention": "Tiêm vaccine COVID-19, đeo khẩu trang"
            },
            {
                "name": "Cúm (Influenza)",
                "description": "Cúm A/H1N1, H3N2 → Biến chứng viêm phổi nặng",
                "prevention": "Tiêm vaccine cúm hàng năm (người >65 tuổi, bệnh mãn tính)",
                "warning": "⚠️ Cúm + Viêm phổi = Rất nguy hiểm!"
            },
            {
                "name": "RSV (Respiratory Syncytial Virus)",
                "description": "Phổ biến ở trẻ nhỏ, người già",
                "risk": "Trẻ <2 tuổi, người >65 tuổi, suy giảm miễn dịch"
            },
            {
                "name": "Adenovirus",
                "description": "Gây viêm phổi ở trẻ em",
                "characteristics": "Sốt cao, ho khan, đau họng"
            }
        ]
    },
    
    "fungi": {
        "name": "Nấm",
        "description": "Hiếm gặp, thường ở người suy giảm miễn dịch nặng",
        "common": [
            "Cryptococcus (người HIV/AIDS)",
            "Aspergillus (người ghép tạng, hóa trị)",
            "Pneumocystis (người HIV/AIDS)"
        ],
        "risk_groups": "Người HIV/AIDS, ghép tạng, hóa trị, dùng corticoid lâu dài"
    },
    
    "risk_factors": {
        "name": "Yếu tố nguy cơ",
        "description": "Những người dễ bị viêm phổi:",
        "age": {
            "name": "Tuổi tác",
            "description": "Trẻ <5 tuổi, người >65 tuổi",
            "reason": "Hệ miễn dịch yếu, phản xạ bảo vệ kém"
        },
        "chronic_diseases": {
            "name": "Bệnh mãn tính",
            "diseases": [
                "COPD, Hen suyễn → Phổi yếu",
                "Tiểu đường → Miễn dịch kém",
                "Suy tim → Phù phổi, dễ nhiễm trùng",
                "Bệnh thận, gan → Miễn dịch yếu"
            ]
        },
        "lifestyle": {
            "name": "Lối sống",
            "factors": [
                "Hút thuốc lá → Phổi yếu, dễ nhiễm trùng",
                "Uống rượu nhiều → Giảm phản xạ ho, dễ hít sặc",
                "Suy dinh dưỡng → Miễn dịch yếu"
            ]
        },
        "immunosuppression": {
            "name": "Suy giảm miễn dịch",
            "causes": [
                "HIV/AIDS",
                "Hóa trị, xạ trị ung thư",
                "Dùng thuốc ức chế miễn dịch (ghép tạng)",
                "Corticoid lâu dài"
            ]
        },
        "other": {
            "name": "Khác",
            "factors": [
                "Nằm viện lâu → Vi khuẩn bệnh viện kháng thuốc",
                "Đặt ống thở máy → Vi khuẩn vào phổi dễ dàng",
                "Đột quỵ, bệnh thần kinh → Mất phản xạ ho, dễ hít sặc",
                "Thời tiết lạnh, ẩm → Dễ nhiễm trùng"
            ]
        }
    }
}

