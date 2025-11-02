#!/usr/bin/env python3
"""
Script to remove sys.path.insert/append from all component files
"""

import os
import re
from pathlib import Path

def fix_file(filepath):
    """Remove sys.path.insert/append lines and related imports from a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        skip_next = False
        i = 0
        
        while i < len(lines):
            line = lines[i]
            
            # Skip sys.path lines
            if 'sys.path.append' in line or 'sys.path.insert' in line:
                i += 1
                continue
            
            # Skip os.path.dirname/abspath/join lines if they're before sys.path lines
            if 'current_dir = os.path.dirname(os.path.abspath(__file__))' in line:
                i += 1
                skip_next = True
                continue
            elif 'parent_dir = os.path.abspath(os.path.join(' in line:
                i += 1
                continue
            
            # Skip comment lines related to sys.path
            if 'Thêm thư mục' in line or 'Add parent directory' in line:
                i += 1
                continue
            
            # Skip empty lines after sys.path
            if skip_next and line.strip() == '':
                i += 1
                continue
            
            skip_next = False
            new_lines.append(line)
            i += 1
        
        # Remove unused sys and os imports if they're no longer used
        final_lines = []
        has_sys = False
        has_os = False
        
        for line in new_lines:
            if line.strip().startswith('import sys'):
                has_sys = True
            elif line.strip().startswith('import os'):
                has_os = True
        
        # Only add imports if they're actually used in the code
        for line in new_lines:
            if line.strip() == 'import sys' and not any('sys.' in l for l in new_lines if l != line):
                continue
            if line.strip() == 'import os' and not any('os.' in l for l in new_lines if l != line):
                continue
            final_lines.append(line)
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(final_lines)
        
        return True
    except Exception as e:
        print(f"Error fixing {filepath}: {e}")
        return False

def main():
    """Main function"""
    components_dirs = [
        'bone_joint_page_components',
        'cardiovascular_page_components',
        'dental_page_components',
        'dermatology_page_components',
        'digestive_page_components',
        'endocrine_page_components',
        'ent_page_components',
        'eye_page_components',
        'neurological_page_components',
        'renal_page_components',
        'respiratory_page_components',
        'diary_components',
        'parasitology_page_components',
        'pediatrics_page_components',
        'women_health_page_components',
        'men_health_page_components',
    ]
    
    fixed_count = 0
    error_count = 0
    
    for dirname in components_dirs:
        if not os.path.exists(dirname):
            continue
        
        for root, dirs, files in os.walk(dirname):
            for file in files:
                if file.endswith('.py'):
                    filepath = os.path.join(root, file)
                    if fix_file(filepath):
                        fixed_count += 1
                    else:
                        error_count += 1
    
    print(f"Fixed {fixed_count} files, {error_count} errors")

if __name__ == '__main__':
    main()

