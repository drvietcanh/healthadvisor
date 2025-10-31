"""
Enhanced Chatbot - Hỗ trợ cả OpenAI và Gemini API

File này giữ lại để backward compatibility.
Code đã được tách thành các modules trong core/chatbot/
"""

from typing import List, Optional
from .chatbot import (
    get_welcome_message,
    get_suggested_questions,
    detect_context,
    get_quick_answers,
    get_template_response,
    get_ai_response
)


class MedicalChatbot:
    """Chatbot y tế thông minh với câu hỏi gợi ý"""
    
    def __init__(self):
        self.conversation = []
        
    def get_welcome_message(self) -> str:
        """Lời chào và giới thiệu"""
        return get_welcome_message()
    
    def get_suggested_questions(self, context: str = "general") -> List[str]:
        """Câu hỏi gợi ý theo ngữ cảnh"""
        return get_suggested_questions(context)
    
    def detect_context(self, message: str) -> str:
        """Phát hiện ngữ cảnh từ câu hỏi"""
        return detect_context(message)
    
    def get_quick_answers(self, question_type: str) -> str:
        """Câu trả lời nhanh cho câu hỏi phổ biến"""
        return get_quick_answers(question_type)
    
    def generate_response(
        self,
        user_message: str,
        use_ai: bool = True,
        provider: str = "gemini",
        api_key: Optional[str] = None
    ) -> tuple:
        """
        Tạo phản hồi cho câu hỏi
        
        Args:
            user_message: Câu hỏi của người dùng
            use_ai: Có dùng AI không
            provider: "gemini" hoặc "openai"
            api_key: API key (optional)
            
        Returns: (response_text, new_context, suggested_questions)
        """
        
        # Phát hiện ngữ cảnh
        context = self.detect_context(user_message)
        
        # Kiểm tra câu hỏi phổ biến
        user_lower = user_message.lower()
        
        quick_answer_map = {
            "huyết áp bình thường": ["huyết áp", "bình thường"],
            "dấu hiệu đột quỵ": ["dấu hiệu", "đột quỵ"],
            "đường cao": ["đường", "cao"],
            "ăn giảm huyết áp": ["ăn", "giảm", "huyết áp"],
            "gọi 115": ["gọi", "115", "cấp cứu"]
        }
        
        # Tìm câu trả lời nhanh
        for answer_key, keywords in quick_answer_map.items():
            if all(kw in user_lower for kw in keywords):
                response = self.get_quick_answers(answer_key)
                if response:
                    suggestions = self.get_suggested_questions(context)
                    return response, context, suggestions
        
        # Nếu không có câu trả lời nhanh, dùng AI hoặc template
        if use_ai:
            response = get_ai_response(user_message, context, provider=provider, api_key=api_key)
        else:
            response = get_template_response(user_message, context)
        
        suggestions = self.get_suggested_questions(context)
        return response, context, suggestions
    
    def _get_ai_response(self, message: str, context: str, provider: str = "gemini", api_key: Optional[str] = None) -> str:
        """Gọi AI (backward compatibility)"""
        return get_ai_response(message, context, provider=provider, api_key=api_key)
    
    def _get_template_response(self, message: str, context: str) -> str:
        """Trả lời mẫu (backward compatibility)"""
        return get_template_response(message, context)

