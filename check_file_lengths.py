#!/usr/bin/env python3
"""
Script kiểm tra độ dài các file Python
Cảnh báo nếu có file >300 dòng
"""

import os
from pathlib import Path

def count_lines(file_path):
    """Đếm số dòng trong file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return len(f.readlines())
    except:
        return 0

def check_large_files(root_dir="diseases", max_lines=300):
    """Kiểm tra các file lớn"""
    large_files = []
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py') and file != '__init__.py':
                file_path = os.path.join(root, file)
                lines = count_lines(file_path)
                
                if lines > max_lines:
                    large_files.append((file_path, lines))
    
    # Sắp xếp theo số dòng giảm dần
    large_files.sort(key=lambda x: x[1], reverse=True)
    
    if large_files:
        print(f"\n⚠️  CẢNH BÁO: Phát hiện {len(large_files)} file vượt quá {max_lines} dòng!\n")
        print("File cần chia nhỏ:")
        print("-" * 70)
        
        for i, (file_path, lines) in enumerate(large_files, 1):
            status = "❌ RẤT DÀI" if lines > 500 else "⚠️  Dài"
            print(f"{i}. {status}: {file_path}")
            print(f"   → {lines} dòng (vượt {lines - max_lines} dòng)")
        
        print("-" * 70)
        print(f"\n💡 Gợi ý: Chia mỗi file thành các module nhỏ hơn (<{max_lines} dòng/file)")
        return False
    else:
        print(f"\n✅ Tất cả file Python đều <={max_lines} dòng!")
        return True

if __name__ == "__main__":
    check_large_files()

