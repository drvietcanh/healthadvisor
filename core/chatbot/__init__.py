"""
Chatbot Module - Tổng hợp các components
"""

from .welcome_messages import get_welcome_message
from .suggested_questions import get_suggested_questions
from .context_detection import detect_context
from .quick_answers import get_quick_answers
from .template_responses import get_template_response
from .ai_providers import get_ai_response

__all__ = [
    'get_welcome_message',
    'get_suggested_questions',
    'detect_context',
    'get_quick_answers',
    'get_template_response',
    'get_ai_response'
]

