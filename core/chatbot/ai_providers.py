"""
AI Providers
Xử lý gọi AI (OpenAI và Gemini)
"""

import streamlit as st
import os
from typing import Optional

# Import AI libraries
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False


def get_ai_response(
    message: str,
    context: str,
    provider: str = "gemini",
    api_key: Optional[str] = None
) -> str:
    """
    Gọi AI (OpenAI hoặc Gemini) để trả lời
    
    Args:
        message: Câu hỏi của người dùng
        context: Ngữ cảnh (hypertension, diabetes, stroke, general)
        provider: "openai" hoặc "gemini"
        api_key: API key (nếu không có sẽ lấy từ env/secrets)
    """
    # System prompts theo context
    system_prompts = {
        "hypertension": "Bạn là chuyên gia tăng huyết áp. Giải thích đơn giản, dễ hiểu bằng tiếng Việt. Luôn nhắc gọi 115 nếu nguy hiểm.",
        "diabetes": "Bạn là chuyên gia tiểu đường. Giải thích về đường huyết bằng cả mmol/L và mg/dL. Ngôn ngữ dễ hiểu, tiếng Việt.",
        "stroke": "Bạn là chuyên gia đột quỵ. Nhấn mạnh BE-FAST và thời gian vàng. Luôn nhắc GỌI 115 NGAY. Trả lời bằng tiếng Việt.",
        "general": "Bạn là bác sĩ gia đình thân thiện. Giải thích y khoa bằng ngôn ngữ đời thường, dễ hiểu. An toàn là trên hết. Trả lời bằng tiếng Việt."
    }
    
    system_prompt = system_prompts.get(context, system_prompts["general"])
    system_prompt += "\n\nQUY TẮC: Không chẩn đoán, không kê đơn. Chỉ giáo dục và tư vấn chung. Trả lời ngắn gọn, dễ hiểu."
    
    # Thử Gemini trước (miễn phí!)
    if provider == "gemini":
        return _get_gemini_response(message, system_prompt, api_key)
    
    # Thử OpenAI
    elif provider == "openai":
        return _get_openai_response(message, system_prompt, api_key)
    
    else:
        return "❌ Provider không hợp lệ. Chọn 'gemini' hoặc 'openai'."


def _get_gemini_response(message: str, system_prompt: str, api_key: Optional[str]) -> str:
    """Gọi Gemini API"""
    try:
        if not GEMINI_AVAILABLE:
            raise ImportError("google-generativeai not installed")
        
        # Lấy API key từ parameter hoặc env/secrets
        gemini_key = api_key or os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY", "")
        
        if not gemini_key:
            return "⚠️ Chưa có Gemini API key. Vui lòng nhập API key ở sidebar!"
        
        genai.configure(api_key=gemini_key)
        model = genai.GenerativeModel('gemini-pro')
        
        # Kết hợp system prompt + user message
        full_prompt = f"{system_prompt}\n\nCâu hỏi: {message}"
        
        response = model.generate_content(full_prompt)
        return response.text
        
    except Exception as e:
        return f"❌ Lỗi Gemini: {str(e)}\n\nVui lòng kiểm tra API key hoặc chuyển sang OpenAI."


def _get_openai_response(message: str, system_prompt: str, api_key: Optional[str]) -> str:
    """Gọi OpenAI API"""
    try:
        if not OPENAI_AVAILABLE:
            raise ImportError("openai not installed")
        
        # Lấy API key
        openai_key = api_key or os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY", "")
        
        if not openai_key:
            return "⚠️ Chưa có OpenAI API key. Vui lòng nhập API key ở sidebar!"
        
        client = openai.OpenAI(api_key=openai_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"❌ Lỗi OpenAI: {str(e)}\n\nVui lòng kiểm tra API key."

