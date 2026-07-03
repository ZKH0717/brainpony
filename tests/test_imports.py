"""基础导入测试。"""

import sys
import os

# 将项目根目录加入 path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


class TestImports:
    """验证所有模块可正常导入。"""

    def test_import_brainpony(self):
        """验证 brainpony 包可导入。"""
        import brainpony
        assert brainpony.__version__ == "1.0.0"
        assert brainpony.__description__ is not None

    def test_get_plugin_info(self):
        """验证 get_plugin_info 返回正确结构。"""
        import brainpony
        info = brainpony.get_plugin_info()
        assert info["name"] == "brainpony"
        assert "phases" in info
        assert len(info["phases"]) == 3
        assert "constraints" in info
        assert len(info["constraints"]) == 3

    def test_verify_constraints(self):
        """验证约束检查函数返回正确结构。"""
        import brainpony
        results = brainpony.verify_constraints()
        assert len(results) == 3
        # HARD-GATE 检查
        assert results[0]["name"] == "HARD-GATE"
        assert results[0]["symbol"] == "⛔"

    def test_check_hard_gate(self):
        """验证 HARD-GATE 检查函数。"""
        import brainpony
        from pathlib import Path

        # 无 spec 目录时返回 False
        result = brainpony.check_hard_gate("/tmp/nonexistent_path_xyz")
        assert result is False

    def test_commands_package(self):
        """验证 commands 包可导入。"""
        import brainpony.commands
        assert brainpony.commands.__doc__ is not None
