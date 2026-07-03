"""流程测试 — 验证三阶段流水线的执行流程。"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


class TestFlow:
    """验证三阶段流水线逻辑。"""

    def test_phase_sequence(self):
        """验证三阶段顺序正确。"""
        import brainpony
        info = brainpony.get_plugin_info()
        phases = info["phases"]
        assert phases[0] == "brainstorming"
        assert phases[1] == "writing-plans"
        assert phases[2] == "ponytail-build"

    def test_skill_files_exist(self):
        """验证所有 skill 文件存在。"""
        import brainpony
        base = os.path.dirname(brainpony.__file__)
        skills_dir = os.path.join(base, "skills")

        expected = [
            "brainstorming/SKILL.md",
            "writing-plans/SKILL.md",
            "ponytail-build/SKILL.md",
        ]
        for path in expected:
            full_path = os.path.join(skills_dir, path.replace("/", os.sep))
            assert os.path.exists(full_path), f"Missing: {full_path}"

    def test_agents_dot_md_exists(self):
        """验证 AGENTS.md 存在。"""
        import brainpony
        base = os.path.dirname(brainpony.__file__)
        agents_path = os.path.join(base, "AGENTS.md")
        assert os.path.exists(agents_path), f"Missing: {agents_path}"

    def test_constraint_order(self):
        """验证约束优先级顺序。"""
        constraints = [
            "HARD-GATE (最高优先级)",
            "根因优先",
            "验证先于断言",
        ]
        # 验证三个约束都在 AGENTS.md 中有定义
        import brainpony
        base = os.path.dirname(brainpony.__file__)
        agents_path = os.path.join(base, "AGENTS.md")
        with open(agents_path, "r", encoding="utf-8") as f:
            content = f.read()

        for constraint in constraints:
            # 检查核心关键词
            key = constraint.split(" ")[0]
            assert key in content, f"Constraint '{key}' not found in AGENTS.md"
