#!/usr/bin/env python3
"""
从 JSON 数据文件生成 life-ideas.html 页面（日常创意）
用法: python3 build_life_ideas.py life_ideas_data.json
AI 只需输出 JSON，本脚本负责渲染 HTML
"""
import json
import sys
import os
from datetime import datetime

os.chdir(os.path.dirname(os.path.abspath(__file__)))

CSS = """*{margin:0;padding:0;box-sizing:border-box}body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:linear-gradient(135deg,#0a0a0f,#1a1a2e 50%,#16213e);min-height:100vh;color:#e8e8e8;line-height:1.6}.container{max-width:1400px;margin:0 auto;padding:20px}header{text-align:center;padding:50px 0;border-bottom:1px solid rgba(255,255,255,0.1);margin-bottom:40px}h1{font-size:3rem;background:linear-gradient(90deg,#ff8c00,#4ecdc4);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:15px;font-weight:800}.subtitle{color:#888;font-size:1.2rem}.date{color:#ff8c00;font-size:0.95rem;margin-top:15px;display:inline-block;background:rgba(255,140,0,0.1);padding:8px 20px;border-radius:20px}.legend{background:rgba(255,255,255,0.03);border-radius:16px;padding:25px;margin-bottom:40px;border:1px solid rgba(255,255,255,0.08)}.legend h3{color:#ff8c00;margin-bottom:15px;font-size:1.1rem}.legend-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:15px}.legend-item{display:flex;align-items:center;gap:10px;font-size:0.9rem;color:#aaa}.legend-item .dot{width:12px;height:12px;border-radius:50%}.dot.m{background:#00ff88}.dot.t{background:#00d9ff}.dot.p{background:#ffd700}.dot.c{background:#ff6b6b}.dot.g{background:#a855f7}.badge{display:inline-block;padding:4px 10px;border-radius:6px;font-size:0.7rem;font-weight:600;margin-left:8px}.badge.d{background:linear-gradient(90deg,#00ff88,#00d9ff);color:#0a0a0f}.top{background:linear-gradient(135deg,rgba(255,140,0,0.1) 0%,rgba(78,205,196,0.05) 100%);border-radius:20px;padding:35px;margin-bottom:50px;border:1px solid rgba(255,140,0,0.2)}.top h2{color:#fff;margin-bottom:25px;font-size:1.6rem}.top-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:20px}.tc{background:rgba(0,0,0,0.3);border-radius:16px;padding:25px;border:1px solid rgba(255,255,255,0.1);transition:all 0.3s;position:relative;overflow:hidden}.tc::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,#ff8c00,#4ecdc4)}.tc:hover{transform:translateY(-8px);box-shadow:0 20px 40px rgba(255,140,0,0.15)}.tc .r{font-size:2.5rem;margin-bottom:12px}.tc .n{font-weight:700;color:#fff;font-size:1.1rem;margin-bottom:8px}.tc .s{color:#4ecdc4;font-size:1.4rem;font-weight:bold;margin-bottom:10px}.tc .re{color:#999;font-size:0.85rem;line-height:1.5}.sec h2{color:#fff;font-size:1.6rem;margin-bottom:30px;padding-left:15px;border-left:4px solid #4ecdc4}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(380px,1fr));gap:25px}.card{background:rgba(255,255,255,0.02);border-radius:20px;padding:25px;border:1px solid rgba(255,255,255,0.06);transition:all 0.3s}.card:hover{background:rgba(255,255,255,0.04);border-color:rgba(255,140,0,0.2);transform:translateY(-5px)}.card.dp{border-color:rgba(0,255,136,0.3);background:rgba(0,255,136,0.02)}.hd{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:15px}.num{background:linear-gradient(135deg,#ff8c00,#4ecdc4);color:#0a0a0f;width:36px;height:36px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-weight:800}.sc{background:rgba(255,140,0,0.15);color:#4ecdc4;padding:5px 14px;border-radius:20px;font-weight:bold}.ti{font-size:1.25rem;color:#fff;margin-bottom:10px;font-weight:700}.ds{color:#aaa;margin-bottom:15px;font-size:0.9rem;line-height:1.6}.tags{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:15px}.tag{padding:5px 12px;border-radius:8px;font-size:0.75rem}.tag.u{background:rgba(255,140,0,0.15);color:#ff8c00}.tag.pr{background:rgba(0,255,136,0.15);color:#00ff88}.tag.dp{background:linear-gradient(90deg,rgba(0,255,136,0.2),rgba(255,140,0,0.2));color:#00ff88;border:1px solid rgba(0,255,136,0.3)}.an{background:rgba(0,0,0,0.2);border-radius:14px;padding:15px;margin-bottom:15px}.an-ti{color:#888;font-size:0.75rem;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px}.bars{display:grid;gap:8px}.bar{display:grid;grid-template-columns:80px 1fr 30px;align-items:center;gap:8px}.bar .l{font-size:0.75rem;color:#aaa}.bar .bg{height:6px;background:rgba(255,255,255,0.1);border-radius:3px;overflow:hidden}.bar .f{height:100%;border-radius:3px}.bar .f.m{background:linear-gradient(90deg,#00ff88,#00cc6a)}.bar .f.t{background:linear-gradient(90deg,#00d9ff,#0099cc)}.bar .f.p{background:linear-gradient(90deg,#ffd700,#ffaa00)}.bar .f.c{background:linear-gradient(90deg,#ff6b6b,#ff4444)}.bar .f.g{background:linear-gradient(90deg,#a855f7,#8b5cf6)}.bar .v{font-size:0.8rem;color:#fff;font-weight:600;text-align:right}.dg{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px}.db{background:rgba(255,255,255,0.03);border-radius:10px;padding:10px}.db h4{color:#ff8c00;font-size:0.75rem;margin-bottom:5px}.db p{color:#999;font-size:0.8rem;line-height:1.4}.rec{background:linear-gradient(135deg,rgba(0,255,136,0.1) 0%,rgba(255,140,0,0.05) 100%);padding:12px;border-radius:10px;border-left:3px solid #00ff88;margin-bottom:10px}.rec h4{color:#00ff88;font-size:0.8rem;margin-bottom:5px}.rec p{color:#ccc;font-size:0.85rem;line-height:1.5}.mvp{background:rgba(168,85,247,0.1);padding:10px;border-radius:10px;border:1px solid rgba(168,85,247,0.2);margin-bottom:10px}.mvp h4{color:#a855f7;font-size:0.75rem;margin-bottom:4px}.mvp p{color:#aaa;font-size:0.8rem}.dep{background:linear-gradient(90deg,rgba(0,255,136,0.1),rgba(255,140,0,0.1));padding:10px;border-radius:10px;border:1px dashed rgba(0,255,136,0.3);margin-bottom:10px}.dep h4{color:#00ff88;font-size:0.75rem;margin-bottom:4px}.dep p{color:#aaa;font-size:0.8rem}.src{margin-top:10px;padding-top:10px;border-top:1px solid rgba(255,255,255,0.05)}.src a{color:#666;font-size:0.7rem;text-decoration:none}.src a:hover{color:#ff8c00}footer{text-align:center;padding:50px 0;margin-top:60px;border-top:1px solid rgba(255,255,255,0.1);color:#666}footer a{color:#ff8c00;text-decoration:none}@media(max-width:768px){h1{font-size:2rem}.grid{grid-template-columns:1fr}.dg{grid-template-columns:1fr}}"""


def gen_card(idea, idx):
    """生成单个创意卡片 HTML"""
    deploy = idea.get("deployable", False)
    dp_class = ' dp' if deploy else ''
    badge = ' <span class="badge d">⚡ 可直接部署</span>' if deploy else ''

    # Tags
    tags_html = f'<span class="tag u">👥 {idea["users"]}</span>'
    if idea.get("type"):
        tags_html += f'<span class="tag pr">🌐 {idea["type"]}</span>'
    if idea.get("platform"):
        tags_html += f'<span class="tag dp">🚀 {idea["platform"]}</span>'

    # Score bars
    sc = idea["scores"]
    dims = [("市场需求", "m"), ("技术可行", "t"), ("变现潜力", "p"), ("竞争优势", "c"), ("增长潜力", "g")]
    bars = ""
    for label, key in dims:
        v = sc.get(key, 0)
        bars += f'<div class="bar"><span class="l">{label}</span><div class="bg"><div class="f {key}" style="width:{v*10}%"></div></div><span class="v">{v}</span></div>\n'

    # Deploy section
    dep_html = ""
    if idea.get("deploy"):
        dep_html = f'<div class="dep"><h4>⚡ 部署方案</h4><p>{idea["deploy"]}</p></div>'

    # Source subreddit
    src = idea.get("source", "")
    src_label = "Reddit"
    for sub in ["SaaS", "SideProject", "Entrepreneur", "SomebodyMakeThis", "AppIdeas"]:
        if sub.lower() in src.lower():
            src_label = f"r/{sub}"
            break

    return f'''<div class="card{dp_class}">
<div class="hd"><span class="num">{idx}</span><span class="sc">{idea["score"]}</span></div>
<h3 class="ti">{idea["title"]}{badge}</h3>
<p class="ds">{idea["desc"]}</p>
<div class="tags">{tags_html}</div>
<div class="an"><div class="an-ti">五维评分</div><div class="bars">
{bars}</div></div>
<div class="dg">
<div class="db"><h4>🎯 目标用户</h4><p>{idea.get("target","")}</p></div>
<div class="db"><h4>💰 商业模式</h4><p>{idea.get("business","")}</p></div>
</div>
<div class="rec"><h4>✅ 推荐理由</h4><p>{idea.get("reason","")}</p></div>
<div class="mvp"><h4>🛠️ MVP</h4><p>{idea.get("mvp","")}</p></div>
{dep_html}
<div class="src"><a href="{src}">📎 来源：{src_label}</a></div>
</div>'''


def build_life_ideas_html(data, output_path="life-ideas.html"):
    """从 JSON 数据生成 life-ideas.html"""
    ideas = data.get("ideas", [])
    date_str = data.get("date", datetime.now().strftime("%Y-%m-%d"))
    weekday_map = {0:"周一",1:"周二",2:"周三",3:"周四",4:"周五",5:"周六",6:"周日"}
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        weekday = weekday_map[dt.weekday()]
    except:
        weekday = ""

    count = len(ideas)

    # Sort by score desc
    ideas.sort(key=lambda x: float(x.get("score", 0)), reverse=True)

    # Top 5
    ranks = ['🥇', '🥈', '🥉', '4️⃣', '5️⃣']
    top5_html = ""
    for i, idea in enumerate(ideas[:5]):
        badge = '<span class="badge d">⚡</span>' if idea.get("deployable") else ''
        short_desc = idea["desc"][:30] + "..." if len(idea["desc"]) > 30 else idea["desc"]
        top5_html += f'<div class="tc"><div class="r">{ranks[i]}</div><div class="n">{idea["title"]}{badge}</div><div class="s">{idea["score"]}</div><div class="re">{short_desc}</div></div>\n'

    # All cards
    cards_html = "\n".join(gen_card(idea, i+1) for i, idea in enumerate(ideas))

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>日常创意广场 - Reddit精选生活创意</title>
<style>{CSS}</style>
</head>
<body>
<div class="container">
<header>
<h1>🏠 日常创意广场</h1>
<p class="subtitle">Reddit精选生活创意 · 每日更新</p>
<p class="date">📅 {date_str} · {weekday} · 收录{count}个创意 · 🔥 优先展示可部署项目</p>
<div style="margin-top:20px">
<a href="/" style="color:#fff;text-decoration:none;margin:0 10px;padding:6px 14px;border:1px solid rgba(255,255,255,0.3);border-radius:20px;font-size:0.85rem">🏠 广场中心</a>
<a href="/all-life-ideas.html" style="color:#4ecdc4;text-decoration:none;margin:0 15px;padding:8px 16px;border:1px solid rgba(78,205,196,0.3);border-radius:20px;font-size:0.9rem">📚 全部日常创意</a>
<a href="/archive/life-ideas/" style="color:#ff8c00;text-decoration:none;margin:0 15px;padding:8px 16px;border:1px solid rgba(255,140,0,0.3);border-radius:20px;font-size:0.9rem">🗂️ 日常创意归档</a>
</div>
</header>

<div class="legend">
<h3>📊 评分说明</h3>
<div class="legend-grid">
<div class="legend-item"><span class="dot m"></span> 市场需求</div>
<div class="legend-item"><span class="dot t"></span> 技术可行</div>
<div class="legend-item"><span class="dot p"></span> 变现潜力</div>
<div class="legend-item"><span class="dot c"></span> 竞争优势</div>
<div class="legend-item"><span class="dot g"></span> 增长潜力</div>
</div>
<p style="margin-top:15px;font-size:0.85rem;color:#888"><span class="badge d">⚡ 可直接部署</span> 标记的项目可部署到 Vercel/Cloudflare，无需后端</p>
</div>

<section class="top">
<h2>🏆 今日 Top 5</h2>
<div class="top-grid">
{top5_html}
</div>
</section>

<section class="sec">
<h2>📋 完整创意分析（{count}个）</h2>
<div class="grid">
{cards_html}
</div>
</section>

<footer>
<p>🏠 日常创意广场 · 每日更新 · 数据来源 Reddit</p>
<p style="margin-top:10px">⚡ 可直接部署 = 纯前端/静态站点，可部署到 Vercel/Cloudflare Pages</p>
</footer>
</div>
</body>
</html>'''

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Generated {output_path} ({len(html)} bytes, {count} ideas)")
    return count


def append_to_all_life_ideas(data, json_db_path="all_life_ideas_data.json", html_path="all-life-ideas.html"):
    """将新创意追加到 JSON 数据库（去重），然后重新生成 all-life-ideas.html

    数据真相存储在 all_life_ideas_data.json，HTML 只是渲染产物。
    """
    import re
    new_ideas = data.get("ideas", [])
    today = data.get("date", datetime.now().strftime("%Y-%m-%d"))

    # 1. 加载现有 JSON 数据库
    existing_data = {"last_updated": today, "total": 0, "ideas": []}
    if os.path.exists(json_db_path):
        with open(json_db_path, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)

    existing_titles = {i["title"].strip() for i in existing_data["ideas"]}

    # 2. 去重追加新创意
    added = []
    for idea in new_ideas:
        title = idea["title"].strip()
        if title not in existing_titles:
            idea.setdefault("added_date", today)
            existing_data["ideas"].append(idea)
            existing_titles.add(title)
            added.append(idea)

    total = len(existing_data["ideas"])
    existing_data["total"] = total
    existing_data["last_updated"] = today

    # 3. 写回 JSON 数据库
    with open(json_db_path, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)

    if not added:
        print(f"ℹ️  No new ideas to add (all duplicates), total: {total}")
    else:
        print(f"✅ Added {len(added)} new ideas to {json_db_path} (total: {total})")

    # 4. 从 JSON 数据库重新生成 all-life-ideas.html
    _rebuild_all_life_ideas_html(existing_data, html_path)

    return total


def _rebuild_all_life_ideas_html(data, output_path="all-life-ideas.html"):
    """从 JSON 数据重新生成完整的 all-life-ideas.html 页面"""
    ideas = data.get("ideas", [])
    total = len(ideas)

    # 按评分降序排列
    ideas_sorted = sorted(ideas, key=lambda x: x.get("score", 0), reverse=True)

    # Top 3
    top3 = ideas_sorted[:3]
    top3_html = ""
    medals = ["🥇", "🥈", "🥉"]
    for i, idea in enumerate(top3):
        top3_html += f'''<div class="tc"><div class="r">{medals[i]}</div>
<div class="n">{idea["title"]}</div>
<div class="s">⭐ {idea.get("score", 0)}</div>
<div class="re">{idea.get("reason", idea.get("desc", ""))[:100]}</div></div>\n'''

    cards_html = "\n".join(gen_card(idea, i+1) for i, idea in enumerate(ideas_sorted))

    # 统计
    deployable_count = sum(1 for i in ideas if i.get("deployable"))

    # 按日期统计
    dates = {}
    for idea in ideas:
        dt = idea.get("added_date", "unknown")
        dates[dt] = dates.get(dt, 0) + 1
    days_count = len([k for k in dates if k not in ("unknown", "")])

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>全部日常创意 - 日常创意广场</title>
<style>{CSS}</style>
</head>
<body>
<div class="container">
<header>
<h1>💡 全部日常创意</h1>
<p class="subtitle">累计收录的所有 Reddit 日常创意项目</p>
<p class="date">📅 累计 {total} 个创意 · 持续更新中</p>
<div class="nav-links" style="margin-top:20px">
<a href="/" style="color:#ff8c00;text-decoration:none;margin:0 15px;padding:8px 16px;border:1px solid rgba(255,140,0,0.3);border-radius:20px;font-size:0.9rem">🏠 广场中心</a>
<a href="/life-ideas.html" style="color:#ff8c00;text-decoration:none;margin:0 15px;padding:8px 16px;border:1px solid rgba(255,140,0,0.3);border-radius:20px;font-size:0.9rem">🏠 今日创意</a>
<a href="/archive/life-ideas/" style="color:#ff8c00;text-decoration:none;margin:0 15px;padding:8px 16px;border:1px solid rgba(255,140,0,0.3);border-radius:20px;font-size:0.9rem">🗂️ 日常创意归档</a>
</div>
</header>

<div class="legend">
<h3>📊 五维评分说明</h3>
<div class="legend-grid">
<div class="legend-item"><span class="dot m"></span>市场潜力 (M)</div>
<div class="legend-item"><span class="dot t"></span>技术可行 (T)</div>
<div class="legend-item"><span class="dot p"></span>盈利能力 (P)</div>
<div class="legend-item"><span class="dot c"></span>竞争优势 (C)</div>
<div class="legend-item"><span class="dot g"></span>成长空间 (G)</div>
</div>
</div>

<div class="top">
<h2>🏆 历史 Top 3</h2>
<div class="top-grid">
{top3_html}
</div>
</div>

<section class="sec">
<h2>📋 全部日常创意（{total}个，按评分排序）</h2>
<div class="grid">
{cards_html}
</div>
</section>

<footer>
<p>💡 日常创意广场 · 每日更新 · 数据来源 Reddit</p>
<p style="margin-top:10px"><a href="/">返回广场中心</a></p>
</footer>
</div>
</body>
</html>'''

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Rebuilt {output_path} ({len(html)} bytes, {total} ideas)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 build_life_ideas.py <life_ideas_data.json>")
        print("")
        print("JSON 格式:")
        print(json.dumps({
            "date": "2026-02-22",
            "ideas": [{
                "title": "创意名称",
                "desc": "一句话描述",
                "score": 8.5,
                "deployable": True,
                "users": "目标用户群",
                "type": "Web工具",
                "platform": "Vercel",
                "target": "详细目标用户",
                "business": "商业模式",
                "reason": "推荐理由",
                "mvp": "MVP路径 | 时间",
                "deploy": "部署方案（可选）",
                "source": "https://reddit.com/...",
                "scores": {"m": 8.5, "t": 9.0, "p": 8.0, "c": 8.5, "g": 8.0}
            }]
        }, ensure_ascii=False, indent=2))
        sys.exit(1)

    json_path = sys.argv[1]
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    build_life_ideas_html(data)
    total = append_to_all_life_ideas(data)
    print(f"📊 累计创意: {total}")
