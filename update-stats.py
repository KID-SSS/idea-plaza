#!/usr/bin/env python3
"""
自动更新首页 index.html 的统计数字
从 ideas.html, all-ideas.html, demands.html, all-demands.html 读取实际数量
"""

import re
import os

# 切换到脚本所在目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def count_cards(filename, pattern='class="card'):
    """统计文件中卡片数量"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        return len(re.findall(pattern, content))
    except:
        return 0

def count_table_rows(filename):
    """统计表格行数（减去表头）"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        return max(0, content.count('<tr>') - 1)
    except:
        return 0

# 统计数据
ideas_today = count_cards('ideas.html')
ideas_total = count_cards('all-ideas.html')
demands_today = count_cards('demands.html')
demands_total = count_table_rows('all-demands.html')

print(f"📊 统计结果:")
print(f"   创意: 今日 {ideas_today}, 累计 {ideas_total}")
print(f"   需求: 今日 {demands_today}, 累计 {demands_total}")

# 读取首页
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 分割为创意部分和需求部分
split_marker = 'href="/demands.html"'
parts = html.split(split_marker, 1)

if len(parts) == 2:
    ideas_part, demands_part = parts[0], split_marker + parts[1]
    
    # 更新创意部分
    ideas_part = re.sub(
        r'(<div class="stat-num">)\d+(</div>\s*<div class="stat-label">今日创意)',
        rf'\g<1>{ideas_today}\2',
        ideas_part
    )
    ideas_part = re.sub(
        r'(<div class="stat-num">)\d+(</div>\s*<div class="stat-label">累计收录)',
        rf'\g<1>{ideas_total}\2',
        ideas_part,
        count=1
    )
    
    # 更新需求部分
    demands_part = re.sub(
        r'(<div class="stat-num">)\d+(</div>\s*<div class="stat-label">今日需求)',
        rf'\g<1>{demands_today}\2',
        demands_part
    )
    demands_part = re.sub(
        r'(<div class="stat-num">)\d+(</div>\s*<div class="stat-label">累计收录)',
        rf'\g<1>{demands_total}\2',
        demands_part,
        count=1
    )
    
    html = ideas_part + demands_part
    
    # 写回
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("✅ index.html 统计已更新")
else:
    print("❌ 无法解析 index.html 结构")
