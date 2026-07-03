#!/bin/bash
# BrainPony 初始化脚本
# 在 Claude Code 中启用 BrainPony 后运行此脚本完成初始设置

echo "🧠🐎 BrainPony 初始化..."
echo ""

# 创建 docs 目录
mkdir -p docs/superpowers/specs
mkdir -p docs/superpowers/plans

echo "✅ 已创建文档目录："
echo "   📁 docs/superpowers/specs/  — 设计文档"
echo "   📁 docs/superpowers/plans/  — 实施计划"
echo ""
echo "BrainPony 已就绪！"
echo ""
echo "使用流程："
echo "1. 提出你的需求，BrainPony 会自动启动 brainstorming"
echo "2. 确认设计后自动进入 writing-plans"
echo "3. 批准计划后自动进入 ponytail-build"
echo ""
echo "三大约束全程生效："
echo "   ⛔ HARD-GATE — 不设计不写代码"
echo "   🔍 根因优先 — 修 bug 先找根因"
echo "   ✅ 验证先于断言 — 证据先于声明"
