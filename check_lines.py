import os
from pathlib import Path

# Tìm tất cả file .py
files_info = []
for root, dirs, files in os.walk('.'):
    # Bỏ qua thư mục ẩn và virtual env
    dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['venv', '__pycache__']]
    
    for file in files:
        if file.endswith('.py') and not file.startswith('check_'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    line_count = len(f.readlines())
                files_info.append((filepath, line_count))
            except:
                pass

# Sắp xếp theo số dòng giảm dần
files_info.sort(key=lambda x: x[1], reverse=True)

# In kết quả
print("\n" + "="*80)
print("KIỂM TRA SỐ DÒNG CODE - QUY TẮC: MAX 300 DÒNG/FILE")
print("="*80)

print("\n🔴 CẦN REFACTOR (> 300 dòng):")
need_refactor = [f for f in files_info if f[1] > 300]
if need_refactor:
    for filepath, lines in need_refactor:
        print(f"  ❌ {filepath:60s} {lines:5d} dòng")
else:
    print("  ✅ Không có file nào!")

print("\n🟡 CẢNH BÁO (200-300 dòng):")
warning_files = [f for f in files_info if 200 <= f[1] <= 300]
if warning_files:
    for filepath, lines in warning_files:
        print(f"  ⚠️  {filepath:60s} {lines:5d} dòng")
else:
    print("  ✅ Không có file nào!")

print("\n🟢 TỐT (< 200 dòng):")
good_files = [f for f in files_info if f[1] < 200]
for filepath, lines in good_files[:10]:  # Chỉ hiện 10 file đầu
    print(f"  ✅ {filepath:60s} {lines:5d} dòng")
if len(good_files) > 10:
    print(f"  ... và {len(good_files) - 10} file khác")

print("\n" + "="*80)
print(f"TỔNG: {len(files_info)} files | Cần refactor: {len(need_refactor)} files")
print("="*80 + "\n")

