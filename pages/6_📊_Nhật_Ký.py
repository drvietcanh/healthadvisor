"""
Trang Nhật ký Sức khỏe - Theo dõi huyết áp, đường huyết, cân nặng
"""
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px
import sys
sys.path.append('..')

from core.ui_config import get_custom_css
from core.utils import classify_blood_pressure, convert_blood_sugar

st.set_page_config(page_title="Nhật ký Sức khỏe", page_icon="📊", layout="wide")

# Áp dụng Dark Mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
st.markdown(get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)

st.title("📊 Nhật ký Sức khỏe của Tôi")
st.markdown("### Theo dõi huyết áp, đường huyết, cân nặng hàng ngày")

# ==================== KHỞI TẠO DỮ LIỆU ====================
if 'health_data' not in st.session_state:
    st.session_state.health_data = pd.DataFrame(columns=[
        'Ngày giờ',
        'Thời điểm',
        'Huyết áp tâm thu',
        'Huyết áp tâm trương',
        'Mạch (nhịp/phút)',
        'Đường huyết (mmol/L)',
        'Đường huyết (mg/dL)',
        'HbA1c (%)',
        'Cholesterol toàn phần (mg/dL)',
        'LDL (mg/dL)',
        'HDL (mg/dL)',
        'Triglyceride (mg/dL)',
        'Acid Uric (mg/dL)',
        'Creatinine (mg/dL)',
        'eGFR (mL/min)',
        'Cân nặng (kg)',
        'Ghi chú'
    ])

# ==================== HƯỚNG DẪN ====================
with st.expander("📖 Hướng dẫn sử dụng - ĐỌC TRƯỚC KHI DÙNG!", expanded=False):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🆕 LẦN ĐẦU SỬ DỤNG:
        
        1. **Nhập dữ liệu** ở mục "➕ Thêm dữ liệu mới"
        2. **Xem biểu đồ** tự động hiện ra
        3. **Click nút 💾 TẢI XUỐNG** (quan trọng!)
        4. File sẽ tự lưu vào thư mục **Downloads**
        
        ⚠️ **QUAN TRỌNG:** Nhớ click "Tải xuống" để lưu dữ liệu!
        Nếu không, khi đóng trình duyệt sẽ **MẤT HẾT**!
        """)
    
    with col2:
        st.markdown("""
        ### 🔄 LẦN SAU SỬ DỤNG:
        
        1. **Click nút 📥 CHỌN FILE** ở mục "Tải lên dữ liệu cũ"
        2. Chọn file `nhat_ky_suc_khoe_*.csv` ở thư mục Downloads
        3. **Dữ liệu cũ tự động hiện ra!**
        4. Nhập thêm dữ liệu mới
        5. **Click 💾 TẢI XUỐNG** lại để cập nhật file
        
        💡 **Mẹo:** Lưu file vào Desktop để dễ tìm!
        """)

# ==================== HƯỚNG DẪN ĐO HUYẾT ÁP ĐÚNG CHUẨN ====================
with st.expander("🩺 Hướng dẫn ĐO HUYẾT ÁP ĐÚNG CHUẨN (WHO/AHA)", expanded=False):
    st.markdown("""
    ## 🩺 CÁCH ĐO HUYẾT ÁP CHÍNH XÁC
    
    ### 📋 CHUẨN BỊ TRƯỚC KHI ĐO (30 phút trước):
    
    ❌ **TRÁNH:**
    - Uống cà phê, trà, thuốc lá
    - Ăn no
    - Vận động mạnh
    - Căng thẳng, lo lắng
    - Nín đi tiểu (nên đi vệ sinh trước khi đo)
    
    ✅ **NÊN:**
    - Ngồi nghỉ yên 5-10 phút
    - Thư giãn, hít thở đều
    - Trong phòng ấm áp, yên tĩnh
    
    ---
    
    ### 🪑 TƯ THẾ ĐO ĐÚNG:
    
    ```
    👤 Ngồi thẳng lưng, dựa vào ghế
    💪 Cánh tay đo đặt trên bàn (ngang tim)
    🦵 Hai chân đặt phẳng sàn, không gác chân
    ✋ Lòng bàn tay ngửa lên
    🤐 Không nói chuyện khi đang đo
    ```
    
    **HÌNH ẢNH:**
    ```
         👤 Đầu thẳng
         |
    💪---+---💪  Tay trên bàn (ngang tim)
         |
        🪑 Ngồi thẳng
         |
    🦵   |   🦵  Chân phẳng sàn
    ```
    
    ---
    
    ### 📏 QUẤN BĂNG ĐO:
    
    1. **Vị trí:** Quấn quanh cánh tay trái (nếu thuận tay phải)
    2. **Độ cao:** Cách khuỷu tay 2-3 cm
    3. **Độ chặt:** Lọt 2 ngón tay vào giữa băng và da
    4. **Ống nghe:** Đặt đúng vị trí động mạch (bên trong khuỷu tay)
    
    ⚠️ **LƯU Ý:**
    - Cởi áo dài tay (không đo qua áo)
    - Không quấn quá chặt hoặc quá lỏng
    - Băng phải ngang mức tim
    
    ---
    
    ### 🔢 ĐO THẾ NÀO:
    
    **Máy điện tử (Tự động):**
    1. Bật máy
    2. Quấn băng đúng vị trí
    3. Ngồi yên, không cử động
    4. Nhấn nút Start
    5. Chờ máy đo xong (1-2 phút)
    6. Ghi lại kết quả
    
    **Máy thủy ngân (Cần người đo):**
    1. Quấn băng
    2. Bơm căng băng đến 180-200 mmHg
    3. Từ từ xả khí, nghe động mạch
    4. Tiếng đầu tiên = Tâm thu
    5. Tiếng cuối cùng = Tâm trương
    
    ---
    
    ### 🔁 ĐO BAO NHIÊU LẦN:
    
    ✅ **ĐÚNG CHUẨN:**
    - Đo **2-3 lần** (cách nhau 1-2 phút)
    - Lấy kết quả **TRUNG BÌNH** của 2-3 lần
    - Nếu chênh lệch > 10 mmHg → Đo lại
    
    ✅ **THỜI ĐIỂM ĐO:**
    - **Sáng:** Sau khi thức dậy, trước khi uống thuốc/ăn sáng
    - **Tối:** Trước khi đi ngủ
    - Đo **cùng giờ** mỗi ngày
    
    ---
    
    ### 📊 GHI CHÉP KẾT QUẢ:
    
    ✅ **Ghi rõ:**
    - Ngày giờ đo
    - Kết quả (ví dụ: 130/85)
    - Mạch (nếu máy có)
    - Thời điểm (sáng/tối, trước/sau ăn)
    - Cảm giác (đau đầu, chóng mặt...)
    
    → **Nhập vào app này để theo dõi xu hướng!**
    
    ---
    
    ### ⚠️ SAI LẦM THƯỜNG GẶP:
    
    | Sai lầm | Hậu quả | Cách khắc phục |
    |---------|---------|----------------|
    | Quấn băng qua áo | Kết quả cao hơn | Cởi áo |
    | Tay thòng xuống | Kết quả cao hơn | Đặt tay lên bàn |
    | Nói chuyện khi đo | Kết quả cao hơn | Im lặng |
    | Gác chân lên chân | Kết quả cao hơn | 2 chân phẳng sàn |
    | Đo 1 lần | Không chính xác | Đo 2-3 lần |
    | Băng quá chặt/lỏng | Sai số lớn | Lọt 2 ngón tay |
    
    ---
    
    ### 🚨 KHI NÀO CẦN GỌI BÁC SĨ:
    
    🚨 **NGAY LẬP TỨC - GỌI 115 (CẤP CỨU):**
    - Huyết áp ≥ 180/120 + đau đầu dữ dội
    - Huyết áp ≥ 180/120 + đau ngực
    - Huyết áp ≥ 180/120 + khó thở
    - Huyết áp ≥ 180/120 + mờ mắt
    - Huyết áp ≥ 180/120 + buồn nôn/nôn
    - Huyết áp ≥ 180/120 + tê tay chân
    
    📞 **HẸN GẶP BÁC SĨ (trong vài ngày):**
    - Huyết áp ≥ 140/90 liên tục 3-5 ngày
    - Dao động nhiều (100/60 → 160/100)
    - Có triệu chứng: chóng mặt, đau đầu, mệt...
    
    ---
    
    ### 📚 NGUỒN THAM KHẢO:
    - American Heart Association (AHA)
    - World Health Organization (WHO)
    - European Society of Hypertension (ESH)
    """)

# ==================== HƯỚNG DẪN CHI TIẾT LƯU/TẢI FILE ====================
with st.expander("💾 Hướng dẫn LƯU/TẢI FILE CSV - TỪNG BƯỚC CHI TIẾT", expanded=False):
    st.markdown("""
    ## 💾 HƯỚNG DẪN LƯU VÀ TẢI FILE CSV
    
    ### 📥 PHẦN 1: LẦN ĐẦU SỬ DỤNG - LƯU FILE
    
    #### Bước 1: Nhập dữ liệu
    ✅ Kéo xuống mục **"➕ Bước 2: Thêm dữ liệu mới"**  
    ✅ Nhập huyết áp, đường huyết, v.v.  
    ✅ Click nút **"💾 LƯU VÀO NHẬT KÝ"**
    
    #### Bước 2: Tải xuống file
    ✅ Kéo xuống mục **"💾 Bước 4: LƯU DỮ LIỆU VÀO MÁY"**  
    ✅ Click nút to màu xanh **"📥 TẢI XUỐNG FILE CSV"**  
    ✅ File tự động lưu vào thư mục **Downloads**
    
    #### Bước 3: Tìm file đã tải (QUAN TRỌNG!)
    
    **Trên Windows:**
    ```
    1. Mở File Explorer (Biểu tượng thư mục trên taskbar)
    2. Click vào "Downloads" bên trái
    3. Tìm file tên "nhat_ky_suc_khoe_30102025_1430.csv"
    4. (Tùy chọn) Kéo file ra Desktop để dễ tìm
    ```
    
    **Trên Mac:**
    ```
    1. Mở Finder
    2. Click "Downloads" bên trái
    3. Tìm file "nhat_ky_suc_khoe_*.csv"
    4. (Tùy chọn) Kéo ra Desktop
    ```
    
    **Trên điện thoại (Android):**
    ```
    1. Mở app "Files" hoặc "My Files"
    2. Vào thư mục "Downloads"
    3. Tìm file CSV
    ```
    
    **Trên iPhone/iPad:**
    ```
    1. Mở app "Files" (Tệp tin)
    2. Vào "On My iPhone" → "Downloads"
    3. Tìm file CSV
    ```
    
    ---
    
    ### 📤 PHẦN 2: LẦN SAU - TẢI FILE LÊN
    
    #### Bước 1: Mở app lại
    ✅ Mở trình duyệt  
    ✅ Vào lại trang Nhật ký Sức khỏe này
    
    #### Bước 2: Tải file lên
    ✅ Tìm mục **"📥 Bước 1: Tải lên dữ liệu cũ"**  
    ✅ Click nút **"Browse files"** (hoặc "Chọn file")
    
    **Windows sẽ mở cửa sổ chọn file:**
    ```
    1. Cửa sổ tự động mở thư mục "Downloads"
    2. Tìm file "nhat_ky_suc_khoe_*.csv"
    3. Click chọn file
    4. Click nút "Open" (Mở)
    ```
    
    ✅ **Ngay lập tức:** Dữ liệu cũ hiện ra!  
    ✅ **Thấy biểu đồ** của tất cả ngày trước!
    
    #### Bước 3: Thêm dữ liệu mới
    ✅ Nhập thêm dữ liệu hôm nay  
    ✅ Kéo xuống click **"TẢI XUỐNG"** lại để cập nhật file
    
    ---
    
    ### 💡 MẸO QUAN TRỌNG:
    
    #### 🎯 Để không bao giờ mất dữ liệu:
    
    **Mẹo 1: Đặt tên file dễ nhớ**
    ```
    Sau khi tải xuống, đổi tên file thành:
    "nhat_ky_BA_NGUYEN.csv"
    hoặc
    "huyet_ap_cua_toi.csv"
    ```
    
    **Mẹo 2: Lưu ở Desktop (Màn hình chính)**
    ```
    1. Mở Downloads
    2. Kéo file ra Desktop
    3. Lần sau dễ tìm hơn!
    ```
    
    **Mẹo 3: Gửi Email cho chính bạn**
    ```
    1. Mở Gmail/Outlook
    2. Soạn email gửi cho chính bạn
    3. Đính kèm file CSV
    4. Gửi!
    → Lưu trên cloud, không bao giờ mất!
    ```
    
    **Mẹo 4: Sao lưu vào USB**
    ```
    1. Cắm USB vào máy
    2. Copy file CSV vào USB
    3. Rút USB cất cẩn thận
    ```
    
    **Mẹo 5: Lưu vào Google Drive/OneDrive**
    ```
    1. Mở Google Drive (drive.google.com)
    2. Click "Upload" (Tải lên)
    3. Chọn file CSV
    → Truy cập từ mọi thiết bị!
    ```
    
    ---
    
    ### 🔄 CÁCH SỬ DỤNG NHIỀU THIẾT BỊ:
    
    **Ví dụ: Nhập ở điện thoại, xem ở máy tính**
    
    1. **Ở điện thoại:**
       - Nhập dữ liệu
       - Tải xuống file CSV
       - Gửi file qua Email cho chính bạn
    
    2. **Ở máy tính:**
       - Mở Email
       - Tải file CSV về
       - Mở app này, tải file lên
       - Thấy ngay dữ liệu từ điện thoại!
    
    ---
    
    ### ❓ TROUBLESHOOTING (Gặp vấn đề):
    
    **Vấn đề 1: Không tìm thấy file đã tải**
    ```
    Giải pháp:
    - Mở File Explorer
    - Gõ "nhat_ky" vào ô tìm kiếm
    - Windows sẽ tìm file cho bạn
    ```
    
    **Vấn đề 2: Tải file lên bị lỗi**
    ```
    Giải pháp:
    - Kiểm tra file có đuôi .csv không
    - Không được mở file bằng Excel rồi sửa
    - Tải file gốc từ app này
    ```
    
    **Vấn đề 3: Dữ liệu bị mất sau khi đóng trình duyệt**
    ```
    Nguyên nhân: Quên click "Tải xuống"
    Giải pháp: Luôn click "Tải xuống" sau khi nhập xong!
    ```
    
    ---
    
    ### 📞 CẦN GIÚP ĐỠ?
    
    - Hỏi con cháu giúp lần đầu
    - Xem lại hướng dẫn này
    - Hỏi AI Bác Sĩ: "Hướng dẫn tôi lưu file"
    """)

st.divider()

# ==================== TẢI LÊN DỮ LIỆU CŨ ====================
st.subheader("📥 Bước 1: Tải lên dữ liệu cũ (nếu có)")

col1, col2 = st.columns([3, 1])

with col1:
    uploaded_file = st.file_uploader(
        "👉 Click đây để chọn file CSV đã lưu trước đó",
        type=['csv'],
        help="Chọn file 'nhat_ky_suc_khoe_*.csv' ở thư mục Downloads của bạn",
        label_visibility="visible"
    )

with col2:
    if uploaded_file is not None:
        st.success(f"✅ Đã chọn file:\n`{uploaded_file.name}`")

if uploaded_file is not None:
    try:
        # Đọc file CSV
        df = pd.read_csv(uploaded_file)
        
        # Kiểm tra format
        required_columns = ['Ngày giờ', 'Huyết áp tâm thu', 'Huyết áp tâm trương']
        if all(col in df.columns for col in required_columns):
            st.session_state.health_data = df
            st.success(f"🎉 **Đã tải thành công {len(df)} bản ghi!**")
            st.balloons()
        else:
            st.error("❌ File không đúng định dạng! Vui lòng chọn file đúng.")
    except Exception as e:
        st.error(f"❌ Lỗi khi đọc file: {str(e)}")
else:
    st.info("💡 **Lần đầu sử dụng?** Bỏ qua bước này, xuống dưới nhập dữ liệu mới!")

st.divider()

# ==================== NHẬP DỮ LIỆU MỚI ====================
st.subheader("➕ Bước 2: Thêm dữ liệu mới")

with st.form("add_health_data", clear_on_submit=True):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📅 Thời gian")
        measurement_date = st.date_input(
            "Ngày đo",
            value=datetime.now(),
            help="Chọn ngày đo"
        )
        measurement_time = st.time_input(
            "Giờ đo",
            value=datetime.now().time(),
            help="Chọn giờ đo"
        )
    
    with col2:
        st.markdown("#### ⏰ Thời điểm")
        time_of_day = st.radio(
            "Đo vào lúc:",
            ["🌅 Sáng (đói)", "🌞 Trưa (sau ăn 2h)", "🌙 Tối (trước ngủ)", "🍽️ Sau ăn"],
            horizontal=False
        )
    
    st.divider()
    
    # Huyết áp
    st.markdown("#### ❤️ Huyết áp")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        systolic = st.number_input(
            "Tâm thu (mmHg)",
            min_value=70,
            max_value=250,
            value=120,
            step=1,
            help="Số lớn (trên)"
        )
    
    with col2:
        diastolic = st.number_input(
            "Tâm trương (mmHg)",
            min_value=40,
            max_value=150,
            value=80,
            step=1,
            help="Số nhỏ (dưới)"
        )
    
    with col3:
        pulse = st.number_input(
            "Mạch (nhịp/phút)",
            min_value=40,
            max_value=200,
            value=75,
            step=1,
            help="Nhịp tim (nhiều máy đo HA có kèm mạch)"
        )
    
    # Đánh giá huyết áp
    if systolic and diastolic:
        bp_category = classify_blood_pressure(systolic, diastolic)
        if "Bình thường" in bp_category:
            st.success(f"✅ {bp_category}")
        elif "Cao" in bp_category or "Nguy hiểm" in bp_category:
            st.error(f"⚠️ {bp_category}")
        else:
            st.warning(f"⚠️ {bp_category}")
    
    # Đánh giá mạch
    if pulse:
        if pulse < 60:
            st.warning(f"⚠️ Mạch chậm ({pulse} < 60)")
        elif pulse > 100:
            st.warning(f"⚠️ Mạch nhanh ({pulse} > 100)")
        else:
            st.success(f"✅ Mạch bình thường (60-100)")
    
    st.divider()
    
    # Đường huyết
    st.markdown("#### 🩸 Đường huyết")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        glucose_unit = st.radio(
            "Đơn vị:",
            ["mmol/L", "mg/dL"],
            horizontal=True
        )
    
    with col2:
        if glucose_unit == "mmol/L":
            glucose_mmol = st.number_input(
                "Đường huyết (mmol/L)",
                min_value=2.0,
                max_value=30.0,
                value=5.5,
                step=0.1
            )
            glucose_mgdl = round(glucose_mmol * 18)
        else:
            glucose_mgdl = st.number_input(
                "Đường huyết (mg/dL)",
                min_value=36,
                max_value=540,
                value=100,
                step=1
            )
            glucose_mmol = round(glucose_mgdl / 18, 1)
    
    with col3:
        st.info(f"📊 **Quy đổi:**\n\n{glucose_mmol} mmol/L\n\n= {glucose_mgdl} mg/dL")
    
    st.divider()
    
    # Cân nặng
    st.markdown("#### ⚖️ Cân nặng (tùy chọn)")
    col1, col2 = st.columns(2)
    
    with col1:
        weight = st.number_input(
            "Cân nặng (kg)",
            min_value=30.0,
            max_value=200.0,
            value=None,
            step=0.1,
            help="Để trống nếu không đo"
        )
    
    with col2:
        st.caption("💡 Cân nặng giúp theo dõi hiệu quả điều trị")
    
    st.divider()
    
    # XÉT NGHIỆM (Tùy chọn - chỉ nhập khi có kết quả)
    st.markdown("#### 🧪 Xét nghiệm (Tùy chọn - Chỉ nhập khi có kết quả)")
    st.info("💡 **Lưu ý:** Các chỉ số bên dưới chỉ nhập khi bạn có kết quả xét nghiệm. Để trống nếu không có!")
    
    # HbA1c
    with st.expander("🩸 HbA1c (Đường huyết trung bình 3 tháng)", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            hba1c = st.number_input(
                "HbA1c (%)",
                min_value=4.0,
                max_value=15.0,
                value=None,
                step=0.1,
                help="Chỉ số HbA1c từ kết quả xét nghiệm máu"
            )
        with col2:
            if hba1c:
                if hba1c < 5.7:
                    st.success(f"✅ Bình thường (< 5.7%)")
                elif hba1c < 6.5:
                    st.warning(f"⚠️ Tiền tiểu đường (5.7-6.4%)")
                else:
                    st.error(f"❌ Tiểu đường (≥ 6.5%)")
            else:
                st.caption("📊 Bình thường: < 5.7%\nTiền TĐ: 5.7-6.4%\nTiểu đường: ≥ 6.5%")
    
    # Mỡ máu
    with st.expander("💊 Mỡ máu (Lipid panel)", expanded=False):
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            cholesterol = st.number_input(
                "Cholesterol toàn phần (mg/dL)",
                min_value=100,
                max_value=400,
                value=None,
                step=1,
                help="Total Cholesterol"
            )
        
        with col2:
            ldl = st.number_input(
                "LDL - Xấu (mg/dL)",
                min_value=50,
                max_value=300,
                value=None,
                step=1,
                help="LDL Cholesterol - Mỡ xấu"
            )
        
        with col3:
            hdl = st.number_input(
                "HDL - Tốt (mg/dL)",
                min_value=20,
                max_value=100,
                value=None,
                step=1,
                help="HDL Cholesterol - Mỡ tốt"
            )
        
        with col4:
            triglyceride = st.number_input(
                "Triglyceride (mg/dL)",
                min_value=50,
                max_value=500,
                value=None,
                step=1,
                help="Chất béo trung tính"
            )
        
        # Đánh giá mỡ máu
        if cholesterol or ldl or hdl or triglyceride:
            st.markdown("**📊 Đánh giá:**")
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                if cholesterol:
                    if cholesterol < 200:
                        st.success("✅ TC: Tốt")
                    elif cholesterol < 240:
                        st.warning("⚠️ TC: Cao biên")
                    else:
                        st.error("❌ TC: Cao")
            
            with col2:
                if ldl:
                    if ldl < 100:
                        st.success("✅ LDL: Tối ưu")
                    elif ldl < 130:
                        st.info("ℹ️ LDL: Gần tối ưu")
                    elif ldl < 160:
                        st.warning("⚠️ LDL: Cao biên")
                    else:
                        st.error("❌ LDL: Cao")
            
            with col3:
                if hdl:
                    if hdl >= 60:
                        st.success("✅ HDL: Tốt")
                    elif hdl >= 40:
                        st.info("ℹ️ HDL: Chấp nhận")
                    else:
                        st.error("❌ HDL: Thấp")
            
            with col4:
                if triglyceride:
                    if triglyceride < 150:
                        st.success("✅ TG: Bình thường")
                    elif triglyceride < 200:
                        st.warning("⚠️ TG: Cao biên")
                    else:
                        st.error("❌ TG: Cao")
    
    # Acid Uric & Chức năng thận
    with st.expander("🔬 Acid Uric & Chức năng thận", expanded=False):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            uric_acid = st.number_input(
                "Acid Uric (mg/dL)",
                min_value=2.0,
                max_value=15.0,
                value=None,
                step=0.1,
                help="Acid uric (liên quan gút)"
            )
            if uric_acid:
                if uric_acid <= 7.0:
                    st.success("✅ Bình thường (≤ 7.0)")
                else:
                    st.error(f"❌ Cao (> 7.0) - Nguy cơ gút!")
        
        with col2:
            creatinine = st.number_input(
                "Creatinine (mg/dL)",
                min_value=0.5,
                max_value=10.0,
                value=None,
                step=0.1,
                help="Creatinine máu - đánh giá thận"
            )
            if creatinine:
                if creatinine <= 1.2:
                    st.success("✅ Bình thường (0.6-1.2)")
                else:
                    st.warning(f"⚠️ Cao (> 1.2) - Kiểm tra thận!")
        
        with col3:
            egfr = st.number_input(
                "eGFR (mL/min/1.73m²)",
                min_value=5,
                max_value=150,
                value=None,
                step=1,
                help="Tốc độ lọc cầu thận ước tính"
            )
            if egfr:
                if egfr >= 90:
                    st.success("✅ Bình thường (≥ 90)")
                elif egfr >= 60:
                    st.info("ℹ️ Giảm nhẹ (60-89)")
                elif egfr >= 30:
                    st.warning("⚠️ Giảm vừa (30-59)")
                else:
                    st.error("❌ Giảm nặng (< 30)")
    
    st.divider()
    
    # Ghi chú
    st.markdown("#### 📝 Ghi chú (tùy chọn)")
    notes = st.text_area(
        "Ghi chú",
        placeholder="Ví dụ: Đau đầu nhẹ, uống thuốc lúc 7h sáng, ăn cơm nhiều...",
        help="Ghi lại cảm giác, triệu chứng, thuốc đã uống...",
        label_visibility="collapsed"
    )
    
    # Nút lưu
    submitted = st.form_submit_button(
        "💾 LƯU VÀO NHẬT KÝ",
        use_container_width=True,
        type="primary"
    )
    
    if submitted:
        # Tạo timestamp
        timestamp = datetime.combine(measurement_date, measurement_time)
        
        # Tạo dòng mới
        new_row = {
            'Ngày giờ': timestamp.strftime("%d/%m/%Y %H:%M"),
            'Thời điểm': time_of_day,
            'Huyết áp tâm thu': systolic,
            'Huyết áp tâm trương': diastolic,
            'Đường huyết (mmol/L)': glucose_mmol,
            'Đường huyết (mg/dL)': glucose_mgdl,
            'Cân nặng (kg)': weight if weight > 0 else None,
            'Ghi chú': notes
        }
        
        # Thêm vào DataFrame
        st.session_state.health_data = pd.concat([
            st.session_state.health_data,
            pd.DataFrame([new_row])
        ], ignore_index=True)
        
        # Sắp xếp theo thời gian mới nhất
        st.session_state.health_data = st.session_state.health_data.sort_values(
            'Ngày giờ', 
            ascending=False
        ).reset_index(drop=True)
        
        st.success("✅ **Đã lưu thành công!** Kéo xuống xem dữ liệu và biểu đồ bên dưới.")
        st.balloons()

st.divider()

# ==================== HIỂN THỊ DỮ LIỆU ====================
if len(st.session_state.health_data) > 0:
    st.subheader("📋 Bước 3: Xem dữ liệu của bạn")
    
    # Tabs
    tab1, tab2, tab3 = st.tabs(["📊 Biểu đồ", "📋 Bảng dữ liệu", "📈 Thống kê"])
    
    # ===== TAB 1: BIỂU ĐỒ =====
    with tab1:
        st.markdown("#### 📈 Xu hướng theo thời gian")
        
        # Chuẩn bị dữ liệu cho biểu đồ
        df_plot = st.session_state.health_data.copy()
        
        # Chọn loại biểu đồ
        chart_type = st.selectbox(
            "Chọn chỉ số muốn xem:",
            ["❤️ Huyết áp", "🩸 Đường huyết", "⚖️ Cân nặng", "📊 Tất cả"]
        )
        
        if chart_type == "❤️ Huyết áp":
            # Biểu đồ huyết áp
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(
                x=df_plot['Ngày giờ'],
                y=df_plot['Huyết áp tâm thu'],
                mode='lines+markers',
                name='Tâm thu',
                line=dict(color='red', width=2),
                marker=dict(size=8)
            ))
            
            fig.add_trace(go.Scatter(
                x=df_plot['Ngày giờ'],
                y=df_plot['Huyết áp tâm trương'],
                mode='lines+markers',
                name='Tâm trương',
                line=dict(color='blue', width=2),
                marker=dict(size=8)
            ))
            
            # Thêm ngưỡng an toàn
            fig.add_hline(y=140, line_dash="dash", line_color="orange", 
                         annotation_text="Ngưỡng cao (140)")
            fig.add_hline(y=90, line_dash="dash", line_color="orange",
                         annotation_text="Ngưỡng cao (90)")
            
            fig.update_layout(
                title="Biểu đồ Huyết áp",
                xaxis_title="Thời gian",
                yaxis_title="Huyết áp (mmHg)",
                height=500,
                hovermode='x unified'
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        elif chart_type == "🩸 Đường huyết":
            # Biểu đồ đường huyết
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(
                x=df_plot['Ngày giờ'],
                y=df_plot['Đường huyết (mmol/L)'],
                mode='lines+markers',
                name='Đường huyết',
                line=dict(color='green', width=2),
                marker=dict(size=8)
            ))
            
            # Ngưỡng bình thường
            fig.add_hrect(y0=3.9, y1=6.1, line_width=0, fillcolor="green", opacity=0.1,
                         annotation_text="Bình thường (3.9-6.1)", annotation_position="top left")
            fig.add_hrect(y0=6.1, y1=7.0, line_width=0, fillcolor="yellow", opacity=0.1,
                         annotation_text="Tiền tiểu đường (6.1-7.0)", annotation_position="top left")
            fig.add_hline(y=7.0, line_dash="dash", line_color="red",
                         annotation_text="Tiểu đường (>7.0)")
            
            fig.update_layout(
                title="Biểu đồ Đường huyết",
                xaxis_title="Thời gian",
                yaxis_title="Đường huyết (mmol/L)",
                height=500,
                hovermode='x unified'
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        elif chart_type == "⚖️ Cân nặng":
            # Biểu đồ cân nặng
            if 'Cân nặng (kg)' in df_plot.columns:
                df_weight = df_plot[df_plot['Cân nặng (kg)'].notna()]
                
                if len(df_weight) > 0:
                    fig = go.Figure()
                    
                    fig.add_trace(go.Scatter(
                        x=df_weight['Ngày giờ'],
                        y=df_weight['Cân nặng (kg)'],
                        mode='lines+markers',
                        name='Cân nặng',
                        line=dict(color='purple', width=2),
                        marker=dict(size=8)
                    ))
                    
                    fig.update_layout(
                        title="Biểu đồ Cân nặng",
                        xaxis_title="Thời gian",
                        yaxis_title="Cân nặng (kg)",
                        height=500,
                        hovermode='x unified'
                    )
                    
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.info("📊 Chưa có dữ liệu cân nặng. Hãy nhập cân nặng khi thêm dữ liệu!")
            else:
                st.info("📊 Chưa có dữ liệu cân nặng.")
        
        else:  # Tất cả
            st.info("📊 Hiển thị tất cả biểu đồ - Kéo xuống để xem!")
            
            # 3 biểu đồ nhỏ
            col1, col2 = st.columns(2)
            
            with col1:
                # Huyết áp
                fig1 = go.Figure()
                fig1.add_trace(go.Scatter(x=df_plot['Ngày giờ'], y=df_plot['Huyết áp tâm thu'],
                                         mode='lines+markers', name='Tâm thu', line=dict(color='red')))
                fig1.add_trace(go.Scatter(x=df_plot['Ngày giờ'], y=df_plot['Huyết áp tâm trương'],
                                         mode='lines+markers', name='Tâm trương', line=dict(color='blue')))
                fig1.update_layout(title="Huyết áp", height=300)
                st.plotly_chart(fig1, use_container_width=True)
            
            with col2:
                # Đường huyết
                fig2 = go.Figure()
                fig2.add_trace(go.Scatter(x=df_plot['Ngày giờ'], y=df_plot['Đường huyết (mmol/L)'],
                                         mode='lines+markers', name='Đường huyết', line=dict(color='green')))
                fig2.update_layout(title="Đường huyết", height=300)
                st.plotly_chart(fig2, use_container_width=True)
    
    # ===== TAB 2: BẢNG DỮ LIỆU =====
    with tab2:
        st.markdown("#### 📋 Tất cả bản ghi")
        
        # Hiển thị bảng
        st.dataframe(
            st.session_state.health_data,
            use_container_width=True,
            height=400
        )
        
        st.info(f"📊 **Tổng cộng:** {len(st.session_state.health_data)} bản ghi")
    
    # ===== TAB 3: THỐNG KÊ =====
    with tab3:
        st.markdown("#### 📈 Thống kê tổng quan")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "📅 Số ngày theo dõi",
                len(st.session_state.health_data)
            )
            
            st.metric(
                "❤️ Huyết áp TB (Tâm thu)",
                f"{st.session_state.health_data['Huyết áp tâm thu'].mean():.0f} mmHg"
            )
        
        with col2:
            st.metric(
                "❤️ Huyết áp TB (Tâm trương)",
                f"{st.session_state.health_data['Huyết áp tâm trương'].mean():.0f} mmHg"
            )
            
            st.metric(
                "🩸 Đường huyết TB",
                f"{st.session_state.health_data['Đường huyết (mmol/L)'].mean():.1f} mmol/L"
            )
        
        with col3:
            if 'Cân nặng (kg)' in st.session_state.health_data.columns:
                weight_data = st.session_state.health_data['Cân nặng (kg)'].dropna()
                if len(weight_data) > 0:
                    st.metric(
                        "⚖️ Cân nặng TB",
                        f"{weight_data.mean():.1f} kg"
                    )
                    
                    if len(weight_data) > 1:
                        weight_change = weight_data.iloc[-1] - weight_data.iloc[0]
                        st.metric(
                            "📊 Thay đổi cân nặng",
                            f"{weight_change:+.1f} kg",
                            delta=f"{weight_change:+.1f} kg"
                        )
else:
    st.info("📊 **Chưa có dữ liệu.** Hãy thêm dữ liệu mới ở trên! ⬆️")

st.divider()

# ==================== TẢI XUỐNG ====================
st.subheader("💾 Bước 4: LƯU DỮ LIỆU VÀO MÁY (QUAN TRỌNG!)")

col1, col2 = st.columns([3, 1])

with col1:
    if len(st.session_state.health_data) > 0:
        # Tạo CSV
        csv = st.session_state.health_data.to_csv(index=False, encoding='utf-8-sig')
        
        # Nút download
        st.download_button(
            label="📥 TẢI XUỐNG FILE CSV (Click đây để lưu!)",
            data=csv,
            file_name=f"nhat_ky_suc_khoe_{datetime.now().strftime('%d%m%Y_%H%M')}.csv",
            mime="text/csv",
            use_container_width=True,
            type="primary",
            help="File sẽ tự động lưu vào thư mục Downloads"
        )
        
        st.success("✅ Click nút trên → File tự động lưu vào **Downloads**")
    else:
        st.warning("⚠️ Chưa có dữ liệu để tải xuống. Hãy thêm dữ liệu trước!")

with col2:
    st.info(f"📊 **Đã có:**\n\n{len(st.session_state.health_data)} bản ghi")

st.warning("""
⚠️ **QUAN TRỌNG:**

1. **MỖI LẦN** thêm dữ liệu mới, nhớ click **"TẢI XUỐNG"** để cập nhật file!
2. File sẽ lưu vào thư mục **Downloads** của bạn
3. **Lần sau** mở app, click **"Chọn file"** ở Bước 1 để tải lại dữ liệu
4. Nếu **không tải xuống**, dữ liệu sẽ **MẤT** khi đóng trình duyệt!
""")

st.divider()

# ==================== MẸO SỬ DỤNG ====================
st.subheader("💡 Mẹo sử dụng hiệu quả")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### ✅ NÊN LÀM:
    
    - ✅ Đo **cùng giờ** mỗi ngày (sáng sau khi thức dậy)
    - ✅ Đo **trước khi** uống thuốc, ăn sáng
    - ✅ **Nghỉ ngơi 5 phút** trước khi đo
    - ✅ Ngồi yên, không nói chuyện khi đo
    - ✅ Click **"Tải xuống"** mỗi lần nhập xong
    - ✅ Sao lưu file CSV vào **USB** hoặc **Email**
    - ✅ Đem file cho **bác sĩ** xem khi khám
    """)

with col2:
    st.markdown("""
    ### ❌ TRÁNH:
    
    - ❌ Đo ngay sau khi ăn/uống cà phê
    - ❌ Đo khi đang căng thẳng/vừa vận động
    - ❌ Quên click "Tải xuống" (sẽ mất dữ liệu!)
    - ❌ Nhập sai đơn vị (mmol/L vs mg/dL)
    - ❌ Xóa file CSV (sẽ mất hết!)
    - ❌ Lo lắng nếu 1-2 lần cao (quan trọng là **xu hướng**)
    """)

st.divider()

# Footer
st.markdown("""
<div style='text-align: center; color: gray; margin-top: 2rem;'>
    <p>💡 <b>Mẹo:</b> Lưu file CSV vào <b>Desktop</b> hoặc gửi Email cho chính bạn để không bao giờ mất!</p>
    <p>📧 Có thắc mắc? Hỏi <b>🤖 AI Bác Sĩ</b>!</p>
</div>
""", unsafe_allow_html=True)

