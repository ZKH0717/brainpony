"""
BrainPony — 先设计，再计划，然后用最懒的方式实现。

一个 Claude Code 插件，融合了 Superpower 的头脑风暴和写计划能力，
与 Ponytail 的"懒人资深开发者"哲学。

核心流水线：
  Brainstorm (设计) → Write Plans (计划) → Ponytail Build (实现)

三大约束：
  ⛔ HARD-GATE: 不设计不写代码
  🔍 根因优先: 修 bug 先找根因
  ✅ 验证先于断言: 证据先于声明
"""

__version__ = "1.0.0"
__author__ = "BrainPony"
__description__ = "先设计，再计划，然后用最懒的方式实现"


def check_hard_gate(spec_path: str = "docs/superpowers/specs") -> bool:
    """检查 HARD-GATE：是否存在已批准的 spec 文档。

    这是一个辅助函数，帮助代理判断是否可以进入实现阶段。

    Args:
        spec_path: spec 文档的目录路径

    Returns:
        如果存在至少一个 spec 文件返回 True
    """
    import os
    from pathlib import Path

    spec_dir = Path(spec_path)
    if not spec_dir.exists():
        return False

    md_files = list(spec_dir.glob("*.md"))
    return len(md_files) > 0


def get_plugin_info() -> dict:
    """返回插件的基本信息。"""
    return {
        "name": "brainpony",
        "version": __version__,
        "author": __author__,
        "description": __description__,
        "phases": ["brainstorming", "writing-plans", "ponytail-build"],
        "constraints": ["hard-gate", "root-cause-first", "verify-before-claim"],
    }


def verify_constraints() -> list:
    """验证三大约束的完整性检查。

    Returns:
        约束检查结果列表，每项包含名称和状态
    """
    results = []

    # 检查 HARD-GATE
    spec_exists = check_hard_gate()
    results.append({
        "name": "HARD-GATE",
        "symbol": "⛔",
        "description": "不设计不写代码",
        "spec_exists": spec_exists,
        "status": "pass" if spec_exists else "no spec found"
    })

    # 根因优先和验证先于断言由 AGENTS.md 强制执行
    results.append({
        "name": "根因优先",
        "symbol": "🔍",
        "description": "修 bug 先找根因",
        "status": "enforced by AGENTS.md"
    })

    results.append({
        "name": "验证先于断言",
        "symbol": "✅",
        "description": "证据先于声明",
        "status": "enforced by AGENTS.md"
    })

    return results


# 插件初始化时输出欢迎信息
print(f"🧠🐎 BrainPony v{__version__} loaded — 先设计，再计划，然后用最懒的方式实现")
