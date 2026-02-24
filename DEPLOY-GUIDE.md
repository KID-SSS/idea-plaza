# 广场中心（idea-plaza）完整部署文档

> 一份文档复刻整个项目。复制到新设备后按步骤执行即可。

---

## 一、项目概览

**线上地址：** https://idea-plaza.vercel.app

**功能：** 每天自动从 Reddit 抓取创意和需求，分析评分后生成网页，部署到 Vercel。

**4 个广场模块：**

| 模块 | 页面 | 定位 | 数据来源 |
|------|------|------|----------|
| 🚀 专业创意广场 | ideas.html | SaaS/技术/产品创意 | r/Entrepreneur, r/SideProject, r/SaaS |
| 🎯 专业需求广场 | demands.html | B端/开发者真实痛点 | r/SomebodyMakeThis, r/AppIdeas, r/smallbusiness |
| 💡 日常创意广场 | life-ideas.html | 普通人生活创意 | r/LifeHacks, r/Parenting, r/AskReddit |
| 🏠 日常需求广场 | life-demands.html | 普通人日常痛点 | r/LifeHacks, r/Frugal, r/AgingParents |

---

## 二、项目结构

```
idea-plaza/
├── index.html                  # 广场中心首页（4宫格入口）
├── ideas.html                  # 今日专业创意
├── demands.html                # 今日专业需求
├── life-ideas.html             # 今日日常创意
├── life-demands.html           # 今日日常需求
├── all-ideas.html              # 累计专业创意
├── all-demands.html            # 累计专业需求
├── all-life-ideas.html         # 累计日常创意
├── all-life-demands.html       # 累计日常需求
├── build_ideas.py              # 专业创意+日常创意 HTML 生成器（双模式）
├── build_demands.py            # 专业需求 HTML 生成器
├── build_life_demands.py       # 日常需求 HTML 生成器
├── update-stats.py             # 首页统计数字更新脚本
├── vercel.json                 # Vercel 部署配置
├── ideas_data.json             # 今日专业创意数据（AI 生成）
├── demands_data.json           # 今日专业需求数据（AI 生成）
├── life_ideas_data.json        # 今日日常创意数据（AI 生成）
├── life_demands_data.json      # 今日日常需求数据（AI 生成）
├── all_ideas_data.json         # 累计专业创意 JSON 数据库
├── all_demands_data.json       # 累计专业需求 JSON 数据库
├── all_life_ideas_data.json    # 累计日常创意 JSON 数据库
├── all_life_demands_data.json  # 累计日常需求 JSON 数据库
└── archive/                    # 每日归档
    ├── ideas/                  # 专业创意归档
    ├── demands/                # 专业需求归档
    ├── life-ideas/             # 日常创意归档
    └── life-demands/           # 日常需求归档
```

---

## 三、核心工作流（每个广场相同）

```
Serper API 搜索 Reddit
        ↓
AI 分析筛选 10-15 条
        ↓
写入 JSON 数据文件（xxx_data.json）
        ↓
Python 脚本生成 HTML（build_xxx.py）
  - 生成今日页面（xxx.html）
  - 追加到累计页面（all-xxx.html，自动去重）
        ↓
update-stats.py 更新首页统计数字
        ↓
vercel --prod --yes 部署
        ↓
通知 BOSS（QQBot）
```

---

## 四、构建脚本用法

### 专业创意（双模式）
```bash
# 专业创意（默认）
python3 build_ideas.py ideas_data.json

# 日常创意
python3 build_ideas.py life_ideas_data.json life
```

### 专业需求
```bash
python3 build_demands.py demands_data.json
```

### 日常需求
```bash
python3 build_life_demands.py life_demands_data.json
```

### 更新首页统计
```bash
python3 update-stats.py
```

---

## 五、JSON 数据格式

### 创意（专业/日常通用）
```json
{
  "date": "2026-02-22",
  "ideas": [
    {
      "title": "创意名称",
      "desc": "一句话描述",
      "score": 8.5,
      "deployable": true,
      "users": "目标用户群",
      "type": "Web工具/SaaS/PWA等",
      "platform": "Vercel/Cloudflare/null",
      "target": "详细目标用户",
      "business": "商业模式",
      "reason": "推荐理由",
      "mvp": "MVP路径 | 时间",
      "deploy": "部署方案（可选，null则不显示）",
      "source": "https://reddit.com/...",
      "scores": {"m": 8.5, "t": 9.0, "p": 8.0, "c": 8.5, "g": 8.0}
    }
  ]
}
```

### 专业需求
```json
{
  "date": "2026-02-22",
  "demands": [
    {
      "title": "需求标题",
      "desc": "需求描述",
      "form": "🌐 Web网站",
      "pain_score": 8,
      "market_score": 7,
      "difficulty": 5,
      "monetization": 8,
      "insight": "商业洞察",
      "competitors": "竞品情况",
      "source": "https://reddit.com/..."
    }
  ]
}
```

### 日常需求
```json
{
  "date": "2026-02-22",
  "life_demands": [
    {
      "title": "需求标题",
      "desc": "需求描述",
      "category": "育儿/健康/家务/出行/宠物/学习/情感/购物/老人关怀/其他",
      "pain_score": 8,
      "freq": 9,
      "audience": 7,
      "difficulty": 5,
      "form": "🌐 Web网站",
      "insight": "为什么这个需求值得做",
      "source": "https://reddit.com/..."
    }
  ]
}
```

---

## 六、依赖与环境

```bash
# 系统要求
- Python 3.8+（标准库即可，无第三方依赖）
- Node.js（用于 Vercel CLI）
- Vercel CLI: npm i -g vercel

# API Keys（需替换为你自己的）
SERPER_API_KEY=f94aa43a02ef40e2fb90120e27207a04f15042ef
VERCEL_TOKEN=s7PMWlklhbTM7vnnpPbOIXBB

# 部署命令
cd idea-plaza && VERCEL_TOKEN=你的token vercel --prod --yes
```

---

## 七、Cron 定时任务（OpenClaw）

每天自动执行 4 个任务，间隔 30 分钟避免并发：

| 任务名 | Cron 表达式 | 时间 |
|--------|------------|------|
| 专业创意广场-每日更新 | `0 8 * * *` | 每天 08:00 |
| 专业需求广场-每日更新 | `30 8 * * *` | 每天 08:30 |
| 日常创意广场-每日更新 | `0 9 * * *` | 每天 09:00 |
| 日常需求广场-每日更新 | `30 9 * * *` | 每天 09:30 |

### 每个 Cron 任务的执行步骤（7步）

1. **归档**：把昨天的页面 cp 到 `archive/xxx/YYYY-MM-DD.html`
2. **抓取**：用 Serper API 搜索 Reddit 子版块（过去24小时）
3. **分析**：AI 筛选 10-15 条，写入 JSON 数据文件
4. **生成**：运行 Python 脚本生成 HTML（今日页 + 累计页）
5. **统计**：运行 `update-stats.py` 更新首页数字
6. **部署**：`vercel --prod --yes`
7. **通知**：通过 QQBot 发送结果给 BOSS

### Cron 任务配置参数

```json
{
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "model": "claude-opus-4-6",
    "channel": "qqbot",
    "deliver": true,
    "to": "你的QQBot_openid"
  },
  "isolation": {
    "postToMainPrefix": "Cron",
    "postToMainMode": "summary",
    "postToMainMaxChars": 8000
  }
}
```

---

## 八、Reddit 数据源

### 专业创意
- `r/Entrepreneur` — idea OR project OR startup
- `r/SideProject` — 全部
- `r/SaaS` — idea OR built

### 专业需求
- `r/SomebodyMakeThis` — 全部
- `r/AppIdeas` — 全部
- `r/Entrepreneur` — "looking for" OR "need" OR "wish there was"
- `r/smallbusiness` — "struggling with" OR "anyone know a tool"

### 日常创意
- `r/LifeHacks` — tool OR app OR wish
- `r/Parenting` — app OR tool OR help OR struggling
- `r/AskReddit` — "wish there was" OR "why isn't there"
- `r/mildlyinfuriating` — app OR tool OR fix
- `r/AgingParents` + `r/CaregiverSupport` — tool OR app

### 日常需求
- `r/LifeHacks` — "wish" OR "need" OR "looking for"
- `r/Parenting` — "struggling" OR "help" OR "need a tool"
- `r/Frugal` — "looking for" OR "alternative" OR "cheaper"
- `r/AgingParents` + `r/CaregiverSupport` — "need" OR "help" OR "tool"
- `r/mildlyinfuriating` — "why" OR "annoying" OR "fix"

---

## 九、从零复刻步骤

### 1. 克隆项目
```bash
git clone <你的仓库地址> idea-plaza
cd idea-plaza
```

### 2. 配置 Vercel
```bash
npm i -g vercel
vercel login
vercel link  # 关联项目
```

### 3. 配置 API Keys
替换以下两个 key：
- `SERPER_API_KEY` — 在 https://serper.dev 注册获取
- `VERCEL_TOKEN` — 在 Vercel 后台 Settings → Tokens 创建

### 4. 首次部署
```bash
VERCEL_TOKEN=你的token vercel --prod --yes
```

### 5. 配置 OpenClaw Cron 任务
在 OpenClaw 中创建 4 个 cron 任务（参考第七节的配置），注意替换：
- `SERPER_API_KEY` 为你的 key
- `VERCEL_TOKEN` 为你的 token
- `to` 为你的 QQBot openid
- 项目路径 `/home/clawdbot/workspace/idea-plaza` 改为你的实际路径

### 6. 验证
访问 https://你的域名.vercel.app 确认 4 个广场正常显示。

---

## 十、注意事项

1. **Serper API 免费额度**：每月 2500 次搜索，4 个任务每天约 20 次，一个月约 600 次，够用
2. **Vercel 免费额度**：每月 100 次部署，每天 4 次约 120 次/月，接近上限，可考虑合并部署
3. **去重逻辑**：累计页面（all-xxx.html）通过标题去重，不会重复添加
4. **归档**：每天自动把前一天的页面存入 archive 目录
5. **首页统计**：update-stats.py 通过正则匹配更新首页数字，修改首页 HTML 结构时注意保持 stat-label 文本一致
