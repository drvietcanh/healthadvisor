"""
Daily Health Tips - Nutrition
Mẹo dinh dưỡng: Xương chắc khỏe và Giảm cholesterol
"""

import streamlit as st


def render_nutrition_bone_health():
    """Mẹo dinh dưỡng: Ăn gì để xương chắc khỏe"""
    st.subheader("🦴 Ăn gì để xương chắc khỏe?")
    
    st.markdown("""
    ### 💡 Tại sao xương cần chăm sóc?
    
    - **Loãng xương** rất phổ biến ở người già (>50 tuổi, đặc biệt phụ nữ)
    - Xương yếu → Dễ gãy, đau nhức
    - Cần bổ sung **Canxi + Vitamin D** từ thực phẩm
    
    ### 🥛 Thực phẩm giàu Canxi:
    
    **1. Sữa và sản phẩm sữa (Nguồn tốt nhất):**
    - 🥛 **Sữa tươi:** 300mg canxi/200ml (1 cốc)
    - 🧀 **Phô mai:** 200-300mg/30g
    - 🍦 **Sữa chua:** 150-200mg/100g
    - 💡 **Mẹo:** Uống 1-2 cốc sữa/ngày (nếu không dị ứng)
    
    **2. Cá và hải sản:**
    - 🐟 **Cá mòi (cả xương):** 400mg/100g → Xương cá mòi rất giàu canxi!
    - 🦐 **Tôm, cua:** 100-150mg/100g
    - 💡 **Mẹo:** Ăn cá nhỏ cả xương (cá mòi, cá cơm) → Nhiều canxi hơn
    
    **3. Rau xanh lá đậm:**
    - 🥬 **Cải xoăn, cải thìa:** 100-150mg/100g
    - 🥦 **Bông cải xanh:** 50-80mg/100g
    - 💡 **Mẹo:** Ăn 1-2 bát rau xanh/bữa → Bổ sung canxi tự nhiên
    
    **4. Đậu và hạt:**
    - 🫘 **Đậu phụ (Tofu):** 150-300mg/100g (tùy loại)
    - 🥜 **Hạnh nhân:** 200-250mg/100g
    - 🥜 **Vừng (mè):** 1000mg/100g → Rất nhiều canxi!
    - 💡 **Mẹo:** Rắc vừng lên cơm, salad → Tăng canxi dễ dàng
    
    **5. Ngũ cốc và thực phẩm tăng cường:**
    - 🥛 **Ngũ cốc tăng cường canxi:** 100-200mg/100g
    - 🥛 **Sữa đậu nành tăng cường:** 300mg/200ml
    - 💡 **Mẹo:** Chọn sản phẩm có ghi "Tăng cường canxi" trên nhãn
    
    ### ☀️ Vitamin D - Giúp hấp thu canxi:
    
    **Nguồn Vitamin D:**
    - ☀️ **Ánh nắng mặt trời:** Phơi nắng 15-20 phút/ngày (7-9h sáng, 4-5h chiều)
    - 🐟 **Cá béo:** Cá hồi, cá thu, cá trích (200-400 IU/100g)
    - 🥚 **Lòng đỏ trứng:** 40-50 IU/quả
    - 🥛 **Sữa tăng cường:** 100-150 IU/200ml
    
    ### 📊 Liều lượng khuyến nghị:
    
    - **Người lớn (19-50 tuổi):** 1000mg canxi/ngày
    - **Người già (>50 tuổi):** 1200mg canxi/ngày
    - **Vitamin D:** 800-1000 IU/ngày (người già)
    
    ### ✅ Mẹo thực hành:
    
    1. **Ăn đa dạng:** Kết hợp sữa, cá, rau xanh, đậu
    2. **Phơi nắng:** 15-20 phút/ngày (không qua kính)
    3. **Hạn chế:** Muối nhiều, rượu bia (gây mất canxi)
    4. **Tập thể dục:** Đi bộ, leo cầu thang → Xương chắc khỏe hơn
    """)
    
    st.info("""
    💡 **Mẹo nhớ:**
    
    - **1 cốc sữa** (200ml) = 300mg canxi → Gần đủ 1/4 nhu cầu
    - **Cá mòi cả xương** = Nhiều canxi nhất (ăn luôn xương)
    - **Vừng (mè)** = Siêu giàu canxi (rắc lên cơm, cháo)
    - **Phơi nắng** = Vitamin D tự nhiên, miễn phí!
    """)


def render_nutrition_cholesterol():
    """Mẹo dinh dưỡng: Chế độ ăn giảm cholesterol"""
    st.subheader("❤️ Chế độ ăn giảm Cholesterol")
    
    st.markdown("""
    ### 💡 Cholesterol là gì?
    
    - **Cholesterol tốt (HDL):** Bảo vệ tim mạch (cần tăng)
    - **Cholesterol xấu (LDL):** Gây xơ vữa động mạch (cần giảm)
    - **Mục tiêu:** LDL < 100mg/dL, HDL > 40mg/dL
    
    ### ✅ Thực phẩm GIẢM cholesterol xấu:
    
    **1. Yến mạch (Oatmeal):**
    - 🌾 **Beta-glucan:** Chất xơ hòa tan giúp giảm LDL
    - 💡 **Cách dùng:** 1 bát cháo yến mạch/bữa sáng
    - 📊 **Hiệu quả:** Giảm 5-10% LDL sau 1 tháng
    
    **2. Cá béo (2-3 lần/tuần):**
    - 🐟 **Cá hồi, cá thu, cá trích:** Giàu Omega-3
    - 💡 **Cách dùng:** 150-200g/lần, nướng hoặc hấp
    - 📊 **Hiệu quả:** Giảm LDL, tăng HDL
    
    **3. Đậu và hạt:**
    - 🫘 **Đậu nành, đậu đen:** Isoflavone giảm cholesterol
    - 🥜 **Hạnh nhân, óc chó:** Chất béo tốt, chất xơ
    - 💡 **Cách dùng:** 30-50g hạt/ngày (1 nắm nhỏ)
    
    **4. Rau xanh và trái cây:**
    - 🥬 **Rau cải, bông cải xanh:** Chất xơ hòa tan
    - 🍎 **Táo, lê, cam:** Pectin giảm hấp thu cholesterol
    - 💡 **Cách dùng:** 2-3 bát rau/bữa, 2-3 trái cây/ngày
    
    **5. Dầu thực vật tốt:**
    - 🫒 **Dầu oliu, dầu hạt cải:** Chất béo không bão hòa đơn
    - 🥑 **Quả bơ:** Chất béo tốt, chất xơ
    - 💡 **Cách dùng:** 1-2 thìa dầu oliu/ngày, không chiên rán
    
    ### 🚫 Thực phẩm TĂNG cholesterol (Cần tránh/hạn chế):
    
    **1. Thịt đỏ và mỡ động vật:**
    - ❌ **Thịt bò, thịt lợn mỡ:** Nhiều chất béo bão hòa
    - ✅ **Thay bằng:** Thịt trắng (gà, cá), bỏ da
    - 💡 **Mẹo:** Ăn thịt đỏ < 2 lần/tuần, chọn phần nạc
    
    **2. Thực phẩm chiên rán:**
    - ❌ **Khoai tây chiên, gà rán:** Chất béo trans
    - ✅ **Thay bằng:** Nướng, hấp, luộc
    - 💡 **Mẹo:** Tránh dầu mỡ đã chiên lại nhiều lần
    
    **3. Đồ ngọt và bánh kẹo:**
    - ❌ **Bánh quy, bánh ngọt:** Nhiều bơ, đường
    - ✅ **Thay bằng:** Trái cây tươi, hạt
    - 💡 **Mẹo:** Hạn chế đồ ngọt, < 1-2 lần/tuần
    
    **4. Sữa và sản phẩm sữa nhiều béo:**
    - ❌ **Sữa nguyên kem, phô mai nhiều béo**
    - ✅ **Thay bằng:** Sữa ít béo, sữa chua không đường
    - 💡 **Mẹo:** Chọn sữa < 2% béo
    
    ### 📊 Thực đơn mẫu (1 ngày):
    
    **🌅 Bữa sáng:**
    - Cháo yến mạch (1 bát) + 1 quả chuối
    - Hoặc: Bánh mì đen + trứng luộc + rau
    
    **🍽️ Bữa trưa:**
    - Cơm gạo lứt (1 bát) + Cá hấp (150g) + Rau luộc (2 bát) + Trái cây
    
    **🌙 Bữa tối:**
    - Cơm (1 bát) + Đậu phụ sốt cà chua + Canh rau + 1 quả táo
    
    **🍎 Bữa phụ:**
    - 1 nắm hạnh nhân (30g) hoặc 1 cốc sữa chua không đường
    
    ### ✅ Mẹo thực hành:
    
    1. **Ăn cá 2-3 lần/tuần** (thay thịt đỏ)
    2. **Cháo yến mạch sáng** (dễ làm, hiệu quả)
    3. **Rau xanh mỗi bữa** (2-3 bát/bữa)
    4. **Hạt mỗi ngày** (1 nắm nhỏ: hạnh nhân, óc chó)
    5. **Tránh chiên rán** → Nướng, hấp, luộc
    6. **Uống đủ nước** (2 lít/ngày)
    """)
    
    st.success("""
    💡 **Mẹo nhớ:**
    
    - **Cháo yến mạch** = Giảm cholesterol hiệu quả nhất
    - **Cá béo** = Omega-3 tốt cho tim
    - **Rau xanh** = Chất xơ giảm hấp thu cholesterol
    - **Hạt** = Chất béo tốt, 1 nắm/ngày
    - **Tránh:** Thịt đỏ nhiều, chiên rán, đồ ngọt
    """)
    
    st.warning("""
    ⚠️ **Lưu ý:**
    
    - Thay đổi chế độ ăn cần **kiên trì 2-3 tháng** mới thấy rõ hiệu quả
    - Kết hợp với **tập thể dục** (30 phút/ngày) → Tăng HDL
    - **Không hút thuốc** → Tăng HDL, giảm LDL
    - **Giảm cân** nếu thừa cân → Giảm cholesterol hiệu quả
    """)

