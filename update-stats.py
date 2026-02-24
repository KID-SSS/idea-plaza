#!/usr/bin/env python3
"""
自动更新首页 index.html 的统计数字
支持4个广场：专业创意、专业需求、日常创意、日常需求
"""

import re
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def count_cards(filename, pattern='class="card'):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return len(re.findall(pattern, f.read()))
    except:
        return 0

def extract_total(filename, pattern):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            m = re.search(pattern, f.read())
            return int(m.group(1)) if m else 0
    except:
        return 0

# 统计数据
ideas_today = count_cards('ideas.html')
ideas_total = extract_total('all-ideas.html', r'累计\s*(\d+)\s*个创意')
demands_today = count_cards('demands.html')
demands_total = extract_total('all-demands.html', r'累计\s*(\d+)\s*个需求')
life_ideas_today = count_cards('life-ideas.html')
life_ideas_total = extract_total('all-life-ideas.html', r'累计\s*(\d+)\s*个')
life_demands_today = count_cards('life-demands.html')
life_demands_total = extract_total('all-life-demands.html', r'累计\s*(\d+)\s*个')

print(f"📊 统计结果:")
print(f"   专业创意: 今日 {ideas_today}, 累计 {ideas_total}")
print(f"   专业需求: 今日 {demands_today}, 累计 {demands_total}")
print(f"   日常创意: 今日 {life_ideas_today}, 累计 {life_ideas_total}")
print(f"   日常需求: 今日 {life_demands_today}, 累计 {life_demands_total}")

# 读取首页
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 按4个卡片的 href 分割
markers = [
    'href="/demands.html"',
    'href="/life-ideas.html"',
    'href="/life-demands.html"',
]

parts = [html]
for marker in markers:
    last = parts[-1]
    split = last.split(marker, 1)
    if len(split) == 2:
        parts[-1] = split[0]
        parts.append(marker + split[1])

if len(parts) == 4:
    ideas_part, demands_part, life_ideas_part, life_demands_part = parts

    # 更新专业创意
    ideas_part = re.sub(
        r'(<div class="stat-num">)\d+(</div>\s*<div class="stat-label">今日创意)',
        rf'\g<1>{ideas_today}\2', ideas_part)
    ideas_part = re.sub(
        r'(<div class="stat-num">)\d+(</div>\s*<div class="stat-label">累计收录)',
        rf'\g<1>{ideas_total}\2', ideas_part, count=1)

    # 更新专业需求
    demands_part = re.sub(
        r'(<div class="stat-num">)\d+(</div>\s*<div class="stat-label">今日需求)',
        rf'\g<1>{demands_today}\2', demands_part)
    demands_part = re.sub(
        r'(<div class="stat-num">)\d+(</div>\s*<div class="stat-label">累计收录)',
        rf'\g<1>{demands_total}\2', demands_part, count=1)

    # 更新日常创意
    life_ideas_part = re.sub(
        r'(<div class="stat-num">)\d+(</div>\s*<div class="stat-label">今日日常创意)',
        rf'\g<1>{life_ideas_today}\2', life_ideas_part)
    life_ideas_part = re.sub(
        r'(<div class="stat-num">)\d+(</div>\s*<div class="stat-label">累计收录)',
        rf'\g<1>{life_ideas_total}\2', life_ideas_part, count=1)

    # 更新日常需求
    life_demands_part = re.sub(
        r'(<div class="stat-num">)\d+(</div>\s*<div class="stat-label">今日日常需求)',
        rf'\g<1>{life_demands_today}\2', life_demands_part)
    life_demands_part = re.sub(
        r'(<div class="stat-num">)\d+(</div>\s*<div class="stat-label">累计收录)',
        rf'\g<1>{life_demands_total}\2', life_demands_part, count=1)

    html = ideas_part + demands_part + life_ideas_part + life_demands_part
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ index.html 统计已更新（4个广场）")
else:
    print(f"❌ 分割失败，只得到 {len(parts)} 段（预期4段）")
