#!/usr/bin/env python3
"""
从归档 HTML 和现有 all-demands.html 中恢复所有需求数据，
创建 all_demands_data.json 和 all_ideas_data.json 作为持久存储。
"""
import re
import os
import json
from datetime import datetime

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def parse_archive_cards(html_path):
    """从归档 HTML（卡片格式）中解析需求数据"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    basename = os.path.basename(html_path)
    date_str = basename.replace('.html', '')
    
    demands = []
    card_splits = content.split('<div class="card')
    
    for card_html in card_splits[1:]:
        d = {}
        
        # Title - may be wrapped in <a> or plain text
        ti_match = re.search(r'class="ti"[^>]*>(?:<a[^>]*>)?([^<]+)', card_html)
        if ti_match:
            title = ti_match.group(1).strip()
            title = re.sub(r'<span[^>]*>.*?</span>', '', title).strip()
            d['title'] = title
        else:
            continue
        
        # Source URL from title link
        source_match = re.search(r'class="ti"[^>]*><a href="([^"]+)"', card_html)
        if source_match:
            d['source'] = source_match.group(1)
        else:
            src_match = re.search(r'来源:?\s*<a href="([^"]+)"', card_html)
            d['source'] = src_match.group(1) if src_match else ''
        
        # Description
        ds_match = re.search(r'class="ds"[^>]*>([^<]+)', card_html)
        d['desc'] = ds_match.group(1).strip() if ds_match else ''
        
        # Scores from bars
        score_vals = re.findall(r'class="v"[^>]*>([0-9.]+)<', card_html)
        if len(score_vals) >= 4:
            d['pain_score'] = float(score_vals[0])
            d['market_score'] = float(score_vals[1])
            d['difficulty'] = float(score_vals[2])
            d['monetization'] = float(score_vals[3])
        elif len(score_vals) >= 2:
            d['pain_score'] = float(score_vals[0])
            d['market_score'] = float(score_vals[1])
            d['difficulty'] = float(score_vals[2]) if len(score_vals) > 2 else 5
            d['monetization'] = float(score_vals[3]) if len(score_vals) > 3 else 5
        
        # Form/type detection
        if '纯前端' in card_html or 'frontend' in card_html.split('class="tags"')[0] if 'class="tags"' in card_html else '':
            d['form'] = '🌐 Web网站'
        elif '原生' in card_html or 'class="badge app"' in card_html:
            d['form'] = '📱 原生APP'
        else:
            d['form'] = '🔧 需后端'
        
        # Better form detection using badge
        if 'badge frontend' in card_html or 'badge both' in card_html or '⚡ 纯前端' in card_html or '⚡ 可前端实现' in card_html:
            d['form'] = '🌐 Web网站'
        elif 'badge app' in card_html or '📱 原生APP' in card_html:
            d['form'] = '📱 原生APP'
        elif '🔧 后端' in card_html or '需后端' in card_html:
            d['form'] = '🔧 需后端'
        
        # Insight
        insight_match = re.search(r'class="insight">.*?<p>([^<]+)</p>', card_html, re.DOTALL)
        d['insight'] = insight_match.group(1).strip() if insight_match else ''
        
        # Competitors
        comp_match = re.search(r'class="competitors">.*?<p>([^<]+)</p>', card_html, re.DOTALL)
        d['competitors'] = comp_match.group(1).strip() if comp_match else ''
        
        d['added_date'] = date_str
        demands.append(d)
    
    return demands


def parse_all_demands_table(html_path):
    """从 all-demands.html（表格格式）中解析需求数据"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    demands = []
    
    # Parse table rows
    rows = re.findall(
        r'<tr><td>(\d+)</td><td>(.*?)</td><td>(.*?)</td><td>([\d.]+)</td><td>([\d.]+)</td><td>([\d.]+)</td><td>(.*?)</td><td>(.*?)</td><td>([\d-]+)</td></tr>',
        content
    )
    
    for row in rows:
        num, title_html, type_html, pain, market, monetization, score_html, source, date = row
        
        d = {}
        title_match = re.search(r'>([^<]+)</a>', title_html)
        if title_match:
            d['title'] = title_match.group(1).strip()
        else:
            d['title'] = re.sub(r'<[^>]+>', '', title_html).strip()
        
        url_match = re.search(r'href="([^"]*)"', title_html)
        d['source'] = url_match.group(1) if url_match else ''
        
        # Type/form
        if '前端' in type_html:
            d['form'] = '🌐 Web网站'
        elif '原生' in type_html or '📱' in type_html:
            d['form'] = '📱 原生APP'
        else:
            d['form'] = '🔧 需后端'
        
        try: d['pain_score'] = float(pain.strip())
        except: d['pain_score'] = 0
        try: d['market_score'] = float(market.strip())
        except: d['market_score'] = 0
        try: d['monetization'] = float(monetization.strip())
        except: d['monetization'] = 0
        
        d['difficulty'] = 5  # Not available in table
        d['desc'] = ''
        d['insight'] = ''
        d['competitors'] = ''
        d['added_date'] = date.strip()
        
        demands.append(d)
    
    return demands


def parse_all_ideas_cards(html_path):
    """从 all-ideas.html（卡片格式）中解析创意数据"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    ideas = []
    card_splits = content.split('<div class="card')
    
    for card_html in card_splits[1:]:
        idea = {}
        
        # Title
        ti_match = re.search(r'class="ti"[^>]*>([^<]+)', card_html)
        if ti_match:
            title = ti_match.group(1).strip()
            title = re.sub(r'<span[^>]*>.*?</span>', '', title).strip()
            idea['title'] = title
        else:
            continue
        
        # Score
        sc_match = re.search(r'class="sc"[^>]*>([0-9.]+)', card_html)
        idea['score'] = float(sc_match.group(1)) if sc_match else 0
        
        # Description
        ds_match = re.search(r'class="ds"[^>]*>([^<]+)', card_html)
        idea['desc'] = ds_match.group(1).strip() if ds_match else ''
        
        # Users tag
        users_match = re.search(r'class="tag u"[^>]*>👥\s*([^<]+)', card_html)
        idea['users'] = users_match.group(1).strip() if users_match else ''
        
        # Type tag
        type_match = re.search(r'class="tag pr"[^>]*>🌐\s*([^<]+)', card_html)
        idea['type'] = type_match.group(1).strip() if type_match else ''
        
        # Platform tag
        platform_match = re.search(r'class="tag dp"[^>]*>🚀\s*([^<]+)', card_html)
        idea['platform'] = platform_match.group(1).strip() if platform_match else ''
        
        # Deployable
        idea['deployable'] = '可直接部署' in card_html
        
        # Five dimension scores
        score_vals = re.findall(r'class="v"[^>]*>([0-9.]+)<', card_html)
        scores = {}
        keys = ['m', 't', 'p', 'c', 'g']
        for i, val in enumerate(score_vals):
            if i < len(keys):
                scores[keys[i]] = float(val)
        idea['scores'] = scores
        
        # Target users
        target_match = re.search(r'🎯 目标用户</h4>\s*<p>([^<]+)', card_html)
        idea['target'] = target_match.group(1).strip() if target_match else ''
        
        # Business model
        biz_match = re.search(r'💰 商业模式</h4>\s*<p>([^<]+)', card_html)
        idea['business'] = biz_match.group(1).strip() if biz_match else ''
        
        # Recommendation
        rec_match = re.search(r'✅ 推荐理由</h4>\s*<p>([^<]+)', card_html)
        idea['reason'] = rec_match.group(1).strip() if rec_match else ''
        
        # MVP
        mvp_match = re.search(r'🛠️ MVP</h4>\s*<p>([^<]+)', card_html)
        idea['mvp'] = mvp_match.group(1).strip() if mvp_match else ''
        
        # Deploy
        dep_match = re.search(r'⚡ 部署方案</h4>\s*<p>([^<]+)', card_html)
        idea['deploy'] = dep_match.group(1).strip() if dep_match else ''
        
        # Source
        src_match = re.search(r'class="src"[^>]*><a href="([^"]+)"', card_html)
        idea['source'] = src_match.group(1).strip() if src_match else ''
        
        # Try to determine date from surrounding content
        idea['added_date'] = ''
        
        ideas.append(idea)
    
    return ideas


def main():
    # ===== DEMANDS =====
    print("=" * 60)
    print("📋 恢复需求数据")
    print("=" * 60)
    
    all_demands = {}  # title -> demand data (for dedup)
    
    # 1. Parse all archive files (richest data - has desc, insight, competitors)
    archive_dir = 'archive/demands'
    archive_files = sorted([f for f in os.listdir(archive_dir) if f.endswith('.html') and f != 'index.html'])
    
    for fname in archive_files:
        fpath = os.path.join(archive_dir, fname)
        demands = parse_archive_cards(fpath)
        print(f"  📁 {fname}: {len(demands)} demands")
        for d in demands:
            title = d['title']
            if title not in all_demands:
                all_demands[title] = d
            else:
                existing = all_demands[title]
                # Keep richer data, but preserve earliest date
                if len(d.get('desc', '')) > len(existing.get('desc', '')):
                    earliest = min(d['added_date'], existing['added_date'])
                    all_demands[title] = d
                    all_demands[title]['added_date'] = earliest
    
    print(f"\n  📊 From archives: {len(all_demands)} unique demands")
    
    # 2. Parse existing all-demands.html table - has data from dates not in archives (e.g. 02-12)
    table_path = 'all-demands.html.bak'
    if os.path.exists(table_path):
        table_demands = parse_all_demands_table(table_path)
        print(f"  📊 From all-demands.html table: {len(table_demands)} demands")
        new_from_table = 0
        enriched = 0
        for d in table_demands:
            title = d['title']
            if title not in all_demands:
                all_demands[title] = d
                new_from_table += 1
            else:
                # Enrich: if archive has richer data, keep it; but use table's date if earlier
                existing = all_demands[title]
                if d.get('added_date') and existing.get('added_date'):
                    if d['added_date'] < existing['added_date']:
                        existing['added_date'] = d['added_date']
                        enriched += 1
                # If archive missing source, use table's
                if not existing.get('source') and d.get('source'):
                    existing['source'] = d['source']
        print(f"  📊 New from table: {new_from_table}")
        print(f"  📊 Date-enriched from table: {enriched}")
    
    total = len(all_demands)
    print(f"\n  ✅ Total unique demands: {total}")
    
    # Sort by added_date, then title
    demands_list = sorted(all_demands.values(), key=lambda x: (x.get('added_date', ''), x.get('title', '')))
    
    # Ensure all fields exist
    for d in demands_list:
        d.setdefault('title', '')
        d.setdefault('desc', '')
        d.setdefault('form', '🔧 需后端')
        d.setdefault('pain_score', 0)
        d.setdefault('market_score', 0)
        d.setdefault('difficulty', 5)
        d.setdefault('monetization', 0)
        d.setdefault('insight', '')
        d.setdefault('competitors', '')
        d.setdefault('source', '')
        d.setdefault('added_date', '')
    
    json_data = {
        'last_updated': datetime.now().strftime('%Y-%m-%d'),
        'total': total,
        'demands': demands_list
    }
    
    with open('all_demands_data.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    print(f"\n  💾 Saved all_demands_data.json ({total} demands)")
    
    dates = {}
    for d in demands_list:
        dt = d.get('added_date', 'unknown')
        dates[dt] = dates.get(dt, 0) + 1
    print("\n  📅 By date:")
    for dt in sorted(dates.keys()):
        print(f"    {dt}: {dates[dt]} demands")
    
    # ===== IDEAS =====
    print("\n" + "=" * 60)
    print("💡 恢复创意数据")
    print("=" * 60)
    
    all_ideas = {}
    
    # Parse archive files first
    ideas_archive_dir = 'archive/ideas'
    ideas_archive_files = sorted([f for f in os.listdir(ideas_archive_dir) if f.endswith('.html') and f != 'index.html'])
    
    for fname in ideas_archive_files:
        fpath = os.path.join(ideas_archive_dir, fname)
        date_str = fname.replace('.html', '')
        ideas = parse_all_ideas_cards(fpath)
        # Set date from filename
        for idea in ideas:
            idea['added_date'] = date_str
        print(f"  📁 {fname}: {len(ideas)} ideas")
        for idea in ideas:
            title = idea['title']
            if title not in all_ideas:
                all_ideas[title] = idea
            else:
                existing = all_ideas[title]
                if len(idea.get('desc', '')) > len(existing.get('desc', '')):
                    earliest = min(idea['added_date'], existing['added_date'])
                    all_ideas[title] = idea
                    all_ideas[title]['added_date'] = earliest
    
    print(f"\n  📊 From archives: {len(all_ideas)} unique ideas")
    
    # Also parse existing all-ideas.html
    if os.path.exists('all-ideas.html.bak'):
        existing_ideas = parse_all_ideas_cards('all-ideas.html.bak')
        print(f"  📊 From all-ideas.html: {len(existing_ideas)} ideas")
        new_from_existing = 0
        for idea in existing_ideas:
            title = idea['title']
            if title not in all_ideas:
                # Try to infer date from existing data (not available in all-ideas.html)
                # These are the ones NOT in archives, keep them with unknown date
                idea['added_date'] = idea.get('added_date', '') or 'unknown'
                all_ideas[title] = idea
                new_from_existing += 1
        print(f"  📊 New from all-ideas.html: {new_from_existing}")
    
    total_ideas = len(all_ideas)
    print(f"\n  ✅ Total unique ideas: {total_ideas}")
    
    ideas_list = sorted(all_ideas.values(), key=lambda x: (x.get('added_date', ''), x.get('title', '')))
    
    for idea in ideas_list:
        idea.setdefault('title', '')
        idea.setdefault('desc', '')
        idea.setdefault('score', 0)
        idea.setdefault('deployable', False)
        idea.setdefault('users', '')
        idea.setdefault('type', '')
        idea.setdefault('platform', '')
        idea.setdefault('target', '')
        idea.setdefault('business', '')
        idea.setdefault('reason', '')
        idea.setdefault('mvp', '')
        idea.setdefault('deploy', '')
        idea.setdefault('source', '')
        idea.setdefault('scores', {})
        idea.setdefault('added_date', '')
    
    ideas_json_data = {
        'last_updated': datetime.now().strftime('%Y-%m-%d'),
        'total': total_ideas,
        'ideas': ideas_list
    }
    
    with open('all_ideas_data.json', 'w', encoding='utf-8') as f:
        json.dump(ideas_json_data, f, ensure_ascii=False, indent=2)
    print(f"\n  💾 Saved all_ideas_data.json ({total_ideas} ideas)")
    
    dates = {}
    for idea in ideas_list:
        dt = idea.get('added_date', 'unknown')
        dates[dt] = dates.get(dt, 0) + 1
    print("\n  📅 By date:")
    for dt in sorted(dates.keys()):
        print(f"    {dt}: {dates[dt]} ideas")


if __name__ == '__main__':
    main()
