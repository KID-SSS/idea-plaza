#!/usr/bin/env python3
"""Generate the 2026-02-10 ideas page with full analysis"""

ideas = [
    {
        "num": 1, "score": 9.2, "deployable": True,
        "title": "一句话网站生成器",
        "desc": "输入一句话描述你的想法，AI即时生成一个完整的网站。无需注册，秒出结果。",
        "users": "创业者/独立开发者", "type": "AI+静态生成", "platform": "Vercel",
        "target": "非技术创业者、快速验证想法者、小微企业主",
        "business": "免费生成+自定义域名$9/月+高级模板$29",
        "reason": "极简体验是核心卖点，一句话到网站的魔法感。AI建站赛道火热，差异化在"零门槛"",
        "mvp": "输入框→AI生成HTML→预览→一键部署 | 3-4周",
        "deploy": "Next.js + OpenAI API + Vercel，静态导出后零运维",
        "source": "https://www.reddit.com/r/SaaS/comments/1r06g93/",
        "scores": {"m": 9.2, "t": 8.5, "p": 9.0, "c": 8.8, "g": 9.5}
    },
    {
        "num": 2, "score": 9.0, "deployable": True,
        "title": "创业点子毒舌评估器",
        "desc": "朋友只会鼓励你，市场会默默让你失败。AI会残酷评估你的创业想法，帮你发现致命问题。",
        "users": "创业者/产品经理", "type": "AI工具", "platform": "Vercel",
        "target": "独立开发者、想创业的程序员、产品经理",
        "business": "免费3次/天+无限使用$4.99/月",
        "reason": ""毒舌"定位有传播性，创意验证是刚需。市场上缺乏"说实话"的工具",
        "mvp": "输入创意→AI分析→输出报告+评分 | 2周",
        "deploy": "React + OpenAI API，Vercel Edge Function处理",
        "source": "https://www.reddit.com/r/SaaS/comments/1qzw9v4/",
        "scores": {"m": 9.0, "t": 9.5, "p": 8.5, "c": 9.0, "g": 8.8}
    },
    {
        "num": 3, "score": 8.8, "deployable": False,
        "title": "AI Pitch Deck 生成器",
        "desc": "用自然语言描述需求，AI自动生成演示文稿视觉效果。如"帮我做Q1-Q4产品发布路线图"。",
        "users": "创业者/投资人", "type": "SaaS", "platform": None,
        "target": "融资中的创业者、商务人员、咨询顾问",
        "business": "免费基础版+Pro $19/月（无限+高级模板）",
        "reason": "Pitch Deck是融资必需品，传统制作耗时2-3天，AI可压缩到10分钟",
        "mvp": "输入描述→选择模板→AI填充内容→导出PPT | 5-6周",
        "deploy": None,
        "source": "https://www.reddit.com/r/SideProject/comments/1qzt2fz/",
        "scores": {"m": 8.8, "t": 8.0, "p": 9.2, "c": 8.2, "g": 8.8}
    },
    {
        "num": 4, "score": 8.6, "deployable": True,
        "title": "离线隐私 AI 日记",
        "desc": "完全本地运行的AI日记：日记、语音笔记、AI总结全部在设备上完成，无数据外传。",
        "users": "隐私敏感用户", "type": "PWA", "platform": "PWA",
        "target": "隐私意识强、写日记习惯者、心理健康关注者",
        "business": "一次性购买$9.99（无订阅，符合隐私定位）",
        "reason": "隐私焦虑日益严重，"数据不离开设备"是强差异化卖点，WebLLM技术成熟",
        "mvp": "本地写日记→WebLLM总结→IndexedDB存储 | 4周",
        "deploy": "PWA + WebLLM + IndexedDB，静态托管即可",
        "source": "https://www.reddit.com/r/SideProject/comments/1qzvlnr/",
        "scores": {"m": 8.6, "t": 8.2, "p": 8.0, "c": 9.2, "g": 8.5}
    },
    {
        "num": 5, "score": 8.5, "deployable": True,
        "title": "加密证据记录器",
        "desc": "使用SHA-256哈希的加密证据记录工具。保证记录完整性，可用于法律纠纷、版权证明。",
        "users": "法律/版权从业者", "type": "静态网站", "platform": "Vercel",
        "target": "创作者、律师、企业法务、知识产权保护者",
        "business": "免费基础版+企业版$29/月（批量+API）",
        "reason": "法律证据保全是刚需，加密哈希提供可验证完整性，技术简单但价值高",
        "mvp": "上传文件→生成哈希→时间戳证明→导出报告 | 2周",
        "deploy": "纯JS + Web Crypto API，零后端",
        "source": "https://www.reddit.com/r/SideProject/comments/1r0858f/",
        "scores": {"m": 8.5, "t": 9.5, "p": 8.2, "c": 8.5, "g": 8.0}
    },
    {
        "num": 6, "score": 8.4, "deployable": True,
        "title": "创意验证框架",
        "desc": "免费创意验证框架，帮你在不花钱的情况下发现、验证和改进创业想法。",
        "users": "创业者", "type": "静态网站", "platform": "Vercel",
        "target": "早期创业者、想验证想法的开发者",
        "business": "免费框架+高级咨询$99/次",
        "reason": "系统化的验证方法论，配合工具落地执行，内容营销引流效果好",
        "mvp": "框架页面→检查清单→模板下载 | 2周",
        "deploy": "静态站点 + Notion 模板，零运维",
        "source": "https://www.reddit.com/r/SaaS/comments/1r08sh0/",
        "scores": {"m": 8.4, "t": 9.5, "p": 7.8, "c": 8.5, "g": 8.2}
    },
    {
        "num": 7, "score": 8.3, "deployable": False,
        "title": "团队旅行规划平台",
        "desc": "解决和朋友规划旅行时的Google Sheet混乱问题，统一管理行程、投票、费用分摊。",
        "users": "旅行者", "type": "Web App", "platform": None,
        "target": "喜欢和朋友旅行的人、团队建设组织者",
        "business": "免费基础版+Pro $4.99/次旅行",
        "reason": "团队旅行协调是高频痛点，现有工具体验差，社交传播属性强",
        "mvp": "创建行程→邀请好友→投票选择→费用分摊 | 4周",
        "deploy": None,
        "source": "https://www.reddit.com/r/SideProject/comments/1r0b8qj/",
        "scores": {"m": 8.3, "t": 8.0, "p": 8.0, "c": 7.8, "g": 8.5}
    },
    {
        "num": 8, "score": 8.2, "deployable": True,
        "title": "WebRTC 信令服务器",
        "desc": "轻量级WebSocket/WebRTC信令服务器，用于学习和构建实时应用架构。",
        "users": "开发者", "type": "开源工具", "platform": "Cloudflare",
        "target": "学习WebRTC的开发者、实时应用构建者",
        "business": "开源免费+托管版$9/月+企业支持",
        "reason": "实时通信需求增长，开发者需要轻量学习工具，开源可积累社区",
        "mvp": "信令服务→房间管理→示例Demo | 2周",
        "deploy": "Cloudflare Workers + Durable Objects",
        "source": "https://www.reddit.com/r/SideProject/comments/1r00jg3/",
        "scores": {"m": 8.2, "t": 9.0, "p": 7.5, "c": 8.0, "g": 8.5}
    },
    {
        "num": 9, "score": 8.0, "deployable": False,
        "title": "轮班工作者饮食规划",
        "desc": "为夜班、轮班工作者生成批量烹饪时间表和实用零食建议，保持健康饮食。",
        "users": "轮班工作者", "type": "Web App", "platform": None,
        "target": "护士、工厂工人、夜班司机、安保人员",
        "business": "免费基础版+个性化计划$6.99/月",
        "reason": "细分市场痛点明确，竞争少，差异化定位清晰，适合内容营销",
        "mvp": "输入排班→生成饮食计划→购物清单 | 3周",
        "deploy": None,
        "source": "https://www.reddit.com/r/SideProject/comments/1r0c8d5/",
        "scores": {"m": 8.0, "t": 8.5, "p": 7.8, "c": 8.8, "g": 7.5}
    },
    {
        "num": 10, "score": 7.8, "deployable": False,
        "title": "评论数据自主管理",
        "desc": "让企业摆脱Trustpilot等平台的数据绑架，自主管理和回复客户评论。",
        "users": "企业主", "type": "SaaS", "platform": None,
        "target": "中小企业主、电商卖家、服务业老板",
        "business": "免费导入+Pro $19/月（自动回复+分析）",
        "reason": "$250/月只为回复自己的评论？这个痛点值得解决，B2B定价空间大",
        "mvp": "导入评论→统一面板→一键回复→导出 | 4周",
        "deploy": None,
        "source": "https://www.reddit.com/r/SideProject/comments/1r09pkr/",
        "scores": {"m": 7.8, "t": 8.0, "p": 8.5, "c": 7.5, "g": 7.8}
    }
]

def gen_card(idea):
    dp_class = ' dp' if idea['deployable'] else ''
    badge = ' <span class="badge d">⚡ 可直接部署</span>' if idea['deployable'] else ''
    
    tags = f'<span class="tag u">👥 {idea["users"]}</span>'
    if idea['type']:
        tags += f'<span class="tag pr">🌐 {idea["type"]}</span>'
    if idea['platform']:
        tags += f'<span class="tag dp">🚀 {idea["platform"]}</span>'
    
    scores = idea['scores']
    bars = f'''<div class="bar"><span class="l">市场需求</span><div class="bg"><div class="f m" style="width:{scores["m"]*10}%"></div></div><span class="v">{scores["m"]}</span></div>
<div class="bar"><span class="l">技术可行</span><div class="bg"><div class="f t" style="width:{scores["t"]*10}%"></div></div><span class="v">{scores["t"]}</span></div>
<div class="bar"><span class="l">变现潜力</span><div class="bg"><div class="f p" style="width:{scores["p"]*10}%"></div></div><span class="v">{scores["p"]}</span></div>
<div class="bar"><span class="l">竞争优势</span><div class="bg"><div class="f c" style="width:{scores["c"]*10}%"></div></div><span class="v">{scores["c"]}</span></div>
<div class="bar"><span class="l">增长潜力</span><div class="bg"><div class="f g" style="width:{scores["g"]*10}%"></div></div><span class="v">{scores["g"]}</span></div>'''
    
    deploy_section = f'''<div class="dep"><h4>⚡ 部署方案</h4><p>{idea["deploy"]}</p></div>''' if idea['deploy'] else ''
    
    return f'''<div class="card{dp_class}">
<div class="hd"><span class="num">{idea["num"]}</span><span class="sc">{idea["score"]}</span></div>
<h3 class="ti">{idea["title"]}{badge}</h3>
<p class="ds">{idea["desc"]}</p>
<div class="tags">{tags}</div>
<div class="an"><div class="an-ti">五维评分</div><div class="bars">
{bars}
</div></div>
<div class="dg">
<div class="db"><h4>🎯 目标用户</h4><p>{idea["target"]}</p></div>
<div class="db"><h4>💰 商业模式</h4><p>{idea["business"]}</p></div>
</div>
<div class="rec"><h4>✅ 推荐理由</h4><p>{idea["reason"]}</p></div>
<div class="mvp"><h4>🛠️ MVP</h4><p>{idea["mvp"]}</p></div>
{deploy_section}
<div class="src"><a href="{idea["source"]}">📎 来源：r/{'SaaS' if 'SaaS' in idea['source'] else 'SideProject'}</a></div>
</div>'''

# Generate top 5
top5 = []
for i, idea in enumerate(ideas[:5]):
    rank = ['🥇', '🥈', '🥉', '4️⃣', '5️⃣'][i]
    badge = '<span class="badge d">⚡</span>' if idea['deployable'] else ''
    top5.append(f'<div class="tc"><div class="r">{rank}</div><div class="n">{idea["title"]}{badge}</div><div class="s">{idea["score"]}</div><div class="re">{idea["desc"][:20]}...</div></div>')

# Generate all cards
cards = [gen_card(idea) for idea in ideas]

html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>创意广场 - Reddit精选产品创意</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: linear-gradient(135deg, #0a0a0f 0%, #1a1a2e 50%, #16213e 100%); min-height: 100vh; color: #e8e8e8; line-height: 1.6; }}
        .container {{ max-width: 1400px; margin: 0 auto; padding: 20px; }}
        header {{ text-align: center; padding: 50px 0; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 40px; }}
        h1 {{ font-size: 3rem; background: linear-gradient(90deg, #00d9ff, #00ff88, #ff6b6b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 15px; font-weight: 800; }}
        .subtitle {{ color: #888; font-size: 1.2rem; }}
        .date {{ color: #00d9ff; font-size: 0.95rem; margin-top: 15px; display: inline-block; background: rgba(0,217,255,0.1); padding: 8px 20px; border-radius: 20px; }}
        .legend {{ background: rgba(255,255,255,0.03); border-radius: 16px; padding: 25px; margin-bottom: 40px; border: 1px solid rgba(255,255,255,0.08); }}
        .legend h3 {{ color: #00d9ff; margin-bottom: 15px; font-size: 1.1rem; }}
        .legend-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 15px; }}
        .legend-item {{ display: flex; align-items: center; gap: 10px; font-size: 0.9rem; color: #aaa; }}
        .legend-item .dot {{ width: 12px; height: 12px; border-radius: 50%; }}
        .dot.m {{ background: #00ff88; }} .dot.t {{ background: #00d9ff; }} .dot.p {{ background: #ffd700; }} .dot.c {{ background: #ff6b6b; }} .dot.g {{ background: #a855f7; }}
        .badge {{ display: inline-block; padding: 4px 10px; border-radius: 6px; font-size: 0.7rem; font-weight: 600; margin-left: 8px; }}
        .badge.d {{ background: linear-gradient(90deg, #00ff88, #00d9ff); color: #0a0a0f; }}
        .top {{ background: linear-gradient(135deg, rgba(0,217,255,0.1) 0%, rgba(0,255,136,0.05) 100%); border-radius: 20px; padding: 35px; margin-bottom: 50px; border: 1px solid rgba(0,217,255,0.2); }}
        .top h2 {{ color: #fff; margin-bottom: 25px; font-size: 1.6rem; }}
        .top-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px; }}
        .tc {{ background: rgba(0,0,0,0.3); border-radius: 16px; padding: 25px; border: 1px solid rgba(255,255,255,0.1); transition: all 0.3s; position: relative; overflow: hidden; }}
        .tc::before {{ content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, #00d9ff, #00ff88); }}
        .tc:hover {{ transform: translateY(-8px); box-shadow: 0 20px 40px rgba(0,217,255,0.15); }}
        .tc .r {{ font-size: 2.5rem; margin-bottom: 12px; }}
        .tc .n {{ font-weight: 700; color: #fff; font-size: 1.1rem; margin-bottom: 8px; }}
        .tc .s {{ color: #00ff88; font-size: 1.4rem; font-weight: bold; margin-bottom: 10px; }}
        .tc .re {{ color: #999; font-size: 0.85rem; line-height: 1.5; }}
        .sec h2 {{ color: #fff; font-size: 1.6rem; margin-bottom: 30px; padding-left: 15px; border-left: 4px solid #00ff88; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(380px, 1fr)); gap: 25px; }}
        .card {{ background: rgba(255,255,255,0.02); border-radius: 20px; padding: 25px; border: 1px solid rgba(255,255,255,0.06); transition: all 0.3s; }}
        .card:hover {{ background: rgba(255,255,255,0.04); border-color: rgba(0,217,255,0.2); transform: translateY(-5px); }}
        .card.dp {{ border-color: rgba(0,255,136,0.3); background: rgba(0,255,136,0.02); }}
        .hd {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 15px; }}
        .num {{ background: linear-gradient(135deg, #00d9ff, #00ff88); color: #0a0a0f; width: 36px; height: 36px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: 800; }}
        .sc {{ background: rgba(0,255,136,0.15); color: #00ff88; padding: 5px 14px; border-radius: 20px; font-weight: bold; }}
        .ti {{ font-size: 1.25rem; color: #fff; margin-bottom: 10px; font-weight: 700; }}
        .ds {{ color: #aaa; margin-bottom: 15px; font-size: 0.9rem; line-height: 1.6; }}
        .tags {{ display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 15px; }}
        .tag {{ padding: 5px 12px; border-radius: 8px; font-size: 0.75rem; }}
        .tag.u {{ background: rgba(0,217,255,0.15); color: #00d9ff; }}
        .tag.pr {{ background: rgba(0,255,136,0.15); color: #00ff88; }}
        .tag.dp {{ background: linear-gradient(90deg, rgba(0,255,136,0.2), rgba(0,217,255,0.2)); color: #00ff88; border: 1px solid rgba(0,255,136,0.3); }}
        .an {{ background: rgba(0,0,0,0.2); border-radius: 14px; padding: 15px; margin-bottom: 15px; }}
        .an-ti {{ color: #888; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px; }}
        .bars {{ display: grid; gap: 8px; }}
        .bar {{ display: grid; grid-template-columns: 80px 1fr 30px; align-items: center; gap: 8px; }}
        .bar .l {{ font-size: 0.75rem; color: #aaa; }}
        .bar .bg {{ height: 6px; background: rgba(255,255,255,0.1); border-radius: 3px; overflow: hidden; }}
        .bar .f {{ height: 100%; border-radius: 3px; }}
        .bar .f.m {{ background: linear-gradient(90deg, #00ff88, #00cc6a); }}
        .bar .f.t {{ background: linear-gradient(90deg, #00d9ff, #0099cc); }}
        .bar .f.p {{ background: linear-gradient(90deg, #ffd700, #ffaa00); }}
        .bar .f.c {{ background: linear-gradient(90deg, #ff6b6b, #ff4444); }}
        .bar .f.g {{ background: linear-gradient(90deg, #a855f7, #8b5cf6); }}
        .bar .v {{ font-size: 0.8rem; color: #fff; font-weight: 600; text-align: right; }}
        .dg {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 12px; }}
        .db {{ background: rgba(255,255,255,0.03); border-radius: 10px; padding: 10px; }}
        .db h4 {{ color: #00d9ff; font-size: 0.75rem; margin-bottom: 5px; }}
        .db p {{ color: #999; font-size: 0.8rem; line-height: 1.4; }}
        .rec {{ background: linear-gradient(135deg, rgba(0,255,136,0.1) 0%, rgba(0,217,255,0.05) 100%); padding: 12px; border-radius: 10px; border-left: 3px solid #00ff88; margin-bottom: 10px; }}
        .rec h4 {{ color: #00ff88; font-size: 0.8rem; margin-bottom: 5px; }}
        .rec p {{ color: #ccc; font-size: 0.85rem; line-height: 1.5; }}
        .mvp {{ background: rgba(168,85,247,0.1); padding: 10px; border-radius: 10px; border: 1px solid rgba(168,85,247,0.2); margin-bottom: 10px; }}
        .mvp h4 {{ color: #a855f7; font-size: 0.75rem; margin-bottom: 4px; }}
        .mvp p {{ color: #aaa; font-size: 0.8rem; }}
        .dep {{ background: linear-gradient(90deg, rgba(0,255,136,0.1), rgba(0,217,255,0.1)); padding: 10px; border-radius: 10px; border: 1px dashed rgba(0,255,136,0.3); margin-bottom: 10px; }}
        .dep h4 {{ color: #00ff88; font-size: 0.75rem; margin-bottom: 4px; }}
        .dep p {{ color: #aaa; font-size: 0.8rem; }}
        .src {{ margin-top: 10px; padding-top: 10px; border-top: 1px solid rgba(255,255,255,0.05); }}
        .src a {{ color: #666; font-size: 0.7rem; text-decoration: none; }}
        .src a:hover {{ color: #00d9ff; }}
        footer {{ text-align: center; padding: 50px 0; margin-top: 60px; border-top: 1px solid rgba(255,255,255,0.1); color: #666; }}
        footer a {{ color: #00d9ff; text-decoration: none; }}
        @media (max-width: 768px) {{ h1 {{ font-size: 2rem; }} .grid {{ grid-template-columns: 1fr; }} .dg {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>
<div class="container">
<header>
<h1>🚀 创意广场</h1>
<p class="subtitle">Reddit精选产品创意 · 深度分析 · 每日更新</p>
<p class="date">📅 2026-02-10 · 周二 · 收录10个创意 · 🔥 优先展示可部署项目</p>
<div class="nav-links" style="margin-top: 20px;">
<a href="/" style="color: #fff; text-decoration: none; margin: 0 10px; padding: 6px 14px; border: 1px solid rgba(255,255,255,0.3); border-radius: 20px; font-size: 0.85rem;">🏠 广场中心</a>
<a href="/all-ideas.html" style="color: #00ff88; text-decoration: none; margin: 0 15px; padding: 8px 16px; border: 1px solid rgba(0,255,136,0.3); border-radius: 20px; font-size: 0.9rem;">📚 全部专业创意</a>
<a href="/archive/ideas/" style="color: #00d9ff; text-decoration: none; margin: 0 15px; padding: 8px 16px; border: 1px solid rgba(0,217,255,0.3); border-radius: 20px; font-size: 0.9rem;">🗂️ 专业创意归档</a>
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
<p style="margin-top:15px;font-size:0.85rem;color:#888;"><span class="badge d">⚡ 可直接部署</span> 标记的项目可直接部署到 Vercel/Cloudflare，无需后端</p>
</div>

<section class="top">
<h2>🏆 今日 Top 5</h2>
<div class="top-grid">
{chr(10).join(top5)}
</div>
</section>

<section class="sec">
<h2>📋 完整创意分析（10个）</h2>
<div class="grid">
{chr(10).join(cards)}
</div>
</section>

<footer>
<p>💡 创意广场 · 每日更新 · 数据来源 Reddit</p>
<p style="margin-top:10px;">⚡ 可直接部署 = 纯前端/静态站点，可部署到 Vercel/Cloudflare Pages</p>
</footer>
</div>
</body>
</html>'''

with open('/home/clawdbot/workspace/idea-plaza/ideas.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Generated ideas.html with {{len(html)}} bytes")