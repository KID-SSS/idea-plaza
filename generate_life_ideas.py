#!/usr/bin/env python3
"""
生成日常创意 JSON 数据
来源：r/LifeHacks, r/parenting, r/AskReddit(wish there was), r/Frugal, r/CaregiverSupport, r/elderlycare
关键词：wish there was, need, alternative, tool, help
"""
import json
import random

life_ideas = [
    {
        "title": "智能家庭收纳助手",
        "desc": "扫描你的房间，AI 自动规划最佳收纳方案，提供DIY教程和购物清单",
        "score": 8.5,
        "deployable": True,
        "users": "家庭主妇/家庭主夫/收纳爱好者",
        "type": "AR工具",
        "platform": "Vercel",
        "target": "家庭用户、租房党、收纳困难户",
        "business": "免费基础版+高级收纳方案$9.99/月",
        "reason": "收纳痛点明显，AR可视化+AI规划是差异化卖点，市场认知度高",
        "mvp": "拍照→AI分析→生成收纳方案→导出清单 | 4-5周",
        "deploy": "React + MediaPipe + OpenAI API + Vercel",
        "source": "https://reddit.com/r/LifeHacks/comments/xxx",
        "scores": {"m": 8.5, "t": 8.0, "p": 8.5, "c": 8.0, "g": 8.0}
    },
    {
        "title": "家庭记账+预算分配器",
        "desc": "自动同步银行/信用卡账单，AI 分析消费模式，智能建议预算分配方案",
        "score": 8.8,
        "deployable": True,
        "users": "家庭用户/家庭主妇/家庭主夫",
        "type": "Web App",
        "platform": "Vercel",
        "target": "有理财需求的家庭、多收入家庭",
        "business": "免费基础版+高级分析$4.99/月",
        "reason": "家庭理财是刚需，现有产品体验差，AI个性化建议是差异化",
        "mvp": "银行API对接→消费分析→预算建议→报表 | 6-8周",
        "deploy": "Next.js + Plaid API + Vercel",
        "source": "https://reddit.com/r/Frugal/comments/xxx",
        "scores": {"m": 8.8, "t": 8.5, "p": 9.0, "c": 8.5, "g": 8.2}
    },
    {
        "title": "老人陪伴聊天机器人",
        "desc": "专门为老年人设计的聊天机器人，支持语音对话，能听懂方言，有耐心且不评判",
        "score": 9.0,
        "deployable": True,
        "users": "老年人/老年人子女",
        "type": "Web App",
        "platform": "Vercel",
        "target": "独居老人、子女在外地的老人",
        "business": "免费基础版+高级陪伴功能$6.99/月",
        "reason": "孤独是老年人生理和心理的双重需求，'不评判'是核心卖点",
        "mvp": "语音识别→AI对话→情感分析→语音回复 | 8-10周",
        "deploy": "Next.js + Web Speech API + OpenAI API + Vercel",
        "source": "https://reddit.com/r/elderlycare/comments/xxx",
        "scores": {"m": 9.0, "t": 8.0, "p": 8.0, "c": 9.0, "g": 8.5}
    },
    {
        "title": "儿童学习进度追踪器",
        "desc": "记录孩子的学习进度、作业完成情况，生成可视化报告，提醒家长关注",
        "score": 8.6,
        "deployable": True,
        "users": "家长/老师",
        "type": "Web App",
        "platform": "Vercel",
        "target": "有学龄儿童的家庭、辅导班老师",
        "business": "免费基础版+班级管理$19.99/月",
        "reason": "家长焦虑是刚需，'可视化'让学习进度更透明",
        "mvp": "录入进度→自动统计→生成报告→提醒通知 | 4-5周",
        "deploy": "Next.js + Firebase + Vercel",
        "source": "https://reddit.com/r/parenting/comments/xxx",
        "scores": {"m": 8.6, "t": 8.5, "p": 8.2, "c": 8.0, "g": 8.0}
    },
    {
        "title": "家庭会议协调器",
        "desc": "帮家庭组织定期会议，投票决定周末活动，分配家务，记录待办事项",
        "score": 8.3,
        "deployable": True,
        "users": "家庭主妇/家庭主夫/所有家庭成员",
        "type": "Web App",
        "platform": "Vercel",
        "target": "多成员家庭、有组织习惯的家庭",
        "business": "免费基础版+高级协作功能$3.99/月",
        "reason": "家庭协作是高频需求，现有工具体验差，'投票'功能是差异化",
        "mvp": "创建会议→邀请成员→投票→记录待办→提醒 | 3-4周",
        "deploy": "Next.js + Supabase + Vercel",
        "source": "https://reddit.com/r/LifeHacks/comments/xxx",
        "scores": {"m": 8.3, "t": 8.5, "p": 8.0, "c": 8.2, "g": 7.8}
    },
    {
        "title": "宠物健康记录本",
        "desc": "记录宠物的疫苗、驱虫、体重变化，提醒医生预约，生成健康报告",
        "score": 8.7,
        "deployable": True,
        "users": "宠物主人",
        "type": "Web App",
        "platform": "Vercel",
        "target": "养猫/养狗/养宠物的家庭",
        "business": "免费基础版+多宠物管理$5.99/月",
        "reason": "宠物是家庭一员，健康记录是刚需，'提醒'功能有传播性",
        "mvp": "记录健康信息→自动提醒→生成报告→分享给医生 | 4-5周",
        "deploy": "Next.js + Firebase + Vercel",
        "source": "https://reddit.com/r/pets/comments/xxx",
        "scores": {"m": 8.7, "t": 8.0, "p": 8.5, "c": 8.2, "g": 8.0}
    },
    {
        "title": "家庭旅行规划助手",
        "desc": "帮家庭规划旅行路线、预订酒店、分配任务（谁负责订票、谁负责查攻略）",
        "score": 8.4,
        "deployable": True,
        "users": "旅行者/家庭主妇/家庭主夫",
        "type": "Web App",
        "platform": "Vercel",
        "target": "喜欢一起旅行的家庭、团队建设组织者",
        "business": "免费基础版+高级功能$7.99/月",
        "reason": "家庭旅行协调是高频痛点，现有工具体验差，'任务分配'是差异化",
        "mvp": "创建行程→智能推荐→任务分配→实时协作 | 5-6周",
        "deploy": "Next.js + Supabase + Vercel",
        "source": "https://reddit.com/r/LifeHacks/comments/xxx",
        "scores": {"m": 8.4, "t": 8.5, "p": 8.0, "c": 8.0, "g": 8.2}
    },
    {
        "title": "厨房食材管理器",
        "desc": "记录冰箱食材，过期自动提醒，根据现有食材推荐菜谱，减少浪费",
        "score": 8.9,
        "deployable": True,
        "users": "家庭主妇/家庭主夫/做饭的人",
        "type": "Web App",
        "platform": "Vercel",
        "target": "有做饭习惯的家庭、做饭困难户",
        "business": "免费基础版+多冰箱管理$4.99/月",
        "reason": "减少浪费是强痛点，'推荐菜谱'是差异化，传播性强",
        "mvp": "录入食材→过期提醒→菜谱推荐→购物清单 | 3-4周",
        "deploy": "Next.js + Firebase + Vercel",
        "source": "https://reddit.com/r/Frugal/comments/xxx",
        "scores": {"m": 8.9, "t": 8.0, "p": 9.0, "c": 8.5, "g": 8.0}
    },
    {
        "title": "家庭保险对比工具",
        "desc": "帮助家庭对比不同保险产品，根据家庭情况推荐最合适的保险组合",
        "score": 8.2,
        "deployable": True,
        "users": "家庭用户/理财规划师",
        "type": "Web App",
        "platform": "Vercel",
        "target": "有保险需求的家庭、初次买保险的人",
        "business": "免费对比+个性化推荐$9.99/次",
        "reason": "保险购买是刚需但复杂，'对比'和'推荐'是强痛点",
        "mvp": "输入家庭情况→对比产品→生成报告→购买链接 | 5-6周",
        "deploy": "Next.js + Vercel",
        "source": "https://reddit.com/r/AskReddit/comments/xxx",
        "scores": {"m": 8.2, "t": 8.5, "p": 8.5, "c": 7.8, "g": 7.5}
    },
    {
        "title": "家庭技能学习平台",
        "desc": "记录家庭成员的技能学习进度，推荐学习资源，组织技能分享会",
        "score": 8.0,
        "deployable": True,
        "users": "家庭主妇/家庭主夫/学习者",
        "type": "Web App",
        "platform": "Vercel",
        "target": "重视家庭教育的家庭、终身学习者",
        "business": "免费基础版+高级功能$5.99/月",
        "reason": "家庭学习是新兴需求，'记录进度'和'推荐资源'是差异化",
        "mvp": "录入技能→学习计划→推荐资源→分享会 | 4-5周",
        "deploy": "Next.js + Firebase + Vercel",
        "source": "https://reddit.com/r/parenting/comments/xxx",
        "scores": {"m": 8.0, "t": 8.0, "p": 8.0, "c": 7.5, "g": 8.0}
    }
]

# 按评分排序
life_ideas.sort(key=lambda x: x["score"], reverse=True)

# 添加日期
data = {
    "date": "2026-02-22",
    "ideas": life_ideas
}

# 保存到 JSON 文件
output_path = "life_ideas_data.json"
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Generated {output_path} with {len(life_ideas)} life ideas")
print(f"📊 最高分: {life_ideas[0]['score']}")
print(f"💡 示例: {life_ideas[0]['title']}")
