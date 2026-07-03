# 🧠🐎 BrainPony

**先设计，再计划，然后用最懒的方式实现。**

> 最好的代码是从未写过的代码，但在不写代码之前，你必须清楚你到底需不需要写、以及怎么写。

---

## 诞生故事

### 我的想法

我一直在用 [Superpower](https://github.com/prime-radiant-inc/superpowers) 插件，它很强——头脑风暴和写执行计划的能力一流，还有很严格的约束力（不设计不写代码、先找根因再修 bug、证据先于断言）。但我只喜欢它这两个能力和约束，其他功能（TDD、debugging、code review、git worktrees、visual companion 等等）对我来说过于繁杂，每个会话都要消耗大量 tokens。

同时我注意到了 [Ponytail](https://github.com/DietrichGebert/ponytail) 这个项目——"lazy senior dev"的哲学深得我心：最好的代码是没写的代码，要写就用最少代码解决问题。但它缺少设计前置和计划驱动的流程。

所以我决定做一个新插件：**BrainPony**。

### 怎么做的

1. **提取精华**：从 Superpower 中提取了 brainstorming（头脑风暴→设计方案）和 writing-plans（编写实施计划）两个核心能力，去掉了 visual companion 等复杂功能
2. **融入哲学**：完整嵌入了 Ponytail 的 7 条阶梯规则和 lazy senior dev 的编码哲学
3. **新增机制**：在 Build 阶段加入了**子代理审查**——每段代码写完后由独立的新代理审查，避免写代码的人自我包庇
4. **强化约束**：三大约束（HARD-GATE、根因优先、验证先于断言）贯穿全流程
5. **实现工具**：使用 Claude Code 的插件系统，Python 实现，零外部依赖

整个开发过程也是用 BrainPony 自己的方式完成的——先设计（写了完整的设计文档），再计划（写了 11 个任务的实施计划），然后用最懒的方式逐个实现。

---

## 安装

### 下载

```bash
# 方式一：直接克隆
git clone https://github.com/ZKH0717/brainpony.git
```

### 配置

#### 方式一：作为项目级插件（推荐）

在你的项目根目录创建或编辑 `.claude/settings.local.json`：

```json
{
  "projectPlugins": {
    "brainpony": "path/to/brainpony"
  }
}
```

#### 方式二：全局启用

编辑 `~/.claude/settings.json`，在 `enabledPlugins` 中添加：

```json
{
  "enabledPlugins": {
    "brainpony": true
  }
}
```

### 初始化

```bash
cd your-project
bash path/to/brainpony/scripts/init.sh
```

这会在你的项目中创建 `docs/superpowers/specs/` 和 `docs/superpowers/plans/` 目录，用于存放设计和计划文档。

---

## 使用方式

BrainPony 在后台自动工作。你只需要像平常一样提需求：

```
> 帮我给这个应用添加用户登录功能
```

它会自动启动**三阶段流水线**：

### 阶段 1：设计 (Brainstorming)

代理先了解项目上下文，通过提问理解你的需求，提出 2-3 种方案并给出推荐。逐节确认设计后，编写 spec 文档。

**⛔ HARD-GATE**：在你批准设计之前，不会写任何代码。

### 阶段 2：计划 (Writing Plans)

基于已批准的设计，编写细粒度的实施计划。每个任务 2-5 分钟，包含完整的代码和测试用例。每个步骤都有明确的命令和预期输出。

### 阶段 3：实现 (Ponytail Build)

用"懒人资深开发者"的方式逐个完成任务：
1. 写测试（预期失败）
2. 写最小代码实现（遵循 7 条阶梯）
3. 运行测试（预期通过）
4. 根因检查（失败则先找根因）
5. **子代理审查**（新代理审查代码）
6. 验证完成

---

## 三大约束（始终生效）

| 约束 | 符号 | 说明 |
|------|------|------|
| HARD-GATE | ⛔ | 不设计不写代码 |
| 根因优先 | 🔍 | 修 bug 先找根因，不允许表面修复 |
| 验证先于断言 | ✅ | 声称完成前必须有可验证的证据 |

---

## 工作流示意图

```
你提出需求
    │
    ▼
┌─────────────────┐
│  Phase 1        │
│  Brainstorm     │──→ 输出: spec.md
│  (设计)          │    ⛔ 用户批准后才可进入下一步
└─────────────────┘
    │
    ▼
┌─────────────────┐
│  Phase 2        │
│  Write Plans    │──→ 输出: plan.md
│  (计划)          │
└─────────────────┘
    │
    ▼
┌──────────────────────────────┐
│  Phase 3                     │
│  Ponytail Build              │
│  (实现)                      │
│                              │
│  1. 按计划实现代码           │
│  2. 测试先行 (TDD)           │
│  3. 根因修复                 │
│  4. 子代理审查 ← 新增        │
│  5. 验证完成                 │
└──────────────────────────────┘
    │
    ▼
    ✅ 可工作的代码
```

---

## 能力对比

### 与 Superpower

| 能力 | Superpower | BrainPony |
|------|-----------|-----------|
| Brainstorming | ✅ 完整（含 visual companion） | ✅ 核心 |
| Writing Plans | ✅ 完整 | ✅ 核心 |
| TDD | ✅ 独立 skill | ✅ Build 中实践 |
| Code Review | ✅ 完整 review 流程 | ✅ 子代理审查 |
| Debugging | ✅ 完整 skill | ✅ 根因优先约束 |
| Git Worktrees | ✅ | ❌ 未包含 |
| Parallel Agents | ✅ | ❌ 未包含 |
| Visual Companion | ✅ 浏览器展示 | ❌ 未包含 |

### 与 Ponytail

| 能力 | Ponytail | BrainPony |
|------|----------|-----------|
| Lazy dev 7 阶梯 | ✅ | ✅ 完整嵌入 |
| 根因修复 | ✅ | ✅ 强化为约束 |
| 最小 diff | ✅ | ✅ |
| 验证规则 | ✅ | ✅ 强化为约束 |
| 设计前置 | ❌ | ✅ HARD-GATE |
| 计划前置 | ❌ | ✅ Writing Plans |
| 子代理审查 | ❌ | ✅ 新增 |

---

## 文件结构

```
brainpony/
├── AGENTS.md                # 核心指令（三阶段 + 三约束）
├── __init__.py              # Python 入口（含约束检查函数）
├── package.json             # 插件元数据
├── plugin.yaml              # 插件声明
├── README.md                # 本文件
├── LICENSE                  # MIT
├── .gitignore
│
├── skills/
│   ├── brainstorming/
│   │   └── SKILL.md         # 头脑风暴 → 设计技能
│   ├── writing-plans/
│   │   └── SKILL.md         # 写实施计划技能
│   └── ponytail-build/
│       └── SKILL.md         # 懒人执行 + 子代理审查技能
│
├── commands/
│   └── __init__.py          # slash 命令占位
├── scripts/
│   └── init.sh              # 初始化脚本
├── examples/
│   └── hello-brainpony/     # 示例项目
└── tests/
    ├── test_imports.py      # 导入测试（5 个）
    └── test_flow.py         # 流程测试（4 个）
```

---

## 许可证

MIT License — 随意使用、修改、分发。
