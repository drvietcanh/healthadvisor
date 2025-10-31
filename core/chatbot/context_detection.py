"""
Context Detection
Phát hiện ngữ cảnh từ câu hỏi
"""


def detect_context(message: str) -> str:
    """Phát hiện ngữ cảnh từ câu hỏi"""
    message_lower = message.lower()
    
    if any(word in message_lower for word in ["huyết áp", "cao huyết áp", "tăng huyết áp", "blood pressure"]):
        return "hypertension"
    elif any(word in message_lower for word in ["tiểu đường", "đường huyết", "insulin", "diabetes"]):
        return "diabetes"
    elif any(word in message_lower for word in ["đột quỵ", "stroke", "be-fast", "liệt"]):
        return "stroke"
    elif any(word in message_lower for word in ["ăn", "thức ăn", "món", "thực đơn", "dinh dưỡng"]):
        return "nutrition"
    elif any(word in message_lower for word in ["thuốc", "uống thuốc", "liều", "medication"]):
        return "medication"
    else:
        return "general"

