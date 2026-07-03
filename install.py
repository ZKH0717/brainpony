#!/usr/bin/env python3
"""BrainPony 一键安装脚本

用法:
    python install.py

自动完成:
    1. 将 BrainPony 安装到 ~/.claude/plugins/cache/brainpony-marketplace/brainpony/1.0.0/
    2. 注册到 Claude Code 设置中
    3. 启用 brainpony
"""

import json
import os
import shutil
import sys
from pathlib import Path

# Windows GBK 编码兼容
if sys.platform == "win32" and sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def main():
    # 路径
    script_dir = Path(__file__).parent.resolve()
    claude_dir = Path.home() / ".claude"
    plugin_dir = claude_dir / "plugins" / "cache" / "brainpony-marketplace" / "brainpony" / "1.0.0"
    settings_path = claude_dir / "settings.json"

    print("🧠🐎 安装 BrainPony...")

    # 1. 复制文件到插件目录
    print(f"   📦 复制到 {plugin_dir}")
    if plugin_dir.exists():
        shutil.rmtree(plugin_dir)
    plugin_dir.parent.mkdir(parents=True, exist_ok=True)

    # 排除不需要的文件
    ignore_list = {".git", "__pycache__", ".pytest_cache", "*.pyc"}

    def ignore_func(src, names):
        return {n for n in names if n in ignore_list or n.endswith(".pyc")}

    shutil.copytree(script_dir, plugin_dir, ignore=ignore_func,
                    dirs_exist_ok=True)

    # 2. 更新 settings.json
    settings = {}
    if settings_path.exists():
        with open(settings_path, "r", encoding="utf-8") as f:
            settings = json.load(f)

    changed = False

    # 添加 marketplace
    settings.setdefault("extraKnownMarketplaces", {})
    marketplace_key = "brainpony-marketplace"
    marketplace_path = str(plugin_dir.parent.parent).replace("\\", "\\\\")

    if marketplace_key not in settings["extraKnownMarketplaces"]:
        settings["extraKnownMarketplaces"][marketplace_key] = {
            "source": {
                "source": "directory",
                "path": str(plugin_dir.parent.parent)
            }
        }
        changed = True

    # 启用插件
    settings.setdefault("enabledPlugins", {})
    plugin_id = "brainpony@brainpony-marketplace"
    if settings["enabledPlugins"].get(plugin_id) is not True:
        settings["enabledPlugins"][plugin_id] = True
        changed = True

    # 禁用 superpower
    superpower_id = "superpowers@superpowers-marketplace"
    if superpower_id in settings.get("enabledPlugins", {}):
        if settings["enabledPlugins"].get(superpower_id) is not False:
            settings["enabledPlugins"][superpower_id] = False
            changed = True

    if changed:
        with open(settings_path, "w", encoding="utf-8") as f:
            json.dump(settings, f, indent=2, ensure_ascii=False)
        print("   ✅ 已注册到 Claude Code")

    print()
    print("   ✅ BrainPony 安装完成！")
    print()
    print("   下次启动 Claude Code 即可使用。")
    print("   提出需求时会自动触发 brainstorming 流程。")


if __name__ == "__main__":
    main()
