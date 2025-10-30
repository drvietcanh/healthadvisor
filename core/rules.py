"""
Core triage rules for StrokeAdvisor.
Deterministic rule-based decision making for stroke screening.
"""
from core.models import AcuteInput, TriageResult, TriageLevel


def triage(input_data: AcuteInput) -> TriageResult:
    """
    Main triage function - evaluates input and returns triage level with explanation.
    
    RED flags (call 115 immediately):
    - Any BE-FAST positive with acute onset (LKW ≤ 24h)
    - Thunderclap headache
    - Head trauma with neurological deficits
    - Anticoagulant use with neurological deficits
    - Decreased consciousness
    - Posterior circulation signs with acute onset
    
    AMBER flags (ED within 24h):
    - TIA-like symptoms (transient, now resolved) with risk factors
    
    GREEN:
    - No acute high-risk pattern detected
    """
    rules_fired = []
    
    # Check for decreased consciousness - always RED
    if input_data.decreased_consciousness:
        rules_fired.append("Giảm ý thức / Decreased consciousness")
        return TriageResult(
            level="RED",
            message_vn="🚨 GỌI 115 NGAY - Giảm ý thức là dấu hiệu nghiêm trọng!",
            message_en="🚨 CALL 115 NOW - Decreased consciousness is a critical sign!",
            rules_fired=rules_fired,
            next_steps_vn="Không tự lái xe. Không ăn uống. Ghi lại thời điểm bình thường cuối cùng. Mang theo danh sách thuốc đang dùng.",
            next_steps_en="Do not drive. Nothing by mouth. Record last known well time. Bring medication list.",
            show_lkw_recorder=True,
            show_hospital_map=True
        )
    
    # Check for BE-FAST signs with acute onset
    befast_positive = any([
        input_data.befast_balance,
        input_data.befast_eyes,
        input_data.befast_face,
        input_data.befast_arm,
        input_data.befast_speech
    ])
    
    if befast_positive:
        if input_data.lkw_minutes is not None and input_data.lkw_minutes <= 24 * 60:
            # Determine which signs are positive
            positive_signs = []
            if input_data.befast_balance:
                positive_signs.append("Mất thăng bằng/Balance")
            if input_data.befast_eyes:
                positive_signs.append("Rối loạn nhìn/Eyes")
            if input_data.befast_face:
                positive_signs.append("Xệ mặt/Face")
            if input_data.befast_arm:
                positive_signs.append("Yếu tay chân/Arm")
            if input_data.befast_speech:
                positive_signs.append("Khó nói/Speech")
            
            rules_fired.append(f"BE-FAST dương tính: {', '.join(positive_signs)}")
            rules_fired.append(f"Khởi phát cấp (≤24 giờ)")
            
            return TriageResult(
                level="RED",
                message_vn=f"🚨 GỌI 115 NGAY - Nghi ngờ đột quỵ!\n\nDấu hiệu: {', '.join(positive_signs)}\nThời gian: {input_data.lkw_minutes // 60} giờ {input_data.lkw_minutes % 60} phút trước",
                message_en=f"🚨 CALL 115 NOW - Suspected stroke!\n\nSigns: {', '.join(positive_signs)}\nTime: {input_data.lkw_minutes // 60}h {input_data.lkw_minutes % 60}m ago",
                rules_fired=rules_fired,
                next_steps_vn="🏥 Tại bệnh viện sẽ:\n• CT/CTA não ngay\n• Xét nghiệm cấp cứu\n• Đánh giá tiêu sợi huyết (nếu trong 4.5 giờ)\n• Đánh giá lấy huyết khối (nếu trong 24 giờ)",
                next_steps_en="🏥 At hospital:\n• Brain CT/CTA\n• Emergency labs\n• Thrombolysis evaluation (if within 4.5h)\n• Thrombectomy evaluation (if within 24h)",
                show_lkw_recorder=True,
                show_hospital_map=True
            )
    
    # Check for thunderclap headache (hemorrhage suspicion)
    if input_data.thunderclap_headache:
        rules_fired.append("Nhức đầu dữ dội đột ngột / Thunderclap headache")
        return TriageResult(
            level="RED",
            message_vn="🚨 GỌI 115 NGAY - Nhức đầu dữ dội đột ngột có thể là xuất huyết não!",
            message_en="🚨 CALL 115 NOW - Thunderclap headache may indicate brain hemorrhage!",
            rules_fired=rules_fired,
            next_steps_vn="🏥 Cần CT não cấp cứu để loại trừ xuất huyết não, phình mạch máu não vỡ.",
            next_steps_en="🏥 Emergency brain CT needed to rule out hemorrhage or ruptured aneurysm.",
            show_lkw_recorder=True,
            show_hospital_map=True
        )
    
    # Check for head trauma with any neuro signs
    if input_data.head_trauma and befast_positive:
        rules_fired.append("Chấn thương đầu + triệu chứng thần kinh / Head trauma + neurological signs")
        return TriageResult(
            level="RED",
            message_vn="🚨 GỌI 115 NGAY - Chấn thương đầu kèm triệu chứng thần kinh!",
            message_en="🚨 CALL 115 NOW - Head trauma with neurological symptoms!",
            rules_fired=rules_fired,
            next_steps_vn="🏥 Cần đánh giá chấn thương sọ não và xuất huyết nội sọ.",
            next_steps_en="🏥 Need evaluation for traumatic brain injury and intracranial bleeding.",
            show_lkw_recorder=True,
            show_hospital_map=True
        )
    
    # Check for anticoagulant use with any neuro signs
    if input_data.anticoagulant_use and befast_positive:
        rules_fired.append("Dùng thuốc chống đông + triệu chứng thần kinh / Anticoagulant + neurological signs")
        return TriageResult(
            level="RED",
            message_vn="🚨 GỌI 115 NGAY - Đang dùng thuốc chống đông và có triệu chứng thần kinh!\n\n⚠️ Nguy cơ xuất huyết cao - cần đánh giá ngay!",
            message_en="🚨 CALL 115 NOW - On anticoagulants with neurological symptoms!\n\n⚠️ High bleeding risk - immediate evaluation needed!",
            rules_fired=rules_fired,
            next_steps_vn="🏥 Mang theo danh sách thuốc đang dùng. Bác sĩ cần biết loại thuốc chống đông và liều dùng.",
            next_steps_en="🏥 Bring medication list. Doctors need to know type and dose of anticoagulant.",
            show_lkw_recorder=True,
            show_hospital_map=True
        )
    
    # Check for posterior circulation signs
    posterior_red_flags = ["vertigo", "ataxia", "diplopia", "dysphagia", "dysarthria"]
    has_posterior_signs = any(sign in input_data.posterior_signs for sign in posterior_red_flags)
    
    if has_posterior_signs and input_data.lkw_minutes is not None and input_data.lkw_minutes <= 24 * 60:
        rules_fired.append("Dấu hiệu tuần hoàn sau + khởi phát cấp / Posterior circulation signs + acute onset")
        return TriageResult(
            level="RED",
            message_vn=f"🚨 GỌI 115 NGAY - Nghi ngờ đột quỵ tuần hoàn sau!\n\nDấu hiệu: {', '.join(input_data.posterior_signs)}",
            message_en=f"🚨 CALL 115 NOW - Suspected posterior circulation stroke!\n\nSigns: {', '.join(input_data.posterior_signs)}",
            rules_fired=rules_fired,
            next_steps_vn="🏥 Đột quỵ tuần hoàn sau (thân não, tiểu não) dễ bỏ sót. Cần đánh giá chuyên khoa ngay.",
            next_steps_en="🏥 Posterior circulation strokes (brainstem, cerebellum) are easily missed. Specialist evaluation needed.",
            show_lkw_recorder=True,
            show_hospital_map=True
        )
    
    # Check for pregnancy/postpartum with any neuro signs
    if input_data.pregnant_or_postpartum and befast_positive:
        rules_fired.append("Thai kỳ/sau sinh + triệu chứng thần kinh / Pregnancy/postpartum + neurological signs")
        return TriageResult(
            level="RED",
            message_vn="🚨 GỌI 115 NGAY - Thai kỳ hoặc sau sinh với triệu chứng thần kinh!\n\n⚠️ Nguy cơ đột quỵ tăng trong thai kỳ và sau sinh.",
            message_en="🚨 CALL 115 NOW - Pregnancy or postpartum with neurological symptoms!\n\n⚠️ Stroke risk is elevated during pregnancy and postpartum.",
            rules_fired=rules_fired,
            next_steps_vn="🏥 Cần đánh giá chuyên khoa sản và thần kinh.",
            next_steps_en="🏥 Need obstetric and neurological specialist evaluation.",
            show_lkw_recorder=True,
            show_hospital_map=True
        )
    
    # If we have transient symptoms (now resolved) - possible TIA
    if befast_positive and (input_data.lkw_minutes is None or input_data.lkw_minutes > 24 * 60):
        rules_fired.append("Triệu chứng thoáng qua - nghi ngờ TIA / Transient symptoms - suspected TIA")
        return TriageResult(
            level="AMBER",
            message_vn="⚠️ KHÁM CẤP CỨU TRONG 24 GIỜ - Nghi ngờ cơn thiếu máu não thoáng qua (TIA)\n\nTIA là dấu hiệu cảnh báo đột quỵ sắp xảy ra!",
            message_en="⚠️ ED VISIT WITHIN 24 HOURS - Suspected transient ischemic attack (TIA)\n\nTIA is a warning sign of impending stroke!",
            rules_fired=rules_fired,
            next_steps_vn="🏥 Cần:\n• Đánh giá nguy cơ (ABCD²)\n• Hình ảnh mạch máu não\n• Siêu âm tim, Holter\n• Bắt đầu điều trị phòng ngừa",
            next_steps_en="🏥 Need:\n• Risk assessment (ABCD²)\n• Brain vascular imaging\n• Cardiac echo, Holter\n• Start preventive treatment",
            show_lkw_recorder=False,
            show_hospital_map=True
        )
    
    # No acute high-risk pattern detected
    rules_fired.append("Không phát hiện dấu hiệu đột quỵ cấp / No acute stroke signs detected")
    return TriageResult(
        level="GREEN",
        message_vn="✅ KHÔNG GỢI Ý ĐỘT QUỴ CẤP\n\nTuy nhiên, nếu có bất kỳ triệu chứng mới hoặc xấu đi, hãy gọi 115 ngay.",
        message_en="✅ NO ACUTE STROKE SIGNS DETECTED\n\nHowever, if any new or worsening symptoms develop, call 115 immediately.",
        rules_fired=rules_fired,
        next_steps_vn="📚 Tìm hiểu:\n• Dấu hiệu nhận biết đột quỵ (BE-FAST)\n• Các yếu tố nguy cơ\n• Phòng ngừa đột quỵ\n• Khi nào cần gọi 115",
        next_steps_en="📚 Learn about:\n• Stroke recognition (BE-FAST)\n• Risk factors\n• Stroke prevention\n• When to call 115",
        show_lkw_recorder=False,
        show_hospital_map=False
    )


def check_thrombolysis_window(lkw_minutes: int) -> dict:
    """Check if patient is within thrombolysis treatment window."""
    if lkw_minutes <= 270:  # 4.5 hours
        return {
            "eligible": True,
            "message_vn": f"✅ Trong khung giờ tiêu sợi huyết (≤ 4.5 giờ). Còn {270 - lkw_minutes} phút!",
            "message_en": f"✅ Within thrombolysis window (≤ 4.5h). {270 - lkw_minutes} minutes remaining!",
            "urgency": "CRITICAL"
        }
    elif lkw_minutes <= 540:  # 9 hours (extended criteria)
        return {
            "eligible": True,
            "message_vn": f"⚠️ Có thể đủ điều kiện tiêu sợi huyết (tiêu chí mở rộng với hình ảnh). Còn {540 - lkw_minutes} phút!",
            "message_en": f"⚠️ May qualify for thrombolysis (extended criteria with imaging). {540 - lkw_minutes} minutes remaining!",
            "urgency": "HIGH"
        }
    else:
        return {
            "eligible": False,
            "message_vn": "❌ Ngoài khung giờ tiêu sợi huyết tiêu chuẩn.",
            "message_en": "❌ Outside standard thrombolysis window.",
            "urgency": "LOW"
        }


def check_thrombectomy_window(lkw_minutes: int) -> dict:
    """Check if patient is within thrombectomy treatment window."""
    if lkw_minutes <= 360:  # 6 hours
        return {
            "eligible": True,
            "message_vn": f"✅ Trong khung giờ lấy huyết khối (≤ 6 giờ). Còn {360 - lkw_minutes} phút!",
            "message_en": f"✅ Within thrombectomy window (≤ 6h). {360 - lkw_minutes} minutes remaining!",
            "urgency": "CRITICAL"
        }
    elif lkw_minutes <= 1440:  # 24 hours (extended criteria)
        return {
            "eligible": True,
            "message_vn": f"⚠️ Có thể đủ điều kiện lấy huyết khối (tiêu chí mở rộng 6-24h với hình ảnh). Còn {1440 - lkw_minutes} phút!",
            "message_en": f"⚠️ May qualify for thrombectomy (extended 6-24h criteria with imaging). {1440 - lkw_minutes} minutes remaining!",
            "urgency": "HIGH"
        }
    else:
        return {
            "eligible": False,
            "message_vn": "❌ Ngoài khung giờ lấy huyết khối.",
            "message_en": "❌ Outside thrombectomy window.",
            "urgency": "LOW"
        }

