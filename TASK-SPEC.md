# 创意广场 - 每日任务规范

## ⏰ 定时任务

| 任务 | 时间 | Cron ID |
|------|------|---------|
| 每日创意 | 08:00 | 5bc4a2ed-8e75-4444-9d8f-8ad763517783 |
| 每日需求 | 08:30 | 37e55e79-0477-42b3-b90b-cfd532eb28e2 |

## 📋 执行清单（必须严格执行）

### 每日创意任务 (08:00)

1. **归档昨日数据**
   - 备份当前 ideas.html 到 `archive/ideas/YYYY-MM-DD.html`

2. **抓取 Reddit 创意**
   - 使用 Serper API 搜索 Reddit 创意帖子
   - 来源：r/SaaS, r/SideProject, r/AppIdeas, r/Entrepreneur

3. **AI 深度分析**（重要！不能偷懒）
   - 每个创意必须包含：
     - ✅ 五维评分条形图（市场需求/技术可行/变现潜力/竞争优势/增长潜力）
     - ✅ 目标用户
     - ✅ 商业模式
     - ✅ 推荐理由
     - ✅ MVP 时间估算
     - ✅ 部署方案（如果是可部署项目）
     - ✅ 来源链接
   - 参考模板：`archive/ideas/2026-02-09.html`

4. **更新文件**
   - ideas.html（今日创意）
   - all-ideas.html（累计表格）

5. **同步首页统计**
   ```bash
   cd /home/clawdbot/workspace/idea-plaza
   python3 update-stats.py
   ```

6. **部署到 Vercel**
   ```bash
   source /home/clawdbot/workspace/.env.vercel
   vercel --prod --yes --token $VERCEL_TOKEN
   ```

7. **通知 BOSS**
   - 发送 QQ 消息，包含：今日数量、累计数量、Top 3、链接

### 每日需求任务 (08:30)

流程同上，文件改为 demands.html / all-demands.html

## ⚠️ 注意事项

- **不要简化分析**：每个创意/需求都要有完整的分析模块
- **不走 GitHub**：直接用 Vercel CLI 部署（GitHub 网络不稳定）
- **必须同步首页**：每次更新后运行 update-stats.py
- **消息必须发送**：任务完成后通知 BOSS

## 📁 文件结构

```
idea-plaza/
├── index.html          # 首页（统计数字需同步）
├── ideas.html          # 今日创意
├── demands.html        # 今日需求
├── all-ideas.html      # 累计创意
├── all-demands.html    # 累计需求
├── update-stats.py     # 首页统计同步脚本
├── TASK-SPEC.md        # 本文件
└── archive/
    ├── ideas/          # 创意归档
    └── demands/        # 需求归档
```

## 🔑 凭证位置

- Vercel Token: `/home/clawdbot/workspace/.env.vercel`
- Serper API Key: `/home/clawdbot/workspace/.env.serper`

---

*最后更新：2026-02-10*
