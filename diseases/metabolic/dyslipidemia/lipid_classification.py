"""
Phân loại mức Lipid Máu
Lipid Level Classification
"""

from typing import Dict, Optional
from .diagnosis import LIPID_CATEGORIES


def classify_lipid_levels(
    cholesterol: Optional[float] = None,
    ldl: Optional[float] = None,
    hdl: Optional[float] = None,
    triglyceride: Optional[float] = None,
    gender: str = "male"
) -> Dict:
    """
    Phân loại mức lipid máu
    
    Args:
        cholesterol: Cholesterol toàn phần (mg/dL)
        ldl: LDL-C (mg/dL)
        hdl: HDL-C (mg/dL)
        triglyceride: Triglyceride (mg/dL)
        gender: "male" hoặc "female"
    
    Returns:
        Dict với classification cho từng chỉ số
    """
    result = {}
    
    # Classify Cholesterol
    if cholesterol:
        for cat in LIPID_CATEGORIES["cholesterol"]:
            if cat["range"][0] <= cholesterol < cat["range"][1]:
                result["cholesterol"] = {
                    "value": cholesterol,
                    "label": cat["label"],
                    "color": cat["color"],
                    "icon": cat["icon"]
                }
                break
    
    # Classify LDL
    if ldl:
        for cat in LIPID_CATEGORIES["ldl"]:
            if cat["range"][0] <= ldl < cat["range"][1]:
                result["ldl"] = {
                    "value": ldl,
                    "label": cat["label"],
                    "color": cat["color"],
                    "icon": cat["icon"]
                }
                break
    
    # Classify HDL (khác nhau nam/nữ)
    if hdl:
        hdl_cats = LIPID_CATEGORIES["hdl_male"] if gender == "male" else LIPID_CATEGORIES["hdl_female"]
        for cat in hdl_cats:
            if cat["range"][0] <= hdl < cat["range"][1]:
                result["hdl"] = {
                    "value": hdl,
                    "label": cat["label"],
                    "color": cat["color"],
                    "icon": cat["icon"]
                }
                break
    
    # Classify Triglyceride
    if triglyceride:
        for cat in LIPID_CATEGORIES["triglyceride"]:
            if cat["range"][0] <= triglyceride < cat["range"][1]:
                result["triglyceride"] = {
                    "value": triglyceride,
                    "label": cat["label"],
                    "color": cat["color"],
                    "icon": cat["icon"]
                }
                break
    
    # Tính các tỷ lệ
    if cholesterol and hdl:
        tc_hdl_ratio = cholesterol / hdl
        if tc_hdl_ratio < 3.5:
            ratio_assessment = "Tốt"
            ratio_color = "#4CAF50"
        elif tc_hdl_ratio < 5.0:
            ratio_assessment = "Trung bình"
            ratio_color = "#FF9800"
        else:
            ratio_assessment = "Nguy cơ cao"
            ratio_color = "#F44336"
        
        result["tc_hdl_ratio"] = {
            "value": round(tc_hdl_ratio, 2),
            "assessment": ratio_assessment,
            "color": ratio_color,
            "target": "<3.5"
        }
    
    # Non-HDL
    if cholesterol and hdl:
        non_hdl = cholesterol - hdl
        result["non_hdl"] = {
            "value": round(non_hdl, 1),
            "target": "<130 mg/dL",
            "assessment": "Tốt" if non_hdl < 130 else "Cao"
        }
    
    return result


