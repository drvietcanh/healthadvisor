"""
Emergency Page Custom CSS
CSS đặc biệt cho trang cấp cứu: nút to, font lớn, màu rõ ràng
"""

def get_emergency_css():
    """CSS cho trang cấp cứu - tối ưu cho người già"""
    return """
<style>
    /* Nút cấp cứu - TO VÀ RÕ */
    .emergency-button {
        padding: 30px !important;
        font-size: 32px !important;
        font-weight: bold !important;
        border-radius: 15px !important;
        margin: 10px 0 !important;
        text-align: center !important;
        cursor: pointer !important;
        border: 3px solid !important;
    }
    
    .btn-critical {
        background: linear-gradient(135deg, #ff0000 0%, #cc0000 100%) !important;
        color: white !important;
        border-color: #990000 !important;
        box-shadow: 0 8px 20px rgba(255,0,0,0.4) !important;
    }
    
    .btn-important {
        background: linear-gradient(135deg, #ff6b00 0%, #cc5500 100%) !important;
        color: white !important;
        border-color: #994400 !important;
    }
    
    .btn-info {
        background: linear-gradient(135deg, #0066ff 0%, #0052cc 100%) !important;
        color: white !important;
        border-color: #003d99 !important;
    }
    
    /* Font lớn cho người già */
    .big-text {
        font-size: 24px !important;
        line-height: 1.6 !important;
    }
    
    .huge-text {
        font-size: 36px !important;
        font-weight: bold !important;
    }
    
    /* Highlight quan trọng */
    .warning-box {
        background: #fff3cd;
        border-left: 5px solid #ff0000;
        padding: 20px;
        margin: 15px 0;
        border-radius: 5px;
        font-size: 20px !important;
    }
</style>
"""

