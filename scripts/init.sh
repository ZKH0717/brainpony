#!/bin/bash
# BrainPony 初始化脚本
# 注册到 Claude Code 并创建必要的文档目录
#
# 用法:
#   bash init.sh                    # 仅创建文档目录
#   bash init.sh --install          # 完整安装（注册到 Claude Code 设置）
#   bash init.sh --install --force  # 强制安装（覆盖已有设置）

set -e

echo "🧠🐎 BrainPony 初始化..."
echo ""

BRAINPONY_DIR="$(cd "$(dirname "$0")/.." && pwd -P)"
CLAUD_CONFIG="$HOME/.claude/settings.json"
MODE="${1:-}"
FORCE="${2:-}"

# 创建文档目录
mkdir -p docs/superpowers/specs
mkdir -p docs/superpowers/plans
echo "✅ 已创建文档目录："
echo "   📁 docs/superpowers/specs/  — 设计文档"
echo "   📁 docs/superpowers/plans/  — 实施计划"

# 注册到 Claude Code 设置
if [ "$MODE" = "--install" ] || [ "$MODE" = "--force" ]; then
    echo ""
    echo "🔧 注册 BrainPony 到 Claude Code..."

    # 使用 Python 修改 settings.json（比 bash 更安全）
    python3 << PYEOF
import json, os

config_path = os.path.expanduser("$CLAUD_CONFIG")
brainpony_path = "$BRAINPONY_DIR".replace("\\", "\\\\")
force = "$FORCE" == "--force"

# 读取或创建设置文件
if os.path.exists(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        settings = json.load(f)
else:
    settings = {}

changed = False

# 确保 extraKnownMarketplaces 存在
if "extraKnownMarketplaces" not in settings:
    settings["extraKnownMarketplaces"] = {}
    changed = True

# 添加 brainpony 本地 marketplace
brainpony_key = "brainpony-marketplace"
if brainpony_key not in settings["extraKnownMarketplaces"] or force:
    settings["extraKnownMarketplaces"][brainpony_key] = {
        "source": {
            "source": "directory",
            "path": brainpony_path
        }
    }
    print("   ✅ 已添加 brainpony-marketplace")
    changed = True
else:
    print("   ⏭️  brainpony-marketplace 已存在（使用 --force 覆盖）")

# 确保 enabledPlugins 存在
if "enabledPlugins" not in settings:
    settings["enabledPlugins"] = {}
    changed = True

# 启用 brainpony
brainpony_plugin = "brainpony@brainpony-marketplace"
if settings["enabledPlugins"].get(brainpony_plugin) != True or force:
    settings["enabledPlugins"][brainpony_plugin] = True
    print("   ✅ 已启用 brainpony@brainpony-marketplace")
    changed = True
else:
    print("   ⏭️  brainpony 已启用")

# 禁用 superpower（可选）
superpower_plugin = "superpowers@superpowers-marketplace"
if superpower_plugin in settings.get("enabledPlugins", {}):
    if settings["enabledPlugins"][superpower_plugin] != False:
        settings["enabledPlugins"][superpower_plugin] = False
        print("   ✅ 已禁用 superpowers（BrainPony 已替代）")
        changed = True

if changed:
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=2, ensure_ascii=False)
    print("   ✅ 设置已保存到: $CLAUD_CONFIG")
else:
    print("   ⏭️  无需修改")

PYEOF
fi

echo ""
echo "🧠🐎 BrainPony 已就绪！"
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
echo ""
echo "📖 在项目中使用时，运行:"
echo "   bash $(dirname "$0")/init.sh"
