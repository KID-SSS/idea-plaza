#!/usr/bin/env python3
"""
从 JSON 数据文件生成 life-demands.html 页面（日常需求广场）
用法: python3 build_life_demands.py life_demands_data.json
AI 只需输出 JSON，本脚本负责渲染 HTML
"""
import json
import sys
import os
import re
from datetime import datetime

os.chdir(os.path.dirname(os.path.abspath(__file__)))

CSS = """*{margin:0;padding:0;box-sizing:border-box}body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:linear-gradient(135deg,#0a0a0f,#1a1a2e 50%,#16213e);min-height:100vh;color:#e8e8e8;line-height:1.6}.container{max-width:1400px;margin:0 auto;padding:20px}header{text-align:center;padding:50px 0;border-bottom:1px solid rgba(255,255,255,0.1);margin-bottom:40px}h1{font-size:3rem;background:linear-gradient(90deg,#ff8c00,#4ecdc4,#ff8c00);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:15px;font-weight:800}.subtitle{color:#888;font-size:1.2rem}.date{color:#ff8c00;font-size:0.95rem;margin-top:15px;display:inline-block;background:rgba(255,140,0,0.1);padding:8px 20px;border-radius:20px}.nav-links{margin-top:20px}.nav-links a{color:#4ecdc4;text-decoration:none;margin:0 15px;padding:8px 16px;border:1px solid rgba(78,205,196,0.3);border-radius:20px;font-size:0.9rem}.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:20px;margin-bottom:40px}.stat-card{background:rgba(255,255,255,0.02);border-radius:16px;padding:25px;border:1px solid rgba(255,255,255,0.06);text-align:center}.stat-card .number{font-size:2.5rem;font-weight:800;background:linear-gradient(90deg,#ff8c00,#4ecdc4);-webkit-background-clip:text;-webkit-text-fill-color:transparent}.stat-card .label{color:#888;font-size:0.9rem;margin-top:8px}.sec{margin-bottom:50px}.sec h2{color:#fff;font-size:1.6rem;margin-bottom:30px;padding-left:15px;border-left:4px solid #ff8c00}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(380px,1fr));gap:25px}.card{background:rgba(255,255,255,0.02);border-radius:20px;padding:25px;border:1px solid rgba(255,255,255,0.06);transition:all 0.3s}.card:hover{transform:translateY(-5px)}.card.web{border-color:rgba(78,205,196,0.3);background:rgba(78,205,196,0.02)}.hd{display:flex;justify-content:space-between;margin-bottom:15px}.num{background:linear-gradient(135deg,#ff8c00,#4ecdc4);color:#0a0a0f;width:36px;height:36px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-weight:800}.sc{background:rgba(255,140,0,0.15);color:#ff8c00;padding:5px 14px;border-radius:20px;font-weight:bold}.ti{font-size:1.25rem;color:#fff;margin-bottom:10px;font-weight:700}.ti a{color:#fff;text-decoration:none}.ds{color:#aaa;margin-bottom:15px;font-size:0.9rem}.source{color:#666;font-size:0.8rem;margin-bottom:15px}.source a{color:#4ecdc4}.tags{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:15px}.tag{padding:5px 12px;border-radius:8px;font-size:0.75rem}.tag.pain{background:rgba(255,140,0,0.15);color:#ff8c00}.tag.freq{background:rgba(78,205,196,0.15);color:#4ecdc4}.tag.audience{background:rgba(255,107,107,0.15);color:#ff6b6b}.tag.category{background:rgba(255,140,0,0.1);color:#ffb347;border:1px solid rgba(255,140,0,0.2)}.tag.web{background:linear-gradient(90deg,rgba(78,205,196,0.2),rgba(0,217,255,0.2));color:#4ecdc4}.an{background:rgba(0,0,0,0.2);border-radius:14px;padding:15px;margin-bottom:15px}.an-ti{color:#888;font-size:0.75rem;margin-bottom:12px}.bars{display:grid;gap:8px}.bar{display:grid;grid-template-columns:80px 1fr 30px;gap:8px}.bar .l{font-size:0.75rem;color:#aaa}.bar .bg{height:6px;background:rgba(255,255,255,0.1);border-radius:3px}.bar .f{height:100%;border-radius:3px}.bar .f.pain{background:#ff8c00}.bar .f.freq{background:#4ecdc4}.bar .f.audience{background:#ff6b6b}.bar .f.diff{background:#00d9ff}.bar .v{font-size:0.8rem;color:#fff;font-weight:600;text-align:right}.insight{background:rgba(255,140,0,0.1);padding:12px;border-radius:10px;border-left:3px solid #ff8c00;margin-bottom:10px}.insight h4{color:#ff8c00;font-size:0.8rem;margin-bottom:5px}.insight p{color:#ccc;font-size:0.85rem}footer{text-align:center;padding:50px 0;margin-top:60px;border-top:1px solid rgba(255,255,255,0.1);color:#666}footer a{color:#4ecdc4}@media(max-width:768px){h1{font-size:2rem}.grid{grid-template-columns:1fr}}.badge{display:inline-block;padding:4px 10px;border-radius:6px;font-size:0.7rem;font-weight:600;margin-left:8px}.badge.web{background:linear-gradient(90deg,#4ecdc4,#00d9ff);color:#0a0a0f}.badge.app{background:linear-gradient(90deg,#ff8c00,#ffd700);color:#0a0a0f}.badge.both{background:linear-gradient(90deg,#a855f7,#4ecdc4);color:#fff}"""


CATEGORY_EMOJI = {
    "育儿": "👶",
    "健康": "💊",
    "家务": "🧹",
    "出行": "🚗",
    "宠物": "🐾",
    "学习": "📚",
    "情感": "💝",
    "购物": "🛒",
    "老人关怀": "👴",
    "其他": "📌",
}


def get_form_badge(form):
    """根据推荐形态返回 badge"""
    form = (form or "").lower()
    if "web" in form and ("app" in form or "原生" in form):
        return '<span class="badge both">🌐📱 两者皆可</span>'
    elif "app" in form or "原生" in form:
        return '<span class="badge app">📱 原生APP</span>'
    else:
        return '<span class="badge web">🌐 Web网站</span>'


def gen_life_demand_card(d, idx):
    """生成单个日常需求卡片 HTML"""
    form = d.get("form", "web")
    card_class = " web" if "web" in form.lower() else ""
    badge = get_form_badge(form)

    category = d.get("category", "其他")
    cat_emoji = CATEGORY_EMOJI.get(category, "📌")

    # Tags
    tags_html = f'<span class="tag category">{cat_emoji} {category}</span>'
    tags_html += f'<span class="tag pain">🔥 痛点: {d.get("pain_score", "?")}/10</span>'
    tags_html += f'<span class="tag freq">🔄 频次: {d.get("freq", "?")}/10</span>'
    tags_html += f'<span class="tag audience">👥 受众: {d.get("audience", "?")}/10</span>'
    if "web" in form.lower():
        tags_html += '<span class="tag web">⚡ 可Web实现</span>'

    # Score bars
    dims = [
        ("痛点强度", "pain", d.get("pain_score", 0)),
        ("需求频次", "freq", d.get("freq", 0)),
        ("受众规模", "audience", d.get("audience", 0)),
        ("实现难度", "diff", d.get("difficulty", 0)),
    ]
    bars = ""
    for label, css_class, v in dims:
        bars += f'<div class="bar"><span class="l">{label}</span><div class="bg"><div class="f {css_class}" style="width:{v*10}%"></div></div><span class="v">{v}</span></div>\n'

    # Source
    src = d.get("source", "")
    src_label = "Reddit"
    for sub in ["LifeHacks", "mildlyinfuriating", "AskReddit", "Parenting", "Frugal",
                 "AgingParents", "CaregiverSupport", "parentalcontrols", "Pets", "EatCheapAndHealthy"]:
        if sub.lower() in src.lower():
            src_label = f"r/{sub}"
            break

    # Average score = (pain_score + freq + audience) / 3
    pain = d.get("pain_score", 0)
    freq = d.get("freq", 0)
    audience = d.get("audience", 0)
    avg_score = round((pain + freq + audience) / 3, 1)

    return f'''<div class="card{card_class}">
<div class="hd"><span class="num">{idx}</span><span class="sc">{avg_score}</span></div>
<h3 class="ti">{d["title"]}{badge}</h3>
<p class="ds">{d["desc"]}</p>
<div class="source">来源: <a href="{src}">{src_label}</a></div>
<div class="tags">{tags_html}</div>
<div class="an"><div class="an-ti">四维评分</div><div class="bars">
{bars}</div></div>
<div class="insight"><h4>💡 需求洞察</h4><p>{d.get("insight", "")}</p></div>
</div>'''


def build_life_demands_html(data, output_path="life-demands.html"):
    """从 JSON 数据生成 life-demands.html"""
    demands = data.get("life_demands", [])
    date_str = data.get("date", datetime.now().strftime("%Y-%m-%d"))
    weekday_map = {0: "周一", 1: "周二", 2: "周三", 3: "周四", 4: "周五", 5: "周六", 6: "周日"}
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        weekday = weekday_map[dt.weekday()]
    except:
        weekday = ""

    count = len(demands)

    # Sort by average score
    def avg_score(d):
        return (d.get("pain_score", 0) + d.get("freq", 0) + d.get("audience", 0)) / 3

    demands.sort(key=avg_score, reverse=True)

    cards_html = "\n".join(gen_life_demand_card(d, i + 1) for i, d in enumerate(demands))

    # Stats
    web_count = sum(1 for d in demands if "web" in (d.get("form", "")).lower())
    avg_pain = round(sum(d.get("pain_score", 0) for d in demands) / count, 1) if count else 0
    categories = set(d.get("category", "其他") for d in demands)

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>日常需求发现 - 日常需求广场</title>
<style>{CSS}</style>
</head>
<body>
<div class="container">
<header>
<h1>🏠 日常需求发现</h1>
<p class="subtitle">来自真实生活的需求 · 每日更新</p>
<p class="date">📅 {date_str} · {weekday} · 今日发现 {count} 个日常需求</p>
<div class="nav-links">
<a href="/">🏠 广场中心</a>
<a href="/all-life-demands.html">📋 全部日常需求</a>
<a href="/archive/life-demands/">🗂️ 日常需求归档</a>
</div>
</header>

<div class="stats">
<div class="stat-card"><div class="number">{count}</div><div class="label">今日需求</div></div>
<div class="stat-card"><div class="number">{web_count}</div><div class="label">可Web实现</div></div>
<div class="stat-card"><div class="number">{avg_pain}</div><div class="label">平均痛点</div></div>
<div class="stat-card"><div class="number">{len(categories)}</div><div class="label">涉及分类</div></div>
</div>

<section class="sec">
<h2>📋 日常需求详情（{count}个）</h2>
<div class="grid">
{cards_html}
</div>
</section>

<footer>
<p>🏠 日常需求广场 · 每日更新 · 数据来源 Reddit</p>
<p style="margin-top:10px">从真实生活需求中发现身边的创业机会</p>
</footer>
</div>
</body>
</html>'''

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Generated {output_path} ({len(html)} bytes, {count} life demands)")
    return count


def append_to_all_life_demands(data, json_db_path="all_life_demands_data.json", html_path="all-life-demands.html"):
    """将新需求追加到 JSON 数据库（去重），然后重新生成 all-life-demands.html

    数据真相存储在 all_life_demands_data.json，HTML 只是渲染产物。
    """
    new_demands = data.get("life_demands", [])
    today = data.get("date", datetime.now().strftime("%Y-%m-%d"))

    # 1. 加载现有 JSON 数据库
    existing_data = {"last_updated": today, "total": 0, "life_demands": []}
    if os.path.exists(json_db_path):
        with open(json_db_path, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)

    existing_titles = {d["title"].strip() for d in existing_data["life_demands"]}

    # 2. 去重追加新需求
    added = []
    for d in new_demands:
        title = d["title"].strip()
        if title not in existing_titles:
            d.setdefault("added_date", today)
            existing_data["life_demands"].append(d)
            existing_titles.add(title)
            added.append(d)

    total = len(existing_data["life_demands"])
    existing_data["total"] = total
    existing_data["last_updated"] = today

    # 3. 写回 JSON 数据库
    with open(json_db_path, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)

    if not added:
        print(f"ℹ️  No new life demands to add (all duplicates), total: {total}")
    else:
        print(f"✅ Added {len(added)} new life demands to {json_db_path} (total: {total})")

    # 4. 从 JSON 数据库重新生成 all-life-demands.html（完整重建）
    _rebuild_all_life_demands_html(existing_data, html_path)

    return total


def _rebuild_all_life_demands_html(data, output_path="all-life-demands.html"):
    """从 JSON 数据重新生成完整的 all-life-demands.html 页面"""
    demands = data.get("life_demands", [])
    total = len(demands)

    # 按综合评分降序排列
    def avg_score(d):
        return (d.get("pain_score", 0) + d.get("freq", 0) + d.get("audience", 0)) / 3

    demands_sorted = sorted(demands, key=avg_score, reverse=True)

    cards_html = "\n".join(gen_life_demand_card(d, i + 1) for i, d in enumerate(demands_sorted))

    # 统计
    web_count = sum(1 for d in demands if "web" in (d.get("form", "")).lower())
    avg_pain = round(sum(d.get("pain_score", 0) for d in demands) / total, 1) if total else 0
    categories = set(d.get("category", "其他") for d in demands)

    # 按日期统计
    dates = {}
    for d in demands:
        dt = d.get("added_date", "unknown")
        dates[dt] = dates.get(dt, 0) + 1
    days_count = len([k for k in dates if k != "unknown"])

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>全部日常需求 - 日常需求广场</title>
<style>{CSS}</style>
</head>
<body>
<div class="container">
<header>
<h1>📋 全部日常需求</h1>
<p class="subtitle">累计收录的所有日常生活需求</p>
<p class="date">📅 累计 {total} 个日常需求 · 收录 {days_count} 天 · 持续更新中</p>
<div class="nav-links">
<a href="/">🏠 广场中心</a>
<a href="/life-demands.html">🏠 今日日常需求</a>
<a href="/archive/life-demands/">🗂️ 日常需求归档</a>
</div>
</header>

<div class="stats">
<div class="stat-card"><div class="number">{total}</div><div class="label">累计需求总数</div></div>
<div class="stat-card"><div class="number">{web_count}</div><div class="label">可Web实现</div></div>
<div class="stat-card"><div class="number">{avg_pain}</div><div class="label">平均痛点</div></div>
<div class="stat-card"><div class="number">{len(categories)}</div><div class="label">涉及分类</div></div>
</div>

<section class="sec">
<h2>📋 全部日常需求（{total}个，按评分排序）</h2>
<div class="grid">
{cards_html}
</div>
</section>

<footer>
<p>🏠 日常需求广场 · 每日更新 · 数据来源 Reddit</p>
<p style="margin-top:10px">从真实生活需求中发现身边的创业机会</p>
</footer>
</div>
</body>
</html>'''

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Rebuilt {output_path} ({len(html)} bytes, {total} life demands)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 build_life_demands.py <life_demands_data.json>")
        print("")
        print("JSON 格式:")
        print(json.dumps({
            "date": "2026-02-22",
            "life_demands": [{
                "title": "需求标题",
                "desc": "需求描述",
                "category": "育儿",
                "pain_score": 8,
                "freq": 9,
                "audience": 7,
                "difficulty": 5,
                "form": "🌐 Web网站",
                "insight": "为什么这个需求值得做",
                "source": "https://reddit.com/..."
            }]
        }, ensure_ascii=False, indent=2))
        sys.exit(1)

    json_path = sys.argv[1]
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    build_life_demands_html(data)
    total = append_to_all_life_demands(data)
    print(f"📊 累计日常需求: {total}")
